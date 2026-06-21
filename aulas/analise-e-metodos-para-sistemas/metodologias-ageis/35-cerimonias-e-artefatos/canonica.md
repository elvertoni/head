---
titulo: Cerimônias e Artefatos do Scrum
tema: Metodologias Ágeis
disciplina: analise-e-metodos-para-sistemas
serie: 1ª
prerequisitos: [Introdução ao Scrum]
objetivos:
  - Reconhecer as quatro cerimônias do Scrum e para que serve cada uma
  - Diferenciar Product Backlog, Sprint Backlog e incremento
  - Relacionar as cerimônias aos pilares de transparência, inspeção e adaptação
trilha: metodologias-ageis
ordem: 35
slug: cerimonias-e-artefatos
modo_origem: seed
fontes:
  - lake/analise-e-metodos-para-sistemas/AULA 35_ANÁLISE E MÉTODO PARA SISTEMAS.pptx
revisao: true
status: aprovada
versao: 2
atualizado_em: 2026-06-21
---

Imagina um time de futebol que nunca conversa: ninguém combina jogada, ninguém revê o que deu errado no primeiro tempo, ninguém sabe o placar. Vira bagunça. Um time Scrum evita isso com **reuniões curtas e combinadas** (as cerimônias) e **listas vivas** que todo mundo enxerga (os artefatos). Na aula passada você montou o time e a lista de tarefas; agora vai ver como esse time se acompanha no dia a dia para nunca se perder.

## Objetivos

Ao final desta aula, você será capaz de:

- Reconhecer as **quatro cerimônias** do Scrum e para que serve cada uma.
- Diferenciar **Product Backlog**, **Sprint Backlog** e **incremento**.
- Relacionar as cerimônias aos pilares de **transparência, inspeção e adaptação**.

## Pré-requisitos

Ter visto a **Aula 34** (papéis do Scrum e Product Backlog).

## Desenvolvimento

### Em uma frase

:::importante
As cerimônias deixam o trabalho visível, enquanto os artefatos mostram o que entra, o que sai e o que fica pronto.
:::

### As quatro cerimônias

Cerimônias são as reuniões combinadas do Scrum. Cada sprint tem quatro momentos:

```diagrama-progressivo
titulo: Uma sprint do começo ao fim
camadas:
  - rotulo: 1. Sprint Planning (início)
    conteudo: O time escolhe, do Product Backlog, o que vai fazer nesta sprint e monta o plano. Define a meta do ciclo.
  - rotulo: 2. Daily Stand-up (todo dia)
    conteudo: Reunião rápida, de pé, de 15 minutos. Cada um diz o que fez, o que fará e se está travado. Mantém o time sincronizado.
  - rotulo: 3. Sprint Review (fim)
    conteudo: O time mostra o que ficou pronto para o PO e interessados. Todos avaliam o resultado e ajustam o que vem depois.
  - rotulo: 4. Sprint Retrospective (fim)
    conteudo: O time olha para o próprio processo: o que funcionou, o que melhorar. É como o time aprende e evolui.
```

:::atencao Erro comum
Transformar a **Daily** numa reunião longa de prestação de contas para o chefe. A Daily é de **15 minutos, em pé** (por isso "stand-up"), e é do time **para o time** — serve para sincronizar e revelar obstáculos, não para alguém cobrar status. Se está virando uma hora sentado, deixou de ser Daily.

:::

### Os artefatos

Artefatos são as "listas vivas" que dão transparência ao trabalho.

:::conceito Product Backlog, Sprint Backlog e incremento
O **Product Backlog** é a lista de **tudo** que o produto precisa (visão geral, cuidada pelo PO). O **Sprint Backlog** é o **recorte** que o time escolheu fazer **nesta sprint**. E o **incremento** é o pedaço **pronto e funcionando** que sai ao final do ciclo. Em resumo: do tudo (Product), tira-se o agora (Sprint), que vira o pronto (incremento).

:::

### Por que tudo isso existe

As cerimônias e os artefatos não são burocracia — eles sustentam os **três pilares** do Scrum:

