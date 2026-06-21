---
titulo: Tipos de Aprendizado de Máquina
tema: Fundamentos de IA
disciplina: inteligencia-artificial
serie: Extra
prerequisitos: [Como a Máquina Aprende]
objetivos:
  - Diferenciar aprendizado supervisionado, não-supervisionado e por reforço
  - Reconhecer o papel dos dados rotulados em cada tipo
  - Classificar um problema no tipo de aprendizado adequado
trilha: fundamentos-de-ia
ordem: 5
slug: tipos-de-aprendizado-de-maquina
modo_origem: tema
fontes: []
revisao: false
status: aprovada
versao: 1
atualizado_em: 2026-06-15
---

Pensa em três jeitos diferentes de aprender uma coisa nova. No primeiro, você estuda com o **gabarito** ao lado: vê a pergunta, vê a resposta certa, e treina até acertar. No segundo, ninguém te dá resposta nenhuma — você recebe um monte de coisas bagunçadas e tem que **descobrir os grupos** sozinho, tipo arrumar a estante por conta própria. No terceiro, você aprende **tentando e errando**, ganhando um "parabéns" quando acerta — como passar de fase num videogame. A máquina aprende exatamente por esses três caminhos, e cada um serve para um tipo de problema. Hoje você conhece os três.

## Objetivos

Ao final desta aula, você será capaz de:

- **Diferenciar** aprendizado supervisionado, não-supervisionado e por reforço.
- Reconhecer o papel dos **dados rotulados** em cada tipo.
- **Classificar** um problema no tipo de aprendizado adequado.

## Pré-requisitos

Ter visto a **Aula 04** (treino, inferência e a ideia de aprender por exemplos).

## Desenvolvimento

### Três caminhos para aprender

O [[aprendizado-de-maquina]] não é uma coisa só. Há três grandes famílias, e a diferença está em **que tipo de dado** a máquina recebe.

```diagrama-progressivo
titulo: Os três tipos de aprendizado de máquina
camadas:
  - rotulo: 1. Supervisionado (com gabarito)
    conteudo: A máquina recebe exemplos JÁ ROTULADOS - esta foto é "gato", esta é "cachorro". Ela aprende a relação entre a entrada e a resposta certa. É o tipo mais comum.
  - rotulo: 2. Não-supervisionado (sem gabarito)
    conteudo: A máquina recebe dados SEM rótulo e tem que achar padrões e grupos sozinha. Ninguém disse o que é o quê - ela organiza por semelhança.
  - rotulo: 3. Por reforço (tentativa e recompensa)
    conteudo: A máquina aprende AGINDO num ambiente e recebendo recompensa ou punição. Acertou, ganha pontos; errou, perde. É assim que IAs aprendem a jogar videogame ou um robô a andar.
```

:::conceito Os três tipos
**[[aprendizado-supervisionado|Supervisionado]]:** aprende de exemplos rotulados (entrada + resposta certa). **[[aprendizado-nao-supervisionado|Não-supervisionado]]:** acha padrões em dados sem rótulo. **[[aprendizado-por-reforco|Por reforço]]:** aprende por tentativa e erro, guiado por recompensas. A escolha depende do problema e de **quais dados** você tem.

:::

:::atencao Erro comum
Achar que toda IA precisa de dados rotulados. Só o **supervisionado** precisa. O não-supervisionado trabalha justamente quando **não há rótulos** — ele descobre a estrutura escondida nos dados. Confundir isso leva a pensar "sem rótulo não dá pra fazer IA", o que é falso.

:::

### Por que isso importa na prática

:::dica O custo escondido do supervisionado
A maior parte da IA comercial hoje é **supervisionada** — e isso tem um preço: alguém precisa **rotular** milhares de exemplos ("isto é spam", "isto é fraude"). Esse trabalho de rotulagem é caro e demorado, e é por isso que dados rotulados de qualidade valem ouro. Quando uma empresa tem dados bem rotulados que ninguém mais tem, ela tem uma vantagem enorme. Entender isso te mostra por que "dados" viraram o novo petróleo.

