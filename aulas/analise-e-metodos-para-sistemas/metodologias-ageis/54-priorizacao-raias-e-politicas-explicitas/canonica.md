---
titulo: "Priorização no quadro: raias e políticas explícitas"
tema: Metodologias Ágeis
disciplina: analise-e-metodos-para-sistemas
serie: 1ª
prerequisitos: ["Kanban: o quadro e o fluxo"]
objetivos:
  - Diferenciar tarefa importante de tarefa urgente e reconhecer a armadilha de tratar tudo como urgente
  - Explicar o que são raias e como elas categorizam o trabalho no quadro
  - Relacionar a raia à classe de serviço — a regra de atendimento de cada tipo de trabalho
  - Escrever políticas explícitas para o quadro de um time
trilha: metodologias-ageis
ordem: 54
slug: priorizacao-raias-e-politicas-explicitas
modo_origem: seed
fontes:
  - lake/analise-e-metodos-para-sistemas/AULA 55_ANÁLISE E MÉTODO PARA SISTEMAS.pptx.pdf
revisao: true
status: aprovada
versao: 1
atualizado_em: 2026-08-13
---

Seu celular vibrou agora. Você vai olhar — quase todo mundo olha. E o trabalho de história que vale nota, com prazo daqui a duas semanas, **não vibra**. Nunca vibrou, nunca vai vibrar. Essa é a assimetria mais cara da vida adulta e da vida profissional: o urgente grita, o importante fica quieto — e quem decide na hora, no impulso, acaba passando o ano inteiro apagando incêndio sem nunca construir nada. Times de software caem nisso todo santo dia. A aula de hoje é sobre a defesa que o Kanban inventou: decidir **antes**, e deixar escrito no quadro.

## Objetivos

Ao final desta aula, você será capaz de:

- Diferenciar tarefa **importante** de tarefa **urgente** — e reconhecer a armadilha de chamar tudo de urgente.
- Explicar o que são **raias** e como elas categorizam o trabalho no quadro.
- Relacionar a raia à **classe de serviço**: a regra de atendimento de cada tipo de trabalho.
- Escrever **políticas explícitas** para o quadro de um time.

## Pré-requisitos

Ter visto a **Aula 53**: quadro, cartão, sistema puxado, limite de WIP e gargalo.

## Desenvolvimento

### Em uma frase

:::importante
O quadro mostra o que está acontecendo, mas não decide o que puxar agora. Quem decide é a **política combinada antes** — não a pessoa que gritar mais alto no momento.
:::

### Importante não é urgente

São duas perguntas diferentes, e confundir as duas é o erro que estraga o trabalho de time inteiro.

- **Importante** responde: *isso muda o resultado?* É a tarefa que aproxima o time do objetivo. Ela quase nunca tem prazo colado — e é justamente por isso que fica pra depois pra sempre.
- **Urgente** responde: *isso precisa ser agora?* É a tarefa que cobra atenção imediata, tenha ela impacto grande ou não.

Cruzando as duas perguntas, todo trabalho cai em um de quatro lugares:

| | **Urgente** | **Não urgente** |
|---|---|---|
| **Importante** | O login do app parou e nenhum usuário entra. Faça **agora**. | Melhorar o código que está bagunçado; escrever os testes. **Agende** — se não agendar, nunca acontece. |
| **Não importante** | Alguém pediu no chat "pra ontem" um relatório que ninguém vai ler. **Questione**. | Trocar a cor de um botão que ninguém reclamou. **Descarte** ou deixe no fim da fila. |

:::atencao O erro que se vê no quadro
O time começa a marcar **tudo** como urgente. Chega a um ponto em que existem seis cartões de urgência no quadro ao mesmo tempo — e aí urgência deixou de significar qualquer coisa, porque se tudo passa na frente, nada passa na frente. Sintoma clássico: o time vive ocupado, apagando incêndio, e o trabalho que realmente importava não andou um centímetro em três semanas. Esse é o quadrante de baixo-esquerda comendo o de cima-direita.

:::

:::importante Corrigindo uma confusão comum
"Importante × urgente" **não é um conceito do Kanban** — é a matriz de Eisenhower, uma ferramenta de decisão pessoal bem mais antiga. Ela ajuda a *pensar*, mas não organiza um time sozinha: não adianta cada pessoa classificar de cabeça, porque cada uma classifica diferente. O mecanismo que o Kanban realmente oferece para isso é a **raia** com uma **classe de serviço** — a mesma ideia, só que escrita no quadro e valendo para todo mundo. É disso que trata o resto da aula.

:::

### Raias: o quadro ganha faixas

:::conceito Raia (swimlane)
É uma **divisão horizontal** do quadro. As colunas continuam sendo as etapas do fluxo (vertical, da esquerda pra direita); a raia corta o quadro no outro sentido e separa **tipos de trabalho** que atravessam essas mesmas etapas. Um cartão anda pelas colunas **dentro** da sua raia.

:::

O critério da raia é escolha do time — pode ser por tipo de trabalho, por produto, por equipe responsável. Mas o uso mais valioso, e o que resolve o problema desta aula, é separar por **urgência**:

- **Raia de urgência** (bem no topo, estreita): o que interrompe. Bug que derrubou o sistema, problema que trava o cliente.
- **Raia padrão** (o corpo do quadro): o trabalho planejado, que anda na ordem da fila.

:::conceito Classe de serviço
É a **regra de atendimento** que a raia carrega. Não basta desenhar a faixa: ela precisa vir com o combinado — quantos cartões cabem ali, quem pode colocar um cartão nela, e o que o time faz quando ela recebe trabalho. Sem essa regra, a raia é só uma linha bonita no quadro.

:::

```diagrama-progressivo
titulo: Chega um cartão urgente no meio da tarde
camadas:
  - rotulo: O chamado entra
    conteudo: O login do aplicativo parou. Ninguém consegue entrar. Alguém precisa decidir o que acontece com o trabalho que já estava em andamento.
  - rotulo: A raia responde por si
    conteudo: O cartão vai para a raia de urgência, que tem limite 1. Se já houver um cartão lá, este espera — e o time descobre na hora que tem duas emergências, o que por si só é uma informação importante.
  - rotulo: A regra já estava escrita
    conteudo: A classe de serviço da raia diz o que fazer. Por exemplo, quem estiver na etapa de desenvolver pausa o cartão atual e assume a urgência.
  - rotulo: Ninguém discutiu no calor do momento
    conteudo: Essa é a sacada inteira. A decisão difícil foi tomada semanas antes, com a cabeça fria, e não às três da tarde com o cliente ligando. O quadro só executou o combinado.
```

### Políticas explícitas: as regras que ninguém precisa perguntar

Todo time tem regras. A diferença é que na maioria dos times elas moram na cabeça das pessoas mais antigas — e quem chega novo descobre no tropeço.

:::conceito Políticas explícitas
São as regras do quadro **escritas e visíveis para todos**, geralmente no próprio quadro. Respondem coisas como: o que precisa estar pronto para um cartão passar desta coluna para a próxima, qual o limite de WIP de cada coluna, quem pode puxar o quê, e o que fazer quando um cartão trava.

:::

Um exemplo de conjunto pequeno e suficiente, escrito na lateral do quadro de um time:

```text
1. Um cartão só sai de "Desenvolver" com outra pessoa tendo lido o código.
2. Limite de "Testar": 2 cartões. Cheio, ninguém puxa nada novo.
3. Cartão travado há mais de 1 dia ganha um adesivo vermelho e vira assunto
   da conversa de amanhã cedo.
4. Só o Product Owner coloca cartão na raia de urgência.
```

Repare no que a regra 4 faz: ela tira a decisão de urgência das mãos de quem está com pressa. É pouca coisa escrita e resolve a briga inteira que a `:::atencao` lá de cima descreveu.

:::importante Onde o Kanban difere do Scrum
Você conheceu o Scrum nas aulas 34 a 41. Os dois são ágeis e convivem bem, mas resolvem o ritmo de formas diferentes:

| | **Scrum** | **Kanban** |
|---|---|---|
| Ritmo | sprints de duração fixa | fluxo contínuo, sem sprint |
| Papéis | definidos (PO, Scrum Master, time) | não exige papéis próprios |
| Como entra trabalho | escolhido no planejamento da sprint | puxado quando abre capacidade |
| O que segura o processo | as cerimônias | o limite de WIP e as políticas explícitas |

Não existe o melhor dos dois: existe o que serve ao trabalho do time. Time com demanda imprevisível — suporte, manutenção — sofre com sprint e prospera com Kanban.

:::

:::dica Onde você vai encontrar isso
Em Trello, Jira e no Projects do GitHub, raia se chama *swimlane* e está lá, esperando ser usada — a maioria dos times nunca liga. E política explícita não precisa de ferramenta: é o arquivo `README` do repositório, a descrição fixada no topo do canal do time, o combinado escrito no card. Em entrevista de estágio, contar que o seu time de trabalho escolar tinha regra escrita para o que fazer quando alguém atrasava vale mais do que listar dez ferramentas.

:::

## Prática

**Atividade "o quadro do plantão" (grupos de 4, sem computador, ~15 min).** Cada grupo administra o quadro de um time que mantém o aplicativo da escola.

1. **Montem o quadro** numa folha: colunas `A fazer · Fazendo · Feito` e **duas raias** horizontais — `Urgente` em cima e `Normal` embaixo.
2. **Distribuam estes 6 cartões** (escrevam cada um num papelzinho) na raia certa, e justifiquem cada escolha em uma frase:
   - o app não abre para ninguém desde as 8h
   - a tela de notas está com uma cor feia
   - a professora pediu um relatório de faltas para amanhã de manhã
   - o código do login está bagunçado e ninguém entende mais
   - um aluno reclamou que o botão de sair é pequeno no celular
   - os dados de 30 alunos sumiram do sistema
