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

# Audit concepts, wikilinks, backlinks and provenance (read-only)
python tools/lint_wiki.py
python tools/lint_wiki.py --format json
python tools/lint_wiki.py --fail-on error

# Check or regenerate the concept catalog
python tools/gerar_indice.py --check
python tools/gerar_indice.py --write

# Bootstrap the transcrever venv on a fresh machine:
#   cd tools\transcrever; uv venv --python 3.12; uv pip install -r requirements.txt

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

Git-ignored by design: `**/saidas/`, `aulas/**/atividades/*.pdf` (the `.html` is the editable source), `lake/**/elite-wiki/` and an explicit extension list of heavy `lake/` binaries (video, audio, PDF, Office, raw images — new formats are not covered until added to `.gitignore`), plus `graphify-out/`, `scratch/`, `.playwright-mcp/` and `.obsidian/`. A `lake/` discipline that looks empty in git usually holds local-only PDFs — check the filesystem before concluding there is no source material.

Provenance has three distinct roles: raw files in `lake/` are the source material and remain immutable; `lake/**/graphify-out/` is a derived Graphify extraction cache that may help recover or audit text but never replaces the missing raw source; `conceitos/`, `aulas/`, `tools/` and `docs/` are versioned operational or synthesized content. When the raw source is absent but a cache exists, keep the provenance gap explicit.

### Lesson Path Convention

`aulas/{disciplina}/{trilha}/{NN-slug}/canonica.md` where `NN` (zero-padded 2-digit) **must match** `ordem` in the lesson's frontmatter and in `manifesto.json`. A lesson folder holds `canonica.md`, `imagens.md` (image brief — always generated, Toni's rule), `capa.png`, and optionally `img/` for body figures.

`NN`/`ordem` is part of the portal's import key — renumbering a lesson already imported creates a duplicate row instead of updating it, leaving the old one published to classes. Renumbering a whole trilha means cleaning up on the portal side afterwards.

A file in `img/` only reaches the student if the canonica references it as `![alt](img/arquivo.png)`; an unreferenced file is imported and never shown. The `alt` carries the accessible description — write it from the brief, not from the filename.

### Canonica Body Vocabulary (closed catalogs)

A lesson body is not free Markdown — the portal and the apostila renderer only understand a fixed block set, specified in `.claude/skills/prof-toni/spec/01-CANONICA.md` §5–§7. Inventing a block type ships a lesson that renders as literal text to students.

- **Callouts (6, closed)** — `:::conceito`, `:::exemplo`, `:::importante`, `:::atencao`, `:::dica`, `:::curiosidade`; opened as `:::tipo Título`, closed with a bare `:::`.
- **`:::roteiro`** — teacher-only stage directions. ProfessorDash shows it in professor mode; the apostila **always** omits it, so it must never hold content the student needs.
- **Interactives (2, closed)** — fenced ```` ```quiz ```` and ```` ```diagrama-progressivo ````. Their bodies are **real YAML**: any text value containing `: ` (colon + space) or starting with a quote must be double-quoted, or the block fails to parse and the student sees raw YAML. Each **question** inside a quiz needs exactly one alternative with `correta: true` (a fence holds several questions — 244 across the 89 lessons). The portal marks *every* alternative carrying the key, so two make two right answers, and none degrades that question to a static list. Diagram `rotulo` must not carry its own number — the component numbers layers, so "1. Navegador" renders as "1 · 1. Navegador". Note the acervo drifted from this: ~186 layers in approved lessons are hand-numbered, so don't copy an existing lesson as the reference here. Code is a normal Markdown fence, not an interactive.
- A quiz's `feedback` is currently rendered by no output; keep writing it (the canonica is richer than any renderer), but never teach through it.

Usage today: 80 quizzes and 73 progressive diagrams across the 89 lessons — a regression in this contract is visible to classes.

### Current vault state (snapshot 2026-09-21)

