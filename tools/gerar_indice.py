#!/usr/bin/env python3
"""Gera o catálogo de conceitos a partir dos frontmatters.

Os resumos já curados em `conceitos/index.md` são preservados por slug. Para
páginas novas, o texto de `## Em uma frase` é usado como resumo. Stubs que já
estavam catalogados permanecem numa seção explícita de pendências.

Uso:
    python tools/gerar_indice.py --check
    python tools/gerar_indice.py --stdout
    python tools/gerar_indice.py --write
"""
from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Optional, Tuple

try:
    from wiki_core import as_list, concept_paths, format_aulas, one_line_summary, parse_frontmatter
except ImportError:  # permite `python -m tools.gerar_indice`
    from tools.wiki_core import as_list, concept_paths, format_aulas, one_line_summary, parse_frontmatter


ROOT = Path(__file__).resolve().parent.parent
INDEX = ROOT / "conceitos" / "index.md"
ENTRY_RE = re.compile(
    r"^-\s+\[\[([^|\]]+)(?:\|[^\]]+)?\]\]\s+—\s+(.*?)\s+·\s+"
    r"(vivo|rascunho|obsoleto)\s+·\s+aulas\s+\[([^\]]*)\]\s*$"
)
DISCIPLINE_LABELS = {
    "desenvolvimento-full-stack-e-cloud-computing": "Desenvolvimento Full Stack e Cloud Computing",
    "inovacao-inteligencia-artificial-e-robotica-educacional": "Inovação, Inteligência Artificial e Robótica Educacional",
    "inovacao-tecnologia-e-empreendedorismo": "Inovação, Tecnologia e Empreendedorismo",
    "inteligencia-artificial": "Inteligência Artificial",
}


def existing_catalog() -> Tuple[Dict[str, str], Dict[str, str], List[str]]:
    """Retorna resumos, linhas e links sem página do índice atual."""
    summaries: Dict[str, str] = {}
    original_lines: Dict[str, str] = {}
    malformed: List[str] = []
    if not INDEX.exists():
        return summaries, original_lines, malformed

    for line in INDEX.read_text(encoding="utf-8-sig").splitlines():
        match = ENTRY_RE.match(line.strip())
        if match:
            slug, summary = match.group(1).strip(), match.group(2).strip()
            summaries.setdefault(slug, summary)
            original_lines.setdefault(slug, line.strip())
        elif "stub" in line.casefold():
            for stub_match in re.finditer(r"\[\[([^\]|#]+)(?:\|[^\]]+)?\]\]", line):
                slug = stub_match.group(1).strip()
                original_lines.setdefault(
                    slug,
                    f"- [[{slug}]] — stub pendente (sem página) · rascunho · aulas []",
                )
    return summaries, original_lines, malformed


def render(root: Path = ROOT) -> Tuple[str, List[str]]:
    summaries, original_lines, errors = existing_catalog()
    records: List[Dict[str, object]] = []
    seen_slugs: Dict[str, Path] = {}
    for path in concept_paths(root):
        text = path.read_text(encoding="utf-8-sig")
        frontmatter = parse_frontmatter(text)
        for code, line, message in frontmatter.errors:
            errors.append(f"{path.relative_to(root).as_posix()}:{line}: {message}")
        data = frontmatter.data
        slug = str(data.get("slug") or "").strip()
        if not slug:
            errors.append(f"{path.relative_to(root).as_posix()}: slug ausente")
            continue
        if slug in seen_slugs:
            errors.append(
                f"slug duplicado: {slug} em {seen_slugs[slug].relative_to(root).as_posix()} "
                f"e {path.relative_to(root).as_posix()}"
            )
            continue
        seen_slugs[slug] = path
        discipline = str(data.get("disciplina") or path.parent.name).strip()
        summary = summaries.get(slug) or one_line_summary(text, frontmatter)
        records.append({
            "slug": slug,
            "discipline": discipline,
            "name": str(data.get("conceito") or slug),
            "summary": summary.replace("\n", " ").strip(),
            "status": str(data.get("status") or ""),
            "aulas": data.get("aulas", []),
        })

    groups: Dict[str, List[Dict[str, object]]] = defaultdict(list)
    for record in records:
        groups[str(record["discipline"])].append(record)

    lines = [
        "# Índice de Conceitos",
        "",
        "> Catálogo do grafo de conceitos do segundo cérebro. Uma linha por nó.",
        "> Regenerável a partir dos frontmatters com `python tools/gerar_indice.py`.",
        "",
    ]
    for discipline in sorted(groups):
        label = DISCIPLINE_LABELS.get(discipline, discipline.replace("-", " ").title())
        lines.append(f"## {label}")
        lines.append("")
        for record in sorted(groups[discipline], key=lambda item: str(item["slug"])):
            lines.append(
                f"- [[{record['slug']}]] — {record['summary']} · "
                f"{record['status']} · aulas [{format_aulas(record['aulas'])}]"
            )
        lines.append("")

    stubs = sorted(slug for slug in original_lines if slug not in seen_slugs)
    if stubs:
        lines.extend(["## Pendências catalogadas", ""])
        for slug in stubs:
            lines.append(original_lines[slug])
        lines.append("")

    return "\n".join(lines).rstrip() + "\n", errors


def main(argv: Optional[List[str]] = None) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--check", action="store_true", help="valida sem escrever")
    modes.add_argument("--stdout", action="store_true", help="imprime o resultado")
    modes.add_argument("--write", action="store_true", help="escreve conceitos/index.md")
    args = parser.parse_args(argv)
    content, errors = render()
    if errors:
        for error in errors:
            print(f"ERRO [index] {error}", file=sys.stderr)
        return 2

    if args.stdout:
        print(content, end="")
        return 0
    if args.write:
        if INDEX.read_text(encoding="utf-8-sig") != content if INDEX.exists() else True:
            INDEX.write_text(content, encoding="utf-8")
            print(f"conceitos/index.md gerado: {sum(1 for _ in concept_paths(ROOT))} conceitos")
        else:
            print("conceitos/index.md já está atualizado")
        return 0

    if not INDEX.exists() or INDEX.read_text(encoding="utf-8-sig") != content:
        print("[check] conceitos/index.md diverge do catálogo gerado", file=sys.stderr)
        return 1
    print("[check] conceitos/index.md sem divergências")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
