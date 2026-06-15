---
titulo: Agentes e Subagentes
tema: Fundamentos de IA
disciplina: inteligencia-artificial
serie: Extra
prerequisitos: [O que é um LLM]
objetivos:
  - Diferenciar um agente de IA de um chatbot comum
  - Explicar o loop de decisão observar-pensar-agir
  - Reconhecer o papel de subagentes em um time orquestrado
trilha: fundamentos-de-ia
ordem: 18
modo_origem: tema
fontes: []
revisao: false
status: aprovada
versao: 1
atualizado_em: 2026-06-15
---

Até agora, na nossa trilha, a IA **respondeu**: você pergunta, ela devolve texto. Útil, mas passivo — como um funcionário que só fala e nunca faz. Agora imagine uma IA que recebe um objetivo ("organize minha pasta de fotos por evento") e **vai lá e faz**: olha o que tem, decide o que fazer, executa, confere o resultado e repete até terminar. Isso não é mais um chatbot. É um **agente**. A diferença entre responder e agir é a fronteira mais quente da IA hoje — e abre o módulo em que a IA sai da conversa e entra na ação.

## Objetivos

Ao final desta aula, você será capaz de:

- Diferenciar um **agente** de IA de um **chatbot** comum.
- Explicar o **loop de decisão**: observar → pensar → agir.
- Reconhecer o papel de **subagentes** em um time orquestrado.

## Pré-requisitos

Ter visto a **Aula 09** (o que é um LLM).

## Desenvolvimento

### Do responder ao agir

:::conceito Agente de IA
É um sistema que usa um [[llm]] não só para responder, mas para **perseguir um objetivo agindo** — ele decide quais passos dar, executa ações e ajusta o rumo até concluir a tarefa. O chatbot devolve um texto e para; o agente entra num **ciclo** de ação até terminar o trabalho.

:::

O coração de um agente é um ciclo que se repete:

```diagrama-progressivo
titulo: O loop de decisão de um agente
camadas:
  - rotulo: 1. Observar
    conteudo: O agente olha o estado atual - o objetivo, o que já fez, o resultado da última ação.
  - rotulo: 2. Pensar
    conteudo: Com base no que observou, decide qual é a próxima ação que mais aproxima do objetivo.
  - rotulo: 3. Agir
    conteudo: Executa a ação - buscar algo, mover um arquivo, escrever um trecho. (Como ele age é a próxima aula: tool use.)
  - rotulo: 4. Repetir ou parar
    conteudo: Olha o resultado. Cumpriu o objetivo? Para. Ainda não? Volta ao passo 1. O ciclo se repete até terminar.
```

:::atencao Erro comum
Confundir agente com chatbot. Um chatbot **responde e para**; um agente **age em ciclo** rumo a um objetivo. E tem um perigo real do agente: se ninguém define uma **condição de parada**, ele pode entrar em **loop infinito** — repetindo ações sem nunca concluir, gastando tempo e dinheiro. Autonomia sem freio é problema, não vantagem.

:::

### Um time de agentes

Para tarefas grandes, um agente sozinho não dá conta — entram os subagentes.

:::conceito Subagentes (orquestrador e filhos)
É dividir o trabalho entre vários agentes. Um **orquestrador** (agente "chefe") quebra a tarefa e distribui pedaços para **subagentes** especializados — um pesquisa, outro escreve, outro revisa — e depois junta os resultados. É como um chefe de cozinha coordenando cozinheiros: cada um cuida de um prato, o chefe monta o cardápio.

:::

:::dica A fronteira do mercado (e o cuidado que vem junto)
Agentes são a aposta mais quente da IA atual: em vez de você fazer tudo na mão com a IA ajudando, o agente executa tarefas inteiras. Mas quanto **mais autonomia**, **menos controle** — e maior o risco de ele errar sem ninguém perceber. Por isso, profissionais sérios sempre colocam **freios** (limites e pontos de aprovação humana). Quem entende isso cedo constrói IA útil **e** segura.

:::

## Prática

**Atividade "seja o agente" (em grupos de 4, sem computador, ~15 min).**

Objetivo do agente: **"organizar uma festa surpresa para um colega"**.

1. **Loop na mão:** o grupo executa o ciclo em voz alta, uma rodada de cada vez — *Observar* (o que já temos?), *Pensar* (qual o próximo passo?), *Agir* (decidir e "fazer"), e repetir. Anotem cada rodada.
2. **Condição de parada:** definam **antes** quando o agente deve parar (objetivo cumprido). O que aconteceria sem essa condição?
3. **Subagentes:** redistribuam como um time — quem é o orquestrador? Quais subagentes (convites, comida, local)? O que cada um entrega ao chefe?
4. **Freio:** que decisão **exigiria** aprovação de um humano antes de agir? (ex.: gastar dinheiro)

Cada grupo apresenta seu loop e seu ponto de "freio humano".

## Avaliação

```quiz
- pergunta: O que diferencia um agente de IA de um chatbot?
  alternativas:
    - texto: O agente é mais bonito
    - texto: O chatbot responde e para; o agente age em ciclo até cumprir um objetivo
      correta: true
    - texto: O agente não usa LLM
    - texto: Não há diferença
  feedback: >
    Chatbot devolve texto e para. Agente entra num loop de observar-pensar-agir até
    concluir a tarefa — ele age, não só responde.
- pergunta: Quais são os passos do loop de decisão de um agente?
  alternativas:
    - texto: Dormir, acordar, comer
    - texto: Observar, pensar, agir e repetir até concluir
      correta: true
    - texto: Perguntar e calar
    - texto: Treinar e inferir
  feedback: >
    O ciclo é observar o estado, pensar a próxima ação, agir e checar o resultado —
    repetindo até cumprir o objetivo (ou bater a condição de parada).
- pergunta: Qual é um risco real de dar autonomia a um agente sem freios?
  alternativas:
    - texto: Ele fica mais barato
    - texto: Loop infinito — repetir ações sem concluir, gastando tempo e dinheiro
      correta: true
    - texto: Ele para de funcionar de propósito
    - texto: Não há risco nenhum
  feedback: >
    Sem condição de parada e limites, o agente pode rodar em loop sem fim. Mais
    autonomia exige mais freios (limites e aprovação humana).
```

## Fechamento

Hoje você descobriu que:

- Um **[[agente|agente de IA]]** não só responde — ele **age em ciclo** para cumprir um objetivo.
- O loop é **observar → pensar → agir → repetir** até concluir.
- **Subagentes** dividem tarefas grandes: um orquestrador coordena agentes especializados.
- Mais autonomia = menos controle: agentes precisam de **freios** (limites e aprovação humana).

**Próxima aula:** no loop, o agente "age". Mas como uma IA, que só gera texto, consegue **fazer coisas** no mundo? Na Aula 19: **tool use e function calling** — dando mãos à IA.

:::roteiro
Abrir com o contraste responder vs agir (funcionário que só fala vs que faz). O loop observar-pensar-agir é o conceito central; construa no quadro como ciclo. O erro chatbot-vs-agente + o risco do loop infinito são essenciais (preparam guardrails da aula 21). A prática da festa surpresa é o loop desplugado; o "freio humano" planta os guardrails. Subagentes = analogia do chefe de cozinha. Aponte pro tool use (aula 19): como o agente realmente age. Conteúdo conceitual estável. 8 min pro quiz.
:::
