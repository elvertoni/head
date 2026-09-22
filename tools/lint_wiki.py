#!/usr/bin/env python3
"""Lint determinístico da wiki de conceitos e das aulas canônicas.

O comando é somente leitura. Ele aponta problemas para revisão humana; não
cria stubs, não promove rascunhos e não altera `lake/`, `conceitos/` ou `aulas/`.

Uso:
    python tools/lint_wiki.py
    python tools/lint_wiki.py --format json
    python tools/lint_wiki.py --fail-on error
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Set, Tuple

try:
    from wiki_core import (
        CONCEPT_FIELDS,
        CONCEPT_STATUSES,
        CONCEPT_TYPES,
        REQUIRED_SECTIONS,
        Diagnostic,
        Frontmatter,
        as_list,
        body_lines,
        concept_paths,
        extract_wikilinks,
        lesson_paths,
        parse_frontmatter,
        relative_path,
    )
except ImportError:  # permite `python -m tools.lint_wiki`
    from tools.wiki_core import (
        CONCEPT_FIELDS,
        CONCEPT_STATUSES,
        CONCEPT_TYPES,
        REQUIRED_SECTIONS,
        Diagnostic,
        Frontmatter,
        as_list,
        body_lines,
        concept_paths,
        extract_wikilinks,
        lesson_paths,
        parse_frontmatter,
        relative_path,
    )


LESSON_REQUIRED = (
    "titulo",
    "disciplina",
    "trilha",
    "ordem",
    "slug",
    "status",
    "versao",
    "atualizado_em",
)
SEVERITY_RANK = {"info": 0, "warning": 1, "error": 2}
INDEX_LINK_RE = re.compile(r"^-\s+\[\[([^|\]]+)(?:\|[^\]]+)?\]\]")
GRAPHIFY_DISCIPLINE = "desenvolvimento-full-stack-e-cloud-computing"
INLINE_CODE_RE = re.compile(r"(?<!`)`([^`\n]+)`(?!`)")
LESSON_PATH_RE = re.compile(
    r"^aulas/[^/\\\s]+/[^/\\\s]+/[0-9]{2}-[^/\\\s]+/canonica\.md$"
)


def _issue(
    diagnostics: List[Diagnostic],
    root: Path,
    path: Path,
    code: str,
    severity: str,
    message: str,
    line: Optional[int] = None,
    target: Optional[str] = None,
) -> None:
    diagnostics.append(
        Diagnostic(code, severity, relative_path(root, path), line, message, target)
    )


def _parse_date(value: Any) -> Optional[dt.date]:
    if value is None:
        return None
    try:
        return dt.date.fromisoformat(str(value))
    except ValueError:
        return None


def _index_stubs(root: Path) -> Set[str]:
    index = root / "conceitos" / "index.md"
    if not index.exists():
        return set()
    result: Set[str] = set()
    for line in index.read_text(encoding="utf-8-sig").splitlines():
        match = INDEX_LINK_RE.match(line.strip())
        if match:
            result.add(match.group(1).strip())
    return result


def _valid_list_of_ints(value: Any) -> bool:
    return all(isinstance(item, int) and not isinstance(item, bool) for item in as_list(value))


def _lesson_order(value: Any) -> Optional[int]:
    if isinstance(value, bool) or value is None:
        return None
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


def _aula_orders(value: Any) -> Set[int]:
    return {
        item
        for item in as_list(value)
        if isinstance(item, int) and not isinstance(item, bool)
    }


def _where_appears_code(lines: List[str], first_line: int) -> List[Tuple[str, int]]:
    """Retorna trechos inline de código da seção `## Onde aparece`."""
    section_start: Optional[int] = None
    for index, line in enumerate(lines):
        if re.match(r"^##\s+Onde aparece\s*$", line.strip()):
            section_start = index + 1
            break
    if section_start is None:
        return []

    result: List[Tuple[str, int]] = []
    in_fence = False
    fence: Optional[str] = None
    for index in range(section_start, len(lines)):
        line = lines[index]
        if re.match(r"^##\s+", line.strip()):
            break
        stripped = line.lstrip()
        fence_match = re.match(r"(```+|~~~+)", stripped)
        if fence_match:
            marker = fence_match.group(1)[0]
            if not in_fence:
                in_fence = True
                fence = marker
            elif marker == fence:
                in_fence = False
                fence = None
            continue
        if in_fence:
            continue
        result.extend(
            (match.group(1).strip(), first_line + index)
            for match in INLINE_CODE_RE.finditer(line)
        )
    return result


def _looks_like_lesson_path(value: str) -> bool:
    return (
        value.startswith(("aulas/", "aulas\\", "./aulas/", "../aulas/"))
        or "canonica.md" in value
    )


def _load_graphify_index(root: Path) -> Optional[Dict[str, Any]]:
    """Carrega o índice derivado sem tratar o cache como fonte bruta."""
    mapping_path = (
        root
        / "lake"
        / GRAPHIFY_DISCIPLINE
        / "graphify-out"
        / ".full_mapping.json"
    )
    if not mapping_path.exists():
        return None
    try:
        payload = json.loads(mapping_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError):
        return {"invalid": True, "path": mapping_path}
    if not isinstance(payload, list):
        return {"invalid": True, "path": mapping_path}

    entries: Dict[str, Dict[str, Any]] = {}
    for item in payload:
        if not isinstance(item, dict):
            continue
        pdf = item.get("pdf")
        if not isinstance(pdf, str) or not pdf.strip():
            continue
        normalized = pdf.replace("\\", "/").strip().casefold()
        entries.setdefault(normalized, item)
    return {"invalid": False, "entries": entries, "path": mapping_path}


def _graphify_cache_status(
    root: Path, source: str, index: Optional[Dict[str, Any]]
) -> Optional[Tuple[str, str]]:
    """Retorna (código, detalhe) para uma fonte ausente com cache mapeado."""
    prefix = f"lake/{GRAPHIFY_DISCIPLINE}/"
    source_key = source.replace("\\", "/").strip().casefold()
    if not source_key.startswith(prefix):
        return None
    if index is None:
        return None
    if index.get("invalid"):
        return "source-cache-invalid", "índice .full_mapping.json inválido"

    entry = None
    for pdf_key, candidate in index.get("entries", {}).items():
        if pdf_key == source_key or pdf_key.endswith(f"/{source_key}"):
            entry = candidate
            break
    if entry is None:
        return None

    txt = entry.get("txt")
    cache_marker = "/graphify-out/txtcache/"
    if not isinstance(txt, str) or cache_marker not in txt.replace("\\", "/").casefold():
        return "source-cache-invalid", "mapeamento sem caminho de txtcache válido"

    cache_name = txt.replace("\\", "/").rstrip("/").rsplit("/", 1)[-1]
    if not cache_name or cache_name in {".", ".."}:
        return "source-cache-invalid", "mapeamento sem arquivo de cache"
    cache_path = (
        root
        / "lake"
        / GRAPHIFY_DISCIPLINE
        / "graphify-out"
        / "txtcache"
        / cache_name
    )
    try:
        text = cache_path.read_text(encoding="utf-8")
    except (OSError, UnicodeError):
        return "source-cache-invalid", f"cache não utilizável: {cache_path.name}"
    if not text.strip():
        return "source-cache-empty", cache_path.name
    return "source-cache-hit", cache_path.name


def lint(root: Path) -> List[Diagnostic]:
    diagnostics: List[Diagnostic] = []
    graphify_index = _load_graphify_index(root)
    concept_records: List[Dict[str, Any]] = []
    concept_by_slug: Dict[str, Dict[str, Any]] = {}
    duplicate_slugs: Dict[str, List[Path]] = defaultdict(list)
    aka_owners: Dict[str, List[Tuple[str, Path]]] = defaultdict(list)

    for path in concept_paths(root):
        text = path.read_text(encoding="utf-8-sig")
        frontmatter = parse_frontmatter(text)
        rel = relative_path(root, path)
        for code, line, message in frontmatter.errors:
            severity = "error" if code in {"frontmatter-missing", "frontmatter-unclosed"} else "warning"
            _issue(diagnostics, root, path, code, severity, message, line)

        data = frontmatter.data
        for field in CONCEPT_FIELDS:
            if field not in data or data[field] in (None, ""):
                _issue(
                    diagnostics,
                    root,
                    path,
                    "frontmatter-missing-field",
                    "error",
                    f"campo obrigatório ausente: {field}",
                    frontmatter.lines.get(field),
                )

        slug = str(data.get("slug") or path.stem)
        record = {"path": path, "text": text, "fm": frontmatter, "slug": slug}
        concept_records.append(record)
        duplicate_slugs[slug].append(path)
        if slug != path.stem:
            _issue(
                diagnostics,
                root,
                path,
                "slug-file-mismatch",
                "error",
                f"slug '{slug}' não corresponde ao nome '{path.stem}'",
                frontmatter.lines.get("slug"),
            )
        discipline = str(data.get("disciplina") or "")
        if discipline and discipline != path.parent.name:
            _issue(
                diagnostics,
                root,
                path,
                "discipline-path-mismatch",
                "warning",
                f"disciplina '{discipline}' difere da pasta '{path.parent.name}'",
                frontmatter.lines.get("disciplina"),
            )
        if data.get("tipo") not in CONCEPT_TYPES:
            _issue(
                diagnostics,
                root,
                path,
                "invalid-type",
                "error",
                f"tipo inválido: {data.get('tipo')!r}",
                frontmatter.lines.get("tipo"),
            )
        if data.get("status") not in CONCEPT_STATUSES:
            _issue(
                diagnostics,
                root,
                path,
                "invalid-status",
                "error",
                f"status inválido: {data.get('status')!r}",
                frontmatter.lines.get("status"),
            )
        if not isinstance(data.get("aka"), list):
            _issue(
                diagnostics,
                root,
                path,
                "invalid-aka",
                "error",
                "aka deve ser uma lista",
                frontmatter.lines.get("aka"),
            )
        for alias in as_list(data.get("aka")):
            normalized = str(alias).strip().casefold()
            if normalized:
                aka_owners[normalized].append((slug, path))
        if not _valid_list_of_ints(data.get("aulas")):
            _issue(
                diagnostics,
                root,
                path,
                "invalid-aulas",
                "warning",
                "aulas deve ser uma lista de números de ordem",
                frontmatter.lines.get("aulas"),
            )
        date_value = data.get("atualizado_em")
        if _parse_date(date_value) is None:
            _issue(
                diagnostics,
                root,
                path,
                "invalid-date",
                "error",
                f"atualizado_em não é uma data ISO válida: {date_value!r}",
                frontmatter.lines.get("atualizado_em"),
            )
        elif _parse_date(date_value) > dt.date.today():
            _issue(
                diagnostics,
                root,
                path,
                "future-date",
                "warning",
                f"atualizado_em está no futuro: {date_value}",
                frontmatter.lines.get("atualizado_em"),
            )

        lines, first_line = body_lines(text, frontmatter)
        headings = {match.group(1).strip() for line in lines if (match := re.match(r"^##\s+(.+?)\s*$", line))}
        for section in REQUIRED_SECTIONS:
            if section not in headings:
                _issue(
                    diagnostics,
                    root,
                    path,
                    "missing-section",
                    "warning",
                    f"seção obrigatória ausente: ## {section}",
                )
        if any(re.match(r"^#\s+", line) for line in lines):
            _issue(
                diagnostics,
                root,
                path,
                "body-h1",
                "warning",
                "o corpo não deve conter H1; o título vem do frontmatter",
            )
        links = list(extract_wikilinks(lines, first_line))
        record["links"] = links
        record["where_code"] = _where_appears_code(lines, first_line)
        if slug not in concept_by_slug:
            concept_by_slug[slug] = record

    for slug, paths in sorted(duplicate_slugs.items()):
        if len(paths) > 1:
            for path in paths:
                _issue(
                    diagnostics,
                    root,
                    path,
                    "duplicate-slug",
                    "error",
                    f"slug duplicado: {slug} ({len(paths)} arquivos)",
                    target=slug,
                )

    for alias, owners in sorted(aka_owners.items()):
        unique_slugs = sorted({slug for slug, _ in owners})
        if len(unique_slugs) > 1:
            for slug, path in owners:
                _issue(
                    diagnostics,
                    root,
                    path,
                    "aka-collision",
                    "warning",
                    f"aka '{alias}' aparece em conceitos distintos: {', '.join(unique_slugs)}",
                    target=alias,
                )

    lesson_records: List[Dict[str, Any]] = []
    for path in lesson_paths(root):
        text = path.read_text(encoding="utf-8-sig")
        frontmatter = parse_frontmatter(text)
        data = frontmatter.data
        if data.get("status") != "aprovada":
            continue
        for field in LESSON_REQUIRED:
            if field not in data or data[field] in (None, ""):
                _issue(
                    diagnostics,
                    root,
                    path,
                    "lesson-frontmatter-missing",
                    "error",
                    f"campo obrigatório ausente na aula: {field}",
                    frontmatter.lines.get(field),
                )
        lines, first_line = body_lines(text, frontmatter)
        links = list(extract_wikilinks(lines, first_line))
        lesson_records.append(
            {
                "path": path,
                "rel": relative_path(root, path),
                "fm": frontmatter,
                "links": links,
                "order": _lesson_order(data.get("ordem")),
            }
        )
        if not links:
            _issue(
                diagnostics,
                root,
                path,
                "lesson-no-links",
                "warning",
                "aula aprovada não referencia nenhum conceito",
            )

    inbound: Counter[str] = Counter()
    for record in concept_records:
        for target, _line in record.get("links", []):
            inbound[target] += 1
    for record in lesson_records:
        for target, _line in record["links"]:
            inbound[target] += 1

    known_stubs = _index_stubs(root) - set(concept_by_slug)
    for record in concept_records:
        path = record["path"]
        for target, line in record.get("links", []):
            if target not in concept_by_slug:
                code = "intentional-stub" if target in known_stubs else "dead-link"
                severity = "info" if code == "intentional-stub" else "warning"
                message = (
                    f"link aponta para stub catalogado: [[{target}]]"
                    if code == "intentional-stub"
                    else f"link sem página correspondente: [[{target}]]"
                )
                _issue(diagnostics, root, path, code, severity, message, line, target)
    for record in lesson_records:
        path = record["path"]
        for target, line in record["links"]:
            if target not in concept_by_slug:
                code = "intentional-stub" if target in known_stubs else "dead-link"
                severity = "info" if code == "intentional-stub" else "warning"
                message = (
                    f"link aponta para stub catalogado: [[{target}]]"
                    if code == "intentional-stub"
                    else f"link sem página correspondente: [[{target}]]"
                )
                _issue(diagnostics, root, path, code, severity, message, line, target)

    for record in concept_records:
        slug = record["slug"]
        if inbound[slug] == 0:
            status = record["fm"].data.get("status")
            severity = "info" if status == "obsoleto" else "warning"
            _issue(
                diagnostics,
                root,
                record["path"],
                "orphan",
                severity,
                f"página sem inlinks ({status})",
                target=slug,
            )

    for record in concept_records:
        path = record["path"]
        concept_updated = _parse_date(record["fm"].data.get("atualizado_em"))
        for source in as_list(record["fm"].data.get("fontes")):
            source = str(source).strip()
            if not source:
                continue
            if re.match(r"^https?://", source, re.I):
                continue
            source_path = root / source.replace("/", "/")
            if source.startswith("lake/"):
                if not source_path.is_file():
                    _issue(
                        diagnostics,
                        root,
                        path,
                        "source-missing",
                        "warning",
                        f"fonte lake não encontrada localmente: {source}",
                        target=source,
                    )
                    cache_status = _graphify_cache_status(root, source, graphify_index)
                    if cache_status:
                        code, detail = cache_status
                        messages = {
                            "source-cache-hit": (
                                "há texto Graphify derivado válido para a fonte ausente "
                                f"({detail}); o cache não substitui a fonte bruta"
                            ),
                            "source-cache-empty": (
                                f"cache Graphify vazio para a fonte ausente: {detail}"
                            ),
                            "source-cache-invalid": (
                                f"cache Graphify inválido ou inutilizável para a fonte ausente: {detail}"
                            ),
                        }
                        _issue(
                            diagnostics,
                            root,
                            path,
                            code,
                            "info",
                            messages[code],
                            target=source,
                        )
                elif concept_updated is not None:
                    try:
                        source_updated = dt.date.fromtimestamp(source_path.stat().st_mtime)
                    except OSError:
                        source_updated = None
                    if source_updated is not None and source_updated > concept_updated:
                        _issue(
                            diagnostics,
                            root,
                            path,
                            "stale",
                            "warning",
                            f"fonte foi modificada em {source_updated}, depois do conceito ({concept_updated})",
                            record["fm"].lines.get("atualizado_em"),
                            source,
                        )
            elif source.startswith("aulas/"):
                _issue(
                    diagnostics,
                    root,
                    path,
                    "source-layer-mismatch",
                    "warning",
                    f"fontes deve apontar para lake/ ou URL; referência a aula: {source}",
                    target=source,
                )
            else:
                _issue(
                    diagnostics,
                    root,
                    path,
                    "source-format",
                    "warning",
                    f"proveniência fora do formato lake/ ou URL: {source}",
                    target=source,
                )

    lessons_by_path = {record["rel"]: record for record in lesson_records}
    lessons_by_order: Dict[int, List[Dict[str, Any]]] = defaultdict(list)
    for record in lesson_records:
        if record["order"] is not None:
            lessons_by_order[record["order"]].append(record)

    for concept in concept_records:
        path = concept["path"]
        slug = concept["slug"]
        data = concept["fm"].data
        aula_orders = _aula_orders(data.get("aulas"))
        where_paths: Dict[str, int] = {}
        seen_paths: Set[str] = set()

        for value, line in concept.get("where_code", []):
            if not _looks_like_lesson_path(value):
                continue
            if value in seen_paths:
                continue
            seen_paths.add(value)
            if not LESSON_PATH_RE.fullmatch(value):
                _issue(
                    diagnostics,
                    root,
                    path,
                    "backlink-path-invalid",
                    "warning",
                    f"caminho de aula malformado em ## Onde aparece: {value!r}",
                    line,
                    value,
                )
                continue

            lesson = lessons_by_path.get(value)
            if lesson is None:
                _issue(
                    diagnostics,
                    root,
                    path,
                    "backlink-path-missing",
                    "warning",
                    f"caminho não corresponde a uma canônica aprovada: {value}",
                    line,
                    value,
                )
                continue

            where_paths[value] = line
            lesson_order = lesson["order"]
            if lesson_order is not None and lesson_order not in aula_orders:
                _issue(
                    diagnostics,
                    root,
                    path,
                    "backlink-missing",
                    "warning",
                    f"conceito aponta para {value}, mas não lista a ordem {lesson_order} em aulas",
                    line,
                    value,
                )
            if slug not in {target for target, _ in lesson["links"]}:
                _issue(
                    diagnostics,
                    root,
                    path,
                    "backlink-missing",
                    "warning",
                    f"## Onde aparece lista {value}, mas essa aula não cita [[{slug}]]",
                    line,
                    value,
                )

        concept["where_paths"] = where_paths

    for lesson in lesson_records:
        lesson_order = lesson["order"]
        lesson_rel = lesson["rel"]
        for target, line in lesson["links"]:
            concept = concept_by_slug.get(target)
            if not concept:
                continue
            aula_orders = _aula_orders(concept["fm"].data.get("aulas"))
            if lesson_order is not None and lesson_order not in aula_orders:
                _issue(
                    diagnostics,
                    root,
                    lesson["path"],
                    "backlink-missing",
                    "warning",
                    f"aula cita [[{target}]], mas o conceito não lista a ordem {lesson_order} em aulas",
                    line,
                    target,
                )

            if lesson_rel in concept.get("where_paths", {}):
                continue
            if lesson_order is None or lesson_order not in aula_orders:
                continue

            same_order = lessons_by_order.get(lesson_order, [])
            if len(same_order) > 1:
                has_path_for_order = any(
                    lessons_by_path[where_path]["order"] == lesson_order
                    for where_path in concept.get("where_paths", {})
                )
                if has_path_for_order:
                    _issue(
                        diagnostics,
                        root,
                        lesson["path"],
                        "backlink-missing",
                        "warning",
                        f"aula cita [[{target}]], mas ## Onde aparece não registra o caminho exato {lesson_rel}",
                        line,
                        target,
                    )
                else:
                    _issue(
                        diagnostics,
                        root,
                        lesson["path"],
                        "backlink-ambiguous",
                        "warning",
                        f"a ordem {lesson_order} aparece em {len(same_order)} canônicas; registre o caminho exato {lesson_rel} em ## Onde aparece",
                        line,
                        target,
                    )
            else:
                _issue(
                    diagnostics,
                    root,
                    lesson["path"],
                    "backlink-missing",
                    "warning",
                    f"aula cita [[{target}]], mas ## Onde aparece não registra o caminho exato {lesson_rel}",
                    line,
                    target,
                )

    for concept in concept_records:
        slug = concept["slug"]
        data = concept["fm"].data
        where_paths = concept.get("where_paths", {})
        for lesson_order in _aula_orders(data.get("aulas")):
            lessons_of_order = lessons_by_order.get(lesson_order, [])
            linked_lessons = [
                lesson
                for lesson in lessons_of_order
                if slug in {target for target, _ in lesson["links"]}
            ]
            path_entries_for_order = [
                lesson
                for where_path in where_paths
                if (lesson := lessons_by_path[where_path])["order"] == lesson_order
            ]
            if not linked_lessons and not path_entries_for_order:
                _issue(
                    diagnostics,
                    root,
                    concept["path"],
                    "backlink-missing",
                    "warning",
                    f"conceito lista a ordem {lesson_order} em aulas, mas nenhuma aula aprovada dessa ordem cita [[{slug}]]",
                    concept["fm"].lines.get("aulas"),
                    slug,
                )

    return sorted(
        diagnostics,
        key=lambda item: (item.path, item.line or 0, item.code, item.target or "", item.message),
    )


def _summary(diagnostics: Iterable[Diagnostic]) -> Dict[str, Any]:
    diagnostics = list(diagnostics)
    by_severity = Counter(item.severity for item in diagnostics)
    by_code = Counter(item.code for item in diagnostics)
    return {
        "total": len(diagnostics),
        "by_severity": {key: by_severity.get(key, 0) for key in ("error", "warning", "info")},
        "by_code": dict(sorted(by_code.items())),
    }


def main(argv: Optional[List[str]] = None) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument("--format", choices=("text", "json"), default="text")
    parser.add_argument("--fail-on", choices=("error", "warning", "info"), default="warning")
    args = parser.parse_args(argv)
    root = args.root.resolve()
    diagnostics = lint(root)
    summary = _summary(diagnostics)

    if args.format == "json":
        print(json.dumps({"summary": summary, "diagnostics": [d.as_dict() for d in diagnostics]}, ensure_ascii=False, indent=2))
    else:
        print(
            "wiki lint: "
            f"{summary['total']} achados "
            f"({summary['by_severity']['error']} erros, "
            f"{summary['by_severity']['warning']} avisos, "
            f"{summary['by_severity']['info']} informações)"
        )
        for diagnostic in diagnostics:
            location = diagnostic.path
            if diagnostic.line:
                location += f":{diagnostic.line}"
            print(f"{diagnostic.severity.upper()} [{diagnostic.code}] {location} — {diagnostic.message}")

    threshold = SEVERITY_RANK[args.fail_on]
    return 1 if any(SEVERITY_RANK[item.severity] >= threshold for item in diagnostics) else 0


if __name__ == "__main__":
    raise SystemExit(main())
