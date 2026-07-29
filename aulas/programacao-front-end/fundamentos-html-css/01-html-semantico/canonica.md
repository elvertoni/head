---
titulo: "HTML semântico: por que <div> não conta a história toda"
tema: HTML Semântico
disciplina: programacao-front-end
serie: 3ª
prerequisitos: [Estrutura básica de uma página HTML, tags e aninhamento]
objetivos:
  - Explicar por que tags semânticas comunicam significado além da aparência visual
  - Diferenciar uma div genérica de sua tag semântica equivalente (header, nav, main, article, aside, footer, section)
  - Reescrever um layout feito só com div usando tags semânticas, sem alterar o resultado visual
  - Relacionar HTML semântico a acessibilidade (leitor de tela) e SEO
trilha: fundamentos-html-css
ordem: 1
slug: html-semantico
modo_origem: material
fontes: [fontes/FLEXBOX.pdf]
revisao: false
status: aprovada
versao: 1
atualizado_em: 2026-07-29
---

Abre o código-fonte de um site qualquer — clique direito, "Ver código-fonte da página", ou `Ctrl+Shift+I` e aba Elements. Se o site for bem feito, você vai ver palavras como `<header>`, `<nav>`, `<main>`, `<footer>` antes mesmo de olhar uma linha de CSS. Isso não é estilo. É o site contando pra qualquer máquina que ler aquele HTML — navegador, leitor de tela, robô do Google — **o que cada pedaço da página significa**, não só onde ele fica na tela.

## Objetivos

Ao final desta aula, você será capaz de:

- Explicar por que uma `<div>` não carrega significado nenhum sozinha.
- Reconhecer e usar as principais tags semânticas: `header`, `nav`, `main`, `article`, `aside`, `footer`, `section`.
- Pegar um layout feito só com `<div>` e reescrevê-lo com tags semânticas, mantendo o CSS e o visual **idênticos**.
- Explicar por que isso importa pra acessibilidade e pra SEO, não só pra organização do código.

## Pré-requisitos

Você precisa saber montar uma página HTML básica (tags abrindo/fechando, atributos como `class` e `id`, aninhamento de elementos). Não precisa saber Flexbox a fundo — vamos reaproveitar um exercício de layout que você já viu, só que agora olhando pro HTML, não pro CSS.

## Desenvolvimento

### O problema da div-soup

`<div>` é a tag mais genérica do HTML. Ela não tem regra: pode virar cabeçalho, rodapé, barra lateral, o que você quiser — porque ela **não significa nada por conta própria**. É uma caixa vazia. Todo o significado que ela carrega vem do `class` ou do `id` que você grudou nela: `class="header"`, `class="nav"`, `class="footer"`.

O problema é que esse significado só existe **pra você**, que escreveu o nome da classe, e pro CSS, que sabe procurar por `.header { }`. Pro navegador, pro leitor de tela e pro Google, `<div class="header">` e `<div class="qualquer-coisa-123">` são **exatamente a mesma coisa**: uma caixa sem nome. Uma página inteira montada só com `<div>` empilhada dentro de `<div>` tem um apelido conhecido: **div-soup** (sopa de divs) — visualmente pode estar perfeita, mas por dentro é um monte de caixas anônimas.

:::conceito Elemento semântico
Uma tag é **semântica** quando o próprio nome dela já diz o que aquele pedaço da página *é*, independente de qualquer `class`. `<nav>` é sempre navegação. `<footer>` é sempre rodapé. Isso vale pro navegador, pro leitor de tela e pra qualquer ferramenta que leia o HTML — não só pra quem escreveu o código.
:::

### O catálogo que resolve isso

O HTML5 trouxe um conjunto de tags feitas exatamente pra substituir a div genérica nos papéis que toda página tem:

| Tag | Papel na página |
|---|---|
| `<header>` | Cabeçalho — logo, título, boas-vindas |
| `<nav>` | Bloco de links de navegação (menu) |
| `<main>` | Conteúdo principal e único da página |
| `<article>` | Um conteúdo que faz sentido sozinho, fora do resto (um post, uma notícia) |
| `<aside>` | Conteúdo relacionado, mas secundário (barra lateral, destaque) |
| `<footer>` | Rodapé — créditos, contato, links legais |
| `<section>` | Um agrupamento temático dentro de `main` ou `article`, quando nenhuma tag mais específica se encaixa |

