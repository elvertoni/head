---
titulo: MCP — Model Context Protocol
tema: Fundamentos de IA
disciplina: inteligencia-artificial
serie: Extra
prerequisitos: [Tool Use e Function Calling]
objetivos:
  - Explicar que problema o MCP resolve
  - Entender o MCP como um protocolo padrão, comparável ao USB e ao HTTP
  - Reconhecer a relação cliente-servidor e o que um servidor MCP oferece
trilha: fundamentos-de-ia
ordem: 20
modo_origem: material
fontes:
  - lake/inteligencia-artificial/ia-coders/o-que-e-model-context-protocol-mcp.md
revisao: true
status: aprovada
versao: 1
atualizado_em: 2026-06-15
---

Na aula passada você viu que a IA age chamando ferramentas. Beleza — mas e se você quiser conectar a IA ao Gmail, ao Google Drive, ao sistema da escola, a dez serviços diferentes? Antes, alguém tinha que programar **na mão** a ligação de cada IA com cada serviço — uma para o Gmail, outra para o Drive, outra para cada coisa. Vira uma teia impossível de manter. Pensa em como era antes do USB: cada aparelho tinha um plugue diferente, uma gaveta cheia de cabos. O MCP é o USB da IA — um padrão único que faz qualquer IA conectar a qualquer ferramenta. Aula vinda direto da prática de quem constrói IA.

## Objetivos

Ao final desta aula, você será capaz de:

- Explicar **que problema** o MCP resolve.
- Entender o MCP como um **protocolo padrão**, comparável ao USB e ao HTTP.
- Reconhecer a relação **cliente-servidor** e o que um servidor MCP oferece.

## Pré-requisitos

Ter visto a **Aula 19** (tool use e function calling).

## Desenvolvimento

### O problema: integração na mão não escala

Imagine ligar **4 IAs** a **4 serviços** programando cada ligação separadamente: dá 16 conexões para construir e manter. Some mais um serviço, mais um app, e a teia explode. Cada uma feita de um jeito diferente. Insustentável.

:::conceito MCP (Model Context Protocol)
É um **protocolo aberto** (criado pela Anthropic em 2024) que **padroniza** como aplicações de IA se conectam a ferramentas, dados e serviços externos. Em vez de cada integração ser feita na mão, todos seguem o mesmo padrão — então qualquer IA que "fala MCP" conecta a qualquer ferramenta que "fala MCP", sem trabalho extra.

:::

### O USB (e o HTTP) da IA

A melhor forma de entender o MCP é por comparação:

```diagrama-progressivo
titulo: Por que um padrão muda tudo
camadas:
  - rotulo: 1. Antes do padrão (o caos)
    conteudo: Como antes do USB - cada aparelho com seu plugue. Cada IA conectava a cada serviço de um jeito diferente, tudo na mão. N x N conexões.
  - rotulo: 2. Surge o protocolo
    conteudo: Assim como o USB padronizou plugues e o HTTP padronizou a web, o MCP padroniza a conexão IA-ferramenta. Um formato que todos entendem.
  - rotulo: 3. Cliente e servidor
    conteudo: A IA tem um "cliente MCP"; cada serviço (Gmail, Drive) oferece um "servidor MCP". O cliente fala com qualquer servidor pelo mesmo protocolo.
  - rotulo: 4. O ecossistema floresce
    conteudo: Quem faz o Gmail cria UM servidor MCP, e qualquer IA do mundo pode usá-lo. Conecta-se uma vez, serve para todos. O padrão destrava a escala.
```

O que um **servidor MCP** oferece à IA? Principalmente **ferramentas** (ações que a IA pode chamar — ver Aula 19, function calling) e **dados/recursos** (informações que ela pode ler). É a ponte padronizada entre o modelo e o mundo.

:::atencao Erro comum
Achar que "MCP é uma IA" ou um modelo inteligente. Não é. MCP é um **protocolo** — um conjunto de regras de comunicação, igual ao HTTP que seu navegador usa para abrir sites. Ele não pensa nem decide nada; só **padroniza a conversa** entre a IA e as ferramentas. Confundir protocolo com inteligência é como achar que a tomada é que faz o aparelho funcionar.

:::

