---
titulo: Guardando informações com let e const
tema: JavaScript na prática
disciplina: programacao-front-end
serie: 2ª
prerequisitos: [Conectar script.js ao HTML, Conferir mensagens no console]
objetivos:
  - Guardar e consultar informações usando variáveis com nomes claros
  - Reatribuir um valor usando let e prever a saída no console
  - Escolher entre let e const conforme a necessidade de reatribuição
trilha: javascript-na-pratica
ordem: 3
slug: variaveis-let-const-nos-estudos
modo_origem: seed
fontes: [docs/plano-apostila-javascript.md]
revisao: true
status: aprovada
versao: 1
atualizado_em: 2026-11-03
---

Na sua lista de estudos, algumas informações vão mudar: a tarefa que você está fazendo agora, por exemplo. Outras podem ficar iguais durante a execução, como o nome do estudante. Hoje você vai dar nomes a essas informações e conferir seus valores no console. Pense em uma etiqueta no caderno: ela ajuda você a encontrar a informação sem precisar adivinhar onde está.

## Objetivos

- Guardar uma informação em uma variável e mostrar seu valor no console.
- Trocar o valor de uma variável criada com `let` e prever o resultado.
- Usar `const` quando não pretende reatribuir o valor e `let` quando precisa reatribuir.

## Pré-requisitos

Abra a pasta `meus-estudos` no VSCode e o `index.html` no navegador. Tenha a aba **Console** aberta nas ferramentas do desenvolvedor, como na aula 02. Seu HTML deve conter `<script src="script.js"></script>` antes de `</body>`, e os dois arquivos devem estar na mesma pasta. Se precisar reconstruir a conexão, retome o passo a passo da aula 02.

## Desenvolvimento

### 1. Retome uma mensagem que você já sabe executar

No VSCode, abra **`script.js`**. Vamos usar esse mesmo arquivo, mantendo o HTML e o CSS da sua página. Substitua o conteúdo de `script.js` pela linha abaixo. Salve com **Ctrl + S**, volte ao navegador e atualize com **Ctrl + R**.

```javascript
console.log("Revisar HTML");
```

O console deve mostrar **Revisar HTML**. A página continua com sua lista e suas cores: esse comando escreve no console. Lembre que o texto entre `<li>` e `</li>` é conteúdo do HTML e a regra `color` é aparência definida pelo CSS. Hoje, os testes acontecem no JavaScript.

### 2. Guarde a tarefa com um nome

Agora substitua **todo o conteúdo de `script.js`** por este exemplo. Salve e atualize.

```javascript
let tarefaAtual = "Revisar HTML";
console.log(tarefaAtual);
```

O resultado continua sendo **Revisar HTML**, mas agora a mensagem veio de uma informação guardada com o nome `tarefaAtual`.

:::conceito Variável
Uma **variável** associa um nome a um valor que seu programa pode consultar. Em `let tarefaAtual = "Revisar HTML";`, você cria o nome `tarefaAtual` e atribui a ele o texto `Revisar HTML`. O sinal `=` faz essa atribuição; aqui ele não está comparando duas coisas.
:::

`let` é uma palavra do JavaScript usada para criar essa variável. `tarefaAtual` é o nome que escolhemos. Usamos um nome sem espaços que descreve a informação guardada; a letra maiúscula no começo da segunda palavra ajuda a separar a leitura.

Observe a diferença: `console.log(tarefaAtual);` consulta o valor associado ao nome. Já `console.log("tarefaAtual");` mostra literalmente a palavra **tarefaAtual**, porque ela está entre aspas. Quando quiser consultar a variável, escreva seu nome **sem aspas**.

### 3. Troque o valor com let

Substitua o conteúdo do **`script.js`** pelo exemplo abaixo. Antes de executar, tente prever as duas mensagens.

```javascript
let tarefaAtual = "Revisar HTML";
console.log(tarefaAtual);

tarefaAtual = "Praticar CSS";
console.log(tarefaAtual);
```

Salve e atualize. As mensagens aparecem nesta ordem:

```txt
Revisar HTML
Praticar CSS
```

O navegador executou as linhas de cima para baixo. Primeiro guardou `Revisar HTML` e mostrou esse valor. Depois, `tarefaAtual = "Praticar CSS";` atribuiu outro valor ao mesmo nome. Essa troca é chamada de **reatribuição**. A mensagem que já foi mostrada antes não muda; a segunda consulta usa o novo valor.

Na primeira linha, usamos `let` para criar a variável. Na troca, escrevemos só o nome e o novo valor. **Não repita `let` para reatribuir a mesma variável nesse trecho.**

:::atencao O nome já foi declarado
**Sintoma:** depois de juntar exemplos, o console aponta um erro como `Identifier 'tarefaAtual' has already been declared`.

**Solução:** confira se você colou dois exemplos um abaixo do outro e criou `let tarefaAtual` duas vezes no mesmo trecho. Use um exemplo completo de cada vez. Para trocar o valor depois da declaração, escreva apenas `tarefaAtual = "Praticar CSS";`. Salve e atualize a página.
:::

### 4. Use const quando não houver reatribuição

Substitua o conteúdo do **`script.js`** por este exemplo. Salve e atualize.

```javascript
const nomeEstudante = "Ana";
console.log(nomeEstudante);
```

O console mostra **Ana**. O `const` também cria uma variável com nome e valor, mas **não permite reatribuir outro valor a esse nome**. Neste programa, escolhemos manter o nome do estudante durante a execução.

