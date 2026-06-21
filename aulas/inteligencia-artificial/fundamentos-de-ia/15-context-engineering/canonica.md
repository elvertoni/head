---
titulo: Context Engineering
tema: Fundamentos de IA
disciplina: inteligencia-artificial
serie: Extra
prerequisitos: [Prompt Engineering, Treino, Fine-tuning e Cutoff]
objetivos:
  - Distinguir prompt engineering de context engineering
  - Explicar o que é a janela de contexto e por que ela é limitada
  - Reconhecer que mais contexto relevante vence mais contexto em quantidade
trilha: fundamentos-de-ia
ordem: 15
slug: context-engineering
modo_origem: material
fontes:
  - lake/inteligencia-artificial/ia-coders/o-que-e-context-engineering.md
revisao: true
status: aprovada
versao: 1
atualizado_em: 2026-06-15
---

Na aula passada você aprendeu a **fazer a pergunta** certa. Mas existe uma camada acima disso, e quem trabalha com IA de verdade jura que ela é ainda mais importante: **o que você coloca junto da pergunta**. Lembra do [[cutoff]]? O modelo não conhece o seu material nem o que é recente. Então, se você quer que ele responda sobre o regulamento da sua escola, você precisa **entregar** esse regulamento junto. Decidir exatamente o que entra nesse "junto" tem nome: context engineering. A tese de quem vive disso é forte — **contexto é o novo código**.

## Objetivos

Ao final desta aula, você será capaz de:

- Distinguir **prompt engineering** de **context engineering**.
- Explicar o que é a **janela de contexto** e por que ela é **limitada**.
- Reconhecer que **mais contexto relevante** vence **mais contexto em quantidade**.

## Pré-requisitos

Ter visto a **Aula 14** (prompt engineering) e a **Aula 12** (cutoff).

## Desenvolvimento

### Como perguntar x o que colocar junto

:::conceito Context engineering
Se o [[prompt-engineering|prompt engineering]] é decidir **como perguntar**, o **context engineering** é decidir **o que colocar ao lado da pergunta**: quais instruções, documentos, exemplos e histórico entram, em que ordem. Como o [[llm]] "não sabe nada além do que está no contexto", montar bem esse contexto é o que permite respostas certas sobre o **seu** material — não só sobre o que o modelo aprendeu no treino.

:::

Por isso a frase "contexto é o novo código": o que você coloca no contexto determina o que a IA consegue fazer, mais do que qualquer truque de frase.

### A janela de contexto é limitada

Tudo que entra — sua pergunta + os documentos + o histórico da conversa — ocupa a **janela de contexto**, medida em [[tokens]]. E ela tem **limite**. Não dá pra jogar a biblioteca inteira lá dentro.

:::atencao Erro comum
"Vou colar tudo no contexto só pra garantir." Péssima ideia. Encher a janela de informação irrelevante **dilui a atenção** do modelo (ele se perde no meio do monte — o famoso "lost in the middle"), **piora** a resposta e ainda **custa mais caro** (mais tokens = mais custo). A regra de ouro é o contrário do que parece: **menos contexto, porém mais relevante**, vence mais contexto jogado de qualquer jeito.

:::

```diagrama-progressivo
titulo: Montar o contexto certo
camadas:
  - rotulo: 1. A pergunta sozinha não basta
    conteudo: "Qual o prazo de entrega do trabalho?" O modelo não sabe - essa info está no regulamento da sua escola, não no treino dele.
  - rotulo: 2. Escolher o que entra
    conteudo: Em vez de colar o regulamento inteiro (90 páginas), você seleciona o trecho sobre prazos. Relevante, não volumoso.
  - rotulo: 3. Ordenar com cuidado
    conteudo: O modelo presta mais atenção no início e no fim do contexto. O essencial vai nos extremos, não enterrado no meio.
  - rotulo: 4. Resposta certa
    conteudo: Com o trecho certo no lugar certo, o modelo responde com base no SEU material - não chuta nem alucina.
```

