---
titulo: O que é um LLM
tema: Fundamentos de IA
disciplina: inteligencia-artificial
serie: Extra
prerequisitos: [Redes Neurais e Deep Learning, IA, ML, Deep Learning e IA Generativa]
objetivos:
  - Explicar o que é um LLM e a ideia de prever o próximo token
  - Reconhecer que o LLM gera por probabilidade, não por compreensão ou busca
  - Situar os LLMs atuais como rede neural profunda treinada em texto massivo
trilha: fundamentos-de-ia
ordem: 9
slug: o-que-e-um-llm
modo_origem: tema
fontes: []
revisao: false
status: aprovada
versao: 1
atualizado_em: 2026-06-15
---

Você manda uma pergunta pro ChatGPT e ele responde um texto bem escrito, na hora, sobre quase qualquer assunto. Parece que tem alguém inteligente do outro lado, lendo e pensando. Não tem. Por baixo dessa conversa existe uma máquina fazendo **uma única coisa**, repetida milhares de vezes: adivinhar qual é a próxima palavrinha mais provável. É um autocompletar do seu teclado — só que treinado com boa parte de tudo que a humanidade já escreveu, e turbinado pelas [[rede-neural|redes neurais profundas]] da aula passada. Essa máquina tem nome: LLM. Hoje começa o módulo mais esperado da trilha.

## Objetivos

Ao final desta aula, você será capaz de:

- Explicar o que é um **LLM** e a ideia de **prever o próximo token**.
- Reconhecer que o LLM **gera por probabilidade**, não por compreensão ou busca.
- Situar os LLMs atuais como uma **rede neural profunda** treinada em texto massivo.

## Pré-requisitos

Ter visto a **Aula 08** (redes neurais e deep learning) e a **Aula 03** (IA generativa).

## Desenvolvimento

### Um autocompletar gigante

:::conceito LLM (Large Language Model)
É um **modelo de linguagem de grande escala**: uma [[rede-neural|rede neural profunda]] treinada com uma quantidade enorme de texto (livros, sites, documentação) para **prever o próximo pedaço de texto** mais provável. "Grande" não é exagero — esses modelos têm bilhões de "pesos" ajustados no treino. Ele é o motor por trás da [[ia-generativa]] de texto, como o ChatGPT.

:::

A mecânica é surpreendentemente simples de descrever:

```diagrama-progressivo
titulo: Como um LLM responde
camadas:
  - rotulo: 1. Sua pergunta vira tokens
    conteudo: O texto que você escreve é quebrado em pedacinhos chamados tokens (assunto da próxima aula). É só assim que a máquina lê.
  - rotulo: 2. O modelo prevê o próximo token
    conteudo: Com base em tudo que aprendeu, ele calcula qual token tem mais probabilidade de vir em seguida - e escolhe um.
  - rotulo: 3. Repete, token a token
    conteudo: Esse novo token entra no contexto, e o modelo prevê o seguinte. E o seguinte. Palavra a palavra, a resposta vai sendo construída.
  - rotulo: 4. Vira texto de volta
    conteudo: A sequência de tokens previstos é remontada no texto que você lê. Toda a "conversa" é essa previsão encadeada, repetida muito rápido.
```

### O que ele NÃO faz

:::atencao Erro comum
"O LLM entende o que diz e busca a resposta certa na internet." Errado nas duas pontas. Ele **não entende** no sentido humano — calcula probabilidades de texto. E, por padrão, **não busca na internet**: responde só com os padrões que aprendeu no treino. Por isso ele pode escrever algo **errado com total confiança** — ele não está consultando um banco de fatos, está completando o texto mais provável. Guardar isso é a diferença entre usar IA com juízo ou cair em armadilha (voltaremos nisso na aula de alucinações).

:::

:::curiosidade Versões que envelhecem rápido
Em 2026, os LLMs mais fortes vêm de famílias como **GPT** (OpenAI), **Claude** (Anthropic), **Gemini** (Google) e **Llama** (Meta), muitos já capazes de ler um milhão de tokens de uma vez. Mas repare: os números de versão sobem de mês em mês. Qualquer modelo específico que eu citar aqui vai estar "velho" rápido — o que **não** muda é a ideia de fundo: prever o próximo token. Foque no conceito, não na versão da moda.