Você pode trocar `Ana` pelo seu nome **no código**, salvar e atualizar. Isso funciona: a atualização inicia uma nova execução usando o arquivo que você salvou. É diferente de mandar o programa reatribuir um valor durante a mesma execução.

:::atencao Tentativa de reatribuir uma const
**Sintoma:** após criar `const nomeEstudante = "Ana";`, você acrescenta `nomeEstudante = "Bia";` e o console aponta um erro como `Assignment to constant variable`.

**Solução:** se a lógica precisa dessa troca durante a execução, use `let` na declaração inicial. Se a informação deve permanecer sem reatribuição, mantenha `const` e retire a linha que tenta reatribuir. Usar `const` não impede você de editar o arquivo e iniciar uma nova execução.
:::

:::dica Nomes que ajudam quem vai ler seu código
Ao desenvolver uma página, você volta ao código para corrigir e acrescentar recursos. `tarefaAtual` explica mais que `x`. Escolha um nome claro e use `const` quando não precisar reatribuir; use `let` quando a mudança fizer parte da lógica. Escreva o nome sempre do mesmo jeito: `tarefaAtual` e `TarefaAtual` são nomes diferentes.
:::

## Prática

### Seu nome e a próxima tarefa

No **`script.js`**, substitua o conteúdo pelo programa completo abaixo. Troque `Ana` pelo seu primeiro nome. Depois, execute e confira as três mensagens.

```javascript
const nomeEstudante = "Ana";
let tarefaAtual = "Revisar HTML";

console.log(nomeEstudante);
console.log(tarefaAtual);

tarefaAtual = "Praticar CSS";
console.log(tarefaAtual);
```

1. Mostre para sua dupla qual linha cria o nome do estudante e qual cria a tarefa atual.
2. Troque somente os dois textos das tarefas por atividades reais da sua semana.
3. Antes de atualizar, diga quais serão as três mensagens e em que ordem aparecerão.
4. Salve, atualize e confira. Explique por que escolhemos `let` para a tarefa e `const` para o nome neste programa.

### Confira antes de entregar

O console deve mostrar seu nome, a primeira tarefa e a segunda tarefa, nessa ordem. No exemplo original, o resultado é:

```txt
Ana
Revisar HTML
Praticar CSS
```

Seu HTML continua conectado ao mesmo `script.js`. Mostre os arquivos e a execução para o professor e guarde a pasta. Você ainda não está alterando automaticamente as tarefas visíveis na página; isso será construído nas aulas de interação com o HTML.

## Avaliação

Responda pensando na execução das linhas, e não apenas na palavra usada para declarar a variável.

```quiz
- pergunta: Você criou let tarefaAtual = "Revisar HTML"; e quer mostrar o valor guardado nessa variável. Qual comando deve usar?
  alternativas:
    - texto: 'console.log("tarefaAtual");'
    - texto: 'console.log(tarefaAtual);'
      correta: true
    - texto: 'console.log("let");'
  feedback: >
    Sem aspas, tarefaAtual consulta a variável e mostra seu valor. Entre aspas, tarefaAtual e let são apenas os textos que serão mostrados.
- pergunta: O programa cria let tarefaAtual = "Revisar HTML";, mostra tarefaAtual, reatribui "Praticar CSS" e mostra tarefaAtual de novo. Quais mensagens aparecem?
  alternativas:
    - texto: Praticar CSS nas duas mensagens
    - texto: Revisar HTML nas duas mensagens
    - texto: Revisar HTML primeiro e Praticar CSS depois
      correta: true
  feedback: >
    A primeira consulta ocorre antes da reatribuição. A segunda usa o novo valor. Trocar o valor não reescreve a mensagem já mostrada.
- pergunta: Seu programa precisa trocar a tarefa atual durante a mesma execução. Qual opção permite criar e depois reatribuir essa variável?
  alternativas:
    - texto: Criar com let e depois usar tarefaAtual = "Outra tarefa";
      correta: true
    - texto: Criar com const e depois atribuir outro texto ao mesmo nome
    - texto: Repetir let tarefaAtual a cada troca no mesmo trecho
  feedback: >
    let permite reatribuição. const impede atribuir outro valor ao mesmo nome, e repetir a declaração com let no mesmo trecho causa conflito de declaração.
```

## Fechamento

- Uma **variável** associa um nome a um valor; use nomes que expliquem a informação.
- **`console.log(tarefaAtual)`** consulta a variável; com aspas, você mostra um texto literal.
- **`let` permite reatribuição:** declare uma vez e use o nome para atribuir o próximo valor.
- **`const` impede reatribuição:** editar o arquivo e atualizar inicia outra execução.

Na próxima aula, vamos reconhecer três tipos de valores que essas variáveis podem guardar: textos, números e booleanos.

:::roteiro
0–7 min: retomar arquivo, console e separação entre conteúdo HTML e aparência CSS. 7–17 min: associar nome e valor, comparar a consulta com e sem aspas. 17–27 min: executar reatribuição e prever a saída antes de atualizar. 27–34 min: const e diferença entre editar a fonte e reatribuir durante a execução. 34–44 min: prática com nome e duas tarefas. 44–50 min: quiz, conferência e fechamento. Adaptação das aulas RCO 79 e 81 ao plano: escopo e imutabilidade de estruturas ficam para depois; esta etapa trata somente de declaração, consulta e reatribuição de textos. As advertências esclarecem const sem equiparar proteção do nome a imutabilidade geral de dados. Se aparecer erro de nome, compare letra por letra sem acrescentar novos conceitos. Não introduzir var, funções, arrays ou manipulação do DOM.
:::
