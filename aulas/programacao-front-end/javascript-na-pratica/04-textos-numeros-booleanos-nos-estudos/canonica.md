---
titulo: Textos, números e booleanos nos estudos
tema: JavaScript na prática
disciplina: programacao-front-end
serie: 2ª
prerequisitos: [Criar variáveis com let e const, Consultar valores no console]
objetivos:
  - Reconhecer valores dos tipos string e number pela forma de escrita
  - Representar uma informação de sim ou não com true e false sem aspas
  - Conferir o tipo de textos, números e booleanos com typeof
trilha: javascript-na-pratica
ordem: 4
slug: textos-numeros-booleanos-nos-estudos
modo_origem: seed
fontes: [docs/plano-apostila-javascript.md]
revisao: true
status: aprovada
versao: 1
atualizado_em: 2026-11-03
---

Você decidiu estudar matemática por 20 minutos e ainda não terminou. Esse pequeno recado contém três informações diferentes: qual é a tarefa, quanto tempo você pretende estudar e se já concluiu. Hoje você vai guardar essas informações como texto, número e resposta de sim ou não. É parecido com uma ficha de estudos: cada campo precisa receber uma informação que faça sentido para ele.

## Objetivos

- Distinguir um texto entre aspas de um número escrito sem aspas.
- Usar `true` e `false` para representar se uma tarefa está concluída.
- Usar `typeof` para conferir o tipo de cada valor no console.

## Pré-requisitos

Use a pasta `meus-estudos`, com `index.html` e `script.js` conectados como na aula 02. Abra o VSCode e, no navegador, sua página com a aba **Console**. Vamos retomar `let`, `const` e `console.log` da aula 03. Todo o código novo será escrito em **`script.js`**.

## Desenvolvimento

### 1. Retome o nome e o valor

Substitua o conteúdo do **`script.js`** pelo exemplo abaixo. Salve com **Ctrl + S** e atualize sua página no navegador com **Ctrl + R**.

```javascript
const nomeEstudante = "Ana";
let tarefaAtual = "Revisar HTML";
console.log(nomeEstudante);
console.log(tarefaAtual);
```

Você deve encontrar **Ana** e **Revisar HTML** no console, nessa ordem. `const` impede reatribuir outro valor ao nome declarado; `let` permite reatribuir. As palavras entre aspas são os valores guardados, e os nomes sem aspas em `console.log` permitem consultá-los.

A página continua mostrando seu HTML e suas cores de CSS. Para alterar o título visível, você ainda edita o texto dentro de `<h1>`; para alterar a cor, edita a regra CSS. Nesta aula, vamos observar os dados no console.

### 2. Distinga texto e número

Substitua o conteúdo do **`script.js`** por este exemplo completo. Salve e atualize.

```javascript
const tarefa = "Estudar matemática";
const minutosDeEstudo = 20;
console.log(tarefa);
console.log(minutosDeEstudo);
```

O console mostra **Estudar matemática** e **20**. O texto foi escrito entre aspas. O número foi escrito sem aspas e sem a palavra “minutos” junto dele.

:::conceito String e number
**`string`** é o nome do tipo usado para textos. Aqui, `"Estudar matemática"` e `"20"` são strings porque foram escritos entre aspas. **`number`** é o tipo numérico: `20` e `2.5`, sem aspas, são exemplos. No código JavaScript, escreva o ponto para separar a parte decimal, como em `2.5`.
:::

Para guardar 20 minutos como número, use `const minutosDeEstudo = 20;`. Se você escrever `const minutosDeEstudo = "20";`, estará guardando um texto, mesmo que esse texto contenha somente algarismos. O nome da variável ajuda a leitura, mas **não determina o tipo do valor**.

Escolha um campo de cada vez: a descrição da tarefa é texto; a quantidade de minutos é número. Na próxima aula, essa distinção vai ajudar você a entender os cálculos.

### 3. Represente sim ou não com um booleano

Substitua o conteúdo do **`script.js`** pelo exemplo abaixo. Antes de executar, diga à sua dupla quais serão as duas mensagens.

