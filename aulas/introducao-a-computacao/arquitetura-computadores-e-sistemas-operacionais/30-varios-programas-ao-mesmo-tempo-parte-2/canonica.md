---
titulo: Vários Programas ao Mesmo Tempo - Parte 2
tema: Threads, escalonamento e gargalos de desempenho
disciplina: introducao-a-computacao
serie: 1ª
prerequisitos: [Vários Programas ao Mesmo Tempo - Parte 1]
objetivos:
  - Definir thread como subtarefa dentro de um processo
  - Explicar como o escalonamento distribui tarefas leves e pesadas
  - Relacionar processos, threads e núcleos a gargalos de desempenho
  - Interpretar travamentos e lentidão a partir do uso de CPU
trilha: arquitetura-computadores-e-sistemas-operacionais
ordem: 30
slug: varios-programas-ao-mesmo-tempo-parte-2
modo_origem: seed
fontes:
  - lake/introducao-a-computacao/AULA 30_INTRODUÇÃO A COMPUTAÇÃO.pptx
revisao: true
status: aprovada
versao: 1
atualizado_em: 2026-06-21
---

Tem uma cena que todo mundo já viveu: você está editando um vídeo, ouvindo música e navegando, e de repente o **vídeo trava** — mas a música **continua tocando lisinha**. Estranho, né? Se o computador travou, por que não travou tudo? A resposta a esse mistério está na peça que faltava da aula passada. Você já sabe que o sistema operacional reveza entre processos. Hoje a gente vai um nível mais fundo: dentro de cada processo existem **subtarefas**, e é a forma como o sistema distribui essas subtarefas que explica por que uma coisa engasga enquanto a outra voa.

## Objetivos

Ao final desta aula, você será capaz de:

- Definir **thread** como uma subtarefa dentro de um processo.
- Explicar como o **escalonamento** distribui tarefas leves e pesadas.
- Relacionar **processos, threads e núcleos** a gargalos de desempenho.
- Interpretar **travamentos e lentidão** a partir do uso de CPU.

## Pré-requisitos

Ter visto a **Aula 29**: processo é programa em execução, multitarefa é alternância rápida, paralelismo real vem de vários núcleos, e o sistema operacional faz o escalonamento.

## Desenvolvimento

### Dentro de um processo cabe mais de uma tarefa

Na Parte 1, a menor unidade era o processo. Mas um processo pode fazer várias coisas internas ao mesmo tempo. Pense num editor de vídeo: ele exibe a prévia, processa o áudio, salva o projeto de fundo — tudo dentro do **mesmo** programa. Cada uma dessas linhas de trabalho é uma **thread**.

:::conceito Thread
É uma **subtarefa** dentro de um processo — uma linha de execução que faz parte do programa. Um único processo pode ter **várias threads** rodando coisas diferentes ao mesmo tempo. Por exemplo, num jogo: uma thread cuida da imagem, outra do som, outra da rede.
:::

A relação encaixa em três níveis, do maior para o menor:

```diagrama-progressivo
titulo: Do programa à subtarefa
camadas:
  - rotulo: 1. Processo
    conteudo: Um programa em execução (o editor de vídeo inteiro). Tem seu espaço próprio na memória.
  - rotulo: 2. Threads
    conteudo: Subtarefas dentro do processo (exibir a prévia, processar o áudio, salvar). Várias podem rodar ao mesmo tempo.
  - rotulo: 3. Núcleos
    conteudo: As unidades físicas da CPU que de fato executam as threads. Mais núcleos = mais threads rodando em paralelo de verdade.
```

:::atencao Erro comum
Confundir **thread** com **programa instalado** ou com um **tipo de memória**. Thread não é um app e não é hardware: é uma **subtarefa** dentro de um processo, uma linha de execução. Quando alguém diz "esse jogo usa muitas threads", quer dizer que ele divide o trabalho interno em várias linhas que podem rodar em paralelo.
:::

### O escalonador como um gerente justo

Com tantos processos e threads disputando poucos núcleos, alguém precisa distribuir o tempo. Esse é o trabalho do **escalonamento**, que você conheceu na Parte 1 — agora visto mais de perto.

:::conceito Escalonamento (revisitado)
É o sistema operacional decidindo, a cada instante, **qual** thread ou processo usa a CPU e **por quanto tempo**. Ele leva em conta o peso de cada tarefa: tarefas leves e contínuas ganham fatias pequenas e frequentes; tarefas pesadas pedem mais. O objetivo é manter o sistema **responsivo** e dividir os recursos de forma equilibrada.
:::

### O mistério do vídeo travado, resolvido

Agora dá para explicar a cena do começo.

:::importante Por que o vídeo trava mas a música não
Tocar música é uma tarefa **leve e contínua**: pede pouca CPU e é fácil de manter rodando em fatias pequenas. Editar vídeo é uma tarefa **pesada**: exige muito processamento. Quando o uso de CPU chega perto do limite — ou não há núcleos suficientes — o escalonador ainda consegue encaixar a tarefa leve (música) nas brechas, mas a tarefa pesada (vídeo) não recebe tempo suficiente e **engasga**. Não é o computador inteiro que travou: é uma tarefa pesada sem CPU suficiente, enquanto as leves seguem nas frestas.
:::

:::conceito Gargalo de desempenho
É o ponto que **limita** a velocidade do sistema — o "pescoço estreito da garrafa". Pode ser a CPU sem núcleos suficientes, a RAM lotada, ou um disco lento. Quando algo trava, identificar o gargalo é descobrir **qual recurso** está no limite.
:::

