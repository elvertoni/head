---
titulo: Montando a lista a partir dos dados com forEach
tema: JavaScript na prática
disciplina: programacao-front-end
serie: 2ª
prerequisitos: [Percorrer arrays, Criar li e inserir na lista, Definir funções]
objetivos:
  - Executar uma função para cada tarefa usando forEach
  - Reconstruir a lista visual a partir do array sem duplicar itens
  - Separar o recebimento da tarefa da função que apresenta os dados
trilha: javascript-na-pratica
ordem: 35
slug: foreach-montando-lista
modo_origem: seed
fontes: [docs/plano-apostila-javascript.md]
revisao: true
status: aprovada
versao: 3
atualizado_em: 2026-11-04
---

Seu array guarda as tarefas, e a página mostra uma lista. Hoje vamos fazer a apresentação ser construída a partir desse conjunto de dados. Pense no placar de um jogo: quando os dados mudam, você atualiza o placar para refletir a situação atual. Aqui vamos limpar a apresentação antiga e mostrar cada tarefa uma vez.

## Objetivos

- Usar `forEach` para executar uma função com cada tarefa do array.
- Limpar e reconstruir os itens visíveis sem apagar os dados.
- Chamar a função de apresentação depois de um envio válido.

## Pré-requisitos

Use `meus-estudos` no VSCode e no navegador. O HTML continua com formulário, mensagem, lista vazia `id="lista-tarefas"` e `script.js` carregado depois desses elementos. Retome as aulas 32–34 para lembrar criação de itens, arrays e repetições. Vamos substituir o `script.js` por um programa completo de cada vez.

## Desenvolvimento

### 1. Percorra sem escrever o controle do índice

No **`script.js`**, substitua o conteúdo anterior por este teste:

```javascript
const tarefas = ["Revisar HTML", "Praticar CSS"];

function conferirTarefa(tarefa) {
  console.log(tarefa);
}

tarefas.forEach(conferirTarefa);
```

Salve e atualize. O console mostra **Revisar HTML** e **Praticar CSS**. No lugar de controlar o índice com `for`, você pediu para executar uma ação para cada elemento.

:::conceito forEach entrega um elemento por vez
**`forEach`** percorre o array e chama a função informada com cada elemento. O parâmetro `tarefa` recebe o texto daquele elemento. `tarefas.forEach(conferirTarefa)` entrega a função sem chamá-la imediatamente, assim como você já fez ao registrar uma função para um evento.
:::

O nome no parâmetro é escolhido por você. Aqui `tarefas` representa o conjunto e `tarefa` representa um texto de cada vez. Um array vazio não faz nenhuma chamada dessa função.

### 2. Transforme cada texto em um item visível

Confira seu HTML. Se precisar recuperar a base, este é o arquivo completo para um **`index.html` vazio**; na página existente, mantenha os mesmos ids e a lista inicial sem itens.

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>Meus estudos</title>
  <style>
    body { background-color: aliceblue; }
    h1 { color: darkgreen; }
  </style>
</head>
<body>
  <h1>Meus estudos</h1>
  <form id="formulario-tarefa">
    <label for="campo-tarefa">Qual é sua próxima tarefa?</label>
    <input type="text" id="campo-tarefa" name="tarefa">
    <button type="submit">Adicionar tarefa</button>
  </form>
  <p id="mensagem">Digite uma tarefa para adicionar.</p>
  <ul id="lista-tarefas"></ul>
  <script src="script.js"></script>
</body>
</html>
```

Substitua o conteúdo de **`script.js`** pelo programa abaixo. É um teste de apresentação com duas tarefas fixas, ainda sem tratar o formulário.

```javascript
const tarefas = ["Revisar HTML", "Praticar CSS"];

function mostrarTarefa(tarefa) {
  const lista = document.getElementById("lista-tarefas");
  const item = document.createElement("li");
  item.textContent = tarefa;
  lista.appendChild(item);
}

function renderizarTarefas() {
  const lista = document.getElementById("lista-tarefas");
  lista.textContent = "";
  tarefas.forEach(mostrarTarefa);
}

renderizarTarefas();
renderizarTarefas();
```

Salve e atualize. A lista deve mostrar **dois itens**, mesmo com duas chamadas de `renderizarTarefas`. **Renderizar**, aqui, significa construir a apresentação usando os dados. A função limpa os itens antigos e depois cria um item para cada texto do array.

`lista.textContent = "";` limpa os elementos da lista visual, mas **não esvazia o array**. Na aula 32, substituir o texto da lista por uma tarefa apagava itens sem reconstruí-los. Aqui a limpeza é intencional e é seguida do percurso de todos os dados.

### 3. Atualize os dados e depois a apresentação

Substitua o conteúdo de **`script.js`** pelo programa final desta aula:

```javascript
const tarefas = [];

function mostrarTarefa(tarefa) {
  const lista = document.getElementById("lista-tarefas");
  const item = document.createElement("li");
  item.textContent = tarefa;
  lista.appendChild(item);
}

function renderizarTarefas() {
  const lista = document.getElementById("lista-tarefas");
  lista.textContent = "";
  tarefas.forEach(mostrarTarefa);
}

function adicionarTarefa(evento) {
  evento.preventDefault();
  const campo = document.getElementById("campo-tarefa");
  const mensagem = document.getElementById("mensagem");
  const tarefa = campo.value.trim();

  if (tarefa === "") {
    mensagem.textContent = "Digite uma tarefa.";
  } else {
    tarefas.push(tarefa);
    renderizarTarefas();
    mensagem.textContent = "Tarefa adicionada. Total: " + tarefas.length;
    campo.value = "";
  }
}

