---
titulo: "MVP: a menor coisa que ensina alguma coisa"
tema: MVP — conceito e tipos
disciplina: programacao-front-end
serie: 2ª
prerequisitos: [Ter a frase de dor da Aula 07 preenchida, com a prova]
objetivos:
  - Explicar por que um MVP é um experimento e não uma versão reduzida do produto
  - Transformar a dor da Aula 07 em uma hipótese que pode ser reprovada
  - Escolher o tipo de MVP adequado ao que se quer descobrir
  - Escrever o briefing da landing page que será construída nas aulas seguintes
trilha: landing-page-mvp
ordem: 8
slug: mvp-a-menor-coisa-que-ensina
modo_origem: tema
fontes: []
revisao: false
status: aprovada
versao: 2
atualizado_em: 2026-08-21
---

Vocês saíram da aula passada com uma frase. O instinto agora é abrir o VSCode e começar o aplicativo — e essa é exatamente a armadilha. Todo ano tem trio que faz isso: passa três meses programando com afinco, entrega em novembro um sistema que funciona, bonito de ver, e descobre na apresentação que ninguém queria aquilo. O trabalho estava certo; a pergunta é que nunca foi feita. A aula de hoje é sobre a pergunta que se faz **antes** de construir: qual é a menor coisa que eu consigo colocar de pé para descobrir se estou errado — em uma semana, e não em três meses?

## Objetivos

Ao final desta aula, você será capaz de:

- Explicar por que MVP **não** é "o produto com menos telas".
- Transformar a dor da aula passada em uma **hipótese** — uma frase que pode dar errado.
- Escolher, entre cinco tipos de MVP, o que responde a sua pergunta pelo menor custo.
- Sair com o **briefing** preenchido: o documento que a aula 10 vai transformar em página.

## Pré-requisitos

A frase de dor da Aula 07, no formato *"[quem] não consegue [o quê] porque [obstáculo]"*, com a prova de como essa pessoa se vira hoje. Trio que perdeu a frase refaz agora, em três minutos, antes de continuar — sem ela o resto da aula não tem sobre o que trabalhar.

## Desenvolvimento

### O mal-entendido que custa um semestre

Pergunte a dez pessoas o que é um MVP e nove respondem alguma variação de "é a primeira versão, mais simples, com o básico". Essa definição parece inofensiva e faz o trio inteiro perder o semestre, porque ela mantém a lógica de **construir**: se MVP é o produto com menos coisa, então o trabalho continua sendo escolher o que cortar. Você corta, corta, corta — e no fim ainda construiu, só que menos. E continua sem saber se alguém queria.

A sigla ajuda a confundir. *Minimum Viable Product* tem a palavra "produto" no nome, e a gente se agarra nela. Mas a palavra que faz o trabalho é outra:

![Comparação de duas leituras. À esquerda, sob a marca de errado, o produto final desenhado como um bloco completo e, ao lado, o mesmo bloco com pedaços removidos, rotulado como versão reduzida — as duas coisas continuam sendo o produto. À direita, sob a marca de certo, uma balança ou instrumento de medida com uma pergunta de um lado e dois pratos de resposta possível, sim e não, mostrando que o MVP é um teste que admite resultado negativo, e não uma parte do produto.](img/mvp-nao-e-produto-menor.png)

:::conceito MVP
**MVP** é o **experimento mais barato capaz de te dar uma resposta confiável** sobre se sua aposta está certa. O objetivo dele não é entregar valor ao cliente — é **entregar aprendizado a você**. Se você aprendeu o que precisava sem escrever uma linha de código, o MVP cumpriu o papel inteiro.
:::

A virada mental é essa: você não está construindo uma versão pequena do produto. Está montando um **teste**. E teste tem uma característica que produto não tem — ele pode dar **negativo**.

:::atencao O diagnóstico de um minuto
Olhe para o que você planejou como MVP e responda: **qual resultado desse teste me faria desistir da ideia?** Se não existe resultado nenhum que te faça mudar de rumo, você não montou um experimento — montou uma demonstração. MVP que só pode confirmar que você estava certo não é MVP. É propaganda que você fez para si mesmo, e ela custa o semestre inteiro.
:::

### Hipótese: a frase que pode dar errado

Para o teste poder dar negativo, a aposta precisa estar escrita de um jeito que admita o "não". Isso tem nome:

:::conceito Hipótese
**Hipótese** é a aposta escrita de forma que a realidade possa desmenti-la. Ela nomeia **quem**, **o que faria** e **em que proporção** — porque sem proporção não existe reprovação: qualquer resultado vira "deu meio certo".
:::

Compare as duas:

| Aposta vaga | Hipótese testável |
|---|---|
| "As pessoas vão gostar do nosso app." | "Pelo menos 3 de cada 5 alunos do 2º ano, ao ver a página por 10 segundos, dizem que ela resolve o problema deles." |
| "Existe mercado para isso." | "Pelo menos 2 de cada 5 pessoas clicam em 'quero usar' depois de ler a página." |

