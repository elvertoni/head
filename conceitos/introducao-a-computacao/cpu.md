---
conceito: CPU
slug: cpu
disciplina: introducao-a-computacao
tipo: conceito
aka: [processador, unidade central de processamento]
status: rascunho
fontes:
  - "lake/introducao-a-computacao/AULA 23_INTRODUÇÃO A COMPUTAÇÃO.pptx"
  - "lake/introducao-a-computacao/AULA 24_INTRODUÇÃO A COMPUTAÇÃO.pptx"
  - "lake/introducao-a-computacao/AULA 25_INTRODUÇÃO A COMPUTAÇÃO.pptx"
  - "lake/introducao-a-computacao/AULA 28_INTRODUÇÃO A COMPUTAÇÃO.pptx"
  - "lake/introducao-a-computacao/AULA 29_INTRODUÇÃO A COMPUTAÇÃO.pptx"
  - "lake/introducao-a-computacao/AULA 30_INTRODUÇÃO A COMPUTAÇÃO.pptx"
  - "lake/introducao-a-computacao/AULA 31_INTRODUÇÃO A COMPUTAÇÃO.pptx"
  - "lake/introducao-a-computacao/AULA 32_INTRODUÇÃO A COMPUTAÇÃO.pptx"
  - "lake/introducao-a-computacao/AULA 35_INTRODUÇÃO A COMPUTAÇÃO.pptx"
  - "lake/introducao-a-computacao/AULA 38_INTRODUÇÃO A COMPUTAÇÃO.pptx"
  - "lake/introducao-a-computacao/AULA_RETOMADA_2_ INTRODUÇÃO A COMPUTAÇÃO.pptx"
  - "lake/introducao-a-computacao/rco/2tri/37-o-que-e-um-sistema-operacional.md"
aulas: [2, 23, 24, 25, 28, 29, 30, 31, 32, 35, 37, 38]
atualizado_em: 2026-09-22
---

A CPU (Unidade Central de Processamento) é o componente que executa instruções: soma, compara, move dados e decide o próximo passo, repetindo o [[ciclo-de-instrucao]] — buscar, decodificar, executar, armazenar — em altíssima velocidade. Ela não pensa nem decide por conta própria; segue, cegamente e na ordem indicada pelo [[contador-de-programa]], a sequência de instruções de um programa que subiu do [[armazenamento-secundario|armazenamento]] para a [[memoria-ram]].

## Em uma frase

A CPU é o componente que executa, uma a uma e em altíssima velocidade, as instruções de um programa.

## O que precisa saber

Internamente, a CPU guarda valores imediatos em [[registrador|registradores]] — memória minúscula e rapidíssima por ficar dentro do próprio processador — e consulta uma [[memoria-cache]] antes de recorrer à RAM, mais lenta. Sua velocidade é medida pelo [[clock]]; processadores atuais reúnem vários [[nucleo-de-processador|núcleos]], permitindo [[paralelismo]] real além da alternância descrita em [[multitarefa]]. Cada programa em execução é um [[processo]], que pode se dividir em [[thread|threads]]; cabe ao [[sistema-operacional]] decidir, via [[escalonamento-de-processos|escalonamento]], qual processo ou thread usa a CPU a cada instante. Quando a CPU está no limite, ela se torna o [[gargalo-de-desempenho]] do sistema — um entre vários pontos possíveis de lentidão.

## Erros comuns

- Chamar a CPU de "cérebro" que pensa ou decide sozinha: ela apenas executa instruções, sem inteligência própria.
- Achar que a CPU controla diretamente cada tecla, pixel ou setor de disco — muitos detalhes físicos ficam a cargo de [[controlador-de-dispositivo|controladores]] especializados.
- Confundir "mais núcleos" com "mais inteligente": num único núcleo a CPU continua executando uma instrução de cada vez.

## Onde aparece

