---
conceito: DQL
slug: dql
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [Data Query Language, linguagem de consulta de dados]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Modelagem de Banco de Dados/33 - Aula 33 - Modelo Físico de Dados II - Apostila (Slides).pdf"
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Linguagens e Aplicações de Banco de Dados/18 - Aula 18 - Estrutura Básica de Consultas (DQL) - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

DQL é a classificação usada para operações SQL de consulta e recuperação de dados, principalmente SELECT. Consultas projetam, filtram, agregam e relacionam dados sem necessariamente modificar as instâncias.

## Em uma frase

DQL recupera e organiza dados conforme uma pergunta declarada.

## O que precisa saber

Uma consulta pode ser correta e ainda custosa ou expor dados indevidos. [[sql]], [[indice-de-banco-de-dados]], permissões e planos do [[sgbd]] participam do resultado. A consulta deve respeitar o significado do [[modelo-relacional]].

## Erros comuns

- Buscar todas as colunas e linhas sem necessidade.
- Confundir consulta com garantia de qualidade da interpretação.
- Expor dados sensíveis sem autorização.

## Onde aparece

- Aula 33 — Modelo Físico de Dados II.
- É uma categoria de [[sql]] ao lado de [[ddl]], [[dml]], [[dcl]] e [[dtl]].

## Fontes

- Aula 33, slides: consultas e operações SQL.
