---
titulo: "Mobile-first: o MVP no celular de quem vai validar"
tema: Design responsivo e media queries
disciplina: programacao-front-end
serie: 2ª
prerequisitos: [Cards de benefício montados com Grid na Aula 13]
objetivos:
  - Explicar o que a meta viewport faz e o que acontece na ausência dela
  - Escrever CSS partindo da tela pequena e acrescentando regras com media query de min-width
  - Substituir tamanhos fixos por unidades relativas nos pontos em que isso importa
  - Impedir que imagens e blocos largos causem rolagem horizontal
  - Testar a página no próprio aparelho pelo endereço publicado
trilha: landing-page-mvp
ordem: 14
slug: mobile-first
modo_origem: tema
fontes: []
revisao: false
status: aprovada
versao: 1
atualizado_em: 2026-08-18
---

Pensa em como o teste da aula 17 vai acontecer de verdade. Você vai chegar em alguém no corredor, entregar **o seu celular** com a página aberta, e essa pessoa vai ter dez segundos. Não vai ser num monitor de 24 polegadas com a janela maximizada — que é exatamente onde vocês vêm construindo tudo até agora. É bem provável que a sua headline de 44 pixels esteja ocupando quatro linhas na tela pequena, que o menu esteja espremido e que a página deslize para os lados quando a pessoa encostar o dedo. Hoje a gente conserta isso, e o teste é feito no aparelho de cada um.

## Objetivos

Ao final desta aula, você será capaz de:

- Explicar o que a **meta viewport** faz — e o desastre que acontece sem ela.
- Escrever CSS **começando pela tela pequena** e acrescentando regras conforme a tela cresce.
- Trocar tamanhos fixos por **unidades relativas** onde isso muda o resultado.
- Eliminar a **rolagem horizontal**, o defeito mais denunciador de página amadora.
- Abrir e ajustar sua página **no seu próprio celular**, pelo link publicado.

## Pré-requisitos

A página das aulas 10 a 10, publicada. Traga o celular com internet — hoje ele é ferramenta de trabalho, e o teste da aula acontece nele.

## Desenvolvimento

### Por que o celular vem primeiro

Não é preferência estética nem discurso: é onde a página vai ser aberta. O tráfego da web hoje é majoritariamente de celular, e o buscador do Google avalia as páginas pela **versão móvel** delas para decidir posição nos resultados. Para o projeto de vocês, o argumento é ainda mais direto: as cinco pessoas do teste de corredor vão receber um celular na mão.

:::conceito Mobile-first
**Mobile-first** é escrever o CSS partindo da tela **pequena** como caso padrão e, à medida que a tela cresce, **acrescentar** o que couber. O caminho inverso — desenhar para o monitor e depois ir remendando para o celular — dá muito mais trabalho, porque desfazer decisões de layout é sempre mais difícil do que adicionar.
:::

Existe um efeito colateral bem-vindo: a tela pequena não perdoa excesso. Quando você é obrigado a decidir o que cabe em 360 pixels, o que sobra costuma ser exatamente o essencial — e a versão grande fica melhor por causa disso.

### A linha sem a qual nada funciona

No `<head>` da sua página, desde a aula 10, existe esta linha:

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

Ela parece burocracia. Não é — sem ela, nada do que vem a seguir tem efeito nenhum.

```diagrama-progressivo
titulo: O que o celular faz com uma página que não declara viewport
camadas:
  - rotulo: O problema de 2007
    conteudo: "Quando os celulares ganharam navegador de verdade, a web inteira já existia e tinha sido feita para telas grandes. Se o aparelho dissesse a verdade sobre seu tamanho, todos os sites do mundo apareceriam quebrados nele."
  - rotulo: A solução da época — mentir
    conteudo: "Os navegadores móveis passaram a fingir uma largura de tela grande, em torno de 980 pixels, mesmo num aparelho estreito. Assim o site era montado como num computador."
  - rotulo: O efeito colateral que você já viu
    conteudo: "Montada essa página larga, o navegador encolhe tudo para caber na tela real. O resultado é a página inteira em miniatura, com texto ilegível, que obriga a pessoa a dar dois toques e arrastar para conseguir ler."
  - rotulo: O que a meta viewport diz
    conteudo: "A linha com width igual a device-width avisa que a página sabe se comportar em tela pequena e pede a largura verdadeira do aparelho. O navegador para de fingir e para de encolher."
  - rotulo: Por que isso vem antes de tudo
    conteudo: "Sem essa linha, o celular acha que tem 980 pixels de largura — e uma regra escrita para telas de até 600 pixels simplesmente nunca é acionada. O CSS responsivo está correto e não é aplicado, o que produz o tipo de erro em que a pessoa procura defeito no lugar errado por horas."
```

### Media query: escrever pequeno e acrescentar

