---
conceito: Minimax
slug: minimax
disciplina: inovacao-inteligencia-artificial-e-robotica-educacional
tipo: conceito
aka: [min-max, algoritmo minimax]
status: rascunho
fontes:
  - "lake/Inovacao-Inteligencia-Artificial-e-Robotica-Educacional/Módulo II - Inteligência Artificial/Inteligência Artificial e Blockchain/10 - Aula 10 - Busca Competitiva - Resumo (Aula em PDF).pdf"
  - "lake/Inovacao-Inteligencia-Artificial-e-Robotica-Educacional/Módulo II - Inteligência Artificial/Inteligência Artificial e Blockchain/12 - Aula 12 - Busca Competitiva III - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Minimax é um algoritmo para jogos de dois agentes em que um agente maximiza sua utilidade e presume que o adversário minimiza essa mesma utilidade. Ele percorre ou aproxima uma árvore de jogo, alternando níveis MAX e MIN, para escolher a ação cujo pior resultado possível seja o melhor entre as alternativas.

## Em uma frase

Minimax escolhe a ação que maximiza o resultado garantido contra um adversário racional.

## O que precisa saber

O algoritmo depende de [[arvore-de-jogo|árvore de jogo]], [[funcao-de-utilidade|função de utilidade]] e hipótese sobre o comportamento adversário. Em árvores grandes, [[poda-alfa-beta|poda alfa-beta]] elimina ramos sem alterar o resultado; [[heuristica-de-corte|corte heurístico]] estima estados quando não há tempo para chegar ao fim.

## Erros comuns

- Confundir minimax com escolher sempre a jogada de maior ganho imediato.
- Aplicá-lo sem distinguir turnos MAX e MIN.
- Ignorar profundidade, custo de expansão e qualidade da avaliação.

## Onde aparece

- Aulas 10–12 — Busca Competitiva, no Módulo II.
- Conecta [[busca-competitiva]], [[arvore-de-jogo]], [[funcao-de-utilidade]], [[poda-alfa-beta]], [[heuristica-de-corte]], [[jogos-deterministicos]], [[jogos-de-azar]] e [[jogo-de-soma-zero]].

## Fontes

- Resumo da Aula 10, páginas 4–5 e 6–11: minimax e jogos.
- Slides da Aula 12, página 2: algoritmo minimax.
