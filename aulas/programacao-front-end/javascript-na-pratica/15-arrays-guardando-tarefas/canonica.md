---
titulo: Guardando várias tarefas em um array
tema: JavaScript na prática
disciplina: programacao-front-end
serie: 2ª
prerequisitos: [Tratar e validar um formulário, Criar itens na lista, Consultar variáveis no console]
objetivos:
  - Criar um array de textos e consultar tarefas pelo índice
  - Acrescentar uma tarefa com push e conferir a quantidade com length
  - Manter o array durante os envios válidos do formulário e distinguir dados de elementos HTML
trilha: javascript-na-pratica
ordem: 15
slug: arrays-guardando-tarefas
modo_origem: seed
fontes: [docs/plano-apostila-javascript.md]
revisao: true
status: aprovada
versao: 1
atualizado_em: 2026-11-04
---

Sua página já acrescenta tarefas visíveis. Agora vamos guardar também os textos em um conjunto organizado no JavaScript, chamado array. Pense em uma fila de cartões: cada cartão tem uma posição, e um novo cartão pode entrar no fim. Esse conjunto vai preparar o projeto para percorrer e mostrar várias tarefas nas próximas aulas.

## Objetivos

- Criar um array e consultar a primeira e a segunda tarefa pelo índice.
- Usar `push` para acrescentar ao final e `length` para conferir a quantidade.
- Guardar os textos recebidos em envios válidos, mantendo a lista visual em correspondência com os dados.

## Pré-requisitos

Abra a pasta `meus-estudos` no VSCode e sua página no navegador, com o **Console** aberto. Vamos reutilizar formulário, `trim`, `if`/`else` e a criação de `li` da aula 14. Primeiro faremos testes isolados no `script.js`; depois voltaremos ao programa completo do formulário.

## Desenvolvimento

### 1. Reúna os textos em um array

No **`script.js`**, substitua o conteúdo anterior por este programa. Não junte os exemplos completos no mesmo arquivo: execute um de cada vez.

```javascript
const tarefas = ["Revisar HTML", "Praticar CSS"];

console.log(tarefas[0]);
console.log(tarefas[1]);
```

Salve com **Ctrl + S** e atualize com **Ctrl + R**. O console mostra **Revisar HTML** e depois **Praticar CSS**. O formulário ainda aparece no HTML, mas este pequeno programa substituiu temporariamente seu tratamento de envio.

:::conceito Array
Um **array** é uma estrutura que reúne vários valores em uma sequência. Aqui usamos colchetes para criar o conjunto e vírgula para separar os textos. Cada texto é um elemento do array. A variável `tarefas` dá nome ao conjunto; hoje vamos guardar somente textos de tarefas nele.
:::

Não confunda o array com o `ul` do HTML. O array guarda valores no JavaScript. O `ul` e os `li` são elementos da página. Um não se transforma automaticamente no outro; o programa precisa criar ou atualizar a apresentação, como você começou a fazer na aula 14.

### 2. Leia as posições e a quantidade

Em `tarefas[0]`, o número entre colchetes é o **índice**: a posição usada para consultar um elemento. **A primeira posição é 0**, a segunda é 1 e a terceira é 2. Na fila de cartões desta aula, numeramos começando por zero.

Substitua o conteúdo de **`script.js`** por este programa completo:

```javascript
const tarefas = ["Revisar HTML", "Praticar CSS"];

console.log(tarefas[0]);
console.log(tarefas[1]);
console.log(tarefas.length);
```

Salve e atualize. As saídas são **Revisar HTML**, **Praticar CSS** e **2**. A propriedade **`length`** informa a quantidade de elementos. Dois elementos ocupam os índices **0 e 1**; a quantidade não é o índice do último item.

:::atencao A primeira tarefa não apareceu como esperado
**Sintoma:** você tentou usar `tarefas[1]` para consultar a primeira tarefa e recebeu a segunda, ou usou `tarefas[2]` em um array de dois elementos e encontrou `undefined`.

**Solução:** comece a contagem dos índices por zero. Com dois elementos, consulte `[0]` e `[1]`; `[2]` ainda não tem uma tarefa nesse array. `undefined` é a indicação encontrada nessa consulta sem elemento, não uma terceira tarefa. Confira a quantidade com `length` e teste novamente.
:::

### 3. Acrescente ao fim com push

Substitua o conteúdo de **`script.js`** pelo exemplo abaixo:

```javascript
const tarefas = ["Revisar HTML", "Praticar CSS"];

tarefas.push("Estudar JavaScript");

console.log(tarefas[2]);
console.log(tarefas.length);
```

Salve e atualize. O console mostra **Estudar JavaScript** e depois **3**. **`push` acrescenta um valor ao final do array**. Os dois anteriores continuam nas posições 0 e 1; o novo ocupa a posição 2.

O array foi criado com `const`, mas você pode acrescentar um elemento a ele. `const` impede reatribuir outro valor ao nome `tarefas`; não impede alterar o conteúdo desse mesmo array. É parecido com a referência ao parágrafo na aula 10: você mantinha o elemento e alterava seu texto.

Também podemos começar com **`const tarefas = [];`**: um array vazio, com quantidade zero, pronto para receber as tarefas digitadas pelo usuário.

### 4. Guarde cada tarefa válida do formulário

No **`index.html`**, mantenha o formulário e a lista vazia identificada da aula 14. Se estiver sem a base, use este HTML completo **somente em um arquivo vazio**:

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

Substitua o conteúdo de **`script.js`** por este programa completo:

