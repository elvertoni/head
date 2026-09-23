---
conceito: Ciclo de instrução
slug: ciclo-de-instrucao
disciplina: introducao-a-computacao
tipo: conceito
aka: [ciclo fetch-decode-execute, ciclo busca-decodifica-executa-armazena]
status: rascunho
fontes:
  - "lake/introducao-a-computacao/AULA 28_INTRODUÇÃO A COMPUTAÇÃO.pptx"
  - "lake/introducao-a-computacao/AULA_RETOMADA_2_ INTRODUÇÃO A COMPUTAÇÃO.pptx"
aulas: [2, 28]
atualizado_em: 2026-09-22
---

Ciclo de instrução é a sequência de quatro etapas que a [[cpu]] repete para executar cada instrução de um programa: buscar a instrução na memória, decodificá-la para entender o que ela pede, executá-la e armazenar o resultado. Terminada uma instrução, o ciclo recomeça para a próxima, sem parar enquanto o computador está ligado.

## Em uma frase

Ciclo de instrução é o buscar-decodificar-executar-armazenar que a CPU repete para cada instrução, sem parar.

## O que precisa saber

Um programa não é executado como bloco único: é uma lista de instruções simples, e cada uma passa pelo ciclo inteiro. O [[contador-de-programa]] é quem indica, a cada volta do ciclo, qual instrução buscar em seguida, garantindo que a sequência seja respeitada. A velocidade com que esse ciclo se repete depende do [[clock]] da CPU, e quantos ciclos podem correr de forma independente ao mesmo tempo depende de quantos [[nucleo-de-processador|núcleos]] a CPU tem. O ciclo de instrução é o mesmo mecanismo, sozinho por trás de qualquer instrução em [[linguagem-de-maquina]] que chega à CPU, seja ela originada por um [[compilador]] ou por um [[interpretador]].

## Erros comuns

- Confundir o ciclo de instrução com a instrução em si — o ciclo é o processo repetido de quatro etapas; a instrução é o dado que passa por ele a cada rodada.
- Achar que o ciclo para entre uma instrução e outra — ele se repete continuamente enquanto o computador está ligado, sem pausas perceptíveis.

## Onde aparece

- Aula 2 — *Retomada - Entendendo a Execução de Programas* `aulas/introducao-a-computacao/nivelamento-e-retomada/02-retomada-execucao-de-programas/canonica.md`
- Aula 28 — *A CPU em Ação - o Ciclo de Instrução* `aulas/introducao-a-computacao/arquitetura-computadores-e-sistemas-operacionais/28-a-cpu-em-acao-o-ciclo-de-instrucao/canonica.md`
- Conceitos vizinhos: [[contador-de-programa]], [[cpu]], [[clock]], [[nucleo-de-processador]]

## Fontes

- Slides SEED da aula 28 (`lake/introducao-a-computacao/AULA 28_INTRODUÇÃO A COMPUTAÇÃO.pptx`), slide 12, e da retomada 2 (`lake/introducao-a-computacao/AULA_RETOMADA_2_ INTRODUÇÃO A COMPUTAÇÃO.pptx`), slide 13: as quatro etapas do ciclo.
- Base da canônica aprovada das aulas 2 e 28, bloco :::conceito Ciclo de instrução e o diagrama progressivo das quatro etapas.
