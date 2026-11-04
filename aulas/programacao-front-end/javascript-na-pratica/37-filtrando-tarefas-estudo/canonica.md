---
titulo: Filtrando as tarefas que aparecem
tema: JavaScript na prática
disciplina: programacao-front-end
serie: 2ª
prerequisitos: [Guardar registros de tarefa, Concluir e reabrir tarefas, Renderizar com forEach]
objetivos:
  - Selecionar tarefas com filter usando uma função que retorna um booleano
  - Alternar a apresentação entre todas, pendentes e concluídas
  - Conferir que filtrar não apaga dados e que os botões continuam ligados à tarefa correta
trilha: javascript-na-pratica
ordem: 37
slug: filtrando-tarefas-estudo
modo_origem: seed
fontes: [docs/plano-apostila-javascript.md]
revisao: true
status: aprovada
versao: 2
atualizado_em: 2026-11-04
---

Quando a lista cresce, você pode querer ver só o que falta fazer. Filtrar é como escolher quais cartões da sua fila colocar à vista, mantendo os demais guardados. Hoje sua página vai mostrar todas as tarefas, apenas pendentes ou apenas concluídas. O filtro muda a apresentação; não é uma ação de apagar tarefas.

## Objetivos

- Usar `filter` com uma função que responde se cada tarefa deve entrar na seleção.
- Mudar o filtro em um seletor da página e conferir a quantidade mostrada.
- Concluir e reabrir tarefas em uma lista filtrada sem alterar a tarefa errada.

## Pré-requisitos

Use a pasta `meus-estudos`, com o programa de registros e conclusão da aula 36. Tenha o VSCode, a página e o console abertos. Vamos reutilizar objetos com `texto` e `concluida`, funções, `if`/`else if`, `forEach` e cliques. `map` e `reduce`, apresentados no fim, são uma extensão opcional; não são necessários para concluir a prática principal.

## Desenvolvimento

### 1. Selecione sem apagar os dados

Substitua o conteúdo de **`script.js`** por este teste isolado:

```javascript
const tarefas = [
  { texto: "Revisar HTML", concluida: false },
  { texto: "Praticar CSS", concluida: true }
];

function estaPendente(tarefa) {
  return tarefa.concluida === false;
}

const pendentes = tarefas.filter(estaPendente);
console.log(pendentes.length);
console.log(pendentes[0].texto);
console.log(tarefas.length);
```

Salve e atualize. O console mostra **1**, **Revisar HTML** e **2**. Há uma tarefa pendente, mas o array original continua com duas tarefas. Esse teste isolado não trata os eventos da página.

:::conceito filter e return
**`filter`** cria um novo array com os elementos aceitos pela função informada. A função recebe uma tarefa por vez e **`return` devolve a resposta** para quem a chamou. Aqui, `true` inclui aquela tarefa; `false` deixa a tarefa fora da seleção. Os dados não são apagados do array original.
:::

Escrever a comparação sem `return` não entrega essa resposta ao método. Repare também no registro `tarefas.filter(estaPendente)`, sem chamar a função antecipadamente.

### 2. Prepare o controle do filtro

No **`index.html`**, mantenha o formulário, a mensagem e a classe `.concluida` da aula 36. Antes do `ul`, acrescente o rótulo, o seletor e o resumo de quantidade do modelo. Este é o HTML completo para recuperação **somente em arquivo vazio**:

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>Meus estudos</title>
  <style>
    body { background-color: aliceblue; }
    h1 { color: darkgreen; }
    .concluida { text-decoration: line-through; color: darkgreen; }
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
  <label for="filtro-tarefas">Mostrar tarefas</label>
  <select id="filtro-tarefas">
    <option value="todas">Todas</option>
    <option value="pendentes">Pendentes</option>
    <option value="concluidas">Concluídas</option>
  </select>
  <p id="resumo">Mostrando 0 de 0 tarefas.</p>
  <ul id="lista-tarefas"></ul>
  <script src="script.js"></script>
</body>
</html>
```

O `select` oferece as opções. Seu `value` informa qual delas está selecionada, assim como você já leu o valor do campo. O rótulo se associa pelo `for` e pelo `id`. O evento **`change`** será usado para reconstruir a apresentação quando a escolha mudar.

### 3. Renderize a seleção atual

Substitua o conteúdo de **`script.js`** pelo programa completo abaixo:

```javascript
const tarefas = [];

