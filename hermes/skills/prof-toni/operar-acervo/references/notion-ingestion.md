# Notion ingestion — tool internals

## How it works

`puxar_notion.py` hits the unofficial Notion API:
- Endpoint: `https://www.notion.so/api/v3/loadPageChunk`
- Method: POST
- No authentication (public pages only)
- Page ID: extracted from URL as 32-char hex (dashes stripped)

## Page ID extraction

URL formats that work:
- `https://<workspace>.notion.site/<Titulo-da-Pagina>-0123456789abcdef0123456789abcdef`
- `0123456789abcdef0123456789abcdef`
- `01234567-89ab-cdef-0123-456789abcdef`

The tool regexes `[0-9a-fA-F]{32}` from input.

## Output format

Each page becomes a `.md` with YAML frontmatter:

```yaml
---
titulo: <page title>
tipo: referencia-externa
fonte: Elite Wiki (Notion publico)
page_id: <uuid>
status: bruto
---
```

Block types rendered: header, sub_header, sub_sub_header, text, bulleted_list,
numbered_list, to_do, toggle, quote, callout, code (with language), divider,
image, page (as wikilink).

## Rate limiting

- 0.8s sleep between pages
- 0.2s between cursor pagination chunks
- Retry with exponential backoff (2s → 30s max) on 429/5xx
- Max 6 retries per request
- Respeita `Retry-After` header when present

## _reorganizar.py MAP

The MAP dict in `tools/notion-wiki/_reorganizar.py` maps basename→target folder.
When a file appears there, it means it was already ingested (likely on the
Windows machine). Use this as a dedup check before re-ingesting.

Current taxonomy (Elite Wiki):
- fundamentos/ — short didactic concepts
- prompts/ — prompt libraries and exemplars
- agentes/ + agentes/encontros-elite/ — agent patterns
- arquitetura/ — system blueprints
- skills-ferramentas/ + skills-ferramentas/imersao-skills/ — tool setups
- workflows/ — development workflows
- _indice/ — navigation maps from Notion
- _descartar/ — trash (untitled pages)
