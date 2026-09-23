---
conceito: Array
slug: array
disciplina: introducao-a-computacao
tipo: conceito
aka: [vetor]
status: rascunho
fontes:
  - "lake/introducao-a-computacao/AULA 34_INTRODUÇÃO A COMPUTAÇÃO.pptx"
aulas: [34]
atualizado_em: 2026-09-22
---

Array é uma coleção de elementos do mesmo tipo guardada em memória contígua: os elementos ficam em posições vizinhas, uma exatamente ao lado da outra, sem buracos entre elas. Essa contiguidade é o que permite ao computador calcular diretamente onde está cada elemento, em vez de procurá-lo posição por posição.

## Em uma frase

Array é uma coleção de elementos do mesmo tipo guardada lado a lado em memória contígua.

## O que precisa saber

Como o endereço de cada elemento pode ser calculado a partir do início do array e da posição desejada, acessar qualquer item — o primeiro, o do meio, o último — custa o mesmo e é rápido. O outro lado dessa vantagem é o custo de crescer: se o espaço logo após o array já está ocupado, não dá para simplesmente "empurrar" mais um elemento. O computador precisa achar um novo bloco contíguo maior, copiar todos os elementos antigos para lá e só então acrescentar o novo — por isso, em várias linguagens, o tamanho de um array é fixado na criação. Um array guarda seus elementos como sequências de [[byte]]s na [[memoria-ram]], e é essa organização contígua, não o tipo do dado guardado, que define o array como estrutura.

## Erros comuns

- Achar que adicionar um elemento a uma coleção é sempre uma operação instantânea e "de graça" — por trás de um comando simples pode estar a cópia inteira do array para um novo lugar da memória.
- Não perceber esse custo escondido dentro de um laço de repetição, onde inserções repetidas podem tornar um programa lento sem causa aparente no código.
- Confundir "tamanho fixo na criação" com limitação de linguagem, quando na verdade é consequência direta de como a memória contígua funciona.

## Onde aparece

- Aula 34 — *Como os Dados Viram Binário - Parte 2* `aulas/introducao-a-computacao/arquitetura-computadores-e-sistemas-operacionais/34-como-os-dados-viram-binario-parte-2/canonica.md`
- Conceitos vizinhos: [[byte]], [[memoria-ram]], [[ponto-flutuante]]

## Fontes

- Definição de array e memória contígua, custo de crescer um array: slides SEED da aula 34 (`lake/introducao-a-computacao/AULA 34_INTRODUÇÃO A COMPUTAÇÃO.pptx`), base da canônica aprovada da aula 34 (blocos `:::conceito Array`, `:::conceito Memória contígua` e `:::importante Crescer um array pode custar caro`).