- Aula 2 — *Retomada - Entendendo a Execução de Programas* `aulas/introducao-a-computacao/nivelamento-e-retomada/02-retomada-execucao-de-programas/canonica.md`
- Aula 23 — *Introdução à Arquitetura de Computadores - Parte 1* `aulas/introducao-a-computacao/arquitetura-computadores-e-sistemas-operacionais/23-introducao-a-arquitetura-de-computadores-parte-1/canonica.md`
- Aula 24 — *Introdução à Arquitetura de Computadores - Parte 2* `aulas/introducao-a-computacao/arquitetura-computadores-e-sistemas-operacionais/24-introducao-a-arquitetura-de-computadores-parte-2/canonica.md`
- Aula 25 — *Como o Computador Lê o seu Código - Parte 1* `aulas/introducao-a-computacao/arquitetura-computadores-e-sistemas-operacionais/25-como-o-computador-le-o-codigo-parte-1/canonica.md`
- Aula 28 — *A CPU em Ação - o Ciclo de Instrução* `aulas/introducao-a-computacao/arquitetura-computadores-e-sistemas-operacionais/28-a-cpu-em-acao-o-ciclo-de-instrucao/canonica.md`
- Aula 29 — *Vários Programas ao Mesmo Tempo - Parte 1* `aulas/introducao-a-computacao/arquitetura-computadores-e-sistemas-operacionais/29-varios-programas-ao-mesmo-tempo-parte-1/canonica.md`
- Aula 30 — *Vários Programas ao Mesmo Tempo - Parte 2* `aulas/introducao-a-computacao/arquitetura-computadores-e-sistemas-operacionais/30-varios-programas-ao-mesmo-tempo-parte-2/canonica.md`
- Aula 31 — *A Memória do Computador - Parte 1 - a Cache* `aulas/introducao-a-computacao/arquitetura-computadores-e-sistemas-operacionais/31-memoria-do-computador-parte-1-a-cache/canonica.md`
- Aula 32 — *A Memória do Computador - Parte 2 - a Hierarquia* `aulas/introducao-a-computacao/arquitetura-computadores-e-sistemas-operacionais/32-memoria-do-computador-parte-2-a-hierarquia/canonica.md`
- Aula 35 — *Sistema Operacional - Conceito e Estrutura* `aulas/introducao-a-computacao/arquitetura-computadores-e-sistemas-operacionais/35-sistema-operacional-conceito-e-estrutura/canonica.md`
- Aula 37 — *O Que o Sistema Operacional Faz por Você* `aulas/introducao-a-computacao/arquitetura-computadores-e-sistemas-operacionais/37-o-que-o-sistema-operacional-faz-por-voce/canonica.md`
- Aula 38 — *O Que é um Sistema Operacional - Definição e Onde Vivem* `aulas/introducao-a-computacao/arquitetura-computadores-e-sistemas-operacionais/38-o-que-e-um-sistema-operacional/canonica.md`
- Conceitos vizinhos: [[ciclo-de-instrucao]], [[registrador]], [[memoria-cache]], [[nucleo-de-processador]], [[escalonamento-de-processos]]

## Fontes

- Papel da CPU no sistema e nas quatro funções básicas: slides SEED das Aulas 23 e 24.
- Ciclo de instrução, contador de programa, clock e núcleos: slides SEED da Aula 28.
- Tradução de código até a execução: slides SEED da Aula 25.
- Multitarefa, paralelismo e escalonamento: slides SEED das Aulas 29 e 30.
- Cache e hierarquia de memória: slides SEED das Aulas 31 e 32.
- Papel da CPU sob o sistema operacional: slides SEED das Aulas 35 e 38, e `lake/introducao-a-computacao/rco/2tri/37-o-que-e-um-sistema-operacional.md` (Aula 37).
- Fluxo integrado disco → RAM → CPU: slides SEED da retomada (`AULA_RETOMADA_2_ INTRODUÇÃO A COMPUTAÇÃO.pptx`), base da canônica aprovada da Aula 2.
