---
conceito: Ordenação de consulta SQL
slug: ordenacao-de-consulta-sql
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [ORDER BY]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Linguagens e Aplicações de Banco de Dados/20 - Aula 20 - Estrutura Básica de Consultas (DQL) III - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Ordenação de consulta SQL organiza as linhas do resultado segundo uma ou mais expressões, normalmente com ORDER BY. Sem ordenação explícita, a sequência devolvida não é contrato.

## Em uma frase

ORDER BY torna explícita a ordem desejada para um resultado SQL.

## O que precisa saber

É possível ordenar por colunas, expressões e direções ascendente ou descendente. A ordenação pode custar caro e deve ser combinada com paginação determinística quando necessário.

## Erros comuns

- Depender da ordem incidental de um índice.
- Ordenar por coluna ambígua após uma junção.
- Paginar sem incluir uma chave de desempate estável.

## Onde aparece

- Linguagens e Aplicações de Banco de Dados, Aula 20, páginas 1–4.
- Relaciona-se a [[dql]], [[juncao-relacional]] e [[filtro-de-consulta-sql]].

## Fontes

- Aula 20, páginas 1–4 dos slides: ORDER BY e ordenação de resultados.