:::

:::dica Saber a mecânica muda como você usa
Quem entende que o LLM **prevê texto provável** usa a ferramenta melhor: confere fatos importantes, desconfia de números e datas, e não trata a resposta como verdade absoluta. Quem acha que é um oráculo onisciente leva rasteira. Essa única noção — "é previsão, não consulta" — já te coloca à frente da maioria dos usuários.

:::

## Prática

**Atividade "seja o LLM" (em duplas, sem computador, ~15 min).**

1. Um aluno começa uma frase e para no meio (ex.: "Hoje o céu está muito..."). O outro fala **só a próxima palavra** mais provável — sem pensar no sentido geral, só no que costuma vir.
2. Continuem, **uma palavra de cada vez**, alternando. Vejam a frase crescer por previsão pura.
3. **Experimento:** comecem uma frase que peça um **fato específico** ("A capital da Mongólia é...") e completem por "som"/probabilidade, sem consultar nada. A resposta saiu? Estava certa? Como vocês saberiam?
4. Discutam: vocês "entenderam" o assunto ou só completaram o provável? É isso que o LLM faz.

Socializem: quando completar pelo provável deu certo, e quando produziu uma bobagem dita com confiança?

## Avaliação

```quiz
- pergunta: O que um LLM faz, em essência?
  alternativas:
    - texto: Busca a resposta certa em um banco de dados na internet
    - texto: Prevê o próximo token (pedaço de texto) mais provável, repetidamente
      correta: true
    - texto: Entende o assunto como um humano e raciocina sobre ele
    - texto: Apenas copia frases prontas que decorou
  feedback: >
    Um LLM é um previsor de texto: token a token, escolhe o mais provável e encadeia.
    Não busca nem entende no sentido humano.
- pergunta: Por que um LLM pode dar uma resposta errada com total confiança?
  alternativas:
    - texto: Porque está com defeito
    - texto: Porque ele completa o texto mais provável, não consulta um banco de fatos
      correta: true
    - texto: Porque sempre mente de propósito
    - texto: Porque ficou sem internet
  feedback: >
    Ele gera o que é provável, não o que é verdadeiro. Sem consultar fatos, pode soar
    seguro e estar errado — assunto da aula de alucinações.
- pergunta: O que torna um LLM "grande" (Large)?
  alternativas:
    - texto: O tamanho físico do computador
    - texto: A enorme quantidade de texto de treino e de pesos (bilhões) da rede neural
      correta: true
    - texto: O tamanho da tela
    - texto: A quantidade de usuários
  feedback: >
    "Grande" se refere à escala: treinado com texto massivo e composto de bilhões de
    pesos numa rede neural profunda.
```

## Fechamento

Hoje você descobriu que:

- Um **[[llm|LLM]]** é uma [[rede-neural|rede neural profunda]] treinada em texto massivo para **prever o próximo token**.
- Toda "conversa" é essa **previsão encadeada**, repetida muito rápido.
- O LLM **não entende** nem **busca na internet** por padrão — por isso pode errar com confiança.
- As **versões** mudam o tempo todo; o **conceito** (prever token) é o que fica.

**Próxima aula:** falei "token" o tempo todo. Mas o que é um token, afinal, e como um texto vira número pra máquina? Na Aula 10: **tokens, embeddings e vetores**.

:::roteiro
Abrir desmontando a mágica: "parece que tem alguém pensando — não tem". A mecânica "prever o próximo token" é o coração; o diagrama mostra o encadeamento. O erro "entende e busca na internet" é o mais importante da aula e prepara alucinações (23). A `:::curiosidade` das versões evita datar a aula — enfatize conceito > versão (cuidado ao citar modelos, eles envelhecem). A prática "seja o LLM" é poderosa: completar por probabilidade e ver sair bobagem confiante é a lição viva. Conteúdo verificado na web (cenário 2026). 8 min pro quiz.
:::
