---
conceito: Busca em largura
slug: busca-em-largura
disciplina: inovacao-inteligencia-artificial-e-robotica-educacional
tipo: conceito
aka: [breadth-first search, BFS]
status: rascunho
fontes:
  - "lake/Inovacao-Inteligencia-Artificial-e-Robotica-Educacional/Módulo II - Inteligência Artificial/Inteligência Artificial e Blockchain/04 - Aula 4 - Busca Cega I - Resumo (Aula em PDF).pdf"
  - "lake/Inovacao-Inteligencia-Artificial-e-Robotica-Educacional/Módulo II - Inteligência Artificial/Inteligência Artificial e Blockchain/06 - Aula 6 - Busca Cega III - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Busca em largura (BFS) é uma estratégia de [[busca-cega|busca cega]] que expande primeiro os nós mais rasos, visitando o espaço por níveis a partir do estado inicial. Com custos uniformes e controle adequado de estados repetidos, pode encontrar uma solução de menor profundidade e é completa sob as hipóteses usuais.

## Em uma frase

BFS explora todos os nós de uma profundidade antes de avançar para a próxima.

## O que precisa saber

A fronteira funciona como uma fila: o primeiro nó inserido é o primeiro a ser expandido. A estratégia favorece soluções rasas, mas pode consumir muita memória porque conserva uma camada ampla da árvore. Suas garantias devem ser descritas pelas [[propriedades-de-algoritmos-de-busca|propriedades de algoritmos de busca]] e pelos custos do problema.

## Erros comuns

- Confundir BFS com busca de menor custo quando as ações têm custos diferentes.
- Ignorar a memória da fila e dos estados já visitados.
- Dizer que BFS é sempre ótima sem explicitar a condição de custos uniformes.

## Onde aparece

- Aulas 4 e 6 — Busca Cega, no Módulo II.
- É uma estratégia de [[busca-cega]] aplicada a um [[problema-de-busca]] e comparada pelas [[propriedades-de-algoritmos-de-busca|propriedades de busca]] e pela [[busca-de-custo-uniforme]].

## Fontes

- Resumo da Aula 4, páginas 8–12: busca em largura.
- Slides da Aula 6, página 4: BFS no conjunto de buscas não informadas.
