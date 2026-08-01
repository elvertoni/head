---
conceito: Cardinalidade
slug: cardinalidade
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [cardinalidade de relacionamento]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Modelagem de Banco de Dados/14 - Aula 14 - Relacionamentos III - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Cardinalidade descreve a quantidade de ocorrências que podem se associar entre entidades, como um-para-um, um-para-muitos ou muitos-para-muitos. Em alguns usos, o termo enfatiza o máximo; a especificação completa também considera participação mínima.

## Em uma frase

Cardinalidade limita quantas ocorrências podem se relacionar.

## O que precisa saber

A regra deve ser lida do ponto de vista de cada entidade e validada com o domínio. [[multiplicidade]] detalha mínimo e máximo; no [[modelo-relacional]], uma relação muitos-para-muitos costuma exigir [[tabela-associativa]].

## Erros comuns

- Ler a cardinalidade no sentido inverso.
- Confundir “muitos” com um limite operacional arbitrário.
- Criar tabela associativa sem registrar a regra de unicidade.

## Onde aparece

- Aulas 13–14 — Relacionamentos II e III.
- Conecta [[relacionamento]], [[multiplicidade]], [[tabela-associativa]] e [[modelo-relacional]].

## Fontes

- Aula 14, slides: cardinalidade e restrições de relacionamentos.
