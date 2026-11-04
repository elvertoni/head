---
titulo: "Projeto FilaZero: do Canvas ao Blueprint e aos requisitos"
tema: Usabilidade e Design de Serviços
disciplina: analise-e-metodos-para-sistemas
serie: 1ª
prerequisitos: ["Lean Canvas: a ideia como hipótese", "Service Blueprint: a planta do serviço", "Priorização do backlog (MoSCoW)"]
objetivos:
  - Usar o Lean Canvas e o Service Blueprint juntos, sabendo a pergunta que cada um responde
  - Encontrar no blueprint pontos de falha que o canvas não mostrava
  - Escrever requisitos com rastreabilidade, indicando de onde cada um veio
  - Priorizar os requisitos de um MVP com MoSCoW
trilha: usabilidade-e-design-de-servicos
ordem: 11
slug: projeto-filazero
modo_origem: seed
fontes:
  - lake/analise-e-metodos-para-sistemas/seed-87-95/95-lean-canvas-e-blueprint-aplicacao.pptx
  - lake/analise-e-metodos-para-sistemas/seed-87-95/94-lean-canvas-e-blueprint.pptx
  - lake/analise-e-metodos-para-sistemas/seed-87-95/90-design-de-servicos-introducao.pptx
revisao: true
status: aprovada
versao: 1
atualizado_em: 2026-11-04
---

Toca o sinal do intervalo. Você tem 15 minutos. Corre para a cantina e encontra uma fila que dobra o corredor. Dez minutos depois, chega a sua vez e o salgado que você queria acabou. Você pega o que sobrou, come em três mordidas e volta correndo. Essa cena é tão comum que nem parece problema: parece a vida. Nas últimas dez aulas você juntou todas as ferramentas para enxergar e consertar uma cena assim: heurísticas, leis de UX, jornada, entrevistas, Lean Canvas e Blueprint. Hoje você vai usá-las juntas, num projeto só: o **FilaZero**, um sistema para acabar com a fila da cantina. E vai sair da aula com o que uma equipe de verdade leva para a primeira sprint: uma lista de requisitos priorizada, cada um com o seu porquê.

## Objetivos

Ao final desta aula, você será capaz de:

- Usar o **Lean Canvas** e o **Service Blueprint** juntos, sabendo a pergunta que cada um responde.
- Encontrar no blueprint **pontos de falha** que o canvas não mostrava.
- Escrever **requisitos com rastreabilidade**, indicando de onde cada um veio.
- Priorizar os requisitos de um **MVP** com **MoSCoW**.

## Pré-requisitos

Ter visto as **Aulas 09 e 10** (Lean Canvas e Service Blueprint) e o método **MoSCoW** da trilha de Metodologias Ágeis (aula 37).

## Desenvolvimento

### Duas ferramentas, duas perguntas

A equipe do FilaZero já fez a lição de casa: entrevistou alunos e as duas atendentes da cantina. A análise das falas (como na aula 08) mostrou três padrões: **a fila come o intervalo**, **o aluno só descobre que o produto acabou quando chega ao balcão** e **as atendentes não conseguem preparar nada antes, porque não sabem o que vai ser pedido**.

Com isso em mãos, cada ferramenta responde a uma pergunta diferente:

| Ferramenta | Pergunta | Ponto de vista |
|---|---|---|
| **Lean Canvas** | **O que** estamos propondo e **por quê**? | Do produto: problema, público, valor, métricas |
| **Service Blueprint** | **Como** isso vai acontecer, etapa por etapa? | Do serviço: usuário, frontstage, backstage, suporte |

O caminho completo fica assim: **problema → proposta de valor → solução → experiência → processos → requisitos**. O canvas cuida da primeira metade e o blueprint, da segunda.

### Passo 1: o canvas do FilaZero

| Bloco | FilaZero | E ou H |
|---|---|---|
| **Problema** | Fila longa e produtos que acabam sem aviso; o aluno perde o intervalo. Hoje: chegar correndo e torcer. | E |
| **Segmentos** | Alunos (primeiros adotantes: o 3º ano, que tem menos tempo de intervalo) e a equipe da cantina | E |
| **Proposta de valor** | "Seu lanche pronto quando você chegar ao balcão." | H |
| **Solução** | Cardápio com o que ainda tem, pedido antecipado, aviso de pedido pronto | H |
| **Canais** | Aplicação web aberta pelo celular; QR Code no mural da cantina | H |
| **Receitas (sustentabilidade)** | A cantina paga a hospedagem com a economia de produto desperdiçado | H |
| **Custos** | Hospedagem, manutenção pela turma de Desenvolvimento de Sistemas | H |
| **Métrica-chave** | Tempo médio entre o sinal do intervalo e o lanche na mão | H |
| **Vantagem injusta** | Feito dentro da escola, com acesso direto a alunos e atendentes | E |

