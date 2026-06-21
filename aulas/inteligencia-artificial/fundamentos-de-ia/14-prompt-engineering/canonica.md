---
titulo: Prompt Engineering
tema: Fundamentos de IA
disciplina: inteligencia-artificial
serie: Extra
prerequisitos: [O que é um LLM]
objetivos:
  - Explicar o que é prompt engineering e por que pedir bem muda a resposta
  - Reconhecer os elementos de um bom prompt
  - Transformar um prompt vago em um prompt eficaz
trilha: fundamentos-de-ia
ordem: 14
slug: prompt-engineering
modo_origem: tema
fontes: []
revisao: false
status: aprovada
versao: 1
atualizado_em: 2026-06-15
---

Duas pessoas usam o mesmo ChatGPT no mesmo dia. Uma sai frustrada com respostas genéricas e inúteis; a outra resolve o trabalho da escola em minutos. A IA é a mesma — o que muda é **como cada uma pediu**. Lembra da Aula 09: o [[llm]] prevê texto a partir do que você dá a ele. Logo, o que você dá determina o que você recebe. Pedir bem para uma IA virou uma habilidade com nome próprio — prompt engineering — e é a primeira coisa que separa quem domina a ferramenta de quem só brinca com ela. Bem-vindo ao módulo de conversar com a IA.

## Objetivos

Ao final desta aula, você será capaz de:

- Explicar o que é **prompt engineering** e por que **pedir bem** muda a resposta.
- Reconhecer os **elementos** de um bom prompt.
- **Transformar** um prompt vago em um prompt eficaz.

## Pré-requisitos

Ter visto a **Aula 09** (o que é um LLM e a previsão de texto).

## Desenvolvimento

### Pedir bem é o jogo

:::conceito Prompt engineering
**Prompt** é a instrução que você dá ao modelo. **Prompt engineering** é a habilidade de **formular essa instrução** para conseguir a melhor resposta possível. Como o [[llm]] gera a partir do que recebe, um pedido claro e bem montado leva a uma resposta boa; um pedido vago leva a uma resposta vaga.

:::

:::atencao Erro comum
Mandar um prompt vago e esperar mágica. "Fale sobre cachorros" devolve um textão genérico que não serve pra nada. O modelo não adivinha o que você quer — ele completa o mais provável. Quanto mais **específico** o pedido (para quem é, com que objetivo, em que formato), mais útil a resposta. Vago entra, vago sai.

:::

### Os ingredientes de um bom prompt

Um prompt eficaz costuma ter alguns destes elementos:

```diagrama-progressivo
titulo: De um prompt vago a um prompt eficaz
camadas:
  - rotulo: 1. Vago
    conteudo: "Fale sobre a Revolução Francesa." Resposta genérica e longa demais, sem foco.
  - rotulo: 2. Adiciona objetivo e público
    conteudo: "Explique a Revolução Francesa para um aluno do 1º ano do ensino médio." Agora o modelo ajusta o nível.
  - rotulo: 3. Adiciona formato
    conteudo: "...em 5 tópicos curtos, com uma data em cada." A resposta vem organizada do jeito que você precisa.
  - rotulo: 4. Adiciona papel e tom
    conteudo: "Aja como um professor de história e use linguagem simples." O modelo assume o papel e o tom certos. Prompt afiado, resposta sob medida.
```

Os ingredientes mais úteis: **clareza** (diga exatamente o que quer), **contexto** (para quem, com que fim), **formato** (lista? tabela? parágrafo?), **exemplos** (mostre um modelo do que espera) e **papel** ("aja como...").

:::dica Isto economiza seu tempo — e é base do que vem a seguir
Um bom prompt te poupa de cinco tentativas frustrades. E é só o começo: na próxima aula você vai ver que, além de **como** perguntar (prompt), importa **o que** você coloca junto da pergunta (contexto). Prompt engineering é o primeiro degrau de conversar bem com a IA — e uma competência cada vez mais pedida no mercado.

:::

## Prática

**Atividade "conserta o prompt" (em duplas, sem computador, ~15 min).** Para cada prompt vago, reescrevam uma versão **eficaz** usando pelo menos 3 ingredientes (objetivo, público, formato, exemplo, papel):

1. "Me ajuda com matemática."
2. "Escreve um texto."
3. "Fala da Amazônia."
4. "Faz um resumo."

Para cada um:
- Identifiquem **por que** o original é ruim (o que falta).
- Reescrevam a versão afiada.

Cada dupla lê um "antes e depois". A turma avalia: a versão nova deixaria a IA acertar mais? (Se houver computador disponível, testem os dois e comparem as respostas.)

## Avaliação

```quiz
- pergunta: O que é prompt engineering?
  alternativas:
    - texto: Programar a IA em código
    - texto: A habilidade de formular bem a instrução dada ao modelo para obter melhores respostas
      correta: true
    - texto: Consertar bugs do ChatGPT
    - texto: Treinar o modelo do zero
  feedback: >
    É a arte de pedir bem. Como o LLM gera a partir do que recebe, formular bem o
    pedido melhora a resposta.
- pergunta: Por que "Fale sobre cachorros" costuma dar uma resposta ruim?
  alternativas:
    - texto: Porque o modelo não conhece cachorros
    - texto: Porque é vago — falta objetivo, público e formato, então o modelo devolve algo genérico
      correta: true
    - texto: Porque cachorros são proibidos
    - texto: Porque o modelo só responde perguntas de matemática
  feedback: >
    Vago entra, vago sai. Sem especificar para quem, com que fim e em que formato, o
    modelo completa o mais genérico possível.
- pergunta: Qual destes é um ingrediente de um bom prompt?
  alternativas:
    - texto: Deixar o pedido o mais curto e vago possível
    - texto: Especificar formato e público (ex.: "em 5 tópicos, para um aluno do 1º ano")
      correta: true
    - texto: Escrever tudo em maiúsculas
    - texto: Repetir a mesma palavra muitas vezes
  feedback: >
    Clareza, contexto, formato, exemplos e papel deixam o pedido específico — e a
    resposta sob medida.
```

## Fechamento

Hoje você descobriu que:

- **[[prompt-engineering|Prompt engineering]]** é a habilidade de **formular bem** o pedido ao [[llm]].
- Pedido **vago** gera resposta **vaga** — o modelo não adivinha o que você quer.
- Bons prompts têm **clareza, contexto, formato, exemplos e papel**.
- Pedir bem economiza tempo e é o primeiro degrau de conversar com a IA.

**Próxima aula:** prompt é **como** perguntar. Mas e **o que** você coloca junto da pergunta? Na Aula 15: **context engineering** — por que "contexto é o novo código".

:::roteiro
Abrir com as duas pessoas e a mesma IA: o que muda é o pedido. O erro do prompt vago é o coração; o exemplo "fale sobre cachorros" gruda. O diagrama mostra a evolução vago→afiado camada a camada — bom pra construir ao vivo no quadro. Se houver internet/computador, a prática fica muito mais forte testando antes/depois no ChatGPT real; sem isso, funciona desplugada avaliando a qualidade. Aponte pro context engineering (aula 15). Conteúdo conceitual estável. 8 min pro quiz.
:::
