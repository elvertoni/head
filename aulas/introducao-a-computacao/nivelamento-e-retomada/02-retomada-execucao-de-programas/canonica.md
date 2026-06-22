---
titulo: Retomada - Entendendo a Execução de Programas
tema: Revisão integrada de armazenamento, memória e processador
disciplina: introducao-a-computacao
serie: 1ª
prerequisitos: [A CPU em Ação - o Ciclo de Instrução]
objetivos:
  - Revisar o fluxo de um programa, do armazenamento até a execução
  - Relacionar disco, RAM e CPU em um único percurso
  - Reaplicar o ciclo de instrução a um exemplo integrado
trilha: nivelamento-e-retomada
ordem: 2
slug: retomada-execucao-de-programas
modo_origem: seed
fontes:
  - lake/introducao-a-computacao/AULA_RETOMADA_2_ INTRODUÇÃO A COMPUTAÇÃO.pptx
revisao: true
status: aprovada
versao: 1
atualizado_em: 2026-06-21
---

Você já viu, em aulas separadas, onde os programas ficam guardados (Aula 27), como a memória trabalha (Aulas 31 e 32) e como a CPU executa instruções (Aula 28). Cada peça fez sentido sozinha. Mas no mundo real elas não trabalham isoladas — elas formam **um único fluxo**, do momento em que você dá dois cliques num programa até ele aparecer rodando na tela. Esta é uma aula de retomada: em vez de conteúdo novo, a gente vai **costurar** o que você já sabe num percurso só, para que a história inteira fique clara. Quando terminar, você vai conseguir narrar a viagem de um programa, do disco até a execução, sem pular nenhuma estação.

## Objetivos

Ao final desta aula, você será capaz de:

- Revisar o **fluxo** de um programa, do **armazenamento** até a **execução**.
- Relacionar **disco, RAM e CPU** em um **único percurso**.
- Reaplicar o **ciclo de instrução** a um exemplo integrado.

## Pré-requisitos

Ter visto a **Aula 27** (RAM × disco), a **Aula 28** (ciclo de instrução) e, de apoio, as **Aulas 31 e 32** (cache e hierarquia de memória).

## Desenvolvimento

### Três peças que você já conhece

Antes de juntar, um lembrete rápido de cada estação da viagem:

:::conceito As três estações da execução
- **Armazenamento (disco — HDD/SSD):** guarda o programa de forma **permanente**, mesmo desligado. É de onde tudo parte.
- **Memória RAM:** guarda o programa e os dados **enquanto ele roda**. Rápida, mas volátil — some ao desligar.
- **CPU (processador):** **executa** as instruções, uma a uma, no ciclo buscar → decodificar → executar → armazenar.
:::

Nenhuma dessas ideias é nova para você. O que talvez ainda não esteja firme é **como elas se conectam** numa sequência.

### A viagem de um programa, do clique à tela

Quando você abre um programa, acontece um percurso na ordem certa. Vamos segui-lo.

```diagrama-progressivo
titulo: A viagem de um programa até rodar
camadas:
  - rotulo: 1. Repouso no disco
    conteudo: O programa está guardado no armazenamento permanente (HDD/SSD). Parado, esperando ser chamado.
  - rotulo: 2. Sobe para a RAM
    conteudo: Ao abrir o programa, ele é copiado do disco para a memória RAM, onde fica acessível e rápido para a CPU usar.
  - rotulo: 3. A CPU executa
    conteudo: A CPU busca as instruções na RAM e roda o ciclo (buscar, decodificar, executar, armazenar) repetidamente.
  - rotulo: 4. Resultado na tela
    conteudo: O processamento vira imagem, som ou ação. Você vê o programa funcionando.
```

:::importante O fio que liga tudo
Um programa **mora** no disco, **trabalha** na RAM e é **executado** pela CPU. Disco é o "sempre", RAM é o "agora", CPU é o "fazer". Sempre que pensar em desempenho — por que algo demora a abrir, por que trava, por que voa —, pergunte em qual dessas três estações está o problema.
:::

### Reaplicando o ciclo de instrução

Para fechar, vamos ver a CPU em ação dentro desse fluxo, com um exemplo concreto. Suponha um programa minúsculo que soma dois números e mostra o resultado. Depois de ele subir para a RAM, a CPU trabalha assim:

:::exemplo
| Ciclo | Buscar | Decodificar | Executar | Armazenar |
|---|---|---|---|---|
| 1 | pega "carregar o número 5" | entende: pôr 5 num registrador | põe 5 | guarda 5 |
| 2 | pega "somar 3" | entende: adicionar 3 ao valor | 5 + 3 | guarda 8 |
| 3 | pega "mostrar resultado" | entende: enviar para a tela | envia 8 | exibe 8 |

Três voltas do mesmo ciclo, na ordem que o contador de programa aponta, e o `5 + 3` vira **8** na tela. É a Aula 28 acontecendo dentro do fluxo que começou no disco.
:::