:::importante O canvas não mostra os bastidores
Repare: nada nesse canvas diz **como** a cantina fica sabendo do pedido, **quem** marca o pedido como pronto ou **o que acontece** quando o salgado acaba no meio do intervalo. O canvas está correto e mesmo assim esconde metade do trabalho. É para isso que serve o próximo passo.
:::

### Passo 2: o blueprint do pedido

```diagrama-progressivo
titulo: O pedido no FilaZero, do celular ao balcão
camadas:
  - rotulo: O aluno faz o pedido
    conteudo: De manhã, antes de entrar na sala, escolhe uma coxinha e um suco no cardápio e confirma. Frontstage, o app mostra "Pedido 37 recebido".
  - rotulo: A cantina recebe
    conteudo: Backstage, o pedido aparece numa tela na cozinha, em ordem de chegada. Suporte, o banco de dados registra o pedido e desconta os itens do estoque.
  - rotulo: O ponto de falha aparece
    conteudo: "F, o estoque do sistema é atualizado à mão no começo do dia. Quando a coxinha acaba às 9h50, o app continua oferecendo coxinha. O pedido 38 vai ser de um produto que não existe mais."
  - rotulo: O pedido fica pronto
    conteudo: Backstage, a atendente separa o lanche e toca em Pronto na tela da cozinha. Frontstage, o celular do aluno avisa "Pedido 37 pronto, retire no balcão 2".
  - rotulo: A retirada
    conteudo: "W, se todos chegam juntos no sinal, forma-se fila no balcão de retirada. O blueprint mostra que o FilaZero precisa de horários de retirada escalonados ou de um balcão só para pedidos antecipados."
```

### Passo 3: do blueprint ao backlog

Cada requisito agora precisa de **origem**: o bloco do canvas, a etapa do blueprint ou a fala de entrevista que o justifica. Isso se chama **rastreabilidade**, e é o que permite responder, meses depois, à pergunta "por que mesmo a gente fez isso?". Com a origem na mão, a equipe prioriza o [[mvp|MVP]] usando o [[moscow|MoSCoW]]:

| Requisito | Origem | MoSCoW |
|---|---|---|
| O sistema deve registrar o pedido do aluno | Canvas, Solução | Must |
| A cantina deve ver os pedidos em ordem de chegada | Blueprint, backstage da recepção do pedido | Must |
| O sistema deve deixar de oferecer um item quando o estoque zerar | Blueprint, **F** do estoque | Must |
| O sistema deve avisar o aluno quando o pedido estiver pronto | Blueprint, frontstage; entrevistas | Should |
| O aluno deve escolher um horário de retirada | Blueprint, **W** da retirada | Could |
| Ranking dos alunos que mais compram | nenhuma | Won't |

:::atencao Erro comum: o requisito que não veio de lugar nenhum
Na hora de listar funções, sempre aparece alguém com "e se tivesse um chat?", "e um ranking de quem mais compra?", "e modo escuro?". Pode até ser legal, mas não veio de nenhum problema, nenhuma etapa e nenhuma fala. Sem origem, é gosto da equipe, e esse tipo de função consome semanas de trabalho sem aproximar o projeto da métrica-chave. O teste é a coluna **Origem**: se ficar vazia, o requisito vai para Won't, pelo menos até alguma evidência aparecer.
:::

:::dica Na profissão e no TCC
Essa sequência (problema, canvas, jornada ou blueprint, requisitos com origem, backlog priorizado) é praticamente o roteiro de documentação de um projeto de software, e é uma ótima estrutura para o seu TCC. Na banca, quando alguém perguntar "por que essa função existe?", você aponta a linha da tabela e a evidência por trás dela. Em empresas, ferramentas como Jira e GitHub Issues guardam exatamente isso: cada item com descrição, prioridade e o link para de onde ele veio.
:::

## Prática

**Atividade "e quando o lanche acaba?" (grupos de 4, sem computador, ~15 min).** O ponto de falha do estoque é o mais sério do FilaZero. Vocês vão resolvê-lo.

1. **Mini-blueprint (6 min).** Desenhem o blueprint do momento em que **um produto acaba durante o intervalo**, em três etapas: *o produto acaba na cozinha*, *um aluno tenta pedir esse produto*, *um aluno que já tinha pedido descobre que não vai receber*. Preencham as cinco camadas e marquem pelo menos um **F**.
2. **Requisitos (6 min).** Escrevam **três requisitos** para esse momento, cada um com sua **origem** (etapa e camada do blueprint) e sua prioridade **MoSCoW**. Pelo menos um deve ser **Must** e pelo menos um deve ser **Won't**, com justificativa.
3. **Volta ao canvas (3 min).** Algum desses requisitos muda o Lean Canvas? Por exemplo, ele cria um custo novo ou muda a métrica-chave? Anotem em uma frase.

Cada grupo lê o seu requisito Must. A turma confere: a origem está clara?

## Avaliação