Not all disciplines are at the same stage. The manifesto is the source of truth for what's importable. Don't confuse presence of `lake/` source with a ready lesson. As of 2026-09-21, `python tools/gerar_manifesto.py --check` validates **89** approved importable lessons.

| Disciplina | Trilha | State |
|---|---|---|
| `inteligencia-artificial` | `fundamentos-de-ia` | aulas 1-25 aprovadas (25) + 37-node concept graph |
| `introducao-a-computacao` | `arquitetura-computadores-e-sistemas-operacionais` | aulas 23-38 aprovadas (16) |
| `programacao-front-end` | `landing-page-mvp` | aulas 7-18 aprovadas (12) — startup/MVP até publicar e validar; 12 infográficos de miolo em `img/` |
| `analise-e-metodos-para-sistemas` | `metodologias-ageis` | aulas 33-41 + 53-54 aprovadas (11) (Scrum/agilidade, Kanban) |
| `tcc` | `blueprint-tcc` | aulas 1-9 aprovadas (9) (blueprints de TCC em canônica) |
| `analise-e-projeto-de-sistemas` | `marketing-digital` | aulas 25-30 aprovadas (6) |
| `programacao-front-end` | `controle-de-versao-git-github` | aulas 2-6 aprovadas (5) + `atividades/` (apoio impresso, fora do manifesto) |
| `introducao-a-computacao` | `nivelamento-e-retomada` | aulas 1-2 aprovadas (2) |
| `analise-e-projeto-de-sistemas` | `analise-de-requisitos` | aula 31 aprovada (1) (engenharia reversa de app) |
| `programacao-front-end` | `fundamentos-html-css` | aula 1 aprovada (1) |
| `programacao-no-desenvolvimento-de-sistemas` | `arquitetura-e-fluxo-de-sistemas` | aula 1 aprovada (1) (o que acontece quando você aperta Enter) |
| `programacao-front-end` | `projeto petfinder` | **HTML-only** (9 `.html` files), no `canonica.md` — apoio/saída, NOT importable |
| `programacao-no-desenvolvimento-de-sistemas` | `blueprint-tcc` | HTML apoio only — the canonical versions of these blueprints live under `tcc/blueprint-tcc` |
| `inovacao-tecnologia-e-empreendedorismo` | — | no canonical lessons yet |

Concept graph (`conceitos/`) holds cerca de 1.042 active nodes, concentrated in the two pós-graduação ingestions: `inovacao-inteligencia-artificial-e-robotica-educacional` and `desenvolvimento-full-stack-e-cloud-computing`, plus the smaller course-specific graphs. Approved lessons currently wire a small subset of concepts; use `python tools/lint_wiki.py` to see lesson coverage and missing backlinks rather than treating the ingestion reservoir as fully integrated.

### manifesto.json

Machine-generated index (`tools/gerar_manifesto.py`). **Never hand-edit.** Only lessons with `status: aprovada` appear in `lessons[]`. ProfessorDash portal reads this file as its import contract.

`conceitos[]` carries `{slug, nome, disciplina}` for every non-obsolete node in `conceitos/`. The portal resolves `[[slug]]` wikilinks in lessons through it — slugs have no accents, so deriving the label from the slug would show the student "aprendizado de maquina". Prefer `[[slug|rótulo]]` in lessons; the map is the fallback for bare links.

The generator's non-obvious behavior — read `tools/gerar_manifesto.py` before changing lesson or discipline metadata:

