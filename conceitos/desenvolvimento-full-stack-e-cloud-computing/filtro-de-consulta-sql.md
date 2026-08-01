---
conceito: Filtro de consulta SQL
slug: filtro-de-consulta-sql
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [filtro SQL, cláusula WHERE]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Linguagens e Aplicações de Banco de Dados/19 - Aula 19 - Estrutura Básica de Consultas (DQL) II - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Filtro de consulta SQL é a restrição de linhas de um resultado por meio de uma condição, normalmente escrita na cláusula WHERE. Ele materializa a [[selecao-relacional]] em uma consulta executável.

## Em uma frase

WHERE reduz o resultado SQL às linhas que satisfazem uma condição.

## O que precisa saber

Condições podem combinar comparações, AND, OR, NOT, intervalos e padrões. O filtro deve respeitar tipos, índices e a lógica de três valores de SQL.

## Erros comuns

- Usar HAVING quando a condição deveria filtrar linhas antes do agrupamento.
- Montar o predicado por concatenação de entrada do usuário.
- Ignorar que NULL não é igual nem diferente de um valor comum.

## Onde aparece

- Linguagens e Aplicações de Banco de Dados, Aula 19, páginas 1–4.
- Implementa [[selecao-relacional]] dentro de [[dql]].

## Fontes

- Aula 19, páginas 1–4 dos slides: filtros e cláusula WHERE.
