---
titulo: Vários Programas ao Mesmo Tempo - Parte 1
tema: Multitarefa, processos e núcleos
disciplina: introducao-a-computacao
serie: 1ª
prerequisitos: [A CPU em Ação - o Ciclo de Instrução]
objetivos:
  - Definir processo como um programa em execução
  - Explicar como a multitarefa cria a ilusão de simultaneidade em um único núcleo
  - Diferenciar paralelismo real (multi-core) de alternância rápida
  - Reconhecer o papel do sistema operacional na divisão do tempo de CPU
trilha: arquitetura-computadores-e-sistemas-operacionais
ordem: 29
slug: varios-programas-ao-mesmo-tempo-parte-1
modo_origem: seed
fontes:
  - lake/introducao-a-computacao/AULA 29_INTRODUÇÃO A COMPUTAÇÃO.pptx
revisao: true
status: aprovada
versao: 1
atualizado_em: 2026-06-21
---

Na aula passada você aprendeu uma coisa que agora vira um problema: a CPU executa **uma** instrução de cada vez, na ordem do contador de programa. Beleza. Só que, neste exato momento, você provavelmente tem música tocando, um navegador aberto, mensagens chegando e ainda este material na tela. Tudo "ao mesmo tempo". Se a CPU faz uma coisa de cada vez, **como** ela dá conta de tantas coisas juntas? Ou será que "ao mesmo tempo" é só uma ilusão muito bem feita? Hoje você descobre o truque.

## Objetivos

Ao final desta aula, você será capaz de:

- Definir **processo** como um programa em execução.
- Explicar como a **multitarefa** cria a ilusão de simultaneidade em um único núcleo.
- Diferenciar **paralelismo real** (vários núcleos) de **alternância rápida**.
- Reconhecer o papel do **sistema operacional** ao dividir o tempo da CPU.

## Pré-requisitos

Ter visto a **Aula 28**: a CPU executa instruções uma a uma, em ciclos, e pode ter **vários núcleos**.

## Desenvolvimento

### Cada programa rodando é um processo

Primeiro, um nome para "um programa que está rodando":

:::conceito Processo
É um programa **em execução**. Não o arquivo guardado no disco, mas o programa **rodando agora**, ocupando memória e pedindo tempo da CPU. Abrir o mesmo programa duas vezes cria dois processos. Cada processo tem seu próprio espaço na memória.
:::

A diferença entre programa e processo é como a diferença entre uma receita e o bolo sendo feito. A receita (o arquivo no disco) fica parada, guardada. O processo é a receita **em ação**, com alguém mexendo a massa agora.

### O truque: alternância rápida demais para você notar

Agora o coração da aula. Suponha um computador com **um único núcleo** — capaz, como você viu, de uma instrução por vez. Como ele toca música e abre o navegador juntos?

A resposta é honesta e surpreendente: **ele não faz os dois ao mesmo tempo**. Ele alterna entre eles **tão rápido** que você não percebe.

:::conceito Multitarefa
É a técnica em que o sistema operacional **alterna rapidamente** entre vários processos, dando a cada um uma fatia minúscula de tempo da CPU. A troca é tão veloz (frações de segundo) que parece, para nós, que tudo roda simultaneamente — mas, em um único núcleo, só um processo usa a CPU em cada instante.
:::

:::exemplo
Pense num professor ajudando 4 alunos com dúvidas, mas com **um** professor só. Ele dá 10 segundos para o aluno 1, pula para o aluno 2 por 10 segundos, depois o 3, o 4, e volta ao 1 — girando rápido. Nenhum aluno é atendido literalmente ao mesmo tempo que outro, mas todos sentem que estão sendo acompanhados "juntos". A CPU de núcleo único faz isso, só que trocando milhares de vezes por segundo, rápido demais para qualquer um notar.
:::

### Quando a simultaneidade é de verdade: vários núcleos

A alternância rápida resolve o caso de um núcleo. Mas você viu na Aula 28 que CPUs modernas têm **vários núcleos**. Isso muda o jogo:

:::conceito Paralelismo real
Quando a CPU tem **vários núcleos**, processos diferentes podem rodar **de verdade ao mesmo tempo**, um em cada núcleo. Aí não é ilusão: é simultaneidade real. Um núcleo toca a música enquanto outro cuida do navegador, no mesmo instante.
:::

:::importante Os dois jeitos de "fazer várias coisas juntas"
- **Alternância rápida (1 núcleo):** a CPU reveza entre processos tão depressa que parece simultâneo. É ilusão de simultaneidade.
- **Paralelismo real (vários núcleos):** processos rodam genuinamente ao mesmo tempo, um por núcleo.
No dia a dia, o computador combina os dois: ele tem alguns núcleos (paralelismo real) e, em cada núcleo, ainda reveza entre muitos processos (alternância). É assim que dezenas de programas convivem com poucos núcleos.
:::

### Quem comanda o revezamento: o sistema operacional

Esse revezamento não acontece sozinho. Tem um maestro.

:::conceito Escalonamento
É a tarefa do **sistema operacional** de decidir **qual processo** usa a CPU **a cada momento** e por quanto tempo. O objetivo é que todos os processos recebam uma fatia justa de tempo e que o computador continue respondendo bem.
:::

