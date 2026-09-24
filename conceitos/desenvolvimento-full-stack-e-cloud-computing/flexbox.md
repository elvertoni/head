---
conceito: Flexbox
slug: flexbox
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [CSS Flexible Box Layout]
status: rascunho
fontes:
  - "lake/programacao-front-end/FLEXBOX.pdf"
  - "lake/programacao-front-end/Front_End_Facina.pdf"
aulas: [12, 13]
atualizado_em: 2026-09-24
---

Flexbox é um modelo de layout CSS unidimensional para distribuir, alinhar e dimensionar itens ao longo de um eixo principal, com controle complementar no eixo transversal. Ele simplifica layouts de linha ou coluna, mas não substitui todo o modelo de layout nem resolve sozinho responsividade e semântica.

## Em uma frase

Flexbox organiza itens em uma dimensão com alinhamento e distribuição flexíveis.

## O que precisa saber

Um container flex define direção, envolvimento, alinhamento e distribuição; seus itens podem crescer, encolher e ocupar espaço disponível. `display: flex` se aplica no elemento pai, que vira o **container**; os filhos diretos viram **itens** automaticamente, sem receber propriedade nenhuma. `justify-content` sempre age ao longo do eixo principal (a direção da fila) e `align-items` sempre age no eixo cruzado (perpendicular) — `flex-direction: column` troca os dois de lugar, por isso decorar "justify é horizontal" trai quem decorou a direção em vez do papel. `gap` substitui margens contadas manualmente entre itens. Flexbox complementa [[css-grid]], [[box-model]] e [[media-query]]. A escolha depende de a relação principal ser linear ou bidimensional.

## Erros comuns

- Confundir eixo principal com eixo transversal.
- Usar margens e alturas fixas quando alinhamento flex resolveria o problema.
- Tratar Flexbox como solução para uma grade complexa de duas dimensões.

## Onde aparece

- `FLEXBOX.pdf`, páginas 1–4; `Front_End_Facina.pdf`, páginas 39–42.
- Aula 13 — *Grid: os três benefícios viram cards* `aulas/programacao-front-end/landing-page-mvp/13-grid-cards-de-beneficio/canonica.md` — comparação Flexbox × Grid pelo número de dimensões do layout.
- Aula 12 — *Flexbox: alinhar de verdade o topo e o hero* `aulas/programacao-front-end/landing-page-mvp/12-flexbox-nav-e-hero/canonica.md`
- Relaciona-se a [[css3]], [[css-grid]], [[box-model]], [[media-query]] e [[unidade-fr]].

## Fontes

- `lake/programacao-front-end/FLEXBOX.pdf`, páginas 1–4.
- `lake/programacao-front-end/Front_End_Facina.pdf`, páginas 39–42.
