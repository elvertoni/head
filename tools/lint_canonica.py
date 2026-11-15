#!/usr/bin/env python3
"""Lint do corpo das aulas canônicas contra o contrato da spec.

Confere o que `.claude/skills/prof-toni/spec/01-CANONICA.md` exige do corpo e o
que o parser do ProfessorDash (`catalog/parser.py`) espera. É complementar ao
`lint_wiki.py`, que cuida do grafo da wiki (links, backlinks, fontes).

Somente leitura: aponta, não corrige. Corrigir aula aprovada exige bump de
`versao`, `gerar_manifesto.py` e a publicação em quatro passos (AGENTS.md).

Uso:
    python tools/lint_canonica.py
    python tools/lint_canonica.py --format json
    python tools/lint_canonica.py --fail-on error
    python tools/lint_canonica.py --todas        # inclui aulas não aprovadas
    python tools/lint_canonica.py aulas/x/y/01-z/canonica.md   # só essas aulas (qualquer status)

Códigos:
    corpo-com-h1           error    `# ` no corpo (o título vem do frontmatter)
    bloco-desconhecido     error    `:::tipo` fora do catálogo (6 callouts + roteiro)
    bloco-nao-fechado      error    `:::tipo` sem o `:::` de fechamento
    quiz-correta           error    pergunta sem exatamente uma `correta: true`
    quiz-sem-alternativas  error    pergunta sem alternativas
    diagrama-sem-camadas   error    diagrama-progressivo sem `camadas`
    secao-ausente          warning  falta `## Objetivos` ou `## Prática` (o layout do portal depende dos ids);
                                    blueprints de TCC (disciplina `tcc`, trilha `blueprint-tcc`) são
                                    documento de projeto e só precisam de `## Objetivos`
    rotulo-numerado        warning  `rotulo` de diagrama com número próprio ("1. Navegador")
    yaml-com-markdown      warning  Markdown em campo de quiz/diagrama (o portal mostra os símbolos crus)
    wikilink-sem-rotulo    info     `[[slug]]` sem `|rótulo` (a spec prefere `[[slug|rótulo]]`)
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Iterator, List, Optional, Tuple

try:
    from wiki_core import Diagnostic, body_lines, lesson_paths, parse_frontmatter, relative_path
except ImportError:  # permite `python -m tools.lint_canonica`
    from tools.wiki_core import Diagnostic, body_lines, lesson_paths, parse_frontmatter, relative_path


CALLOUTS = {"conceito", "exemplo", "importante", "atencao", "atenção", "dica", "curiosidade"}
BLOCOS = CALLOUTS | {"roteiro"}
SECOES_DE_LAYOUT = ("Objetivos", "Prática")
# Documento de projeto, não aula: não há atividade a inventar (parecer ASTRA, decisão #044).
SEM_PRATICA = {("tcc", "blueprint-tcc")}
SEVERIDADE = {"error": 3, "warning": 2, "info": 1}

ABRE_BLOCO = re.compile(r"^:::\s*([^\s:]+)")
FECHA_BLOCO = re.compile(r"^:::\s*$")
FENCE = re.compile(r"^(`{3,}|~{3,})\s*([\w-]*)")
ROTULO_NUMERADO = re.compile(r"""^\s*-?\s*rotulo:\s*["']?\s*\d+\s*[.)\-–—:]""")
CAMPO_TEXTO = re.compile(r"""^\s*-?\s*(pergunta|texto|feedback|titulo|rotulo|conteudo):\s*(.*)$""")
MARKDOWN = re.compile(r"`[^`]+`|\*\*[^*]+\*\*|\[[^\]]+\]\([^)]+\)")
WIKILINK_SEM_ROTULO = re.compile(r"\[\[([^\]|#]+)\]\]")


def _fences(lines: List[str], primeira: int) -> Iterator[Tuple[str, int, List[Tuple[int, str]]]]:
    """Devolve (linguagem, linha de abertura, [(nº da linha, texto)]) de cada bloco cercado."""
    i = 0
    while i < len(lines):
        m = FENCE.match(lines[i])
        if not m:
            i += 1
            continue
        marca, lang, inicio = m.group(1), m.group(2), i
        corpo: List[Tuple[int, str]] = []
        i += 1
        while i < len(lines) and not lines[i].startswith(marca[0] * len(marca)):
            corpo.append((primeira + i, lines[i]))
            i += 1
        yield lang, primeira + inicio, corpo
        i += 1


def _fora_de_fence(lines: List[str], primeira: int) -> Iterator[Tuple[int, str]]:
    dentro, marca = False, ""
    for i, linha in enumerate(lines):
        m = FENCE.match(linha)
        if m and not dentro:
            dentro, marca = True, m.group(1)[0] * len(m.group(1))
            continue
        if dentro and linha.startswith(marca):
            dentro = False
            continue
        if not dentro:
            yield primeira + i, linha


def _perguntas(corpo: List[Tuple[int, str]]) -> List[Tuple[int, List[str]]]:
    perguntas: List[Tuple[int, List[str]]] = []
    for n, linha in corpo:
        if re.match(r"^-\s*pergunta:", linha):
            perguntas.append((n, [linha]))
        elif perguntas:
            perguntas[-1][1].append(linha)
    return perguntas