:::dica O raciocínio que essa visão integrada te dá
Com o fluxo inteiro na cabeça, você diagnostica de verdade. "Demora a **abrir**" → a viagem do disco para a RAM está lenta (talvez um HDD antigo). "Trava com **vários programas**" → a RAM lotou (estação 2). "Roda, mas **devagar**" → pode ser a CPU no limite (estação 3). Quem enxerga as três estações conectadas não chuta: localiza a estação do gargalo. É assim que pensa um profissional de suporte e de desenvolvimento.
:::

:::atencao Erro comum
Achar que o programa "roda direto do disco". Não: ele precisa **subir para a RAM** antes de a CPU conseguir executá-lo com agilidade. O disco é permanente, mas lento demais para a CPU trabalhar diretamente nele o tempo todo. Pular a estação da RAM no seu raciocínio é o erro que mais atrapalha na hora de explicar por que um computador está lento.
:::

## Prática

**Atividade "narradores da viagem" (desplugada, 12 a 15 min).** A turma reconstrói o fluxo inteiro e o explica em voz alta.

**Parte 1 — ordenar a viagem (em grupos):** o professor entrega cartões embaralhados com as etapas: *"programa guardado no disco"*, *"programa copiado para a RAM"*, *"CPU busca a instrução"*, *"CPU executa o ciclo"*, *"resultado aparece na tela"*. Os grupos colocam na ordem correta.

**Parte 2 — narrar (em grupos):** cada grupo escolhe um programa real (um jogo, um navegador) e **narra a viagem dele** em 4 ou 5 frases, do clique até a tela, usando as palavras disco, RAM e CPU.

**Parte 3 — diagnóstico (turma):** o professor lê sintomas e a turma aponta a **estação** provável:

- "Demora muito para abrir." → ?
- "Trava quando abro muitos programas." → ?
- "Abre rápido, mas roda travando nos momentos pesados." → ?

Fechem discutindo: por que o programa precisa **subir para a RAM** antes de a CPU executá-lo bem?

**Extensão opcional no VSCode:** rode um programinha que soma dois números e mostra o resultado. Em 3 frases, descreva a viagem desse programa do arquivo no disco até o número aparecer no terminal, citando disco, RAM e CPU.

## Avaliação

```quiz
- pergunta: Qual é a ordem correta do fluxo de execução de um programa?
  alternativas:
    - texto: CPU executa → sobe para a RAM → fica no disco
    - texto: Fica no disco → sobe para a RAM → CPU executa → resultado na tela
      correta: true
    - texto: Aparece na tela → vai para o disco → some
    - texto: Vai direto do disco para a tela, sem RAM nem CPU
  feedback: >
    O programa mora no disco (permanente), é copiado para a RAM (rápida) ao abrir,
    e então a CPU executa as instruções. O resultado aparece na tela.
- pergunta: Por que um programa precisa ser copiado para a RAM antes de rodar bem?
  alternativas:
    - texto: Porque o disco apaga os programas ao ligar
    - texto: Porque o disco é lento demais para a CPU trabalhar diretamente nele o tempo todo; a RAM é rápida
      correta: true
    - texto: Porque a RAM guarda os dados para sempre
    - texto: Porque a CPU não consegue ler binário
  feedback: >
    A RAM é muito mais rápida que o disco. O programa sobe para a RAM para a CPU
    acessá-lo com agilidade. O disco guarda; a RAM serve o trabalho do momento.
- pergunta: Um computador "trava quando abro muitos programas ao mesmo tempo". Qual estação é o provável gargalo?
  alternativas:
    - texto: O disco rígido está apagado
    - texto: A RAM, que lota quando muitos programas estão em uso ao mesmo tempo
      correta: true
    - texto: A tela está com defeito
    - texto: O contador de programa parou
  feedback: >
    Muitos programas abertos lotam a RAM (a estação do "agora"). Demora para abrir
    aponta o disco; lentidão em tarefas pesadas aponta a CPU. Cada sintoma, uma estação.
```

## Fechamento

Esta retomada costurou as peças num fluxo só:

- Um programa **mora no disco**, **trabalha na RAM** e é **executado pela CPU**.
- A viagem é: **disco → RAM → CPU → tela**, nessa ordem.
- A CPU executa rodando o **ciclo de instrução** (buscar, decodificar, executar, armazenar).
- Localizar a **estação** certa (disco, RAM ou CPU) transforma "está lento" em diagnóstico.

Com o fluxo inteiro firme, todas as aulas anteriores deixam de ser peças soltas e viram uma história única — a história de como o seu programa sai de um arquivo parado e ganha vida na tela. Esse é o mapa que você leva para tudo o que vier a desenvolver.

:::roteiro
Aula de RETOMADA: zero conteúdo novo, tudo é integração. O objetivo é a turma conseguir NARRAR o fluxo disco→RAM→CPU→tela sem pular etapa. Usar o diagrama da viagem como espinha e a tabela do ciclo (5+3=8) para reativar a Aula 28 dentro do fluxo. O :::importante (disco=sempre, RAM=agora, CPU=fazer) é o resumo de bolso — repetir. A parte de diagnóstico por sintomas é o ponto alto: liga teoria à dor real do usuário e mostra valor profissional. O :::atencao (não roda direto do disco) corrige o erro mais comum. Como é revisão, priorizar a fala dos alunos sobre a explicação do professor.
:::
