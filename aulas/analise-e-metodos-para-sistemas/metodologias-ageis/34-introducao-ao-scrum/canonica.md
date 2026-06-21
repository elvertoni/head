---
titulo: Introdução ao Scrum
tema: Metodologias Ágeis
disciplina: analise-e-metodos-para-sistemas
serie: 1ª
prerequisitos: [Fundamentos da Agilidade]
objetivos:
  - Explicar o que é o Scrum e o que é uma sprint
  - Identificar os três papéis do Scrum e a responsabilidade de cada um
  - Reconhecer o Product Backlog como a lista que guia o trabalho
trilha: metodologias-ageis
ordem: 34
slug: introducao-ao-scrum
modo_origem: seed
fontes:
  - lake/analise-e-metodos-para-sistemas/AULA 34_ANÁLISE E MÉTODO PARA SISTEMAS.pptx
revisao: true
status: aprovada
versao: 1
atualizado_em: 2026-06-15
---

Você já participou de um trabalho em grupo onde "todo mundo fazia tudo" e, no fim, ninguém tinha feito nada direito? Sem papéis claros, o time anda em círculos. O Scrum nasceu pra resolver exatamente isso no desenvolvimento de software: dar a cada pessoa um papel, dividir o trabalho em ciclos curtos e manter todo mundo apontando para o mesmo lugar. Na aula passada você viu o que é ser ágil; agora vai conhecer a ferramenta ágil mais usada do planeta — e como ela organiza um time de verdade.

## Objetivos

Ao final desta aula, você será capaz de:

- Explicar o que é o **Scrum** e o que é uma **sprint**.
- Identificar os **três papéis** do Scrum e a responsabilidade de cada um.
- Reconhecer o **Product Backlog** como a lista que guia todo o trabalho.

## Pré-requisitos

Ter visto a **Aula 33** (o que é agilidade e a ideia de entregar valor).

## Desenvolvimento

### O que é Scrum

:::conceito Scrum
É um **framework ágil** para desenvolver produtos de forma **iterativa e incremental** — ou seja, em ciclos que se repetem, entregando um pedaço pronto de cada vez. O time trabalha em **sprints**, ciclos curtos (geralmente de 2 a 4 semanas) ao fim dos quais sempre existe algo funcionando para mostrar.

:::

Em vez de sumir por seis meses e reaparecer com o produto inteiro (que pode estar errado), o time Scrum entrega de pedacinho em pedacinho e corrige o rumo a cada sprint.

### Os três papéis

Num time Scrum, cada pessoa tem um papel com responsabilidade definida. São três:

| Papel | Responsabilidade | Em uma frase |
|---|---|---|
| **Product Owner (PO)** | maximizar o valor do produto; cuida e prioriza o Product Backlog | decide **o que** fazer e em que ordem |
| **Scrum Master (SM)** | garantir que o time siga o Scrum; remove obstáculos | facilita e **protege** o time |
| **Equipe de Desenvolvimento** | construir e entregar o incremento a cada sprint | faz **acontecer** |

:::atencao Erro comum
Achar que o **Scrum Master é o chefe** do time. Não é. Ele não manda nas pessoas nem distribui ordens — ele é um **facilitador**: tira pedras do caminho, organiza as reuniões e protege o time de interrupções. Quem decide o que entra no produto é o PO; quem decide **como** fazer é a própria equipe.

:::

### O Product Backlog

:::conceito Product Backlog
É a **lista ordenada** de tudo que o produto precisa: funcionalidades, melhorias e correções. Fica sob responsabilidade do **Product Owner**, que a mantém **priorizada** — o mais importante no topo. É dessa lista que o time puxa o trabalho de cada sprint.

:::

:::dica Como times reais se organizam
Esses papéis não são invenção de escola: abra qualquer vaga de "desenvolvedor júnior" e você vai ver "trabalhar em time ágil com PO e Scrum Master". Entender quem faz o quê agora é entender como será seu **primeiro emprego** numa equipe de software.

:::

## Prática

**Atividade "montando o time" (em grupos de 3-4, sem computador, ~15 min).** A turma vai criar o **app da cantina da escola** (ver cardápio, fazer pedido, pagar). Cada grupo:

1. **Distribui os papéis** — quem é PO, quem é SM, quem é Dev? (pode ter mais de um Dev)
2. **PO em ação** — escrevam **5 itens** que entrariam no Product Backlog desse app.
3. **Priorizem** — qual desses 5 é o mais importante para um primeiro pedaço funcionando?
4. **SM em ação** — citem **um obstáculo** que poderia travar o time e o que o Scrum Master faria.

Cada grupo apresenta seu backlog priorizado. A turma compara o "item nº 1" de cada um.

## Avaliação

```quiz
- pergunta: O que é uma sprint no Scrum?
  alternativas:
    - texto: A reunião final do projeto
    - texto: Um ciclo curto (2 a 4 semanas) ao fim do qual há algo pronto para mostrar
      correta: true
    - texto: O nome do chefe do time
    - texto: Um documento com todos os requisitos
  feedback: >
    Sprint é o ciclo de trabalho do Scrum. A cada sprint o time entrega um incremento
    funcionando — desenvolvimento iterativo e incremental.
- pergunta: Qual a função do Scrum Master?
  alternativas:
    - texto: Mandar nas pessoas e distribuir ordens
    - texto: Facilitar o processo e remover obstáculos do time
      correta: true
    - texto: Decidir sozinho o que o produto terá
    - texto: Substituir o Product Owner
  feedback: >
    O SM é facilitador, não chefe. Ele protege o time e tira pedras do caminho; quem
    prioriza o produto é o PO.
- pergunta: Quem cuida e prioriza o Product Backlog?
  alternativas:
    - texto: O Scrum Master
    - texto: O Product Owner
      correta: true
    - texto: Qualquer pessoa da empresa
    - texto: Ninguém, ele se organiza sozinho
  feedback: >
    O Product Backlog é responsabilidade do Product Owner, que o mantém ordenado por
    valor — o mais importante no topo.
```

## Fechamento

Hoje você descobriu que:

- **Scrum** é um framework ágil que entrega o produto em **sprints** — ciclos curtos e repetidos.
- O time tem **três papéis**: **PO** (decide o quê e a ordem), **SM** (facilita e protege), **Equipe** (constrói).
- O **Product Backlog** é a lista priorizada que guia o trabalho, cuidada pelo PO.
- O Scrum Master **não é chefe** — é facilitador.

**Próxima aula:** o time está montado e tem a lista. Mas como ele se organiza no dia a dia para não se perder? Vamos às **cerimônias e artefatos** do Scrum.

:::roteiro
Abrir com a dor do trabalho em grupo "todo mundo faz tudo". A tabela dos papéis é o miolo — use perguntas ("quem decide se o app terá pagamento por Pix? quem tira o time do bloqueio?") pra eles deduzirem PO vs SM. O erro "SM = chefe" é o mais comum e vale insistir. Na prática do app da cantina, circule garantindo que o backlog tenha itens de VALOR (ver cardápio) e não só técnicos. Se sobrar tempo, peça que um grupo encene 30s de "o SM removendo um obstáculo". Alura ("Iniciação do projeto") opcional. 8 min pro quiz.
:::
