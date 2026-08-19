---
titulo: "A ossatura: toda landing do mundo tem o mesmo esqueleto"
tema: Estrutura semântica de uma landing page
disciplina: programacao-front-end
serie: 2ª
prerequisitos: [Criar um arquivo .html no VSCode e abrir no navegador, Saber que HTML é feito de tags que abrem e fecham, Briefing da Aula 08 e kit de copy da Aula 09]
objetivos:
  - Identificar as cinco seções que se repetem em toda landing page e a ordem entre elas
  - Explicar o que é a dobra e o que precisa caber nela
  - Escolher a tag semântica correta para cada parte da página em vez de usar div
  - Publicar a página e obter um endereço público funcionando
trilha: landing-page-mvp
ordem: 10
slug: a-ossatura-da-landing
modo_origem: tema
fontes: []
revisao: false
status: aprovada
versao: 1
atualizado_em: 2026-08-18
---

Abre agora, no celular, os três últimos sites que tentaram te vender alguma coisa — um tênis, um curso, um jogo. Ignora as cores e as fotos e olha só a forma. Você vai ver a mesma coisa nos três: uma frase enorme no topo com um botão embaixo, depois um trecho contando por que aquilo presta, depois uma prova de que não é conversa, e no fim o mesmo botão de novo. Não é falta de criatividade. É que essa ordem responde, na sequência certa, às cinco perguntas que você faz sem perceber quando abre um link. Hoje vocês montam esse esqueleto com o texto do próprio projeto — e saem daqui com o endereço no ar.

## Objetivos

Ao final desta aula, você será capaz de:

- Reconhecer as **cinco seções** que toda landing page tem, e por que a ordem entre elas não é aleatória.
- Explicar o que é a **dobra** e decidir o que precisa caber nela.
- Usar a **tag semântica** certa para cada parte, em vez de empilhar `<div>`.
- **Publicar** a página e sair da aula com um link que abre no celular de qualquer pessoa.

## Pré-requisitos

Saber criar um arquivo `.html` no VSCode, salvar e abrir no navegador; e saber que uma tag abre (`<p>`) e fecha (`</p>`), podendo ter outras dentro. Nada além disso — o CSS começa só na próxima aula, e hoje a página vai ficar **feia de propósito**.

Traga o **briefing** da aula 08 e o **kit de copy** da aula 09. Sem eles você vai passar a aula inventando texto em vez de aprender estrutura. Quem estiver sem, use o exemplo do fim da Prática e substitua depois.

## Desenvolvimento

### O esqueleto que se repete em todo site que vende

Na aula 09 vocês viram as cinco perguntas que o visitante faz em ordem: *que coisa é essa? isso é para mim? o que eu ganho? por que acreditar? o que eu faço agora?* Uma landing page é literalmente essa lista virada de pé — cada pergunta vira uma faixa horizontal da página, na mesma sequência.

| Faixa | Responde | O que vai dentro |
|---|---|---|
| **Topo** | *Que site é esse?* | Nome do produto e um menu curto |
| **Hero** | *Que coisa é essa? É para mim?* | Headline, subheadline e o botão |
| **Benefícios** | *O que eu ganho?* | Os três benefícios do kit de copy |
| **Prova** | *Por que eu acreditaria?* | Número, depoimento, print, "como as pessoas se viram hoje" |
| **Chamada final** | *E agora?* | O mesmo botão, repetido |

"Hero" é o nome que se usa no mercado para o primeiro bloco grande, o que ocupa a tela inteira quando a página abre. Não tem tradução boa em português e você vai ouvir esse nome a vida inteira — decore.

A ordem importa porque as perguntas são encadeadas: ninguém quer saber do benefício antes de descobrir o assunto, e ninguém repara na prova antes de querer o benefício. Página que começa apresentando a equipe está respondendo a uma pergunta que ninguém fez.

### A dobra: o único pedaço garantido