:::importante Transparência, inspeção e adaptação
**Transparência:** todos enxergam o mesmo (os backlogs são abertos). **Inspeção:** o time olha com frequência o trabalho e o processo (Review e Retrospectiva). **Adaptação:** com base no que viu, ajusta o rumo. É esse ciclo — mostrar, olhar, corrigir — que torna o Scrum capaz de lidar com a mudança.

:::

:::dica No seu futuro estágio
Quando você entrar num time, a Daily será sua primeira rotina: todo dia, 15 minutos, três respostas. Saber que ela é curta e do time pra time (não um interrogatório) já te deixa à frente de muita gente que chega achando que é "reunião de chefe".

:::

## Prática

**Atividade "Daily de mentira" (em grupos de 3-4, sem computador, ~15 min).** Cada grupo é um time Scrum desenvolvendo o app da cantina (da aula passada). Façam uma **Daily de verdade**, de pé:

1. Cada integrante responde, em até 30 segundos: **o que fiz ontem**, **o que farei hoje**, **estou travado em quê?** (inventem tarefas plausíveis do app).
2. Anotem **um obstáculo** que apareceu e decidam: o que o Scrum Master faria com ele?
3. Ao final, classifiquem cada artefato citado: era Product Backlog, Sprint Backlog ou incremento?

Um grupo encena sua Daily (em pé!) para a turma em 1 minuto. A turma cronometra — passou de 15 "minutos" simbólicos?

## Avaliação

```quiz
- pergunta: Qual cerimônia é uma reunião diária, rápida e de pé, para sincronizar o time?
  alternativas:
    - texto: Sprint Review
    - texto: Daily Stand-up
      correta: true
    - texto: Sprint Planning
    - texto: Retrospectiva
  feedback: >
    A Daily é de 15 minutos, em pé, do time para o time. Sincroniza o trabalho e
    revela obstáculos — não é reunião de status para o chefe.
- pergunta: Qual a diferença entre Product Backlog e Sprint Backlog?
  alternativas:
    - texto: São a mesma coisa com nomes diferentes
    - texto: Product Backlog é tudo que o produto precisa; Sprint Backlog é o recorte da sprint atual
      correta: true
    - texto: Product Backlog é só do Scrum Master
    - texto: Sprint Backlog é a lista de bugs apenas
  feedback: >
    Do "tudo" (Product Backlog) o time tira o "agora" (Sprint Backlog), que ao final
    vira o "pronto" (incremento).
- pergunta: A qual pilar do Scrum corresponde a Retrospectiva, em que o time revê o próprio processo?
  alternativas:
    - texto: Apenas transparência
    - texto: Inspeção e adaptação
      correta: true
    - texto: Nenhum pilar
    - texto: Somente velocidade
  feedback: >
    Na Retrospectiva o time inspeciona como trabalhou e adapta para melhorar — o
    ciclo olhar/corrigir que é o coração do Scrum.
```

## Fechamento

Hoje você descobriu que:

- O Scrum tem **quatro cerimônias**: **Planning** (planeja), **Daily** (sincroniza), **Review** (mostra o resultado), **Retrospectiva** (melhora o processo).
- Os artefatos vão do geral ao pronto: **Product Backlog** → **Sprint Backlog** → **incremento**.
- Tudo isso sustenta três pilares: **transparência, inspeção e adaptação**.
- A **Daily** é curta (15 min, de pé) e do time para o time — não é reunião de chefe.

**Próxima aula:** o Product Backlog pode virar uma lista gigante e bagunçada. Como organizar isso? Vamos aprender a agrupar funcionalidades em **épicos**.

:::roteiro
Abrir com a metáfora do time de futebol que não conversa. O diagrama da sprint dá a espinha — revele cerimônia por cerimônia. O erro da Daily longa é o mais valioso pra vida profissional: insista no "15 min, em pé, time pra time". A distinção dos três artefatos costuma confundir — a frase "do tudo, tira o agora, que vira o pronto" ajuda a fixar. A prática da Daily encenada é ouro: faça-os levantarem de verdade, o desconforto de ficar em pé ensina por que a reunião é curta. Alura ("Iniciação do projeto") opcional. 8 min pro quiz.
:::
