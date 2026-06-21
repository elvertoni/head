---
titulo: Tokens, Embeddings e Vetores
tema: Fundamentos de IA
disciplina: inteligencia-artificial
serie: Extra
prerequisitos: [O que é um LLM]
objetivos:
  - Explicar o que é um token e por que não é o mesmo que palavra
  - Entender que embeddings transformam significado em vetores
  - Reconhecer que proximidade de vetores representa proximidade de significado
trilha: fundamentos-de-ia
ordem: 10
slug: tokens-embeddings-e-vetores
modo_origem: tema
fontes: []
revisao: false
status: aprovada
versao: 1
atualizado_em: 2026-06-15
---

A máquina não lê "gato". Ela não faz a menor ideia do que é uma letra, uma palavra ou uma frase — ela só sabe lidar com **números**. Então, antes de qualquer coisa, todo texto que entra num [[llm]] precisa virar número. Esse caminho de "texto humano → número que a máquina processa → texto humano de volta" passa por duas ideias que você ouviu de relance na aula passada: **tokens** e **embeddings**. Hoje a gente abre as duas — e você vai entender por que "incrível" pode custar dois tokens e por que, pra máquina, "cão" e "cachorro" moram quase no mesmo lugar.

## Objetivos

Ao final desta aula, você será capaz de:

- Explicar o que é um **token** e por que **não** é o mesmo que palavra.
- Entender que **embeddings** transformam significado em **vetores**.
- Reconhecer que **proximidade de vetores** representa **proximidade de significado**.

## Pré-requisitos

Ter visto a **Aula 09** (o que é um LLM e a previsão de tokens).

## Desenvolvimento

### Token: o pedaço, não a palavra

:::conceito Token
É a **unidade de texto** que o modelo processa — um pedaço que pode ser uma palavra inteira, um pedaço de palavra ou até um sinal de pontuação. Um tokenizador quebra o texto em tokens antes de o [[llm]] trabalhar, e remonta no fim. Regra prática: **token não é palavra**. Palavras comuns viram um token; palavras longas ou raras viram vários ("incrivelmente" pode virar "incrivel" + "mente").

:::

:::atencao Erro comum
Achar que "1 token = 1 palavra". Quase, mas não. Espaços, pontuação e pedaços de palavras contam. Por isso, quando você ouve "este modelo aceita 1 milhão de tokens de contexto", isso **não** é 1 milhão de palavras — é mais ou menos uns 750 mil, porque muitas palavras gastam mais de um token. Essa diferença importa na prática: o custo de usar uma IA e o tamanho do texto que ela aguenta são medidos em **tokens**, não em palavras.

:::

### Embedding: significado virou número

Quebrar em tokens resolve "que pedaço é este". Falta o mais difícil: capturar o **significado**. É aí que entram os embeddings.

:::conceito Embedding (vetor de significado)
É a transformação de um token (ou texto) em uma **lista de números** — um **vetor** — que representa o seu significado. O truque genial: textos com sentido parecido recebem vetores **próximos**. Assim a máquina compara significados medindo **distância entre vetores**, em vez de comparar letras. "Cão" e "cachorro" caem pertinho; "cachorro" e "imposto" caem longe.

:::

```diagrama-progressivo
titulo: Do texto ao vetor
camadas:
  - rotulo: 1. Texto
    conteudo: "O cachorro late." É o que você escreve - puro texto humano.
  - rotulo: 2. Tokens
    conteudo: O tokenizador quebra em pedaços: "O", "cachorro", "late", ".". Cada pedaço é um token.
  - rotulo: 3. Embeddings (vetores)
    conteudo: Cada token vira uma lista de números que captura seu significado. Significados parecidos = vetores próximos.
  - rotulo: 4. A máquina compara por distância
    conteudo: Agora dá para medir "quão perto" dois significados estão calculando a distância entre seus vetores. É a base da busca por significado.
```

