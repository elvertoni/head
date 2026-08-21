---
titulo: "JavaScript na conta certa: três comportamentos, vinte linhas"
tema: Primeiro JavaScript — eventos e manipulação de classe
disciplina: programacao-front-end
serie: 2ª
prerequisitos: [Página com movimento e estados aplicados na Aula 15]
objetivos:
  - Explicar o papel do JavaScript como camada de comportamento sobre HTML e CSS
  - Selecionar um elemento com querySelector e registrar um ouvinte com addEventListener
  - Alternar uma classe com classList.toggle para abrir e fechar o menu no celular
  - Reconhecer quando o CSS já resolve e o JavaScript é desnecessário
  - Diagnosticar o erro causado por script executado antes de o elemento existir
trilha: landing-page-mvp
ordem: 16
slug: os-tres-javascripts
modo_origem: tema
fontes: []
revisao: false
status: aprovada
versao: 2
atualizado_em: 2026-08-21
---

Sua página está bonita, responsiva e reage ao toque — e ainda é uma folha de papel. Ela não **faz** nada. Hoje entra o JavaScript, e vai entrar em dose pequena de propósito: três comportamentos, cerca de vinte linhas no total, escolhidos porque resolvem problemas que vocês já têm nessa página específica. Um deles, inclusive, vamos descobrir que não precisa de JavaScript nenhum — e essa vai ser a lição mais valiosa da aula, porque saber quando **não** usar a ferramenta é o que separa quem programa de quem só sabe a sintaxe.

## Objetivos

Ao final desta aula, você será capaz de:

- Explicar por que JavaScript é a **camada de comportamento**, e o que deve continuar funcionando sem ele.
- **Encontrar** um elemento na página e **escutar** um evento nele.
- Abrir e fechar o menu no celular alternando uma **classe**.
- Reconhecer quando o **CSS já resolve** e o JavaScript seria desperdício.
- Diagnosticar o erro clássico de script que roda antes de o elemento existir.

## Pré-requisitos

A página das aulas 10 a 15. Não é preciso ter programado antes — este é o primeiro contato com JavaScript, e ele começa do zero.

## Desenvolvimento

### Três camadas, e o que sobra quando uma falha

Uma página bem construída é feita de três camadas empilhadas, e cada uma tem um trabalho: o **HTML** carrega o conteúdo e a estrutura, o **CSS** cuida da aparência, e o **JavaScript** cuida do comportamento — o que acontece **em resposta** a alguma coisa que a pessoa faz.

:::conceito Camada de comportamento
JavaScript é a camada que **reage**. Isso implica uma regra de projeto: o conteúdo essencial da página não deve depender dele. Se o script falhar — e ele falha, por internet ruim, erro de digitação ou navegador antigo —, o visitante ainda precisa conseguir ler a headline, entender os benefícios e clicar no botão. Comportamento que enriquece a experiência, sim; comportamento que segura o conteúdo como refém, não.
:::

Para o projeto de vocês isso é concreto: o teste da aula 17 vai acontecer no celular de alguém, com o wi-fi da escola. Página cujo conteúdo só aparece depois que o JavaScript roda é página que pode chegar em branco na mão de quem vai avaliar.

### Achar o elemento, e deixar um recado

Todo JavaScript de interface faz duas coisas antes de qualquer outra: encontra um elemento e diz o que fazer quando algo acontecer com ele.

![Linha do tempo horizontal dividida em dois territórios. No trecho inicial, marcado como leitura do arquivo, o navegador percorre as linhas do script de cima a baixo, e no ponto da linha que registra o ouvinte aparece um envelope guardado, com a indicação de que a função não foi executada. Logo depois, a linha do tempo entra num trecho longo e vazio, rotulado como espera. Mais adiante, um toque de dedo marca o evento, o envelope guardado é aberto e só então a função aparece em execução. Abaixo, uma ramificação mostra o caso em que o script é lido antes de o elemento existir — a busca volta vazia.](img/o-recado-que-fica-esperando.png)

