---
conceito: Função de aptidão
slug: funcao-de-aptidao
disciplina: inovacao-inteligencia-artificial-e-robotica-educacional
tipo: conceito
aka: [fitness function, função de fitness]
status: rascunho
fontes:
  - "lake/Inovacao-Inteligencia-Artificial-e-Robotica-Educacional/Módulo II - Inteligência Artificial/Inteligência Artificial e Blockchain/07 - Aula 7 - Busca Heurística - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Função de aptidão é a medida que atribui uma pontuação a cada solução candidata de uma população, indicando quão bem ela atende ao objetivo do problema. Em [[algoritmos-geneticos]], essa pontuação orienta a seleção dos indivíduos que participarão das próximas gerações.

## Em uma frase

A função de aptidão transforma a qualidade de uma solução candidata em um valor comparável.

## O que precisa saber

Uma boa função de aptidão precisa refletir o objetivo e permitir comparar soluções. No exemplo das N Rainhas, ela pode avaliar conflitos entre rainhas para distinguir configurações melhores e piores. A métrica não é universal: depende da representação, das restrições e da direção de otimização do problema.

## Erros comuns

- Definir uma pontuação que recompensa um comportamento diferente do objetivo real.
- Confundir a pontuação de aptidão com a solução final.
- Ignorar penalidades ou restrições ao avaliar indivíduos inviáveis.

## Onde aparece

- Aula 7 — Busca Heurística, no Módulo II.
- É o critério de avaliação usado por [[algoritmos-geneticos]].

## Fontes

- Slides da Aula 7, página 4: exemplo das N Rainhas e função de aptidão.
