---
conceito: Busca de custo uniforme
slug: busca-de-custo-uniforme
disciplina: inovacao-inteligencia-artificial-e-robotica-educacional
tipo: conceito
aka: [uniform-cost search, UCS, busca pelo menor custo]
status: rascunho
fontes:
  - "lake/Inovacao-Inteligencia-Artificial-e-Robotica-Educacional/Módulo II - Inteligência Artificial/Inteligência Artificial e Blockchain/04 - Aula 4 - Busca Cega I - Resumo (Aula em PDF).pdf"
  - "lake/Inovacao-Inteligencia-Artificial-e-Robotica-Educacional/Módulo II - Inteligência Artificial/Inteligência Artificial e Blockchain/06 - Aula 6 - Busca Cega III - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Busca de custo uniforme é uma estratégia de [[busca-cega|busca cega]] que expande o nó com menor custo acumulado desde o estado inicial. Ela generaliza a preferência por caminhos baratos e pode obter uma solução ótima quando os custos das ações são não negativos e as demais condições do problema são atendidas.

## Em uma frase

Busca de custo uniforme sempre expande primeiro o caminho de menor custo acumulado.

## O que precisa saber

A fronteira é ordenada por `g(n)`, o custo do caminho percorrido. Diferentemente de [[busca-em-largura]], ela não prioriza simplesmente a menor profundidade; diferentemente da [[busca-gulosa]], não usa apenas uma estimativa do que falta. A análise deve considerar completude, optimalidade, tempo e espaço.

## Erros comuns

- Confundir menor profundidade com menor custo.
- Permitir custos negativos sem rever as garantias do algoritmo.
- Chamar a busca gulosa de custo uniforme só porque ambas usam uma fila de prioridade.

## Onde aparece

- Aulas 4 e 6 — Busca Cega, no Módulo II.
- É uma estratégia de [[busca-cega]] aplicada a um [[problema-de-busca]]. Compara-se com [[busca-em-largura]], [[busca-gulosa]] e [[busca-a-estrela]], conforme as [[propriedades-de-algoritmos-de-busca|propriedades de busca]].

## Fontes

- Resumo da Aula 4, página 5: busca pelo menor custo.
- Slides da Aula 6, página 4: busca pelo menor custo no conjunto de buscas não informadas.
