---
titulo: Histórias de Usuário
tema: Metodologias Ágeis
disciplina: analise-e-metodos-para-sistemas
serie: 1ª
prerequisitos: [Planejamento em Scrum — visão integrada]
objetivos:
  - Escrever histórias de usuário no formato Como/Quero/Para que
  - Explicar o papel dos critérios de aceitação
  - Reconhecer o Sprint Planning como o momento de selecionar histórias para a sprint
trilha: metodologias-ageis
ordem: 40
slug: historias-de-usuario
modo_origem: seed
fontes:
  - lake/analise-e-metodos-para-sistemas/AULA 40_ANÁLISE E MÉTODO PARA SISTEMAS.pptx
revisao: true
status: aprovada
versao: 2
atualizado_em: 2026-06-21
---

"O sistema deve permitir autenticação via credenciais com hash." Você entendeu? Provavelmente metade. Agora: "Como aluno, quero entrar no app com meu e-mail e senha para ver minhas notas." Essa qualquer um entende — inclusive quem vai usar o app. A diferença entre as duas frases é o segredo desta aula. No Scrum, a gente não descreve o que o sistema faz com jargão técnico frio; a gente conta o que a **pessoa** precisa, na forma de uma pequena história. Hoje você aprende a escrever essas histórias de usuário — a maneira ágil de registrar requisitos.

## Objetivos

Ao final desta aula, você será capaz de:

- **Escrever** histórias de usuário no formato **Como / Quero / Para que**.
- Explicar o papel dos **critérios de aceitação**.
- Reconhecer o **Sprint Planning** como o momento de selecionar histórias para a sprint.

## Pré-requisitos

Ter visto a **Aula 39** (visão integrada do Scrum) e o conceito de backlog.

## Desenvolvimento

### Em uma frase

:::importante
História de usuário é requisito escrito de um jeito que a pessoa entende, não o sistema.
:::

### A fórmula da história de usuário

:::conceito História de usuário
É uma descrição **simples e na linguagem do usuário** de algo que ele precisa, capturada numa fórmula de três partes:

> **Como** [tipo de usuário], **quero** [ação] **para que** [benefício].

Ela não descreve a solução técnica — descreve a **necessidade** e o **porquê**. Exemplo: *"Como cliente da cantina, quero salvar meus pedidos favoritos para que eu peça mais rápido no recreio."*

:::

As três partes importam: **quem** (o tipo de usuário), **o quê** (a ação que ele quer) e — a mais esquecida — **para quê** (o benefício, a razão). É o "para que" que mantém o time focado em valor, não em funcionalidade pela funcionalidade.

:::atencao Erro comum
Escrever a história focada na **solução técnica** em vez da **necessidade do usuário**. "Quero um banco de dados PostgreSQL" não é história de usuário — usuário nenhum quer um banco de dados, ele quer **resolver um problema**. A história diz o que a pessoa precisa e por quê; **como** fazer (a tecnologia) é decisão da equipe depois.

:::

### Como saber que está pronto

Uma história sozinha pode ser vaga. Por isso ela vem acompanhada de **critérios de aceitação**.

:::conceito Critérios de aceitação
São as condições que definem **quando** a história está concluída — o "combinado" que diz se ficou pronta de verdade. Para a história de salvar favoritos: *"o cliente consegue marcar um pedido como favorito; o favorito aparece no topo na próxima visita; é possível desmarcar."* Sem critérios, "pronto" vira opinião; com critérios, vira fato verificável.

:::

### Onde as histórias entram: o Sprint Planning

```diagrama-progressivo
titulo: Da história ao trabalho da sprint
camadas:
  - rotulo: 1. As histórias estão no backlog
    conteudo: O Product Owner mantém as histórias priorizadas no Product Backlog, as mais valiosas no topo.
  - rotulo: 2. Sprint Planning
    conteudo: No início da sprint, o time e o PO se reúnem, escolhem as histórias do topo que cabem na sprint e esclarecem dúvidas e critérios.
  - rotulo: 3. Estimativa e seleção
    conteudo: O time estima o esforço de cada história e seleciona um conjunto que caiba na sua capacidade. Essas viram o Sprint Backlog.
  - rotulo: 4. Mãos à obra
    conteudo: A sprint começa. O time trabalha nas histórias selecionadas até entregá-las prontas, segundo os critérios de aceitação.
```

