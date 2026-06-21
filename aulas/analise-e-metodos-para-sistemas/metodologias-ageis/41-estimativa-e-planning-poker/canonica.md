---
titulo: Estimativa e Planning Poker
tema: Metodologias Ágeis
disciplina: analise-e-metodos-para-sistemas
serie: 1ª
prerequisitos: [Histórias de Usuário]
objetivos:
  - Explicar o que é estimar esforço e por que se estima de forma relativa
  - Aplicar o Planning Poker para chegar a um consenso de estimativa
  - Revisar a trilha relacionando estimativa, priorização e planejamento
trilha: metodologias-ageis
ordem: 41
slug: estimativa-e-planning-poker
modo_origem: seed
fontes:
  - lake/analise-e-metodos-para-sistemas/AULA 41_ANÁLISE E MÉTODO PARA SISTEMAS.pptx
revisao: true
status: aprovada
versao: 1
atualizado_em: 2026-06-15
---

Quanto tempo leva pra arrumar o seu quarto? Se você responder sozinho, na pressa, provavelmente erra feio — "uns 10 minutos" vira duas horas. Agora, se três pessoas que já arrumaram aquele quarto palpitarem juntas, a estimativa fica bem melhor. Times de software vivem esse problema: precisam adivinhar quanto esforço cada história vai dar, e errar custa caro. Para acertar mais, o Scrum usa um jogo de cartas — sim, cartas — chamado Planning Poker. Nesta última aula da trilha, você aprende a estimar em grupo e amarra tudo que viu até aqui.

## Objetivos

Ao final desta aula, você será capaz de:

- Explicar o que é **estimar esforço** e por que se estima de forma **relativa**.
- Aplicar o **Planning Poker** para chegar a um **consenso** de estimativa.
- Revisar a trilha, relacionando estimativa, priorização e planejamento.

## Pré-requisitos

Ter visto a **Aula 40** (histórias de usuário) e a ideia de capacidade do time (Aula 38).

## Desenvolvimento

### Estimar é prever esforço, não cravar horas

:::conceito Estimativa de esforço
É a previsão de **quanto trabalho** uma história de usuário vai dar. No ágil, costuma ser **relativa**: em vez de "isto leva 3 horas", compara-se — "isto é mais ou menos o dobro daquilo". Comparar é mais fácil e mais confiável do que adivinhar horas exatas, que quase nunca batem.

:::

A estimativa serve para dois usos que você já conhece: ajuda a **priorizar** (uma história de muito valor e pouco esforço fura a fila) e ajuda a planejar **quanto cabe** numa sprint (a capacidade da Aula 38).

### O Planning Poker

:::conceito Planning Poker
É uma técnica para estimar **em consenso**. Cada pessoa do time recebe cartas com números, geralmente da **sequência de Fibonacci** (1, 2, 3, 5, 8, 13, 21...). Para cada história, todos escolhem em segredo a carta que representa o esforço que imaginam e **revelam ao mesmo tempo**. Se as cartas batem, fechou. Se variam muito, discute-se o porquê e joga-se de novo, até chegar a um consenso.

:::

```diagrama-progressivo
titulo: Uma rodada de Planning Poker
camadas:
  - rotulo: 1. Apresenta a história
    conteudo: O time lê e tira dúvidas sobre a história de usuário a ser estimada.
  - rotulo: 2. Cada um escolhe em segredo
    conteudo: Sem mostrar aos outros, cada pessoa separa a carta (1, 2, 3, 5, 8...) que representa o esforço que acha necessário.
  - rotulo: 3. Revelam ao mesmo tempo
    conteudo: Todas as cartas viram juntas. A revelação simultânea evita que alguém seja influenciado pela opinião do colega mais experiente.
  - rotulo: 4. Discutem e repetem
    conteudo: Se houver grande diferença (ex.: um 2 e um 13), os dois explicam seu raciocínio. Joga-se de novo até o time convergir.
```

:::atencao Erro comum
Deixar a **primeira pessoa a falar** ancorar todo mundo. Se o membro mais experiente diz "isso é 8" antes da votação, os outros tendem a concordar por insegurança — e a estimativa fica enviesada. É justamente por isso que no Planning Poker as cartas são escolhidas **em segredo** e reveladas **ao mesmo tempo**: para que cada opinião nasça independente. A revelação simultânea não é firula, é o coração do método.

:::

