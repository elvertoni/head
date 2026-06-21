---
titulo: Transformers e Atenção
tema: Fundamentos de IA
disciplina: inteligencia-artificial
serie: Extra
prerequisitos: [Tokens, Embeddings e Vetores]
objetivos:
  - Explicar o problema que o transformer resolveu em relação aos modelos antigos
  - Entender a ideia de atenção como "olhar para as palavras que importam"
  - Reconhecer o transformer como a base dos LLMs atuais
trilha: fundamentos-de-ia
ordem: 11
slug: transformers-e-atencao
modo_origem: tema
fontes: []
revisao: false
status: aprovada
versao: 1
atualizado_em: 2026-06-15
---

Leia esta frase: "Joana colocou o livro na mochila porque **ela** estava pesada." Quem estava pesada — Joana ou a mochila? Você resolveu isso num piscar de olhos, **prestando atenção** na palavra certa ("mochila") e ignorando o resto. Por décadas, os computadores eram péssimos nisso: liam palavra por palavra, em fila, e quando chegavam no "ela" já tinham meio esquecido o começo. Em 2017, uma invenção mudou o jogo ao ensinar a máquina a fazer o que você acabou de fazer — olhar para as palavras que importam, todas de uma vez. Essa invenção se chama **transformer**, e o "T" do ChatGPT vem dela.

## Objetivos

Ao final desta aula, você será capaz de:

- Explicar o **problema** que o transformer resolveu frente aos modelos antigos.
- Entender a ideia de **atenção** como "olhar para as palavras que importam".
- Reconhecer o **transformer** como a base dos LLMs atuais.

## Pré-requisitos

Ter visto a **Aula 10** (tokens e embeddings) e a **Aula 09** (o que é um LLM).

## Desenvolvimento

### O problema dos modelos antigos

Antes de 2017, os modelos de linguagem liam o texto **em fila**, uma palavra de cada vez, carregando uma "memória" do que veio antes. O problema: em frases longas, a memória do começo **desbotava**. Quando o modelo chegava ao fim, já tinha perdido pistas importantes do início — como tentar entender uma frase enorme lembrando só das últimas palavras.

:::conceito Transformer
É a **arquitetura** de rede neural, apresentada em 2017 no artigo "Attention is All You Need", que virou a base de praticamente todos os [[llm|LLMs]] modernos. A grande sacada: em vez de ler em fila e esquecer, o transformer olha para **todas as palavras ao mesmo tempo** e decide, para cada uma, quais outras são relevantes. O "**T**" de Chat**GPT** (Generative Pre-trained **Transformer**) vem daqui.

:::

### Atenção: olhar para o que importa

O mecanismo que torna isso possível tem um nome perfeito: atenção.

:::conceito Atenção (attention)
É o mecanismo que permite ao modelo, ao processar uma palavra, **pesar quais outras palavras do texto importam** para entendê-la. No nosso exemplo, ao processar "ela", a atenção "ilumina" a palavra "mochila" mais que "Joana". É como destacar com marca-texto, para cada palavra, as outras de que ela depende — e fazer isso para todas, simultaneamente.

:::

```diagrama-progressivo
titulo: Atenção em ação - "ela estava pesada"
camadas:
  - rotulo: 1. O modelo chega em "ela"
    conteudo: Precisa decidir a quem "ela" se refere para entender a frase.
  - rotulo: 2. Olha todas as palavras de uma vez
    conteudo: Diferente dos modelos antigos, não lê em fila esquecendo o começo - tem todas as palavras disponíveis ao mesmo tempo.
  - rotulo: 3. Pesa a relevância (atenção)
    conteudo: Calcula quanto cada palavra importa para "ela". "Mochila" recebe peso alto; "porque" recebe peso baixo.
  - rotulo: 4. Decide com contexto
    conteudo: Com "mochila" em destaque, o modelo entende que é a mochila que está pesada. Contexto resolvido, sem perder o começo da frase.
```

:::atencao Erro comum
Imaginar que o transformer "lê em ordem, como a gente". Não é bem assim: ele processa as palavras **em paralelo** (todas juntas) e usa a atenção para descobrir as relações entre elas. Essa leitura paralela é, inclusive, o que permitiu treinar modelos gigantes de forma viável — e é parte do porquê da explosão da IA que vimos na Aula 02.