Repara: nenhuma dessas tags muda como a página **parece**. `<header>` por padrão se comporta igual a uma `<div>` (ocupa a largura toda, quebra linha antes e depois). A diferença inteira é de **significado**, não de aparência — e é justamente por isso que trocar de uma pra outra é seguro.

:::exemplo O layout do Flexbox, sem nome nenhum
Lembra do exercício de reproduzir este layout com `display: flex`?

```html
<!-- como o material de Flexbox ensina -->
<div class="flex-container">
  <div class="header">Header</div>
  <div class="corpo">
    <div class="article">Article</div>
    <div class="aside">Aside</div>
    <div class="nav">Nav</div>
  </div>
  <div class="footer">Footer</div>
</div>
```

Visualmente perfeito: header em cima, três colunas no meio, footer embaixo. Mas repara — o nome "header" ali é só uma palavra dentro de um atributo `class`. Pro navegador, é uma `<div>` qualquer chamada de qualquer jeito. Se alguém trocar `class="header"` por `class="topo-da-pagina"`, nada quebra e nada muda — porque **nada ali sabia, de verdade, que aquilo era um cabeçalho**.
:::

Agora troca só as tags, mantendo as classes exatamente iguais — o CSS nem percebe a diferença:

```html
<!-- mesmo layout, agora com significado -->
<div class="flex-container">
  <header class="header">Header</header>
  <div class="corpo">
    <article class="article">Article</article>
    <aside class="aside">Aside</aside>
    <nav class="nav">Nav</nav>
  </div>
  <footer class="footer">Footer</footer>
</div>
```

O `display: flex` no `.flex-container` continua funcionando exatamente igual, porque `header`, `article`, `aside`, `footer` e `nav` são todos elementos de bloco por padrão — do ponto de vista do Flexbox, é como se nada tivesse mudado. Do ponto de vista de quem (ou do que) lê a página, mudou tudo.

:::atencao Erro comum
Um erro comum é achar que trocar `<div class="header">` por `<header class="header">` é redundante ou é "frescura". Não é: o `class="header"` é o nome que **você e o CSS** usam; a tag `<header>` é o nome que **o navegador, o leitor de tela e o Google** usam. São duas informações diferentes, guardadas em dois lugares diferentes, e as duas continuam necessárias — uma não substitui a outra.
:::

### Por que isso importa fora da tela

A parte que não aparece pra quem enxerga é onde a semântica prova o valor dela.

Um aluno com deficiência visual navega a web com um **leitor de tela** — um programa que lê a página em voz alta. Leitores de tela têm um atalho pra pular direto pros "landmarks" (marcos) da página: pula pro `<nav>`, pula pro `<main>`, pula pro `<footer>`. Numa página feita só de `<div>`, esse atalho **não existe** — o leitor de tela lê tudo em sequência, do topo ao fim, sem conseguir pular pra "onde está o conteúdo principal". A pessoa fica presa ouvindo o menu inteiro toda vez que abre uma página nova do mesmo site.

```diagrama-progressivo
titulo: Como o leitor de tela navega uma página
camadas:
  - rotulo: Só div
    conteudo: "O leitor de tela encontra uma sequência de caixas sem nome. Só resta ler tudo, de cima a baixo, sem atalho."
  - rotulo: Com tags semânticas
    conteudo: "O leitor de tela reconhece header, nav, main, footer como marcos. O usuário pede 'pular pro conteúdo principal' e chega direto no main."
  - rotulo: O ganho real
    conteudo: "A mesma pessoa que levava 30 segundos ouvindo o menu inteiro agora pula pro artigo em 2 segundos — sem o site mudar de aparência nem uma linha de CSS."
```

O Google funciona parecido: o robô que indexa seu site (o *crawler*) usa `<article>`, `<h1>` e `<main>` pra entender qual é o conteúdo de verdade da página, separado de menu e rodapé. Um site em div-soup entrega tudo no mesmo nível de importância pro robô; um site semântico diz "isto aqui é o que importa".

:::importante O ponto-chave
Visual idêntico **não** significa código idêntico. Duas páginas podem parecer gêmeas na tela e serem completamente diferentes pra quem não enxerga a tela — seja uma pessoa com deficiência visual, seja um robô de busca. Semântica é uma camada de informação que só existe se você escrever a tag certa; nenhum CSS "espertinho" compensa a falta dela.
:::

:::dica Onde você vai ver isso de novo
Da próxima vez que inspecionar (`Ctrl+Shift+I`) um site grande — G1, Mercado Livre, GitHub — procura por `header`, `nav`, `main`, `article` na aba Elements. Você vai achar em praticamente todos. Semântica não é purismo de curso técnico: é prática de mercado.
:::

