---
titulo: IA, ML, Deep Learning e IA Generativa
tema: Fundamentos de IA
disciplina: inteligencia-artificial
serie: Extra
prerequisitos: [O que é Inteligência Artificial, História da IA e os Invernos]
objetivos:
  - Organizar IA, machine learning, deep learning e IA generativa como campos aninhados
  - Explicar o que cada camada acrescenta à anterior
  - Classificar exemplos do dia a dia na camada correta
trilha: fundamentos-de-ia
ordem: 3
modo_origem: tema
fontes:
  - lake/inteligencia-artificial/ufpr
revisao: false
status: aprovada
versao: 1
atualizado_em: 2026-06-15
---

"IA", "machine learning", "deep learning", "IA generativa" — você ouve esses quatro termos jogados como se fossem a mesma coisa, inclusive por gente que deveria saber a diferença. Não são sinônimos. Eles são como bonecas russas, uma dentro da outra: cada uma cabe dentro da maior e acrescenta algo novo. Confundir os quatro é como chamar todo animal de "cachorro". Hoje você organiza esse alfabeto de uma vez — e sai falando de IA com a precisão de quem entende, não de quem repete manchete.

## Objetivos

Ao final desta aula, você será capaz de:

- **Organizar** IA, machine learning, deep learning e IA generativa como campos **aninhados**.
- Explicar **o que cada camada acrescenta** à anterior.
- **Classificar** exemplos do dia a dia na camada correta.

## Pré-requisitos

Ter visto as **Aulas 01 e 02** (o que é IA e sua história).

## Desenvolvimento

### As bonecas russas da IA

A relação entre os quatro termos não é de sinônimos nem de rivais — é de **continência**: um vive dentro do outro.

```diagrama-progressivo
titulo: Os quatro campos, do maior ao menor
camadas:
  - rotulo: 1. Inteligência Artificial (a maior)
    conteudo: O campo todo — qualquer técnica que faça máquinas realizarem tarefas inteligentes. Inclui até abordagens antigas baseadas em regras escritas à mão.
  - rotulo: 2. Machine Learning (dentro da IA)
    conteudo: A parte da IA em que a máquina APRENDE padrões a partir de dados, em vez de seguir regras fixas. É o coração da IA moderna.
  - rotulo: 3. Deep Learning (dentro do ML)
    conteudo: Um tipo de machine learning que usa redes neurais com muitas camadas. É o que destravou reconhecer imagens, voz e linguagem com qualidade altíssima.
  - rotulo: 4. IA Generativa (dentro do Deep Learning)
    conteudo: Modelos de deep learning que CRIAM conteúdo novo — texto, imagem, áudio, vídeo. É a onda atual (ChatGPT, geradores de imagem).
```

:::conceito Aprendizado de máquina (Machine Learning)
É o ramo da [[inteligencia-artificial|IA]] em que o sistema **aprende padrões a partir de dados** em vez de seguir regras escritas por um programador. Mostre milhares de e-mails marcados como "spam" ou "não spam", e o [[aprendizado-de-maquina|ML]] descobre sozinho o que caracteriza um spam. É a virada que tirou a IA do segundo inverno.

:::

### O que o "profundo" acrescenta

:::conceito Deep Learning e IA Generativa
**[[deep-learning|Deep learning]]** ("aprendizado profundo") é um tipo de ML que usa **redes neurais com muitas camadas** empilhadas — inspiradas, de longe, no cérebro. Cada camada aprende algo mais abstrato que a anterior. A **[[ia-generativa|IA generativa]]** é um uso do deep learning voltado a **criar** conteúdo novo (textos, imagens, músicas) em vez de só classificar ou prever. ChatGPT e geradores de imagem são IA generativa.

:::

A regra de ouro: **toda IA generativa é deep learning; todo deep learning é machine learning; todo machine learning é IA — mas não o contrário.** Um semáforo com regra fixa é "IA antiga" mas não é ML. Um filtro de spam é ML mas pode não ser deep learning. E assim por diante.

:::atencao Erro comum
Usar os quatro termos como sinônimos — "ah, é tudo IA". Tecnicamente "é tudo IA" até está certo (todos estão dentro dela!), mas chamar o ChatGPT de "machine learning comum" ou um filtro de spam de "IA generativa" mostra que a pessoa não entende as camadas. Precisão importa: cada termo diz algo específico sobre **como** o sistema funciona.

