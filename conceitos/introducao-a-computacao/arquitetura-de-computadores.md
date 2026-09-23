---
conceito: Arquitetura de computadores
slug: arquitetura-de-computadores
disciplina: introducao-a-computacao
tipo: conceito
aka: []
status: rascunho
fontes:
  - "lake/introducao-a-computacao/AULA 23_INTRODUÇÃO A COMPUTAÇÃO.pptx"
  - "lake/introducao-a-computacao/AULA 24_INTRODUÇÃO A COMPUTAÇÃO.pptx"
aulas: [23, 24]
atualizado_em: 2026-09-22
---

Arquitetura de computadores é o estudo de como os componentes de um computador — processamento, memória, armazenamento, comunicação interna e entrada/saída — se organizam e interagem para executar programas. Não é um inventário de peças: o que define a arquitetura é o modo como cada parte conversa com as demais, tanto na estrutura física (o hardware em si) quanto na estrutura lógica (a organização que faz essas peças cooperarem sob comando do software).

## Em uma frase

Arquitetura de computadores é a organização das partes de um computador e o modo como elas trabalham juntas para executar programas.

## O que precisa saber

Um sistema computacional combina quatro funções básicas — processamento, armazenamento, transferência e controle — distribuídas entre [[cpu]], [[memoria-ram]], [[armazenamento-secundario]], [[dispositivos-de-entrada-e-saida]] e os [[barramento|barramentos]] que os conectam. Essa organização costuma ser descrita em níveis: usuário e programas no topo, sistema operacional coordenando recursos, hardware principal executando e guardando dados, e dispositivos com seus [[controlador-de-dispositivo|controladores]] na base. [[hardware]] fornece a capacidade física; [[software]] é o que transforma essa capacidade em tarefa útil — nenhuma das duas partes sozinha faz um computador funcionar.

## Erros comuns

- Tratar arquitetura como lista decorada de peças, sem entender como uma se comunica com a outra.
- Confundir arquitetura com aparência externa: dois notebooks parecidos por fora podem ter organizações internas bem diferentes.
- Usar analogias (como "CPU é o cérebro") que trocam função por aparência e escondem que a CPU só executa instruções, sem pensar.

## Onde aparece

- Aula 23 — *Introdução à Arquitetura de Computadores - Parte 1* `aulas/introducao-a-computacao/arquitetura-computadores-e-sistemas-operacionais/23-introducao-a-arquitetura-de-computadores-parte-1/canonica.md`
- Aula 24 — *Introdução à Arquitetura de Computadores - Parte 2* `aulas/introducao-a-computacao/arquitetura-computadores-e-sistemas-operacionais/24-introducao-a-arquitetura-de-computadores-parte-2/canonica.md`
- Conceitos vizinhos: [[cpu]], [[memoria-ram]], [[barramento]], [[hardware]], [[software]]

## Fontes

- Definição e as quatro funções básicas: slides SEED da Aula 23 (`lake/introducao-a-computacao/AULA 23_INTRODUÇÃO A COMPUTAÇÃO.pptx`), base da canônica aprovada da Aula 23.
- Organização hierárquica em níveis e estrutura física/lógica: slides SEED da Aula 24 (`lake/introducao-a-computacao/AULA 24_INTRODUÇÃO A COMPUTAÇÃO.pptx`), base da canônica aprovada da Aula 24.
