---
conceito: Atributo simples
slug: atributo-simples
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [atributo atômico]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Modelagem de Banco de Dados/10 - Aula 10 - Entidade e Atributos II - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Atributo simples é uma propriedade que não precisa ser decomposta em partes menores para cumprir o uso do domínio. Seu valor é tratado como uma unidade no modelo.

## Em uma frase

Atributo simples representa um valor que o domínio usa como unidade.

## O que precisa saber

A classificação depende do uso: nome pode ser simples em um contexto e composto em outro. Atributos simples ainda precisam de [[dominio-de-atributo]] e podem participar de uma [[chave-primaria]]. A decisão deve servir a consultas, validações e regras do domínio.

## Erros comuns

- Tratar todo texto como atributo simples.
- Ignorar partes que serão consultadas ou validadas separadamente.
- Dividir um valor sem uma necessidade real do domínio.

## Onde aparece

- Aulas 10–11 — Entidade e Atributos.
- É um tipo de [[atributo]] e relaciona-se a [[atributo-composto]].

## Fontes

- Aula 10, slides: classificação e representação de atributos.
