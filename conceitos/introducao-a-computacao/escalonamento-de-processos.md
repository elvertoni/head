---
conceito: Escalonamento de processos
slug: escalonamento-de-processos
disciplina: introducao-a-computacao
tipo: conceito
aka: [agendamento de processos, scheduling]
status: rascunho
fontes:
  - "lake/introducao-a-computacao/AULA 29_INTRODUÇÃO A COMPUTAÇÃO.pptx"
  - "lake/introducao-a-computacao/AULA 30_INTRODUÇÃO A COMPUTAÇÃO.pptx"
  - "lake/introducao-a-computacao/AULA 35_INTRODUÇÃO A COMPUTAÇÃO.pptx"
aulas: [29, 30, 35]
atualizado_em: 2026-09-22
---

Escalonamento de processos é a tarefa do sistema operacional de decidir qual [[processo]] (ou [[thread]]) usa a CPU a cada instante e por quanto tempo, distribuindo o tempo do [[nucleo-de-processador|núcleo]] entre tarefas leves e pesadas para manter o sistema responsivo. Não confundir com [[escalonamento]], termo já usado neste vault para o ajuste de capacidade computacional em nuvem (scaling horizontal/vertical) — são dois fenômenos distintos que só compartilham a raiz da palavra.

## Em uma frase

Escalonamento de processos é o sistema operacional decidindo quem usa a CPU, e por quanto tempo, a cada instante.

## O que precisa saber

É o mecanismo que viabiliza a [[multitarefa]]: sem uma decisão de quem usa a CPU agora, não haveria revezamento organizado entre processos. O escalonamento leva em conta o peso de cada tarefa — tarefas leves e contínuas (como tocar música) recebem fatias pequenas e frequentes, enquanto tarefas pesadas (como editar vídeo) pedem fatias maiores; quando a CPU está no limite, é isso que explica por que uma trava e a outra continua fluindo. No [[sistema-operacional]] como um todo, o escalonamento é uma das funções centrais do [[kernel]], ao lado da gerência de memória e de dispositivos, e é o que o usuário observa indiretamente ao abrir o Gerenciador de Tarefas.

## Erros comuns

- Confundir este conceito com [[escalonamento]] (ajuste de capacidade em nuvem) só pela semelhança do nome.
- Achar que o escalonamento apenas reparte tempo igualmente entre processos, ignorando que tarefas leves e pesadas recebem tratamento diferente.
- Interpretar um processo pesado sem CPU suficiente como "o computador travou por completo", quando, na verdade, tarefas leves continuam sendo atendidas nas frestas.

## Onde aparece

- Aula 29 — *Vários Programas ao Mesmo Tempo - Parte 1* `aulas/introducao-a-computacao/arquitetura-computadores-e-sistemas-operacionais/29-varios-programas-ao-mesmo-tempo-parte-1/canonica.md`
- Aula 30 — *Vários Programas ao Mesmo Tempo - Parte 2* `aulas/introducao-a-computacao/arquitetura-computadores-e-sistemas-operacionais/30-varios-programas-ao-mesmo-tempo-parte-2/canonica.md`
- Aula 35 — *Sistema Operacional - Conceito e Estrutura* `aulas/introducao-a-computacao/arquitetura-computadores-e-sistemas-operacionais/35-sistema-operacional-conceito-e-estrutura/canonica.md`
- Conceitos vizinhos: [[processo]], [[multitarefa]], [[thread]], [[gargalo-de-desempenho]], [[sistema-operacional]], [[escalonamento]]

## Fontes

- Escalonamento como decisão do sistema operacional sobre qual processo usa a CPU: slides SEED da Aula 29 (`lake/introducao-a-computacao/AULA 29_INTRODUÇÃO A COMPUTAÇÃO.pptx`), base da canônica aprovada da Aula 29.
- Escalonamento por peso de tarefa (leve × pesada) e sua ligação com travamentos: slides SEED da Aula 30 (`lake/introducao-a-computacao/AULA 30_INTRODUÇÃO A COMPUTAÇÃO.pptx`), base da canônica aprovada da Aula 30.
- Escalonamento como função do kernel dentro da estrutura em camadas do SO: slides SEED da Aula 35 (`lake/introducao-a-computacao/AULA 35_INTRODUÇÃO A COMPUTAÇÃO.pptx`), base da canônica aprovada da Aula 35.