:::conceito A dobra
**A dobra** é a linha onde a tela acaba quando a página abre, antes de qualquer rolagem. O que está acima dela é a única parte que **todo mundo** vê. O que está abaixo só é visto por quem decidiu continuar — e essa decisão é tomada com base no que está acima. O nome vem do jornal impresso, que ficava dobrado na banca mostrando só a metade de cima: era ali que a manchete tinha que convencer alguém a comprar.
:::

No celular, a dobra é impiedosa: cabe pouco mais que a headline, uma linha de apoio e o botão. Então a regra prática é essa — **se a pessoa só puder ler uma frase da sua página inteira, qual é?** Essa frase vai na dobra. Tudo o mais desce.

:::importante Ninguém rola por educação
É tentador pensar "quem se interessar vai descer e ler o resto". Não vai. A rolagem não é o começo da leitura, é a **recompensa** por a dobra ter funcionado. Página cuja primeira tela não diz do que se trata não perde só o topo: perde a página inteira, porque o resto nunca é aberto.
:::

### Tags que dizem o que a coisa é

Dá para montar essa página inteira usando só `<div>`. Funciona, o navegador desenha igual, e o resultado na tela é idêntico. E ainda assim é a escolha errada — porque a tela não é o único lugar onde a sua página é lida.

:::conceito Elemento semântico
Uma tag é **semântica** quando o nome dela já diz o que aquele pedaço da página **é**, sem depender de `class` nenhuma. `<nav>` é sempre navegação. `<footer>` é sempre rodapé. `<div>` é uma caixa sem nome: só existe significado para quem escreveu, e some para todo o resto.
:::

```diagrama-progressivo
titulo: A mesma página, quatro leitores diferentes
camadas:
  - rotulo: Você, olhando a tela
    conteudo: "Para você não muda nada. Div ou tag semântica, o navegador desenha o mesmo retângulo no mesmo lugar. É por isso que o erro passa despercebido por meses — visualmente não existe sintoma nenhum."
  - rotulo: Uma pessoa cega, usando leitor de tela
    conteudo: "O leitor de tela anuncia as regiões da página e permite pular direto para o conteúdo principal. Com tags semânticas, ela ouve navegação, conteúdo principal, rodapé, e escolhe. Com div, ela ouve caixa, caixa, caixa — e tem que atravessar tudo na unha."
  - rotulo: O robô do Google
    conteudo: "O buscador tenta entender do que a página trata para decidir a quem mostrá-la. Título dentro de h1 e conteúdo dentro de main são pistas fortes. Uma pilha de div não informa nada, e a página compete em desvantagem com outra que informou."
  - rotulo: O colega que vai mexer no seu código
    conteudo: "Daqui a três semanas, alguém abre seu arquivo para trocar um texto. Com header, main e footer, ele acha o lugar em segundos. Com quarenta div aninhadas, ele conta chaves com o dedo na tela. Esse colega, na maior parte das vezes, é você mesmo."
```

O catálogo que resolve isso é curto:

| Tag | Papel |
|---|---|
| `<header>` | Cabeçalho do topo — nome do produto |
| `<nav>` | Bloco de links de navegação |
| `<main>` | O conteúdo principal — **um por página** |
| `<section>` | Cada faixa temática da página |
| `<footer>` | Rodapé |
| `<h1>` | O título mais importante — **um por página**, e é a headline |
| `<h2>` | Título de cada seção |

Os dois "um por página" não são frescura de organização: `<main>` é o que permite pular direto ao conteúdo, e `<h1>` é o que declara o assunto da página. Repetidos, os dois perdem a função — dizer que tudo é principal é o mesmo que não dizer nada.

## Prática

