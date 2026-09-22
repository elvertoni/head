#!/usr/bin/env python3
"""Gera os mapas de conteudo (MOCs) de `mapas/` a partir da proveniencia dos conceitos.

Cada conceito declara em `fontes` o arquivo do lake de onde saiu. Nas pos-graduacoes
esse caminho ja carrega a estrutura do curso — `lake/{Curso}/{Modulo}/{Materia}/{NN - Aula N - Titulo - Apostila}.pdf`
— entao o mapa agrupa por modulo, materia e aula, e lista os conceitos de cada aula.
Um conceito que aparece em varias aulas entra em todas: o mapa serve para consultar
"o que caiu na aula 3", nao para contar conceitos.

O mapa e derivado, como `conceitos/index.md`: nunca editar a mao, rodar de novo.

Uso:
    python tools/gerar_mapas.py            # escreve mapas/{disciplina}.md
    python tools/gerar_mapas.py --check    # exit != 0 se algum mapa estiver desatualizado
"""
from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Optional, Tuple

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.gerar_manifesto import LABELS_DISCIPLINA, label_de_slug  # noqa: E402
from tools.wiki_core import as_list, concept_paths, parse_frontmatter  # noqa: E402

MAPAS = ROOT / "mapas"
LABELS_POS = {
    "inovacao-inteligencia-artificial-e-robotica-educacional": "Pós — Inovação, IA e Robótica Educacional",
    "desenvolvimento-full-stack-e-cloud-computing": "Pós — Desenvolvimento Full Stack e Cloud Computing",
}
SEM_GRUPO = "(sem módulo)"
OUTRAS = "Outras fontes"
RE_SUFIXO = re.compile(r"\s*-\s*(Apostila|Resumo|Slides|Material)\b.*$", re.IGNORECASE)
RE_NUM = re.compile(r"(\d+)")


def rotulo_aula(arquivo: str) -> str:
    """'03 - Aula 3 - IOT e 5G - Apostila (Slides).pdf' -> 'Aula 3 — IOT e 5G'."""
    nome = re.sub(r"\.[A-Za-z0-9]{2,4}$", "", arquivo)
    nome = RE_SUFIXO.sub("", nome)
    partes = [p.strip() for p in nome.split(" - ") if p.strip()]
    if partes and partes[0].isdigit():
        partes = partes[1:]
    if len(partes) >= 2 and partes[0].lower().startswith("aula"):
        return f"{partes[0]} — {' - '.join(partes[1:])}"
    return " - ".join(partes) or arquivo


def _ordem(texto: str) -> Tuple[int, str]:
    m = RE_NUM.search(texto)
    return (int(m.group(1)) if m else 10**6, texto)


def _grupo(fonte: str) -> Optional[Tuple[str, str, str]]:
    """(modulo, materia, aula) de uma fonte do lake; None se nao for do lake."""
    if not fonte.startswith("lake/"):
        return None
    partes = fonte.split("/")[2:]  # tira "lake" e a pasta do curso/disciplina
    if not partes:
        return None
    aula = rotulo_aula(partes[-1])
    pastas = partes[:-1]
    modulo = pastas[0] if pastas else SEM_GRUPO
    materia = " / ".join(pastas[1:]) if len(pastas) > 1 else ""
    return modulo, materia, aula


def coletar(root: Path) -> Dict[str, List[dict]]:
    por_disc: Dict[str, List[dict]] = defaultdict(list)
    for caminho in concept_paths(root):
        fm = parse_frontmatter(caminho.read_text(encoding="utf-8")).data
        if not fm.get("slug") or fm.get("status") == "obsoleto":
            continue
        por_disc[str(fm.get("disciplina", caminho.parent.name))].append({
            "slug": str(fm["slug"]),
            "nome": str(fm.get("conceito") or fm["slug"]),
            "status": str(fm.get("status", "")),
            "tipo": str(fm.get("tipo", "")),
            "caminho": caminho.relative_to(root).with_suffix("").as_posix(),
            "fontes": [str(f) for f in as_list(fm.get("fontes"))],
        })
    return por_disc


