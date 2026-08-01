---
conceito: Divisão relacional
slug: divisao-relacional
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [divisão de relações]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Linguagens e Aplicações de Banco de Dados/08 - Aula 8 - Operações de Conjunto IV - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Divisão relacional identifica as tuplas da primeira relação associadas a todas as tuplas de uma segunda relação. É a operação formal para perguntas com quantificação universal.

## Em uma frase

Divisão encontra entidades relacionadas a todos os requisitos de um conjunto.

## O que precisa saber

Uma consulta “clientes que compraram todos os produtos” é um exemplo típico. Em [[sql]], a operação costuma ser expressa por agrupamento, contagem ou [[subconsulta-sql]] com dupla negação.

## Erros comuns

- Confundir “todos” com “pelo menos um”.
- Esquecer o caso de uma relação divisor vazia.
- Implementar a condição universal sem testar itens faltantes.

## Onde aparece

- Linguagens e Aplicações de Banco de Dados, Aula 8, páginas 1 e 4–5.
- Relaciona-se a [[operacoes-de-conjunto-relacional]] e [[subconsulta-sql]].

## Fontes

- Aula 8, páginas 1 e 4–5 dos slides: divisão relacional e consultas universais.
