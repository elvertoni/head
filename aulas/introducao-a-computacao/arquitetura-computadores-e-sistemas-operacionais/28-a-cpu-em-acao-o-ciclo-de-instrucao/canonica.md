---
titulo: A CPU em Ação - o Ciclo de Instrução
tema: Execução de programas e ciclo de instrução
disciplina: introducao-a-computacao
serie: 1ª
prerequisitos: [Memória e Armazenamento - o Temporário e o Permanente]
objetivos:
  - Descrever as etapas do ciclo de instrução (buscar, decodificar, executar, armazenar)
  - Explicar o papel do contador de programa na ordem das instruções
  - Relacionar velocidade de clock e número de núcleos ao desempenho
  - Reconhecer que um programa é uma sequência de instruções para a CPU
trilha: arquitetura-computadores-e-sistemas-operacionais
ordem: 28
slug: a-cpu-em-acao-o-ciclo-de-instrucao
modo_origem: seed
fontes:
  - lake/introducao-a-computacao/AULA 28_INTRODUÇÃO A COMPUTAÇÃO.pptx
revisao: true
status: aprovada
versao: 1
atualizado_em: 2026-06-21
---

Seu código virou binário (Aulas 25 e 26) e está guardado na memória (Aula 27). Agora vem a parte mágica — só que não é mágica nenhuma, é um processo. A CPU pega aquelas instruções e **executa** uma por uma, numa velocidade que beira o absurdo: bilhões de vezes por segundo. Mas como ela sabe **qual** instrução vem primeiro? E a próxima? E a próxima? A resposta é um ciclo simples, repetido sem parar enquanto o computador está ligado. Hoje você vai ver o coração do computador batendo.

## Objetivos

Ao final desta aula, você será capaz de:

- Descrever as etapas do **ciclo de instrução**: buscar, decodificar, executar, armazenar.
- Explicar o papel do **contador de programa** na ordem das instruções.
- Relacionar **velocidade de clock** e **número de núcleos** ao desempenho.
- Reconhecer que um **programa** nada mais é que uma **sequência de instruções**.

## Pré-requisitos

Ter visto a **Aula 24** (a CPU busca, interpreta, executa e guarda — apresentado por cima) e a **Aula 27** (instruções e dados ficam guardados na memória).

## Desenvolvimento

### Um programa é uma fila de ordens

Antes de ver a CPU trabalhar, uma ideia que muda tudo: para o computador, um programa **não** é uma coisa só. É uma **lista de instruções** pequenas e simples, uma atrás da outra, esperando para serem executadas na ordem.

:::conceito Instrução
É uma única ordem que a CPU sabe executar — algo bem básico, como "some estes dois números", "mova este dado para ali" ou "compare estes dois valores". Programas grandes são feitos de **milhões** dessas ordens simples, executadas em sequência e em altíssima velocidade.
:::

A CPU não faz uma tarefa gigante de uma vez. Ela faz um zilhão de tarefinhas minúsculas, rápido demais para a gente perceber.

### O ciclo de instrução: o batimento da CPU

Para executar cada instrução, a CPU repete sempre as mesmas quatro etapas. Esse é o **ciclo de instrução**.

:::conceito Ciclo de instrução
É a sequência de etapas que a CPU repete para executar cada instrução: **buscar** a instrução na memória, **decodificar** (entender o que ela pede), **executar** a operação e **armazenar** o resultado. Terminou uma, começa a próxima — sem parar, enquanto o computador estiver ligado.
:::

```diagrama-progressivo
titulo: As quatro etapas que se repetem sem parar
camadas:
  - rotulo: 1. Buscar (fetch)
    conteudo: A CPU vai até a memória e pega a próxima instrução que precisa executar.
  - rotulo: 2. Decodificar (decode)
    conteudo: A CPU interpreta a instrução para descobrir o que ela está mandando fazer.
  - rotulo: 3. Executar (execute)
    conteudo: A CPU realiza a operação — soma, comparação, movimento de dados, o que a instrução pediu.
  - rotulo: 4. Armazenar (store)
    conteudo: O resultado é guardado, e a CPU já parte para buscar a próxima instrução. O ciclo recomeça.
```

