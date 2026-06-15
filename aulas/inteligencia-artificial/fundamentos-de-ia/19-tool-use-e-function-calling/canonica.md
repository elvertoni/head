---
titulo: Tool Use e Function Calling
tema: Fundamentos de IA
disciplina: inteligencia-artificial
serie: Extra
prerequisitos: [Agentes e Subagentes]
objetivos:
  - Explicar como um LLM age no mundo usando ferramentas
  - Entender que o modelo pede a chamada, e o sistema executa
  - Reconhecer exemplos de ferramentas e o papel do formato estruturado
trilha: fundamentos-de-ia
ordem: 19
modo_origem: tema
fontes: []
revisao: false
status: aprovada
versao: 1
atualizado_em: 2026-06-15
---

Aqui mora um paradoxo que confunde muita gente. Um [[llm]] só sabe fazer **uma** coisa: gerar texto (Aula 09). Ele não tem mãos, não acessa a internet, não roda código, não manda e-mail. E, no entanto, os agentes da aula passada **fazem** tudo isso. Como? A resposta é elegante: o modelo não executa nada — ele **pede**. Ele gera um texto especial dizendo "execute a calculadora com 7×8", e um sistema do lado de fora executa e devolve o resultado. Esse mecanismo de dar "mãos" à IA tem nome: tool use, ou function calling. É o que conecta a IA ao mundo real.

## Objetivos

Ao final desta aula, você será capaz de:

- Explicar como um LLM **age no mundo** usando ferramentas.
- Entender que o modelo **pede** a chamada, e o **sistema executa**.
- Reconhecer exemplos de ferramentas e o papel do **formato estruturado**.

## Pré-requisitos

Ter visto a **Aula 18** (agentes e o loop de ação) e a **Aula 09** (o LLM só gera texto).

## Desenvolvimento

### A IA não tem mãos — ela pede

:::conceito Tool use (function calling)
É a capacidade do [[llm]] de **chamar ferramentas** (funções) para fazer coisas que ele sozinho não consegue: calcular, buscar na web, ler um arquivo, enviar uma mensagem. O segredo: o modelo **não executa** a ferramenta — ele gera, num **formato estruturado**, o pedido "use a ferramenta X com estes dados". Um sistema externo executa de verdade e devolve o resultado para o modelo continuar.

:::

:::atencao Erro comum
"O modelo roda o código / acessa a internet sozinho." Não. O LLM só produz texto — inclusive o texto que **pede** uma ação. Quem realmente executa (roda o código, faz a busca, manda o e-mail) é o **sistema ao redor** (o harness, da Aula 21). É como um chef que grita o pedido "duas batatas fritas!" — ele não vai à fritadeira; quem frita é a cozinha. O modelo pede; o sistema faz.

:::

### Por que o formato estruturado importa

Para o sistema entender o pedido, ele não pode vir em texto solto — precisa ser **estruturado** (organizado em campos claros: qual ferramenta, quais dados).

```diagrama-progressivo
titulo: Uma chamada de ferramenta, do pedido ao resultado
camadas:
  - rotulo: 1. O usuário pede algo
    conteudo: "Quanto é 1234 x 5678?" O LLM é péssimo em conta exata - mas sabe que existe uma ferramenta calculadora.
  - rotulo: 2. O modelo PEDE a ferramenta
    conteudo: Em vez de chutar, ele gera um pedido estruturado - usar a ferramenta "calculadora" com os dados 1234 e 5678.
  - rotulo: 3. O sistema EXECUTA
    conteudo: O harness recebe o pedido, roda a calculadora de verdade e obtém 7.006.652.
  - rotulo: 4. O resultado volta ao modelo
    conteudo: O modelo recebe o número correto e o usa para escrever a resposta final ao usuário. Sem chute, com ferramenta.
```

Exemplos de ferramentas comuns: **buscar na web**, **rodar código**, **ler/escrever arquivos**, **enviar mensagens**, **consultar um banco de dados**. Cada ferramenta tem uma descrição que ensina o modelo **quando** e **como** usá-la.

