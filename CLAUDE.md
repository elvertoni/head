# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Repo Is

Content acervo for Prof. Toni Coimbra (Curso Técnico em Desenvolvimento de Sistemas, SEED-PR). Implements a lake→warehouse pipeline: raw sources → concept wiki → canonical lessons → rendered outputs.

```
lake/          raw sources (transcripts, PDFs, Notion dumps) — never LLM-edit
conceitos/     atomic concept wiki nodes
aulas/         canonical lessons (warehouse, source of truth)
tools/         CLI scripts
hermes/        skills for the Quíron agent (Hermes Agent on VPS) — versioned here, deployed via git pull + copy to ~/.hermes/skills/
```

## Commands

```powershell
# Validate manifesto.json matches aulas/ state
python tools/gerar_manifesto.py --check

# Regenerate manifesto.json after any aula add/approve/change
python tools/gerar_manifesto.py

# Transcribe audio/video to lake/ (faster-whisper, local; GPU preferred, CPU fallback)
# Positional <video> first, then --flags. Wrapper runs transcrever.py in tools/transcrever/.venv.
.\tools\transcrever\transcrever.ps1 "C:\videos\aula.mp4" --disciplina inteligencia-artificial --fonte ia-coders --titulo "MCP na prática"

# Sync Notion pages to lake/ (raw dump)
python tools/notion-wiki/puxar_notion.py

# Push the approved-lesson index to the Notion "Aulas" base (one-way, repo → Notion)
# Needs $env:NOTION_TOKEN. Run gerar_manifesto.py first — this reads manifesto.json.
python tools/sync_notion.py --dry-run   # plan only
python tools/sync_notion.py             # apply (create/update)
python tools/sync_notion.py --prune     # apply + archive orphan rows
```

`tools/sync_notion.py` mirrors the lesson **index** (metadata + ProfessorDash link, no body) into the `Aulas` database of the "Toni's Brain" Notion workspace, keyed on the `Caminho` property. Strictly one-way — Notion is a read-only projection of `canonica.md`, never an input. Requires an internal Notion integration token in `NOTION_TOKEN` and the `Aulas` + `Projetos` bases shared with that integration.

`tools/imagen-generator/` is **not a script**. Its `prompt.xml` is the v6 source of truth for unbranded lesson base art, split into two profiles — `capa` (dense, 3:2, the portal-facing cover) and `infografico` (sparse, 16:9, a body figure teaching one concept). The v6 density rules were derived from an audit of the 54 approved images already in the acervo, and its `R3` rule catalogs 12 defects that have actually shipped. **Images are generated here, by delegating the composed prompt to the Codex CLI's native image tool** (verified 2026-07-29). The browser Project (ChatGPT web) remains a valid fallback. Either way, Claude Code composes the fully-resolved v6 prompt and audits the returned PNG — handing the model the raw XML and letting it interpret the design system produces light backgrounds and occupied corners. Read `.claude/skills/gerar-imagem-aula/SKILL.md` first. Never attach the logo to the image model: Photoshop later applies the official logo, course identifier, and canonical canvas through a deterministic action. No CLI entrypoint.

## Architecture

### 4-Layer Pipeline

| Layer | Path | Role |
|---|---|---|
| Lake | `lake/{disciplina}/` | Immutable raw sources (`status: bruto`) |
| Conceitos | `conceitos/{disciplina}/{slug}.md` | Atomic wiki nodes; LLM reads, humans approve |
| Aulas | `aulas/{disciplina}/{trilha}/{NN-slug}/canonica.md` | Canonical lesson — **single source of truth** |
| Saídas | `aulas/**/{NN-slug}/saidas/` | Generated artifacts (HTML, PDF) — not git-versioned, always regenerable |

### Lesson Path Convention

`aulas/{disciplina}/{trilha}/{NN-slug}/canonica.md` where `NN` (zero-padded 2-digit) **must match** `ordem` in the lesson's frontmatter and in `manifesto.json`. A lesson folder holds `canonica.md`, `imagens.md` (image brief — always generated, Toni's rule), and `capa.png`.

### Current vault state (8 disciplines)

Not all disciplines are at the same stage. The manifesto is the source of truth for what's importable. Don't confuse presence of `lake/` source with a ready lesson. As of 2026-08-18, `python tools/gerar_manifesto.py --check` validates 77 approved importable lessons.

| Disciplina | Trilha | State |
|---|---|---|
| `inteligencia-artificial` | `fundamentos-de-ia` | aulas 1-25 aprovadas + 37-node concept graph |
| `introducao-a-computacao` | `arquitetura-computadores-e-sistemas-operacionais` | aulas 23-38 aprovadas |
| `analise-e-metodos-para-sistemas` | `metodologias-ageis` | aulas 33-41 + 53-54 aprovadas (Scrum/agilidade, Kanban) |
| `tcc` | `blueprint-tcc` | aulas 1-9 aprovadas (blueprints de TCC em canônica) |
| `analise-e-projeto-de-sistemas` | `marketing-digital` | aulas 25-30 aprovadas |
| `analise-e-projeto-de-sistemas` | `analise-de-requisitos` | aula 31 aprovada (engenharia reversa de app) |
| `programacao-front-end` | `controle-de-versao-git-github` | aulas 2-6 aprovadas + `atividades/` (apoio impresso, fora do manifesto) |
| `programacao-front-end` | `fundamentos-html-css` | aula 1 aprovada |
| `introducao-a-computacao` | `nivelamento-e-retomada` | aulas 1-2 aprovadas |
| `programacao-no-desenvolvimento-de-sistemas` | `arquitetura-e-fluxo-de-sistemas` | aula 1 aprovada (o que acontece quando você aperta Enter) |
| `programacao-front-end` | `projeto petfinder` | **HTML-only** (9 `.html` files), no `canonica.md` — apoio/saída, NOT importable |
| `programacao-no-desenvolvimento-de-sistemas` | `blueprint-tcc` | HTML apoio only — the canonical versions of these blueprints live under `tcc/blueprint-tcc` |
| `inovacao-tecnologia-e-empreendedorismo` | — | no canonical lessons yet |

