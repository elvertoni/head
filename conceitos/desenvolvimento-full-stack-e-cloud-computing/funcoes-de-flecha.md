---
conceito: Funções de flecha
slug: funcoes-de-flecha
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [arrow functions]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/JavaScript e Aplicações Práticas/03 - Aula 3 - Funções - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Funções de flecha são uma sintaxe concisa do JavaScript para declarar funções com `=>`. Além da forma abreviada, elas têm regras próprias para `this`, não possuem `arguments` próprio e não funcionam como construtoras com `new`.

## Em uma frase

Funções de flecha encurtam a declaração de funções e capturam o `this` léxico.

## O que precisa saber

Uma função de flecha pode omitir chaves e `return` em expressões simples, mas a escolha deve preservar legibilidade. Sua captura léxica de `this` é útil em callbacks; quando é necessário contexto dinâmico ou uso com `new`, uma função tradicional é mais adequada. Elas são uma forma de [[funcoes-em-javascript]].

## Erros comuns

- Supor que toda função de flecha possui `this` próprio.
- Esquecer que chaves no corpo exigem `return` explícito.
- Usar arrow function quando o código depende de construtor ou `arguments`.

## Onde aparece

- JavaScript e Aplicações Práticas, Aula 3, páginas 4–5.
- Relaciona-se a [[javascript]], [[funcoes-em-javascript]] e [[fechamento-em-javascript]].

## Fontes

- JavaScript e Aplicações Práticas, Aula 3, slides sobre sintaxe de funções.