function estaPendente(tarefa) {
  return tarefa.concluida === false;
}

function estaConcluida(tarefa) {
  return tarefa.concluida === true;
}

function mostrarTarefa(tarefa) {
  const lista = document.getElementById("lista-tarefas");
  const item = document.createElement("li");
  const texto = document.createElement("span");
  const botao = document.createElement("button");
  texto.textContent = tarefa.texto + " ";
  botao.type = "button";

  if (tarefa.concluida) {
    texto.classList.add("concluida");
    botao.textContent = "Reabrir";
  } else {
    botao.textContent = "Concluir";
  }

  function alternarConclusao() {
    tarefa.concluida = tarefa.concluida === false;
    renderizarTarefas();
  }

  botao.addEventListener("click", alternarConclusao);
  item.appendChild(texto);
  item.appendChild(botao);
  lista.appendChild(item);
}

function renderizarTarefas() {
  const lista = document.getElementById("lista-tarefas");
  const filtro = document.getElementById("filtro-tarefas");
  const resumo = document.getElementById("resumo");
  let visiveis = tarefas;

  if (filtro.value === "pendentes") {
    visiveis = tarefas.filter(estaPendente);
  } else if (filtro.value === "concluidas") {
    visiveis = tarefas.filter(estaConcluida);
  }

  lista.textContent = "";
  visiveis.forEach(mostrarTarefa);
  resumo.textContent = "Mostrando " + visiveis.length + " de " + tarefas.length + " tarefas.";
}

function adicionarTarefa(evento) {
  evento.preventDefault();
  const campo = document.getElementById("campo-tarefa");
  const mensagem = document.getElementById("mensagem");
  const texto = campo.value.trim();

  if (texto === "") {
    mensagem.textContent = "Digite uma tarefa.";
  } else {
    tarefas.push({ texto: texto, concluida: false });
    renderizarTarefas();
    mensagem.textContent = "Tarefa adicionada. Total: " + tarefas.length;
    campo.value = "";
  }
}

const formulario = document.getElementById("formulario-tarefa");
formulario.addEventListener("submit", adicionarTarefa);
const seletorFiltro = document.getElementById("filtro-tarefas");
seletorFiltro.addEventListener("change", renderizarTarefas);
renderizarTarefas();
```

Salve os dois arquivos e atualize. Adicione três tarefas e conclua uma. Alterne entre **Todas**, **Pendentes** e **Concluídas**. O resumo deve indicar **3 de 3**, **2 de 3** e **1 de 3**, respectivamente.

Em `renderizarTarefas`, começamos mostrando todas. Se houver um filtro, escolhemos a seleção e percorremos `visiveis`. `filter` cria o array da seleção, mas os registros continuam sendo os das tarefas. O botão de cada item usa aquele registro; não depende da posição que a tarefa ocupa na lista filtrada.

Se concluir uma tarefa no filtro Pendentes, ela deixa de satisfazer o filtro e sai dessa apresentação. Mude para Todas ou Concluídas para encontrá-la. Se adicionar uma tarefa enquanto vê Concluídas, ela entra como pendente e não aparece nesse filtro; a confirmação e o total indicam que foi recebida.

:::atencao O filtro ficou vazio, mas há tarefas
**Sintoma:** a lista não mostra itens após você escolher Concluídas.

**Solução:** confira se há alguma tarefa concluída. Mostrar zero itens pode ser o resultado correto. Volte a Todas e leia o resumo. Se houver dados compatíveis e nada aparecer, confira os valores `pendentes` e `concluidas` do seletor e o `return` das funções de seleção.
:::

:::dica Filtrar não é remover
Deixe claro qual conjunto está sendo mostrado. O resumo distingue a quantidade visível da quantidade total. Teste também alterar o estado dentro de um filtro, porque a tarefa pode mudar de grupo imediatamente sem ter sido apagada.
:::

### 4. Aprofundamento guiado opcional: map e reduce

O projeto principal usa **`filter` para selecionar** e **`forEach` para executar uma ação por tarefa**. Os exemplos seguintes são opcionais, para depois da prática ou com orientação do professor. Execute-os isoladamente no `script.js` e **restaure o programa da etapa 3 ao terminar**.

**`map` transforma cada elemento em um valor de um novo array.** Aqui extraímos os textos dos registros:

```javascript
const tarefas = [
  { texto: "Revisar HTML", concluida: false },
  { texto: "Praticar CSS", concluida: true }
];

