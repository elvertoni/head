---
conceito: Hoisting
slug: hoisting
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [elevação de declarações]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/JavaScript e Aplicações Práticas/03 - Aula 3 - Funções - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Hoisting descreve como declarações de variáveis e funções são registradas no ambiente antes da execução do código. O comportamento varia entre var, let, const e declarações de função.

## Em uma frase

Hoisting explica a disponibilidade antecipada de certas declarações JavaScript.

## O que precisa saber

var pode ser lido como undefined antes da atribuição; let e const permanecem na temporal dead zone. A prática mais segura é declarar antes de usar e respeitar [[escopo-de-variavel]].

## Erros comuns

- Dizer que o interpretador move literalmente todas as linhas.
- Usar var e depender de comportamento implícito.
- Confundir declaração elevada com valor já inicializado.

## Onde aparece

- JavaScript e Aplicações Práticas, Aula 3, página 3.
- Relaciona-se a [[var-let-const]], [[escopo-de-variavel]] e [[funcoes-em-javascript]].

## Fontes

- Aula 3, página 3 dos slides: hoisting e declarações.