const formulario = document.getElementById("formulario-tarefa");
formulario.addEventListener("submit", adicionarTarefa);
renderizarTarefas();
```

Salve e atualize. Envie duas tarefas. A primeira continua visível quando a segunda aparece, e não deve haver cópias extras. O envio agora **acrescenta ao array e chama a apresentação**; quem cria os itens é `mostrarTarefa`, executada por `forEach`.

### 4. Confira vazio, repetição e continuidade

Agora confira se renderizar mais de uma vez é seguro. Acrescente temporariamente mais uma chamada `renderizarTarefas();` no fim do arquivo, depois da que já existe. Salve e atualize: a lista começa vazia, porque atualizar a página reinicia o array. Envie duas tarefas. Cada uma deve aparecer uma única vez: a chamada extra não cria dados nem duplica itens, porque cada renderização limpa a lista antes de recriá-la.

Retire a chamada extra para terminar com o programa do modelo. Envie o campo vazio e só com espaços: a orientação deve aparecer, sem acrescentar dados nem apagar os itens existentes.

:::atencao A lista está duplicando
**Sintoma:** depois do segundo envio, a primeira tarefa aparece mais de uma vez.

**Solução:** confira a limpeza `lista.textContent = "";` no início de `renderizarTarefas`. Retire do envio a criação direta de `li` que vinha da aula 33; agora ela só acontece em `mostrarTarefa`. Use o programa completo para não manter os dois modos de inserir itens ao mesmo tempo.
:::

:::atencao Apareceu um item vazio e um erro no console
**Sintoma:** ao enviar uma tarefa, a lista ganha um marcador sem texto, a confirmação não aparece, o campo não é limpo e o console aponta `TypeError: undefined is not a function`.

**Solução:** confira se escreveu `tarefas.forEach(mostrarTarefa());`, com parênteses. Assim você chama `mostrarTarefa` uma vez, sem nenhuma tarefa, e entrega ao `forEach` o resultado dessa chamada, que não é uma função. Escreva `tarefas.forEach(mostrarTarefa);`, sem parênteses, como no registro de eventos. Salve, atualize e envie de novo.
:::

:::dica Separe as responsabilidades
Receber dados e apresentar dados são ações diferentes. Manter `adicionarTarefa`, `renderizarTarefas` e `mostrarTarefa` com nomes claros ajuda a localizar onde conferir entrada, atualizar o array e construir a página.
:::

## Prática

### Dados que viram lista

Use o programa completo da etapa 3 e o HTML identificado desta aula.

1. Envie três tarefas e confira os totais e a ordem dos itens.
2. Envie texto vazio e só com espaços; confira que a lista permanece igual.
3. Explique à dupla por que limpar a lista visual não apaga o array e por que a reconstrução não deve duplicar itens.
4. No teste fixo da etapa 2, acrescente uma terceira tarefa no array e execute. Confira três itens após as duas chamadas. Depois restaure o programa final da etapa 3.

### Confira antes de entregar

Mostre o array atualizado, a função que percorre seus elementos e a função que cria cada item. O formulário deve continuar validando os dados e limpando o campo após sucesso. A lista é temporária, como nas aulas anteriores. Guarde a pasta para acrescentar o estado de conclusão.

## Avaliação

```quiz
- pergunta: O que tarefas.forEach(mostrarTarefa) faz neste programa?
  alternativas:
    - texto: Executa mostrarTarefa uma única vez com o array inteiro
    - texto: Executa mostrarTarefa para cada elemento, entregando uma tarefa por vez
      correta: true
    - texto: Apaga as tarefas após mostrar o primeiro elemento
  feedback: >
    forEach chama a função com um elemento por vez. Não apaga o array nem entrega todo o conjunto como primeiro parâmetro dessa função.
- pergunta: Por que renderizarTarefas limpa a lista visual antes do percurso?
  alternativas:
    - texto: Para reconstruir a apresentação sem acumular cópias de itens anteriores
      correta: true
    - texto: Para apagar os valores do array
    - texto: Para validar o campo de texto
  feedback: >
    A limpeza remove a apresentação antiga; o percurso reconstrói os itens com os dados atuais. O array permanece, e a validação ocorre no envio.
- pergunta: Depois de um envio válido, qual sequência mantém os dados e a apresentação atualizados?
  alternativas:
    - texto: Renderizar primeiro e não guardar o texto
    - texto: Criar um li fora da função e reutilizá-lo para todas as tarefas
    - texto: Acrescentar ao array e chamar renderizarTarefas
      correta: true
  feedback: >
    A apresentação usa os dados atuais. Por isso o texto é acrescentado antes de reconstruir a lista, e mostrarTarefa cria um elemento por tarefa.
```

## Fechamento

- **`forEach` chama uma função por elemento**, sem você escrever o controle do índice.
- **Renderizar** é construir a apresentação a partir dos dados.
- Limpe a **lista visual**, depois recrie os itens; o array continua guardando as tarefas.
- Depois de aceitar uma tarefa, **atualize os dados e a apresentação**.

Na próxima aula, cada tarefa também vai guardar se está concluída, e a página vai mostrar essa situação com uma classe CSS.

:::roteiro
0–8 min: forEach com função nomeada e um parâmetro. 8–22 min: criar item por texto, limpar e reconstruir; duas chamadas sem duplicação. 22–34 min: integrar formulário, separando dados e apresentação. 34–46 min: prática, com apoio por reunir vários conhecimentos. 46–50 min: quiz e fechamento. RCO 82/86/87 reorganizado: percorrer antes de transformar e filtrar. Não introduzir arrow functions, objetos ou estado de conclusão nesta aula. forEach não é ensinado como mecanismo de transformação de array; sua função aqui é executar uma ação por elemento.
:::
