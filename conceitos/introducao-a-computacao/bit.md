---
conceito: Bit
slug: bit
disciplina: introducao-a-computacao
tipo: conceito
aka: []
status: rascunho
fontes:
  - "lake/introducao-a-computacao/AULA 33_INTRODUÇÃO A COMPUTAÇÃO.pptx"
  - "lake/introducao-a-computacao/AULA 34_INTRODUÇÃO A COMPUTAÇÃO.pptx"
aulas: [33, 34]
atualizado_em: 2026-09-22
---

Bit é a menor unidade de informação que um computador manipula: um único dígito que vale 0 ou 1, espelhando os dois estados físicos que um circuito digital sustenta (ligado/desligado). Isolado, um bit só distingue duas possibilidades; é o agrupamento de vários bits que carrega significado prático.

## Em uma frase

Bit é o 0 ou 1 mínimo a partir do qual todo dado digital é construído.

## O que precisa saber

Nenhum dado relevante — um número, uma letra, uma cor — é representado por um único bit. A unidade de trabalho real é o [[byte]] (8 bits agrupados), e é sobre esse alicerce que se apoiam o [[sistema-binario]] (a lógica posicional que dá valor a cada bit), a [[codificacao-de-caracteres]] (que mapeia sequências de bits a letras e símbolos) e o [[ponto-flutuante]] (que reparte bits entre sinal, expoente e mantissa para representar decimais). Quando o professor fala em MB, GB ou TB, está contando bytes — ou seja, contando bits aos montes, sempre em grupos de oito.

## Erros comuns

- Tratar bit e byte como sinônimos ou intercambiáveis; um byte são 8 bits, não 1.
- Ler prefixos de armazenamento (MB, GB) como se contassem bits em vez de bytes.
- Esperar que um bit isolado "signifique" algo por si só, sem uma convenção (tabela ou formato) que o interprete.

## Onde aparece

- Aula 33 — *Como os Dados Viram Binário - Parte 1* `aulas/introducao-a-computacao/arquitetura-computadores-e-sistemas-operacionais/33-como-os-dados-viram-binario-parte-1/canonica.md`
- Aula 34 — *Como os Dados Viram Binário - Parte 2* `aulas/introducao-a-computacao/arquitetura-computadores-e-sistemas-operacionais/34-como-os-dados-viram-binario-parte-2/canonica.md`
- Conceitos vizinhos: [[byte]], [[sistema-binario]], [[codificacao-de-caracteres]], [[ponto-flutuante]]

## Fontes

- Definição de bit e a relação 8 bits = 1 byte: slides SEED da aula 33 (`lake/introducao-a-computacao/AULA 33_INTRODUÇÃO A COMPUTAÇÃO.pptx`), base da canônica aprovada da aula 33 (bloco `:::conceito Bit e byte`).
- Reforço do bit como base do ponto flutuante (sinal, expoente, mantissa em bits): slides SEED da aula 34 (`lake/introducao-a-computacao/AULA 34_INTRODUÇÃO A COMPUTAÇÃO.pptx`), base da canônica aprovada da aula 34.
