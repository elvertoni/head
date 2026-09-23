---
conceito: Multitarefa
slug: multitarefa
disciplina: introducao-a-computacao
tipo: conceito
aka: [multitasking]
status: rascunho
fontes:
  - "lake/introducao-a-computacao/AULA 29_INTRODUÇÃO A COMPUTAÇÃO.pptx"
aulas: [29]
atualizado_em: 2026-09-22
---

Multitarefa é a técnica pela qual o sistema operacional alterna rapidamente o uso da CPU entre vários [[processo|processos]], dando a cada um uma fatia minúscula de tempo. Em um [[nucleo-de-processador|núcleo]] único, a troca é tão veloz — frações de segundo — que cria a ilusão de simultaneidade, embora, em cada instante exato, apenas um processo esteja de fato usando o processador.

## Em uma frase

Multitarefa é a ilusão de simultaneidade produzida por alternância rápida da CPU entre processos, num único núcleo.

## O que precisa saber

Multitarefa resolve o caso de um único núcleo: como a CPU executa uma instrução por vez, o [[sistema-operacional]] reveza entre os processos concorrentes por meio do [[escalonamento-de-processos]], que decide qual processo recebe a CPU a cada instante. É essencial diferenciar multitarefa de [[paralelismo]]: em multitarefa a simultaneidade é aparente (um núcleo revezando); em paralelismo real, vários núcleos executam processos genuinamente ao mesmo tempo. Na prática, um computador moderno combina os dois — paralelismo entre os poucos núcleos disponíveis e multitarefa dentro de cada núcleo — o que permite que dezenas de processos convivam mesmo com poucos núcleos físicos.

## Erros comuns

- Achar que "abrir mais programas" torna a CPU capaz de processá-los verdadeiramente ao mesmo tempo; num núcleo único ela continua executando um de cada vez, só reveza mais depressa.
- Não perceber que abrir programas em excesso deixa tudo mais lento porque a fatia de tempo de cada processo encolhe conforme mais processos disputam o mesmo núcleo.
- Tratar multitarefa e paralelismo como sinônimos.

## Onde aparece

- Aula 29 — *Vários Programas ao Mesmo Tempo - Parte 1* `aulas/introducao-a-computacao/arquitetura-computadores-e-sistemas-operacionais/29-varios-programas-ao-mesmo-tempo-parte-1/canonica.md`
- Conceitos vizinhos: [[processo]], [[paralelismo]], [[escalonamento-de-processos]]

## Fontes

- Definição de multitarefa, a alternância entre processos e o erro comum sobre CPU "mais inteligente": slides SEED da Aula 29 (`lake/introducao-a-computacao/AULA 29_INTRODUÇÃO A COMPUTAÇÃO.pptx`), base da canônica aprovada da Aula 29.
