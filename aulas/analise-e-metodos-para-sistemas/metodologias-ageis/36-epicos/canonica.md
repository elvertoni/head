---
titulo: Elaboração dos Épicos
tema: Metodologias Ágeis
disciplina: analise-e-metodos-para-sistemas
serie: 1ª
prerequisitos: [Cerimônias e Artefatos do Scrum]
objetivos:
  - Explicar o que é um épico no Scrum
  - Agrupar funcionalidades relacionadas em temas para organizar o backlog
  - Decompor um épico em itens menores e registrá-lo de forma clara
trilha: metodologias-ageis
ordem: 36
slug: epicos
modo_origem: seed
fontes:
  - lake/analise-e-metodos-para-sistemas/AULA 36_ANÁLISE E MÉTODO PARA SISTEMAS.pptx
revisao: true
status: aprovada
versao: 1
atualizado_em: 2026-06-15
---

Pensa numa lista de compras com 80 itens jogados em qualquer ordem: arroz, sabão, maçã, detergente, frango, shampoo... Você anda o mercado inteiro, ziguezagueando, e ainda esquece coisa. Agora pensa na mesma lista **agrupada** por seção: hortifrúti, limpeza, açougue. Tudo fica fácil. Um Product Backlog de software tem o mesmo problema: dezenas de funcionalidades soltas viram caos. A solução é a mesma do mercado — **agrupar por tema**. No Scrum, esses grandes grupos têm um nome: épicos.

## Objetivos

Ao final desta aula, você será capaz de:

- Explicar o que é um **épico** no Scrum.
- **Agrupar** funcionalidades relacionadas em temas para organizar o backlog.
- **Decompor** um épico em itens menores e registrá-lo de forma clara.

## Pré-requisitos

Ter visto a **Aula 35** (artefatos do Scrum, em especial o Product Backlog).

## Desenvolvimento

### O que é um épico

:::conceito Épico
É uma **unidade de trabalho de alto nível** que junta um conjunto de requisitos relacionados, normalmente ligados a uma **funcionalidade ampla** ou um **tema** comum. O épico não é detalhado: ele dá a visão geral de uma grande parte do produto e depois é **quebrado** em itens menores.

:::

Voltando ao app da cantina: "Pagamento" é um épico — dentro dele cabem várias funcionalidades (pagar por Pix, por cartão, ver histórico de pagamentos). "Cardápio" é outro épico. Cada um agrupa um monte de coisa relacionada.

:::atencao Erro comum
Confundir épico com "uma tarefa grande qualquer". Épico não é só algo trabalhoso — é um **tema que reúne funcionalidades relacionadas**. "Arrumar um bug no botão" é tarefa, não épico. "Sistema de Pagamento" é épico, porque engloba várias funcionalidades sob o mesmo guarda-chuva.

:::

### De épico a item pequeno

O épico é só o começo. Depois de identificá-lo, o time o **decompõe** em pedaços cada vez menores e mais gerenciáveis:

```diagrama-progressivo
titulo: Quebrando um épico
camadas:
  - rotulo: 1. Épico (tema amplo)
    conteudo: "Pagamento no app da cantina." Grande demais para fazer de uma vez.
  - rotulo: 2. Itens menores (histórias)
    conteudo: Quebra-se em partes: "pagar com Pix", "pagar com cartão", "ver histórico de pagamentos". Cada uma cabe melhor numa sprint.
  - rotulo: 3. Tarefas
    conteudo: Cada item ainda pode virar tarefas técnicas concretas, que a equipe executa no dia a dia.
```

Esse processo é **iterativo**: à medida que o projeto anda, novos épicos surgem e outros são refinados. Não se faz tudo de uma vez no começo.

### Registrar com clareza

Aqui entra um gancho com **Linguagens** (a parte de Formação Geral do seu curso): elaborar épicos é, no fundo, **organizar informação por escrito**. Bons épicos têm títulos objetivos, agrupam itens semelhantes e ficam registrados em listas claras — qualquer colega do time entende sem precisar perguntar.

