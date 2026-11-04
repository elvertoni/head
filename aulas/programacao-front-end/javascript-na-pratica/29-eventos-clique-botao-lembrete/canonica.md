---
titulo: Um botão que mostra seu lembrete
tema: JavaScript na prática
disciplina: programacao-front-end
serie: 2ª
prerequisitos: [Definir uma função, Localizar um elemento pelo id, Alterar textContent]
objetivos:
  - Criar e localizar um botão com id próprio
  - Registrar uma função para responder ao evento click com addEventListener
  - Conferir que a mensagem muda após a ativação do botão e volta ao estado inicial ao atualizar
trilha: javascript-na-pratica
ordem: 29
slug: eventos-clique-botao-lembrete
modo_origem: seed
fontes: [docs/plano-apostila-javascript.md]
revisao: true
status: aprovada
versao: 2
atualizado_em: 2026-11-04
---

Sua página já consegue mostrar um lembrete com JavaScript. Hoje você vai deixar a escolha do momento para quem usa a página: o texto só muda quando o botão “Mostrar lembrete” é ativado. Pense na campainha: instalar o botão não é tocar a campainha. Você prepara a ação e espera alguém apertar.

## Objetivos

- Criar um botão e localizá-lo pelo `id`.
- Usar `addEventListener` para associar o clique à função do lembrete.
- Testar o estado inicial, o clique e a atualização da página.

## Pré-requisitos

Abra a pasta `meus-estudos` no VSCode e sua página no navegador. Mantenha o console disponível para conferir erros. Você vai editar **`index.html` e `script.js`**, retomando o parágrafo `id="mensagem"`, a função sem parâmetros e a propriedade `textContent` da aula 28. O CSS pode continuar o mesmo.

## Desenvolvimento

### 1. Retome a função e retire a execução automática

No **`script.js`**, substitua o conteúdo anterior pelo código abaixo. Ele tem a definição da função, mas não tem a chamada que executava o lembrete ao carregar a página.

```javascript
function mostrarLembrete() {
  const mensagem = document.getElementById("mensagem");
  mensagem.textContent = "Hora de revisar HTML!";
}
```

Salve com **Ctrl + S** e atualize a página com **Ctrl + R**. O parágrafo deve mostrar o texto inicial do HTML: **Escolha uma tarefa para começar.**. Se você personalizou a mensagem na aula anterior, use essa frase como texto inicial do parágrafo para os testes de hoje.

Como vimos na aula 27, definir uma função não executa seu corpo. Hoje o clique vai disparar a ação no momento escolhido pelo usuário.

### 2. Acrescente e localize o botão

No **`index.html`**, insira esta linha **logo depois do parágrafo com `id="mensagem"` e antes da lista**. Acrescente apenas um botão.

```html
<button type="button" id="botao-lembrete">Mostrar lembrete</button>
```

`button` cria um botão nativo da página. O `type="button"` especifica um botão de ação. O `id="botao-lembrete"` permite localizar esse elemento; o texto entre as tags será o rótulo visível.

Mantenha `<script src="script.js"></script>` **depois do parágrafo, do botão e da lista, antes de `</body>`**. Se precisar recuperar a base, este é o HTML completo. **Use-o inteiro somente em um `index.html` vazio**; se já tem sua página, preserve suas personalizações e insira apenas o botão no local indicado.

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
  <button type="button" id="botao-lembrete">Mostrar lembrete</button>
  <ul>
    <li>Revisar HTML</li>
    <li>Praticar CSS</li>
  </ul>
  <script src="script.js"></script>
</body>
</html>
```

Salve o HTML. Para conferir a busca do botão, substitua o conteúdo de **`script.js`** por este pequeno teste:

```javascript
const botaoLembrete = document.getElementById("botao-lembrete");
console.log(botaoLembrete.textContent);
```

Salve e atualize. O botão aparece na página, e o console mostra **Mostrar lembrete**. Clicar nele ainda não muda a mensagem: nosso teste apenas localizou o botão e consultou seu texto. Vamos ligar o clique à ação.

### 3. Registre a função para o clique

Substitua o conteúdo de **`script.js`** pelo programa completo abaixo:

```javascript
function mostrarLembrete() {
  const mensagem = document.getElementById("mensagem");
  mensagem.textContent = "Hora de revisar HTML!";
}

