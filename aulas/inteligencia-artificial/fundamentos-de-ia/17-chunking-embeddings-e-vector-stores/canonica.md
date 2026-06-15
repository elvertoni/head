---
titulo: Chunking, Embeddings e Vector Stores
tema: Fundamentos de IA
disciplina: inteligencia-artificial
serie: Extra
prerequisitos: [RAG — Recuperação com Geração Aumentada, Tokens, Embeddings e Vetores]
objetivos:
  - Explicar o que é chunking e por que o tamanho do pedaço importa
  - Relacionar embeddings e vector store à busca por significado
  - Descrever o pipeline de ingestão de um RAG
trilha: fundamentos-de-ia
ordem: 17
modo_origem: material
fontes:
  - lake/inteligencia-artificial/ia-master
  - lake/inteligencia-artificial/elite-wiki/arquitetura/blueprint-sistema-rag-para-suporte-a-alunos.md
revisao: true
status: aprovada
versao: 1
atualizado_em: 2026-06-15
---

Na aula passada, o [[rag|RAG]] "buscou o trecho certo" do acervo como se fosse mágica. Hora de abrir a caixa. Como um sistema acha, no meio de 300 páginas, justo o parágrafo que responde a sua pergunta — mesmo que você use palavras totalmente diferentes das do texto? A resposta junta três peças que vão fechar o módulo e amarrar tudo que você viu sobre [[tokens]] e [[embeddings]]: **chunking, embeddings e vector stores**. É a engrenagem que faz o RAG girar.

## Objetivos

Ao final desta aula, você será capaz de:

- Explicar o que é **chunking** e por que o **tamanho do pedaço** importa.
- Relacionar **embeddings** e **vector store** à **busca por significado**.
- Descrever o **pipeline de ingestão** de um RAG.

## Pré-requisitos

Ter visto a **Aula 16** (RAG) e a **Aula 10** (tokens e embeddings).

## Desenvolvimento

### Primeiro: quebrar em pedaços (chunking)

Não dá pra vetorizar um livro inteiro como um bloco só — o significado vira uma papa sem foco. Então o primeiro passo é cortar.

:::conceito Chunking
É **cortar o documento em pedaços menores** (chunks) antes de processá-lo. Cada pedaço será buscável por conta própria. O **tamanho** é uma decisão importante: pedaço **grande demais** mistura vários assuntos e perde foco; **pequeno demais** corta a ideia no meio e perde sentido. Costuma-se usar uma pequena **sobreposição** entre chunks, para nenhuma ideia ficar partida bem na fronteira.

:::

### Depois: virar vetor e guardar

Aí entram dois velhos conhecidos da Aula 10, agora trabalhando juntos:

```diagrama-progressivo
titulo: O pipeline de ingestão do RAG
camadas:
  - rotulo: 1. Chunking
    conteudo: O documento é cortado em pedaços do tamanho certo (com leve sobreposição). Cada chunk vira uma unidade buscável.
  - rotulo: 2. Embeddings
    conteudo: Cada chunk vira um vetor de significado (Aula 10). Pedaços de sentido parecido ficam com vetores próximos.
  - rotulo: 3. Vector store
    conteudo: Os vetores são guardados num banco especial (o vector store), feito para achar rapidamente os mais parecidos com um vetor de consulta.
  - rotulo: 4. Busca na hora da pergunta
    conteudo: A pergunta também vira vetor; o vector store devolve os chunks de vetor mais próximo. São esses que vão para o contexto do LLM.
```

:::conceito Vector store
É o **banco que guarda os embeddings** dos chunks e responde rápido à pergunta "quais são os mais parecidos com este vetor?". É onde o [[rag]] busca na hora da consulta. Como compara **vetores** (significado) e não palavras, ele acha "como cancelar minha assinatura" num texto que diz "encerrar plano" — sem nenhuma palavra em comum.

:::

:::atencao Erro comum
Achar que a busca é por **palavra-chave**, como o Ctrl+F. Não é. A busca do RAG é por **significado** (vetores próximos): pode acertar sem nenhuma palavra igual — e, às vezes, errar quando o sentido é ambíguo. E cuidado com o chunk: se a recuperação está trazendo trechos ruins, o **tamanho do chunk** costuma ser o primeiro suspeito, não o modelo.

