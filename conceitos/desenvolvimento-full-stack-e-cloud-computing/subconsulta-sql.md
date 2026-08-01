---
conceito: Subconsulta SQL
slug: subconsulta-sql
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [consulta aninhada, subquery]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Linguagens e Aplicações de Banco de Dados/28 - Aula 28 - Consultas Avançadas - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Subconsulta SQL é uma consulta colocada dentro de outra consulta para produzir um valor, conjunto ou condição intermediária. Ela pode ser independente ou depender da linha da consulta externa.

## Em uma frase

Subconsulta usa uma consulta como parte da expressão de outra.

## O que precisa saber

Subconsultas aparecem em WHERE, FROM e SELECT e podem ser correlacionadas. [[divisao-relacional]] e [[diferenca-relacional]] frequentemente ganham traduções por EXISTS, NOT EXISTS ou agregação.

## Erros comuns

- Retornar várias linhas onde era esperado um escalar.
- Criar correlação desnecessária e degradar o desempenho.
- Esquecer a semântica de NULL em NOT IN.

## Onde aparece

- Linguagens e Aplicações de Banco de Dados, Aula 28, páginas 1–5.
- Relaciona-se a [[dql]], [[divisao-relacional]] e [[diferenca-relacional]].

## Fontes

- Aula 28, páginas 1–5 dos slides: subconsultas correlacionadas e não correlacionadas.
