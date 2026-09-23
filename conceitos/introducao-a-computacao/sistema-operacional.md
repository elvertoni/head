---
conceito: Sistema operacional
slug: sistema-operacional
disciplina: introducao-a-computacao
tipo: conceito
aka: [SO]
status: rascunho
fontes:
  - "lake/introducao-a-computacao/AULA 29_INTRODUÇÃO A COMPUTAÇÃO.pptx"
  - "lake/introducao-a-computacao/AULA 35_INTRODUÇÃO A COMPUTAÇÃO.pptx"
  - "lake/introducao-a-computacao/AULA 36_INTRODUÇÃO A COMPUTAÇÃO.pptx"
  - "lake/introducao-a-computacao/AULA 38_INTRODUÇÃO A COMPUTAÇÃO.pptx"
  - "lake/introducao-a-computacao/rco/2tri/37-o-que-e-um-sistema-operacional.md"
aulas: [29, 35, 36, 37, 38]
atualizado_em: 2026-09-22
---

É o [[software-de-base]] que faz a ponte entre as aplicações e o [[hardware]], gerenciando e compartilhando os recursos da máquina — processador, memória e dispositivos de entrada e saída — e oferecendo ao usuário uma forma de operar o sistema. É o software que torna o hardware utilizável e os programas executáveis; sem ele, nenhum outro programa tem onde rodar.

## Em uma frase

O software de base que gerencia os recursos do computador e faz a ponte entre aplicações e hardware.

## O que precisa saber

O SO ocupa a camada do meio numa estrutura de três níveis: hardware na base, sistema operacional no meio, aplicações no topo — um aplicativo nunca fala direto com o hardware, sempre pede ao SO. Sua parte central, que interage diretamente com o hardware, é o [[kernel]]; em volta dele ficam os serviços do sistema e os [[driver|drivers]]. Na prática, o SO se desdobra em funções concretas: decidir qual [[processo]] usa a CPU a cada instante ([[escalonamento-de-processos]]), fazer [[gerencia-de-memoria]], manter o [[sistema-de-arquivos]] e conversar com dispositivos via drivers. O usuário comanda tudo isso por [[interface-de-linha-de-comando]] ou [[interface-grafica]]. Historicamente, o SO nasceu para substituir o [[processamento-em-lote]] manual dos anos 1950; hoje aparece em praticamente qualquer equipamento com eletrônica embarcada — não só PCs e celulares. [[linux]] é um exemplo de SO de código aberto.

## Erros comuns

- Confundir "sistema operacional" com "os programas que vêm instalados" (navegador, editor de fotos): esses são aplicações rodando em cima do SO, não o SO em si.
- Achar que o computador "liga e os programas funcionam sozinhos": antes de qualquer aplicativo, o SO precisa carregar e assumir o comando.
- Tratar como automático o que na verdade é o SO trabalhando nos bastidores a cada instante (escalonar, gerenciar memória, organizar arquivos, acionar drivers).

## Onde aparece

- Aula 29 — *Vários Programas ao Mesmo Tempo - Parte 1* `aulas/introducao-a-computacao/arquitetura-computadores-e-sistemas-operacionais/29-varios-programas-ao-mesmo-tempo-parte-1/canonica.md`
- Aula 35 — *Sistema Operacional - Conceito e Estrutura* `aulas/introducao-a-computacao/arquitetura-computadores-e-sistemas-operacionais/35-sistema-operacional-conceito-e-estrutura/canonica.md`
- Aula 36 — *História e Evolução dos Sistemas Operacionais* `aulas/introducao-a-computacao/arquitetura-computadores-e-sistemas-operacionais/36-historia-e-evolucao-dos-sistemas-operacionais/canonica.md`
- Aula 37 — *O Que o Sistema Operacional Faz por Você* `aulas/introducao-a-computacao/arquitetura-computadores-e-sistemas-operacionais/37-o-que-o-sistema-operacional-faz-por-voce/canonica.md`
- Aula 38 — *O Que é um Sistema Operacional - Definição e Onde Vivem* `aulas/introducao-a-computacao/arquitetura-computadores-e-sistemas-operacionais/38-o-que-e-um-sistema-operacional/canonica.md`
- Conceitos vizinhos: [[kernel]], [[software-de-base]], [[gerencia-de-memoria]], [[sistema-de-arquivos]], [[driver]], [[escalonamento-de-processos]], [[linux]]

## Fontes

- Definição formal e função de gerente de recursos: base da canônica aprovada da Aula 35 e da Aula 38, ambas derivadas dos slides SEED (`lake/introducao-a-computacao/AULA 35_INTRODUÇÃO A COMPUTAÇÃO.pptx`, `lake/introducao-a-computacao/AULA 38_INTRODUÇÃO A COMPUTAÇÃO.pptx`).
- Origem histórica (processamento em lote) e ubiquidade em dispositivos diversos: slides SEED da Aula 36 (`lake/introducao-a-computacao/AULA 36_INTRODUÇÃO A COMPUTAÇÃO.pptx`) e extração RCO da Aula 37 (`lake/introducao-a-computacao/rco/2tri/37-o-que-e-um-sistema-operacional.md`).
- Papel no escalonamento entre processos: slides SEED da Aula 29 (`lake/introducao-a-computacao/AULA 29_INTRODUÇÃO A COMPUTAÇÃO.pptx`).
