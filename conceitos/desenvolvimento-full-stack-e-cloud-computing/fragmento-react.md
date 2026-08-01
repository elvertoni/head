---
conceito: Fragmento React
slug: fragmento-react
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [React Fragment]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Projeto Front - End e Desenvolvimento Web/08 - Aula 8 - Sintaxe da Linguagem JSX III - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Fragmento React agrupa múltiplos elementos JSX sem inserir um elemento extra no DOM. Ele permite que um componente devolva irmãos mantendo a estrutura semântica e o layout necessários ao documento.

## Em uma frase

Fragmento agrupa elementos JSX sem criar um nó adicional na árvore DOM.

## O que precisa saber

A sintaxe curta `<>...</>` atende agrupamentos simples; a forma explícita permite propriedades como `key` quando o fragmento participa de uma lista. O fragmento é uma construção de [[jsx]] e não um contêiner visual com estilo próprio.

## Erros comuns

- Esperar aplicar CSS diretamente no fragmento.
- Usar a forma curta quando uma `key` é necessária.
- Adicionar divs apenas para satisfazer o retorno do componente.

## Onde aparece

- Projeto Front-End e Desenvolvimento Web, Aula 8, páginas 3–4.
- Relaciona-se a [[react]], [[jsx]], [[componente-react]] e [[chaves-de-lista-react]].

## Fontes

- Projeto Front-End e Desenvolvimento Web, Aula 8, slides sobre agrupamento de elementos JSX.
