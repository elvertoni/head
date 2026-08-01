---
conceito: Produto cartesiano relacional
slug: produto-cartesiano-relacional
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [produto cartesiano]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Linguagens e Aplicações de Banco de Dados/08 - Aula 8 - Operações de Conjunto IV - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Produto cartesiano relacional forma uma relação com todas as combinações entre as tuplas de duas relações. Seu tamanho potencial é o produto das quantidades de linhas dos operandos.

## Em uma frase

Produto cartesiano combina cada tupla de uma relação com cada tupla de outra.

## O que precisa saber

Ele é uma base formal para algumas [[juncao-relacional]], mas uma junção costuma restringi-lo por uma condição. Em consultas reais, a operação sem filtro pode ser muito cara.

## Erros comuns

- Produzir um produto cartesiano acidental por esquecer a condição de junção.
- Subestimar o crescimento combinatório.
- Confundir combinação de relações com união de linhas.

## Onde aparece

- Linguagens e Aplicações de Banco de Dados, Aula 8, páginas 1–3.
- Relaciona-se a [[operacoes-de-conjunto-relacional]] e [[juncao-relacional]].

## Fontes

- Aula 8, páginas 1–3 dos slides: produto cartesiano.