:::dica Isto é o motor da busca semântica
Essa ideia — significado vira vetor, proximidade vira semelhança — é o que faz a IA achar "como cancelar assinatura" num texto que diz "encerrar plano", mesmo sem palavras em comum. É também a base do [[rag]] e do [[chunking]] que você verá mais à frente na trilha. Entender embedding agora é plantar a semente desses temas avançados.

:::

## Prática

**Atividade "tokenizar e aproximar" (em duplas, sem computador, ~15 min).**

Parte A — **tokens**:
1. Peguem a frase "A inteligência artificial é incrivelmente poderosa." Tentem quebrá-la em **pedaços** que fariam sentido pra uma máquina (palavras comuns inteiras; palavras longas em 2 pedaços). Quantos "tokens" deu?
2. Comparem com a contagem de **palavras**. Bateu? Por que não?

Parte B — **embeddings (na mão)**:
3. Recebam estas palavras: *rei, rainha, gato, cachorro, maçã, banana, príncipe, leão*. **Agrupem por significado** e desenhem num "mapa" 2D — coloquem as parecidas perto e as diferentes longe.
4. Comparem os mapas das duplas: onde "rei" e "rainha" ficaram? E "maçã" e "banana"? Foi isso que o embedding faz, só que com muitos números.

Socializem: o que ficou perto de quê, e por quê?

## Avaliação

```quiz
- pergunta: Token é o mesmo que palavra?
  alternativas:
    - texto: Sim, sempre 1 token = 1 palavra
    - texto: Não — token é um pedaço de texto; uma palavra pode virar vários tokens
      correta: true
    - texto: Sim, mas só em inglês
    - texto: Não, token é sempre uma letra
  feedback: >
    Token é a unidade que o modelo processa: pode ser palavra, pedaço de palavra ou
    pontuação. Palavras longas/raras viram vários tokens.
- pergunta: O que é um embedding?
  alternativas:
    - texto: Uma foto do texto
    - texto: Uma lista de números (vetor) que representa o significado de um texto
      correta: true
    - texto: O nome do modelo de IA
    - texto: Uma regra fixa de gramática
  feedback: >
    Embedding transforma significado em vetor. Textos de sentido parecido ganham
    vetores próximos.
- pergunta: O que significa dois vetores estarem "próximos"?
  alternativas:
    - texto: Que os textos têm as mesmas letras
    - texto: Que os textos têm significado parecido
      correta: true
    - texto: Que foram escritos no mesmo dia
    - texto: Que têm o mesmo tamanho de arquivo
  feedback: >
    Proximidade de vetores = proximidade de significado. É assim que a máquina compara
    sentido, não letras — a base da busca semântica.
```

## Fechamento

Hoje você descobriu que:

- **[[tokens|Token]]** é o pedaço de texto que o modelo processa — e **não** é o mesmo que palavra.
- Contexto e custo de uma IA se medem em **tokens** (1 milhão de tokens ≠ 1 milhão de palavras).
- **[[embeddings|Embedding]]** transforma significado em **vetor**: sentido parecido → vetores próximos.
- Essa proximidade é a base da **busca por significado** (e do [[rag]] lá na frente).

**Próxima aula:** os LLMs só ficaram bons depois de uma invenção de 2017 que mudou tudo. Na Aula 11: **transformers e atenção** — o mecanismo que destravou a IA moderna.

:::roteiro
Abrir com "a máquina não lê 'gato', só números". Token primeiro: o exemplo "incrivelmente" em pedaços quebra a ideia de 1 token = 1 palavra; reforce com "1M tokens ≠ 1M palavras" (impacta custo real). Embedding com a analogia do mapa: significado vira posição, proximidade vira semelhança. A prática parte B (mapa de palavras) é embedding desplugado — rei/rainha perto é o "aha". Conecte com RAG/chunking (sementes pro módulo 4). Conteúdo conceitual estável. 8 min pro quiz.
:::
