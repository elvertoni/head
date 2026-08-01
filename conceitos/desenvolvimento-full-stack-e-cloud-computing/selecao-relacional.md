---
conceito: Seleção relacional
slug: selecao-relacional
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [operador seleção, sigma relacional]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Linguagens e Aplicações de Banco de Dados/02 - Aula 2 - Álgebra Relacional II - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Seleção relacional é a operação que retém as tuplas de uma relação que satisfazem um predicado. É representada por σ e corresponde conceitualmente ao filtro de uma consulta.

## Em uma frase

Seleção relacional filtra linhas por uma condição.

## O que precisa saber

O predicado pode combinar comparações e operadores lógicos. Em [[sql]], sua tradução mais comum é [[filtro-de-consulta-sql]], implementado com WHERE, antes ou junto de outras operações da [[algebra-relacional]].

## Erros comuns

- Confundir seleção, que escolhe tuplas, com [[projecao-relacional]], que escolhe atributos.
- Usar uma condição que não representa o domínio dos dados.
- Esquecer o tratamento de valores nulos no filtro SQL.

## Onde aparece

- Linguagens e Aplicações de Banco de Dados, Aula 2, páginas 1–5.
- Relaciona-se a [[algebra-relacional]] e [[filtro-de-consulta-sql]].

## Fontes

- Aula 2, páginas 1–5 dos slides: operador σ e filtros relacionais.
