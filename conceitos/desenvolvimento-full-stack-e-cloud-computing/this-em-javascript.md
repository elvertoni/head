---
conceito: this em JavaScript
slug: this-em-javascript
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [this keyword]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/JavaScript e Aplicações Práticas/03 - Aula 3 - Funções - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

this em JavaScript é uma referência determinada pelo modo de chamada da função, pelo objeto de invocação ou pelo contexto léxico das arrow functions. Não é simplesmente um alias fixo da função atual.

## Em uma frase

this depende do contexto de chamada e da forma da função.

## O que precisa saber

Métodos, call, apply, bind, funções comuns e arrow functions têm regras diferentes. Entender o valor de this evita bugs em callbacks e handlers de eventos.

## Erros comuns

- Assumir que this sempre aponta para o objeto onde a função foi escrita.
- Passar método como callback e perder seu contexto.
- Usar arrow function quando é necessário this dinâmico.

## Onde aparece

- JavaScript e Aplicações Práticas, Aula 3, páginas 5–7.
- Relaciona-se a [[funcoes-em-javascript]], [[fechamento-em-javascript]] e [[modelo-de-eventos-do-dom]].

## Fontes

- Aula 3, páginas 5–7 dos slides: this e contexto de funções.