- **Identity comes from the path**; the frontmatter is validated against it. A disciplina/trilha/ordem/slug mismatch is reported as a divergence, never silently fixed.
- **`slug` must be unique across the whole vault**, not just inside its trilha — it is both the wikilink target and part of the portal key. The generator only *enforces* it among approved lessons (`vistos_slug` in `coletar()`), so a clash with a rascunho or a `conceitos/` node passes `--check` and still breaks wikilink resolution.
- **The frontmatter parser is deliberately minimal**: top-level scalar keys only, indented lines and list items skipped. Contract fields have to stay flat scalars.
- **The generator merges over the existing `manifesto.json` as its base.** `version`, `vault`, `descricao`, `arquitetura`, `series[]` and each discipline's `serie`/`status`/`lake`/`warehouse` are carried over from the file, and `disciplinas[]` only emits slugs that are already there. A brand-new discipline folder therefore yields lessons in `lessons[]` with no matching entry in `disciplinas[]` until its curated metadata is seeded — the one narrow exception to "never hand-edit".
- **Display labels are maintained** in `LABELS_DISCIPLINA` / `LABELS_TRILHA` inside `tools/gerar_manifesto.py`. Register a curated label there when creating a discipline or track; do not rely on a lesson title as the permanent track label.

`gerar_manifesto.py --check`, `lint_wiki.py` and `sync_notion.py --check` are the repo's automated validators. The wiki lint is read-only and reports findings; it never auto-fixes content. The repository has no CI (`.github/` does not exist), so run `python -m unittest discover -s tests -v` locally before committing tool changes.

## Key Invariants

1. **Canonica is SOT** — all exports (HTML, portal import, PDF) derive from `canonica.md`; never edit outputs directly.
2. **Manifesto regeneration** — run `python tools/gerar_manifesto.py` after every aula add, status change, or frontmatter edit.
3. **Version bump** — every edit to a published (`status: aprovada`) lesson must increment `versao` or advance `atualizado_em`.
4. **Lake immutability** — LLM never edits files under `lake/`; only reads for source material.
5. **Portal frontmatter contract** — `titulo`, `disciplina`, `trilha`, `ordem`, `slug`, `status`, `versao`, `atualizado_em` must be complete for ProfessorDash import.
6. **Publishing is four steps, in order** — `gerar_manifesto.py` → **push the acervo** → deploy the portal → **reimport with `--force`**. The portal reads a GitHub tarball, so pushing before deploying is what makes the new content visible; the reimport is what reprocesses lesson HTML. Skipping step 4 leaves the portal silently behind with no error anywhere — it happened, and the portal sat 13 lessons and 14 covers stale. Reimport via the "Importar do GitHub" button in `/catalogo/` (admin) or `import_acervo --force` in the container.

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

Ingestion does not create a lesson automatically: a PDF, transcript, course note,
or study annotation may remain in `lake/` or update a draft concept without
creating a canonical lesson. Create/edit `aulas/**/canonica.md` only after an
explicit pedagogical decision; only canonical lessons enter `manifesto.json`.

Frontmatter required fields: `conceito`, `slug`, `disciplina`, `tipo` (`conceito|entidade|sintese`), `status` (`vivo|rascunho|obsoleto`).

Aulas reference concepts via `[[slug]]` wikilinks. Backlink sync checked by lint workflow described in `AGENTS.md §4`.

## Memory

Durable project memory lives in **ai-memory** (MCP), not in local files.

**Read before you write.** Call `memory_query` before proposing architecture, before re-deriving a decision that may already exist, and before telling the user you don't know something about this project. Call `memory_recent` at session start when no handoff arrived. Storing memory nobody reads is wasted disk — the retrieval side is the one that has to be deliberate.

Write with `memory_write_page`, choosing the path by kind: `decisions/` for architectural calls (pinned, ADR shape), `_rules/` for standing rules, plus `gotchas/`, `notes/`, `procedures/`, `concepts/`. Do **not** duplicate what this file, `AGENTS.md`, or `manifesto.json` already document — memory that mirrors the repo rots and then contradicts it.

The legacy file store at `~/.claude/projects/C--PROJETOS-PROF-TONI/memory/` is **frozen**: read-only history, never add to it.

## Git

Remote uses SSH dual-account setup. This repo → `elvertoni` account (not `tonicoimbra`). Commits go straight to `main` — no PR flow in this acervo. See ai-memory page `_rules/git-ssh-duas-contas.md` for SSH config details.
