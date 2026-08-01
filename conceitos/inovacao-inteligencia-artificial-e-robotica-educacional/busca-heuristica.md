---
conceito: Busca heurística
slug: busca-heuristica
disciplina: inovacao-inteligencia-artificial-e-robotica-educacional
tipo: conceito
aka: [busca informada, informed search, heuristic search]
status: rascunho
fontes:
  - "lake/Inovacao-Inteligencia-Artificial-e-Robotica-Educacional/Módulo II - Inteligência Artificial/Inteligência Artificial e Blockchain/07 - Aula 7 - Busca Heurística - Apostila (Slides).pdf"
  - "lake/Inovacao-Inteligencia-Artificial-e-Robotica-Educacional/Módulo II - Inteligência Artificial/Inteligência Artificial e Blockchain/08 - Aula 8 - Busca Heurística II - Apostila (Slides).pdf"
  - "lake/Inovacao-Inteligencia-Artificial-e-Robotica-Educacional/Módulo II - Inteligência Artificial/Inteligência Artificial e Blockchain/09 - Aula 9 - Busca Heurística III - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Busca heurística é uma estratégia de busca informada que usa uma estimativa sobre a distância ou o custo restante para priorizar estados promissores. Ela direciona a exploração do espaço de estados por conhecimento do problema, complementando o custo já acumulado e reduzindo a expansão de caminhos pouco promissores.

## Em uma frase

Busca heurística usa uma estimativa do que falta para escolher quais estados explorar primeiro.

## O que precisa saber

Uma heurística `h(n)` estima o custo de um estado até uma meta. A [[busca-gulosa]] prioriza essa estimativa; a [[busca-a-estrela|busca A*]] combina o custo percorrido com ela. Uma heurística que não superestima o custo real é [[heuristica-admissivel|admissível]]. A busca heurística pertence ao repertório de [[inteligencia-artificial]] e contrasta com estratégias cegas, que não usam informação específica sobre a meta.

## Erros comuns

- Tratar qualquer palpite como heurística admissível sem verificar se ele pode superestimar o custo.
- Confundir a ordem de expansão com uma garantia automática de caminho ótimo.
- Ignorar que uma heurística ruim pode oferecer pouco ganho ou até orientar a busca para regiões inadequadas.

## Onde aparece

- Aulas 7–9 — Busca Heurística, no Módulo II.
- Conecta [[busca-gulosa]], [[busca-a-estrela]], [[heuristica-admissivel]], [[algoritmos-geneticos]], [[problema-de-busca]], [[inteligencia-artificial]] e contrasta com [[busca-cega]].

## Fontes

- Slides da Aula 7, cabeçalhos e seções sobre busca heurística e algoritmos genéticos.
- Slides da Aula 8, seções sobre busca gulosa.
- Slides da Aula 9, seção sobre busca A*.