:::dica Organização é habilidade profissional
Saber pegar uma bagunça de ideias e agrupá-las em temas claros é uma das competências mais valorizadas em qualquer profissão — não só em TI. Quando você organiza um backlog em épicos, está treinando exatamente isso: transformar caos em estrutura comunicável.

:::

## Prática

**Atividade "caça aos épicos" (em duplas, sem computador, ~15 min).** Aqui está um monte de funcionalidades soltas de um **app de streaming de músicas**:

> criar playlist · login com senha · buscar música · pagar assinatura · seguir artista · recuperar senha · baixar música offline · ver letra · cadastrar cartão · compartilhar playlist · login com Google · recomendações

No caderno:

1. **Agrupem** essas funcionalidades em **3 ou 4 épicos** (temas amplos). Deem um título objetivo a cada épico.
2. Sobrou alguma funcionalidade difícil de encaixar? Discutam onde ela cabe melhor.
3. Escolham **um** épico e quebrem-no em itens menores (como no diagrama).

Cada dupla apresenta seus épicos. A turma compara: os agrupamentos bateram? Onde divergiram, qual fazia mais sentido?

## Avaliação

```quiz
- pergunta: O que é um épico no Scrum?
  alternativas:
    - texto: Qualquer tarefa que dá muito trabalho
    - texto: Uma unidade de alto nível que agrupa funcionalidades relacionadas de um tema
      correta: true
    - texto: O nome da reunião diária
    - texto: Um bug que precisa ser corrigido
  feedback: >
    Épico é tema amplo que reúne requisitos relacionados — não é só "algo grande".
    Ele depois é quebrado em itens menores.
- pergunta: Qual a ordem correta do mais amplo ao mais específico?
  alternativas:
    - texto: Tarefa → história → épico
    - texto: Épico → história (item menor) → tarefa
      correta: true
    - texto: História → épico → tarefa
    - texto: Tudo é a mesma coisa
  feedback: >
    Começa amplo (épico), quebra em itens menores (histórias) e estes em tarefas
    concretas — do guarda-chuva ao detalhe.
- pergunta: Por que agrupar funcionalidades em épicos ajuda o projeto?
  alternativas:
    - texto: Porque deixa o backlog organizado e dá visão clara das grandes partes
      correta: true
    - texto: Porque elimina a necessidade de planejar
    - texto: Porque substitui o Product Owner
    - texto: Porque torna o trabalho mais lento de propósito
  feedback: >
    Como agrupar a lista de compras por seção: o épico organiza o caos e dá uma
    visão geral que facilita priorizar e dividir o trabalho.
```

## Fechamento

Hoje você descobriu que:

- **Épico** é uma unidade de alto nível que **agrupa funcionalidades relacionadas** de um tema.
- Épico **não** é "tarefa grande qualquer" — é um guarda-chuva temático.
- O épico é **decomposto** em itens menores (histórias) e depois em tarefas.
- Elaborar épicos é organizar informação com clareza — uma habilidade que vale em qualquer área.

**Próxima aula:** com o backlog organizado em épicos, surge a pergunta inevitável: por onde começar? Vamos aprender a **priorizar o backlog**.

:::roteiro
Abrir com a lista de compras bagunçada vs agrupada — analogia que gruda na hora. O erro "épico = tarefa grande" é o ponto a martelar: contraste "arrumar um bug" (tarefa) com "Sistema de Pagamento" (épico). O diagrama de decomposição mostra que épico é só o topo. Na prática do app de streaming, a graça é a divergência nos agrupamentos — "recomendações" e "seguir artista" geram bom debate sobre onde encaixam. Conecte de leve com Linguagens (organizar/escrever com clareza). Alura ("Persona épico" / "Técnicas para elaborar") opcional. 8 min pro quiz.
:::