:::dica Ferramentas tapam os buracos do LLM
Repare como tool use resolve fraquezas que vimos antes: o modelo erra contas? Dá a ele uma calculadora. Não sabe o que é recente (o [[cutoff]])? Dá a ele uma busca na web. Não conhece seu material? Conecta a um [[rag]]. Tool use é como a IA **compensa** suas limitações pedindo ajuda às ferramentas certas — exatamente o que um bom profissional faz.

:::

## Prática

**Atividade "dê ferramentas ao colega-IA" (em duplas, sem computador, ~15 min).**

Um aluno é o **"LLM"** (só pode falar, não pode calcular nem consultar nada de cabeça). O outro é o **"sistema"** que executa ferramentas. Disponíveis (cartões): **calculadora**, **busca**, **relógio**.

1. O "usuário" (podem revezar) faz pedidos: "quanto é 47×89?", "que horas são?", "qual a capital da Austrália?".
2. O **"LLM"** não responde direto: ele **pede** a ferramenta no formato `usar [ferramenta] com [dados]`.
3. O **"sistema"** executa (faz a conta, olha o relógio, "busca") e devolve o resultado.
4. O **"LLM"** então monta a resposta final com o resultado recebido.
5. **Pegadinha:** peçam algo **sem ferramenta disponível** (ex.: "qual meu nome?"). O que o LLM deve fazer? (pedir a info ou dizer que não tem como saber — não inventar.)

Discussão: o que o "LLM" conseguiu fazer com ferramentas que não conseguiria sozinho?

## Avaliação

```quiz
- pergunta: Quando um LLM "usa uma ferramenta", o que realmente acontece?
  alternativas:
    - texto: O modelo executa a ferramenta sozinho
    - texto: O modelo PEDE a chamada num formato estruturado, e um sistema externo executa
      correta: true
    - texto: A ferramenta substitui o modelo
    - texto: O usuário executa tudo na mão
  feedback: >
    O LLM só gera texto — inclusive o pedido da ação. Quem executa (roda, busca, envia)
    é o sistema ao redor. O modelo pede; o sistema faz.
- pergunta: Por que o pedido de ferramenta precisa ser "estruturado"?
  alternativas:
    - texto: Para ficar mais bonito
    - texto: Para o sistema entender qual ferramenta usar e com quais dados
      correta: true
    - texto: Porque texto solto é proibido
    - texto: Para gastar mais tokens
  feedback: >
    Estruturado = campos claros (qual ferramenta, quais dados). Assim o sistema sabe
    exatamente o que executar, sem ambiguidade.
- pergunta: Como o tool use ajuda com o problema do cutoff?
  alternativas:
    - texto: Retreina o modelo
    - texto: Dá ao modelo uma ferramenta de busca para obter informação atual
      correta: true
    - texto: Apaga o conhecimento antigo
    - texto: Não ajuda em nada
  feedback: >
    O modelo não sabe o que é recente, mas pode pedir a ferramenta "busca na web" e
    usar o resultado — compensando o cutoff com uma ferramenta.
```

## Fechamento

Hoje você descobriu que:

- **[[tool-use|Tool use (function calling)]]** dá "mãos" ao [[llm]]: ele chama ferramentas para fazer o que não consegue sozinho.
- O modelo **pede** a ação num **formato estruturado**; o **sistema executa** e devolve o resultado.
- Ferramentas comuns: buscar, calcular, ler/escrever arquivos, enviar mensagens.
- Ferramentas **compensam** as limitações do modelo (conta, cutoff, material próprio).

**Próxima aula:** cada ferramenta nova precisa ser conectada à IA. Fazer isso uma a uma vira um caos. Existe um padrão pra resolver — o "USB da IA". Na Aula 20: **MCP**.

:::roteiro
Abrir com o paradoxo: o LLM só gera texto, mas o agente faz coisas — como? A resposta "ele pede, o sistema faz" é o coração; a analogia do chef que grita o pedido (não vai à fritadeira) gruda. O erro "o modelo executa sozinho" é o alvo. O diagrama da calculadora mostra o fluxo pedido→execução→resultado. A `:::dica` amarra com cutoff/RAG (ferramentas tapam buracos). A prática do colega-IA com cartões é function calling desplugado — a pegadinha sem ferramenta prepara não-alucinar. Aponte pro MCP (aula 20). Conteúdo conceitual estável. 8 min pro quiz.
:::
