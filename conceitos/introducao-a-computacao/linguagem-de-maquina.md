---
conceito: Linguagem de máquina
slug: linguagem-de-maquina
disciplina: introducao-a-computacao
tipo: conceito
aka: [código de máquina, machine code]
status: rascunho
fontes:
  - "lake/introducao-a-computacao/AULA 25_INTRODUÇÃO A COMPUTAÇÃO.pptx"
aulas: [25]
atualizado_em: 2026-09-22
---

Linguagem de máquina é o único código que um processador executa diretamente: sequências binárias de 0 e 1 em que cada padrão corresponde a uma operação elementar — somar dois valores, mover um dado, comparar dois números. É a camada mais baixa da tradução de software, específica da arquitetura de cada processador, e por isso é rápida de executar mas impraticável de ler ou escrever manualmente em qualquer escala.

## Em uma frase

Linguagem de máquina é a sequência binária que o processador executa sem nenhuma tradução adicional.

## O que precisa saber

Toda [[linguagem-de-alto-nivel]] precisa virar linguagem de máquina antes de rodar — é o trabalho de um [[compilador]] ou de um [[interpretador]]. Cada instrução binária corresponde a uma microoperação que a [[cpu]] busca, decodifica e executa dentro do [[ciclo-de-instrucao]]. O conjunto de instruções reconhecido é definido pela arquitetura do processador, o que explica por que um executável compilado para uma arquitetura não roda em outra sem recompilação. Na prática didática da disciplina, linguagem de máquina é sempre o alvo da tradução — o ponto de chegada — nunca a ferramenta de trabalho cotidiana do desenvolvedor.

## Erros comuns

- Tratar "linguagem de máquina" como um padrão binário único e universal, quando na verdade o conjunto de instruções é específico de cada arquitetura de processador.
- Achar que dá para ler ou escrever linguagem de máquina fluentemente como texto comum — na prática, mesmo quem trabalha nesse nível depende de ferramentas de apoio, não de leitura direta do binário.

## Onde aparece

- Aula 25 — *Como o Computador Lê o seu Código - Parte 1* `aulas/introducao-a-computacao/arquitetura-computadores-e-sistemas-operacionais/25-como-o-computador-le-o-codigo-parte-1/canonica.md`
- Conceitos vizinhos: [[linguagem-de-alto-nivel]], [[compilador]], [[interpretador]], [[cpu]]

## Fontes

- Slides SEED da aula 25 (`lake/introducao-a-computacao/AULA 25_INTRODUÇÃO A COMPUTAÇÃO.pptx`), slides 8–12: definição de linguagem de máquina como instruções binárias específicas de cada processador.
- Base da canônica aprovada da aula 25, bloco :::conceito Linguagem de máquina.
