---
conceito: Funções escalares SQL
slug: funcoes-escalares-sql
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [scalar SQL functions]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Linguagens e Aplicações de Banco de Dados/25 - Aula 25 - Funções de Agregação de Dados - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Funções escalares SQL recebem um valor ou expressão por vez e devolvem um resultado para cada linha processada, como transformar texto, extrair partes de datas ou converter tipos. Elas diferem das [[funcoes-de-agregacao-sql]], que combinam várias linhas, e das funções armazenadas.

## Em uma frase

Funções escalares transformam valores linha a linha dentro de uma consulta SQL.

## O que precisa saber

Exemplos incluem `LOWER`, `UPPER`, `EXTRACT`, `TO_CHAR` e `CAST`. A função deve respeitar o dialeto do SGBD e o tipo recebido. Aplicá-la sobre uma coluna filtrada pode afetar índices e desempenho; legibilidade e portabilidade também entram na decisão.

## Erros comuns

- Confundir função escalar com agregação.
- Usar funções específicas de um dialeto sem considerar portabilidade.
- Transformar a coluna inteira antes de filtrar sem avaliar o plano da consulta.

## Onde aparece

- Linguagens e Aplicações de Banco de Dados, Aula 25, páginas 2–3.
- Relaciona-se a [[sql]], [[funcoes-de-agregacao-sql]], [[funcao-de-banco-de-dados]] e [[tipos-de-dados-sql]].

## Fontes

- Linguagens e Aplicações de Banco de Dados, Aula 25, slides de funções aplicadas a dados.
