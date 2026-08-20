---
titulo: "Kanban: o quadro e o fluxo"
tema: Metodologias Ágeis
disciplina: analise-e-metodos-para-sistemas
serie: 1ª
prerequisitos: [Fundamentos da Agilidade, Introdução ao Scrum]
objetivos:
  - Explicar o que é Kanban e por que ele é um sistema puxado
  - Descrever a anatomia do quadro — colunas como etapas do fluxo real e cartões como trabalho
  - Explicar por que limitar o trabalho em progresso (WIP) faz o time entregar mais rápido
  - Identificar um gargalo olhando para o quadro
trilha: metodologias-ageis
ordem: 53
slug: kanban-o-quadro-e-o-fluxo
modo_origem: seed
fontes:
  - lake/analise-e-metodos-para-sistemas/AULA 53_ANÁLISE E MÉTODO PARA SISTEMAS.pptx.pdf
  - lake/analise-e-metodos-para-sistemas/AULA 54_ANÁLISE E MÉTODO PARA SISTEMAS.pptx.pdf
revisao: true
status: aprovada
versao: 2
atualizado_em: 2026-08-20
---

Abre o caderno e conta quantos trabalhos você tem em aberto agora. Não os que terminou — os que **começou e não terminou**: a pesquisa de história, o exercício de matemática pela metade, o vídeo que prometeu editar pro grupo. Provavelmente são uns quatro ou cinco. E aqui vai a parte incômoda: se alguém perguntasse hoje "quantos desses estão prontos?", a resposta seria *nenhum*. Todo esse trabalho existe, custou horas suas, e mesmo assim não entregou nada a ninguém. Times de software vivem exatamente esse problema, só que multiplicado por dez pessoas — e inventaram um quadro de parede pra resolver.

## Objetivos

Ao final desta aula, você será capaz de:

- Explicar o que é **Kanban** e por que ele é um sistema **puxado**.
- Descrever a anatomia do quadro: **colunas** são as etapas do fluxo real, **cartões** são o trabalho.
- Explicar por que **limitar o trabalho em progresso** faz o time entregar mais rápido.
- Identificar um **gargalo** só de olhar para o quadro.

## Pré-requisitos

Ter visto a **Aula 33** (o que é agilidade) e a **Aula 34** (time Scrum). Não é preciso saber programar.

## Desenvolvimento

### Em uma frase

:::importante
Kanban não é uma lista de tarefas bonita. É um jeito de tornar o trabalho **visível** e depois **limitar quanto trabalho pode estar acontecendo ao mesmo tempo** — porque time que começa tudo não termina nada.
:::

### O quadro torna visível um trabalho que é invisível

Trabalho físico se vê: numa oficina, dá pra andar pelo galpão e enxergar quantos carros estão sem porta. Software não. O trabalho de um programador cabe inteiro dentro da cabeça dele e de um arquivo que ninguém mais abriu. Se o time não fizer um esforço deliberado para mostrar o trabalho, ele simplesmente **não existe** para os outros — e aí ninguém sabe quem está atolado, o que travou, ou o que já podia ter sido entregue.

:::conceito Kanban
Método de gestão do trabalho baseado em **sinais visuais**. A palavra vem do japonês e significa mais ou menos "cartão de sinalização". O time representa cada pedaço de trabalho como um **cartão** e move esse cartão por **colunas** que representam as etapas reais do processo, do começo até a entrega.

:::

As duas peças são simples, mas cada uma tem uma regra que quase todo iniciante erra:

- **Coluna = uma etapa real do fluxo do time.** Não é "A Fazer / Fazendo / Feito" porque alguém copiou de um vídeo. É o caminho que o trabalho percorre *neste* time: `Analisar → Desenvolver → Testar → Publicar`. Se o time revisa o trabalho antes de publicar e não existe coluna de revisão, essa etapa fica invisível — e o que está invisível não é gerenciado.
- **Cartão = um pedaço de trabalho que entrega valor sozinho**, não uma tarefa solta. Ele carrega o que precisa para alguém pegar e tocar: descrição, responsável, prazo se houver.