:::

## Prática

**Atividade "que tipo de aprendizado?" (em duplas, sem computador, ~15 min).** Para cada problema, decidam o tipo (**supervisionado**, **não-supervisionado** ou **por reforço**) e justifiquem:

1. Prever a **nota** de um aluno na prova a partir das horas que ele estudou.
2. Agrupar os clientes de uma loja em **perfis parecidos**, sem categorias pré-definidas.
3. Ensinar um **robô a andar** sem cair, deixando ele tentar e dando pontos quando avança.
4. Identificar se um e-mail é **spam ou não**, a partir de milhares de e-mails já marcados.
5. Descobrir **temas escondidos** num monte de comentários, sem saber quais temas existem.

Cada dupla apresenta a classificação de um item. A turma confere: o tipo bate? Qual foi o mais difícil de decidir?

## Avaliação

```quiz
- pergunta: O que caracteriza o aprendizado supervisionado?
  alternativas:
    - texto: A máquina age e recebe recompensas
    - texto: A máquina aprende de exemplos já rotulados (com a resposta certa)
      correta: true
    - texto: A máquina acha grupos sem nenhum rótulo
    - texto: A máquina não usa dados
  feedback: >
    Supervisionado = aprender com gabarito. Os exemplos vêm com a resposta certa, e a
    máquina aprende a relação entre entrada e resposta.
- pergunta: Qual tipo de aprendizado é usado quando NÃO há rótulos e a máquina precisa achar grupos sozinha?
  alternativas:
    - texto: Supervisionado
    - texto: Não-supervisionado
      correta: true
    - texto: Por reforço
    - texto: Nenhum, é impossível sem rótulos
  feedback: >
    Sem rótulos, entra o não-supervisionado: a máquina descobre padrões e grupos pela
    semelhança dos dados, sem ninguém dizer o que é o quê.
- pergunta: Ensinar uma IA a jogar videogame, ganhando pontos quando avança, é exemplo de qual tipo?
  alternativas:
    - texto: Aprendizado por reforço
      correta: true
    - texto: Aprendizado supervisionado
    - texto: Aprendizado não-supervisionado
    - texto: Não é aprendizado de máquina
  feedback: >
    Por reforço: a máquina age, recebe recompensa (pontos) ou punição, e aprende por
    tentativa e erro qual estratégia rende mais.
```

## Fechamento

Hoje você descobriu que:

- O [[aprendizado-de-maquina]] tem **três tipos**: [[aprendizado-supervisionado|supervisionado]] (com gabarito), [[aprendizado-nao-supervisionado|não-supervisionado]] (sem gabarito) e [[aprendizado-por-reforco|por reforço]] (tentativa e recompensa).
- Só o **supervisionado** exige dados rotulados; o não-supervisionado acha padrões sem rótulo.
- A escolha depende do **problema** e de **quais dados** você tem.
- Rotular dados é caro — por isso bons dados rotulados valem ouro.

**Próxima aula:** vamos mergulhar no tipo mais usado, o supervisionado, e ver suas duas tarefas clássicas: **classificação** ("qual categoria?") e **regressão** ("quanto?").

:::roteiro
Abrir com os três jeitos de aprender (gabarito / arrumar estante sozinho / videogame) — analogias que todos têm. O diagrama dos três tipos é o esqueleto. O erro "toda IA precisa de rótulo" é o alvo: enfatize que o não-supervisionado existe justamente sem rótulo. A prática de classificar problemas é o coração — o item 5 (temas escondidos) costuma confundir com supervisionado, ótimo pra debater. A `:::dica` da rotulagem ("dados são o novo petróleo") conecta com carreira. Conteúdo estável, sem web. 8 min pro quiz.
:::
