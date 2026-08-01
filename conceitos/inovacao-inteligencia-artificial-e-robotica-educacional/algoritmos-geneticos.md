---
conceito: Algoritmos genéticos
slug: algoritmos-geneticos
disciplina: inovacao-inteligencia-artificial-e-robotica-educacional
tipo: conceito
aka: [genetic algorithms, algoritmo genético]
status: rascunho
fontes:
  - "lake/Inovacao-Inteligencia-Artificial-e-Robotica-Educacional/Módulo II - Inteligência Artificial/Inteligência Artificial e Blockchain/07 - Aula 7 - Busca Heurística - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Algoritmos genéticos são métodos de busca e otimização inspirados na evolução: mantêm uma população de soluções codificadas, avaliam sua qualidade e produzem novas gerações por seleção, recombinação e mutação. No material, o exemplo das N Rainhas mostra como um cromossomo pode representar uma solução e como a [[funcao-de-aptidao|função de aptidão]] orienta a escolha.

## Em uma frase

Algoritmos genéticos evoluem uma população de soluções usando avaliação, seleção, recombinação e mutação.

## O que precisa saber

Cada indivíduo representa uma solução candidata; a função de aptidão mede quão bem ela atende ao objetivo. A seleção favorece indivíduos melhores, a recombinação combina partes de soluções e a mutação introduz variação. É uma abordagem de [[busca-heuristica|busca informada]] para espaços em que explorar diretamente todas as possibilidades é caro, mas não garante automaticamente o ótimo global.

## Erros comuns

- Confundir aptidão com uma prova de que a solução é ótima.
- Usar seleção forte demais e perder diversidade da população.
- Aplicar mutação ou recombinação sem uma representação válida para o problema.

## Onde aparece

- Aula 7 — Busca Heurística, no Módulo II.
- Conecta [[busca-heuristica]] e [[funcao-de-aptidao]].

## Fontes

- Slides da Aula 7, páginas 1–4: seção “Algoritmos Genéticos”, exemplo das N Rainhas, cromossomo, aptidão, seleção, recombinação e mutação.