```js
const botao = document.querySelector("#menu-botao");

botao.addEventListener("click", function () {
  console.log("clicaram em mim");
});
```

`querySelector` procura na página usando **a mesma linguagem do CSS**: `#menu-botao` é o elemento de `id="menu-botao"`, `.card` é o de `class="card"`. Quem já sabe escrever seletor de CSS já sabe procurar elemento em JavaScript.

`addEventListener` é a parte que confunde no começo, porque ela **não executa nada agora**:

```diagrama-progressivo
titulo: O que realmente acontece quando o navegador lê o seu script
camadas:
  - rotulo: O arquivo é lido uma vez, de cima a baixo
    conteudo: "O navegador percorre o script inteiro na ordem em que está escrito, e faz isso uma única vez, assim que chega nele. Não existe repetição automática e não existe espera embutida."
  - rotulo: addEventListener não roda a função
    conteudo: "Ao encontrar essa linha, o navegador guarda um recado — quando houver um clique neste elemento, execute esta função. A função em si não é executada agora; ela fica registrada e adormecida."
  - rotulo: O script termina, e a página fica esperando
    conteudo: "Lida a última linha, o script acabou. A página não fica travada nem verificando nada: ela simplesmente aguarda, e os recados registrados continuam valendo."
  - rotulo: A pessoa clica, e só então a função roda
    conteudo: "O clique dispara o recado guardado, e aí sim a função é executada. Pode acontecer três segundos depois, ou dez minutos depois, ou nunca. É por isso que dizemos que a página reage a eventos em vez de seguir um roteiro."
  - rotulo: E é por isso que a ordem importa
    conteudo: "Se o script for lido antes de o elemento existir na página, querySelector não acha nada e devolve vazio — e o recado não chega a ser registrado em lugar nenhum. Nesse caso não há erro de digitação para procurar: o problema é que o script chegou cedo demais."
```

:::atencao O erro de todo primeiro JavaScript
A mensagem que vai aparecer, quase com certeza, é esta: `Uncaught TypeError: Cannot read properties of null (reading 'addEventListener')`. Traduzindo: você pediu para pendurar um ouvinte em **nada**. E o "nada" tem uma causa quase sempre: o `<script>` está no `<head>` ou no topo do `<body>`, então ele rodou **antes** de o navegador ter criado o elemento que `querySelector` foi procurar — o elemento existe no seu arquivo, mas ainda não existia naquele instante. As outras duas causas, bem menos frequentes, são erro de digitação no seletor e falta do `#` ou do `.`. Diagnóstico em dez segundos: escreva `console.log(botao)` logo depois do `querySelector`. Se aparecer `null`, o problema é ordem ou seletor — nunca a linha do `addEventListener`, que é só onde o erro estourou. **Solução:** ponha o `<script>` como última coisa antes de `</body>`.
:::

### O menu que abre no celular

No celular, os links do menu não cabem ao lado do nome do produto. A solução universal é escondê-los e mostrar um botão que os revela. E a mecânica é mais simples do que parece — **quem esconde e mostra é o CSS**; o JavaScript só liga e desliga uma classe.

:::conceito classList.toggle
`elemento.classList.toggle("aberto")` **alterna** a classe: se o elemento não a tem, ela é adicionada; se já tem, é removida. Uma linha cobre abrir e fechar, sem `if` nenhum. O CSS, por sua vez, define o que aquela classe significa visualmente. Essa divisão — JavaScript decide o **estado**, CSS decide a **aparência do estado** — é o padrão em interfaces bem construídas.
:::

### Quando o CSS já resolve

O terceiro comportamento da nossa lista era a rolagem suave até o botão: em vez de a página pular abruptamente ao clicar num link interno, ela desliza.

Isso já foi um clássico de biblioteca JavaScript, com dezenas de linhas. Hoje é uma linha de CSS:

```css
html {
  scroll-behavior: smooth;
}
```

