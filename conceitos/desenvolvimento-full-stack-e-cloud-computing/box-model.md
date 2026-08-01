---
conceito: Box model
slug: box-model
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [modelo de caixa CSS]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Padrões Web - HTML e CSS/02 - Aula 2 - CSS3 - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

O box model é o modelo pelo qual o CSS calcula a caixa de cada elemento: conteúdo, padding, borda e margin. As quatro camadas influenciam espaço interno, contorno, distância entre elementos e dimensões percebidas no layout.

## Em uma frase

Toda caixa CSS combina conteúdo, padding, borda e margin.

## O que precisa saber

O modelo é uma parte do [[css3]]. A largura declarada pode representar apenas o conteúdo ou a caixa inteira, conforme box-sizing; por isso o cálculo de dimensões precisa considerar padding e bordas. O box model também explica muitos problemas de alinhamento e espaçamento em componentes de [[bootstrap]].

## Erros comuns

- Somar width, padding e borda sem saber qual box-sizing está em uso.
- Confundir margin com espaço interno.
- Corrigir overflow aumentando dimensões sem verificar a caixa real.

## Onde aparece

- Aula 2 — CSS3, na trilha Padrões Web — HTML e CSS.
- Desdobra [[css3]] e afeta layouts com [[bootstrap]] e [[media-query]].

## Fontes

- Aula 2, páginas 6–7 dos slides: conteúdo, padding, borda e margin.
