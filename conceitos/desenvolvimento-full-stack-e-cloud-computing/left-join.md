---
conceito: LEFT JOIN
slug: left-join
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [LEFT OUTER JOIN, junção externa à esquerda]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Linguagens e Aplicações de Banco de Dados/23 - Aula 23 - Junções III - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

LEFT JOIN preserva todas as linhas da relação à esquerda e acrescenta dados correspondentes da relação à direita. Quando não há correspondência, as colunas da direita recebem NULL.

## Em uma frase

LEFT JOIN mantém a relação esquerda mesmo sem correspondência.

## O que precisa saber

Ele é útil para encontrar entidades sem registros relacionados. Predicados colocados no ON e no WHERE podem mudar a preservação, portanto a posição do filtro importa.

## Erros comuns

- Colocar no WHERE um filtro da tabela direita e transformar a junção em INNER JOIN.
- Tratar NULL de ausência como valor real.
- Ignorar duplicação causada por relações um-para-muitos.

## Onde aparece

- Linguagens e Aplicações de Banco de Dados, Aula 23, páginas 1–4.
- Relaciona-se a [[juncao-relacional]] e [[inner-join]].

## Fontes

- Aula 23, páginas 1–4 dos slides: junção externa à esquerda.