:::importante Antes de escrever script, pergunte se o CSS já faz
Muita coisa que exigia JavaScript há alguns anos passou para o CSS e para o próprio HTML: rolagem suave, abrir e fechar um bloco de texto com `<details>`, validação básica de formulário, carregamento preguiçoso de imagem. Código que não existe não tem bug, não pesa e não precisa de manutenção. A pergunta certa antes de abrir o arquivo `.js` é sempre a mesma: **o CSS ou o HTML já resolvem isso?** É uma pergunta que economiza mais tempo de carreira do que qualquer truque de sintaxe.
:::

:::dica Vinte linhas resolvem mais do que parece
Existe uma impressão comum de que projeto sério exige framework. Boa parte das páginas institucionais e de campanha que estão no ar hoje roda com algumas dezenas de linhas de JavaScript direto, sem biblioteca nenhuma — porque uma landing page não tem estado complexo para gerenciar. Framework resolve problema de aplicação grande, e traz um custo próprio. Saber fazer o simples sem ele é uma habilidade valorizada e, na prática, é o que se pede em boa parte das vagas de entrada.
:::

## Prática

**Os três comportamentos (~15 min).**

**1. No `index.html`,** acrescente o botão do menu dentro do `<header>` e o `<script>` como **última linha antes de `</body>`**:

```html
<header>
  <p>NomeDoProduto</p>

  <button id="menu-botao" aria-label="Abrir menu">☰</button>

  <nav id="menu">
    <a href="#beneficios">Benefícios</a>
    <a href="#comecar">Começar</a>
  </nav>
</header>
```

```html
  <script src="script.js"></script>
</body>
```

**2. No `estilo.css`** — o CSS decide a aparência dos dois estados, e a rolagem suave sai de graça:

```css
html { scroll-behavior: smooth; }

#menu-botao {
  background: none;
  border: 1px solid var(--cor-apoio);
  border-radius: 8px;
  font-size: 20px;
  padding: 6px 12px;
  cursor: pointer;
}

#menu { display: none; }          /* escondido no celular */
#menu.aberto { display: flex; }   /* a classe que o JS liga */

@media (min-width: 768px) {
  #menu-botao { display: none; }  /* na tela grande o botão não faz falta */
  #menu { display: flex; }        /* e o menu fica sempre visível */
}
```

**3. Crie `script.js`** na mesma pasta:

```js
// 1 — menu que abre e fecha no celular
const menuBotao = document.querySelector("#menu-botao");
const menu = document.querySelector("#menu");

menuBotao.addEventListener("click", function () {
  menu.classList.toggle("aberto");
});

// 2 — copiar o link da página, para o teste da próxima aula
const copiar = document.querySelector("#copiar-link");

copiar.addEventListener("click", function () {
  navigator.clipboard.writeText(window.location.href);
  copiar.textContent = "Link copiado!";
});
```

**4. O botão de copiar** vai no `<footer>`, e é ferramenta de trabalho para a aula 17:

```html
<button id="copiar-link">Copiar link desta página</button>
```

Detalhe que importa: `navigator.clipboard` só funciona em página servida por conexão segura. No endereço publicado do GitHub Pages funciona; abrindo o arquivo com dois cliques na sua máquina, pode não funcionar. Se falhar local e funcionar publicado, **não é bug** — é o navegador protegendo a área de transferência.

**5. Teste (3 min).** No celular: o menu abre e fecha? O botão de copiar cola o link certo no WhatsApp? Nos dois casos, a página continua legível se o script não rodar?

**Entrega:** página republicada, com menu funcional no celular e botão de copiar testado no aparelho.

## Avaliação

