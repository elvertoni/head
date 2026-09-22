# Acervo de Conhecimento — Prof. Toni Coimbra

Segundo cérebro (vault Obsidian) do Curso Técnico em Desenvolvimento de Sistemas (SEED-PR). Arquitetura **data lake → data warehouse**:

```
   LAKE  ──curadoria (skill prof-toni + rubrica)──►  WAREHOUSE  ──►  saídas
 (bruto)                                            (impecável)      (HTML / ProfessorDash)
 lake/                                              aulas/.../canonica.md
 livros, PDFs, transcrições, vídeos                 Canônica = fonte única de verdade
```

- **`lake/{disciplina}/`** — conteúdo cru, sem curadoria: livros, PDFs, transcrições, vídeo-aulas, anotações. Insumo.
- **`conceitos/{disciplina}/{slug}.md`** — wiki persistente de conceitos, entidades e sínteses mantida pelo LLM, com wikilinks e proveniência.
- **`aulas/{disciplina}/{trilha}/{NN-slug}/canonica.md`** — warehouse: Aulas Canônicas ricas, auditadas, neutras de plataforma. **Fonte única de verdade.**
- **`conceitos/index.md`** e **`conceitos/log.md`** — catálogo regenerável e diário append-only da wiki.
- **`manifesto.json`** — índice máquina do acervo (disciplinas, séries, trilhas, aulas, status). **Gerado** por `python tools/gerar_manifesto.py` — nunca editar à mão.

Cada Canônica é a fonte única de onde se derivam todos os formatos (apostila HTML standalone, ProfessorDash, PDF).

## Contrato de import do portal (INVIOLÁVEL — leitura obrigatória p/ qualquer IA)

O **ProfessorDash** importa as aulas lendo `manifesto.json` + `aulas/**/canonica.md`.
Toda geração/edição **tem** que sair compatível com o contrato, senão a aula não
aparece no portal. A especificação completa e inviolável está em **[`AGENTS.md` §5.1](AGENTS.md)**
(também replicada na skill `prof-toni`). Resumo operacional:

- Frontmatter mínimo de cada `canonica.md`: `titulo, disciplina, trilha, ordem, slug, status: aprovada, versao, atualizado_em`.
- Caminho `aulas/{disciplina}/{trilha}/{NN}-{slug}/canonica.md`, `NN` = `ordem` em 2 dígitos, casando com o manifesto.
- Portal só importa `status: aprovada`; só re-importa aula existente se `versao` **ou** `atualizado_em` mudou → **bumpe sempre** que editar conteúdo publicado.
- Ao adicionar/aprovar/editar aula: **regere** com `python tools/gerar_manifesto.py` (valide com `--check`, exit ≠ 0 = divergência).

## Manutenção do segundo cérebro

O fluxo segue `ingest → query → lint`: fontes entram em `lake/`, o LLM atualiza
conceitos existentes antes de criar duplicatas, consultas relevantes podem virar
sínteses permanentes e o lint apenas propõe problemas para revisão humana.

**Ingestão não é publicação de aula.** PDFs, transcrições, anotações e materiais
de cursos podem ficar no `lake/` ou alimentar conceitos e sínteses em rascunho.
Uma aula canônica só nasce quando existe uma decisão pedagógica explícita; ter
uma fonte ingerida nunca adiciona uma entrada ao `manifesto.json` por si só.
Uma fonte repetida ou contextual pode permanecer somente como material de estudo
no `lake/`, sem criar conceito nem aula.

```powershell
python tools/lint_wiki.py                 # auditoria completa, somente leitura
python tools/lint_wiki.py --format json   # diagnóstico para automação
python tools/lint_wiki.py --fail-on error # gate estrutural
python tools/gerar_indice.py --check      # verifica o catálogo
python tools/gerar_indice.py --write      # regenera index.md preservando resumos
```

Detalhes de promoção, proveniência, stubs e registro de consultas estão em
[`docs/manutencao-wiki.md`](docs/manutencao-wiki.md) e no schema de
[`AGENTS.md`](AGENTS.md).

## Onde vivem as aulas

```
aulas/{disciplina}/{trilha}/{NN-slug}/
├── canonica.md   ← a aula de verdade (único arquivo editável)
├── fontes/       ← material de origem (SEED, PDF, links) — imutável
└── saidas/       ← derivados gerados — descartáveis, regeneráveis (não versionado)
```

- `disciplina`: slug minúsculo (`programacao`, `banco-de-dados`, `redes`…)
- `trilha`: a sequência didática (`caderno-de-estudos`, `engenharia-de-intencao`…)
- `NN`: ordem na trilha, dois dígitos (`01`, `02`…)

## As skills (em `.claude/skills/`)

| Skill | O que faz | Entrada → Saída |
|---|---|---|
| **`prof-toni`** | Gera a Aula Canônica no padrão (protocolo + rubrica). | tema / material / SEED → `canonica.md` |
| **`aula-estatica`** | Veste a Canônica numa apostila HTML standalone (dark/light, A4, offline). | `canonica.md` → `aula.html` |

A inteligência mora na Canônica; vestir é operação separada. Detalhes em `.claude/skills/README.md`.

## Como criar uma aula

Rode o Claude Code **na raiz deste repo** e peça em linguagem natural:

> "cria uma aula sobre APIs REST com Django, série 3ª, trilha programacao"

A skill `prof-toni` lê o protocolo, **apresenta um plano e espera seu OK**, gera a `canonica.md`, passa pela rubrica (`Rubrica 7/7 ✓`) e salva no acervo. Uma aula por vez.

Para distribuir offline depois:

> "aplica a skill aula-estatica na canônica da Aula NN"

## Regra que amarra tudo

A `canonica.md` é a fonte única de verdade. Erro de conteúdo? Corrige a Canônica e regenera a saída — **nunca** edita o `.html` na mão. Por isso `saidas/` não é versionado.
