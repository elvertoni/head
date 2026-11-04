---
titulo: Mudando uma mensagem da página com JavaScript
tema: JavaScript na prática
disciplina: programacao-front-end
serie: 2ª
prerequisitos: [Identificar tags HTML, Conectar script.js ao HTML, Definir e chamar uma função]
objetivos:
  - Identificar um elemento HTML por um id único
  - Localizar esse elemento com document.getElementById
  - Alterar seu texto com textContent e conferir o resultado na página
trilha: javascript-na-pratica
ordem: 28
slug: dom-alterando-mensagem-estudos
modo_origem: seed
fontes: [docs/plano-apostila-javascript.md]
revisao: true
status: aprovada
versao: 2
atualizado_em: 2026-11-04
---

Até aqui, seu programa conversou principalmente pelo console. Agora uma mensagem vai aparecer no lugar em que quem usa a página pode vê-la. Vamos localizar um parágrafo da lista “Meus estudos” e trocar seu texto pelo JavaScript. Pense em um mural: primeiro você identifica qual aviso quer atualizar; depois escreve a nova mensagem naquele lugar.

## Objetivos

- Dar um `id` único ao parágrafo da mensagem.
- Usar `document.getElementById` para localizar esse parágrafo.
- Mudar seu `textContent` e conferir a alteração visível no navegador.

## Pré-requisitos

Abra a pasta `meus-estudos` no VSCode e sua página no navegador. Vamos editar **`index.html` e `script.js`**, salvando cada arquivo antes de atualizar a página. Mantenha o console disponível para conferir possíveis erros. Você vai retomar tags, variáveis e uma função sem parâmetros da aula 27.

## Desenvolvimento

### 1. Prepare um lugar para a mensagem

No **`index.html`**, localize o parágrafo que fica abaixo do título. Substitua **somente esse parágrafo** pela linha abaixo. Preserve o título, a lista e o CSS.

```html
<p id="mensagem">Escolha uma tarefa para começar.</p>
```

O atributo **`id`** dá uma identificação ao elemento. Aqui o nome escolhido é `mensagem`. Cada `id` deve identificar um único elemento nessa página. Não crie outro parágrafo com o mesmo `id`.

Confira também que `<script src="script.js"></script>` continua perto do fim do HTML, **antes de `</body>` e depois do parágrafo**. Assim o navegador encontra o parágrafo antes de executar nosso arquivo JavaScript.

Se você perdeu o arquivo anterior, este é um HTML completo para recuperar a base. **Use o bloco inteiro somente se estiver começando com um `index.html` vazio.** Quem já tem a página faz apenas a troca do parágrafo indicada acima.

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>Meus estudos</title>
  <style>
    body {
      background-color: aliceblue;
    }
    h1 {
      color: darkgreen;
    }
  </style>
</head>
<body>
  <h1>Meus estudos</h1>
  <p id="mensagem">Escolha uma tarefa para começar.</p>
  <ul>
    <li>Revisar HTML</li>
    <li>Praticar CSS</li>
  </ul>
  <script src="script.js"></script>
</body>
</html>
```

Salve o HTML com **Ctrl + S**. O `script.js` ainda pode ter o programa da aula anterior; vamos substituí-lo na próxima etapa. Os testes de hoje usam a mensagem inicial exatamente como está no modelo.

### 2. Localize o parágrafo pelo DOM

O navegador transforma o HTML em uma representação dos elementos na memória, chamada **DOM**. É por essa representação que o JavaScript consegue localizar o parágrafo e trabalhar com ele. Imagine um mapa do mural: o `id` ajuda a encontrar um aviso específico nesse mapa.

No **`script.js`**, substitua o conteúdo anterior por este programa completo:

```javascript
const mensagem = document.getElementById("mensagem");
console.log(mensagem.textContent);
```

Salve e atualize. Na página, o parágrafo continua mostrando **Escolha uma tarefa para começar.**. No console, aparece esse mesmo texto.

:::conceito Encontrar o elemento
`document` dá acesso ao documento da página. `getElementById("mensagem")` procura o elemento cujo `id` é `mensagem`. Guardamos uma referência a esse elemento na variável `mensagem`. A propriedade `textContent` permite consultar ou alterar seu conteúdo de texto.
:::

Copie o nome `getElementById` com as letras maiúsculas do modelo. O texto entre aspas deve ser igual ao `id` do HTML. Para essa busca, escreva **`"mensagem"` sem `#`**. Ter os mesmos nomes no exemplo ajuda a leitura, mas a conexão com o HTML é feita pelo texto passado a `getElementById`.

### 3. Troque o texto que aparece na página

Substitua o conteúdo do **`script.js`** pelo programa abaixo:

```javascript
const mensagem = document.getElementById("mensagem");
mensagem.textContent = "Hora de revisar HTML!";
```

Salve e atualize. **Agora observe a própria página:** no lugar da mensagem inicial deve aparecer **Hora de revisar HTML!**. O título, a lista e as cores continuam como estavam.

O `=` atribui um novo texto à propriedade `textContent` do elemento encontrado. A variável criada com `const` continua apontando para o mesmo elemento; alteramos uma propriedade desse elemento, sem reatribuir outro valor ao nome `mensagem`.

O arquivo HTML salvo no VSCode ainda contém a mensagem inicial. A mudança foi feita no documento carregado pelo navegador. A cada atualização, o navegador lê o HTML e executa o JavaScript novamente.

:::atencao O elemento não foi encontrado
**Sintoma:** a mensagem não muda e o console aponta um erro envolvendo `textContent` e `null`.

