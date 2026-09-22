"""Leitura compartilhada da wiki de conceitos.

O vault usa um subconjunto pequeno de YAML no frontmatter. Este parser aceita
somente esse subconjunto (escalares, listas inline e listas em bloco), sem
executar tags ou estruturas arbitrárias. Isso mantém as ferramentas da wiki
stdlib-only e previsíveis.
"""
from __future__ import annotations

import ast
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, Iterator, List, Optional, Sequence, Tuple


CONCEPT_FIELDS = (
    "conceito",
    "slug",
    "disciplina",
    "tipo",
    "aka",
    "status",
    "fontes",
    "aulas",
    "atualizado_em",
)
CONCEPT_TYPES = {"conceito", "entidade", "sintese"}
CONCEPT_STATUSES = {"vivo", "rascunho", "obsoleto"}
REQUIRED_SECTIONS = (
    "Em uma frase",
    "O que precisa saber",
    "Erros comuns",
    "Onde aparece",
    "Fontes",
)
WIKILINK_RE = re.compile(r"\[\[([^\]\n]+)\]\]")


@dataclass
class Frontmatter:
    data: Dict[str, Any]
    lines: Dict[str, int]
    errors: List[Tuple[str, int, str]]
    end_index: Optional[int]


@dataclass(frozen=True)
class Diagnostic:
    code: str
    severity: str
    path: str
    line: Optional[int]
    message: str
    target: Optional[str] = None

    def as_dict(self) -> Dict[str, Any]:
        return {
            "code": self.code,
            "severity": self.severity,
            "path": self.path,
            "line": self.line,
            "target": self.target,
            "message": self.message,
        }


def _split_inline_items(value: str) -> List[str]:
    """Divide uma lista YAML simples respeitando aspas e colchetes."""
    result: List[str] = []
    current: List[str] = []
    quote: Optional[str] = None
    escaped = False
    depth = 0

    for char in value:
        if escaped:
            current.append(char)
            escaped = False
            continue
        if char == "\\" and quote:
            current.append(char)
            escaped = True
            continue
        if quote:
            current.append(char)
            if char == quote:
                quote = None
            continue
        if char in ("'", '"'):
            quote = char
            current.append(char)
        elif char == "[":
            depth += 1
            current.append(char)
        elif char == "]":
            depth = max(0, depth - 1)
            current.append(char)
        elif char == "," and depth == 0:
            result.append("".join(current).strip())
            current = []
        else:
            current.append(char)
    result.append("".join(current).strip())
    return [item for item in result if item]


def _parse_scalar(value: str) -> Any:
    value = value.strip()
    if not value:
        return ""
    if value in {"[]", "[ ]"}:
        return []
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1].strip()
        return [_parse_scalar(item) for item in _split_inline_items(inner)] if inner else []
    if value in {"null", "Null", "NULL", "~"}:
        return None
    if value.lower() == "true":
        return True
    if value.lower() == "false":
        return False
    if re.fullmatch(r"-?\d+", value):
        return int(value)
    if len(value) >= 2 and value[0] == value[-1] and value[0] in ("'", '"'):
        try:
            return ast.literal_eval(value)
        except (SyntaxError, ValueError):
            return value[1:-1]
    return value


def parse_frontmatter(text: str) -> Frontmatter:
    """Lê o frontmatter restrito do vault e preserva linhas para diagnósticos."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return Frontmatter({}, {}, [("frontmatter-missing", 1, "bloco YAML ausente")], None)

    end_index: Optional[int] = None
    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            end_index = index
            break
    errors: List[Tuple[str, int, str]] = []
    if end_index is None:
        errors.append(("frontmatter-unclosed", len(lines), "bloco YAML sem fechamento '---'"))
        end_index = len(lines)

    data: Dict[str, Any] = {}
    field_lines: Dict[str, int] = {}
    index = 1
    while index < end_index:
        raw = lines[index]
        stripped = raw.strip()
        if not stripped or stripped.startswith("#"):
            index += 1
            continue
        if raw[0].isspace() or stripped.startswith("-"):
            index += 1
            continue
        match = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", raw)
        if not match:
            errors.append(("frontmatter-line", index + 1, f"linha não reconhecida: {stripped}"))
            index += 1
            continue

        key, value = match.group(1), match.group(2).strip()
        if key in data:
            errors.append(("frontmatter-duplicate", index + 1, f"chave duplicada: {key}"))
        field_lines.setdefault(key, index + 1)

        if value:
            data[key] = _parse_scalar(value)
            index += 1
            continue

        items: List[Any] = []
        cursor = index + 1
        while cursor < end_index:
            child = lines[cursor]
            child_match = re.match(r"^\s*-\s*(.*)$", child)
            if child_match:
                items.append(_parse_scalar(child_match.group(1)))
                cursor += 1
                continue
            if not child.strip():
                cursor += 1
                continue
            if child[0].isspace():
                # Estruturas aninhadas não fazem parte do contrato da wiki.
                cursor += 1
                continue
            break
        data[key] = items
        index = cursor

    return Frontmatter(data, field_lines, errors, end_index)


def body_lines(text: str, frontmatter: Frontmatter) -> Tuple[List[str], int]:
    lines = text.splitlines()
    if frontmatter.end_index is None:
        return lines, 1
    return lines[frontmatter.end_index + 1 :], frontmatter.end_index + 2


def extract_wikilinks(lines: Sequence[str], first_line: int = 1) -> Iterator[Tuple[str, int]]:
    """Retorna (slug, linha), ignorando blocos de código."""
    in_fence = False
    fence: Optional[str] = None
    for offset, line in enumerate(lines):
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
        for match in WIKILINK_RE.finditer(line):
            target = match.group(1).split("|", 1)[0].split("#", 1)[0].strip()
            if target:
                yield target, first_line + offset


def as_list(value: Any) -> List[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def concept_paths(root: Path) -> List[Path]:
    return sorted(
        path
        for path in (root / "conceitos").rglob("*.md")
        if path.name not in {"index.md", "log.md"}
    )


def lesson_paths(root: Path) -> List[Path]:
    return sorted((root / "aulas").rglob("canonica.md"))


def relative_path(root: Path, path: Path) -> str:
    return path.relative_to(root).as_posix()


def one_line_summary(text: str, frontmatter: Frontmatter) -> str:
    lines, _ = body_lines(text, frontmatter)
    for index, line in enumerate(lines):
        if re.match(r"^##\s+Em uma frase\s*$", line.strip(), re.I):
            for following in lines[index + 1 :]:
                if following.strip().startswith("#"):
                    break
                if following.strip():
                    return following.strip()
    paragraph: List[str] = []
    for line in lines:
        if line.strip().startswith("#"):
            break
        if line.strip():
            paragraph.append(line.strip())
    return " ".join(paragraph) or str(frontmatter.data.get("conceito", ""))


def format_aulas(value: Any) -> str:
    items = as_list(value)
    return ",".join(str(item) for item in items)
