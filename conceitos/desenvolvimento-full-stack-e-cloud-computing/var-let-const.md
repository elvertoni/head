---
conceito: var, let e const
slug: var-let-const
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [declarações de variável JavaScript]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Padrões Web - HTML e CSS/04 - Aula 4 - Variáveis, Comandos de Entrada e Saída e Operadores - Resumo (Aula em PDF).pdf"
aulas: []
atualizado_em: 2026-07-31
---

var, let e const são formas de declarar nomes em JavaScript com comportamentos diferentes de escopo, redeclaração e reatribuição. A escolha deve refletir se o vínculo precisa mudar e qual região do programa deve enxergá-lo.

## Em uma frase

let e const favorecem escopo de bloco; var tem regras históricas de escopo de função e hoisting.

## O que precisa saber

let permite reatribuição no escopo de bloco; const impede reatribuição do vínculo; var tem escopo de função e pode ser redeclarada. Essas diferenças pertencem ao [[escopo-de-variavel]] e afetam o uso de [[variaveis-em-javascript]]. Const não congela automaticamente o objeto referenciado.

## Erros comuns

- Tratar var, let e const como sinônimos.
- Usar var em novos blocos sem necessidade e ampliar o escopo.
- Confundir const com imutabilidade profunda.

## Onde aparece

- Aula 4 — Variáveis, Comandos de Entrada e Saída e Operadores.
- É uma especialização de [[variaveis-em-javascript]] e [[escopo-de-variavel]].

## Fontes

- Resumo da Aula 4, páginas 1–5: diferenças entre var, let e const.
