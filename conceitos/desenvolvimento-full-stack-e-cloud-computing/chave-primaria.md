---
conceito: Chave primária
slug: chave-primaria
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [primary key, PK]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Modelagem de Banco de Dados/21 - Aula 21 - Esquemas, Relações e Chaves - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Chave primária é o atributo ou conjunto de atributos escolhido para identificar unicamente cada tupla de uma relação. Ela não deve aceitar duplicidade e, no modelo relacional, expressa a identidade das ocorrências.

## Em uma frase

Chave primária identifica unicamente cada registro de uma relação.

## O que precisa saber

Pode ser simples ou composta; candidatos que não foram escolhidos formam [[chave-candidata]]. A chave pode ser referenciada por uma [[chave-estrangeira]], apoiando [[integridade-referencial]]. A decisão precisa considerar estabilidade, unicidade e uso do domínio.

## Erros comuns

- Escolher um valor que muda como chave sem planejar referências.
- Permitir nulos ou duplicidades na chave.
- Confundir chave primária com o índice usado para desempenho.

## Onde aparece

- Aulas 21–23 — Esquemas, Relações e Chaves.
- Conecta [[relacao]], [[tupla]], [[chave-candidata]], [[chave-estrangeira]] e [[modelo-relacional]].

## Fontes

- Aula 21, slides: identificação, unicidade e chaves primárias.
