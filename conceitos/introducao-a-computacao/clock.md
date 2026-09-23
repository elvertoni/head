---
conceito: Clock
slug: clock
disciplina: introducao-a-computacao
tipo: conceito
aka: [velocidade de clock, clock speed, frequência de clock]
status: rascunho
fontes:
  - "lake/introducao-a-computacao/AULA 28_INTRODUÇÃO A COMPUTAÇÃO.pptx"
aulas: [28]
atualizado_em: 2026-09-22
---

Clock é o ritmo em que a CPU executa ciclos, medido em hertz — normalmente em gigahertz (GHz) nos processadores atuais. Um clock de 3 GHz significa cerca de 3 bilhões de ciclos por segundo; quanto maior o clock, mais instruções por segundo cada núcleo consegue processar, em geral.

## Em uma frase

Clock é o ritmo, em ciclos por segundo, com que a CPU executa instruções.

## O que precisa saber

O clock mede a velocidade de cada [[nucleo-de-processador|núcleo]] isoladamente: é diferente de quantos núcleos a CPU tem, que é o segundo fator de desempenho ao lado do clock. Ao ler uma especificação como "3.2 GHz, 8 núcleos", o 3.2 GHz descreve o ritmo de cada núcleo repetindo o [[ciclo-de-instrucao]], e os 8 núcleos descrevem quantos trabalham em paralelo — os dois números respondem perguntas diferentes sobre desempenho e não devem ser somados nem confundidos. Um programa que não divide seu trabalho entre múltiplos núcleos depende quase inteiramente do clock; um programa bem paralelizado se beneficia mais de ter mais núcleos do que de um clock mais alto.

## Erros comuns

- Achar que clock mais alto sempre significa computador proporcionalmente mais rápido, ignorando o número de núcleos e se o software aproveita paralelismo.
- Confundir clock (ritmo de cada núcleo) com número de núcleos (quantos trabalham ao mesmo tempo) ao ler especificações de hardware.

## Onde aparece

- Aula 28 — *A CPU em Ação - o Ciclo de Instrução* `aulas/introducao-a-computacao/arquitetura-computadores-e-sistemas-operacionais/28-a-cpu-em-acao-o-ciclo-de-instrucao/canonica.md`
- Conceitos vizinhos: [[nucleo-de-processador]], [[ciclo-de-instrucao]], [[cpu]]

## Fontes

- Slides SEED da aula 28 (`lake/introducao-a-computacao/AULA 28_INTRODUÇÃO A COMPUTAÇÃO.pptx`), slide 13: velocidade de relógio e número de núcleos como fatores de eficiência do processador.
- Base da canônica aprovada da aula 28, bloco :::conceito Velocidade de clock e a dica sobre leitura de especificações de hardware.
