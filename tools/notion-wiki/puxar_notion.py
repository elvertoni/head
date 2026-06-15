#!/usr/bin/env python
"""Ingere uma wiki publica do Notion (.notion.site) para markdown no lake.

Usa a API publica nao-oficial loadPageChunk (sem auth, so paginas publicas).
Dois modos:
    --index            mapeia a arvore (titulos) ate --depth, sem baixar
    (default)          baixa cada pagina como .md em --saida

Uso:
    python puxar_notion.py <page_id_ou_url> --index --depth 2
    python puxar_notion.py <page_id_ou_url> --saida ../../lake/inteligencia-artificial/elite-wiki --depth 3
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
import unicodedata
import urllib.request
from pathlib import Path

API = "https://www.notion.so/api/v3/loadPageChunk"
HEADERS = {"Content-Type": "application/json", "User-Agent": "Mozilla/5.0"}


def to_uuid(s: str) -> str:
    s = s.strip()
    m = re.search(r"([0-9a-fA-F]{32})", s.replace("-", ""))
    if not m:
        raise SystemExit(f"[erro] nao achei um page id em: {s}")
    h = m.group(1).lower()
    return f"{h[0:8]}-{h[8:12]}-{h[12:16]}-{h[16:20]}-{h[20:32]}"


def slugify(t: str) -> str:
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode()
    t = re.sub(r"[^\w\s-]", "", t).strip().lower()
    return re.sub(r"[\s_-]+", "-", t) or "pagina"


def _post(body: bytes, tentativas: int = 6) -> dict:
    """POST com retry e backoff exponencial em 429 / 5xx."""
    espera = 2.0
    for i in range(tentativas):
        req = urllib.request.Request(API, data=body, headers=HEADERS)
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.loads(r.read())
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503, 504) and i < tentativas - 1:
                ra = e.headers.get("Retry-After")
                pausa = float(ra) if ra and ra.isdigit() else espera
                print(f"  [rate-limit {e.code}] aguardando {pausa:.0f}s...", flush=True)
                time.sleep(pausa)
                espera = min(espera * 2, 30)
                continue
            raise
    raise SystemExit("[erro] falhou apos varias tentativas (rate limit).")


def load_chunk(page_id: str) -> dict:
    """Busca todos os blocos de uma pagina (com paginacao por cursor)."""
    time.sleep(0.8)  # ritmo polido entre paginas (evita 429)
    blocks: dict = {}
    cursor = {"stack": []}
    for _ in range(40):  # teto de seguranca
        body = json.dumps({
            "pageId": page_id, "limit": 100, "cursor": cursor,
            "chunkNumber": 0, "verticalColumns": False,
        }).encode()
        data = _post(body)
        for bid, rec in data.get("recordMap", {}).get("block", {}).items():
            v = rec.get("value", {}).get("value") or rec.get("value")
            if v:
                blocks[bid] = v
        cursor = data.get("cursor", {})
        if not cursor.get("stack"):
            break
        time.sleep(0.2)
    return blocks


def rich(props: dict | None, key: str = "title") -> str:
    if not props or key not in props:
        return ""
    out = []
    for seg in props[key]:
        out.append(seg[0] if seg and isinstance(seg, list) else "")
    return "".join(out)


def title_of(block: dict) -> str:
    return rich(block.get("properties")) or "(sem titulo)"


PAGE_TYPES = {"page", "collection_view_page"}


def page_refs_in(block: dict) -> list[tuple[str, str]]:
    """Extrai (titulo, page_id) de links inline (mencao 'p' ou URL notion.so) no rich text."""
    refs: list[tuple[str, str]] = []
    for seg in (block.get("properties") or {}).get("title", []):
        if len(seg) > 1 and seg[1]:
            for ann in seg[1]:
                if not ann:
                    continue
                if ann[0] == "p" and len(ann) > 1:
                    refs.append((seg[0], ann[1]))
                elif ann[0] == "a" and len(ann) > 1 and "notion.so" in ann[1]:
                    refs.append((seg[0], ann[1]))
    return refs


def child_pages(page_id: str, blocks: dict) -> list[tuple[str, str]]:
    """Subpaginas de uma pagina: blocos-pagina + links inline. Dedup por uuid."""
    out: list[tuple[str, str]] = []
    seen: set[str] = set()
    page = blocks.get(page_id, {})
    for cid in page.get("content", []):
        b = blocks.get(cid)
        if not b:
            continue
        cands: list[tuple[str, str]] = []
        if b.get("type") in PAGE_TYPES:
            cands.append((title_of(b), cid))
        cands += page_refs_in(b)
        for titulo, target in cands:
            try:
                u = to_uuid(target)
            except SystemExit:
                continue
            if u in seen or u == page_id:
                continue
            seen.add(u)
            rotulo = titulo.strip() if titulo.strip() and titulo.strip() != "‣" else None
            out.append((rotulo, u))
    return out


def render_md(page_id: str, blocks: dict) -> str:
    """Converte os blocos de uma pagina em markdown."""
    page = blocks.get(page_id, {})
    linhas = [f"# {title_of(page)}", ""]
    num = 0
    for cid in page.get("content", []):
        b = blocks.get(cid)
        if not b:
            continue
        t = b.get("type")
        txt = rich(b.get("properties"))
        if t in ("header",):
            linhas += [f"## {txt}", ""]
        elif t in ("sub_header",):
            linhas += [f"### {txt}", ""]
        elif t in ("sub_sub_header",):
            linhas += [f"#### {txt}", ""]
        elif t == "text":
            linhas += [txt, ""] if txt else [""]
        elif t == "bulleted_list":
            linhas.append(f"- {txt}")
        elif t == "numbered_list":
            num += 1
            linhas.append(f"{num}. {txt}")
        elif t == "to_do":
            chk = "x" if (b.get("properties", {}).get("checked", [["No"]])[0][0] == "Yes") else " "
            linhas.append(f"- [{chk}] {txt}")
        elif t == "toggle":
            linhas += [f"- {txt}"]
        elif t == "quote":
            linhas += [f"> {txt}", ""]
        elif t == "callout":
            linhas += [f"> {txt}", ""]
        elif t == "code":
            lang = rich(b.get("properties"), "language") or ""
            linhas += [f"```{lang.lower()}", txt, "```", ""]
        elif t == "divider":
            linhas += ["---", ""]
        elif t in ("image",):
            src = (b.get("properties", {}).get("source", [[""]])[0][0])
            if src:
                linhas += [f"![imagem]({src})", ""]
        elif t in PAGE_TYPES:
            linhas += [f"- [[{title_of(b)}]]  (subpagina)"]
        else:
            if txt:
                linhas += [txt, ""]
        if t not in ("numbered_list",):
            num = 0
    return "\n".join(linhas).strip() + "\n"


def walk_index(page_id: str, depth: int, prefix: str = "", seen: set | None = None,
               rotulo: str | None = None) -> None:
    seen = seen if seen is not None else set()
    if page_id in seen or depth < 0:
        return
    seen.add(page_id)
    blocks = load_chunk(page_id)
    nome = rotulo or title_of(blocks.get(page_id, {}))
    filhos = child_pages(page_id, blocks)
    print(f"{prefix}{nome}  ({len(filhos)} subpag.)" if filhos else f"{prefix}{nome}")
    if depth > 0:
        for rot, cid in filhos:
            walk_index(cid, depth - 1, prefix + "  ", seen, rot)


def walk_dump(page_id: str, depth: int, saida: Path, seen: set | None = None,
              rotulo: str | None = None) -> int:
    seen = seen if seen is not None else set()
    if page_id in seen or depth < 0:
        return 0
    seen.add(page_id)
    blocks = load_chunk(page_id)
    titulo = rotulo or title_of(blocks.get(page_id, {}))
    md = render_md(page_id, blocks)
    saida.mkdir(parents=True, exist_ok=True)
    arq = saida / f"{slugify(titulo)}.md"
    fm = ("---\n"
          f"titulo: {titulo}\n"
          "tipo: referencia-externa\n"
          "fonte: Elite Wiki (Notion publico)\n"
          f"page_id: {page_id}\n"
          "status: bruto\n"
          "---\n\n")
    arq.write_text(fm + md, encoding="utf-8")
    print(f"[ok] {arq.relative_to(saida.parents[0]) if saida.parents else arq.name}", flush=True)
    n = 1
    if depth > 0:
        for rot, cid in child_pages(page_id, blocks):
            n += walk_dump(cid, depth - 1, saida / slugify(titulo), seen, rot)
    return n


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("page", help="id ou URL da pagina raiz do Notion publico")
    p.add_argument("--index", action="store_true", help="so mapeia a arvore (nao baixa)")
    p.add_argument("--depth", type=int, default=2, help="profundidade de recursao (default 2)")
    p.add_argument("--saida", default=None, help="pasta de saida (modo dump)")
    args = p.parse_args()

    pid = to_uuid(args.page)
    if args.index:
        walk_index(pid, args.depth)
    else:
        if not args.saida:
            raise SystemExit("[erro] modo dump exige --saida")
        total = walk_dump(pid, args.depth, Path(args.saida).resolve())
        print(f"\n[fim] {total} paginas salvas em {args.saida}")


if __name__ == "__main__":
    main()