```javascript
const tarefas = [];

function adicionarTarefa(evento) {
  evento.preventDefault();

  const campo = document.getElementById("campo-tarefa");
  const mensagem = document.getElementById("mensagem");
  const lista = document.getElementById("lista-tarefas");
  const tarefa = campo.value.trim();

  if (tarefa === "") {
    mensagem.textContent = "Digite uma tarefa.";
  } else {
    tarefas.push(tarefa);

    const item = document.createElement("li");
    item.textContent = tarefa;
    lista.appendChild(item);

    mensagem.textContent = "Tarefa adicionada. Total: " + tarefas.length;
    console.log(tarefas[0]);
    campo.value = "";
  }
}

const formulario = document.getElementById("formulario-tarefa");
formulario.addEventListener("submit", adicionarTarefa);
```

Salve os dois arquivos e atualize. Envie **Revisar HTML**: a lista ganha um item e a mensagem indica **Total: 1**. Envie **Praticar CSS**: a lista ganha outro e o total passa a **2**. No console, a consulta `tarefas[0]` mostra a primeira tarefa nos dois envios: **Revisar HTML**.

O array vazio foi criado **fora da função**, uma vez ao carregar o arquivo. Cada envio válido acrescenta um texto nesse mesmo array. Depois o programa cria o item visível, como na aula 14. Envios vazios não entram no array nem criam itens.

:::atencao O total volta a 1 a cada envio
**Sintoma:** a lista visual cresce, mas o total calculado pelo array fica sempre em 1.

**Solução:** confira se `const tarefas = [];` está fora da função, no começo do arquivo, como no modelo. Criar um array vazio dentro da função a cada envio descarta a continuidade que este programa precisa. Salve, atualize e faça dois envios válidos de novo.
:::

:::dica Dados e apresentação têm papéis diferentes
O array guarda os textos para o programa consultar; os itens HTML mostram esses textos na interface. Neste passo, atualizamos os dois no mesmo envio válido. Na aula 17 vamos percorrer os dados para montar a apresentação. Por enquanto, os dados ficam apenas durante a execução: atualizar a página cria um novo array vazio e restaura a lista vazia do HTML.
:::

## Prática

### Três tarefas e suas posições

Use o **programa completo da etapa 4** e a lista vazia no HTML.

1. Atualize para começar um novo teste. Envie três tarefas suas e confira os totais **1**, **2** e **3**, com um item visível por tarefa.
2. Envie um campo vazio e outro só com espaços. Confira que não aparecem itens novos. Depois envie uma quarta tarefa válida: o total deve ser **4**, não 6.
3. Confira que o console mostra a primeira tarefa a cada envio válido. Explique à dupla por que `tarefas[0]` continua consultando a mesma posição.
4. Aponte no código a criação do array, o acréscimo com `push`, a quantidade com `length` e a criação do `li`. Diga qual parte guarda valores e qual parte altera a página.

### Confira antes de entregar

O array e a lista devem crescer apenas com envios válidos. As tarefas ficam na ordem de entrada; a primeira ocupa o índice **0** e a segunda, o índice **1**. Mostre ao professor os totais e o teste de campo vazio. Atualizar reinicia o array e a lista desta versão; o projeto ainda não tem armazenamento permanente. Guarde os arquivos para estudar repetições na aula 16.

## Avaliação

Considere um array de textos criado com `const tarefas = ["Revisar HTML", "Praticar CSS"];`.

```quiz
- pergunta: Qual consulta lê a segunda tarefa desse array?
  alternativas:
    - texto: tarefas[0]
    - texto: tarefas[1]
      correta: true
    - texto: tarefas[2]
  feedback: >
    A contagem começa por zero. O primeiro elemento está em 0 e o segundo em 1. O índice 2 ainda não contém uma tarefa nesse array de dois elementos.
- pergunta: Após tarefas.push("Estudar JavaScript"), qual valor tarefas.length informa?
  alternativas:
    - texto: "3"
      correta: true
    - texto: "2"
    - texto: "0"
  feedback: >
    push acrescentou um terceiro elemento ao final. length informa quantidade, não o índice do último elemento, que agora é 2.
- pergunta: Por que o array vazio do programa do formulário é criado fora da função adicionarTarefa?
  alternativas:
    - texto: Para que os textos sejam gravados automaticamente no arquivo HTML
    - texto: Para impedir qualquer alteração no conteúdo do array
    - texto: Para manter o mesmo conjunto de tarefas entre os envios dessa execução
      correta: true
  feedback: >
    O conjunto precisa continuar existindo entre os envios. Ele pode receber textos por push, mas não grava sozinho o arquivo HTML nem persiste depois de atualizar a página.
```

## Fechamento

- Um **array reúne valores em sequência**, como os textos das suas tarefas.
- Os **índices começam em 0**; `[1]` consulta o segundo elemento.
- **`push` acrescenta ao final** e **`length` informa a quantidade**.
- O **array guarda dados e o HTML mostra elementos**; esta versão mantém ambos apenas durante a execução.

Na próxima aula, vamos usar uma repetição para percorrer os valores de um array, um de cada vez.

:::roteiro
0–8 min: array com duas strings, ligação com a lista conhecida e distinção entre dados e HTML. 8–19 min: índices começando em zero e length. 19–28 min: push e const sem reatribuição do nome. 28–36 min: integrar array externo à função de envio mantendo validação e apresentação incremental da aula 14. 36–46 min: prática. 46–50 min: quiz e fechamento. Adaptação das coleções do RCO 86/92 ao plano: array, índice, push e length antes de laços e métodos de iteração. Não introduzir objetos, remoção, localStorage ou reconstrução da lista. O array e os itens são atualizados no mesmo ramo válido; a explicação sobre execução temporária evita confundir array com persistência.
:::