```javascript
let tarefaConcluida = false;
console.log(tarefaConcluida);

tarefaConcluida = true;
console.log(tarefaConcluida);
```

Salve e atualize. O console mostra **false** primeiro e **true** depois. Você já viu essa troca na aula 03: a variável criada com `let` recebe outro valor durante a execução.

:::conceito Booleano
Um **booleano**, chamado `boolean` no JavaScript, tem dois valores possíveis: **`true`** (verdadeiro) e **`false`** (falso). Para a pergunta “a tarefa está concluída?”, usamos `false` quando a resposta é não e `true` quando a resposta é sim. Escreva essas palavras em inglês, em letras minúsculas e sem aspas.
:::

`false` não significa erro no programa. Neste exemplo, é uma informação válida: a tarefa ainda não foi concluída. `"false"`, com aspas, seria apenas um texto. `"sim"` e `"não"` também seriam textos, não valores booleanos.

:::atencao A tradução não é o comando
**Sintoma:** depois de escrever `let tarefaConcluida = verdadeiro;`, o console aponta que `verdadeiro` não foi definido.

**Solução:** use o valor do JavaScript `true`, sem aspas. Para falso, use `false`. O idioma do texto da tarefa pode ser português, mas esses dois valores da linguagem são escritos em inglês. Salve e atualize após corrigir.
:::

### 4. Use typeof para conferir o tipo

Às vezes, só olhar o resultado no console não deixa claro se você tem `20` ou `"20"`. Podemos pedir ao JavaScript que informe o tipo do valor. Substitua o conteúdo do **`script.js`** pelo programa abaixo:

```javascript
const minutosComoNumero = 20;
const minutosComoTexto = "20";
const tarefaConcluida = false;

console.log(typeof minutosComoNumero);
console.log(typeof minutosComoTexto);
console.log(typeof tarefaConcluida);
```

Salve e atualize. Você deve encontrar estas palavras, nesta ordem:

```txt
number
string
boolean
```

O **`typeof`** é um operador que informa o tipo do valor. Em `console.log(typeof minutosComoNumero);`, o programa consulta o valor de `minutosComoNumero`, verifica seu tipo e mostra o resultado. Escreva `typeof`, um espaço e o nome da variável, como no modelo.

Para os três tipos estudados hoje, leia assim: **`number` = número; `string` = texto; `boolean` = booleano**. Essas palavras são o resultado da consulta de tipo. Para ver o próprio valor, você continua usando, por exemplo, `console.log(minutosComoNumero);`.

:::atencao Eu esperava um número, mas apareceu string
**Sintoma:** `typeof minutosDeEstudo` mostra `string`, embora você queira guardar uma quantidade numérica.

**Solução:** confira a declaração. Se ela está como `const minutosDeEstudo = "20";`, as aspas tornam esse valor um texto. Neste exercício, corrija o valor inicial no arquivo para `20`, sem aspas, salve e atualize. Isso é uma edição do seu código; as funções que convertem textos recebidos pelo programa serão estudadas depois.
:::

:::dica Informações bem representadas facilitam o trabalho
Ao desenvolver uma lista de tarefas, você precisa distinguir a descrição, a duração e a situação de conclusão. Use texto para a descrição, número para a quantidade e booleano para a resposta de sim ou não. `typeof` ajuda a conferir se o valor foi escrito como você pretendia antes de construir cálculos e decisões.
:::

## Prática

### Uma ficha para sua tarefa

Substitua o conteúdo do **`script.js`** pelo programa abaixo. Ele mostra o valor e, na linha seguinte, o tipo de cada informação.

```javascript
const tarefa = "Revisar HTML";
const minutosDeEstudo = 20;
let tarefaConcluida = false;

console.log(tarefa);
console.log(typeof tarefa);
console.log(minutosDeEstudo);
console.log(typeof minutosDeEstudo);
console.log(tarefaConcluida);
console.log(typeof tarefaConcluida);
```

