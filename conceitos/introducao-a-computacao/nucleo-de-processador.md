---
conceito: Núcleo de processador
slug: nucleo-de-processador
disciplina: introducao-a-computacao
tipo: conceito
aka: [núcleo, core, processador multi-core]
status: rascunho
fontes:
  - "lake/introducao-a-computacao/AULA 28_INTRODUÇÃO A COMPUTAÇÃO.pptx"
  - "lake/introducao-a-computacao/AULA 29_INTRODUÇÃO A COMPUTAÇÃO.pptx"
  - "lake/introducao-a-computacao/AULA 30_INTRODUÇÃO A COMPUTAÇÃO.pptx"
aulas: [28, 29, 30]
atualizado_em: 2026-09-22
---

Núcleo de processador é uma unidade de processamento completa dentro da CPU, capaz de rodar sozinha o [[ciclo-de-instrucao]] inteiro. Uma CPU com vários núcleos (multi-core) pode executar vários ciclos de instrução simultaneamente, um por núcleo — como ter vários trabalhadores em vez de um só.

## Em uma frase

Núcleo de processador é uma unidade de execução completa da CPU; vários núcleos rodam instruções ao mesmo tempo de verdade.

## O que precisa saber

Vários núcleos são o mecanismo por trás do [[paralelismo]] real: diferente da [[multitarefa]], em que um único núcleo reveza entre [[processo|processos]] tão rápido que parece simultâneo, com múltiplos núcleos os processos rodam genuinamente ao mesmo tempo, um em cada núcleo. Na prática, um computador combina os dois: tem alguns núcleos rodando em paralelo de verdade e, dentro de cada núcleo, ainda reveza entre vários processos ou [[thread|threads]] por [[escalonamento-de-processos|escalonamento]]. O número de núcleos, junto com o [[clock]], é um dos dois fatores centrais de desempenho de uma CPU — mas só ajuda de fato quando o software é escrito para dividir trabalho entre eles.

## Erros comuns

- Achar que mais núcleos aceleram automaticamente qualquer programa — um processo que não divide seu trabalho em múltiplas threads usa só um núcleo por vez, os demais ficam disponíveis para outros processos.
- Confundir paralelismo real (vários núcleos executando ao mesmo tempo) com multitarefa (um único núcleo revezando entre processos rápido demais para perceber).

## Onde aparece

- Aula 28 — *A CPU em Ação - o Ciclo de Instrução* `aulas/introducao-a-computacao/arquitetura-computadores-e-sistemas-operacionais/28-a-cpu-em-acao-o-ciclo-de-instrucao/canonica.md`
- Aula 29 — *Vários Programas ao Mesmo Tempo - Parte 1* `aulas/introducao-a-computacao/arquitetura-computadores-e-sistemas-operacionais/29-varios-programas-ao-mesmo-tempo-parte-1/canonica.md`
- Aula 30 — *Vários Programas ao Mesmo Tempo - Parte 2* `aulas/introducao-a-computacao/arquitetura-computadores-e-sistemas-operacionais/30-varios-programas-ao-mesmo-tempo-parte-2/canonica.md`
- Conceitos vizinhos: [[cpu]], [[clock]], [[paralelismo]], [[multitarefa]], [[thread]], [[escalonamento-de-processos]]

## Fontes

- Slides SEED da aula 28 (`lake/introducao-a-computacao/AULA 28_INTRODUÇÃO A COMPUTAÇÃO.pptx`), slide 13; da aula 29 (`lake/introducao-a-computacao/AULA 29_INTRODUÇÃO A COMPUTAÇÃO.pptx`), slide 12; e da aula 30 (`lake/introducao-a-computacao/AULA 30_INTRODUÇÃO A COMPUTAÇÃO.pptx`), slide 10: núcleos como unidades físicas capazes de executar tarefas em paralelo.
- Base da canônica aprovada das aulas 28–30, blocos :::conceito Núcleo e :::importante "Os dois jeitos de fazer várias coisas juntas" da aula 29.