A coluna da direita tem uma propriedade rara e desconfortável: se der 1 em 5, **você errou**, e não tem como discutir. É esse desconforto que faz o método funcionar. O número escolhido não precisa ser científico — precisa ser escolhido **antes**, porque critério definido depois do resultado é sempre generoso com quem o define.

### Cinco jeitos de testar sem construir

Escolhido o que se quer descobrir, escolhe-se a ferramenta. Estes são os cinco formatos clássicos, do mais braçal ao mais barato:

| Tipo de MVP | Como funciona | Serve para descobrir |
|---|---|---|
| **Concierge** | Você entrega o serviço na mão, para pouquíssimas pessoas, sem sistema nenhum | Se o problema é real e como as pessoas realmente se comportam |
| **Mágico de Oz** | Por fora parece automático; por dentro é você fazendo tudo manualmente | Se a experiência agrada, antes de gastar meses automatizando |
| **Protótipo** | Telas clicáveis que parecem o app, mas nada funciona de verdade | Se as pessoas entendem e conseguem usar |
| **Vídeo** | Um vídeo curto mostrando o produto como se ele já existisse | Se as pessoas querem, quando o produto seria caríssimo de construir |
| **Landing page** | Uma página que explica a proposta e oferece uma ação | Se a promessa convence — e quantos aceitam |

:::curiosidade O homem que vendeu sapatos que não tinha
Quando quis descobrir se as pessoas comprariam sapato pela internet — numa época em que ninguém comprava —, o fundador da Zappos não montou estoque nem sistema. Ele ia às sapatarias da cidade, fotografava os pares na prateleira e publicava as fotos. Quando alguém comprava, ele voltava à loja, pagava o sapato do próprio bolso e despachava na mão. Dava trabalho, não dava lucro e não escalava nada — e não era para isso que servia. Servia para responder uma pergunta que nenhuma pesquisa de opinião responderia: **as pessoas dão o número do cartão?** Deram. Aí valeu a pena construir a empresa.
:::

### Por que a landing page é o MVP mais barato do mundo

Dos cinco, um se destaca para o que vocês precisam agora: a **landing page** — uma página única, com um assunto só e uma ação só, feita para testar se a promessa convence.

Ela ganha por três motivos. É a mais rápida de colocar de pé: dá para publicar em uma aula. É a que exige a coisa mais difícil e mais valiosa do projeto — **explicar em cinco segundos o que o produto resolve**, o que obriga vocês a entender o próprio projeto de verdade. E é a única que produz um **link**, que qualquer pessoa abre no celular sem instalar nada. Um protótipo você precisa estar do lado para mostrar; um link você manda no grupo e volta amanhã para ver o que aconteceu.

```diagrama-progressivo
titulo: O caso Dropbox — como um vídeo substituiu dois anos de programação
camadas:
  - rotulo: O problema técnico
    conteudo: "A ideia era manter uma pasta sincronizada entre vários computadores, sem o usuário fazer nada. Isso é difícil de verdade — exigiria muitos meses de trabalho pesado antes de existir qualquer coisa para mostrar a alguém."
  - rotulo: A dúvida que ninguém conseguia responder
    conteudo: "Já existiam produtos parecidos e nenhum tinha emplacado. A pergunta era anterior ao código — as pessoas se importam com isso a ponto de querer usar? Perguntar não resolvia, porque todo mundo diz que sim quando é de graça e hipotético."
  - rotulo: O MVP que eles fizeram
    conteudo: "Gravaram um vídeo curto demonstrando o produto funcionando, narrado como se ele já estivesse pronto. Boa parte do que aparecia ali ainda não existia. Publicaram o vídeo num fórum de gente da área e ofereceram uma lista de espera."
  - rotulo: A resposta que chegou em uma noite
    conteudo: "A lista de espera saltou de alguns milhares para dezenas de milhares de inscritos da noite para o dia. A hipótese passou — e só então valeu a pena encarar os meses de programação difícil."
  - rotulo: O que isso ensina para o projeto de vocês
    conteudo: "O vídeo não era o produto e não entregou valor a ninguém. Ele entregou uma resposta. É exatamente esse o papel da landing page que vocês vão construir nas próximas aulas."
```

:::dica O nome disso no mercado e no seu TCC
Fora da escola essas palavras andam juntas e são confundidas o tempo todo: **protótipo** testa se dá para usar, **prova de conceito** testa se dá para construir, e **MVP** testa se alguém quer. Saber a diferença já coloca você à frente de muito estagiário. E vale aqui dentro: no TCC do ano que vem, a banca vai perguntar por que vocês construíram o que construíram. Chegar com "porque testamos antes e 4 de 5 pessoas clicaram" é uma resposta de outro nível em relação a "porque achamos que seria útil".
:::

## Prática

**O briefing (em trios, ~15 min).** Este é o documento que a aula 10 vai consumir. Preencham com o cuidado de quem sabe que outra pessoa vai depender disso — porque vai.