:::dica Por que Fibonacci e não 1,2,3,4,5
Os números crescem com saltos (1, 2, 3, 5, 8, 13...) de propósito: quanto maior a história, mais incerta é a estimativa, então não faz sentido discutir se é "7 ou 8". Os saltos forçam o time a assumir a incerteza — uma lição honesta que vale para qualquer previsão na vida profissional.

:::

## Prática

**Atividade "Planning Poker de verdade" (em grupos de 3-4, sem computador, ~15 min).** Vamos jogar — com histórias do cotidiano para focar no **método**, não no conteúdo técnico.

1. Cada grupo cria **5 histórias** simples de tarefas do dia: ex. *"chupar uma bala", "ir embora para casa", "organizar a mochila", "fazer a lição de matemática", "lavar a louça"*.
2. Cada integrante recebe cartas (escrevam números de Fibonacci em pedaços de papel: 1, 2, 3, 5, 8, 13).
3. Para cada história, todos escolhem a carta de esforço **em segredo** e **revelam juntos**. Onde houver grande diferença, discutam e rejoguem.
4. Com os esforços definidos, **priorizem** quais histórias fariam **hoje** e quais ficariam para **amanhã** — e expliquem com base em quê (esforço? importância?).

Cada grupo conta um caso em que as cartas vieram bem diferentes e o que descobriram ao discutir.

## Avaliação

```quiz
- pergunta: No ágil, como costuma ser feita a estimativa de esforço?
  alternativas:
    - texto: Em horas exatas, sempre precisas
    - texto: De forma relativa, comparando histórias entre si
      correta: true
    - texto: Pelo Scrum Master, sozinho
    - texto: Não se faz estimativa no ágil
  feedback: >
    Estima-se comparando ("isto é o dobro daquilo"), o que é mais confiável que cravar
    horas exatas que quase nunca batem.
- pergunta: Por que no Planning Poker as cartas são reveladas ao mesmo tempo?
  alternativas:
    - texto: Para deixar o jogo mais divertido apenas
    - texto: Para que cada opinião seja independente, sem ser ancorada pela do colega
      correta: true
    - texto: Para o Scrum Master decidir sozinho
    - texto: Para acelerar a reunião sem discutir
  feedback: >
    A revelação simultânea evita o viés de ancoragem — ninguém é influenciado pela
    opinião do mais experiente antes de formar a sua.
- pergunta: Para que serve a estimativa de esforço, além de prever o trabalho?
  alternativas:
    - texto: Para nada além de cumprir burocracia
    - texto: Para ajudar a priorizar e a saber quanto cabe numa sprint
      correta: true
    - texto: Para substituir as histórias de usuário
    - texto: Para escolher o Product Owner
  feedback: >
    A estimativa alimenta a priorização (valor x esforço) e o planejamento da sprint
    (capacidade) — amarrando tudo que vimos na trilha.
```

## Fechamento

Hoje você descobriu que:

- **Estimar esforço** é prever quanto trabalho uma história dá — e no ágil isso é **relativo**, por comparação.
- O **Planning Poker** estima em **consenso**, com cartas de **Fibonacci** reveladas **ao mesmo tempo**.
- A revelação simultânea evita o **viés de ancoragem** — a grande sacada do método.
- A estimativa amarra a trilha: alimenta a **priorização** e o **planejamento** das sprints.

**Fim da trilha:** você percorreu a agilidade inteira — do **Manifesto Ágil** ao time Scrum, das **cerimônias** aos **épicos**, da **priorização** às **releases**, das **histórias de usuário** à **estimativa**. Você já tem o vocabulário e a prática que um time de software espera de quem está chegando. Próximo passo, na vida real: viver um projeto de ponta a ponta.

:::roteiro
Última aula da trilha — vale abrir reconhecendo o percurso. A analogia "quanto leva pra arrumar o quarto" prepara a estimativa em grupo. O Planning Poker é o ápice: NÃO pule a prática, ela é o melhor momento da trilha. Prepare cartas de papel antes, ou peça que escrevam. O erro de ancoragem é o conceito-chave — encene: diga "eu acho que é 8" em voz alta antes de uma rodada e mostre como todos tendem a copiar; depois faça em segredo e compare. As histórias bobas (chupar bala) são de propósito: focam no método sem travar no conteúdo técnico. Reserve 2-3 min finais para amarrar a trilha inteira (cite cada aula). Alura ("Planning Poker") opcional.
:::