**Solução:** neste caso, a busca não encontrou o elemento no momento em que foi executada. Confira se o HTML tem `id="mensagem"`, se o JavaScript busca `"mensagem"` com a mesma escrita e se a tag que carrega `script.js` está depois do parágrafo, antes de `</body>`. Salve os dois arquivos e atualize. Confira também se abriu a página da pasta correta.
:::

### 4. Organize a mudança em uma função

Vamos reutilizar a ideia da aula 27. Substitua o conteúdo de **`script.js`** pelo programa completo abaixo:

```javascript
function mostrarLembrete() {
  const mensagem = document.getElementById("mensagem");
  mensagem.textContent = "Hora de revisar HTML!";
}

mostrarLembrete();
```

Salve e atualize. A página mostra a mesma mensagem da etapa anterior. A função reúne a busca e a alteração; a chamada `mostrarLembrete();` executa a ação quando o arquivo é carregado.

Agora retire **somente a última chamada**, deixando a definição da função. Salve e atualize: deve voltar a aparecer **Escolha uma tarefa para começar.**, o texto inicial do HTML. Recoloque a chamada, salve e atualize: o lembrete volta a aparecer. Isso retoma a diferença entre definir uma função e executá-la.

:::dica Atualize o texto no lugar certo
Ao desenvolver uma interface, dê uma identificação clara ao elemento que será atualizado e altere apenas o necessário. Para uma mensagem simples, `textContent` permite trabalhar com texto. O conteúdo atribuído é tratado como texto, não como novas tags HTML. Na próxima aula, vamos decidir quando executar essa mesma ação usando um botão.
:::

## Prática

### Um lembrete com a sua tarefa

Mantenha o parágrafo com `id="mensagem"` e a tag de carregamento no HTML. Substitua o conteúdo de **`script.js`** por este programa completo:

```javascript
function mostrarLembrete() {
  const mensagem = document.getElementById("mensagem");
  mensagem.textContent = "Minha próxima tarefa é revisar HTML.";
}

mostrarLembrete();
```

1. Execute o exemplo e confira a nova mensagem na página, abaixo do título.
2. Troque somente o texto atribuído a `textContent` por uma tarefa real sua. Salve e atualize.
3. Mostre à dupla o `id` no HTML, a busca no JavaScript e a chamada da função.
4. Faça o teste de retirar a chamada, salvar e atualizar. Explique por que a mensagem inicial reaparece. Recoloque a chamada para terminar.

### Confira antes de entregar

A página deve mostrar seu lembrete personalizado, mantendo o título e a lista. O console não deve apontar erro causado por seu código. No HTML salvo, o parágrafo ainda tem a mensagem inicial; no navegador, o JavaScript fez a troca. Mostre os dois arquivos ao professor e guarde a pasta, porque vamos usar essa função com um botão na aula 29.

## Avaliação

Considere o parágrafo com `id="mensagem"` e o JavaScript carregado depois dele, como no modelo.

```quiz
- pergunta: Qual instrução localiza o parágrafo pelo id usado no HTML?
  alternativas:
    - texto: 'document.getElementById("#mensagem")'
    - texto: 'document.getElementById("mensagem")'
      correta: true
    - texto: 'console.log("mensagem")'
  feedback: >
    getElementById recebe o próprio valor do id, sem #. Mostrar a palavra mensagem no console não localiza o elemento da página.
- pergunta: A variável mensagem já aponta para o parágrafo. Qual linha troca o texto visível desse elemento?
  alternativas:
    - texto: 'mensagem.textContent = "Hora de estudar!";'
      correta: true
    - texto: 'console.log("Hora de estudar!");'
    - texto: 'const tarefa = "Hora de estudar!";'
  feedback: >
    Atribuir a textContent altera o texto do elemento. console.log mostra uma mensagem no console; guardar uma string em outra variável não atualiza o parágrafo sozinho.
- pergunta: A função mostrarLembrete está definida, mas sua chamada foi retirada. Após salvar e atualizar, qual texto aparece no parágrafo neste exemplo?
  alternativas:
    - texto: O novo lembrete, porque definir a função já executa sua ação
    - texto: Uma mensagem de console no lugar do título
    - texto: O texto inicial salvo no HTML, pois a função não foi chamada
      correta: true
  feedback: >
    A atualização carrega o HTML novamente. Sem uma chamada para executar a troca, o parágrafo mantém o texto inicial. A definição da função sozinha não altera a página.
```

## Fechamento

- O **DOM representa os elementos** do HTML carregado no navegador.
- Um **`id` único** identifica o elemento que você quer localizar.
- **`document.getElementById` busca pelo id** e **`textContent` consulta ou altera o texto**.
- A **chamada da função executa a mudança**; nesta aula, ela acontece ao carregar o arquivo.

Na próxima aula, vamos acrescentar um botão e executar o lembrete somente quando ele receber um clique.

:::roteiro
0–8 min: retomar HTML/CSS e acrescentar id ao parágrafo; recuperação completa é só para quem perdeu o arquivo. 8–19 min: representação DOM, busca e consulta do texto no console. 19–29 min: atribuição a textContent, diferença entre documento carregado e arquivo salvo e diagnóstico de elemento não encontrado. 29–35 min: função e teste com/sem chamada. 35–45 min: prática. 45–50 min: quiz e fechamento. Adaptação da base DOM do RCO 89 ao plano; busca única pelo id antes de coleções. As advertências evitam pressupor que uma busca sempre encontra o elemento. Não introduzir querySelectorAll, innerHTML, criação de elementos ou eventos. A referência criada com const permanece a mesma; alterar propriedade não é reatribuir o nome.
:::
