---
conceito: Poda alfa-beta
slug: poda-alfa-beta
disciplina: inovacao-inteligencia-artificial-e-robotica-educacional
tipo: conceito
aka: [alpha-beta pruning, poda alpha-beta]
status: rascunho
fontes:
  - "lake/Inovacao-Inteligencia-Artificial-e-Robotica-Educacional/Módulo II - Inteligência Artificial/Inteligência Artificial e Blockchain/10 - Aula 10 - Busca Competitiva - Resumo (Aula em PDF).pdf"
  - "lake/Inovacao-Inteligencia-Artificial-e-Robotica-Educacional/Módulo II - Inteligência Artificial/Inteligência Artificial e Blockchain/12 - Aula 12 - Busca Competitiva III - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Poda alfa-beta é uma otimização de minimax que deixa de explorar ramos quando os limites já encontrados mostram que eles não podem alterar a decisão final. Alfa registra a melhor alternativa conhecida para MAX; beta registra a melhor alternativa conhecida para MIN; a poda preserva o resultado de minimax, mas reduz trabalho em ordens favoráveis.

## Em uma frase

Alfa-beta corta ramos irrelevantes sem mudar a escolha que minimax produziria.

## O que precisa saber

A eficácia depende da ordem em que sucessores são examinados. A técnica não muda a função de utilidade nem torna uma busca infinita possível; combina-se com [[heuristica-de-corte|corte heurístico]] quando a árvore precisa ser interrompida.

## Erros comuns

- Confundir poda com remover uma ação permanentemente do jogo.
- Atualizar alfa e beta no nível errado.
- Acreditar que a otimização elimina a necessidade de limite de tempo.

## Onde aparece

- Aulas 10–12 — Busca Competitiva, no Módulo II.
- Otimiza [[busca-competitiva|busca competitiva]] e [[minimax]], e depende de [[arvore-de-jogo]] e [[heuristica-de-corte]].

## Fontes

- Resumo da Aula 10, páginas 5 e 11: poda alfa-beta.
- Slides da Aula 12, página 4: poda em minimax.