:::conceito Media query e breakpoint
Uma **media query** é um bloco de CSS que só vale quando uma condição sobre a tela é verdadeira. O **breakpoint** é a largura escolhida como fronteira. Em mobile-first, a condição usada é `min-width`: as regras valem **a partir** daquela largura, ou seja, para telas maiores.
:::

```css
/* padrão: vale para todo mundo, inclusive celular */
h1 { font-size: 32px; }

/* a partir de 768px de largura, acrescenta */
@media (min-width: 768px) {
  h1 { font-size: 44px; }
}
```

Leia na ordem em que o navegador lê: todo mundo recebe 32px; quem tem tela de 768 pixels ou mais recebe 44px por cima. Escolha poucos breakpoints — dois resolvem quase tudo: um por volta de 768px (tablet) e outro por volta de 1024px (monitor). Breakpoints não devem ser escolhidos pelo modelo de aparelho, e sim pelo ponto em que **o seu layout** começa a ficar feio: estreite a janela até incomodar, e é ali.

### Unidades relativas e o pesadelo da rolagem lateral

Tamanho fixo em pixel é uma promessa que a tela pequena não consegue cumprir. Onde isso mais dói:

| Em vez de | Use | Por quê |
|---|---|---|
| `width: 800px` | `max-width: 800px` | Vira teto, não obrigação: em tela de 360px ele simplesmente cede |
| `padding: 40px` fixo nas laterais | `padding: 0 5%` ou `clamp()` | Em tela estreita, 40px de cada lado comem um quarto da largura |
| `font-size: 14px` no corpo | `1rem` como base | `rem` acompanha o tamanho de fonte que a pessoa configurou no aparelho |

E a regra que toda página precisa ter, sem exceção:

```css
img {
  max-width: 100%;
  height: auto;
}
```

Uma foto de 1200 pixels de largura numa tela de 360 força a página inteira a ter 1200 pixels. `max-width: 100%` a obriga a nunca passar da largura do container, e `height: auto` mantém a proporção em vez de achatá-la.

:::atencao A página que desliza para os lados
O sintoma é inconfundível: no celular, a pessoa arrasta o dedo e a página inteira anda para a esquerda, revelando uma faixa vazia. Passa uma impressão de descuido antes de qualquer texto ser lido. A causa é sempre a mesma — **algum elemento é mais largo que a tela** —, e as três origens mais comuns são imagem sem `max-width`, um bloco com largura fixa em pixels, e largura em porcentagem somada a `padding`. Esta última é a mais traiçoeira: `width: 100%` mais `padding: 24px` dá 100% **mais** 48 pixels, porque por padrão o padding é somado por fora da largura. A correção que resolve os três casos de uma vez, e que praticamente todo projeto profissional adota na primeira linha do CSS, é `* { box-sizing: border-box; }` — com ela, `padding` e `border` passam a ser contados **dentro** da largura declarada. Diagnóstico: estreite a janela até aparecer a barra horizontal e vá escondendo blocos até ela sumir; o último que você escondeu é o culpado.
:::

:::curiosidade A mentira que ficou
Aquela largura falsa de 980 pixels continua sendo o padrão dos navegadores móveis até hoje, quase vinte anos depois — não porque seja boa, mas porque existem milhões de páginas antigas que quebrariam se ela fosse removida. É um exemplo perfeito de uma coisa que você vai encontrar a carreira inteira: decisões técnicas tomadas por compatibilidade com o passado, que sobrevivem muito além do problema que resolviam. Por isso a meta viewport é uma linha que você **pede** — o padrão continua sendo o comportamento antigo.
:::

:::dica O que o mercado testa antes de entregar
Nenhuma equipe entrega uma página sem abrir em tela estreita. E a ferramenta usada no dia a dia está no seu navegador: as ferramentas de desenvolvedor têm um modo de simulação de dispositivo, que reproduz larguras de celular sem sair do computador. Use para trabalhar rápido — mas confirme no aparelho real antes de entregar, porque simulação não reproduz dedo grosso, brilho de tela ao sol nem conexão ruim. As três coisas vão estar presentes no teste da aula 17.
:::

## Prática

**Deixar a página apresentável no celular (~15 min).**

**1. Primeira linha do `estilo.css`** — antes de qualquer outra regra:

```css
* {
  box-sizing: border-box;
}

img {
  max-width: 100%;
  height: auto;
}
```

**2. Inverta a escala:** os tamanhos grandes passam a valer só a partir do tablet.

```css
/* padrão — celular */
h1 { font-size: 32px; }
h2 { font-size: 24px; }

#hero { min-height: 70vh; padding: 24px; }

main { padding: 0 20px; }

/* a partir de 768px */
@media (min-width: 768px) {
  h1 { font-size: 44px; }
  h2 { font-size: 28px; }
  #hero { min-height: 80vh; }
}
```

**3. Resolva o topo**, que é o que mais quebra em tela estreita — no celular ele empilha, no tablet volta a ficar lado a lado:

```css
header {
  flex-direction: column;
  gap: 12px;
  text-align: center;
}

@media (min-width: 768px) {
  header {
    flex-direction: row;
    text-align: left;
  }
}
```

**4. O teste que importa (5 min).** Abra o **link publicado** no **seu celular** — não o arquivo local, não o simulador. Percorra a lista:

- [ ] A página desliza para os lados? (se sim, cace o elemento largo)
- [ ] A headline cabe em no máximo três linhas?
- [ ] Dá para ler tudo **sem aproximar com os dedos**?
- [ ] O botão é grande o bastante para o dedo, sem precisar de mira?
- [ ] O texto encosta na borda da tela?

**Entrega:** página republicada e aprovada nos cinco itens, verificada no aparelho. Troque o celular com o colega do lado e confira na tela dele também — aparelho diferente revela problema diferente.

## Avaliação

```quiz
- pergunta: O que acontece com uma página no celular se a meta viewport não estiver declarada?
  alternativas:
    - texto: A página não carrega
    - texto: "O navegador finge ter cerca de 980 pixels de largura, monta a página como num computador e encolhe tudo — e as media queries de tela pequena nunca são acionadas"
      correta: true
    - texto: O CSS é ignorado por completo
    - texto: A página fica com rolagem horizontal apenas nas imagens
  feedback: >
    É o erro mais frustrante do responsivo, porque o CSS está correto e mesmo
    assim não tem efeito. Sem a linha, o celular acha que é largo, e uma regra
    escrita para até 600 pixels simplesmente não se aplica.
- pergunta: Em mobile-first, como se escrevem as regras?
  alternativas:
    - texto: "Primeiro as regras do monitor, depois media queries de max-width reduzindo para telas menores"
    - texto: "Primeiro as regras da tela pequena como padrão, depois media queries de min-width acrescentando para telas maiores"
      correta: true
    - texto: Uma media query separada para cada modelo de celular
    - texto: Dois arquivos CSS, um para celular e outro para computador
  feedback: >
    O padrão é a tela pequena, e min-width vai somando o que cabe conforme a tela
    cresce. Acrescentar é sempre mais simples do que desfazer decisões de layout
    tomadas para uma tela grande.
- pergunta: A página desliza para os lados no celular. Qual destas é a causa mais provável?
  alternativas:
    - texto: Falta declarar a altura do body
    - texto: "Algum elemento é mais largo que a tela — imagem sem max-width, largura fixa em pixels, ou largura de 100% somada a padding"
      correta: true
    - texto: O celular está com o zoom desconfigurado
    - texto: Há media queries demais no arquivo
  feedback: >
    Rolagem horizontal é sempre alguém ultrapassando a largura disponível.
    box-sizing border-box resolve o caso do padding somado, e max-width de 100%
    resolve o das imagens.
```

## Fechamento

O que ficou de hoje:

- **O celular é onde a página vai ser julgada** — inclusive no teste da aula 17.
- **Mobile-first é escrever para a tela pequena e acrescentar** com `min-width`, porque adicionar é mais fácil que desfazer.
- **Sem a meta viewport, o CSS responsivo não é aplicado** — o celular finge ser largo e as regras não disparam.
- **`max-width` em vez de `width`, `rem` em vez de pixel fixo, `max-width: 100%` em toda imagem.**
- **`box-sizing: border-box` na primeira linha** evita a maior parte das rolagens horizontais.
- Breakpoint se escolhe onde **o seu layout** quebra, não pelo modelo do aparelho.

**Próxima aula:** a página funciona em qualquer tela e ainda está estática — nada responde ao toque, nada indica que o botão é clicável, nada conduz o olho até a ação. Vamos acrescentar movimento, com uma regra rígida: **movimento que não leva o olho até o botão é ruído**, e ruído se corta.

:::roteiro
Comece com a página de um aluno no projetor e reduza a janela ao vivo até quebrar. É mais eficaz que qualquer argumento sobre a importância do responsivo — e escolha uma página caprichada, para deixar claro que não é questão de capricho.

Para o viewport, se der, mostre o antes e depois de verdade: comente a meta tag numa página responsiva e abra no celular projetado. A miniatura ilegível explica sozinha.

O ponto conceitual da aula é `min-width` versus `max-width`. Vai ter aluno escrevendo `max-width` e obtendo o oposto do esperado. Ancore com a frase: "min-width é a partir de".

A rolagem horizontal é o momento mais divertido: peça que todos deslizem o dedo para o lado no próprio celular. Metade da turma vai descobrir o defeito ao mesmo tempo, e a caçada ao elemento largo funciona bem como atividade coletiva.

Reserve os 5 min finais de verdade para o teste no aparelho, e faça a troca de celular entre colegas — aparelho diferente e mão diferente revelam problemas que o dono já não enxerga.

Se a escola bloquear o acesso ou a internet cair, use o modo de simulação de dispositivo do navegador e marque o teste real como tarefa para casa. Não cancele o teste: é ele que sustenta a aula 17.
:::