function obterTexto(tarefa) {
  return tarefa.texto;
}

const textos = tarefas.map(obterTexto);
console.log(textos[0]);
console.log(textos.length);
```

O resultado é **Revisar HTML** e **2**. O array novo contém textos, enquanto o original continua contendo registros.

**`reduce` combina valores em um resultado acumulado.** Este exemplo soma três períodos. A função recebe o total acumulado e o próximo número; devolve a nova soma. O `0` depois da função é o total inicial.

```javascript
const periodos = [10, 20, 15];

function somarPeriodo(total, minutos) {
  return total + minutos;
}

const total = periodos.reduce(somarPeriodo, 0);
console.log(total);
```

O resultado é **45**: 0 + 10, depois 10 + 20, depois 30 + 15. Não é necessário usar `map` ou `reduce` para concluir o filtro desta aula.

## Prática

### Mostre somente o grupo escolhido

Use o programa completo da etapa 3.

1. Adicione três tarefas, conclua a segunda e confira Todas, Pendentes e Concluídas e suas quantidades.
2. Em Pendentes, conclua a primeira tarefa que aparece. Volte a Todas e confira se a tarefa correta mudou de estado.
3. Em Concluídas, reabra uma tarefa. Confira que ela sai desse filtro e reaparece em Pendentes.
4. Adicione uma tarefa enquanto vê Concluídas. Confira o total e depois localize a nova tarefa em Pendentes. Envie texto vazio e confira que os dados não crescem.

### Confira antes de entregar

Os filtros devem mudar apenas a apresentação. O total não diminui ao trocar de filtro ou concluir/reabrir. Os botões devem continuar ligados aos registros corretos. Mostre um filtro vazio e depois volte a Todas para provar que os dados continuam presentes. Atualizar ainda reinicia o projeto desta versão.

## Avaliação

O aprofundamento opcional não faz parte destas questões.

```quiz
- pergunta: Qual é a função do return na função estaPendente usada pelo filter?
  alternativas:
    - texto: Apagar definitivamente a tarefa concluída
    - texto: Devolver o booleano que decide se a tarefa entra na seleção
      correta: true
    - texto: Criar automaticamente um li no HTML
  feedback: >
    filter usa a resposta da função para selecionar elementos. Não apaga os dados originais nem cria os elementos da página.
- pergunta: Existem três tarefas e apenas uma está concluída. Qual resumo deve aparecer no filtro Concluídas?
  alternativas:
    - texto: Mostrando 1 de 3 tarefas.
      correta: true
    - texto: Mostrando 1 de 1 tarefas.
    - texto: Mostrando 3 de 3 tarefas.
  feedback: >
    Uma tarefa satisfaz o filtro, mas o conjunto original continua com três. A quantidade selecionada é diferente do total.
- pergunta: Você concluiu uma tarefa enquanto via Pendentes e ela saiu da lista. O que deve conferir primeiro?
  alternativas:
    - texto: Se o arquivo HTML foi apagado
    - texto: Se é necessário recriar manualmente o array
    - texto: Se a tarefa está agora em Concluídas ou Todas, pois deixou de ser pendente
      correta: true
  feedback: >
    A tarefa mudou de grupo. O programa atualizou seu registro e reconstruiu a seleção, sem apagar os dados.
```

## Fechamento

- **`filter` seleciona elementos** usando a resposta devolvida por uma função.
- **`return` entrega essa resposta** para o método que chamou a função.
- O seletor muda a **apresentação**, preservando os registros do conjunto original.
- Teste **filtros vazios e mudanças de estado**, conferindo visíveis e total.

Na próxima aula, vamos revisar o projeto completo, testar os cenários e melhorar sua organização e suas mensagens.

:::roteiro
0–10 min: filter isolado e return booleano. 10–17 min: seletor e change. 17–32 min: programa integrado, resumo e estado mudando entre grupos; priorizar explicar alterações em relação à aula 36, com código disponível para copiar. 32–45 min: prática principal. 45–50 min: quiz e fechamento. Map/reduce são aprofundamento fora do núcleo desses 50 minutos, como aprovado no plano; não exigir na avaliação. RCO 87/92/93 reorganizado: seleção antes de transformação e acumulação. Não substituir o array principal pelo resultado do filtro. Os botões retêm o registro da tarefa, evitando usar índice da seleção como se fosse índice dos dados completos.
:::
