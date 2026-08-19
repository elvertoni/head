---
titulo: "Movimento com propósito: o que leva o olho até o botão"
tema: Transições, estados e acessibilidade de movimento
disciplina: programacao-front-end
serie: 2ª
prerequisitos: [Página responsiva e testada no celular na Aula 14]
objetivos:
  - Justificar cada movimento pela função que ele cumpre na página
  - Usar transition para suavizar a mudança entre estados
  - Aplicar transform para deslocar um elemento sem empurrar o layout
  - Dar estado visível de hover e de foco ao botão principal
  - Respeitar a preferência de movimento reduzido do sistema do usuário
trilha: landing-page-mvp
ordem: 15
slug: movimento-com-proposito
modo_origem: tema
fontes: []
revisao: false
status: aprovada
versao: 1
atualizado_em: 2026-08-18
---

Passa o mouse por cima do seu botão. Não acontece nada. O cursor vira uma mãozinha e só — nenhum sinal de que aquilo ali é a coisa mais importante da página, nenhuma resposta ao seu gesto. Agora repara em qualquer aplicativo que você usa: tudo reage. O botão escurece um pouco, o card sobe um milímetro, o menu desliza em vez de aparecer do nada. Não é enfeite, e é aqui que mora a confusão desta aula — a maior parte da animação que existe na web é ruído, e um pouquinho dela é o que faz o produto parecer vivo. Hoje a gente aprende a diferença, e aplica só a parte que serve.

## Objetivos

Ao final desta aula, você será capaz de:

- Decidir se um movimento **cumpre função** ou é só efeito — e cortar o segundo.
- Usar **`transition`** para suavizar a passagem entre estados.
- Usar **`transform`** para deslocar um elemento sem bagunçar o resto da página.
- Dar ao botão principal um estado de **hover** e um estado de **foco** visíveis.
- Respeitar quem configurou o aparelho para **reduzir movimento**.

## Pré-requisitos

A página das aulas 10 a 11, responsiva e testada no celular. Hoje mexemos só em aparência e resposta ao gesto — nada de estrutura.

## Desenvolvimento

### Movimento é informação, não enfeite

Existe um teste único, e ele é severo: **o que este movimento informa?**

Movimento que informa tem sempre uma dessas três funções. Ele **confirma** que o sistema recebeu o seu gesto — você tocou e a coisa reagiu. Ele **conduz** o olho para onde a página quer que você olhe. Ou ele **explica uma mudança**, mostrando de onde algo veio, para você não perder o fio quando a tela muda.

Movimento fora dessas três é decoração, e decoração cobra caro: rouba atenção do botão, atrasa quem já sabia o que queria fazer, e no celular ainda gasta bateria. A regra da aula, então: **movimento que não leva o olho até a ação é ruído.**

:::importante Rápido é elegante
A duração certa para as transições desta página está entre 150 e 300 milissegundos — mais ou menos um piscar de olhos. Parece pouquíssimo e é exatamente o ponto: nessa faixa a pessoa **sente** a resposta sem **esperar** por ela. Passando de meio segundo, o movimento deixa de acompanhar o gesto e começa a atrapalhar quem já decidiu o que fazer. Amador demora; profissional é rápido.
:::

### `transition`: a diferença entre pular e mudar

Sem transição, mudança de estado é um corte seco: o botão simplesmente **é** de outra cor no quadro seguinte. Com transição, o navegador desenha os passos intermediários.

```css
a.botao {
  background-color: var(--cor-destaque);
  transition: background-color 200ms ease, transform 200ms ease;
}

a.botao:hover {
  background-color: #24583e;   /* um tom mais escuro do destaque */
}
```

A propriedade se declara no estado **normal**, não no `:hover` — assim ela vale nos dois sentidos, na ida e na volta. E ela **nomeia** o que vai ser animado. Existe o atalho `transition: all`, e é melhor não pegar o hábito: ele manda o navegador vigiar todas as propriedades, incluindo as caras, e é uma das causas comuns de animação travada em celular mais simples.

### `transform`: mover sem empurrar o resto

Para fazer um card subir um pouquinho no hover, o caminho intuitivo seria mexer na margem ou na posição. Funciona mal: mudar margem faz o navegador **recalcular o layout inteiro** — as posições dos elementos vizinhos mudam junto, e o resultado é aquele efeito de página tremendo.

`transform` resolve porque ele desloca o elemento **visualmente**, sem alterar o espaço que ele ocupa. O vizinho nem fica sabendo.

```css
.card {
  transition: transform 200ms ease, box-shadow 200ms ease;
}

.card:hover {
  transform: translateY(-4px);              /* sobe 4px */
  box-shadow: 0 8px 20px rgba(0,0,0,0.10);  /* e a sombra cresce junto */
}
```

Os três movimentos que resolvem quase tudo: `translateY()` para deslocar, `scale()` para crescer de leve — `1.02` já se percebe, `1.2` é exagero — e `rotate()`, que numa landing page raramente tem função.

### Quem toca, quem clica e quem usa teclado