def renderizar(disciplina: str, conceitos: List[dict]) -> str:
    arvore: Dict[str, Dict[str, Dict[str, List[dict]]]] = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
    for c in conceitos:
        vistos = set()
        grupos = [g for g in (_grupo(f) for f in c["fontes"]) if g]
        for g in grupos or [(OUTRAS, "", "")]:
            if g not in vistos:
                vistos.add(g)
                arvore[g[0]][g[1]][g[2]].append(c)

    rotulo = LABELS_POS.get(disciplina) or LABELS_DISCIPLINA.get(disciplina) or label_de_slug(disciplina)
    vivos = sum(1 for c in conceitos if c["status"] == "vivo")
    out = [
        "---",
        "tipo: mapa",
        f"disciplina: {disciplina}",
        f"conceitos: {len(conceitos)}",
        "gerado_por: tools/gerar_mapas.py",
        "---",
        "",
        f"# Mapa — {rotulo}",
        "",
        f"> Gerado de `conceitos/{disciplina}/` pela proveniência (`fontes`). **Não editar à mão** — "
        "rodar `python tools/gerar_mapas.py`.",
        f"> {len(conceitos)} conceitos · {vivos} vivos · {len(conceitos) - vivos} rascunhos. "
        "Um conceito citado em várias aulas aparece em cada uma.",
    ]
    marca = {"vivo": "", "rascunho": " · _rascunho_"}
    for modulo in sorted(arvore, key=lambda m: (m == OUTRAS, _ordem(m))):
        out += ["", f"## {modulo}"]
        for materia in sorted(arvore[modulo]):
            if materia:
                out += ["", f"### {materia}"]
            for aula in sorted(arvore[modulo][materia], key=_ordem):
                if aula:
                    out += ["", f"#### {aula}"]
                out.append("")
                for c in sorted(arvore[modulo][materia][aula], key=lambda c: c["nome"].lower()):
                    extra = marca.get(c["status"], f" · _{c['status']}_")
                    if c["tipo"] == "sintese":
                        extra += " · síntese"
                    out.append(f"- [[{c['caminho']}|{c['nome']}]]{extra}")
    return "\n".join(out) + "\n"


def renderizar_indice(por_disc: Dict[str, List[dict]]) -> str:
    """Pagina de entrada do vault no Obsidian: mapas, bases e indices derivados."""
    out = [
        "---",
        "tipo: mapa",
        "gerado_por: tools/gerar_mapas.py",
        "---",
        "",
        "# Início — segundo cérebro PROF-TONI",
        "",
        "> Gerado por `tools/gerar_mapas.py`. **Não editar à mão.**",
        "",
        "## Mapas por disciplina",
        "",
    ]
    for disciplina, conceitos in sorted(por_disc.items(), key=lambda kv: -len(kv[1])):
        rotulo = LABELS_POS.get(disciplina) or LABELS_DISCIPLINA.get(disciplina) or label_de_slug(disciplina)
        vivos = sum(1 for c in conceitos if c["status"] == "vivo")
        out.append(f"- [[mapas/{disciplina}|{rotulo}]] — {len(conceitos)} conceitos, {vivos} vivos")
    out += [
        "",
        "## Vistas (Bases)",
        "",
        "- [[mapas/conceitos.base|Conceitos]] — fila de promoção, pós por tipo, vivos, sínteses",
        "- [[mapas/rco.base|Aulas RCO (SEED)]] — as aulas extraídas do RCO, por disciplina e trimestre",
        "",
        "## Índices",
        "",
        "- [[conceitos/index|Catálogo de conceitos]]",
        "- [[conceitos/log|Diário da wiki]] (append-only)",
        "- [[docs/rco-triagem|Triagem das aulas RCO]] (Jev)",
    ]
    return "\n".join(out) + "\n"


def main(argv: Optional[List[str]] = None) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--check", action="store_true", help="não escreve; exit 1 se algum mapa mudaria")
    args = ap.parse_args(argv)

    por_disc = coletar(ROOT)
    saidas = [(MAPAS / f"{d}.md", renderizar(d, c), len(c)) for d, c in sorted(por_disc.items())]
    saidas.append((MAPAS / "index.md", renderizar_indice(por_disc), sum(len(c) for c in por_disc.values())))
    desatualizados = 0
    for destino, texto, conceitos in saidas:
        atual = destino.read_text(encoding="utf-8") if destino.exists() else None
        if atual == texto:
            continue
        desatualizados += 1
        if args.check:
            print(f"desatualizado: {destino.relative_to(ROOT).as_posix()}")
        else:
            MAPAS.mkdir(exist_ok=True)
            destino.write_text(texto, encoding="utf-8", newline="\n")
            print(f"escrito: {destino.relative_to(ROOT).as_posix()} ({conceitos} conceitos)")
    if not desatualizados:
        print(f"[mapas] {len(saidas)} mapas em dia")
    return 1 if args.check and desatualizados else 0


if __name__ == "__main__":
    sys.exit(main())