:::

:::dica No mercado, a palavra certa abre portas
Numa entrevista ou reunião, usar "deep learning" e "IA generativa" no lugar certo mostra domínio real. Quem fala "fiz um modelo de IA" diz pouco; quem fala "usei machine learning para classificar e um modelo generativo para resumir" mostra que sabe do que fala. Vocabulário preciso é cartão de visitas técnico.

:::

## Prática

**Atividade "em que camada cai?" (em duplas, sem computador, ~15 min).** Classifiquem cada exemplo na camada **mais específica** possível (IA-com-regras / Machine Learning / Deep Learning / IA Generativa):

> um filtro de spam que aprendeu com e-mails · o ChatGPT escrevendo uma redação · um gerador de imagens a partir de texto · um jogo de xadrez antigo que segue regras programadas · reconhecimento facial que desbloqueia o celular · uma assistente que cria uma música nova

1. Para cada um, escrevam a camada e **uma frase** justificando.
2. Quais foram **difíceis** de classificar? Por quê?
3. Desenhem as quatro bonecas russas e coloquem cada exemplo no anel certo.

Cada dupla apresenta um exemplo difícil. A turma debate: caiu na camada certa?

## Avaliação

```quiz
- pergunta: Qual a relação correta entre os quatro campos?
  alternativas:
    - texto: São quatro coisas separadas e sem relação
    - texto: IA contém ML, que contém Deep Learning, que contém IA Generativa
      correta: true
    - texto: IA Generativa é a maior e contém todas as outras
    - texto: São quatro nomes para a mesma coisa
  feedback: >
    São aninhados como bonecas russas: IA ⊃ Machine Learning ⊃ Deep Learning ⊃ IA
    Generativa. Cada um é um caso mais específico do anterior.
- pergunta: O que define o machine learning dentro da IA?
  alternativas:
    - texto: Seguir regras fixas escritas por um programador
    - texto: Aprender padrões a partir de dados, em vez de regras fixas
      correta: true
    - texto: Ter consciência própria
    - texto: Ser sempre um robô físico
  feedback: >
    ML é a parte da IA que aprende de dados. Regras fixas escritas à mão são IA
    "antiga", mas não machine learning.
- pergunta: O ChatGPT e os geradores de imagem são exemplos de quê?
  alternativas:
    - texto: IA com regras fixas
    - texto: IA Generativa (que é um tipo de deep learning)
      correta: true
    - texto: Machine learning que não é deep learning
    - texto: Não são IA
  feedback: >
    Eles criam conteúdo novo usando deep learning — são IA generativa, o anel mais
    interno e a onda do momento.
```

## Fechamento

Hoje você descobriu que:

- **IA, ML, deep learning e IA generativa** são campos **aninhados**, não sinônimos.
- **[[aprendizado-de-maquina|Machine learning]]** é a IA que aprende de dados; **[[deep-learning|deep learning]]** é ML com redes de muitas camadas; **[[ia-generativa|IA generativa]]** é deep learning que **cria** conteúdo.
- Regra de ouro: toda IA generativa é deep learning, todo deep learning é ML, todo ML é IA — nunca o contrário.
- **Vocabulário preciso** é cartão de visitas técnico.

**Próxima aula:** falamos que a máquina "aprende". Mas o que isso quer dizer, de verdade? Na Aula 04 a gente abre o capô e vê como uma máquina aprende a partir de dados.

:::roteiro
Abrir com os quatro termos jogados na mesa e perguntar "qual a diferença?" — quase ninguém sabe, e é o gancho. A metáfora das bonecas russas é o coração; desenhe os anéis concêntricos no quadro e vá preenchendo. O diagrama-progressivo reforça do maior ao menor. O erro "é tudo a mesma coisa" é o alvo. Na prática, os exemplos difíceis (reconhecimento facial: deep learning; xadrez antigo: regras) geram o melhor debate. A fonte ufpr (lake) embasa o enquadramento conceitual. Conteúdo estável — sem necessidade de web nesta. 8 min pro quiz.
:::
