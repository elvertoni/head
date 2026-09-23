---
conceito: Contador de programa
slug: contador-de-programa
disciplina: introducao-a-computacao
tipo: conceito
aka: [program counter, PC]
status: rascunho
fontes:
  - "lake/introducao-a-computacao/AULA 28_INTRODUÇÃO A COMPUTAÇÃO.pptx"
aulas: [28]
atualizado_em: 2026-09-22
---

Contador de programa é um [[registrador]] dentro da CPU que guarda a posição da próxima instrução a ser executada. Depois que uma instrução é processada, o contador avança para apontar a instrução seguinte, garantindo que o programa seja executado na ordem correta.

## Em uma frase

Contador de programa é o registrador que marca qual instrução vem a seguir.

## O que precisa saber

É o contador de programa que resolve a pergunta "como a CPU sabe qual é a próxima instrução": ela não decora a lista de instruções, ela consulta esse registrador a cada volta do [[ciclo-de-instrucao]]. Na etapa de buscar, a CPU usa o valor do contador para localizar a instrução na memória; depois de executá-la, o contador é atualizado para apontar a posição seguinte. Em fluxos puramente sequenciais o avanço é linear, instrução após instrução; desvios no fluxo do programa mudam esse valor para outra posição em vez de simplesmente avançar, o que é o mecanismo por trás de decisões condicionais e repetições em código de alto nível.

## Erros comuns

- Confundir contador de programa com uma contagem de quantos programas estão abertos ou instalados no computador — é um registrador interno da CPU, específico de cada processo em execução.
- Achar que o contador sempre avança de forma estritamente sequencial — desvios no fluxo do programa alteram seu valor para apontar outra posição, não apenas a próxima em ordem.

## Onde aparece

- Aula 28 — *A CPU em Ação - o Ciclo de Instrução* `aulas/introducao-a-computacao/arquitetura-computadores-e-sistemas-operacionais/28-a-cpu-em-acao-o-ciclo-de-instrucao/canonica.md`
- Conceitos vizinhos: [[registrador]], [[ciclo-de-instrucao]], [[cpu]]

## Fontes

- Slides SEED da aula 28 (`lake/introducao-a-computacao/AULA 28_INTRODUÇÃO A COMPUTAÇÃO.pptx`), slides 9–10: papel do contador de programa em manter a ordem de execução.
- Base da canônica aprovada da aula 28, bloco :::conceito Contador de programa e o exemplo das três instruções em sequência.
