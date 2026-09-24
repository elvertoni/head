---
conceito: CSS Grid
slug: css-grid
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [CSS Grid Layout]
status: rascunho
fontes:
  - "lake/programacao-front-end/Front_End_Facina.pdf"
aulas: [12, 13]
atualizado_em: 2026-09-24
---

CSS Grid é um modelo de layout bidimensional que organiza elementos em linhas, colunas e áreas nomeadas. Ele permite definir a estrutura geral de uma interface e distribuir espaço nos dois eixos, enquanto [[flexbox]] costuma organizar relações lineares dentro de cada região.

## Em uma frase

CSS Grid organiza uma interface em duas dimensões de linhas, colunas e áreas.

## O que precisa saber

O container define trilhas e áreas; os itens podem ocupar células explícitas ou implícitas. Grid ajuda a separar estrutura de apresentação e pode combinar-se com [[flexbox]], [[media-query]] e [[css3]]. Responsividade exige definir como áreas e conteúdo se reorganizam em tamanhos diferentes.

## Erros comuns

- Escolher Grid ou Flexbox por hábito, sem considerar a dimensão do problema.
- Fixar todas as colunas e quebrar em telas menores.
- Usar áreas visuais para esconder uma estrutura HTML semântica ruim.

## Onde aparece

- `Front_End_Facina.pdf`, páginas 44–49.
- Aula 12 — *Flexbox: alinhar de verdade o topo e o hero* `aulas/programacao-front-end/landing-page-mvp/12-flexbox-nav-e-hero/canonica.md` — comparação Flexbox × Grid pelo número de dimensões do layout.
- Aula 13 — *Grid: os três benefícios viram cards* `aulas/programacao-front-end/landing-page-mvp/13-grid-cards-de-beneficio/canonica.md` — `grid-template-columns`, a unidade `fr` e `repeat(auto-fit, minmax(...))`.
- Relaciona-se a [[flexbox]], [[css3]], [[media-query]], [[estrutura-de-documento-html]] e [[unidade-fr]].

## Fontes

- `lake/programacao-front-end/Front_End_Facina.pdf`, páginas 44–49.