## Prática

**Reescreva o layout do Flexbox com tags semânticas (VSCode, ~15 min).**

Pegue o exercício de layout que você já fez com `display: flex` (header em cima, article/aside/nav no meio, footer embaixo — o mesmo do material de Flexbox). Sem mudar nenhuma propriedade de CSS:

1. Troque cada `<div class="...">` de papel fixo (header, article, aside, nav, footer) pela tag semântica correspondente, **mantendo o `class` como estava**.
2. Rode no navegador e confira: o layout visual precisa continuar **idêntico** ao de antes.
3. Abra o inspecionar de elementos e confirme que agora aparecem `<header>`, `<article>`, `<aside>`, `<nav>`, `<footer>` na árvore — não mais `<div>` genérica.
4. Bônus: o `<div class="corpo">` que agrupa article/aside/nav pode virar `<div>` mesmo (não tem tag semântica óbvia pra "container do meio"), ou virar `<section>` se você achar que é um agrupamento temático. Justifique sua escolha em um comentário no HTML.

## Avaliação

```quiz
- pergunta: Por que trocar <div class="header"> por <header class="header"> muda alguma coisa, se o CSS continua igual?
  alternativas:
    - texto: "Porque muda o layout visual da página"
    - texto: "Porque a tag <header> dá significado à caixa pra navegador, leitor de tela e buscador — não só pro CSS"
      correta: true
    - texto: "Não muda nada, é só estética de código"
    - texto: "Porque <header> é mais rápido de carregar que <div>"
  feedback: >
    O visual não muda porque header também é elemento de bloco por padrão. O que
    muda é que agora existe uma informação de significado que só o nome da tag
    carrega — o class continua servindo só pro CSS.
- pergunta: Um leitor de tela navega uma página feita só com <div>. O que acontece?
  alternativas:
    - texto: "Ele detecta os nomes das classes e pula direto pro conteúdo principal"
    - texto: "Ele não consegue ler a página"
    - texto: "Ele lê tudo em sequência, sem atalho pra pular pro conteúdo principal"
      correta: true
    - texto: "Ele avisa o usuário que o site tem um erro"
  feedback: >
    Sem tags semânticas não existem "landmarks" pra pular. O usuário fica preso
    ouvindo a página inteira em ordem, sem conseguir saltar direto pro main.
- pergunta: Qual tag é a mais indicada pra um bloco de links de navegação (o menu do site)?
  alternativas:
    - texto: "<section>"
    - texto: "<aside>"
    - texto: "<nav>"
      correta: true
    - texto: "<article>"
  feedback: >
    nav é a tag feita especificamente pra blocos de navegação — é a que os
    leitores de tela reconhecem como atalho de menu.
```

## Fechamento

Hoje você viu que:

- `<div>` não tem significado nenhum sozinha — todo "nome" que ela carrega vem do `class`, que só o CSS entende.
- Tags semânticas (`header`, `nav`, `main`, `article`, `aside`, `footer`, `section`) dão significado real, lido por navegador, leitor de tela e buscador.
- Trocar `<div>` por tag semântica **não muda o visual nem quebra o CSS** — ambos continuam se comportando como elemento de bloco.
- Isso importa de verdade pra quem usa leitor de tela (navegação por atalho) e pra SEO (o robô entende o que é conteúdo principal).

**Próxima aula:** e quando o layout precisa de um formulário — de login, de contato, de busca? HTML também tem tags semânticas pra isso, e é aí que a maioria dos sites erra feio na acessibilidade.

:::roteiro
Abrir pedindo pra um aluno inspecionar (F12) o site que ele mais usa no celular/PC — provavelmente vai achar header/nav/main na hora. Isso ancora que não é "coisa de curso", é prática real. No trecho da div-soup, resistir a explicar tudo de uma vez: perguntar "e se eu trocar o nome dessa classe, o que quebra?" antes de responder — deixa a turma perceber sozinha que nada quebra, porque nada ali sabia que era um cabeçalho de verdade. Na demonstração do leitor de tela, se der, mostrar de fato um leitor de tela (VoiceOver/NVDA/ChromeVox) navegando uma página com e sem semântica — o efeito "uau" é maior ao vivo do que descrito. Reservar uns 15 min pra prática — é o momento em que a ficha cai de verdade, quando o aluno vê o próprio layout do Flexbox virar semântico na tela dele. Fechar com o quiz, sem pressa, comentando o feedback de cada questão em voz alta.
:::