const botaoLembrete = document.getElementById("botao-lembrete");
botaoLembrete.addEventListener("click", mostrarLembrete);
```

Salve e atualize. Primeiro confira que o parágrafo ainda mostra **Escolha uma tarefa para começar.**. Depois clique no botão. Agora ele deve mostrar **Hora de revisar HTML!**.

:::conceito Evento e ação
Um **evento** avisa que algo aconteceu na página. O evento `"click"` sinaliza a ativação por clique do botão. `addEventListener` registra qual função deve ser executada quando esse evento ocorrer. Aqui você registra a função `mostrarLembrete` no botão encontrado.
:::

Leia a última linha como “quando este botão receber um clique, execute `mostrarLembrete`”. O nome `click` fica entre aspas; depois vem uma vírgula e o nome da função.

Observe que escrevemos **`mostrarLembrete` sem `()` nessa linha**. Você está entregando a função para ser chamada quando o evento ocorrer. Na aula 28, `mostrarLembrete();` fazia a execução imediatamente ao chegar àquela linha. Agora queremos esperar pelo clique.

:::atencao O lembrete aparece antes de clicar
**Sintoma:** você atualiza a página e a mensagem já está trocada, antes de usar o botão.

**Solução:** retire uma eventual chamada direta `mostrarLembrete();` que tenha sobrado da aula 28. Na linha de `addEventListener`, confira que está `mostrarLembrete` sem parênteses. Se você escrever `mostrarLembrete()` ali, estará executando a função naquele momento, em vez de registrar a própria função como ação. Salve e atualize para testar desde o início.
:::

### 4. Teste o começo, o clique e a atualização

Depois de salvar os dois arquivos, faça a sequência completa: **atualize → observe a mensagem inicial → clique → observe o lembrete**. Clique outra vez: a função é executada novamente, mas você continua vendo o mesmo lembrete, pois ela atribui o mesmo texto. Este botão não alterna entre duas mensagens.

Você também pode testar pelo teclado: pressione **Tab** até o botão receber foco e depois **Enter** ou **Espaço**. Por ser um botão nativo, ele permite essa ativação pelo teclado e dispara a ação registrada no clique.

Atualize novamente. A frase inicial reaparece porque o navegador recarregou o HTML, e agora a função está aguardando outro clique. A troca feita no documento carregado não reescreveu o arquivo HTML nem foi salva como um dado permanente.

:::atencao O botão aparece, mas a mensagem não muda
**Sintoma:** o botão está visível, mas a ação esperada não acontece.

**Solução:** abra o console e confira os nomes. O HTML precisa ter `id="botao-lembrete"` e o JavaScript precisa buscar esse mesmo texto; a mensagem precisa ter `id="mensagem"`. O evento deve ser `"click"`, sem traduzir para português. Confira a conexão com `script.js`, a posição da tag após os elementos e se os dois arquivos foram salvos. Atualize e teste novamente. Se o clique repetido não produzir uma mudança visual adicional, lembre que a ação escreve o mesmo texto.
:::

:::dica Uma ação preparada, um momento de execução
Em interfaces, funções organizam o que fazer e eventos ajudam a decidir quando fazer. Manter a função com nome facilita localizar a ação registrada no botão. Prefira o elemento `button` para uma ação de botão: ele já oferece comportamento esperado para quem navega com teclado.
:::

## Prática

### Seu lembrete ao clicar

Mantenha o parágrafo e o botão no HTML. Substitua o conteúdo de **`script.js`** pelo programa completo abaixo:

```javascript
function mostrarLembrete() {
  const mensagem = document.getElementById("mensagem");
  mensagem.textContent = "Minha próxima tarefa é revisar HTML.";
}

