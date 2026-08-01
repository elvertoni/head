---
conceito: Junção relacional
slug: juncao-relacional
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [join relacional]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Linguagens e Aplicações de Banco de Dados/04 - Aula 4 - Álgebra Relacional IV - Apostila (Slides).pdf"
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Linguagens e Aplicações de Banco de Dados/21 - Aula 21 - Junções - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Junção relacional combina tuplas de duas relações quando uma condição de correspondência é satisfeita. Ela formaliza a recomposição de informações distribuídas em tabelas relacionadas.

## Em uma frase

Junção relacional combina relações por atributos relacionados.

## O que precisa saber

As condições normalmente usam [[chave-primaria]] e [[chave-estrangeira]]. Em [[sql]], a ideia aparece em [[inner-join]], [[left-join]] e [[right-join]], com resultados diferentes para correspondências ausentes.

## Erros comuns

- Juntar tabelas sem condição e produzir um produto cartesiano involuntário.
- Ignorar a cardinalidade e multiplicar linhas inesperadamente.
- Filtrar uma junção externa no WHERE e eliminar a preservação esperada.

## Onde aparece

- Linguagens e Aplicações de Banco de Dados, Aula 4, páginas 1–6.
- Relaciona-se a [[algebra-relacional]], [[inner-join]], [[left-join]] e [[right-join]].

## Fontes

- Aula 4, páginas 1–6 dos slides: operador de junção e condições de combinação.
