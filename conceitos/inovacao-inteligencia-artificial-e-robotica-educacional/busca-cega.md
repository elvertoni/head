---
conceito: Busca cega
slug: busca-cega
disciplina: inovacao-inteligencia-artificial-e-robotica-educacional
tipo: conceito
aka: [busca não informada, uninformed search, busca por força bruta]
status: rascunho
fontes:
  - "lake/Inovacao-Inteligencia-Artificial-e-Robotica-Educacional/Módulo II - Inteligência Artificial/Inteligência Artificial e Blockchain/04 - Aula 4 - Busca Cega I - Resumo (Aula em PDF).pdf"
  - "lake/Inovacao-Inteligencia-Artificial-e-Robotica-Educacional/Módulo II - Inteligência Artificial/Inteligência Artificial e Blockchain/06 - Aula 6 - Busca Cega III - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Busca cega, ou busca não informada, explora o espaço de estados sem usar uma estimativa específica de distância até a meta. Ela se apoia apenas na formulação do [[problema-de-busca]], na ordem dos nós e nos custos disponíveis, como ocorre em estratégias de largura, profundidade e custo uniforme.

## Em uma frase

Busca cega procura sem uma heurística que indique quais estados parecem mais próximos da meta.

## O que precisa saber

As estratégias diferem na ordem em que expandem a fronteira: [[busca-em-largura]] prioriza menor profundidade, [[busca-em-profundidade]] segue um ramo antes de voltar e [[busca-de-custo-uniforme]] prioriza menor custo acumulado. Em contraste, [[busca-heuristica|busca heurística]] acrescenta informação estimada sobre a meta.

## Erros comuns

- Confundir falta de heurística com falta de objetivo ou teste de meta.
- Presumir que toda busca cega é incompleta ou que toda busca cega é ótima.
- Ignorar ciclos, custos e a estrutura do espaço ao comparar estratégias.

## Onde aparece

- Aulas 4–6 — Busca Cega, no Módulo II.
- Parte de [[problema-de-busca]] e abrange [[busca-em-largura]], [[busca-em-profundidade]], [[busca-de-custo-uniforme]] e o contraste com [[busca-heuristica]].

## Fontes

- Resumo da Aula 4, páginas 5–8: busca não informada e estratégias básicas.
- Slides da Aula 6, páginas 4–5: busca não informada, BFS e DFS.
