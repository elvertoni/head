---
titulo: Priorização do Backlog
tema: Metodologias Ágeis
disciplina: analise-e-metodos-para-sistemas
serie: 1ª
prerequisitos: [Elaboração dos Épicos]
objetivos:
  - Explicar por que priorizar o backlog é essencial no Scrum
  - Aplicar o método MoSCoW para classificar itens por importância
  - Reconhecer que a priorização é feita por valor e urgência, e é contínua
trilha: metodologias-ageis
ordem: 37
slug: priorizacao-do-backlog
modo_origem: seed
fontes:
  - lake/analise-e-metodos-para-sistemas/AULA 37_ANÁLISE E MÉTODO PARA SISTEMAS.pptx
revisao: true
status: aprovada
versao: 2
atualizado_em: 2026-06-21
---

Imagina que faltam três dias para a prova de todas as matérias e você não tem como estudar tudo. O que você faz? Estuda primeiro o que **vale mais nota** e o que você **domina menos**. Isso é priorizar — e é exatamente o que um time Scrum faz com o backlog. Por mais que a lista de funcionalidades seja enorme, o tempo é curto e a equipe é pequena. Não dá para fazer tudo de uma vez, então alguém precisa decidir: o que vem **primeiro**? Hoje você aprende a responder essa pergunta com método.

## Objetivos

Ao final desta aula, você será capaz de:

- Explicar **por que** priorizar o backlog é essencial no Scrum.
- Aplicar o método **MoSCoW** para classificar itens por importância.
- Reconhecer que a priorização é feita por **valor e urgência**, e é **contínua**.

## Pré-requisitos

Ter visto a **Aula 36** (épicos e organização do backlog).

## Desenvolvimento

### Em uma frase

:::importante
Priorizar é escolher o que entra primeiro para entregar mais valor com menos tempo desperdiçado.
:::

### Por que priorizar

:::conceito Priorização do backlog
É o processo de **ordenar** os itens do backlog para que o time trabalhe primeiro no que tem **maior valor e urgência**. Quem lidera é o **Product Owner**, junto com o time e os interessados. O objetivo: entregar o que mais importa **antes**, maximizando o retorno do esforço.

:::

Sem priorização, o time corre o risco de gastar a primeira sprint num detalhe bonitinho enquanto o essencial — aquilo sem o qual o produto nem funciona — fica para depois.

:::atencao Erro comum
Priorizar pelo que é **mais fácil ou mais divertido** de fazer, em vez do que tem mais valor. É tentador começar pela funcionalidade legal e deixar a chata (mas essencial) para o fim. Resultado: o produto fica cheio de enfeites e sem o básico. Priorize por **valor para o usuário**, não por conforto do time.

:::

### O método MoSCoW

Uma das formas mais usadas de priorizar é o **MoSCoW**. O nome é um truque de memória com quatro categorias:

```diagrama-progressivo
titulo: As quatro caixas do MoSCoW
camadas:
  - rotulo: M — Must have (precisa ter)
    conteudo: Sem isso o produto não funciona. É inegociável. Ex.: no app da cantina, "fazer um pedido".
  - rotulo: S — Should have (deveria ter)
    conteudo: Importante, agrega muito valor, mas o produto sobrevive sem por um tempo. Ex.: "ver histórico de pedidos".
  - rotulo: C — Could have (poderia ter)
    conteudo: Bom se der tempo, mas não faz falta agora. Ex.: "tema escuro no app".
  - rotulo: W — Won't have (não terá agora)
    conteudo: Fica de fora desta entrega. Pode entrar no futuro. Ex.: "programa de pontos e recompensas".
```

A beleza do MoSCoW é forçar escolhas: nem tudo pode ser "Must". Se tudo é prioridade, nada é prioridade.

### Priorizar é para sempre

:::importante A lista nunca fica pronta
A priorização **não** acontece uma vez só no início. Ela é **contínua e iterativa**: a cada sprint o time revê o backlog, porque surgem novos itens, o mercado muda e o que era urgente deixa de ser. O backlog é um documento **vivo**, reordenado o tempo todo pelo PO.

:::

:::dica A habilidade que vale para a vida
Saber priorizar — separar o essencial do desejável sob tempo limitado — é uma das competências mais úteis que existem, dentro e fora da TI. Você usa no estudo para a prova, na organização do dia e vai usar todo dia como profissional. O MoSCoW é só uma ferramenta para treinar esse músculo.

:::

## Prática

**Atividade "MoSCoW na prática" (em duplas, sem computador, ~15 min).** O time tem tempo para entregar só uma parte do **app da cantina** na primeira versão. Classifiquem cada item abaixo em **M, S, C ou W**:

> ver o cardápio do dia · fazer um pedido · pagar com Pix · tema escuro · avaliar a comida com estrelas · receber notificação quando o pedido ficar pronto · programa de fidelidade · login

1. Distribuam os 8 itens nas quatro caixas. **Regra:** no máximo 3 itens podem ser "Must".
2. Defendam: por que cada "Must" é realmente inegociável?
3. Qual item gerou mais discordância na dupla? Por quê?

Cada dupla apresenta seus "Must". A turma compara — todo mundo elegeu os mesmos essenciais?

## Avaliação

```quiz
- pergunta: Quem lidera a priorização do backlog no Scrum?
  alternativas:
    - texto: O Scrum Master
    - texto: O Product Owner, junto com o time e os interessados
      correta: true
    - texto: Apenas a equipe de desenvolvimento
    - texto: O cliente sozinho
  feedback: >
    O PO é o dono do backlog e lidera a priorização, sempre colaborando com o time
    e os stakeholders para decidir o que tem mais valor.
- pergunta: No MoSCoW, o que significa a categoria "Must have"?
  alternativas:
    - texto: O que seria bom ter se sobrar tempo
    - texto: O que é inegociável — sem isso o produto não funciona
      correta: true
    - texto: O que nunca será feito
    - texto: O que é mais fácil de programar
  feedback: >
    "Must" é o essencial, inegociável. Se tudo virar "Must", a priorização perde o
    sentido — por isso é preciso ser rigoroso.
- pergunta: Com que frequência o backlog deve ser priorizado?
  alternativas:
    - texto: Uma única vez, no início do projeto
    - texto: Continuamente, pois é um documento vivo que muda a cada sprint
      correta: true
    - texto: Nunca, ele se organiza sozinho
    - texto: Só quando o projeto termina
  feedback: >
    Priorização é contínua. Novos itens surgem e prioridades mudam — o PO reordena o
    backlog o tempo todo.
```

## Fechamento

Hoje você descobriu que:

- **Priorizar o backlog** é ordenar os itens por **valor e urgência**, liderado pelo **Product Owner**.
- O **MoSCoW** classifica em **Must, Should, Could e Won't** — e força escolhas reais.
- Priorizar pelo fácil em vez do valioso é uma armadilha comum.
- O backlog é **vivo**: a priorização é contínua, sprint após sprint.

**Próxima aula:** sabendo o que fazer primeiro, o time precisa combinar **quando** entregar cada parte. Vamos ao **planejamento de releases**.

:::roteiro
Abrir com a analogia da semana de provas — priorizar o que vale mais nota. O erro "priorizar pelo fácil" é universal entre adolescentes; use isso. O diagrama MoSCoW é o centro: a regra "no máximo 3 Must" na prática é o que ensina de verdade, porque os obriga a abrir mão. A discordância dentro da dupla é o ponto alto — peça que defendam. Reforce que o backlog é vivo (conecta com a próxima aula). Alura ("Priorização do backlog") opcional. 8 min pro quiz.
:::
