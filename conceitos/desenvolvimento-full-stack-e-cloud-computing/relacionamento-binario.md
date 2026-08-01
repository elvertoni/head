---
conceito: Relacionamento binário
slug: relacionamento-binario
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [relação binária]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Modelagem de Banco de Dados/13 - Aula 13 - Relacionamentos II - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Relacionamento binário associa ocorrências de duas entidades, como Pessoa realiza Pedido. Ele é o caso mais comum de relacionamento e pode assumir diferentes multiplicidades e participações.

## Em uma frase

Relacionamento binário conecta duas entidades por uma associação do domínio.

## O que precisa saber

Cada lado tem um papel e uma [[multiplicidade]]; [[cardinalidade]] e participação ajudam a especificar limites. A transformação para o [[modelo-relacional]] depende do caso, podendo usar [[chave-estrangeira]] ou [[tabela-associativa]].

## Erros comuns

- Esquecer que os dois lados têm papéis distintos.
- Tratar toda relação binária como um-para-um.
- Perder atributos próprios da associação durante o mapeamento.

## Onde aparece

- Aula 13 — Relacionamentos II.
- É um tipo de [[relacionamento]] e conecta [[multiplicidade]], [[cardinalidade]] e [[modelo-relacional]].

## Fontes

- Aula 13, slides: relacionamentos binários, papéis e multiplicidade.