```quiz
- pergunta: O que addEventListener faz no momento em que o navegador lê essa linha?
  alternativas:
    - texto: Executa a função imediatamente
    - texto: "Registra um recado — a função fica guardada e só é executada quando o evento acontecer"
      correta: true
    - texto: Fica repetindo a verificação até alguém clicar
    - texto: Cria o elemento indicado no seletor
  feedback: >
    Nada visível acontece ali. A função é registrada e adormece; o clique é que a
    acorda, podendo ser dez minutos depois ou nunca. É a diferença entre um roteiro
    executado do começo ao fim e uma página que reage a eventos.
- pergunta: Aparece "Cannot read properties of null" ao clicar. Qual é a causa mais provável?
  alternativas:
    - texto: A função dentro do addEventListener está com erro de sintaxe
    - texto: "O script rodou antes de o elemento existir na página, então querySelector devolveu null"
      correta: true
    - texto: O navegador não suporta addEventListener
    - texto: Falta declarar a variável com let em vez de const
  feedback: >
    O erro estoura no addEventListener, mas nasce antes: não havia elemento para
    pendurar o ouvinte. Colocar o script como última linha antes de fechar o body
    resolve na maioria dos casos. Um console.log logo depois do querySelector
    confirma o diagnóstico em dez segundos.
- pergunta: Você quer que a página deslize suavemente até a seção ao clicar num link interno. Qual é o melhor caminho?
  alternativas:
    - texto: Escrever uma função em JavaScript que anima a posição da rolagem
    - texto: "Uma linha de CSS com scroll-behavior smooth, porque o navegador já faz isso nativamente"
      correta: true
    - texto: Instalar uma biblioteca especializada em rolagem
    - texto: Não é possível sem JavaScript
  feedback: >
    Isso já exigiu bastante código, e hoje é nativo. Código que não existe não tem
    bug, não pesa e não precisa de manutenção — antes de abrir o arquivo .js,
    pergunte sempre se o CSS ou o HTML já resolvem.
```

## Fechamento

O que ficou de hoje:

- **JavaScript é a camada de comportamento.** O conteúdo essencial precisa sobreviver se o script falhar.
- **`querySelector` usa a linguagem do CSS**; quem sabe seletor já sabe procurar elemento.
- **`addEventListener` não executa nada** — deixa um recado que só o evento aciona.
- **`classList.toggle`** abre e fecha em uma linha: o JavaScript decide o **estado**, o CSS decide a **aparência do estado**.
- **`scroll-behavior: smooth`** mostra que às vezes a melhor solução é não escrever script.
- **`<script>` como última linha antes de `</body>`** — é a causa número um do primeiro erro de todo mundo.

**Próxima aula:** a construção acaba aqui. A aula 17 é de **auditoria e encontro com a realidade**: uma lista de verificação para tirar os defeitos que só aparecem depois de publicado, e então o teste com cinco pessoas de verdade, que vão olhar a sua página por dez segundos e dizer o que entenderam. É o dado que a aula 18 vai analisar.

:::roteiro
Comece pela promessa da dose: "hoje são vinte linhas". Turma que ouve "vamos começar JavaScript" trava; turma que ouve "três comportamentos, vinte linhas" senta e escreve.

O diagrama do `addEventListener` é o miolo conceitual. Faça na lousa, devagar: leia o script em voz alta apontando linha por linha, diga "acabou" e fique em silêncio uns segundos. Então clique. Esse silêncio é a explicação inteira.

O erro de `null` vai acontecer — deixe acontecer. Peça que ninguém apague nada e resolva um caso no projetor, com o `console.log`, mostrando o `null` na tela. Ensinar a ler a mensagem de erro vale mais que ensinar a evitá-la, porque a mensagem vai acompanhar eles a carreira inteira.

O momento do `scroll-behavior` merece encenação: pergunte quantas linhas de JavaScript eles acham que isso exige, colha os palpites, e então escreva a linha de CSS. O contraste ensina restrição melhor que qualquer sermão.

Cuidado com o tempo no HTML: o botão do menu e o `<script>` no lugar certo é onde a turma se perde. Projete o HTML final e deixe no quadro durante a Prática.

O botão de copiar link parece supérfluo hoje e é ferramenta da aula 17 — diga isso em voz alta, para ninguém pular. Se falhar localmente, aproveite para explicar a exigência de conexão segura: é um caso raro em que o aluno vê, na prática, uma decisão de segurança do navegador afetando o código dele.
:::
