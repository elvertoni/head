---
conceito: União relacional
slug: uniao-relacional
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [união de relações, UNION]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Linguagens e Aplicações de Banco de Dados/05 - Aula 5 - Operações de Conjunto - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

União relacional reúne as tuplas de duas relações compatíveis, eliminando duplicatas no modelo relacional. Em SQL, sua forma usual é UNION.

## Em uma frase

União combina resultados compatíveis em um conjunto comum.

## O que precisa saber

As relações precisam ter o mesmo número de atributos e domínios compatíveis. [[sql]] também oferece UNION ALL quando a preservação de duplicatas é desejada.

## Erros comuns

- Tentar unir colunas semanticamente incompatíveis.
- Confundir UNION com [[juncao-relacional]].
- Ignorar o custo de deduplicação.

## Onde aparece

- Linguagens e Aplicações de Banco de Dados, Aula 5, páginas 1–5.
- Relaciona-se a [[operacoes-de-conjunto-relacional]] e [[sql]].

## Fontes

- Aula 5, páginas 1–5 dos slides: união e compatibilidade de relações.