def lint_aula(root: Path, path: Path) -> List[Diagnostic]:
    try:
        rel = relative_path(root, path)
    except ValueError:  # aula fora do repo (rascunho, teste)
        rel = path.as_posix()
    text = path.read_text(encoding="utf-8-sig")
    fm = parse_frontmatter(text)
    lines, primeira = body_lines(text, fm)
    out: List[Diagnostic] = []

    def issue(code: str, sev: str, line: Optional[int], msg: str, target: Optional[str] = None) -> None:
        out.append(Diagnostic(code, sev, rel, line, msg, target))

    titulos = set()
    aberto: Optional[Tuple[str, int]] = None
    for n, linha in _fora_de_fence(lines, primeira):
        if re.match(r"^#\s", linha):
            issue("corpo-com-h1", "error", n, "título `# ` no corpo; o título vem do campo `titulo` do frontmatter")
        m = re.match(r"^##\s+(.+?)\s*$", linha)
        if m:
            titulos.add(m.group(1))
        if FECHA_BLOCO.match(linha):
            if aberto:
                aberto = None
            continue
        m = ABRE_BLOCO.match(linha)
        if m:
            tipo = m.group(1).lower()
            if aberto:
                issue("bloco-nao-fechado", "error", aberto[1], f"`:::{aberto[0]}` aberto sem `:::` antes de outro bloco")
            if tipo not in BLOCOS:
                issue("bloco-desconhecido", "error", n, f"`:::{tipo}` fora do catálogo ({', '.join(sorted(BLOCOS - {'atenção'}))})", tipo)
            aberto = (tipo, n)
        for wl in WIKILINK_SEM_ROTULO.finditer(linha):
            issue("wikilink-sem-rotulo", "info", n, f"`[[{wl.group(1)}]]` sem rótulo; prefira `[[{wl.group(1)}|rótulo]]`", wl.group(1))
    if aberto:
        issue("bloco-nao-fechado", "error", aberto[1], f"`:::{aberto[0]}` sem `:::` de fechamento")

    isento = (str(fm.data.get("disciplina", "")), str(fm.data.get("trilha", ""))) in SEM_PRATICA
    for secao in SECOES_DE_LAYOUT:
        if secao == "Prática" and isento:
            continue
        if secao not in titulos:
            issue("secao-ausente", "warning", None, f"falta `## {secao}` (o leitor do portal monta o layout pelo id dessa seção)", secao)

    for lang, n0, corpo in _fences(lines, primeira):
        if lang not in ("quiz", "diagrama-progressivo"):
            continue
        for n, linha in corpo:
            campo = CAMPO_TEXTO.match(linha)
            if campo and MARKDOWN.search(campo.group(2)):
                issue("yaml-com-markdown", "warning", n, f"Markdown no campo `{campo.group(1)}`: o portal mostra os símbolos crus", campo.group(1))
        if lang == "diagrama-progressivo":
            if not any(re.match(r"^camadas:", l) for _, l in corpo):
                issue("diagrama-sem-camadas", "error", n0, "diagrama-progressivo sem `camadas`")
            for n, linha in corpo:
                if ROTULO_NUMERADO.match(linha):
                    issue("rotulo-numerado", "warning", n, "`rotulo` com número próprio; o componente já numera (vira \"1 · 1. …\")")
        else:
            for n, bloco in _perguntas(corpo):
                if not any(re.match(r"^\s*-\s*texto:", l) for l in bloco):
                    issue("quiz-sem-alternativas", "error", n, "pergunta sem alternativas")
                    continue
                certas = sum(1 for l in bloco if re.match(r"^\s*correta:\s*true\s*$", l, re.I))
                if certas != 1:
                    issue("quiz-correta", "error", n, f"pergunta com {certas} alternativas `correta: true` (precisa de exatamente 1)")
    return out


def lint(root: Path, todas: bool = False, caminhos: Optional[List[Path]] = None) -> List[Diagnostic]:
    diagnostics: List[Diagnostic] = []
    if caminhos:
        for path in caminhos:
            path = path.resolve()
            # diretório: todas as canonica.md dentro dele, de qualquer status
            alvos = sorted(path.rglob("canonica.md")) if path.is_dir() else [path]
            for alvo in alvos:
                diagnostics.extend(lint_aula(root, alvo))
        return diagnostics
    for path in lesson_paths(root):
        if not todas:
            fm = parse_frontmatter(path.read_text(encoding="utf-8-sig"))
            if fm.data.get("status") != "aprovada":
                continue
        diagnostics.extend(lint_aula(root, path))
    return diagnostics


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument("--format", choices=("text", "json"), default="text")
    parser.add_argument("--fail-on", choices=("error", "warning", "info"), default="error")
    parser.add_argument("--todas", action="store_true", help="inclui aulas que não estão aprovadas")
    parser.add_argument("caminhos", nargs="*", type=Path, help="canonica.md ou pastas específicas (ignora o status)")
    args = parser.parse_args(argv)

    diagnostics = lint(args.root.resolve(), args.todas, args.caminhos)
    por_codigo = Counter(d.code for d in diagnostics)
    por_sev = Counter(d.severity for d in diagnostics)
    aulas = len({d.path for d in diagnostics})
    summary = {"total": len(diagnostics), "aulas": aulas, "by_severity": dict(por_sev), "by_code": dict(por_codigo)}
    if args.format == "json":
        print(json.dumps({"summary": summary, "diagnostics": [d.as_dict() for d in diagnostics]}, ensure_ascii=False, indent=2))
    else:
        for d in diagnostics:
            onde = f"{d.path}:{d.line}" if d.line else d.path
            print(f"{d.severity.upper()} [{d.code}] {onde} — {d.message}")
        resumo = ", ".join(f"{c} {n}" for c, n in sorted(por_codigo.items())) or "nenhum achado"
        print(f"\n{len(diagnostics)} achado(s) em {aulas} aula(s): {resumo}")
    limite = SEVERIDADE[args.fail_on]
    return 1 if any(SEVERIDADE[d.severity] >= limite for d in diagnostics) else 0


if __name__ == "__main__":
    sys.exit(main())
