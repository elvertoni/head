#!/usr/bin/env python
"""Ingere uma wiki publica do Notion (.notion.site) para markdown no lake.

Usa a API publica nao-oficial (sem auth, so paginas publicas):
    loadPageChunk      blocos de uma pagina
    syncRecordValues   blocos avulsos por id (filhos de toggle, links externos)

Dois modos:
    --index            mapeia a arvore (titulos) ate --depth, sem baixar
    (default)          baixa cada pagina como .md em --saida

O loadPageChunk sozinho perde conteudo em dois pontos, ambos tratados aqui:
  - filhos de toggle: os ids vem declarados em content[] mas os blocos nao vem
    na resposta. Sem buscar, uma pagina de 200 KB rende 900 chars.
  - links: viram o marcador '‣' sem destino. Tres formas — eoi e p precisam de
    fetch, lm ja traz href embutido.

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
SYNC = "https://www.notion.so/api/v3/syncRecordValues"
HEADERS = {"Content-Type": "application/json", "User-Agent": "Mozilla/5.0"}

# caches de resolucao de link (o Notion so devolve o marcador '‣' no texto)
EOI_URLS: dict[str, str] = {}       # external_object_instance -> url
PAGE_TITULOS: dict[str, str] = {}   # mencao a pagina -> titulo

# console do Windows usa cp1252 e estoura em travessao/seta dos titulos do Notion
for _stream in (sys.stdout, sys.stderr):
    if hasattr(_stream, "reconfigure"):
        _stream.reconfigure(encoding="utf-8", errors="replace")


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


def _post(body: bytes, url: str = API, tentativas: int = 6) -> dict:
    """POST com retry e backoff exponencial em 429 / 5xx."""
    espera = 2.0
    for i in range(tentativas):
        req = urllib.request.Request(url, data=body, headers=HEADERS)
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


def fetch_blocks(ids) -> dict:
    """Busca blocos avulsos por id via syncRecordValues.

    O loadPageChunk devolve o bloco `toggle` e declara os ids dos filhos em
    `content[]`, mas nao inclui esses filhos na resposta. Esta funcao os busca.
    Serve tambem para os registros `external_object_instance` (links externos).
    """
    out: dict = {}
    ids = list(ids)
    for i in range(0, len(ids), 30):
        lote = ids[i:i + 30]
        body = json.dumps({"requests": [
            {"pointer": {"table": "block", "id": x}, "version": -1} for x in lote
        ]}).encode()
        data = _post(body, SYNC)
        for bid, rec in data.get("recordMap", {}).get("block", {}).items():
            v = rec.get("value", {})
            v = v.get("value", v)
            if v:
                out[bid] = v
        time.sleep(0.4)
    return out


def _resolver_links(blocks: dict) -> None:
    """Resolve os destinos dos links citados nos blocos.

    O Notion representa link no texto como o marcador '‣' e guarda o destino
    na anotacao. Sem resolver, todo link vira um simbolo mudo. Tres formas:
      eoi  registro externo, precisa de fetch (url em format.original_url)
      p    mencao a outra pagina, precisa de fetch (queremos o titulo)
      lm   link mention, ja traz href/title embutidos — resolvido em rich()
    """
    pendentes = set()
    for b in blocks.values():
        for seg in (b.get("properties") or {}).get("title", []):
            if len(seg) > 1 and seg[1]:
                for ann in seg[1]:
                    if not ann or len(ann) < 2 or not isinstance(ann[1], str):
                        continue
                    if ann[0] == "eoi" and ann[1] not in EOI_URLS:
                        pendentes.add(ann[1])
                    elif ann[0] == "p" and ann[1] not in PAGE_TITULOS:
                        pendentes.add(ann[1])
    if not pendentes:
        return
    for bid, v in fetch_blocks(pendentes).items():
        url = (v.get("format") or {}).get("original_url")
        if url:
            EOI_URLS[bid] = url
            continue
        titulo = rich(v.get("properties"))
        if titulo:
            PAGE_TITULOS[bid] = titulo


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

    # busca em cascata os filhos declarados mas nao devolvidos (toggle, colunas).
    # um filho pode ter filhos proprios, entao repete ate fechar.
    for _ in range(10):  # teto de seguranca
        faltando = {c for b in blocks.values() for c in (b.get("content") or [])
                    if c not in blocks and c != page_id}
        if not faltando:
            break
        novos = fetch_blocks(faltando)
        if not novos:
            break  # nao resolveu nenhum; evita loop infinito
        blocks.update(novos)

    _resolver_links(blocks)
    return blocks


def rich(props: dict | None, key: str = "title") -> str:
    if not props or key not in props:
        return ""
    out = []
    for seg in props[key]:
        if not (seg and isinstance(seg, list)):
            out.append("")
            continue
        texto = seg[0]
        # link: o texto e so o marcador '‣'; troca pelo destino resolvido
        for ann in (seg[1] if len(seg) > 1 and seg[1] else []):
            if not ann or len(ann) < 2:
                continue
            if ann[0] == "eoi" and isinstance(ann[1], str):
                texto = EOI_URLS.get(ann[1], texto)
            elif ann[0] == "p" and isinstance(ann[1], str):
                titulo = PAGE_TITULOS.get(ann[1])
                # sem titulo (pagina privada ou removida): guarda ao menos a URL
                texto = f"[[{titulo}]]" if titulo else \
                    f"https://notion.so/{ann[1].replace('-', '')}"
            elif ann[0] == "lm" and isinstance(ann[1], dict):
                # link mention ja traz tudo embutido, sem chamada extra
                href = ann[1].get("href")
                if href:
                    rotulo = ann[1].get("title") or href
                    texto = f"[{rotulo}]({href})"
        out.append(texto)
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


LISTAS = {"bulleted_list", "numbered_list", "to_do"}


def render_md(page_id: str, blocks: dict) -> str:
    """Converte os blocos de uma pagina em markdown."""
    page = blocks.get(page_id, {})
    linhas = [f"# {title_of(page)}", ""]
    _render(page.get("content", []), blocks, linhas, "")
    return "\n".join(linhas).strip() + "\n"


def _render(ids: list, blocks: dict, linhas: list, ident: str) -> None:
    """Emite os blocos de um nivel e recursa nos filhos.

    Lista indenta os filhos; toggle nao — o conteudo dele costuma ser bloco de
    codigo, e indentar quebraria a cerca ```.
    """
    num = 0
    for cid in ids:
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
            linhas.append(f"{ident}- {txt}")
        elif t == "numbered_list":
            num += 1
            linhas.append(f"{ident}{num}. {txt}")
        elif t == "to_do":
            chk = "x" if (b.get("properties", {}).get("checked", [["No"]])[0][0] == "Yes") else " "
            linhas.append(f"{ident}- [{chk}] {txt}")
        elif t == "toggle":
            linhas += [f"{ident}- {txt}"]
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
            linhas += [f"{ident}- [[{title_of(b)}]]  (subpagina)"]
        else:
            if txt:
                linhas += [txt, ""]
        if t not in ("numbered_list",):
            num = 0

        # subpagina nao entra inline: walk_dump a salva em arquivo proprio
        filhos = b.get("content") or []
        if filhos and t not in PAGE_TYPES:
            _render(filhos, blocks, linhas, ident + "  " if t in LISTAS else ident)


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
