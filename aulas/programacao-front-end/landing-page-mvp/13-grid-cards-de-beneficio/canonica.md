---
titulo: "Grid: os três benefícios viram cards"
tema: Layout bidimensional com CSS Grid
disciplina: programacao-front-end
serie: 2ª
prerequisitos: [Topo e hero alinhados com Flexbox na Aula 12]
objetivos:
  - Decidir entre Flexbox e Grid a partir do número de dimensões do layout
  - Declarar colunas com grid-template-columns e a unidade fr
  - Usar repeat com auto-fit e minmax para obter reorganização automática sem media query
  - Construir um card como componente reutilizável
  - Diagnosticar o estouro de linha causado por largura em porcentagem somada ao gap
trilha: landing-page-mvp
ordem: 13
slug: grid-cards-de-beneficio
modo_origem: tema
fontes: []
revisao: false
status: aprovada
versao: 2
atualizado_em: 2026-08-21
---

Os três benefícios do kit de copy estão na página como uma lista: um embaixo do outro, cada um com seu titulozinho e seu parágrafo. Funciona, e não convence. Em toda landing page do mundo esses três aparecem **lado a lado**, em caixinhas iguais — porque três coisas em paralelo comunicam "escolha entre alternativas equivalentes", enquanto três coisas empilhadas comunicam "leia isso tudo". É a mesma informação dizendo coisas diferentes só pela forma. Hoje vocês montam esses cards, e de quebra levam um truque que faz eles se reorganizarem sozinhos no celular — sem escrever uma linha a mais para isso.

## Objetivos

Ao final desta aula, você será capaz de:

- Decidir entre **Flexbox e Grid** perguntando quantas dimensões o layout tem.
- Declarar colunas com **`grid-template-columns`** e entender a unidade **`fr`**.
- Usar **`repeat(auto-fit, minmax(...))`** para o layout se reorganizar sozinho.
- Montar um **card** como componente que se repete.
- Reconhecer o estouro de linha que aparece quando se mistura porcentagem com `gap`.

## Pré-requisitos

A página das aulas 10 a 12, com Flexbox aplicado no topo e no hero. Hoje o assunto é a seção de benefícios, que continua intocada.

## Desenvolvimento

### Uma dimensão, duas dimensões

Flexbox resolveu o topo porque o topo é uma **fila**: coisas numa direção só, com sobra de espaço para distribuir. É exatamente o que ele faz melhor.

Os cards são outro problema. Você não quer só três coisas em fila — quer três coisas de **largura igual**, **altura igual** e **espaço igual**, formando uma grade que se comporta bem quando a tela muda. Isso são duas dimensões, e para duas dimensões existe uma ferramenta feita sob medida.

:::conceito CSS Grid
**Grid** é o sistema de layout em que você declara, no container, a estrutura de **linhas e colunas** — e os filhos se encaixam nela. A diferença de mentalidade em relação ao Flexbox é essa: no Flex você descreve como a fila se distribui e o tamanho sai do conteúdo; no Grid você desenha a grade primeiro, e o conteúdo se acomoda dentro dela.
:::

A regra de bolso que os times usam: **uma direção, Flex; duas direções, Grid.** E não é escolha excludente — a mesma página usa os dois, e é comum um card feito com Grid ter Flexbox por dentro.

### Declarando colunas, e a unidade que só existe aqui

```css
.beneficios {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 24px;
}
```

Três valores, três colunas. E `fr` é uma unidade que não existe em nenhum outro lugar do CSS:

:::conceito A unidade fr
`fr` significa **fração do espaço livre**. `1fr 1fr 1fr` divide em três partes iguais o que sobrou **depois** de descontar o `gap` e as margens. É por isso que ela quase nunca estoura: enquanto a porcentagem é calculada sobre o total e ignora os espaços entre as colunas, `fr` reparte só o que de fato sobrou.
:::

`repeat()` encurta a escrita quando as colunas se repetem: `repeat(3, 1fr)` é idêntico a `1fr 1fr 1fr`.

:::atencao O estouro de linha que parece bug do navegador
A tentação é escrever `width: 33.33%` em cada card e um `gap: 24px` entre eles. Faz todo sentido — e quebra. Três vezes 33,33% já é 100% da largura, e os dois espaços de 24px são somados **por cima** disso: o total passa de 100%, o terceiro card não cabe e cai para a linha de baixo. O sintoma é característico e confunde: dois cards em cima, um sozinho embaixo, sem nenhuma regra pedindo isso. Diagnóstico: se o layout quebra ao acrescentar `gap`, o problema é a largura fixa em porcentagem. Troque por `fr` e o problema desaparece, porque `fr` só reparte o que sobrou depois do `gap`.
:::

### O truque que dispensa a media query

`repeat(3, 1fr)` tem um defeito sério: são **sempre** três colunas. Num celular de 360 pixels, cada card fica com cerca de 100 pixels — três colunas espremidas e ilegíveis. Você pode consertar isso com media query, e vai aprender media query na aula 14. Mas para grade de cards existe algo melhor, que resolve antes de o problema existir.

