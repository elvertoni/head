---
titulo: Evals e Economia de Tokens
tema: Fundamentos de IA
disciplina: inteligencia-artificial
serie: Extra
prerequisitos: [Alucinações — Causas, Tipos e Mitigação, Tokens, Embeddings e Vetores]
objetivos:
  - Explicar o que é um eval e por que medir vence o achismo
  - Entender que o uso de IA tem custo medido em tokens
  - Reconhecer práticas para economizar tokens sem perder qualidade
trilha: fundamentos-de-ia
ordem: 24
modo_origem: tema
fontes: []
revisao: false
status: aprovada
versao: 1
atualizado_em: 2026-06-15
---

Você ajustou seu prompt, deu contexto, ligou um RAG. A resposta parece melhor. **Parece.** Mas será que está mesmo, ou você só se acostumou? E mais: cada uma dessas respostas **custou dinheiro** — porque usar IA não é de graça, e o custo pode escapar do controle sem você perceber. As duas perguntas que todo profissional de IA aprende a responder são: "como **medir** se está bom?" e "como não **estourar o custo**?". Esta penúltima aula te dá as duas respostas: evals e economia de tokens.

## Objetivos

Ao final desta aula, você será capaz de:

- Explicar o que é um **eval** e por que **medir** vence o achismo.
- Entender que o uso de IA tem **custo medido em [[tokens]]**.
- Reconhecer práticas para **economizar tokens** sem perder qualidade.

## Pré-requisitos

Ter visto a **Aula 23** (alucinações) e a **Aula 10** (tokens).

## Desenvolvimento

### Medir, não achar

:::conceito Eval (avaliação)
É uma forma **sistemática** de medir a qualidade das respostas de uma IA — em vez de confiar no "achei que ficou bom". Você monta um conjunto de perguntas com as respostas certas (um "gabarito") e verifica quantas a IA acerta, com critérios claros. É o equivalente, no mundo da IA, ao **teste** que um programador roda no código antes de confiar nele.

:::

:::atencao Erro comum
Avaliar IA "no olho": mudar o prompt, ler uma resposta, achar que melhorou e seguir. Isso engana — a impressão é subjetiva e você pode ter piorado sem notar. Sem um eval (um conjunto fixo de casos com gabarito), você está **adivinhando** se a mudança ajudou. Profissional sério mede; amador acha.

:::

### IA custa — e a conta é em tokens

Lembra dos [[tokens]] da Aula 10? Eles não são só a unidade de texto — são a unidade de **cobrança**. Cada token que entra (sua pergunta + contexto) e cada token que sai (a resposta) é cobrado. Isso tem consequências práticas diretas:

```diagrama-progressivo
titulo: Onde o custo escapa (e como segurar)
camadas:
  - rotulo: 1. Contexto inchado custa caro
    conteudo: Lembra da Aula 15? Colar documentos demais não só piora a resposta - cada token extra é pago. Contexto enxuto economiza e melhora ao mesmo tempo.
  - rotulo: 2. Conversas longas crescem
    conteudo: A cada turno, todo o histórico é reenviado. Conversas muito longas ficam caras. Resumir ou recomeçar quando muda de assunto controla isso.
  - rotulo: 3. Reaproveitar o que repete
    conteudo: Partes fixas (instruções padrão) podem ser reaproveitadas em vez de reenviadas inteiras toda vez, cortando custo em pedidos repetitivos.
  - rotulo: 4. Escolher o tamanho certo do modelo
    conteudo: Nem toda tarefa precisa do modelo mais caro. Tarefas simples rodam em modelos menores e mais baratos. Use o canhão só quando precisa.
```

:::dica Eficiência é o que separa protótipo de produto
Um app de IA que funciona na demo mas custa uma fortuna por usuário **não vira negócio**. Por isso, quem constrói IA de verdade vive de dois números: **qualidade** (medida por evals) e **custo** (medido em tokens). Equilibrar os dois — boas respostas a um custo viável — é a engenharia que transforma uma ideia legal num produto que se sustenta. É também por isso que "menos contexto, porém mais relevante" (Aula 15) é regra de ouro: economiza **e** melhora.

