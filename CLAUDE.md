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
```

`tools/imagen-generator/` is **not a script** — it's a prompt bundle (`prompt.xml` + official logo + `LEIA-ME`) fed to an external image GPT to produce lesson cover/infographic PNGs. No CLI entrypoint.

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

Not all disciplines are at the same stage. The manifesto is the source of truth for what's importable. Don't confuse presence of `lake/` source with a ready lesson. As of 2026-07-23, `python tools/gerar_manifesto.py --check` validates 67 approved importable lessons.

| Disciplina | Trilha | State |
|---|---|---|
| `inteligencia-artificial` | `fundamentos-de-ia` | 25 aulas aprovadas + 35-node concept graph |
| `analise-e-metodos-para-sistemas` | `metodologias-ageis` | aulas 33-41 aprovadas (Scrum/agilidade) |
| `analise-e-projeto-de-sistemas` | `marketing-digital` | aulas 25-30 aprovadas |
| `introducao-a-computacao` | `nivelamento-e-retomada` | aulas 1-2 aprovadas |
| `introducao-a-computacao` | `arquitetura-computadores-e-sistemas-operacionais` | aulas 23-38 aprovadas |
| `tcc` | `blueprint-tcc` | aulas 1-9 aprovadas (blueprints de TCC em canônica) |
| `programacao-front-end` | `projeto petfinder` | **HTML-only** (9 `.html` files), no `canonica.md` — apoio/saída, NOT importable |
| `programacao-no-desenvolvimento-de-sistemas` | `blueprint-tcc` | HTML apoio only — the canonical versions of these blueprints live under `tcc/blueprint-tcc` |
| `inovacao-tecnologia-e-empreendedorismo` | — | no canonical lessons yet |

Concept graph (`conceitos/`) currently only populated for `inteligencia-artificial`.

### manifesto.json

Machine-generated index (`tools/gerar_manifesto.py`). **Never hand-edit.** Only lessons with `status: aprovada` appear in `lessons[]`. ProfessorDash portal reads this file as its import contract.

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

Skills live in `.claude/skills/` and read their `spec/` subfolder for anatomy, rubrica, and examples. Do not bypass them for lesson creation — the 7-point rubrica in `.claude/skills/prof-toni/spec/02-RUBRICA.md` is an approval gate.

`hermes/skills/prof-toni/` holds separate skills (`operar-acervo`, `alimentar-cerebro`) for the Quíron agent that operates this acervo from a VPS — not Claude Code skills; see `hermes/README.md`.

## Concept Wiki

`conceitos/` uses Karpathy llm-wiki pattern. Key files:
- `conceitos/index.md` — regenerable catalog (one line per concept)
- `conceitos/log.md` — append-only audit log; never rewrite entries

Frontmatter required fields: `conceito`, `slug`, `disciplina`, `tipo` (`conceito|entidade|sintese`), `status` (`vivo|rascunho|obsoleto`).

Aulas reference concepts via `[[slug]]` wikilinks. Backlink sync checked by lint workflow described in `AGENTS.md §4`.

## Git

Remote uses SSH dual-account setup. This repo → `elvertoni` account (not `tonicoimbra`). See memory `git-ssh-duas-contas.md` for SSH config details.