:::dica RAG é context engineering automático
E quando o material é grande demais pra escolher o trecho na mão? Existe uma técnica que faz isso automaticamente: busca o pedaço mais relevante e injeta no contexto. Chama-se **[[rag|RAG]]**, e é exatamente o tema da próxima aula. Context engineering é a ideia; o RAG é uma das ferramentas mais poderosas pra colocá-la em prática.

:::

## Prática

**Atividade "monte o contexto" (em duplas, sem computador, ~15 min).** Vocês querem que a IA responda: **"Posso entregar o trabalho de história com 2 dias de atraso?"**

Têm à disposição estes "documentos" para colocar no contexto (mas a janela é pequena — escolham com cuidado):

> A) regulamento de prazos e atrasos da escola · B) cardápio da cantina · C) a ementa da disciplina de história · D) o histórico de notas da turma · E) a regra específica do professor sobre atrasos · F) notícias de esporte

1. **Selecionem** só os documentos **relevantes** para a pergunta. Quais entram? Quais ficam de fora?
2. Justifiquem por que **não** colocar os outros (lembrem: dilui atenção e custa caro).
3. **Ordem:** dos que entraram, qual vai no começo (mais importante)?
4. Comparem com outra dupla: escolheram o mesmo? Alguém colou demais "pra garantir"?

Socializem: o que acontece com a resposta se vocês incluírem o cardápio e as notícias junto?

## Avaliação

```quiz
- pergunta: Qual a diferença entre prompt engineering e context engineering?
  alternativas:
    - texto: São exatamente a mesma coisa
    - texto: Prompt é COMO perguntar; context engineering é O QUE colocar junto da pergunta
      correta: true
    - texto: Context engineering é só para imagens
    - texto: Prompt engineering treina o modelo
  feedback: >
    Prompt = como perguntar. Context engineering = o que entra junto (documentos,
    instruções, histórico) e em que ordem.
- pergunta: Por que "colar tudo no contexto só para garantir" é um erro?
  alternativas:
    - texto: Porque é proibido pelas empresas de IA
    - texto: Porque dilui a atenção, piora a resposta e custa mais (mais tokens)
      correta: true
    - texto: Porque o modelo fica mais inteligente
    - texto: Porque não muda nada
  feedback: >
    Encher a janela de coisa irrelevante causa "lost in the middle", piora a resposta e
    aumenta o custo. Menos contexto relevante vence mais contexto qualquer.
- pergunta: Por que dar contexto resolve o problema do cutoff?
  alternativas:
    - texto: Porque retreina o modelo na hora
    - texto: Porque o modelo responde com base no material que você fornece, mesmo sem ter aprendido no treino
      correta: true
    - texto: Porque apaga a memória do modelo
    - texto: Porque aumenta a janela de contexto infinitamente
  feedback: >
    O modelo não sabe além do treino, mas usa o que está no contexto. Fornecer o
    material certo o faz responder sobre o que ele nunca "aprendeu".
```

## Fechamento

Hoje você descobriu que:

- **[[context-engineering|Context engineering]]** é decidir **o que colocar junto** da pergunta — "contexto é o novo código".
- Tudo entra na **janela de contexto** (medida em [[tokens]]), que é **limitada**.
- **Encher** o contexto piora e encarece: vale **menos contexto, porém mais relevante**.
- O modelo presta mais atenção aos **extremos** — coloque o essencial no começo e no fim.

**Próxima aula:** e quando o material é grande demais pra escolher o trecho na mão? Entra a estrela do módulo: **RAG** — recuperação com geração aumentada.

:::roteiro
Esta aula vem de transcrição do curso ia-coders (modo Material), simplificada do contexto de coding-agents para o nível 14-18 — o essencial: prompt (como) vs context (o quê), janela limitada, menos-é-mais. O erro "colar tudo pra garantir" é o ponto central (lost in the middle + custo). A prática de selecionar documentos é context engineering desplugado puro — o cardápio e as notícias são as pegadinhas. Aponte forte pro RAG (aula 16) como a automação disso. Revisão aplicada: recortei o stack técnico (7 camadas, harness) por estar acima da faixa. 8 min pro quiz.
:::