:::dica Padrões são onde o mercado se organiza
A história da tecnologia é feita de padrões que destravaram tudo: o HTTP fez a web existir, o USB acabou com a gaveta de cabos. O MCP está fazendo isso para a IA agora, e é uma habilidade muito procurada — saber conectar IA a ferramentas via MCP coloca você na fronteira. E a lição vale além da IA: quem entende **por que** padrões importam entende como a tecnologia evolui.

:::

## Prática

**Atividade "antes e depois do padrão" (em duplas, sem computador, ~15 min).**

1. **O caos:** desenhem **3 IAs** de um lado e **3 serviços** (Gmail, Drive, calendário) do outro. Liguem **cada IA a cada serviço** com uma linha. Quantas linhas deram? (resposta: 9 — e cada uma feita na mão.)
2. **O padrão:** agora desenhem um "MCP" no meio. Cada IA liga **uma vez** ao padrão; cada serviço liga **uma vez** ao padrão. Quantas linhas agora? Comparem.
3. **Analogias:** completem — "MCP está para a IA assim como ___ está para os aparelhos" e "___ está para a web".
4. **Pegadinha:** o MCP "pensa" ou "responde perguntas"? Justifiquem por que não.

Cada dupla mostra os dois desenhos (caos vs padrão). A turma sente, no olho, por que o padrão vence.

## Avaliação

```quiz
- pergunta: Que problema o MCP resolve?
  alternativas:
    - texto: Deixa o modelo mais inteligente
    - texto: A integração na mão de cada IA com cada serviço, que não escala
      correta: true
    - texto: A falta de energia dos computadores
    - texto: O preço dos modelos
  feedback: >
    Sem padrão, cada ligação IA-serviço é feita na mão (N x N), virando uma teia
    impossível. O MCP padroniza isso — conecta uma vez, serve para todos.
- pergunta: O MCP é melhor descrito como…
  alternativas:
    - texto: Um modelo de IA muito inteligente
    - texto: Um protocolo (padrão de comunicação), como o USB ou o HTTP
      correta: true
    - texto: Um tipo de computador
    - texto: Um site de buscas
  feedback: >
    MCP é um protocolo — regras de comunicação padronizadas. Não pensa nem responde;
    só padroniza a conversa entre IA e ferramentas, como o HTTP faz na web.
- pergunta: O que um servidor MCP oferece à IA?
  alternativas:
    - texto: Apenas imagens
    - texto: Ferramentas (ações) e dados/recursos que a IA pode usar
      correta: true
    - texto: Um novo modelo de linguagem
    - texto: Mais memória RAM
  feedback: >
    O servidor MCP expõe ferramentas (ações chamáveis, como na Aula 19) e dados que a
    IA pode ler — a ponte padronizada entre o modelo e o mundo.
```

## Fechamento

Hoje você descobriu que:

- O **[[mcp|MCP]]** resolve o caos de conectar cada IA a cada serviço **na mão** — que não escala.
- É um **protocolo aberto** (padrão de comunicação), o **"USB da IA"**, comparável ao HTTP da web.
- Funciona por **cliente** (na IA) e **servidor** (no serviço): conecta-se uma vez, serve para todos.
- Um servidor MCP oferece **ferramentas** ([[tool-use]]) e **dados** à IA — e **não** é uma IA que pensa.

**Próxima aula:** ferramentas, MCP, loop de decisão, memória, freios... tudo isso ao redor do modelo tem um nome coletivo. Fechamos o módulo com **harness engineering** — a infraestrutura que faz a IA agir de verdade.

:::roteiro
Vem da transcrição ia-coders (modo Material), simplificada do contexto de coding-agents para 14-18. Abrir com a "gaveta de cabos antes do USB" — a analogia carrega a aula toda. O problema (N x N na mão) precede a solução (protocolo). O erro "MCP é uma IA" é crucial: é protocolo, não inteligência (como HTTP). A prática do desenho caos-vs-padrão é poderosa: contar as linhas faz o argumento sozinho. Revisão aplicada: cortei as 3 primitivas detalhadas, JSON-RPC, transportes STDio/HTTP por estarem acima da faixa — mantive tools+dados. Aponte pro harness (21). 8 min pro quiz.
:::