```diagrama-progressivo
titulo: O mesmo botão, quatro pessoas diferentes
camadas:
  - rotulo: Em repouso
    conteudo: "O botão precisa parecer clicável antes de qualquer interação — cor de destaque, respiro interno generoso e cantos arredondados. Se ele só se revela quando o mouse chega, quem nunca passou o mouse por ali nunca soube que era um botão."
  - rotulo: Quem usa mouse
    conteudo: "Ao passar o cursor, o hover confirma que aquele elemento responde. É a única dica que essa pessoa recebe antes de clicar, e é barata de dar — uma mudança de tom já resolve."
  - rotulo: Quem navega pelo teclado
    conteudo: "Sem mouse, a pessoa percorre a página com a tecla Tab e precisa enxergar onde está. Esse é o estado de foco, e ele é atendido por uma propriedade diferente da do hover. Sem foco visível, a navegação por teclado vira caminhar no escuro."
  - rotulo: Quem está no celular
    conteudo: "Aqui está a virada — no toque não existe hover. O dedo não paira sobre nada, ele encosta e já ativa. Todo efeito que você amarrou ao hover simplesmente não existe para essa pessoa."
  - rotulo: A conclusão que muda o projeto de vocês
    conteudo: "Como o teste da aula 17 será feito no celular, hover é enfeite para quem vai avaliar, não informação. Ele pode existir, mas nada essencial pode depender dele. O botão precisa se anunciar em repouso — e o estado de foco precisa existir de verdade, porque nele há gente que depende."
```

:::atencao A borda feia que não deve ser apagada
Quando um elemento recebe foco, o navegador desenha um contorno em volta dele. Muita gente acha aquilo feio e resolve com uma linha: `outline: none`. É provavelmente a alteração mais destrutiva que se faz em CSS por motivo estético. Quem navega por teclado — por deficiência motora, por preferência, ou porque o mouse quebrou — perde completamente a noção de onde está na página: a tecla Tab continua avançando, e nada na tela indica para onde. Diagnóstico: aperte Tab várias vezes na sua página e olhe a tela. Se você não consegue apontar com o dedo onde está o foco, a sua página está quebrada para essas pessoas. E a solução nunca é apagar — é **substituir** por um destaque melhor, usando `:focus-visible`, que aplica o realce só quando a navegação é por teclado, sem sujar o clique de mouse.
:::

```css
a.botao:focus-visible {
  outline: 3px solid var(--cor-texto);
  outline-offset: 3px;
}
```

:::curiosidade Movimento que passa mal
Nos ajustes de acessibilidade de qualquer celular existe uma opção chamada "reduzir movimento". Ela não é firula: para algumas pessoas, animação de tela — sobretudo deslocamento amplo e paralaxe — provoca sintomas físicos reais, como enjoo, tontura e dor de cabeça, ligados ao mesmo mecanismo do enjoo de carro. O CSS consegue **ler** essa preferência do sistema, e uma página bem feita a respeita. É um caso raro e bonito: uma coisa que custa quatro linhas e literalmente evita que alguém passe mal usando o seu site.
:::

```css
@media (prefers-reduced-motion: reduce) {
  * {
    transition-duration: 0.01ms !important;
    animation-duration: 0.01ms !important;
  }
}
```

:::dica O que separa interface boa de interface bonita
Em qualquer equipe de produto séria, movimento é assunto de acessibilidade antes de ser assunto de estética, e o padrão é justamente este: elementos interativos precisam ter estado visível, animação é curta e discreta, e a preferência do sistema é respeitada. Quem chega numa entrevista sabendo o que é `:focus-visible` e `prefers-reduced-motion` demonstra algo raro em quem está começando — que aprendeu a pensar em quem usa a página, não só em como ela aparece. É um assunto barato de dominar e muito caro de improvisar depois.
:::

## Prática

**Dar vida à página (~15 min).** Acrescente ao final do `estilo.css`.

**1. O botão principal — os três estados:**

```css
#hero a, #comecar a {
  display: inline-block;
  background-color: var(--cor-destaque);
  color: #ffffff;
  padding: 14px 28px;
  border-radius: 8px;
  text-decoration: none;
  font-weight: 600;
  transition: background-color 200ms ease, transform 200ms ease;
}

#hero a:hover, #comecar a:hover {
  background-color: #24583e;
  transform: translateY(-2px);
}

#hero a:focus-visible, #comecar a:focus-visible {
  outline: 3px solid var(--cor-texto);
  outline-offset: 3px;
}
```

**2. Os cards respondendo:**

```css
.card {
  transition: transform 200ms ease, box-shadow 200ms ease;
}

.card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.10);
}
```

**3. Uma entrada discreta no hero** — aparece subindo de leve, uma vez só:

```css
#hero h1, #hero p, #hero a {
  animation: entrada 400ms ease both;
}

@keyframes entrada {
  from { opacity: 0; transform: translateY(12px); }
  to   { opacity: 1; transform: translateY(0); }
}
```

**4. E a linha que respeita quem pediu menos movimento** — no fim do arquivo:

