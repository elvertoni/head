---
titulo: Enviando uma tarefa pelo formulário
tema: JavaScript na prática
disciplina: programacao-front-end
serie: 2ª
prerequisitos: [Ler value, Alterar textContent, Usar funções e if com else]
objetivos:
  - Organizar o campo e o botão em um formulário
  - Tratar submit sem executar o envio padrão do formulário
  - Recusar uma tarefa vazia ou composta somente por espaços
trilha: javascript-na-pratica
ordem: 31
slug: formulario-validando-tarefa
modo_origem: seed
fontes: [docs/plano-apostila-javascript.md]
revisao: true
status: aprovada
versao: 2
atualizado_em: 2026-11-04
---

Na aula anterior, o botão mostrava até uma tarefa vazia. Hoje vamos organizar a entrada em um formulário e conferir o texto antes de aceitá-lo. Pense em entregar uma ficha: primeiro você verifica se escreveu a informação necessária. No seu projeto, o programa vai orientar quem deixou o campo vazio, sem recarregar a página durante o envio.

## Objetivos

- Reunir rótulo, campo e botão dentro de um `form`.
- Registrar o evento `submit` e impedir seu comportamento padrão com `preventDefault`.
- Usar `trim` e uma condição para recusar texto vazio ou só com espaços.

## Pré-requisitos

Abra a pasta `meus-estudos`, com `index.html` e `script.js` conectados. Tenha o navegador e o console disponíveis. Vamos retomar `value` da aula 30, `textContent`, funções e o `if`/`else`. As duas tarefas fixas do HTML continuam nesta etapa; criar uma tarefa nova na lista será o passo da aula 32.

## Desenvolvimento

### 1. Reúna os elementos em um formulário

No **`index.html`**, substitua o trecho que tem rótulo, campo e botão por este formulário. O parágrafo de mensagem deve ficar depois dele. Não mantenha outro campo ou botão da versão anterior.

```html
<form id="formulario-tarefa">
  <label for="campo-tarefa">Qual é sua próxima tarefa?</label>
  <input type="text" id="campo-tarefa" name="tarefa">
  <button type="submit">Receber tarefa</button>
</form>
<p id="mensagem">Digite uma tarefa e envie o formulário.</p>
```

O **`form`** reúne a entrada de dados. O botão agora tem **`type="submit"`**, pois sua ação é solicitar o envio desse formulário. O `label` continua associado ao `input`. O `name="tarefa"` dá nome a esse dado em um envio; neste exercício, vamos ler o campo por seu `id` usando JavaScript.

Se precisar recuperar a base, use este HTML completo **somente em um arquivo vazio**:

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
    <button type="submit">Receber tarefa</button>
  </form>
  <p id="mensagem">Digite uma tarefa e envie o formulário.</p>
  <ul>
    <li>Revisar HTML</li>
    <li>Praticar CSS</li>
  </ul>
  <script src="script.js"></script>
</body>
</html>
```

Salve o HTML. Vamos substituir o JavaScript antigo, que ainda procura o botão da aula 30 pelo evento de clique.

### 2. Responda ao envio do formulário

No **`script.js`**, substitua o conteúdo anterior por este programa completo:

```javascript
function receberTarefa(evento) {
  evento.preventDefault();

  const campo = document.getElementById("campo-tarefa");
  const mensagem = document.getElementById("mensagem");
  mensagem.textContent = "Tarefa recebida: " + campo.value;
}

const formulario = document.getElementById("formulario-tarefa");
formulario.addEventListener("submit", receberTarefa);
```

Salve os dois arquivos e atualize a página. Digite **Revisar HTML** e use **Receber tarefa**. A mensagem deve ser **Tarefa recebida: Revisar HTML**. Digite outra tarefa e pressione **Enter dentro do campo**: neste formulário, isso também solicita o envio e deve atualizar a resposta.

:::conceito submit e evento
O evento **`submit`** acontece no formulário quando um envio é solicitado. O navegador entrega à função uma informação sobre esse evento; escolhemos chamar essa informação de `evento`, dentro dos parênteses da definição. **`evento.preventDefault()`** impede o envio padrão, permitindo tratar a ação nesta página com JavaScript.
:::

Agora a função recebe uma informação, diferente das funções sem parâmetros das aulas anteriores. Você não precisa criar nem passar `evento` manualmente no registro. Mantenha `formulario.addEventListener("submit", receberTarefa);`, com o nome da função sem parênteses. O navegador a chama quando o evento ocorre.

### 3. Confira se há uma tarefa de verdade

Substitua o conteúdo de **`script.js`** pelo programa completo abaixo. Ele mantém o tratamento de envio e acrescenta uma condição.

```javascript
function receberTarefa(evento) {
  evento.preventDefault();

  const campo = document.getElementById("campo-tarefa");
  const mensagem = document.getElementById("mensagem");
  const tarefa = campo.value.trim();

  if (tarefa === "") {
    mensagem.textContent = "Digite uma tarefa.";
  } else {
    mensagem.textContent = "Tarefa recebida: " + tarefa;
  }
}