```
NOME PROVISÓRIO DO PRODUTO: ..........................................

A DOR (da Aula 07):
[quem] .................. não consegue .................. porque ..................

A HIPÓTESE (com número, escolhido agora):
Pelo menos ....... de cada 5 ....................... vão .......................
depois de ver a página.

QUEM VAI ABRIR ESSA PÁGINA (uma pessoa concreta, não "as pessoas"):
......................................................................

O QUE A PÁGINA PRECISA PROVAR EM 5 SEGUNDOS:
......................................................................

A ÚNICA AÇÃO QUE O VISITANTE DEVE FAZER:
......................................................................
```

Duas regras de fechamento. **Uma ação só** — página que pede "cadastre-se, siga a gente e responda a pesquisa" não recebe nenhuma das três. E **o número da hipótese é escolhido agora**, com o trio olhando na cara um do outro; quem deixa para definir depois do resultado sempre descobre que o resultado foi ótimo.

**Entrega:** o briefing preenchido, com o número da hipótese. Ele precisa chegar inteiro na aula 10 — não pela metade.

## Avaliação

```quiz
- pergunta: Um trio planeja o MVP assim — "vamos fazer o app com só três telas em vez de dez". O que há de errado?
  alternativas:
    - texto: Nada, é exatamente o que MVP significa
    - texto: "Três telas ainda é muito; o certo seria uma tela só"
    - texto: "Continua sendo construir o produto, só que menor — não é um teste que possa dar negativo e dizer que a ideia está errada"
      correta: true
    - texto: O erro é usar telas em vez de páginas de site
  feedback: >
    MVP não é o produto reduzido, é o experimento mais barato que dá uma resposta
    confiável. Cortar telas não cria a possibilidade de reprovação — o trio vai
    construir do mesmo jeito e continuar sem saber se alguém queria.
- pergunta: Qual destas é uma hipótese testável?
  alternativas:
    - texto: Nosso aplicativo vai ajudar muita gente
    - texto: "Pelo menos 3 de cada 5 alunos do 2º ano clicam em quero usar depois de ler a página"
      correta: true
    - texto: Existe um grande mercado para esse tipo de solução
    - texto: As pessoas gostam de aplicativos que economizam tempo
  feedback: >
    Só uma nomeia quem, o que a pessoa faria e em que proporção. Por isso ela pode
    dar errado — se der 1 em 5, a aposta foi reprovada e não há como discutir. As
    outras três não têm resultado nenhum capaz de desmenti-las.
- pergunta: O produto exigiria meses de programação difícil e a dúvida é se alguém se interessaria. Qual tipo de MVP responde isso mais barato?
  alternativas:
    - texto: Construir uma versão simplificada e publicar nas lojas de aplicativos
    - texto: "Um vídeo ou uma landing page mostrando a proposta e medindo quantos demonstram interesse"
      correta: true
    - texto: Uma pesquisa perguntando se as pessoas usariam um app assim
    - texto: Um protótipo de telas clicáveis apresentado individualmente
  feedback: >
    A dúvida é sobre desejo, não sobre usabilidade nem viabilidade técnica — então
    o teste precisa medir gente agindo, não opinando. Vídeo e landing page pedem
    uma ação real e custam quase nada. Perguntar "você usaria?" é o pior caminho:
    de graça e no hipotético, quase todo mundo diz que sim.
```

## Fechamento

O que ficou de hoje:

- **MVP é experimento, não produto reduzido.** O que ele entrega é aprendizado para você, não valor para o cliente.
- **Se nenhum resultado te faria desistir, não é um MVP** — é uma demonstração que você montou para se convencer.
- **Hipótese precisa de número, definido antes.** Sem proporção não existe reprovação, e critério escolhido depois é sempre generoso.
- Entre os cinco tipos, a **landing page** é a que responde mais rápido, obriga vocês a explicar o produto em cinco segundos e produz um **link** que roda sozinho no celular dos outros.

**Próxima aula:** o briefing tem os campos preenchidos, mas ainda não tem o **texto**. E é o texto que decide se a página convence em cinco segundos ou se o visitante fecha a aba. Vamos escrever a headline, os benefícios e a chamada — a parte que trava mais gente que qualquer CSS.

:::roteiro
Abrir cobrando a frase da aula passada de pé, em voz alta, uns três trios. Quem não tem, refaz agora — não deixe a aula andar sem isso, porque o briefing do fim depende dela e trio sem frase vira trio parado nos últimos 15 min.

A pergunta que carrega a aula é uma só: "qual resultado faria vocês desistirem?". Faça essa pergunta trio por trio na Prática — é ela que revela quem entendeu. Resposta "nenhum" significa que o aluno ainda está no modo construir.

No caso Dropbox, revele uma camada por vez e pergunte antes de abrir a seguinte: "o que vocês fariam no lugar deles?". A camada 3 (o vídeo de um produto que não existia) costuma provocar reação de "mas isso é trapaça" — é o melhor momento da aula. Conduza: não é trapaça porque ninguém pagou por nada; foi uma pergunta feita do jeito honesto, e quem se inscreveu recebeu o produto depois.

Não deixe o número da hipótese ficar para depois. Circule exigindo o número escrito. O trio que resiste é justamente o que mais precisa.

Recolher os briefings (foto serve) — sem eles a aula 10 começa no vazio. Se algum trio não terminou, marque para completar até a próxima; o briefing incompleto trava dois alunos, não um.
:::
