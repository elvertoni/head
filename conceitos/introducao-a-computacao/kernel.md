---
conceito: Kernel
slug: kernel
disciplina: introducao-a-computacao
tipo: conceito
aka: [núcleo do sistema operacional]
status: rascunho
fontes:
  - "lake/introducao-a-computacao/AULA 35_INTRODUÇÃO A COMPUTAÇÃO.pptx"
aulas: [35]
atualizado_em: 2026-09-22
---

É o núcleo do [[sistema-operacional]] — a parte que interage diretamente com o [[hardware]]. É ele que gerencia a memória, o tempo de CPU e os dispositivos de entrada e saída, tornando possível a execução dos programas: quando um aplicativo precisa de algum recurso físico, é o kernel que, no fundo, atende ao pedido.

## Em uma frase

A parte do sistema operacional que fala diretamente com o hardware.

## O que precisa saber

Se o sistema operacional é o gerente do restaurante, o kernel é o gerente dentro da cozinha, que comanda diretamente os fogões e os cozinheiros — ou seja, o hardware. O SO não é uma camada homogênea: o kernel fica no centro, e em volta dele ficam os serviços do sistema e os [[driver|drivers]] (que ensinam o SO a conversar com cada dispositivo específico); mais acima, ficam os programas que o usuário usa. Na prática, é o kernel quem concretiza funções que o SO "decide", como [[gerencia-de-memoria]] e escalonamento de [[processo|processos]] pela CPU — o SO oferece a política, o kernel executa perto do hardware. Entender essa distinção evita tratar "sistema operacional" e "kernel" como sinônimos intercambiáveis.

## Erros comuns

- Achar que kernel e sistema operacional são a mesma coisa: o kernel é o núcleo central; o SO também inclui serviços do sistema, drivers e a camada que interage com o usuário.
- Achar que o kernel é opcional ou substituível por um driver comum: é o contrário — os drivers dependem do kernel para acessar o hardware, não o inverso.

## Onde aparece

- Aula 35 — *Sistema Operacional - Conceito e Estrutura* `aulas/introducao-a-computacao/arquitetura-computadores-e-sistemas-operacionais/35-sistema-operacional-conceito-e-estrutura/canonica.md`
- Conceitos vizinhos: [[sistema-operacional]], [[driver]], [[gerencia-de-memoria]], [[hardware]]

## Fontes

- Definição e metáfora do "gerente da cozinha": base da canônica aprovada da Aula 35, derivada dos slides SEED (`lake/introducao-a-computacao/AULA 35_INTRODUÇÃO A COMPUTAÇÃO.pptx`).