:::dica Por que isso importa para quem desenvolve
Quando você abre o **Gerenciador de Tarefas** (Windows) ou o **Monitor de Atividade** (Mac) e vê a lista de processos com o quanto cada um usa de CPU, está olhando o escalonamento na prática. Um programa mal feito pode "segurar" a CPU e travar o resto — e diagnosticar isso é parte do trabalho de quem desenvolve e dá suporte. Entender processo, multitarefa e escalonamento é o primeiro passo para entender por que um sistema fica lento ou travado.
:::

:::atencao Erro comum
Achar que "ter mais programas abertos" significa que a CPU ficou "mais inteligente" para fazer tudo junto. Não: com um núcleo, ela continua fazendo uma coisa de cada vez — só reveza mais. É por isso que abrir programas demais deixa tudo lento: a CPU precisa dividir o mesmo tempo entre mais processos, e a fatia de cada um encolhe.
:::

## Prática

**Atividade "processador humano" (desplugada, 12 a 15 min).** A turma vai encenar a multitarefa e sentir a diferença entre revezar e paralelizar.

Escolha **1 aluno** para ser o **Processador** (núcleo único). Escolha 3 ou 4 alunos para serem **Processos**, cada um com uma tarefa contínua e simples (montar um quebra-cabeça pequeno, desenhar, copiar uma frase).

**Rodada 1 — um núcleo:** a regra é que cada Processo só pode trabalhar enquanto o Processador estiver **ao lado dele**. O Processador gira entre os Processos, ficando poucos segundos com cada um. Todos avançam "ao mesmo tempo"? Tecnicamente não — mas todos progridem. Cronometrem quanto tempo até todos terminarem.

**Rodada 2 — vários núcleos:** agora use **3 Processadores** ao mesmo tempo, cada um fixo em um Processo. Cronometrem de novo.

Discutam:

- Na Rodada 1, algum Processo estava **mesmo** trabalhando enquanto o Processador atendia outro? (Não — ilusão de simultaneidade.)
- Por que a Rodada 2 terminou mais rápido? (Paralelismo real.)
- Se houvesse **10** Processos para 1 Processador, o que aconteceria com a sensação de "rápido"?

**Extensão opcional no VSCode:** abra o Gerenciador de Tarefas / Monitor de Atividade enquanto roda alguns programas. Anote 3 processos e quanto cada um usa de CPU. Em 2 linhas, relacione o que você vê com a ideia de escalonamento.

## Avaliação

```quiz
- pergunta: O que é um processo?
  alternativas:
    - texto: Um arquivo guardado no disco rígido
    - texto: Um programa em execução, ocupando memória e pedindo tempo de CPU
      correta: true
    - texto: Um tipo de memória permanente
    - texto: O cabo que liga o computador à energia
  feedback: >
    Processo é o programa rodando agora — a receita em ação, não o arquivo
    parado. Cada processo tem seu espaço na memória e disputa tempo de CPU.
- pergunta: Como um computador de um único núcleo executa vários programas "ao mesmo tempo"?
  alternativas:
    - texto: Ele realmente executa todos simultaneamente
    - texto: Ele alterna entre os processos tão rápido que parece simultâneo (multitarefa)
      correta: true
    - texto: Ele desliga uns para ligar outros
    - texto: Ele copia os programas para a internet
  feedback: >
    Com um núcleo, a CPU faz uma coisa de cada vez. A multitarefa reveza entre os
    processos em frações de segundo, criando a ilusão de simultaneidade.
- pergunta: Qual é a diferença entre alternância rápida e paralelismo real?
  alternativas:
    - texto: Não há diferença, são a mesma coisa
    - texto: Na alternância, um núcleo reveza entre processos; no paralelismo real, vários núcleos rodam processos ao mesmo tempo de verdade
      correta: true
    - texto: A alternância só funciona desligada da tomada
    - texto: O paralelismo real só existe em celulares
  feedback: >
    Alternância (1 núcleo) é ilusão de simultaneidade por revezamento veloz.
    Paralelismo real (vários núcleos) é simultaneidade de verdade, um processo
    por núcleo.
```

## Fechamento

Hoje você desvendou a ilusão da simultaneidade:

- Um **processo** é um programa em execução, com seu espaço na memória.
- A **multitarefa** reveza entre processos tão rápido que parece simultâneo — em um núcleo, ainda é uma coisa de cada vez.
- **Vários núcleos** trazem **paralelismo real**: processos rodando ao mesmo tempo de verdade.
- O **sistema operacional** faz o **escalonamento**: decide quem usa a CPU e quando.

Você já entende a ideia geral do revezamento. Na próxima aula — **Parte 2** — a gente abre essa caixa: o que é dividir um processo em **threads**, como o sistema operacional escolhe a ordem e por que, às vezes, o vídeo trava mas a música continua tocando.

:::roteiro
Abrir explorando a tensão: "a CPU faz uma coisa de cada vez (Aula 28), mas você usa tudo junto — como?" Deixar a turma propor antes de revelar. O exemplo do professor com 4 alunos é o que faz a multitarefa "clicar"; vale encenar no quadro. Ser honesto: em um núcleo NÃO é simultâneo, é revezamento. Distinguir bem alternância × paralelismo real, porque a Aula 30 aprofunda threads e escalonamento. Na prática, a comparação cronometrada entre 1 e 3 processadores torna o paralelismo concreto. Fechar ganchando a Parte 2 (threads e o caso do vídeo travando).
:::