3. **Escrevam 3 políticas explícitas** para esse quadro. Uma delas obrigatoriamente responde: *quem pode colocar cartão na raia Urgente?*
4. **Teste de estresse:** o professor entrega um sétimo cartão surpresa — *"o diretor quer, agora, um gráfico bonito para a reunião de amanhã"*. Aplicando **só o que vocês escreveram**, em qual raia ele cai? Se as políticas do grupo não responderem, reescrevam a que faltou.

Cada grupo lê em voz alta a política que mais gerou discussão interna.

## Avaliação

```quiz
- pergunta: Qual das tarefas abaixo é importante mas NÃO é urgente?
  alternativas:
    - texto: O sistema caiu e nenhum usuário consegue entrar
    - texto: Melhorar o código bagunçado do login, que ainda funciona
      correta: true
    - texto: Trocar a cor de um botão que ninguém reclamou
    - texto: Um relatório pedido no chat para daqui a dez minutos
  feedback: >
    Ela muda o resultado do time no médio prazo e não tem prazo colado — por isso
    precisa ser agendada, senão nunca acontece.
- pergunta: O que uma raia (swimlane) faz no quadro Kanban?
  alternativas:
    - texto: Divide o quadro na horizontal, separando tipos de trabalho que atravessam as mesmas etapas
      correta: true
    - texto: Substitui as colunas do fluxo de trabalho
    - texto: Marca quais dias da semana o time trabalha
    - texto: Indica quantas horas cada cartão vai levar
  feedback: >
    Coluna é etapa do fluxo, na vertical; raia é categoria de trabalho, na horizontal.
    O cartão anda pelas colunas dentro da sua raia.
- pergunta: Por que não basta desenhar uma raia de urgência no quadro?
  alternativas:
    - texto: Porque raia só funciona em quadro digital, nunca em papel
    - texto: Porque a raia precisa vir com a classe de serviço — limite, quem pode usar e o que o time faz quando ela recebe trabalho
      correta: true
    - texto: Porque a raia atrapalha a leitura do quadro
    - texto: Porque urgência deve ser decidida pelo time no momento em que o problema aparece
  feedback: >
    Sem a regra de atendimento escrita, a raia é só uma linha. A classe de serviço é
    o que faz a decisão acontecer sem discussão no calor do momento.
- pergunta: Um time escreve na lateral do quadro "Só o Product Owner coloca cartão na raia de urgência". Isso é um exemplo de quê?
  alternativas:
    - texto: Uma cerimônia do Scrum
    - texto: Uma política explícita
      correta: true
    - texto: Um limite de WIP
    - texto: Uma estimativa de esforço
  feedback: >
    É uma regra do quadro escrita e visível a todos — exatamente a definição de
    política explícita. Ela evita que quem está com pressa decida sozinho o que é urgente.
```

## Fechamento

Hoje você descobriu que:

- **Importante** e **urgente** são perguntas diferentes, e time que chama tudo de urgente perde os dois — o urgente deixa de significar algo e o importante não anda.
- A **raia** divide o quadro na horizontal e separa tipos de trabalho; a **classe de serviço** é a regra de atendimento que ela carrega.
- **Políticas explícitas** tiram as regras da cabeça das pessoas e colocam no quadro, onde quem chegou ontem também enxerga.
- A grande sacada é o **momento** da decisão: combinar com a cabeça fria, semanas antes, em vez de discutir com o cliente ligando.

**Fim do bloco de Kanban:** você percorreu a agilidade inteira nesta trilha — do **Manifesto Ágil** ao time Scrum, das **cerimônias** e **histórias de usuário** à **estimativa**, e agora do **quadro Kanban** ao fluxo puxado, ao limite de WIP e às políticas explícitas. São duas famílias de método que qualquer time de software espera que você reconheça. Na vida real, o próximo passo é medir: quanto tempo um cartão leva do começo à entrega — e o que fazer quando esse número não agrada.

:::roteiro
Abrir com o celular de novo (na 53 já foi usado, e a repetição aqui é proposital): peça que digam quantas notificações chegaram durante a aula anterior, e depois pergunte quantos trabalhos escolares "notificaram". O silêncio é o gancho. A matriz 2x2 vale ir ao quadro branco e preencher COM a turma, pedindo exemplos deles antes de mostrar os do texto — o quadrante "não importante e urgente" é o que gera mais discussão e é o mais útil da vida. Marque bem a correção da origem: "importante x urgente" é matriz de Eisenhower, não é Kanban; o deck da SEED apresenta como se fosse conceito nativo, e o mecanismo Kanban de verdade é raia + classe de serviço. Na prática, o cartão-surpresa do passo 4 é o momento pedagógico — não entregue antes dos grupos terem escrito as políticas, senão perde a graça; a resposta certa costuma ser "não é urgente, é só barulhento", mas aceite qualquer resposta que as políticas do grupo sustentem. A tabela Scrum × Kanban cobre o escopo do deck 53 da SEED e fecha a trilha; se o tempo apertar, corte o exemplo em bloco de código, não a tabela. Alura ("Kanban: análises e implementação", tarefas de raias e políticas explícitas) e o vídeo de políticas explícitas ficam como apoio opcional pra quem quiser seguir em casa.
:::