```css
@media (prefers-reduced-motion: reduce) {
  * {
    transition-duration: 0.01ms !important;
    animation-duration: 0.01ms !important;
  }
}
```

**5. Os dois testes obrigatórios (3 min):**

- **Teclado:** aperte `Tab` várias vezes e confirme que **sempre dá para ver onde você está**.
- **Celular:** abra o link no aparelho e verifique que o botão se anuncia sozinho, **sem depender de hover**.

**Entrega:** página republicada, aprovada nos dois testes. E uma pergunta a se fazer honestamente para cada efeito que você adicionou: *isso leva o olho até o botão?* Se não leva, apague — apagar hoje conta como acerto.

## Avaliação

```quiz
- pergunta: Por que usar transform translateY em vez de mudar a margem para fazer um card subir no hover?
  alternativas:
    - texto: Porque margem não aceita valores negativos
    - texto: "Porque transform desloca o elemento visualmente sem alterar o espaço que ele ocupa, então os vizinhos não são reposicionados"
      correta: true
    - texto: Porque transform é a única propriedade que funciona com transition
    - texto: Porque margem não funciona dentro de um container Grid
  feedback: >
    Mexer na margem obriga o navegador a recalcular a posição dos elementos ao
    redor, e a página treme. transform só muda a aparência do elemento — o espaço
    reservado a ele continua o mesmo.
- pergunta: Por que não se pode depender de :hover para indicar que um elemento é clicável?
  alternativas:
    - texto: Porque hover deixa a página mais lenta em celulares
    - texto: "Porque em telas de toque não existe hover — o dedo não paira, ele já ativa; e quem navega por teclado também nunca o aciona"
      correta: true
    - texto: Porque hover não funciona em links, apenas em botões
    - texto: Porque hover é uma funcionalidade obsoleta do CSS
  feedback: >
    Hover é um bônus para quem usa mouse. O elemento precisa se anunciar como
    clicável já em repouso, e precisa ter estado de foco para quem usa teclado.
    Como o teste do projeto será no celular, isso deixa de ser detalhe.
- pergunta: Qual é o problema de escrever outline none nos elementos interativos?
  alternativas:
    - texto: Nenhum, é a forma correta de remover o contorno padrão
    - texto: "Quem navega por teclado perde a indicação visual de onde está na página, e a navegação fica impossível"
      correta: true
    - texto: O CSS deixa de validar e o navegador ignora o arquivo
    - texto: O contorno volta a aparecer no celular
  feedback: >
    O contorno é a única pista de posição para quem usa Tab. Se ele incomoda
    esteticamente, o caminho é substituí-lo por um realce melhor com
    focus-visible — nunca simplesmente apagá-lo.
```

## Fechamento

O que ficou de hoje:

- **Movimento informa ou é ruído.** Ele confirma o gesto, conduz o olho ou explica uma mudança — fora disso, sai.
- **Entre 150 e 300 milissegundos**: sente-se a resposta sem esperar por ela.
- **`transition` se declara no estado normal** e nomeia o que anima; `transition: all` custa caro.
- **`transform` move sem empurrar o layout** — margem e posição fazem a página tremer.
- **No toque não existe hover.** O botão se anuncia em repouso; o foco existe para quem usa teclado e nunca se apaga.
- **`prefers-reduced-motion`**: quatro linhas que evitam que alguém passe mal na sua página.

**Próxima aula:** o primeiro JavaScript do projeto — e vai ser pouco de propósito. Três funcionalidades, cerca de vinte e cinco linhas no total, todas resolvendo problemas que vocês já têm: o menu que não cabe no celular, o botão que está longe demais depois de rolar, e o jeito de passar o link para as cinco pessoas do teste da aula 17.

:::roteiro
Abra com dois sites no projetor: um sem nenhuma resposta ao gesto e outro bem feito. Não explique — só passe o mouse nos dois. A turma nomeia a diferença sozinha, e aí você já tem o vocabulário da aula.

O risco desta aula é o oposto do de sempre: aqui o aluno faz **demais**. Vai aparecer card girando, botão pulsando, texto entrando de todos os lados. Estabeleça a pergunta única desde o início — "isso leva o olho até o botão?" — e use como resposta padrão o resto da aula. Dizer que apagar conta como acerto muda o comportamento da turma.

A camada 4 do diagrama, "no toque não existe hover", costuma ser choque, porque eles acabaram de investir no hover. Deixe o choque acontecer: é o que garante que o botão seja desenhado para se anunciar em repouso.

O teste do Tab funciona melhor coletivo. Peça que todos apertem Tab cinco vezes e digam onde está o foco. Quem não achar descobre na hora por que a borda existe.

Se sobrar tempo, ative "reduzir movimento" nos ajustes de acessibilidade de um celular e recarregue a página com a media query aplicada. Ver a preferência do sistema mudando a página é o tipo de coisa que a turma não esquece.

Guarde 5 min finais para a poda: peça que cada um apague um efeito que não passou no teste. É a parte mais formativa da aula e a primeira a ser sacrificada se você deixar.
:::
