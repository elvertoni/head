---
name: alimentar-cerebro
description: >
  Alimentar o segundo cérebro do Prof. Toni (repo PROF-TONI) com material novo:
  receber conteúdo (texto colado, link, PDF, dump de Notion) via Telegram ou git,
  registrar a fonte bruta no lake/, e CURAR o grafo de conceitos/ — extrair
  conceitos/entidades, criar/atualizar páginas atômicas, cruzar [[wikilinks]],
  regenerar index e logar. Use quando o Toni mandar material para o Quíron
  "aprender", ingerir, curar, indexar, ou enriquecer o cérebro/wiki/conceitos —
  mesmo sem virar aula.
version: 1.0.0
platforms: [linux, macos]
metadata:
  hermes:
    tags: [ingest, curadoria, segundo-cerebro, conceitos, lake, prof-toni, wiki]
    category: prof-toni
    requires_toolsets: [terminal]
---

# Alimentar o cérebro PROF-TONI (workflow `ingest`)

Procedimento para o Quíron ingerir material novo e **curar** o segundo cérebro do
Toni com segurança. O repositório é clonado na VPS (ex.: `~/projetos/PROF-TONI`).
**Sempre opere de dentro da raiz do repo** — lá o `AGENTS.md`/`CLAUDE.md` do projeto
já carrega o schema completo. **Leia `AGENTS.md` §5 antes de qualquer ingest.**

Distinta da skill `operar-acervo` (que opera o warehouse: manifesto, render, ops de
aula). Esta governa a **entrada** (lake) e a **camada 2** (grafo de conceitos).

## Quando usar

Toni manda um material (texto, link, PDF, Notion) e diz "aprende isso", "ingere",
"cura", "indexa no cérebro", "extrai os conceitos", "guarda pra usar depois". O
objetivo NÃO é necessariamente virar aula — é o cérebro **compor** conhecimento
reusável. Virar aula é passo opcional no fim (delega à skill `prof-toni`).

## Modelo mental (pipeline lake→warehouse)

```
lake/        fontes brutas (status: bruto) — Toni cura; entram aqui
conceitos/   wiki atômica (Karpathy llm-wiki) — VOCÊ mantém. É o "aprender".
aulas/       aula canônica (fonte única) — só via skill prof-toni
```

`conceitos/{disciplina}/{slug}.md` = um conceito por arquivo, atômico. `slug` é
**único em todo o vault** (wikilinks resolvem por nome de arquivo no Obsidian).

## Invariantes (NUNCA violar)

1. **lake/ é imutável** — você pode **criar arquivo NOVO** de fonte bruta, mas
   **nunca editar nem apagar** um arquivo de lake já existente. Curadoria é na
   camada 2 (conceitos), não reescrevendo a fonte.
2. **Classificação é decisão do Toni** — disciplina e fonte de um material novo
   você **propõe**; confirme com ele antes de gravar no lake (ele cura a entrada).
3. **Voz própria nos conceitos** — nunca colar trecho longo da fonte; reescrever.
   O conceito cita a proveniência em `## Fontes`.
4. **`conceitos/log.md` é append-only** — nunca reescrever linha antiga.
5. **`conceitos/index.md` é regenerável** — pode reescrever inteiro a partir dos
   frontmatters.
6. **Nada de auto-commit** — mostre o diff e proponha a mensagem; Toni alinha
   PC/git/VPS por conta dele.
7. **Checar duplicata antes de criar** conceito (por `slug` ou `aka`). Atualizar
   página existente é o caso comum, não criar nova.

## Passo 0 — estado antes de agir

```bash
cd ~/projetos/PROF-TONI && git pull
git status --short          # não misturar trabalho humano não versionado
```

Leia `AGENTS.md` §2 (formato do conceito) e §5 (workflows) antes de escrever.

## Passo 1 — receber o material (intake)

Fontes possíveis e como tratar:

