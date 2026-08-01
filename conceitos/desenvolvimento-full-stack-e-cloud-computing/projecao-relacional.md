---
conceito: Projeção relacional
slug: projecao-relacional
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [operador projeção, pi relacional]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Linguagens e Aplicações de Banco de Dados/03 - Aula 3 - Álgebra Relacional III - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Projeção relacional é a operação que escolhe atributos de uma relação e elimina repetições no resultado. É representada por π e corresponde conceitualmente à lista de colunas de uma consulta.

## Em uma frase

Projeção relacional escolhe quais atributos aparecem no resultado.

## O que precisa saber

A operação reduz a largura da relação e pode remover duplicatas no modelo formal. Em [[sql]], combina-se com [[dql]] e com [[selecao-relacional]] para expressar consultas sobre o [[modelo-relacional]].

## Erros comuns

- Confundir projeção com filtro de linhas.
- Supor que toda implementação SQL remove duplicatas automaticamente.
- Projetar colunas insuficientes para uma etapa posterior da consulta.

## Onde aparece

- Linguagens e Aplicações de Banco de Dados, Aula 3, páginas 1–6.
- Relaciona-se a [[algebra-relacional]] e [[dql]].

## Fontes

- Aula 3, páginas 1–6 dos slides: operador π e seleção de atributos.
