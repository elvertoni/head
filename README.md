# Acervo de Conhecimento — Prof. Toni Coimbra

Segundo cérebro (vault Obsidian) do Curso Técnico em Desenvolvimento de Sistemas (SEED-PR). Arquitetura **data lake → data warehouse**:

```
   LAKE  ──curadoria (skill prof-toni + rubrica)──►  WAREHOUSE  ──►  saídas
 (bruto)                                            (impecável)      (HTML / ProfessorDash)
 lake/                                              aulas/.../canonica.md
 livros, PDFs, transcrições, vídeos                 Canônica = fonte única de verdade
```

- **`lake/{disciplina}/`** — conteúdo cru, sem curadoria: livros, PDFs, transcrições, vídeo-aulas, anotações. Insumo.
- **`aulas/{disciplina}/{trilha}/{NN-slug}/canonica.md`** — warehouse: Aulas Canônicas ricas, auditadas, neutras de plataforma. **Fonte única de verdade.**
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
