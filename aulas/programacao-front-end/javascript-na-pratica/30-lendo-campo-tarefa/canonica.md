---
titulo: Lendo a tarefa que você digitou
tema: JavaScript na prática
disciplina: programacao-front-end
serie: 2ª
prerequisitos: [Localizar elementos pelo id, Alterar textContent, Registrar um clique]
objetivos:
  - Associar um rótulo a um campo de texto no HTML
  - Consultar o texto atual do campo pela propriedade value no clique
  - Mostrar uma resposta na página usando o texto digitado
trilha: javascript-na-pratica
ordem: 30
slug: lendo-campo-tarefa
modo_origem: seed
fontes: [docs/plano-apostila-javascript.md]
revisao: true
status: aprovada
versao: 3
atualizado_em: 2026-11-04
---

Na aula 29, o botão mostrava uma tarefa escrita dentro do JavaScript. Hoje você vai escolher a tarefa digitando em um campo. É como preencher um bilhete: o campo recebe o que você escreveu e o botão pede para ler o bilhete. A resposta vai aparecer na própria página, sem precisar editar o código a cada nova tarefa.

## Objetivos

- Criar um campo com um rótulo que diga o que digitar.
- Ler o texto do campo com `.value` quando o botão for ativado.
- Mostrar uma resposta que use o texto digitado naquele momento.

## Pré-requisitos

Abra `meus-estudos` no VSCode e o `index.html` no navegador. Mantenha o console disponível para conferir erros. Vamos editar e salvar os dois arquivos, `index.html` e `script.js`. Retome a aula 29 se precisar lembrar a ligação entre função e clique. **HTML organiza os elementos; JavaScript responde à ação do usuário.**

## Desenvolvimento

### 1. Prepare o campo e seu rótulo

No **`index.html`**, apague o botão **Mostrar lembrete** da aula 29, que fica depois do parágrafo `id="mensagem"`. Depois, insira as três linhas abaixo **antes desse parágrafo**. Preserve o título, a lista e o CSS. No final, a página deve ter um único botão: **Mostrar tarefa**.

```html
<label for="campo-tarefa">Qual é sua próxima tarefa?</label>
<input type="text" id="campo-tarefa">
<button type="button" id="botao-tarefa">Mostrar tarefa</button>
```

O **`label`** é o rótulo do campo. Seu `for="campo-tarefa"` corresponde ao `id="campo-tarefa"` do `input`. Essa ligação permite clicar no rótulo para levar o foco ao campo e ajuda quem usa tecnologias de leitura de tela. O `input type="text"` é a caixa em que você digita.

Se precisar recuperar a base, use o HTML completo abaixo **somente em um arquivo vazio**. Quem já tem a página faz a troca indicada acima e mantém o carregamento de `script.js` depois dos elementos, antes de `</body>`.

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
  <label for="campo-tarefa">Qual é sua próxima tarefa?</label>
  <input type="text" id="campo-tarefa">
  <button type="button" id="botao-tarefa">Mostrar tarefa</button>
  <p id="mensagem">Digite uma tarefa e use o botão.</p>
  <ul>
    <li>Revisar HTML</li>
    <li>Praticar CSS</li>
  </ul>
  <script src="script.js"></script>
</body>
</html>
```

Salve o HTML. No seu parágrafo de mensagem, use a frase inicial **Digite uma tarefa e use o botão.**. Vamos substituir também o JavaScript antigo, que ainda procura o botão da aula 29.

### 2. Leia o campo no momento do clique

No **`script.js`**, substitua o conteúdo anterior pelo programa completo abaixo:

```javascript
function mostrarTarefa() {
  const campo = document.getElementById("campo-tarefa");
  console.log(campo.value);
}

const botao = document.getElementById("botao-tarefa");
botao.addEventListener("click", mostrarTarefa);
```

Salve os dois arquivos com **Ctrl + S** e atualize o navegador com **Ctrl + R**. Digite **Estudar matemática** no campo e clique em **Mostrar tarefa**. O console deve mostrar esse texto. Troque o que está digitado por **Ler o capítulo de história** e clique de novo. A nova mensagem deve usar o novo texto.

:::conceito value lê o conteúdo do campo
Em um campo de texto, **`value`** contém o texto digitado. `campo.value` consulta esse valor. A leitura está dentro de `mostrarTarefa`, por isso acontece a cada ativação do botão, usando o que está no campo naquele momento.
:::

Em `console.log(campo.value)`, você mostra o valor no console. Na próxima etapa vamos usar esse mesmo valor para atualizar um parágrafo da página.

### 3. Mostre a resposta na página

Substitua o conteúdo de **`script.js`** por este programa completo:

```javascript
function mostrarTarefa() {
  const campo = document.getElementById("campo-tarefa");
  const mensagem = document.getElementById("mensagem");
  const tarefa = campo.value;

  mensagem.textContent = "Você digitou: " + tarefa;
}