:::

:::dica Você fechou o ciclo
Repare como tudo se conecta: [[tokens]] e [[embeddings]] (Aula 10) viram a base; [[rag]] (Aula 16) usa essa base; e agora você vê a engrenagem completa. Sistemas de busca de empresas, assistentes que respondem sobre documentos internos, suporte automático — tudo roda sobre chunking + embeddings + vector store. É um dos conjuntos de habilidades mais pedidos em vagas de IA hoje.

:::

## Prática

**Atividade "RAG por dentro, na mão" (em duplas, sem computador, ~15 min).**

Parte A — **chunking**:
1. Peguem um texto curto (um parágrafo do livro ou do regulamento). Cortem em **chunks** de 1 a 2 frases. Quantos deram?
2. Testem um chunk **grande demais** (o parágrafo inteiro) e um **pequeno demais** (3 palavras). Qual responderia melhor a uma pergunta específica? Por quê?

Parte B — **busca por significado**:
3. Escrevam 4 chunks em fichas. Façam uma pergunta usando **sinônimos** (sem repetir as palavras das fichas).
4. Qual ficha responde? Vocês acharam **pelo significado**, não pela palavra igual — exatamente como o vector store faz.

Socializem: o que acontece se dois chunks tiverem significados muito parecidos? Qual o sistema escolheria?

## Avaliação

```quiz
- pergunta: O que é chunking?
  alternativas:
    - texto: Treinar o modelo do zero
    - texto: Cortar o documento em pedaços menores antes de vetorizá-lo
      correta: true
    - texto: Apagar partes irrelevantes do texto
    - texto: Traduzir o documento
  feedback: >
    Chunking é fatiar o documento em pedaços buscáveis. O tamanho importa: nem grande
    demais (perde foco) nem pequeno demais (perde sentido).
- pergunta: O que faz um vector store?
  alternativas:
    - texto: Guarda os embeddings e acha rapidamente os mais parecidos com a consulta
      correta: true
    - texto: Treina o LLM
    - texto: Armazena imagens apenas
    - texto: Corta o texto em pedaços
  feedback: >
    O vector store guarda os vetores dos chunks e responde "quais os mais próximos?" —
    é onde o RAG busca por significado.
- pergunta: A busca do RAG funciona como o Ctrl+F (palavra-chave)?
  alternativas:
    - texto: Sim, procura a palavra exata
    - texto: Não — busca por significado (vetores próximos), podendo achar sem palavras em comum
      correta: true
    - texto: Sim, mas só em PDFs
    - texto: Não, ela busca por cor
  feedback: >
    É busca semântica: compara significado (vetores), não letras. Acha "encerrar plano"
    quando você pergunta "cancelar assinatura".
```

## Fechamento

Hoje você descobriu que:

- **[[chunking|Chunking]]** corta o documento em pedaços; o **tamanho** do chunk é decisão crítica.
- Cada chunk vira **[[embeddings|embedding]]** (vetor de significado) e é guardado num **[[vector-store|vector store]]**.
- A busca do [[rag|RAG]] é por **significado** (vetores próximos), não por palavra-chave.
- Esse pipeline — chunk → embedding → vector store → busca — é a **engrenagem do RAG**.

**Próximo módulo (IA que age):** até aqui a IA respondeu. No próximo módulo ela passa a **agir** — vamos conhecer os **agentes** e como a IA usa ferramentas para fazer coisas no mundo.

:::roteiro
Fecha o módulo amarrando com a Aula 10 (tokens/embeddings) e 16 (RAG) — mostre que tudo se conecta. Vem de material ia-master + blueprint elite-wiki (modo Material). Chunking primeiro: o tradeoff tamanho (grande perde foco / pequeno perde sentido) é o conceito central. Vector store = busca por significado, não palavra — o exemplo "cancelar assinatura" / "encerrar plano" é o aha. A prática na mão (chunking + busca por sinônimo) torna concreto o abstrato. O erro "é Ctrl+F" é comum. Aponte pro módulo de agentes. 8 min pro quiz.
:::