:::dica O raciocínio profissional por trás do "está travando"
Quem desenvolve ou dá suporte não para em "o programa travou". Pergunta: o uso de **CPU** está no talo? Provável gargalo de processamento — talvez faltem núcleos para tantas threads pesadas. A **RAM** está cheia? Outro gargalo. O **disco** está a 100%? Mais outro. Cada gargalo pede uma solução diferente. Entender processos, threads e escalonamento é o que transforma "tá travando" em um **diagnóstico**.
:::

### Por que isso vale a pena entender

Saber como o computador distribui o trabalho permite quatro coisas concretas, hoje e na carreira:

- **Otimizar programas** — escrever software que aproveita vários núcleos.
- **Entender gargalos** — descobrir qual recurso limita o desempenho.
- **Resolver travamentos e lentidão** — diagnosticar a causa, não só reclamar do sintoma.
- **Desenvolver aplicações mais eficientes** — dividir tarefas pesadas em threads bem pensadas.

## Prática

**Atividade "central de tarefas" (desplugada, 12 a 15 min).** A turma vai sentir na pele o escalonamento de tarefas leves e pesadas.

Escolha **1 aluno** como **Processador** (CPU). Os demais formam **processos**, e alguns processos terão **mais de uma thread** (mais de uma tarefa ao mesmo tempo). Distribua tarefas com pesos diferentes:

| Tarefa | Peso |
|---|---|
| bater palma a cada 5 segundos | leve e contínua (a "música") |
| resolver uma conta de cabeça difícil | pesada (o "vídeo") |
| dizer "presente" quando chamado | leve |

O **Processador** só pode dar atenção a uma tarefa por vez e precisa **revezar**. A regra: tarefas leves recebem visitas curtas e frequentes; a tarefa pesada precisa de visitas longas para avançar.

Rodem por alguns minutos e discutam:

- A tarefa leve (palmas) conseguiu se manter "rodando" mesmo quando a pesada travava? Por quê?
- Se entrasse uma **segunda** tarefa pesada, o que aconteceria com o ritmo de todas?
- Onde estava o **gargalo**: na quantidade de "núcleos" (Processadores) ou no peso das tarefas?

**Extensão opcional no VSCode:** com o Gerenciador de Tarefas / Monitor de Atividade aberto, rode um programa leve e um pesado ao mesmo tempo. Observe a coluna de CPU. Em 3 linhas, identifique qual tarefa é o provável gargalo e por quê.

## Avaliação

```quiz
- pergunta: O que é uma thread?
  alternativas:
    - texto: Um programa instalado no computador
    - texto: Uma subtarefa (linha de execução) dentro de um processo
      correta: true
    - texto: Um tipo de memória permanente
    - texto: Uma peça de hardware do computador
  feedback: >
    Thread é uma subtarefa dentro de um processo. Um mesmo programa pode ter
    várias threads — som, imagem, rede — rodando ao mesmo tempo.
- pergunta: Por que, às vezes, um vídeo pesado trava enquanto a música continua tocando?
  alternativas:
    - texto: Porque a música está guardada na nuvem
    - texto: Porque a tarefa leve (música) cabe nas frestas de CPU, mas a tarefa pesada (vídeo) não recebe tempo suficiente
      correta: true
    - texto: Porque o vídeo desligou o processador
    - texto: Porque música e vídeo usam teclados diferentes
  feedback: >
    O escalonador encaixa a tarefa leve e contínua nas brechas de CPU. A tarefa
    pesada precisa de muito processamento e engasga quando a CPU está no limite.
- pergunta: O que é um gargalo de desempenho?
  alternativas:
    - texto: Um vírus que apaga arquivos
    - texto: O recurso que está no limite e limita a velocidade do sistema (CPU, RAM ou disco)
      correta: true
    - texto: Um cabo solto na parte de trás do computador
    - texto: Um programa que abre sozinho
  feedback: >
    Gargalo é o "pescoço estreito da garrafa": o recurso no limite que segura o
    desempenho. Diagnosticar é descobrir qual recurso (CPU, RAM ou disco) está
    saturado.
```

## Fechamento

Hoje você fechou o quebra-cabeça da simultaneidade:

- Uma **thread** é uma subtarefa dentro de um processo; um processo pode ter várias.
- O **escalonamento** distribui o tempo da CPU entre tarefas leves e pesadas.
- **Processos, threads e núcleos** juntos explicam por que algo trava enquanto outra coisa segue.
- Identificar o **gargalo** (CPU, RAM ou disco) transforma "está lento" em diagnóstico.

A gente já falou bastante de CPU e de tempo de processamento. Mas teve um detalhe escondido por trás de tudo: a CPU precisa que os dados cheguem **rápido** até ela, ou todo esse revezamento veloz não adianta. Na próxima aula, vamos olhar a memória mais de perto e conhecer uma peça pouco falada, mas decisiva para a velocidade: a **memória cache**.

:::roteiro
Abrir pela cena do vídeo travado com a música tocando — é o gancho perfeito porque é universal e contraintuitivo. Construir thread como "subtarefa dentro do processo" e amarrar os três níveis (processo > threads > núcleos) com o diagrama. O :::importante do vídeo travado é o clímax: voltar a ele depois de apresentar escalonamento e gargalo. Reforçar o salto profissional — de "travou" para "qual recurso é o gargalo". Na prática, a entrada de uma segunda tarefa pesada mostra o gargalo na pele. Fechar ganchando a Aula 31 (cache): de nada adianta CPU veloz se os dados chegam devagar.
:::