### O contador de programa: quem marca o lugar

Mas falta responder à pergunta do começo: como a CPU sabe **qual** é a "próxima" instrução? Ela não decora a lista. Ela usa um marcador.

:::conceito Contador de programa
É um pequeno registrador dentro da CPU que guarda a **posição da próxima instrução** a ser executada. Depois que uma instrução é executada, o contador avança para apontar a seguinte. É ele que garante que o programa seja executado **na ordem certa**.
:::

Pense em ler um livro e usar o dedo para marcar a linha que você está lendo. Quando termina a linha, o dedo desce para a próxima. O contador de programa é esse dedo: ele nunca deixa a CPU se perder sobre onde parou.

:::exemplo
Imagine três instruções guardadas na memória, nas posições 1, 2 e 3:

| Posição | Instrução |
|---|---|
| 1 | pegue o número 5 |
| 2 | some 3 a ele |
| 3 | mostre o resultado |

O contador começa apontando para a posição 1. A CPU busca, decodifica, executa e armazena. O contador avança para 2. Mesmo ciclo. Avança para 3. Mesmo ciclo. É essa repetição disciplinada que faz `5 + 3` virar `8` na tela.
:::

:::atencao Erro comum
Chamar a CPU de "cérebro" e achar que ela **pensa** ou decide sozinha o que fazer. A CPU não tem ideias. Ela segue a lista de instruções, na ordem que o contador aponta, cegamente e rápido. A inteligência está em **quem escreveu o programa** — ou seja, em você. A CPU é uma executora obediente e veloz, não uma pensadora.
:::

### O que faz uma CPU ser mais rápida

Se toda CPU faz o mesmo ciclo, por que umas são mais rápidas que outras? Dois fatores principais:

:::conceito Velocidade de clock
É o ritmo em que a CPU executa os ciclos, medido em **hertz** (geralmente gigahertz, GHz). Um clock de 3 GHz significa cerca de **3 bilhões** de ciclos por segundo. Quanto maior o clock, mais instruções por segundo — em geral, mais velocidade.
:::

:::conceito Núcleo
É uma unidade de processamento completa dentro da CPU. Uma CPU com vários núcleos (**multi-core**) pode executar vários ciclos de instrução **ao mesmo tempo**, um em cada núcleo — como ter vários trabalhadores em vez de um só.
:::

:::dica Por que isso aparece na hora de comprar um computador
Quando você lê "processador de 3.2 GHz, 8 núcleos" numa loja, agora você sabe ler isso: 3.2 GHz é o **ritmo** de cada núcleo (quão rápido ele repete o ciclo) e 8 núcleos é **quantos** trabalham em paralelo. Um programa pesado roda melhor quando consegue dividir o trabalho entre vários núcleos. Entender isso evita cair em propaganda e ajuda a escolher a máquina certa para cada uso.
:::

## Prática

**Atividade "vira CPU" (desplugada, 12 a 15 min).** Cada grupo vai *ser* um processador e sentir o ciclo de instrução no corpo.

Divida a turma em grupos de 3. Dentro de cada grupo, três papéis:

| Papel | Faz o quê |
|---|---|
| **Buscador** | vai até a "memória" (uma área da sala com cartões) e traz o próximo cartão |
| **Decodificador** | lê o cartão e diz qual ação ele representa |
| **Executor** | realiza a ação |

O professor espalha cartões coloridos na "memória", cada cor com um significado combinado (ex.: vermelho = bater palma, azul = levantar a mão, verde = dizer "pronto"). Os cartões ficam **numerados em ordem** — esse número faz o papel do contador de programa.