```diagrama-progressivo
titulo: A vida de um cartão no quadro
camadas:
  - rotulo: Nasce na fila
    conteudo: O trabalho entra pela coluna da esquerda, geralmente chamada de "A fazer" ou "Pronto para começar". Ele existe, está escrito, mas ninguém encostou nele ainda.
  - rotulo: Alguém puxa
    conteudo: Ninguém distribui o cartão. Quem terminou o trabalho anterior vai lá e puxa o próximo. É essa inversão que dá nome ao sistema puxado.
  - rotulo: Atravessa as etapas
    conteudo: O cartão vai andando pelas colunas do time — desenvolver, testar, revisar. A posição dele no quadro é o status. Não existe outro relatório de andamento.
  - rotulo: Chega ao fim
    conteudo: O cartão entra na última coluna só quando está entregue de verdade, no critério combinado pelo time. Aí ele para de ocupar espaço e a capacidade volta a ficar livre.
```

:::curiosidade De onde isso saiu
O Kanban nasceu na Toyota, no Japão do pós-guerra. Taiichi Ohno, o engenheiro por trás do sistema, se inspirou em algo bem prosaico: o **supermercado americano**. Ele notou que o funcionário não enche a prateleira num cronograma fixo — ele repõe quando o cliente tira. O consumo é que dispara a produção. Levar essa ideia para a linha de montagem virou o Sistema Toyota de Produção; levá-la para software só aconteceu por volta de 2007, quase sessenta anos depois.

:::

### Puxar em vez de empurrar: o limite de WIP

Aqui está o coração da aula, e é a parte que parece errada na primeira leitura.

:::conceito Limite de WIP
**WIP** vem de *Work In Progress* — trabalho em progresso: tudo que já começou e ainda não terminou. O **limite de WIP** é um número escrito no alto de cada coluna dizendo quantos cartões podem ficar ali ao mesmo tempo. Coluna cheia, ninguém puxa mais nada: quem estiver livre vai **ajudar a terminar** o que já está em andamento.

:::

Por que raios um time se **impediria** de trabalhar? Volta pros seus cinco trabalhos escolares. Suponha que cada um dá 1 hora de esforço, e você tem 5 horas.

- **Empurrando tudo junto** (um pouco de cada, revezando): na hora 5, os cinco ficam prontos ao mesmo tempo. Antes disso, o número de trabalhos entregues é **zero** o tempo inteiro.
- **Puxando um de cada vez:** o primeiro fica pronto na hora 1. O segundo na hora 2. Na hora 5 você tem os mesmos cinco prontos.

O esforço total foi idêntico. Mas no segundo caso você teve **algo pronto quatro horas antes** — e, se a professora antecipar o prazo de um deles, você já entregou. É por isso que limitar o WIP não faz o time trabalhar menos: faz o trabalho **terminar mais cedo**. O que se corta não é esforço, é fila.

:::atencao Erro comum, e dá pra diagnosticar de longe
Olhe um quadro com **12 cartões em "Em andamento" e 1 em "Concluído"**. Esse time não está produtivo — está travado. Cada cartão parado ali é trabalho já pago e ainda não entregue, e cada troca de contexto entre eles custa mais um pedaço de atenção. Sintoma clássico: todo mundo se diz ocupadíssimo e a entrega não sai. O quadro denuncia na hora, e é exatamente para isso que ele serve.

:::

### Onde o trabalho trava: o gargalo

:::conceito Gargalo
É a etapa **mais lenta** do fluxo — a que recebe trabalho mais rápido do que consegue despachar. No quadro, ela se entrega sozinha: os cartões vão se **empilhando** na entrada dela enquanto as colunas seguintes ficam vazias.

:::