| Chega como | O que fazer |
|---|---|
| **Texto colado** (Telegram) | É o conteúdo bruto. Vá ao passo 2. |
| **Link/URL** | Buscar o conteúdo (fetch). Guardar a URL como proveniência. |
| **PDF** (anexo) | Extrair texto: `pdftotext arquivo.pdf -` (precisa `poppler-utils`). Se não houver, peça ao Toni ou use o modelo multimodal para ler. |
| **Dump de Notion** | Tratar como fonte; passa pelas mesmas regras do lake. |

Classifique e **confirme com o Toni**: `disciplina` (slug existente do vault) e
`fonte` (origem curta, ex.: `ia-coders`, `notion`, `pycodebr`).

## Passo 2 — registrar a fonte no lake (arquivo NOVO)

Grave em `lake/{disciplina}/{fonte}/{slug-descritivo}.md`. Frontmatter mínimo de
fonte bruta:

```yaml
---
titulo: <título humano do material>
disciplina: <slug-da-disciplina>
fonte: <origem>
origem: <URL ou "telegram" ou "notion" ou "pdf:nome.pdf">
status: bruto
data: <YYYY-MM-DD>
---
```

Binários (PDF cru) ficam gitignored — o que entra no git é o `.md` extraído. Nunca
edite esse arquivo depois para "virar aula"; a curadoria é no passo 3.

## Passo 3 — curar o grafo de conceitos (o "aprender")

Este é o coração do ingest (`AGENTS.md` §5). Para o material:

1. **Extrair** conceitos e entidades relevantes.
2. Para cada um: **checar se já existe** (`slug`/`aka`) em `conceitos/`. Se existe,
   **atualizar** (enriquecer corpo, adicionar fonte, avançar `atualizado_em`). Se
   não, **criar** `conceitos/{disciplina}/{slug}.md` no formato de `AGENTS.md` §2:
   - Frontmatter completo: `conceito, slug, disciplina, tipo (conceito|entidade|
     sintese), aka, status (vivo|rascunho|obsoleto), fontes, aulas, atualizado_em`.
   - Anatomia fixa: Definição (1 parágrafo denso) → `## Em uma frase` →
     `## O que precisa saber` → `## Erros comuns` → `## Onde aparece` → `## Fontes`.
   - Sem H1 no corpo. Voz própria.
3. **Cruzar referências**: adicionar `[[wikilinks]]` nos conceitos vizinhos e
   atualizar a seção `## Onde aparece`. Link liberal — `[[slug]]` sem arquivo é
   stub intencional (vira tarefa futura), não erro.
4. **Regenerar** `conceitos/index.md` (uma linha por conceito) e **anexar** linha
   em `conceitos/log.md`:
   ```
   ## [YYYY-MM-DD] ingest | <material> (<fonte>) → [[slug1]], [[slug2]], [[slug3]]
   ```
5. Tocar 5–15 arquivos numa ingestão é **normal**.

## Passo 4 (opcional) — virar aula

Só se o Toni pedir. Criar aula canônica **é da skill `prof-toni`** (segue `spec/`,
rubrica como gate). Não burlar. Depois, regenerar manifesto (skill `operar-acervo`).

## Saúde (lint) — quando o Toni pedir "revisa o cérebro"

Varrer `conceitos/` e reportar uma linha por achado (NÃO corrigir sozinho — propor):
link morto (`[[slug]]` sem arquivo), órfão (sem inlink), backlink faltando, stale,
contradição, duplicata (checar `aka`), frontmatter incompleto. Toni aprova merge/
obsolescência. Detalhe em `AGENTS.md` §5 `lint`.

## Checklist de saída

- [ ] Fonte gravada em `lake/{disciplina}/{fonte}/` com frontmatter `status: bruto`
- [ ] Disciplina/fonte confirmadas com o Toni (não inventadas)
- [ ] Conceitos criados/atualizados em voz própria, frontmatter completo, sem H1
- [ ] `[[wikilinks]]` cruzados e `## Onde aparece` atualizado nos vizinhos
- [ ] `conceitos/index.md` regenerado e linha anexada em `conceitos/log.md`
- [ ] Nenhum arquivo de `lake/` existente foi editado/apagado
- [ ] Diff revisado; commit proposto ao Toni (não auto-commitado)