Ao iniciar o cronômetro, o ciclo roda: o **Buscador** traz o cartão 1, o **Decodificador** anuncia a ação, o **Executor** realiza — e então parte-se para o cartão 2, depois o 3, sempre na ordem do número. Rodem por um tempo combinado.

Depois, discutam:

- O que aconteceria se o **Buscador** pegasse os cartões fora de ordem? (Quebra do contador de programa.)
- Se houvesse **dois grupos** trabalhando em metades diferentes da lista ao mesmo tempo, o trabalho terminaria mais rápido? (Ideia de **núcleos**.)
- Se vocês fizessem o ciclo **mais rápido**, processariam mais cartões no mesmo tempo? (Ideia de **clock**.)

**Extensão opcional no VSCode:** escreva um programa de 3 linhas que guarda um número, soma outro e mostra o resultado (ex.: `a = 5` / `b = a + 3` / `print(b)`). Em 3 linhas, explique por que a **ordem** das linhas importa — e relacione isso com o contador de programa.

## Avaliação

```quiz
- pergunta: Quais são as etapas do ciclo de instrução que a CPU repete?
  alternativas:
    - texto: Ligar, carregar, navegar e desligar
    - texto: Buscar, decodificar, executar e armazenar
      correta: true
    - texto: Salvar, imprimir, copiar e colar
    - texto: Baixar, instalar, abrir e fechar
  feedback: >
    A CPU busca a instrução na memória, decodifica para entender o que fazer,
    executa a operação e armazena o resultado — e repete isso sem parar.
- pergunta: Qual é a função do contador de programa?
  alternativas:
    - texto: Guardar a posição da próxima instrução a ser executada, mantendo a ordem
      correta: true
    - texto: Contar quantos programas estão instalados no computador
    - texto: Medir a temperatura do processador
    - texto: Guardar as fotos do usuário
  feedback: >
    O contador de programa é como um dedo marcando a linha: aponta a próxima
    instrução e avança a cada ciclo, garantindo que o programa rode na ordem certa.
- pergunta: O que significa uma CPU ter vários núcleos (multi-core)?
  alternativas:
    - texto: Que ela tem vários monitores
    - texto: Que ela pode executar vários ciclos de instrução ao mesmo tempo, um por núcleo
      correta: true
    - texto: Que ela guarda mais arquivos permanentes
    - texto: Que ela nunca esquenta
  feedback: >
    Cada núcleo é uma unidade de processamento completa. Vários núcleos permitem
    executar instruções em paralelo, como ter vários trabalhadores em vez de um.
```

## Fechamento

Hoje você viu o coração do computador bater:

- Um **programa** é uma **sequência de instruções** simples para a CPU.
- A CPU repete o **ciclo de instrução**: buscar, decodificar, executar, armazenar.
- O **contador de programa** marca a próxima instrução e garante a ordem.
- **Velocidade de clock** (ritmo) e **número de núcleos** (quantos trabalham juntos) definem boa parte do desempenho.

Você viu a CPU executar **um** fluxo de instruções, na ordem. Mas no seu dia a dia você usa vários programas ao mesmo tempo — música, navegador, mensagens. Como uma CPU que executa uma instrução de cada vez consegue dar conta de tudo isso junto? É exatamente o mistério da próxima aula.

:::roteiro
Abrir conectando as aulas anteriores: o código já é binário, já está na memória — agora a CPU age. Vender o ciclo de instrução como um "batimento" que nunca para; a imagem do dedo marcando a linha (contador de programa) é o que faz a ordem fazer sentido. O :::atencao sobre "CPU não pensa" é importante: desfaz a mística do cérebro e devolve o protagonismo ao programador. Na prática do "vira CPU", o momento de ouro é a discussão final — fora de ordem (quebra o contador), dois grupos (núcleos), mais rápido (clock) plantam as três sementes. Fechar com o gancho forte da Aula 29: uma CPU, vários programas ao mesmo tempo — como?
:::