E aqui está a virada de chave: a velocidade do time inteiro é a velocidade do gargalo. Não adianta desenvolver mais rápido se tudo empaca no teste — só aumenta a pilha. Acelerar o time significa **atacar a coluna que empilhou**, mesmo que ela não seja a sua.

:::exemplo O quadro contando a história
Um time tem `Desenvolver → Testar → Publicar`. Na segunda-feira o quadro mostra 2 cartões em Desenvolver, 7 em Testar e 0 em Publicar. Não existe reunião necessária pra descobrir o problema: o teste é o gargalo. E a decisão correta é contraintuitiva — os desenvolvedores **param de começar coisa nova** e vão ajudar a testar. Se em vez disso puxarem mais três cartões pra desenvolver, a pilha do teste vira dez e a entrega demora ainda mais.

:::

:::dica Onde você vai encontrar isso
Todo quadro que você já viu na internet é um Kanban: Trello, quadro de Projects do GitHub, Jira, Notion. Em processo seletivo de estágio, "sei trabalhar com quadro Kanban" só impressiona quem consegue completar a frase — falar de **limite de WIP** e de **gargalo** separa quem usou a ferramenta de quem entendeu o método. E vale fora do trabalho: um quadro de três colunas para as matérias do bimestre, com limite de 2 em andamento, resolve mais do que parece.

:::

## Prática

**Atividade "Meu Kanban da semana" (individual, no caderno, ~10 min).** Cada aluno monta o próprio quadro Kanban com tarefas reais da vida escolar. O objetivo é sentir na pele os três conceitos da aula — cartão, coluna e limite de WIP — aplicados a algo que é dele, não a um exemplo abstrato.

1. **Liste o trabalho real.** No caderno, escreva 5 tarefas escolares que estão em aberto **agora** — dever de casa, trabalho em grupo, estudo pra prova, redação. Cada uma vira um cartão: um retângulo pequeno com o nome da tarefa dentro.
2. **Desenhe o quadro.** Trace 3 colunas lado a lado com estes títulos: `A Fazer` · `Fazendo` · `Feito`. Essas são as etapas reais do trabalho de estudar — do jeito que ele acontece de verdade.
3. **Posicione cada cartão.** Olhe as 5 tarefas e coloque cada uma na coluna que representa a situação dela **hoje**: ainda nem começou (`A Fazer`), já começou mas não terminou (`Fazendo`), ou já entregou (`Feito`).
4. **Aplique o limite de WIP.** Regra: **no máximo 2 cartões na coluna `Fazendo`.** Se já tem 2 ali e quer começar uma terceira tarefa, não pode — primeiro termina uma das duas e move pra `Feito`. É a mesma regra do supermercado: só repõe quando alguém tira.
5. **Ache seu gargalo.** Olhe pra coluna `Fazendo`: qual tarefa está parada ali há mais tempo? Escreva uma frase respondendo por que ela travou — faltou tempo, ficou difícil, dependia de outra pessoa?

Fechem com uma pergunta pra turma: quem tinha mais de 2 tarefas "começadas" antes de desenhar o quadro? E quantas dessas estavam de fato prontas?

## Avaliação

