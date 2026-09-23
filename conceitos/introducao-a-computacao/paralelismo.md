---
conceito: Paralelismo
slug: paralelismo
disciplina: introducao-a-computacao
tipo: conceito
aka: [paralelismo real]
status: rascunho
fontes:
  - "lake/introducao-a-computacao/AULA 29_INTRODUÇÃO A COMPUTAÇÃO.pptx"
aulas: [29]
atualizado_em: 2026-09-22
---

Paralelismo é a execução verdadeiramente simultânea de vários [[processo|processos]], possível quando a CPU tem mais de um [[nucleo-de-processador|núcleo]]: cada núcleo roda um processo diferente no mesmo instante exato, sem depender de revezamento. É o oposto da simultaneidade aparente produzida pela [[multitarefa]] num núcleo único.

## Em uma frase

Paralelismo é vários núcleos executando processos ao mesmo tempo de verdade, não por ilusão de revezamento.

## O que precisa saber

A distinção entre paralelismo e multitarefa é o núcleo conceitual da Aula 29 desta trilha: com um único núcleo, a CPU só consegue simular simultaneidade por alternância veloz ([[multitarefa]]); com vários núcleos, cada um pode executar um processo próprio, e aí a simultaneidade é real. Na prática, computadores modernos combinam as duas estratégias — paralelismo real entre os núcleos físicos disponíveis, e multitarefa dentro de cada núcleo — permitindo que muito mais processos convivam do que o número de núcleos existentes. O [[escalonamento-de-processos]] feito pelo [[sistema-operacional]] decide tanto em qual núcleo um processo roda quanto por quanto tempo, coordenando paralelismo e multitarefa ao mesmo tempo.

## Erros comuns

- Achar que qualquer computador com múltiplos programas abertos está necessariamente em paralelismo; sem vários núcleos livres, é multitarefa.
- Assumir que mais núcleos elimina a necessidade de escalonamento — mesmo com paralelismo, o sistema operacional ainda decide qual processo vai para qual núcleo.
- Confundir paralelismo (nível de hardware/execução) com a divisão de um processo em threads, que é uma organização interna do próprio processo.

## Onde aparece

- Aula 29 — *Vários Programas ao Mesmo Tempo - Parte 1* `aulas/introducao-a-computacao/arquitetura-computadores-e-sistemas-operacionais/29-varios-programas-ao-mesmo-tempo-parte-1/canonica.md`
- Conceitos vizinhos: [[multitarefa]], [[processo]], [[nucleo-de-processador]]

## Fontes

- Definição de paralelismo real, contraste com multitarefa e a combinação dos dois em CPUs modernas: slides SEED da Aula 29 (`lake/introducao-a-computacao/AULA 29_INTRODUÇÃO A COMPUTAÇÃO.pptx`), base da canônica aprovada da Aula 29.