```quiz
- pergunta: Que pergunta o Lean Canvas responde, e qual o Service Blueprint responde?
  alternativas:
    - texto: O canvas responde como o serviço acontece; o blueprint, quanto custa
    - texto: O canvas responde o que estamos propondo e por quê; o blueprint, como isso vai acontecer etapa por etapa
      correta: true
    - texto: Os dois respondem a mesma pergunta com desenhos diferentes
    - texto: O canvas é para o usuário e o blueprint é para o professor
  feedback: >
    Canvas é a visão do produto (problema, valor, métricas). Blueprint é a visão da
    entrega do serviço (usuário, palco, bastidores, suporte).
- pergunta: No Lean Canvas de um sistema de consultas, a equipe identificou a necessidade de reduzir faltas. Ao construir o blueprint, que ação transforma melhor essa necessidade em processo do serviço?
  alternativas:
    - texto: Escolher as cores da interface
    - texto: Colocar mais pessoas na equipe de programação
    - texto: Enviar automaticamente uma confirmação e um lembrete antes da consulta
      correta: true
    - texto: Criar o logotipo antes de definir o fluxo do usuário
  feedback: >
    A necessidade do canvas vira uma etapa do serviço (agendar, confirmar, lembrar,
    comparecer) e, daí, um requisito do sistema.
- pergunta: No FilaZero, o app continua oferecendo coxinha depois que ela acabou, porque o estoque do sistema é atualizado à mão no começo do dia. Onde esse problema aparece e o que ele gera?
  alternativas:
    - texto: No canvas, e gera uma nova proposta de valor
    - texto: No blueprint, como ponto de falha no suporte, e gera o requisito de deixar de oferecer o item quando o estoque zerar
      correta: true
    - texto: Em nenhuma ferramenta, porque é problema da cantina e não do sistema
    - texto: Na tela de login, e gera a troca de senha
  feedback: >
    O canvas não mostra os bastidores; o blueprint sim. O F no estoque vira requisito
    com origem clara.
- pergunta: Qual destes requisitos NÃO tem rastreabilidade no FilaZero?
  alternativas:
    - texto: A cantina deve ver os pedidos em ordem de chegada
    - texto: O sistema deve avisar quando o pedido estiver pronto
    - texto: O sistema deve mostrar um ranking dos alunos que mais compram
      correta: true
    - texto: O sistema deve deixar de oferecer um item sem estoque
  feedback: >
    O ranking não vem de nenhum problema, etapa do blueprint ou fala de entrevista.
    Sem origem, vai para Won't.
- pergunta: Para o MVP do FilaZero, qual requisito é um Must?
  alternativas:
    - texto: Modo escuro no aplicativo
    - texto: Escolher horário de retirada
    - texto: Registrar o pedido do aluno e mostrá-lo à cantina
      correta: true
    - texto: Chat entre alunos
  feedback: >
    Sem registrar o pedido e fazê-lo chegar à cantina, o FilaZero não funciona. O
    resto pode esperar uma próxima entrega.
```

## Fechamento

Hoje você descobriu que:

- **Lean Canvas** e **Service Blueprint** se completam: um diz **o que e por quê**, o outro mostra **como**.
- O blueprint revela **pontos de falha** que o canvas esconde, como o estoque que não se atualiza.
- Todo requisito precisa de **origem**; a **rastreabilidade** separa necessidade de gosto da equipe.
- Com **MoSCoW**, a lista vira um **MVP**: o mínimo que já resolve o problema.

**Fim do bloco:** você começou olhando um botão ("funciona, mas é fácil de usar?") e terminou desenhando um serviço inteiro, da fila até o banco de dados. Heurísticas, leis de UX, jornada, entrevistas, Canvas e Blueprint são as ferramentas de quem **entende o problema antes de programar**. No mercado, é isso que diferencia quem só escreve código de quem constrói sistemas que as pessoas realmente usam.

:::roteiro
Abrir com a cena do intervalo e uma enquete rápida de mão levantada: quem já ficou sem lanche por causa da fila? É o problema mais universal da escola e prende a turma. O FilaZero e a tabela do canvas vêm do deck 95 da SEED; acrescentamos a coluna E/H, a métrica de tempo (no deck era "tempo de espera e nº de pedidos", e número de pedidos não mede o problema), o F do estoque (vem do caso da cantina do deck 90, em que itens apareciam disponíveis depois de acabar) e a tabela com rastreabilidade e MoSCoW. O desafio "reduzir faltas" do deck 95 virou a questão 2 do quiz. No diagrama, pare antes de "O ponto de falha aparece" e pergunte "o que acontece quando a coxinha acaba?". Se a turma não lembrar do MoSCoW, revise em um minuto com o próprio exemplo da tabela. Na prática, Won't bons costumam ser "reembolso automático por pix" (custo e complexidade) ou "sugerir produto substituto com IA". Requisitos Must esperados: "remover o item do cardápio quando o estoque zerar" e "avisar o aluno cujo pedido não poderá ser atendido". Como encerramento do bloco, se houver tempo, pergunte que ferramenta das 11 aulas cada um usaria no próprio TCC.
:::