const botao = document.getElementById("botao-tarefa");
botao.addEventListener("click", mostrarTarefa);
```

Salve e atualize. Digite **Revisar HTML** e ative o botão. A página deve mostrar **Você digitou: Revisar HTML**. O `+` junta o começo da mensagem com o texto digitado, retomando a concatenação da aula 23.

Aqui, **`value` lê o campo** e **`textContent` escreve no parágrafo**. Digitar algo não atualiza sozinho a resposta: a função é executada quando você ativa o botão.

:::atencao O campo tem texto, mas a resposta veio vazia
**Sintoma:** você digitou uma tarefa, mas o programa não mostra esse texto.

**Solução:** confira se a leitura é `campo.value`, com `value` em minúsculas, e se a busca usa `"campo-tarefa"`. O texto digitado em um input é lido por `value`, não por `textContent`. Salve, atualize e digite novamente antes de clicar.
:::

### 4. Confira o valor atual e os limites deste passo

Digite **Revisar HTML**, ative o botão, troque o campo para **Praticar CSS** e ative novamente. A segunda resposta deve ser **Você digitou: Praticar CSS**. O parágrafo é atualizado, e a lista de dois itens do HTML continua como estava.

Se você esvaziar o campo e ativar o botão, verá apenas **Você digitou:**, seguido do espaço que está na mensagem. Ainda não programamos uma verificação para impedir esse caso. Na aula 31, vamos acrescentar essa regra.

:::atencao O programa usa sempre o valor antigo
**Sintoma:** você altera o campo, mas a resposta usa um texto capturado antes.

**Solução:** mantenha `const tarefa = campo.value;` dentro da função executada no clique. Se essa leitura for feita uma única vez ao carregar a página, ela não consulta novamente o que você digitou depois. Compare com o programa completo, salve e teste com duas tarefas diferentes.
:::

:::dica Rótulo, entrada e resposta
Ao criar uma interface, deixe claro o que a pessoa deve preencher, qual ação ela deve executar e onde o resultado aparece. Use um rótulo visível ligado ao campo e uma mensagem que confirme o texto recebido. A propriedade `value` deste campo retorna texto, inclusive quando a pessoa digita algarismos.
:::

## Prática

### Uma resposta para sua tarefa

Use o **programa completo da etapa 3** no `script.js` e o campo com rótulo no HTML. Faça uma mudança por vez.

1. Digite uma tarefa sua e confira a resposta após ativar o botão.
2. Troque a tarefa sem atualizar a página e ative novamente. Confira se a resposta acompanha o valor atual.
3. Personalize o começo da mensagem no JavaScript, por exemplo para `"Sua próxima tarefa é: "`, mantendo `+ tarefa`.
4. Clique no rótulo e confira se o foco vai ao campo. Use Tab para chegar ao botão e Enter ou Espaço para ativá-lo.

### Confira antes de entregar

A página deve ter um rótulo visível, um campo e um botão. A resposta deve incluir a tarefa digitada no momento da ativação. Mostre ao professor dois textos diferentes e indique onde `value` é lido e onde `textContent` é alterado. Guarde a pasta para acrescentar o formulário na próxima aula.

## Avaliação

Considere o campo localizado na variável `campo` e o parágrafo na variável `mensagem`.

```quiz
- pergunta: Qual propriedade consulta o texto que a pessoa digitou no input?
  alternativas:
    - texto: campo.textContent
    - texto: campo.value
      correta: true
    - texto: mensagem.id
  feedback: >
    value lê o conteúdo atual do campo. textContent é usado aqui para o texto de elementos como o parágrafo; o id identifica um elemento, não contém o texto digitado.
- pergunta: Para ler uma nova tarefa a cada clique, onde deve ficar a consulta campo.value neste programa?
  alternativas:
    - texto: Dentro da função registrada para o clique
      correta: true
    - texto: Apenas antes de registrar o evento, ao carregar a página
    - texto: Dentro da regra color do CSS
  feedback: >
    A função executada a cada clique faz uma nova consulta. Uma leitura única ao carregar não captura alterações posteriores, e CSS não executa essa leitura de dados.
- pergunta: Qual ligação associa o rótulo ao campo no HTML desta aula?
  alternativas:
    - texto: Usar o mesmo texto no título e no botão
    - texto: Dar o mesmo id ao rótulo, ao campo e ao botão
    - texto: Usar for="campo-tarefa" no label e id="campo-tarefa" no input
      correta: true
  feedback: >
    O for do label corresponde ao id do input. Os ids identificam elementos únicos, não devem ser repetidos, e textos iguais em outros elementos não fazem essa associação.
```

## Fechamento

- O **`label` se liga ao input** pela correspondência entre `for` e `id`.
- **`value` consulta o texto atual** do campo.
- Leia o valor **dentro da função de clique** para acompanhar o que foi digitado depois.
- Use **`textContent` para mostrar a resposta** no parágrafo da página.

Na próxima aula, vamos reunir a entrada em um formulário, tratar seu envio e impedir uma tarefa vazia.

:::roteiro
0–8 min: retomar HTML/CSS e eventos; inserir campo e rótulo, removendo o botão antigo. 8–18 min: value dentro da função e conferência no console com dois textos. 18–29 min: resposta no parágrafo por concatenação. 29–35 min: valor atual e campo vazio como limite ainda não tratado. 35–45 min: prática. 45–50 min: quiz e fechamento. Adaptação dos campos e interações do RCO 94 ao plano: entrada textual antes de formulário e validação. Evitar introduzir submit, trim, Number, criação de elementos ou arrays aqui. A atualização pode restaurar estado do campo conforme o navegador; pedir que o aluno confira e digite o texto do teste, sem presumir que atualizar sempre limpa inputs.
:::