const botaoLembrete = document.getElementById("botao-lembrete");
botaoLembrete.addEventListener("click", mostrarLembrete);
```

1. Execute o exemplo: atualize e confira a mensagem inicial antes de clicar; depois clique e confira o lembrete.
2. Troque somente o texto dentro da função por uma tarefa real sua. Salve, atualize e repita o teste completo.
3. Ative o botão pelo teclado com Tab e Enter ou Espaço. Confira que ele executa a mesma ação.
4. Mostre à dupla a função que define a ação e a linha que registra o momento de executá-la. Explique por que não há uma chamada direta no final do arquivo.

### Confira antes de entregar

Antes da ativação, a página deve mostrar a mensagem inicial do HTML. Depois da ativação, deve mostrar seu lembrete personalizado. Um segundo clique mantém esse mesmo texto, e atualizar restaura a mensagem inicial. O título e a lista continuam presentes. Mostre esses estados e o console sem erros do seu código ao professor e guarde a pasta para a aula 30.

## Avaliação

Considere o botão já localizado em `botaoLembrete` e a função `mostrarLembrete` definida como no modelo.

```quiz
- pergunta: Qual linha registra a função para executar quando o botão receber o evento click?
  alternativas:
    - texto: 'botaoLembrete.addEventListener("click", mostrarLembrete());'
    - texto: 'botaoLembrete.addEventListener("click", mostrarLembrete);'
      correta: true
    - texto: 'console.log("click");'
  feedback: >
    O registro recebe a própria função, sem chamá-la nesse momento. Com parênteses, você executa a função imediatamente. Mostrar a palavra click no console não registra a ação.
- pergunta: Ao atualizar, o lembrete já aparece antes de clicar. Qual detalhe deve ser conferido?
  alternativas:
    - texto: Se sobrou uma chamada direta da função ou se ela foi chamada dentro do registro do evento
      correta: true
    - texto: Se o título está verde no CSS
    - texto: Se o botão foi clicado duas vezes na execução anterior
  feedback: >
    Uma chamada direta executa a ação ao carregar o arquivo, e chamar a função no argumento do registro também antecipa a ação. A cor do título não controla esse momento; atualizar reinicia os estados deste exemplo.
- pergunta: Depois de clicar e ver o lembrete, você atualiza a página. O que acontece antes de outro clique neste programa?
  alternativas:
    - texto: A mensagem personalizada permanece porque o arquivo HTML foi reescrito
    - texto: O botão e a lista são apagados
    - texto: A mensagem inicial do HTML reaparece e a função aguarda nova ativação
      correta: true
  feedback: >
    A mudança ocorreu no documento carregado, sem reescrever o arquivo. Ao atualizar, o navegador recarrega o HTML e registra a ação novamente; ela aguarda outro clique.
```

## Fechamento

- O **botão tem um id próprio** e é localizado pelo JavaScript.
- **`addEventListener("click", mostrarLembrete)`** registra a função para a ativação.
- O **nome da função vai sem parênteses no registro**; a execução acontece quando o evento ocorre.
- Teste **antes, depois da ativação e após atualizar**, incluindo o uso pelo teclado.

Na próxima aula, vamos acrescentar um campo e ler o texto que o usuário digitou para mostrar uma resposta na página.

:::roteiro
0–6 min: retomar definição sem chamada e restaurar mensagem inicial. 6–17 min: botão, id e busca; recuperação completa do HTML só para quem precisar. 17–29 min: addEventListener e diferença entre fornecer uma função e chamá-la imediatamente. 29–35 min: estados, repetição, atualização e teclado. 35–45 min: prática. 45–50 min: quiz e fechamento. Adaptação dos eventos do RCO 83/94 ao plano: um botão, uma função nomeada, um evento e alteração textual. Não introduzir funções anônimas, parâmetros do evento, formulários, preventDefault, alternância ou persistência. A tag script fica após os elementos. O teste de teclado usa o comportamento nativo do botão, sem criar atalhos próprios.
:::