:::

:::dica Por que isto importa pra você
Você não vai programar um transformer tão cedo — mas entender que a IA moderna funciona por **atenção ao contexto** explica muita coisa do dia a dia: por que dar **mais contexto** num prompt melhora a resposta, por que o modelo "se perde" em textos enormes, por que a ordem das informações importa. Esse entendimento vira habilidade prática quando você aprender a conversar com a IA (próximos módulos).

:::

## Prática

**Atividade "marca-texto da atenção" (em duplas, sem computador, ~15 min).**

Para cada frase, a dupla decide: ao entender a **palavra em negrito**, em quais outras palavras o modelo deveria "prestar atenção" (marcar)?

1. "O cachorro perseguiu o gato até **ele** subir na árvore." (quem subiu?)
2. "Maria deu o presente para a irmã porque era o aniversário **dela**." (de quem?)
3. "Coloquei o bolo no forno; vou tirá-**lo** em 40 minutos." (tirar o quê?)
4. "Os alunos terminaram a prova e **a** entregaram." (entregaram o quê?)

1. Sublinhem, em cada frase, a(s) palavra(s) de **atenção alta**.
2. Há frase **ambígua**, em que daria pra prestar atenção em mais de uma? Qual?
3. Discutam: como vocês resolveram tão rápido? É isso que a atenção faz na máquina.

Socializem as ambíguas — onde até humanos hesitam, a IA também pode errar.

## Avaliação

```quiz
- pergunta: Qual problema dos modelos antigos o transformer resolveu?
  alternativas:
    - texto: Eles eram rápidos demais
    - texto: Liam em fila e "esqueciam" o começo de textos longos
      correta: true
    - texto: Não usavam eletricidade
    - texto: Só funcionavam com imagens
  feedback: >
    Modelos antigos liam palavra a palavra e perdiam o início em frases longas. O
    transformer olha tudo de uma vez e pesa o que importa.
- pergunta: O que faz o mecanismo de atenção?
  alternativas:
    - texto: Apaga as palavras menos usadas
    - texto: Pesa quais palavras do texto importam para entender cada palavra
      correta: true
    - texto: Traduz o texto para inglês
    - texto: Conta quantas letras tem a frase
  feedback: >
    Atenção é destacar, para cada palavra, as outras de que ela depende — como
    marca-texto, e para todas ao mesmo tempo.
- pergunta: Qual a relação entre transformer e os LLMs atuais?
  alternativas:
    - texto: Nenhuma, são coisas diferentes
    - texto: O transformer (2017) é a arquitetura base de praticamente todos os LLMs modernos
      correta: true
    - texto: Transformer substituiu os LLMs
    - texto: LLMs existiam muito antes do transformer
  feedback: >
    O transformer é a fundação dos LLMs atuais — o "T" de GPT vem dele. Foi o que
    destravou a IA generativa moderna.
```

## Fechamento

Hoje você descobriu que:

- Modelos antigos liam **em fila** e esqueciam o começo; o **[[transformers|transformer]]** (2017) olha tudo de uma vez.
- A **[[atencao|atenção]]** pesa, para cada palavra, quais outras importam — resolvendo o contexto.
- O transformer processa palavras **em paralelo**, o que viabilizou treinar modelos gigantes.
- É a **base** de praticamente todos os LLMs atuais (o "T" de GPT).

**Próxima aula:** se o modelo aprendeu tudo num treino, o que acontece depois? Por que ele não sabe a notícia de ontem? Na Aula 12: **treino, fine-tuning e cutoff**.

:::roteiro
Abrir com a frase ambígua "ela estava pesada" — todos resolvem na hora, e é a deixa pra atenção. O contraste com modelos antigos (ler em fila e esquecer) dá o "porquê" do transformer. Atenção = marca-texto do que importa: a analogia é forte. O erro "lê em ordem como a gente" introduz o paralelismo (que conecta com o porquê da explosão, aula 02). A prática do marca-texto é atenção desplugada; as frases ambíguas mostram que IA também hesita. Conteúdo histórico/conceitual estável (transformer 2017). 8 min pro quiz.
:::
