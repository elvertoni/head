#!/usr/bin/env python3
"""Triagem das aulas RCO extraidas (lake/**/rco/) com o Jev (TypeSafe).

Para cada aula RCO, uma unica chamada ao Jev responde tres perguntas sobre o
mesmo `state` (titulo + objetivos + conteudo dos slides, sem o boilerplate SEED):

- `aula_aprovada` (choice): qual aula aprovada da mesma disciplina, segundo o
  manifesto.json, ja ensina o mesmo conteudo central — ou `nenhuma`;
- `natureza` (choice): conceitual, pratica, projeto ou revisao-avaliacao;
- `densidade` (score): quanta materia tecnica nova a aula traz.

O codigo so le e resume: nao altera lake/, aulas/ nem conceitos/. Respostas ficam
em cache (scratch/jev-rco/, pela hash do pedido), entao rodar de novo nao cobra
o que ja foi perguntado. Saida: docs/rco-triagem.md.

Uso:
    python tools/triar_rco.py --disciplina analise-e-metodos-para-sistemas
    python tools/triar_rco.py              # todas
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import unicodedata
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.gerar_manifesto import LABELS_DISCIPLINA, LABELS_TRILHA  # noqa: E402
from tools.jev import choice, score, system_one  # noqa: E402
from tools.wiki_core import as_list, parse_frontmatter  # noqa: E402

CACHE = ROOT / "scratch" / "jev-rco"
SAIDA = ROOT / "docs" / "rco-triagem.md"
VERSAO_PERGUNTAS = "2"
LIMITE_CONTEUDO = 20000  # caracteres (~6k tokens), bem abaixo dos 32k do Jev; so 8000 cortava materia
CONF_REVISAR = 0.5
CONF_EQUIVALENCIA = 0.7  # no piloto AMS, equivalencias erradas vieram com 0.55-0.65

# Slides do template SEED voltados ao professor ou a matriz curricular: saem inteiros.
SLIDE_TEMPLATE = re.compile(
    r"ORGANIZA[ÇC][ÃA]O CURRICULAR|COMPET[ÊE]NCIA\(S\)|HABILIDADE\(S\)|SLIDE DO|ATEN[ÇC][ÃA]O,? PROFESSOR|"
    r"Esta aula integra conhecimentos|professor tem total autonomia|falta de conex[ãa]o|OBJETOS DO CONHECIMENTO|"
    r"^Refer[êe]ncias( bibliogr[áa]ficas)?:?$",
    re.IGNORECASE,
)
# Linhas soltas de template que aparecem no meio de slides de conteudo.
BOILERPLATE = re.compile(
    r"Google Play|App Store|aplicativo da Alura|Para um melhor aproveitamento|Plano de Curso|"
    r"Matriz Curricular|^\d[\d.]*\s*h(oras)?$|EM13[A-Z]{3}\d{3}|Acesse aqui|https?://|"
    r"^(Fonte|Imagem|Disponível em)\b|^Para pensarmos juntos\.*$",
    re.IGNORECASE,
)


@dataclass
class Aula:
    caminho: Path
    titulo: str
    disciplina: str
    trimestre: int
    ordem_rco: int
    objetivos: List[str]
    conteudo: str


def carregar(caminho: Path) -> Aula:
    texto = caminho.read_text(encoding="utf-8")
    fm = parse_frontmatter(texto).data
    slides = texto.split("## Slides", 1)[-1]
    slides = re.split(r"^## (?:Atividade|Prática|Outros documentos)\s*$", slides, maxsplit=1, flags=re.M)[0]
    objetivos: List[str] = []
    linhas: List[str] = []
    blocos = re.split(r"^### Slide \d+.*$", slides, flags=re.M)[1:]
    for bloco in blocos[1:]:  # o slide 1 e a capa; o titulo ja vem do frontmatter
        itens = []
        for l in bloco.splitlines():
            l = l.strip()
            if l.startswith("- "):
                itens.append(l[2:].strip())
            elif l.startswith("|") and not re.fullmatch(r"\|(\s*-+\s*\|)+", l):
                # linha de tabela vira "celula; celula" — tabela de slide costuma ser materia
                celulas = [c.strip() for c in re.split(r"(?<!\\)\|", l.strip("|")) if c.strip()]
                if celulas:
                    itens.append("; ".join(c.replace("\\|", "|") for c in celulas))
        if any(SLIDE_TEMPLATE.search(i) for i in itens):
            continue
        em_objetivos = False
        for item in itens:
            if not item or BOILERPLATE.search(item):
                continue
            if re.match(r"^nesta aula,? vamos", item, re.I):
                em_objetivos = True
                continue
            (objetivos if em_objetivos else linhas).append(item)
    vistos, unicas = set(), []
    for item in linhas:  # slides de transicao repetem cabecalhos
        if item.lower() not in vistos:
            vistos.add(item.lower())
            unicas.append(item)
    conteudo = "\n".join(unicas)[:LIMITE_CONTEUDO]
    return Aula(
        caminho=caminho,
        titulo=str(fm.get("titulo", caminho.stem)),
        disciplina=str(fm.get("disciplina", "")),
        trimestre=int(fm.get("trimestre", 0) or 0),
        ordem_rco=int(fm.get("ordem_rco", 0) or 0),
        objetivos=objetivos[:8],
        conteudo=conteudo,
    )


def aprovadas_por_disciplina() -> Dict[str, List[Dict[str, Any]]]:
    """Aulas do manifesto por disciplina, com os `objetivos` da canonica.

    Sem os objetivos o Jev compara o conteudo da aula RCO com um titulo solto e
    responde com confianca baixa ate para pares de titulo identico.
    """
    manifesto = json.loads((ROOT / "manifesto.json").read_text(encoding="utf-8"))
    out: Dict[str, List[Dict[str, Any]]] = {}
    for lic in manifesto.get("lessons", []):
        lic = dict(lic)
        canonica = ROOT / "aulas" / lic["disciplina"] / lic["trilha"] / f"{int(lic['ordem']):02d}-{lic['slug']}" / "canonica.md"
        objetivos: List[str] = []
        if canonica.exists():
            fm = parse_frontmatter(canonica.read_text(encoding="utf-8")).data
            objetivos = [str(o) for o in as_list(fm.get("objetivos"))]
        lic["objetivos"] = objetivos
        out.setdefault(lic["disciplina"], []).append(lic)
    return out


def normalizar_titulo(titulo: str) -> str:
    sem_acento = unicodedata.normalize("NFKD", titulo).encode("ascii", "ignore").decode("ascii")
    return re.sub(r"[^a-z0-9]+", " ", sem_acento.lower()).strip()


def mesmo_titulo(aula: "Aula", aprovadas: List[Dict[str, Any]]) -> Optional[str]:
    """Slug da unica aula aprovada com titulo identico (normalizado), se houver."""
    alvo = normalizar_titulo(aula.titulo)
    achadas = [lic["slug"] for lic in aprovadas if normalizar_titulo(lic["titulo"]) == alvo]
    return achadas[0] if len(achadas) == 1 else None


def perguntas(aprovadas: List[Dict[str, Any]]) -> Dict[str, Dict[str, Any]]:
    q: Dict[str, Dict[str, Any]] = {
        "natureza": choice(
            "Qual é o foco principal da aula descrita em `aula`?",
            {
                "conceitual": "Explicar conceitos, definições ou fundamentos técnicos novos para a turma",
                "pratica": "Executar uma ferramenta, técnica ou exercício guiado, com pouca teoria nova",
                "projeto": "Desenvolver ou avançar um projeto, produto ou entrega da própria turma",
                "revisao-avaliacao": "Revisar, retomar, nivelar ou avaliar conteúdos já vistos, sem conteúdo novo",
            },
        ),
        "densidade": score(
            "Quanta matéria técnica nova a aula descrita em `aula` ensina?",
            [
                "Nenhuma matéria técnica nova: só dinâmica, orientação, revisão ou avaliação",
                "Pouca: um ou dois termos técnicos citados de passagem, sem definição",
                "Moderada: alguns conceitos técnicos apresentados com definição ou exemplo",
                "Alta: vários conceitos técnicos novos, cada um definido e exemplificado",
            ],
        ),
    }
    if aprovadas:
        criterios: Dict[str, Any] = {
            lic["slug"]: {
                "aula_aprovada": lic["titulo"],
                "trilha": LABELS_TRILHA.get(lic["trilha"], lic["trilha"]),
                "objetivos": lic.get("objetivos", [])[:4],
            }
            for lic in sorted(aprovadas, key=lambda x: (x["trilha"], int(x["ordem"])))
        }
        criterios["nenhuma"] = "Nenhuma das aulas aprovadas listadas ensina o mesmo conteúdo central da aula em `aula`"
        q["aula_aprovada"] = choice(
            "Qual aula aprovada do acervo já ensina o mesmo conteúdo central da aula descrita em `aula`? "
            "Tema apenas vizinho ou só mencionado de passagem não conta: escolha `nenhuma`.",
            criterios,
        )
    return q


def _chave(state: Dict[str, Any], q: Dict[str, Any]) -> str:
    bruto = json.dumps([VERSAO_PERGUNTAS, state, q], ensure_ascii=False, sort_keys=True)
    return hashlib.sha1(bruto.encode("utf-8")).hexdigest()


def julgar(aula: Aula, aprovadas: List[Dict[str, Any]]) -> Dict[str, Any]:
    state = {
        "aula": {
            "disciplina": LABELS_DISCIPLINA.get(aula.disciplina, aula.disciplina),
            "titulo": aula.titulo,
            "objetivos": aula.objetivos,
            "conteudo_dos_slides": aula.conteudo,
        }
    }
    q = perguntas(aprovadas)
    arq = CACHE / f"{_chave(state, q)}.json"
    if arq.exists():
        return json.loads(arq.read_text(encoding="utf-8"))
    resp = system_one(state, q)
    CACHE.mkdir(parents=True, exist_ok=True)
    arq.write_text(json.dumps(resp, ensure_ascii=False), encoding="utf-8")
    return resp


def _celula(texto: str) -> str:
    return texto.replace("|", "\\|")


def relatorio(linhas: List[Dict[str, Any]], aprovadas: Dict[str, List[Dict[str, Any]]]) -> str:
    titulos = {lic["slug"]: lic for ls in aprovadas.values() for lic in ls}
    out = [
        "# Triagem das aulas RCO (Jev)",
        "",
        "Gerado por `tools/triar_rco.py` a partir de `lake/**/rco/`. **Não editar à mão** — rodar de novo.",
        "",
        "Julgamentos do Jev (TypeSafe), um pedido por aula. São **triagem**, não decisão: "
        f"confiança abaixo de {CONF_REVISAR} — ou equivalência com aula aprovada abaixo de {CONF_EQUIVALENCIA} — "
        "vira ⚠ e pede olho humano. "
        "Densidade vai de 0 (nada novo) a 3 (vários conceitos definidos).",
        "",
        "## Resumo por disciplina",
        "",
        "| Disciplina | Aulas RCO | Já cobertas (confiável) | Cobertas a confirmar ⚠ | Conceituais | Densidade ≥ 2 sem aula aprovada | ⚠ total |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    por_disc: Dict[str, List[Dict[str, Any]]] = {}
    for l in linhas:
        por_disc.setdefault(l["disciplina"], []).append(l)
    for disc, ls in sorted(por_disc.items()):
        cobertas = sum(1 for l in ls if l["aprovada"] not in (None, "nenhuma") and not l["revisar"])
        a_confirmar = sum(1 for l in ls if l["aprovada"] not in (None, "nenhuma") and l["revisar"])
        conceituais = sum(1 for l in ls if l["natureza"] == "conceitual")
        candidatas = sum(1 for l in ls if l["densidade"] >= 2 and l["aprovada"] in (None, "nenhuma"))
        revisar = sum(1 for l in ls if l["revisar"])
        out.append(f"| {LABELS_DISCIPLINA.get(disc, disc)} | {len(ls)} | {cobertas} | {a_confirmar} | {conceituais} | {candidatas} | {revisar} |")
    for disc, ls in sorted(por_disc.items()):
        out += ["", f"## {LABELS_DISCIPLINA.get(disc, disc)}", "",
                "| Tri | Aula RCO | Natureza | Dens. | Aula aprovada equivalente | |",
                "| --- | --- | --- | --- | --- | --- |"]
        for l in sorted(ls, key=lambda x: (x["trimestre"], x["ordem_rco"])):
            link = f"[{_celula(l['titulo'])}](../{l['caminho']})"
            ap = l["aprovada"]
            if ap is None:
                ap_txt = "—"
            elif ap == "nenhuma":
                ap_txt = f"nenhuma ({l['conf_aprovada']:.2f})"
            else:
                lic = titulos.get(ap, {})
                certeza = "título idêntico" if l.get("metodo") == "titulo" else f"{l['conf_aprovada']:.2f}"
                ap_txt = f"{_celula(lic.get('titulo', ap))} ({certeza})"
            out.append(f"| {l['trimestre']} | {link} | {l['natureza']} ({l['conf_natureza']:.2f}) | "
                       f"{l['densidade']:.1f} | {ap_txt} | {'⚠' if l['revisar'] else ''} |")
    return "\n".join(out) + "\n"


def main(argv: Optional[List[str]] = None) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--disciplina", action="append", help="slug(s) de disciplina; padrão: todas")
    ap.add_argument("--paralelo", type=int, default=8)
    args = ap.parse_args(argv)

    caminhos = sorted((ROOT / "lake").glob("*/rco/*tri/*.md"))
    aulas = [carregar(c) for c in caminhos]
    if args.disciplina:
        aulas = [a for a in aulas if a.disciplina in args.disciplina]
    if not aulas:
        print("nenhuma aula RCO extraída — rode tools/extrair_rco.py", file=sys.stderr)
        return 2
    aprovadas = aprovadas_por_disciplina()

    with ThreadPoolExecutor(max_workers=args.paralelo) as ex:
        respostas = list(ex.map(lambda a: julgar(a, aprovadas.get(a.disciplina, [])), aulas))

    linhas, tokens = [], 0
    for aula, resp in zip(aulas, respostas):
        ans = resp["answers"]
        tokens += resp.get("usage", {}).get("input_tokens", 0)
        apr = ans.get("aula_aprovada")
        conf_n = ans["natureza"]["confidence"]
        conf_a = apr["confidence"] if apr else 1.0
        escolha = apr["choice"] if apr else None
        metodo = "jev" if apr else None
        # titulo identico e decisao de codigo, nao de modelo
        igual = mesmo_titulo(aula, aprovadas.get(aula.disciplina, []))
        if igual:
            escolha, conf_a, metodo = igual, 1.0, "titulo"
        linhas.append({
            "caminho": aula.caminho.relative_to(ROOT).as_posix(),
            "titulo": aula.titulo,
            "disciplina": aula.disciplina,
            "trimestre": aula.trimestre,
            "ordem_rco": aula.ordem_rco,
            "natureza": ans["natureza"]["choice"],
            "conf_natureza": conf_n,
            "densidade": ans["densidade"]["score"],
            "aprovada": escolha,
            "conf_aprovada": conf_a,
            "metodo": metodo,
            "revisar": conf_n < CONF_REVISAR or conf_a < CONF_REVISAR
            or (escolha not in (None, "nenhuma") and conf_a < CONF_EQUIVALENCIA),
        })

    # relatorio parcial nao pode apagar as outras disciplinas: reune com o JSON anterior
    json_saida = SAIDA.with_suffix(".json")
    if args.disciplina and json_saida.exists():
        anteriores = json.loads(json_saida.read_text(encoding="utf-8"))
        linhas = [l for l in anteriores if l["disciplina"] not in args.disciplina] + linhas
    SAIDA.parent.mkdir(parents=True, exist_ok=True)
    json_saida.write_text(json.dumps(linhas, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    SAIDA.write_text(relatorio(linhas, aprovadas), encoding="utf-8", newline="\n")
    print(f"[triagem] {len(aulas)} aulas julgadas | {tokens} tokens de entrada, cache incluso "
          f"(~US$ {tokens * 0.042 / 1e6:.4f}) | saída {SAIDA.relative_to(ROOT).as_posix()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
