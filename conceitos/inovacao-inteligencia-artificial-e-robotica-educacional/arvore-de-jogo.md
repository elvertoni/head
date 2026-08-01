---
conceito: Árvore de jogo
slug: arvore-de-jogo
disciplina: inovacao-inteligencia-artificial-e-robotica-educacional
tipo: conceito
aka: [game tree, árvore de estados de jogo]
status: rascunho
fontes:
  - "lake/Inovacao-Inteligencia-Artificial-e-Robotica-Educacional/Módulo II - Inteligência Artificial/Inteligência Artificial e Blockchain/10 - Aula 10 - Busca Competitiva - Resumo (Aula em PDF).pdf"
  - "lake/Inovacao-Inteligencia-Artificial-e-Robotica-Educacional/Módulo II - Inteligência Artificial/Inteligência Artificial e Blockchain/11 - Aula 11 - Busca Competitiva II - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Árvore de jogo é a representação dos estados possíveis de uma partida a partir de um estado inicial, expandindo ações de jogadores alternados e resultados. Ela explicita escolhas, respostas, estados terminais e valores, mas cresce rapidamente conforme aumentam profundidade e fator de ramificação.

## Em uma frase

A árvore de jogo organiza estados, ações e respostas possíveis de uma partida.

## O que precisa saber

Nós representam estados; arestas representam ações; folhas podem ser estados terminais ou avaliações aproximadas. [[busca-competitiva]] explora a estrutura; [[minimax]] propaga valores; [[funcao-de-utilidade|função de utilidade]] avalia resultados. Jogos determinísticos e jogos com acaso exigem árvores com estruturas diferentes.

## Erros comuns

- Confundir toda árvore de jogo com uma árvore completamente enumerada.
- Ignorar ciclos, estados equivalentes e limite de profundidade.
- Avaliar uma folha sem considerar de quem é o turno.

## Onde aparece

- Aulas 10–12 — Busca Competitiva, no Módulo II.
- É a estrutura de [[busca-competitiva]], [[minimax]], [[funcao-de-utilidade]], [[poda-alfa-beta]], [[jogos-deterministicos]], [[jogos-de-azar]] e [[jogos]].

## Fontes

- Resumo da Aula 10, páginas 2–5: estados, ações e árvore.
- Slides da Aula 11, páginas 3–6: expansão e avaliação da árvore.