![Três telas de larguras diferentes alinhadas lado a lado, da mais larga à mais estreita, todas com a mesma linha de código idêntica escrita abaixo delas. Na tela larga os três cards aparecem em três colunas; na tela média, dois cards em cima e um embaixo; na tela estreita, os três empilhados em coluna única — nenhum card fica abaixo do piso de largura mínima definido, e o código não mudou entre as três situações.](img/auto-fit-conta-sozinho.png)

```diagrama-progressivo
titulo: Como o navegador decide quantos cards cabem na linha
camadas:
  - rotulo: A versão rígida
    conteudo: "Com repeat de 3 por 1fr, existem sempre três colunas, em qualquer largura. Num monitor fica ótimo. Num celular de 360 pixels, cada card recebe pouco mais de 100 pixels e o texto vira uma coluna de duas letras."
  - rotulo: Primeira metade do truque — um piso
    conteudo: "Com minmax de 250px até 1fr, cada coluna passa a ter uma regra dupla: nunca menor que 250 pixels, e podendo crescer até ocupar a fração de espaço que lhe cabe. O piso protege a legibilidade."
  - rotulo: Segunda metade — deixar o navegador contar
    conteudo: "Trocando o número 3 por auto-fit, você para de dizer quantas colunas existem. O navegador passa a calcular sozinho quantas colunas de pelo menos 250 pixels cabem na largura disponível, e cria exatamente essa quantidade."
  - rotulo: O mesmo código, três telas
    conteudo: "Num monitor largo cabem três colunas e os três cards ficam lado a lado. Num tablet cabem duas, e o terceiro card desce sozinho. Num celular cabe uma, e eles se empilham. Uma linha de CSS, nenhuma media query, e o layout nunca fica ilegível."
  - rotulo: Por que isso é diferente do que virá na aula 14
    conteudo: "Media query é você decidindo o ponto de virada e escrevendo regras diferentes para cada faixa de tela. Isto é o contrário — você declara a intenção, o piso de 250 pixels, e delega a contagem. Quando serve, é sempre a solução mais robusta, porque funciona em larguras que você nunca testou."
```

```css
.beneficios {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 24px;
}
```

Essa linha é uma das mais úteis de todo o CSS moderno, e vale decorar o formato: `repeat(auto-fit, minmax(LARGURA_MÍNIMA, 1fr))`.

### O card: um componente que se repete

Card não é uma tag — é um **padrão**: um pedaço de conteúdo autocontido, visualmente destacado do fundo, que se repete com a mesma aparência. Ele se constrói com quatro decisões:

| Decisão | Propriedade | Por quê |
|---|---|---|
| Respiro interno | `padding` | Texto colado na borda parece apertado e some |
| Separação do fundo | `background` ou `border` | O card precisa se distinguir da página |
| Cantos | `border-radius` | Canto reto parece caixa de sistema; arredondado parece produto |
| Peso | `box-shadow` (discreto) | Sugere que o card está acima do fundo |

Como cada benefício é um bloco de conteúdo que faz sentido sozinho, a tag correta é `<article>` — vale a mesma lógica semântica da aula 10.

:::dica Onde você vai reencontrar essa linha
Grade de cards é a estrutura mais reaproveitada da web: produto de loja virtual, vídeo em plataforma de streaming, publicação em rede social, painel de indicadores no trabalho. Todas são a mesma grade. Quem sai daqui sabendo escrever `repeat(auto-fit, minmax(...))` já resolve, sozinho, a maior parte dos layouts de listagem que vai encontrar — e resolve **de forma responsiva desde o primeiro dia**, que é o detalhe que separa quem aprendeu Grid de quem só decorou três colunas.
:::

:::curiosidade Uma unidade que só nasceu em 2017
Boa parte da web que você usa foi construída antes de o Grid existir nos navegadores, com propriedades desviadas da função original — `float`, criada para texto contornar imagem, virou a base de layouts inteiros durante quinze anos, com uma coleção de truques para consertar os efeitos colaterais. O Grid foi o primeiro sistema desenhado do zero para pensar em duas dimensões, e trouxe junto a unidade `fr`, que não existe em nenhuma outra parte do CSS. Você está aprendendo direto na ferramenta certa, sem passar pela era das gambiarras.
:::

## Prática

**Montar os cards (~15 min).**

**1. No `index.html`,** envolva cada benefício num `<article>` e agrupe os três:

```html
<section id="beneficios">
  <h2>O que muda para você</h2>

  <div class="beneficios">
    <article class="card">
      <h3>Benefício 1</h3>
      <p>Uma frase explicando.</p>
    </article>

    <article class="card">
      <h3>Benefício 2</h3>
      <p>Uma frase explicando.</p>
    </article>

    <article class="card">
      <h3>Benefício 3</h3>
      <p>Uma frase explicando.</p>
    </article>
  </div>
</section>
```