**Montar e publicar (~15 min).** Crie a pasta do projeto e, dentro dela, o arquivo `index.html`. O nome é obrigatório e em letras minúsculas — é ele que o servidor procura sozinho.

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>NOME DO PRODUTO — o que ele resolve</title>
</head>
<body>

  <header>
    <p>NomeDoProduto</p>
    <nav>
      <a href="#beneficios">Benefícios</a>
      <a href="#comecar">Começar</a>
    </nav>
  </header>

  <main>

    <section id="hero">
      <h1>SUA HEADLINE AQUI</h1>
      <p>Sua subheadline: para quem é ou como funciona.</p>
      <a href="#comecar">SUA CHAMADA PARA AÇÃO</a>
    </section>

    <section id="beneficios">
      <h2>O que muda para você</h2>
      <h3>Benefício 1</h3>
      <p>Uma frase explicando.</p>
      <h3>Benefício 2</h3>
      <p>Uma frase explicando.</p>
      <h3>Benefício 3</h3>
      <p>Uma frase explicando.</p>
    </section>

    <section id="prova">
      <h2>Não é só a gente falando</h2>
      <p>Sua prova: número, depoimento ou como as pessoas se viram hoje.</p>
    </section>

    <section id="comecar">
      <h2>Pronto para começar?</h2>
      <a href="#comecar">SUA CHAMADA PARA AÇÃO</a>
    </section>

  </main>

  <footer>
    <p>Projeto de NOMES DO TRIO — 2A — Curso Técnico em Desenvolvimento de Sistemas</p>
  </footer>

</body>
</html>
```

Troque **todo** texto em maiúsculas pelo do seu kit de copy. Abra no navegador: vai estar horrível, sem cor, tudo empilhado. É exatamente o esperado — hoje é estrutura, não aparência.

**Publicar (últimos 5 min).** Crie o repositório no GitHub, envie o `index.html` para dentro dele, e ative a publicação em **Settings → Pages**, escolhendo a branch `main` e a pasta raiz. Em um ou dois minutos o endereço fica no ar. Se a turma já usa Git, faça pelo terminal com `commit` e `push`; se não, arraste o arquivo direto na página do repositório — o resultado é o mesmo.

**Entrega:** o link, anotado no caderno e mandado no grupo da turma. Guarde bem: ele é o mesmo até o fim do projeto, e é ele que vai ser testado com gente de verdade na aula 17.

:::atencao O erro que só aparece depois de publicar
Local funciona, publicado dá página em branco ou erro 404. Em quase todos os casos é o nome do arquivo. Três causas, em ordem de frequência: **maiúscula** (`Index.html` — o Windows não liga, o servidor liga, e para ele é outro arquivo); **extensão dupla escondida** (`index.html.txt`, quando o arquivo foi salvo pelo Bloco de Notas); e **acento ou espaço** no nome da pasta ou do arquivo (`página inicial.html`). Diagnóstico rápido: se abrindo o arquivo com dois cliques funciona e pelo link não, não procure erro no HTML — o HTML está certo. Olhe o nome. E adote a regra que vale para o resto da carreira: **tudo minúsculo, sem acento, sem espaço** — use hífen no lugar do espaço.
:::

:::dica Por que publicar hoje, com a página feia
Publicar cedo é hábito profissional, não pressa de escola. Times de produto colocam a versão feia no ar no primeiro dia porque publicar é a etapa que mais dá problema — nome errado, caminho errado, permissão errada —, e problema de publicação descoberto na véspera da entrega custa a entrega inteira. Descobrindo hoje, você tem sete aulas para resolver. Tem outro efeito, mais silencioso: a partir de agora seu projeto existe fora do seu computador. Toda melhoria que você fizer vai estar visível no mundo em dois minutos, e isso muda o tamanho do trabalho na sua cabeça.
:::

## Avaliação

```quiz
- pergunta: O que deve caber acima da dobra numa landing page aberta no celular?
  alternativas:
    - texto: A apresentação da equipe que desenvolveu o projeto
    - texto: "A headline, uma linha de apoio e o botão de ação"
      correta: true
    - texto: A lista completa das funcionalidades do produto
    - texto: O rodapé com os contatos e as redes sociais
  feedback: >
    A dobra é a única parte que todo mundo vê, e é ela que decide se a pessoa
    continua. Por isso leva a frase que você escolheria se pudesse mostrar só uma.
    O resto desce, porque só chega a quem a dobra convenceu.
