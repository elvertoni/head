# Acervo de Aulas — Prof. Toni Coimbra

Este repositório é o **acervo de Aulas Canônicas** do Curso Técnico em Desenvolvimento de Sistemas (SEED-PR). Cada aula é um documento Markdown rico e neutro de plataforma — a **fonte única de verdade** de onde se derivam todos os formatos (site ProfessorDash, apostila HTML, PDF).

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