:::dica Isto é levantamento de requisitos
Escrever boas histórias de usuário **é** uma das formas mais usadas de levantar requisitos de software hoje — uma habilidade central do técnico em desenvolvimento de sistemas. E note a conexão com Linguagens: você está produzindo um texto curto, claro e centrado em quem lê. Comunicação boa é requisito bom.

:::

## Prática

**Atividade "escreva a história" (em duplas, sem computador, ~15 min).** Para o **app da cantina**, escrevam **3 histórias de usuário** completas, cada uma no formato:

> Como [usuário], quero [ação] para que [benefício].

1. Escrevam as 3 histórias — cuidado para o **"para que"** ser um benefício real, não repetição da ação.
2. Para **uma** delas, escrevam **2 critérios de aceitação** (como saber que ficou pronta).
3. Troquem com outra dupla: a história da outra dupla está clara? O "para que" faz sentido? O critério é verificável?

Cada dupla lê uma história. A turma "audita": tem os três pedaços? O benefício é de verdade?

## Avaliação

```quiz
- pergunta: Qual é o formato correto de uma história de usuário?
  alternativas:
    - texto: "O sistema deve usar tecnologia X com configuração Y"
    - texto: "Como [usuário], quero [ação] para que [benefício]"
      correta: true
    - texto: "Lista de bugs a corrigir"
    - texto: "Nome do desenvolvedor responsável"
  feedback: >
    A história tem quem (usuário), o quê (ação) e por quê (benefício). Foca na
    necessidade da pessoa, não na solução técnica.
- pergunta: Por que escrever a história focada na solução técnica é um erro?
  alternativas:
    - texto: Porque o usuário quer resolver um problema, não uma tecnologia específica
      correta: true
    - texto: Porque tecnologia não importa para ninguém
    - texto: Porque histórias não podem ter benefício
    - texto: Porque o PO proíbe
  feedback: >
    Usuário nenhum quer "um banco de dados". A história descreve a necessidade e o
    porquê; a tecnologia é decisão da equipe, depois.
- pergunta: Para que servem os critérios de aceitação?
  alternativas:
    - texto: Para definir quem é o Scrum Master
    - texto: Para definir quando a história está concluída, de forma verificável
      correta: true
    - texto: Para listar os bugs do sistema
    - texto: Para escolher a linguagem de programação
  feedback: >
    Critérios de aceitação são o "combinado" que torna o "pronto" verificável, em vez
    de opinião. Eles dizem quando a história está realmente concluída.
```

## Fechamento

Hoje você descobriu que:

- **História de usuário** descreve uma necessidade no formato **Como / Quero / Para que** — foco na pessoa, não na tecnologia.
- O **"para que"** mantém o time focado em **valor**.
- **Critérios de aceitação** definem quando a história está pronta, de forma verificável.
- No **Sprint Planning**, o time escolhe e estima as histórias do topo do backlog para a sprint.

**Próxima aula:** já temos as histórias. Mas quanto esforço cada uma dá? E como o time decide isso junto, sem brigar? Vamos fechar a trilha com **estimativa e Planning Poker**.

:::roteiro
Abrir com o contraste das duas frases (jargão técnico vs história de usuário) — o impacto é imediato. A fórmula Como/Quero/Para que é o miolo; insista no "para que", que é sempre o esquecido. O erro "história técnica" é fundamental: usuário não quer banco de dados, quer resolver problema. Critérios de aceitação podem ser novos pra eles — use o exemplo dos favoritos. Na prática, a troca entre duplas (auditar a história da outra) é a parte que mais ensina. Conecte com Linguagens e com levantamento de requisitos. Alura ("História de Usuário" / "Sprint planning") opcional. 8 min pro quiz.
:::