:::

## Prática

**Atividade "crie seu eval + cace o custo" (em duplas, sem computador, ~15 min).**

Parte A — **eval**:
1. Imaginem um assistente que responde dúvidas de matemática da turma. Montem um **mini-eval**: escrevam **5 perguntas com a resposta certa** (o gabarito).
2. Definam o **critério de acerto**: a resposta tem que bater exatamente? aceitar formas diferentes? Como vocês decidiriam "passou ou não"?

Parte B — **custo**:
3. Lembrando que tudo é cobrado por token: das duas formas de pedir abaixo, qual gasta **menos** e por quê?
   - (i) colar as 90 páginas do livro e perguntar; (ii) colar só o parágrafo relevante e perguntar.
4. Citem **uma** prática da aula para reduzir custo sem piorar a resposta.

Cada dupla apresenta uma pergunta do seu eval e sua escolha de custo. A turma discute: o eval pega uma resposta errada de verdade?

## Avaliação

```quiz
- pergunta: O que é um eval?
  alternativas:
    - texto: Um modelo de IA mais caro
    - texto: Uma forma sistemática de medir a qualidade das respostas, com casos e gabarito
      correta: true
    - texto: Uma ferramenta de busca
    - texto: O custo da IA em reais
  feedback: >
    Eval é medir qualidade com método (casos + gabarito + critérios), como um teste de
    software — em vez de avaliar "no olho".
- pergunta: Por que avaliar IA "no olho" é um problema?
  alternativas:
    - texto: Porque é mais rápido
    - texto: Porque a impressão é subjetiva — você pode piorar sem perceber
      correta: true
    - texto: Porque é proibido
    - texto: Porque a IA não pode ser avaliada
  feedback: >
    Sem um conjunto fixo de casos com gabarito, você adivinha se a mudança ajudou. Medir
    com eval troca o achismo por evidência.
- pergunta: Qual prática reduz o custo (em tokens) sem piorar a resposta?
  alternativas:
    - texto: Colar o máximo de documentos possível no contexto
    - texto: Enviar só o contexto relevante, em vez de tudo "para garantir"
      correta: true
    - texto: Usar sempre o modelo mais caro para tudo
    - texto: Repetir a pergunta várias vezes
  feedback: >
    Contexto enxuto economiza tokens E melhora a resposta (Aula 15). Inchar o contexto
    custa mais e ainda dilui a atenção.
```

## Fechamento

Hoje você descobriu que:

- **[[evals|Eval]]** mede a qualidade da IA com método (casos + gabarito) — **medir vence achar**.
- Usar IA **custa**, e a conta é em **[[tokens]]** (entrada + saída).
- O custo escapa com **contexto inchado** e **conversas longas**; controla-se com contexto enxuto, reaproveitamento e o **modelo do tamanho certo**.
- Equilibrar **qualidade × custo** é o que transforma protótipo em **produto**.

**Última aula:** você já sabe construir, usar e medir IA. Falta a pergunta mais importante de todas — **devemos**? Fechamos a trilha com **ética, responsabilidade e IA no Brasil**.

:::roteiro
Penúltima aula — duas ideias práticas: medir (eval) e custo (tokens). Abrir com "parece melhor — mas parece?" para motivar o eval. Eval = teste de software (analogia forte se já viram testes). O erro "avaliar no olho" é o alvo da parte de qualidade. Tokens como unidade de COBRANÇA (não só de texto) é a virada da parte de custo — amarra com a aula 15 (contexto enxuto economiza E melhora). A `:::dica` "demo barata vs produto caro" dá o porquê profissional. A prática junta os dois: criar eval + escolher o pedido mais barato. Aponte pro fechamento ético. 8 min pro quiz.
:::
