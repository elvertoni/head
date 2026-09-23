---
conceito: Thread
slug: thread
disciplina: introducao-a-computacao
tipo: conceito
aka: [linha de execução]
status: rascunho
fontes:
  - "lake/introducao-a-computacao/AULA 30_INTRODUÇÃO A COMPUTAÇÃO.pptx"
aulas: [30]
atualizado_em: 2026-09-22
---

Thread é uma subtarefa dentro de um [[processo]] — uma linha de execução que faz parte do mesmo programa e compartilha seu espaço de memória. Um único processo pode ter várias threads rodando coisas diferentes ao mesmo tempo; num editor de vídeo, por exemplo, uma thread exibe a prévia, outra processa o áudio, outra salva o projeto em segundo plano.

## Em uma frase

Thread é uma subtarefa dentro de um processo, uma linha de execução que pode rodar junto com outras do mesmo programa.

## O que precisa saber

A relação de escala vai do maior para o menor: [[processo]] (o programa inteiro, com memória própria) contém uma ou mais threads, que por sua vez são executadas pelos [[nucleo-de-processador|núcleos]] físicos da CPU. Mais núcleos permitem mais threads rodando em paralelismo real; com poucos núcleos, o [[escalonamento-de-processos]] também revezar entre threads, do mesmo jeito que reveza entre processos. Quando um programa é descrito como usando "muitas threads", significa que ele dividiu seu trabalho interno em várias linhas de execução que podem avançar concorrentemente, aproveitando melhor os núcleos disponíveis — é essa divisão interna que explica por que uma parte de um programa (o áudio) pode continuar fluindo enquanto outra parte do mesmo programa (o vídeo) engasga.

## Erros comuns

- Confundir thread com um programa instalado (aplicativo); thread é uma subtarefa interna de um processo, não um software independente.
- Confundir thread com um tipo de memória ou peça de hardware; ela é puramente uma linha de execução.
- Achar que threads de um mesmo processo rodam sempre em núcleos separados; isso só ocorre quando há núcleos livres o bastante — senão, elas também disputam tempo por escalonamento.

## Onde aparece

- Aula 30 — *Vários Programas ao Mesmo Tempo - Parte 2* `aulas/introducao-a-computacao/arquitetura-computadores-e-sistemas-operacionais/30-varios-programas-ao-mesmo-tempo-parte-2/canonica.md`
- Conceitos vizinhos: [[processo]], [[escalonamento-de-processos]], [[nucleo-de-processador]], [[gargalo-de-desempenho]]

## Fontes

- Definição de thread como subtarefa dentro de um processo, o diagrama processo → threads → núcleos e o erro comum de confundi-la com hardware ou app: slides SEED da Aula 30 (`lake/introducao-a-computacao/AULA 30_INTRODUÇÃO A COMPUTAÇÃO.pptx`), base da canônica aprovada da Aula 30.
