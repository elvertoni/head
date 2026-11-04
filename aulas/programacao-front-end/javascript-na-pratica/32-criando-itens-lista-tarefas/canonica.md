---
titulo: Criando tarefas na lista da página
tema: JavaScript na prática
disciplina: programacao-front-end
serie: 2ª
prerequisitos: [Tratar submit, Recusar texto vazio, Localizar elementos e alterar textContent]
objetivos:
  - Criar um elemento li com document.createElement
  - Preencher seu texto e inseri-lo na lista com appendChild
  - Adicionar um item novo por envio válido sem apagar os anteriores
trilha: javascript-na-pratica
ordem: 32
slug: criando-itens-lista-tarefas
modo_origem: seed
fontes: [docs/plano-apostila-javascript.md]
revisao: true
status: aprovada
versao: 2
atualizado_em: 2026-11-04
---

Seu formulário já recebe uma tarefa e avisa quando o campo está vazio. Hoje, cada tarefa aceita vai ganhar um item próprio na lista. É como acrescentar uma linha em uma folha de planejamento: você mantém o que já escreveu e adiciona a próxima tarefa abaixo. A página vai começar com uma lista vazia e crescer a cada envio válido.

## Objetivos

- Criar um elemento `li` usando JavaScript.
- Colocar o texto da tarefa nesse elemento e inseri-lo na lista.
- Repetir o envio sem substituir os itens anteriores nem aceitar texto vazio.

## Pré-requisitos

Abra `meus-estudos` no VSCode e no navegador. Vamos retomar o formulário, `submit`, `preventDefault`, `trim` e `if`/`else` da aula 31. Você vai editar `index.html` e `script.js`; o CSS pode permanecer igual. Tenha o console aberto para conferir erros se algo não aparecer.

## Desenvolvimento

### 1. Prepare uma lista vazia identificada

No **`index.html`**, substitua **a lista inteira antiga**, incluindo os dois itens fixos, por esta linha, depois do parágrafo de mensagem:

```html
<ul id="lista-tarefas"></ul>
```

O `ul` marca uma lista com marcadores, como na aula 19. O `li` marca cada item. Desta vez os itens serão criados pelo JavaScript. O `id` permite localizar a lista em que você quer colocá-los.

No botão de envio, troque o texto visível para **Adicionar tarefa**, mantendo `type="submit"`. Para recuperar a base se estiver sem o HTML, este é o arquivo completo. **Use-o inteiro somente em um arquivo vazio**; na página existente, faça as trocas indicadas.

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

Salve o HTML. O JavaScript da aula 31 ainda pode confirmar o texto, mas não cria um item. Vamos aprender essa parte antes de integrá-la ao formulário.

### 2. Crie, escreva e coloque na página

No **`script.js`**, substitua o conteúdo anterior por este pequeno exemplo:

```javascript
const item = document.createElement("li");
item.textContent = "Revisar HTML";
```

Salve e atualize. **A lista ainda não mostra esse item.** `document.createElement("li")` criou um elemento na memória, e `textContent` colocou um texto nele, mas ainda falta inseri-lo na lista da página.

Agora substitua o conteúdo do **`script.js`** pelo programa completo abaixo:

```javascript
const lista = document.getElementById("lista-tarefas");
const item = document.createElement("li");
item.textContent = "Revisar HTML";
lista.appendChild(item);
```

Salve e atualize. A lista deve mostrar um marcador com **Revisar HTML**. O programa executa essa criação ao carregar o arquivo. Por enquanto, enviar o formulário não acrescenta outro item, pois substituímos o programa que tratava o envio.

:::conceito Criar não é inserir
**`createElement("li")` cria** um novo elemento de item. **`item.textContent` preenche** seu texto. **`lista.appendChild(item)` insere** esse elemento como filho da lista, depois dos itens que já existirem. São etapas diferentes da mesma ação.
:::

Escreva `"li"` sem os sinais `<` e `>` em `createElement`. A lista já existente é localizada por `getElementById`; o item novo é criado por `createElement`.

### 3. Crie um item para cada envio válido

Substitua o conteúdo de **`script.js`** pelo programa completo abaixo. Agora voltamos ao formulário, mantendo a verificação da aula 31.

```javascript
function adicionarTarefa(evento) {
  evento.preventDefault();

  const campo = document.getElementById("campo-tarefa");
  const mensagem = document.getElementById("mensagem");
  const lista = document.getElementById("lista-tarefas");
  const tarefa = campo.value.trim();

  if (tarefa === "") {
    mensagem.textContent = "Digite uma tarefa.";
  } else {
    const item = document.createElement("li");
    item.textContent = tarefa;
    lista.appendChild(item);
    mensagem.textContent = "Tarefa adicionada.";
    campo.value = "";
  }
}

const formulario = document.getElementById("formulario-tarefa");
formulario.addEventListener("submit", adicionarTarefa);
```

Salve os dois arquivos e atualize. Digite **Revisar HTML** e envie. Deve aparecer um item na lista, a confirmação **Tarefa adicionada.** e o campo vazio. Digite **Praticar CSS** e envie. Agora devem existir **dois itens**, na ordem dos envios.