Concept graph (`conceitos/`) holds 1028 nodes, concentrated in the two pós-graduação ingestions: `inovacao-inteligencia-artificial-e-robotica-educacional` (523) and `desenvolvimento-full-stack-e-cloud-computing` (466), plus `inteligencia-artificial` (37) and `inovacao-tecnologia-e-empreendedorismo` (2). Only `inteligencia-artificial` nodes are currently wired into approved lessons via `[[slug]]`.

### manifesto.json

Machine-generated index (`tools/gerar_manifesto.py`). **Never hand-edit.** Only lessons with `status: aprovada` appear in `lessons[]`. ProfessorDash portal reads this file as its import contract.

`conceitos[]` carries `{slug, nome, disciplina}` for every non-obsolete node in `conceitos/`. The portal resolves `[[slug]]` wikilinks in lessons through it — slugs have no accents, so deriving the label from the slug would show the student "aprendizado de maquina". Prefer `[[slug|rótulo]]` in lessons; the map is the fallback for bare links.

## Key Invariants

1. **Canonica is SOT** — all exports (HTML, portal import, PDF) derive from `canonica.md`; never edit outputs directly.
2. **Manifesto regeneration** — run `python tools/gerar_manifesto.py` after every aula add, status change, or frontmatter edit.
3. **Version bump** — every edit to a published (`status: aprovada`) lesson must increment `versao` or advance `atualizado_em`.
4. **Lake immutability** — LLM never edits files under `lake/`; only reads for source material.
5. **Portal frontmatter contract** — `titulo`, `disciplina`, `trilha`, `ordem`, `slug`, `status`, `versao`, `atualizado_em` must be complete for ProfessorDash import.

## Skills

| Skill | Trigger | What it does |
|---|---|---|
| `prof-toni` | Creating/planning lessons | Produces `canonica.md` following the spec protocol (read `.claude/skills/prof-toni/spec/00-PROTOCOLO.md` first) |
| `aula-estatica` | Rendering lessons | Converts `canonica.md` → standalone `.html` (dark/light, A4-print) |
| `gerar-imagem-aula` | Lesson images | Picks the profile (`capa` 3:2 / `infografico` 16:9), composes the v6 prompt, generates via Codex (or hands the prompt to the browser Project), then audits the returned PNG against the 12 known defects (upper corners empty, branding external) |

Skills live in `.claude/skills/`. Do not bypass `prof-toni` for lesson creation or `gerar-imagem-aula` for visual generation. The 7-point rubrica in `.claude/skills/prof-toni/spec/02-RUBRICA.md` is an approval gate.

`hermes/skills/prof-toni/` holds separate skills (`operar-acervo`, `alimentar-cerebro`) for the Quíron agent that operates this acervo from a VPS — not Claude Code skills; see `hermes/README.md`.

## Concept Wiki

`conceitos/` uses Karpathy llm-wiki pattern. Key files:
- `conceitos/index.md` — regenerable catalog (one line per concept)
- `conceitos/log.md` — append-only audit log; never rewrite entries

Frontmatter required fields: `conceito`, `slug`, `disciplina`, `tipo` (`conceito|entidade|sintese`), `status` (`vivo|rascunho|obsoleto`).

Aulas reference concepts via `[[slug]]` wikilinks. Backlink sync checked by lint workflow described in `AGENTS.md §4`.

## Memory

Durable project memory lives in **ai-memory** (MCP), not in local files.

**Read before you write.** Call `memory_query` before proposing architecture, before re-deriving a decision that may already exist, and before telling the user you don't know something about this project. Call `memory_recent` at session start when no handoff arrived. Storing memory nobody reads is wasted disk — the retrieval side is the one that has to be deliberate.

Write with `memory_write_page`, choosing the path by kind: `decisions/` for architectural calls (pinned, ADR shape), `_rules/` for standing rules, plus `gotchas/`, `notes/`, `procedures/`, `concepts/`. Do **not** duplicate what this file, `AGENTS.md`, or `manifesto.json` already document — memory that mirrors the repo rots and then contradicts it.

The legacy file store at `~/.claude/projects/C--PROJETOS-PROF-TONI/memory/` is **frozen**: read-only history, never add to it.

## Git

Remote uses SSH dual-account setup. This repo → `elvertoni` account (not `tonicoimbra`). Commits go straight to `main` — no PR flow in this acervo. See ai-memory page `_rules/git-ssh-duas-contas.md` for SSH config details.
