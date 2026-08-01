---
conceito: Problema de busca
slug: problema-de-busca
disciplina: inovacao-inteligencia-artificial-e-robotica-educacional
tipo: conceito
aka: [search problem, problema de busca em IA]
status: rascunho
fontes:
  - "lake/Inovacao-Inteligencia-Artificial-e-Robotica-Educacional/Módulo II - Inteligência Artificial/Inteligência Artificial e Blockchain/05 - Aula 5 - Busca Cega II - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Problema de busca é a especificação de uma tarefa de encontrar uma sequência de ações que leve de um estado inicial a uma meta em um espaço de estados. A formulação precisa indicar estados, ações ou operadores, transições, teste de meta e, quando aplicável, custo das ações.

## Em uma frase

Um problema de busca define de onde começar, quais ações são possíveis e como reconhecer uma solução.

## O que precisa saber

O espaço de busca reúne estados alcançáveis e transições produzidas pelos operadores. Uma solução é um caminho que passa no teste de meta; uma solução ótima minimiza o custo definido para os passos. A formulação antecede a escolha entre [[busca-cega|busca cega]] e [[busca-heuristica|busca heurística]].

## Erros comuns

- Confundir o estado inicial com o problema completo.
- Omitir ações, custos ou o teste de meta e deixar a busca sem critério verificável.
- Comparar algoritmos usando problemas formulados com objetivos ou custos diferentes.

## Onde aparece

- Aula 5 — Busca Cega II, no Módulo II.
- É a base formal para [[busca-cega]], [[busca-em-largura]], [[busca-em-profundidade]], [[busca-de-custo-uniforme]], [[busca-heuristica]] e [[propriedades-de-algoritmos-de-busca|suas propriedades de avaliação]].

## Fontes

- Slides da Aula 5, páginas 2–6: espaço de busca, estado inicial, estados, ações, operadores, problema, custo e solução.
