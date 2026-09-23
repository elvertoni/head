---
conceito: Processo
slug: processo
disciplina: introducao-a-computacao
tipo: conceito
aka: []
status: rascunho
fontes:
  - "lake/introducao-a-computacao/AULA 29_INTRODUÇÃO A COMPUTAÇÃO.pptx"
  - "lake/introducao-a-computacao/AULA 30_INTRODUÇÃO A COMPUTAÇÃO.pptx"
  - "lake/introducao-a-computacao/AULA 35_INTRODUÇÃO A COMPUTAÇÃO.pptx"
  - "lake/introducao-a-computacao/rco/2tri/37-o-que-e-um-sistema-operacional.md"
aulas: [29, 30, 35, 37]
atualizado_em: 2026-09-22
---

Processo é um programa em execução — não o arquivo parado no disco, mas a instância ativa dele, ocupando um espaço próprio de memória e disputando tempo de CPU. É a unidade que o sistema operacional efetivamente gerencia; abrir o mesmo programa duas vezes cria dois processos independentes, cada um com sua própria área de memória.

## Em uma frase

Processo é o programa rodando agora, com memória própria, e não o arquivo guardado no disco.

## O que precisa saber

A distinção programa × processo é a base de tudo que vem depois nesta trilha: o [[sistema-operacional]] não gerencia arquivos parados, gerencia processos vivos, decidindo por meio do [[escalonamento-de-processos]] quem usa a CPU e por quanto tempo. Em um único [[nucleo-de-processador]], vários processos convivem por [[multitarefa]] — alternância rápida demais para o usuário perceber; com vários núcleos, processos diferentes podem rodar em [[paralelismo]] real, um por núcleo. Internamente, um processo pode se dividir em [[thread|threads]] — subtarefas que compartilham o mesmo espaço de memória do processo. A função de "gerência de processos" é uma das atribuições centrais que caracterizam um sistema operacional como [[software-de-base]].

## Erros comuns

- Confundir o arquivo instalado no disco com o processo em execução — são coisas diferentes; o arquivo é a receita parada, o processo é a receita em ação.
- Achar que encerrar a janela sempre encerra o processo; nem sempre a interface reflete o estado real do processo para o sistema operacional.
- Achar que "processo" e "programa" são sinônimos intercambiáveis em qualquer contexto técnico.

## Onde aparece

- Aula 29 — *Vários Programas ao Mesmo Tempo - Parte 1* `aulas/introducao-a-computacao/arquitetura-computadores-e-sistemas-operacionais/29-varios-programas-ao-mesmo-tempo-parte-1/canonica.md`
- Aula 30 — *Vários Programas ao Mesmo Tempo - Parte 2* `aulas/introducao-a-computacao/arquitetura-computadores-e-sistemas-operacionais/30-varios-programas-ao-mesmo-tempo-parte-2/canonica.md`
- Aula 35 — *Sistema Operacional - Conceito e Estrutura* `aulas/introducao-a-computacao/arquitetura-computadores-e-sistemas-operacionais/35-sistema-operacional-conceito-e-estrutura/canonica.md`
- Aula 37 — *O Que o Sistema Operacional Faz por Você* `aulas/introducao-a-computacao/arquitetura-computadores-e-sistemas-operacionais/37-o-que-o-sistema-operacional-faz-por-voce/canonica.md`
- Conceitos vizinhos: [[multitarefa]], [[paralelismo]], [[escalonamento-de-processos]], [[thread]], [[sistema-operacional]]

## Fontes

- Definição de processo, memória própria e a metáfora receita/bolo: slides SEED da Aula 29 (`lake/introducao-a-computacao/AULA 29_INTRODUÇÃO A COMPUTAÇÃO.pptx`), base da canônica aprovada da Aula 29.
- Processo como unidade que disputa CPU junto de threads e núcleos: slides SEED da Aula 30 (`lake/introducao-a-computacao/AULA 30_INTRODUÇÃO A COMPUTAÇÃO.pptx`), base da canônica aprovada da Aula 30.
- Processo como recurso coordenado pelo sistema operacional na estrutura em camadas: slides SEED da Aula 35 (`lake/introducao-a-computacao/AULA 35_INTRODUÇÃO A COMPUTAÇÃO.pptx`), base da canônica aprovada da Aula 35.
- Encerrar processo travado e gerência de processos como função do SO: RCO 2º trimestre, extração da Aula 38 (`lake/introducao-a-computacao/rco/2tri/37-o-que-e-um-sistema-operacional.md`), base da canônica aprovada da Aula 37.
