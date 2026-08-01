---
conceito: Busca em profundidade
slug: busca-em-profundidade
disciplina: inovacao-inteligencia-artificial-e-robotica-educacional
tipo: conceito
aka: [depth-first search, DFS]
status: rascunho
fontes:
  - "lake/Inovacao-Inteligencia-Artificial-e-Robotica-Educacional/Módulo II - Inteligência Artificial/Inteligência Artificial e Blockchain/04 - Aula 4 - Busca Cega I - Resumo (Aula em PDF).pdf"
  - "lake/Inovacao-Inteligencia-Artificial-e-Robotica-Educacional/Módulo II - Inteligência Artificial/Inteligência Artificial e Blockchain/06 - Aula 6 - Busca Cega III - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Busca em profundidade (DFS) é uma estratégia de [[busca-cega|busca cega]] que segue um ramo o mais fundo possível antes de retroceder para explorar alternativas. Ela usa pouca memória em comparação com uma busca por níveis, mas pode ficar presa em ramos infinitos ou encontrar uma solução profunda quando havia outra mais curta.

## Em uma frase

DFS mergulha em um ramo antes de voltar e testar os irmãos do caminho.

## O que precisa saber

A fronteira se comporta como uma pilha, priorizando o nó mais recentemente descoberto. Limites de profundidade e detecção de ciclos podem tornar o comportamento controlável. A completude e a optimalidade dependem das hipóteses do problema e devem ser comparadas pelas [[propriedades-de-algoritmos-de-busca|propriedades de busca]].

## Erros comuns

- Confundir pouca memória com garantia de encontrar a melhor solução.
- Omitir detecção de ciclos em grafos com caminhos recorrentes.
- Usar DFS sem limite em espaços de profundidade infinita.

## Onde aparece

- Aulas 4 e 6 — Busca Cega, no Módulo II.
- É uma estratégia de [[busca-cega]] aplicada a um [[problema-de-busca]] e comparada pelas [[propriedades-de-algoritmos-de-busca|propriedades de busca]].

## Fontes

- Resumo da Aula 4, página 8: busca em profundidade.
- Slides da Aula 6, página 5: DFS no conjunto de buscas não informadas.