```quiz
- pergunta: O que caracteriza o Kanban como um sistema puxado?
  alternativas:
    - texto: Um líder distribui as tarefas entre os membros do time todo dia de manhã
    - texto: Quem termina o trabalho anterior é que puxa o próximo cartão da fila
      correta: true
    - texto: As tarefas são sorteadas entre os membros do time
    - texto: Todas as tarefas começam ao mesmo tempo, no início do projeto
  feedback: >
    No sistema puxado é a capacidade livre que dispara o próximo trabalho — a mesma
    ideia do supermercado que repõe a prateleira quando o cliente tira o produto.
- pergunta: O que as colunas de um quadro Kanban devem representar?
  alternativas:
    - texto: Os dias da semana em que o trabalho será feito
    - texto: As etapas reais pelas quais o trabalho daquele time passa
      correta: true
    - texto: Os membros do time, uma coluna para cada pessoa
    - texto: Sempre exatamente três, com os nomes A Fazer, Fazendo e Feito
  feedback: >
    A coluna representa uma etapa do fluxo real. Etapa que o time executa mas não
    tem coluna vira trabalho invisível — e o que está invisível não é gerenciado.
- pergunta: Por que limitar o trabalho em progresso faz o time entregar mais rápido?
  alternativas:
    - texto: Porque obriga cada pessoa a trabalhar mais horas por dia
    - texto: Porque reduz a fila de coisas começadas, fazendo o trabalho terminar mais cedo
      correta: true
    - texto: Porque diminui a quantidade total de trabalho que o time precisa fazer
    - texto: Porque permite que o time comece muito mais tarefas ao mesmo tempo
  feedback: >
    O esforço total é o mesmo; o que muda é a fila. Terminar um item antes de começar
    o próximo entrega valor mais cedo e corta o custo de trocar de contexto.
- pergunta: No quadro há 2 cartões em Desenvolver, 7 em Testar e 0 em Publicar. O que isso indica?
  alternativas:
    - texto: O time está muito produtivo, pois há bastante trabalho em andamento
    - texto: O teste é o gargalo, e a entrega do time inteiro está limitada por ele
      correta: true
    - texto: A coluna Publicar deveria ser eliminada do quadro
    - texto: Faltam desenvolvedores no time
  feedback: >
    Cartão empilhando na entrada de uma etapa é a assinatura do gargalo. A ação
    correta é ajudar a esvaziar o teste, não puxar mais trabalho para desenvolver.
```

## Fechamento

Hoje você descobriu que:

- **Kanban** torna visível um trabalho que, em software, é naturalmente invisível — com **cartões** andando por **colunas** que são as etapas reais do time.
- É um sistema **puxado**: ninguém distribui tarefa, quem tem capacidade livre puxa a próxima.
- O **limite de WIP** parece freio, mas é acelerador: menos coisa começada ao mesmo tempo significa coisa terminada mais cedo.
- O **gargalo** é a etapa onde os cartões se empilham — e a velocidade do time inteiro é a velocidade dele.

**Próxima aula:** o quadro te mostra *o que* está acontecendo, mas não decide *o que puxar agora*. Quando chega um bug que derrubou o sistema no meio de uma tarefa importante, quem passa na frente? Vamos ver as **raias**, a diferença entre **importante e urgente**, e as **políticas explícitas** — as regras que fazem o quadro funcionar sem alguém apitando.

:::roteiro
Abrir mandando contar os trabalhos escolares em aberto, de verdade, em voz alta — o número costuma envergonhar e é exatamente o gancho. NÃO entregue o limite de WIP como regra pronta: pergunte primeiro "por que um time se proibiria de trabalhar?" e deixe a turma achar absurdo, o efeito da prática depende desse estranhamento inicial. A conta dos 5 trabalhos (1h cada) vale ir ao quadro branco desenhando a linha do tempo das duas estratégias; é o momento em que a ficha cai. A prática do "Meu Kanban da semana" é individual e rápida — cada aluno usa as próprias tarefas reais, então não precisa preparar material antes. Se algum aluno reclamar que não tem 5 tarefas em aberto, peça pra incluir também compromissos fora da escola (estágio, casa). O passo do limite de WIP costuma gerar resistência ("mas eu consigo fazer 3 ao mesmo tempo") — não ceda, é exatamente esse desconforto que ensina o conceito. Fusão de origem: esta aula cobre os decks 53 e 54 da SEED, que repetem o mesmo conteúdo de quadro/cartão/WIP; o "como montar o quadro" do deck 54 virou a prática. Curso Alura ("Kanban: análises e implementação") é apoio opcional para quem quiser seguir em casa — não cabe em 50 min junto com a prática.
:::