A linha `campo.value = "";` escreve um texto vazio no campo depois do sucesso. Aqui usamos a mesma propriedade da aula 30, agora para alterar o campo. A tarefa já foi copiada para o texto do novo item antes da limpeza.

Observe que a criação acontece dentro do `else`, **a cada envio válido**. Se o texto estiver vazio, o programa só orienta o preenchimento e não acrescenta item.

### 4. Teste crescimento e estado inicial

Envie mais uma tarefa e confira se as anteriores continuam. Depois envie com o campo vazio e só com espaços: deve aparecer **Digite uma tarefa.**, sem criar novos marcadores.

Atualize a página. A lista volta a ficar vazia porque o HTML salvo contém um `ul` sem itens. O programa desta aula altera o documento carregado, mas não grava tarefas em arquivo ou armazenamento permanente. Se o navegador restaurar o texto do campo, confira e apague esse texto antes de começar um novo teste; o estado da lista continua sendo o definido pelo programa.

:::atencao Só uma tarefa aparece e seu texto vai mudando
**Sintoma:** ao enviar a segunda tarefa, o primeiro item é substituído em vez de aparecer outro.

**Solução:** confira se `document.createElement("li")` está dentro da função, no caminho do texto válido, como no exemplo. Cada envio precisa de um elemento novo. Não use `lista.textContent = tarefa`, porque isso substitui o conteúdo da lista. Salve, atualize e teste com duas tarefas diferentes.
:::

:::atencao Criei o item, mas ele não apareceu
**Sintoma:** você tem um `li` com texto no código, mas não há marcador na página.

**Solução:** confira a chamada `lista.appendChild(item)` e se a busca da lista corresponde a `id="lista-tarefas"`. Criar o elemento não o coloca automaticamente na página. Verifique erros no console, salve e atualize.
:::

:::dica Separe entrada, conferência e apresentação
Ao construir uma interface, primeiro leia a entrada, confira se ela é aceitável e só então altere a apresentação. Aqui, o texto é tratado por `trim`, validado pelo `if` e inserido como texto de um novo item. Essa organização ajuda a identificar em qual etapa uma falha aconteceu.
:::

## Prática

### Monte sua lista de estudos

Use o **programa completo da etapa 3** e o `ul` vazio com `id="lista-tarefas"` no HTML.

1. Atualize para começar com a lista vazia e confira o campo antes de digitar.
2. Envie três tarefas reais, uma por vez, usando o botão ou Enter. Confira os três itens e a ordem.
3. Envie o campo vazio e depois só com espaços. Confira que a quantidade de itens não aumenta.
4. Explique à dupla quais linhas criam, preenchem e inserem cada item e por que a criação fica no caminho da tarefa válida.

### Confira antes de entregar

A lista deve ter um item por envio válido, preservando os anteriores. O campo deve ser limpo após cada sucesso, e envios vazios não devem criar marcadores. Mostre os testes ao professor antes de atualizar, pois a lista ainda é temporária. Guarde os arquivos para a aula 33.

## Avaliação

Considere o formulário e a lista identificada da aula.

```quiz
- pergunta: Qual instrução cria um novo elemento de item de lista?
  alternativas:
    - texto: 'document.getElementById("li")'
    - texto: 'document.createElement("li")'
      correta: true
    - texto: 'console.log("li")'
  feedback: >
    createElement cria um elemento do tipo informado. getElementById procura um elemento já existente pelo id; console.log mostra uma informação no console.
- pergunta: O item já foi criado e recebeu um texto. Qual ação o coloca no final da lista?
  alternativas:
    - texto: lista.appendChild(item);
      correta: true
    - texto: campo.value = "";
    - texto: 'item.textContent = "Tarefa";'
  feedback: >
    appendChild insere o elemento na lista. Limpar o campo e escrever texto no item não fazem essa inserção.
- pergunta: Em qual momento o programa completo cria o novo li?
  alternativas:
    - texto: Uma única vez fora da função, para reutilizar o mesmo item
    - texto: Sempre que o campo estiver vazio
    - texto: Dentro da função, no caminho em que a tarefa foi aceita
      correta: true
  feedback: >
    Cada envio válido cria um elemento novo. Isso permite preservar os itens anteriores, enquanto o caminho vazio só mostra uma orientação.
```

## Fechamento

- **`createElement("li")` cria** um novo item na memória.
- **`textContent` preenche** o texto do item.
- **`appendChild` insere** o item na lista sem apagar os anteriores.
- Crie o item **após validar cada envio**; a lista desta etapa é temporária.

Na próxima aula, vamos guardar várias tarefas em um array e consultar seus valores por posição.

:::roteiro
0–8 min: retomar form e trocar lista fixa por ul vazio identificado. 8–20 min: criar sem inserir, depois acrescentar appendChild e conferir a diferença. 20–33 min: integrar o envio com validação conhecida; criar um elemento novo dentro do caminho válido e limpar o campo depois. 33–45 min: prática e testes negativos. 45–50 min: quiz e fechamento. Adaptação da criação de elementos do RCO 94/95 ao plano: um li por tarefa textual, sem array ainda. Não introduzir innerHTML, templates, laços, remoção ou persistência. Explicar que o exemplo isolado substitui temporariamente o tratamento do formulário; o código completo da etapa 3 é o programa final.
:::