**2. No `estilo.css`:**

```css
.beneficios {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 24px;
  margin: 32px 0;
}

.card {
  background-color: var(--cor-fundo);
  border: 1px solid var(--cor-apoio);
  border-radius: 12px;
  padding: 24px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
}

.card h3 {
  margin-top: 0;
}
```

**3. O teste que prova o truque (2 min).** Pegue a borda da janela do navegador e vá estreitando devagar. Os três cards viram dois, depois um — sozinhos, sem media query nenhuma. Depois **abra no celular**: já está resolvido.

**Entrega:** página republicada, com os três benefícios em cards que se reorganizam. Confira no celular e mande o link no grupo.

## Avaliação

```quiz
- pergunta: Quando usar Grid em vez de Flexbox?
  alternativas:
    - texto: Sempre que houver mais de dois elementos para posicionar
    - texto: "Quando o layout tem duas dimensões — linhas e colunas ao mesmo tempo; para uma direção só, Flexbox é mais direto"
      correta: true
    - texto: Somente quando a página precisa ser responsiva
    - texto: Grid substituiu o Flexbox e deve ser usado em todos os casos
  feedback: >
    A pergunta é quantas dimensões o layout tem. Barra de navegação é uma fila e
    pede Flex; grade de cards é linhas e colunas e pede Grid. E os dois convivem —
    é comum um card montado por Grid usar Flexbox por dentro.
- pergunta: O que repeat com auto-fit e minmax de 250px a 1fr faz?
  alternativas:
    - texto: Cria sempre três colunas de no mínimo 250 pixels
    - texto: "Deixa o navegador calcular quantas colunas de pelo menos 250 pixels cabem na largura disponível e cria essa quantidade"
      correta: true
    - texto: Define a largura máxima da grade em 250 pixels
    - texto: Faz os cards diminuírem proporcionalmente conforme a tela encolhe
  feedback: >
    Você para de dizer quantas colunas existem e passa a dizer qual é a largura
    mínima aceitável. O navegador conta sozinho, e o layout se reorganiza em
    qualquer tela — inclusive em larguras que você nunca testou.
- pergunta: Três cards com width 33.33% e gap de 24px — o terceiro card cai para a linha de baixo. Por quê?
  alternativas:
    - texto: Porque gap não funciona junto com width em porcentagem
    - texto: "Porque as porcentagens já somam 100% e os espaços do gap são somados por cima, estourando a largura da linha"
      correta: true
    - texto: Porque o navegador limita a três colunas por linha
    - texto: Porque falta declarar flex-wrap no container
  feedback: >
    Porcentagem é calculada sobre o total e ignora os espaços entre as colunas.
    A unidade fr resolve porque ela reparte apenas o que sobrou depois de
    descontar o gap.
```

## Fechamento

O que ficou de hoje:

- **Uma direção pede Flex; duas direções pedem Grid.** Não são rivais, e convivem na mesma página.
- **`fr` reparte o espaço que sobrou** depois do `gap` — por isso não estoura como a porcentagem.
- **`repeat(auto-fit, minmax(250px, 1fr))`** entrega reorganização automática sem nenhuma media query, e é uma das linhas mais reaproveitáveis do CSS.
- **Card é padrão, não tag**: respiro por dentro, separação do fundo, cantos arredondados e sombra discreta.
- Sua seção de benefícios já se comporta em qualquer largura.

**Próxima aula:** os cards já se viram sozinhos, mas o resto da página não. A headline de 44px continua gigante no celular, o topo aperta, e o conteúdo encosta nas bordas. Vamos assumir de vez que **o MVP vai ser aberto no celular de quem vai validar** — e ajustar a página para essa realidade, testando no aparelho de cada um.

:::roteiro
Comece mostrando os três benefícios empilhados e a mesma seção em cards, lado a lado, no projetor — sem explicar. Pergunte o que muda na mensagem. A turma percebe sozinha que empilhado parece texto para ler e lado a lado parece opções para comparar.

Não introduza `auto-fit` de cara. Escreva `repeat(3, 1fr)`, mostre funcionando, e só então estreite a janela até esmagar. O truque precisa chegar como solução de um problema que eles acabaram de ver.

O diagrama funciona melhor com a janela do navegador na mão: revele a camada e arraste a borda para confirmar. Camada 4 é o momento da aula — três, dois, um, sem tocar no código.

O estouro com porcentagem vai aparecer, porque algum aluno vai tentar. Se não aparecer, provoque: escreva no projetor e quebre de propósito. É a melhor justificativa possível para `fr`.

Vigie o HTML: a parte que mais dá errado hoje não é o CSS, é esquecer de envolver os três `<article>` na `<div class="beneficios">`. Sem o container, o Grid não tem onde ser aplicado e o aluno acha que a linha não funciona.

Termine com todo mundo estreitando a janela ao mesmo tempo. É satisfatório, dura trinta segundos e planta a aula 14.
:::