1. Troque o texto da tarefa por algo que você precisa estudar e escolha uma quantidade de minutos. Escreva a tarefa entre aspas e o número de minutos sem aspas.
2. Antes de executar, preveja as seis mensagens. Salve, atualize e confira valor e tipo de cada informação.
3. Troque o valor inicial `false` por `true` no arquivo, como se a tarefa já estivesse concluída. Salve e atualize. Confira que o valor mudou, mas o tipo continua `boolean`.
4. Coloque aspas somente em volta do número de minutos no código, salve e atualize. Confira que o tipo agora é `string`. Depois retire essas aspas, salve e atualize para terminar com uma quantidade numérica.

### Confira antes de entregar

Com os valores originais do exemplo, o resultado é:

```txt
Revisar HTML
string
20
number
false
boolean
```

Na sua versão final, a tarefa e os minutos podem ser diferentes; a tarefa deve ter tipo `string`, os minutos devem ter tipo `number` e a conclusão deve ter tipo `boolean`. Você pode terminar com `true` ou `false`, conforme a situação que escolheu representar. Mostre o código e as seis mensagens para o professor e guarde os arquivos.

## Avaliação

Pense no valor escrito no código. Se precisar, use `typeof` no seu arquivo para conferir sua resposta e depois restaure a versão final da prática.

```quiz
- pergunta: Qual declaração guarda a quantidade de minutos como number?
  alternativas:
    - texto: 'const minutosDeEstudo = "20";'
    - texto: 'const minutosDeEstudo = 20;'
      correta: true
    - texto: 'const minutosDeEstudo = "20 minutos";'
  feedback: >
    O número 20 sem aspas é number. Os valores entre aspas são strings, mesmo quando contêm algarismos ou a palavra minutos.
- pergunta: Você quer guardar que uma tarefa ainda não foi concluída usando um booleano. Qual declaração representa isso?
  alternativas:
    - texto: 'let tarefaConcluida = "false";'
    - texto: 'let tarefaConcluida = "não";'
    - texto: 'let tarefaConcluida = false;'
      correta: true
  feedback: >
    false sem aspas é um valor booleano que aqui representa a tarefa não concluída. Com aspas, false e não são textos.
- pergunta: Depois de const minutosDeEstudo = "20";, qual resultado console.log(typeof minutosDeEstudo); mostra?
  alternativas:
    - texto: string
      correta: true
    - texto: number
    - texto: boolean
  feedback: >
    As aspas definem esse valor como texto. typeof informa string, mesmo que o nome da variável indique minutos. O nome não transforma o tipo do valor.
```

## Fechamento

- **Texto:** valores entre aspas, como `"Revisar HTML"` e `"20"`, são do tipo `string`.
- **Número:** valores como `20` e `2.5`, sem aspas, são do tipo `number`.
- **Booleano:** `true` e `false`, sem aspas, representam verdadeiro e falso.
- **Conferência:** `typeof` informa o tipo do valor; `console.log` permite observar o resultado.

Na próxima aula, vamos usar números em cálculos e entender por que o sinal `+` pode somar números ou juntar textos.

:::roteiro
0–6 min: retomar variáveis, console e papel de HTML/CSS. 6–17 min: texto e número com descrição e minutos, comparando valores com e sem aspas. 17–27 min: booleano e reatribuição de false para true; verificar que falso não significa erro. 27–35 min: typeof e previsão de resultados para 20 e "20". 35–45 min: prática com ficha da tarefa, incluindo mudança de aspas e restauração do número. 45–50 min: quiz e fechamento. Adaptação da base de tipos/conversão do RCO 80 e das retomadas do RCO 90 ao plano: conversões e operações ficam para a aula 05; a preparação adiciona booleanos explícitos e uma conferência de tipos. Não sugerir que const determina tipo ou que string se limita a letras. Não introduzir null, undefined, arrays, objetos, coerção ou operadores de comparação nesta aula. Se houver filtro no console, usar o diagnóstico da aula 02.
:::
