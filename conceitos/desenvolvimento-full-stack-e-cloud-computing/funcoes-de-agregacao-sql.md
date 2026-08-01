---
conceito: Funções de agregação SQL
slug: funcoes-de-agregacao-sql
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [agregações SQL, funções agregadas]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Linguagens e Aplicações de Banco de Dados/25 - Aula 25 - Funções de Agregação de Dados - Apostila (Slides).pdf"
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Linguagens e Aplicações de Banco de Dados/27 - Aula 27 - Funções de Agregação de Dados III - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Funções de agregação SQL resumem várias linhas em um valor, como contagem, soma, média, mínimo ou máximo. Elas permitem produzir medidas sobre um resultado ou sobre grupos.

## Em uma frase

Agregações SQL transformam muitas linhas em medidas resumidas.

## O que precisa saber

COUNT, SUM, AVG, MIN e MAX têm regras próprias para NULL. Com [[agrupamento-de-dados-sql]], a agregação é calculada por grupo; sem GROUP BY, o resultado costuma ser uma única linha.

## Erros comuns

- Confundir COUNT(*) com COUNT(coluna).
- Misturar colunas não agregadas sem GROUP BY válido.
- Interpretar média ou soma sem considerar a população efetivamente filtrada.

## Onde aparece

- Linguagens e Aplicações de Banco de Dados, Aulas 25 e 27.
- Relaciona-se a [[dql]], [[agrupamento-de-dados-sql]] e [[filtro-de-consulta-sql]].

## Fontes

- Aulas 25 e 27, páginas 1–3 dos slides: funções de agregação.