- pergunta: Por que usar header, main e footer em vez de div, se o resultado na tela é idêntico?
  alternativas:
    - texto: Porque o navegador desenha a página mais rápido com tags semânticas
    - texto: Porque div está obsoleto e não deve mais ser usado
    - texto: "Porque a tela não é o único leitor da página — leitor de tela, buscador e quem for mexer no código dependem do nome da tag para saber o que cada parte é"
      correta: true
    - texto: Porque só com tags semânticas é possível aplicar CSS depois
  feedback: >
    Visualmente não muda nada, e é por isso que o erro passa despercebido. A
    diferença aparece para quem lê a página sem enxergá-la. E div continua sendo
    uma tag válida e útil — o problema é usá-la onde existe uma tag com nome.
- pergunta: A página abre certinho com dois cliques no computador, mas pelo link publicado dá erro 404. Qual é a causa mais provável?
  alternativas:
    - texto: Falta alguma tag de fechamento no HTML
    - texto: "O nome do arquivo — maiúscula, extensão dupla ou acento; o servidor diferencia maiúsculas de minúsculas e o Windows não"
      correta: true
    - texto: O navegador precisa ser atualizado
    - texto: A página está pesada demais para o servidor
  feedback: >
    Se abre local e não abre publicado, o HTML está correto — o que mudou foi
    quem procura o arquivo. Servidor procura exatamente index.html, em minúsculas.
    Index.html e index.html.txt são, para ele, outros arquivos.
```

## Fechamento

O que ficou de hoje:

- Toda landing page tem o mesmo esqueleto — **topo, hero, benefícios, prova, chamada final** — porque ele responde às cinco perguntas do visitante na ordem em que elas aparecem.
- **A dobra é o único pedaço garantido.** Se só uma frase for lida, ela precisa estar ali.
- **Tag semântica é informação para quem não vê a tela**: leitor de tela, buscador e o próximo programador — que costuma ser você.
- **Um `<main>` e um `<h1>` por página.** Dizer que tudo é principal é não dizer nada.
- Seu projeto tem **endereço público** desde hoje, feio e no ar.

**Próxima aula:** a página está estruturalmente certa e visualmente sofrível — parece documento do Word. Vamos resolver isso com menos CSS do que você imagina: **duas fontes e quatro cores**, definidas uma vez só num lugar só. É a aula em que o projeto passa a parecer um produto.

:::roteiro
Comece com o celular na mão da turma de verdade: peça que abram um site de vender qualquer coisa e descrevam a forma, não o conteúdo. Em dois minutos eles descobrem o padrão sozinhos, e a tabela das cinco faixas vira confirmação em vez de matéria nova.

O nome "hero" causa estranheza — aproveite. Termo de mercado dito na aula 10 gruda; dito na 14 soa como cobrança.

Sobre semântica, resista a justificar com organização. A turma não se move por isso. O que move é a camada 2 do diagrama, o leitor de tela — se puder, ative o narrador do sistema numa página só de div e depois na versão semântica. Trinta segundos disso valem a aula inteira.

Reserve os 5 min finais para publicar e **não deixe ninguém sair sem link**, mesmo com a página pela metade. Publicar é a etapa que trava, e travar hoje é barato. Circule já esperando os três erros de nome de arquivo — aparecem todos, sempre.

Se a turma nunca viu Git, não ensine Git hoje: arrastar o arquivo na interface do GitHub resolve e economiza vinte minutos que a aula não tem. Se já viu, cobre o push, que é reforço bem-vindo.

Anote os links num só lugar seu — planilha, papel, o que for. Você vai precisar deles na aula 17 e sempre falta um.
:::