const formulario = document.getElementById("formulario-tarefa");
formulario.addEventListener("submit", receberTarefa);
```

Salve e atualize. Envie com o campo vazio: deve aparecer **Digite uma tarefa.**. Digite somente espaços e envie: deve aparecer a mesma orientação. Agora digite **Revisar HTML** e envie: deve aparecer **Tarefa recebida: Revisar HTML**.

O **`trim()`** produz uma versão do texto sem espaços no começo e no fim. Se o campo só tinha espaços, o resultado será o texto vazio `""`. A condição `tarefa === ""` verifica esse caso. Os espaços entre palavras, como em **Revisar HTML**, permanecem.

O texto tratado fica na variável `tarefa`. `trim()` não muda sozinho o valor visível no campo; estamos usando seu resultado na mensagem e na conferência.

### 4. Teste os dois caminhos do envio

Faça quatro testes: campo vazio, somente espaços, uma tarefa comum e uma tarefa com espaços antes e depois. No último caso, digite alguns espaços, escreva **Praticar CSS**, acrescente outros espaços e envie. A resposta deve usar **Praticar CSS** sem os espaços das pontas.

Você ainda não adiciona um novo item à lista. Neste passo, o formulário recebe e confere a tarefa, e o parágrafo confirma o resultado. O programa não envia os dados a um servidor nem os guarda permanentemente.

:::atencao A página recarrega ao enviar
**Sintoma:** depois de ativar o botão ou pressionar Enter, a página navega ou recarrega, e a resposta não permanece como esperado.

**Solução:** confira se o evento é `"submit"` no formulário e se a primeira instrução da função é `evento.preventDefault();`. O nome `evento` deve ser o mesmo no parâmetro e nessa instrução. Mantenha a tag de `script.js` depois dos elementos, salve e atualize. Não mantenha também o código antigo de clique.
:::

:::atencao O programa aceita somente espaços
**Sintoma:** um campo sem palavras recebe uma confirmação de tarefa.

**Solução:** confira se criou `const tarefa = campo.value.trim();` e comparou `tarefa === ""`. Verificar apenas o texto original não remove os espaços das pontas. Use o resultado tratado tanto na comparação quanto na resposta, salve e teste de novo.
:::

:::dica Valide no caminho do envio
Registrar o `submit` trata a ação do formulário, incluindo o botão e o Enter neste exemplo. Verifique o dado antes de aceitar a tarefa e dê uma orientação clara para corrigir o problema. Essa verificação melhora a experiência na página; aplicações com servidor também precisam conferir os dados no servidor.
:::

## Prática

### Receba uma tarefa preenchida

Use o **programa completo da etapa 3**. Teste um caso de cada vez, observando a mensagem.

1. Envie o campo vazio e depois com três espaços. Confira **Digite uma tarefa.** nos dois casos.
2. Envie uma tarefa sua pelo botão e outra pressionando Enter no campo. Confira se as duas são recebidas sem navegação da página.
3. Digite espaços antes e depois de uma tarefa. Confira que o texto da resposta foi tratado e que os espaços entre palavras continuam.
4. Personalize a mensagem de sucesso, mantendo a orientação para campo vazio. Explique à dupla a função de `preventDefault`, `trim` e `if`.

### Confira antes de entregar

O formulário deve recusar texto vazio e só com espaços e mostrar uma confirmação para texto preenchido. A lista fixa permanece igual. Mostre os casos ao professor e guarde a pasta: na próxima aula, uma tarefa válida vai virar um novo item visível.

## Avaliação

Considere o programa completo com `submit`, `preventDefault` e `trim`.

```quiz
- pergunta: Qual evento deve ser registrado no formulário para tratar o envio deste exemplo pelo botão e pelo Enter no campo?
  alternativas:
    - texto: click apenas no parágrafo
    - texto: submit no formulário
      correta: true
    - texto: color no campo
  feedback: >
    submit corresponde ao envio do formulário. O clique no parágrafo não representa esse envio, e color é uma propriedade CSS, não o evento usado aqui.
- pergunta: Qual é o papel de evento.preventDefault() neste programa?
  alternativas:
    - texto: Impedir o envio padrão para tratar a ação com JavaScript na página
      correta: true
    - texto: Apagar automaticamente os espaços do campo
    - texto: Adicionar uma tarefa à lista
  feedback: >
    preventDefault impede o comportamento padrão do envio. O tratamento dos espaços vem de trim; a criação de itens ainda não faz parte deste programa.
- pergunta: A pessoa digitou somente três espaços. Por que tarefa === "" será verdadeira após campo.value.trim()?
  alternativas:
    - texto: Porque qualquer texto vira vazio quando usamos trim
    - texto: Porque o navegador já apagou o campo antes do evento
    - texto: Porque trim retira os espaços das pontas e não sobra nenhuma palavra
      correta: true
  feedback: >
    Quando há apenas espaços, retirá-los produz uma string vazia. trim preserva as palavras e os espaços entre elas; não significa que o campo foi apagado pelo navegador.
```

## Fechamento

- **`form` reúne a entrada** e o botão `submit` solicita seu envio.
- **`submit` registra a ação de envio**; o navegador entrega o evento à função.
- **`preventDefault()` impede o envio padrão** para tratar a ação na página.
- **`trim()` e `if` ajudam a recusar uma tarefa vazia**, inclusive só com espaços.

Na próxima aula, vamos criar um item de lista para cada tarefa válida recebida.

:::roteiro
0–8 min: trocar entrada por formulário e retomar rótulo, campo e script após os elementos. 8–21 min: submit, parâmetro evento e preventDefault; testar botão e Enter. 21–33 min: trim, comparação com string vazia e if/else. 33–45 min: prática com quatro casos, reservando tempo de apoio por reunir conteúdos anteriores. 45–50 min: quiz e fechamento. Adaptação dos formulários do RCO 94/95 ao plano: validação textual simples no envio. Não usar required neste exercício para não ocultar o caminho de validação JavaScript pelo bloqueio nativo. Não introduzir servidor, regex, return antecipado ou criação de elementos. A observação sobre servidor delimita o papel desta validação sem transformá-la em checklist de segurança.
:::
