---
conceito: Fechamento em JavaScript
slug: fechamento-em-javascript
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [closure]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/JavaScript e Aplicações Práticas/03 - Aula 3 - Funções - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Fechamento é uma função acompanhada do ambiente léxico em que foi criada, permitindo acessar variáveis mesmo depois que a função externa terminou. Ele sustenta encapsulamento e fábricas de funções.

## Em uma frase

Closure retém o ambiente léxico necessário à execução futura.

## O que precisa saber

O fechamento captura referências, não uma fotografia automática de todos os valores. Ele se relaciona a [[funcoes-em-javascript]], escopo e callbacks assíncronos.

## Erros comuns

- Capturar variável mutável em um laço e obter valor inesperado.
- Reter grandes objetos e causar vazamento de memória.
- Confundir closure com cópia independente do estado.

## Onde aparece

- JavaScript e Aplicações Práticas, Aula 3, página 3.
- Relaciona-se a [[funcoes-em-javascript]], [[escopo-de-variavel]] e [[programacao-assincrona]].

## Fontes

- Aula 3, página 3 dos slides: closures em JavaScript.
