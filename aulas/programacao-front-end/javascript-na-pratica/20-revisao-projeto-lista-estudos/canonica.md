---
titulo: Revisando e testando sua lista de estudos
tema: JavaScript na prática
disciplina: programacao-front-end
serie: 2ª
prerequisitos: [Adicionar e validar tarefas, Renderizar registros, Concluir e filtrar tarefas]
objetivos:
  - Explicar o caminho da entrada até os dados e a apresentação
  - Executar cenários de teste do projeto completo e localizar a responsabilidade de uma falha
  - Melhorar mensagens e organização sem alterar o comportamento esperado
trilha: javascript-na-pratica
ordem: 20
slug: revisao-projeto-lista-estudos
modo_origem: seed
fontes: [docs/plano-apostila-javascript.md]
revisao: true
status: aprovada
versao: 1
atualizado_em: 2026-11-04
---

Você começou com título, mensagem e duas tarefas fixas. Agora consegue receber uma tarefa, conferir seu texto, guardá-la, marcar sua conclusão e escolher o que aparece. Hoje vamos fechar esse percurso como quem confere uma bicicleta antes de sair: não basta olhar se está bonita; é preciso testar o que ela faz e explicar o que precisa de ajuste.

## Objetivos

- Explicar como um envio válido vira um registro e depois um item da página.
- Testar entrada, conclusão, filtros e reinício do projeto.
- Melhorar mensagens e organização, repetindo os testes depois de uma mudança.

## Pré-requisitos

Abra `meus-estudos` no VSCode e a página no navegador, com o console disponível. Use o projeto da aula 19. Nesta aula, não vamos acrescentar uma nova funcionalidade: vamos revisar o que já existe. A referência completa abaixo permite recuperar o projeto se algum arquivo ficou incompleto.

## Desenvolvimento

### 1. Relembre o percurso de uma tarefa

O **HTML** organiza rótulo, campo, botão, seletor, mensagem e lista. O **CSS** mostra o estilo de conclusão. O **JavaScript** responde aos eventos e mantém os dados durante a execução.

Quando o formulário recebe um envio, `adicionarTarefa` impede o comportamento padrão, lê e trata o texto. Um texto vazio recebe orientação. Um texto válido vira um registro com `texto` e `concluida: false`, que entra no array.

Depois, `renderizarTarefas` escolhe os registros visíveis conforme o filtro, limpa a apresentação antiga e chama `mostrarTarefa` para cada registro. O botão criado para aquela tarefa muda seu estado e pede nova renderização.

:::conceito Uma responsabilidade por parte
`adicionarTarefa` recebe e confere a entrada. `estaPendente` e `estaConcluida` respondem às perguntas do filtro. `renderizarTarefas` organiza a apresentação do conjunto. `mostrarTarefa` monta um item e sua ação. Os nomes ajudam a localizar onde investigar uma falha.
:::

### 2. Confira os dois arquivos de referência

Se seu projeto já funciona, **compare antes de substituir**. Para recuperar a base, este é o conteúdo completo de **`index.html`**. Preserve os ids se personalizar os textos ou o estilo.

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

Este é o conteúdo completo de **`script.js`**. Ele retoma o programa da aula 19, sem os exercícios opcionais de `map` e `reduce`. Mantenha os dois arquivos na mesma pasta.

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

Salve os dois arquivos e abra `index.html` no navegador. Comece cada rodada de testes após atualizar, lembrando que o array e a lista desta versão começam vazios. Confira o filtro selecionado e escolha **Todas**; alguns navegadores podem restaurar a escolha anterior do controle.

### 3. Execute os cenários e observe o resultado

Use os casos abaixo, na ordem, com as tarefas **Revisar HTML**, **Praticar CSS** e **Estudar JavaScript**. Confira o estado atual antes de decidir que há um erro.

| Caso | O que fazer | O que deve acontecer |
|---|---|---|
| Começo | Atualizar e escolher Todas | Lista vazia e resumo de 0 de 0. |
| Entrada inválida | Enviar vazio e somente espaços | Orientação de preenchimento, sem criar registros ou itens. |
| Entrada válida | Enviar as três tarefas, uma por vez | Três itens na ordem, campo limpo a cada sucesso e total 3. |
| Conclusão | Concluir somente Praticar CSS | Só esse texto fica riscado e seu botão muda para Reabrir. |
| Seleção | Escolher Pendentes e depois Concluídas | Respectivamente 2 de 3 e 1 de 3 tarefas. |
| Mudança no filtro | Em Concluídas, reabrir Praticar CSS | Ela sai desse filtro, mas aparece em Pendentes e Todas. |
| Nova tarefa oculta | Em Concluídas, adicionar Ler história | A confirmação indica total 4; a nova tarefa está em Pendentes. |
| Repetição e reinício | Alternar filtros várias vezes e depois atualizar | Não há cópias extras. Ao atualizar, os dados reiniciam vazios. |

Ative também os controles pelo teclado. O campo tem rótulo, os botões são nativos e o seletor permite trocar a opção. O texto riscado e a mudança no rótulo do botão indicam conclusão sem depender só de cor.

:::atencao A tarefa sumiu da apresentação
**Sintoma:** após concluir ou reabrir, você não encontra a tarefa na lista atual.

**Solução:** confira o filtro e o resumo. A tarefa pode ter mudado de grupo. Volte a Todas antes de concluir que um dado foi apagado. Se o total caiu sem atualizar a página, investigue se o array principal foi substituído por uma seleção do filtro.
:::

### 4. Faça uma melhoria pequena e teste novamente

Escolha **uma** alteração: tornar o rótulo do campo mais claro, personalizar a mensagem de sucesso ou ajustar a cor da classe `.concluida`, mantendo o risco no texto. Salve e repita os cenários que dependem dessa parte. Não troque ids sem ajustar as buscas correspondentes.

Se algo falhar, procure a responsabilidade antes de recomeçar todo o projeto. Campo vazio aceito? Confira `trim` e o `if` do envio. Itens duplicados? Confira a limpeza na renderização. Estado perdido? Confira se o botão muda a propriedade do registro. Filtro sem resultados? Confira seleção, `return` e compatibilidade dos dados.

:::atencao Alterei um nome e a página deixou de funcionar
**Sintoma:** depois de renomear uma função ou um id, aparece um erro no console ou uma ação para de acontecer.

**Solução:** compare os lugares relacionados. O nome da função precisa corresponder aos registros de eventos e às chamadas. O id no HTML precisa corresponder à busca no JavaScript. Faça uma mudança por vez, salve e teste; não altere vários nomes ao mesmo tempo.
:::

:::dica Faça outra pessoa testar
Quem desenvolve já sabe o caminho que pretendia programar. Outra pessoa pode encontrar uma entrada, um filtro ou uma ordem de ações que você não conferiu. Peça à dupla para usar os cenários sem você conduzir cada clique e anote o que ela observou.
:::

## Prática

### Revisão em dupla

Use seu projeto ou recupere os dois arquivos da etapa 2.

1. Execute os cenários da etapa 3. Em papel, marque o resultado de cada um e anote a mensagem observada quando houver dúvida.
2. Troque de lugar com uma dupla: ela testa seu projeto e você testa o dela. Compare os resultados.
3. Escolha uma melhoria pequena da etapa 4, faça e repita os testes relacionados.
4. Apresente ao professor uma tarefa percorrendo entrada, array, item visual, conclusão e filtro. Aponte as funções responsáveis.

### Confira antes de entregar

Entregue a pasta com **`index.html` e `script.js`** e seu registro dos testes. O projeto deve recusar vazios, preservar tarefas durante os envios, concluir/reabrir o registro correto, filtrar sem apagar e não duplicar itens. Explique seu limite atual: atualizar reinicia os dados; não há conta, servidor ou armazenamento permanente nesta versão.

## Avaliação

```quiz
- pergunta: Qual explicação descreve o caminho de uma tarefa aceita?
  alternativas:
    - texto: O CSS lê o campo e grava os dados permanentemente
    - texto: O envio trata o texto, acrescenta um registro ao array e pede a renderização
      correta: true
    - texto: O filtro cria outro formulário e apaga os dados antigos
  feedback: >
    O JavaScript trata o envio e atualiza dados e apresentação. CSS define aparência, e filtrar não é criar formulário nem apagar o conjunto original.
- pergunta: No filtro Concluídas, você adiciona uma tarefa nova, pendente. O total aumenta, mas ela não aparece ali. Qual teste deve fazer?
  alternativas:
    - texto: Escolher Pendentes ou Todas e procurar a nova tarefa
      correta: true
    - texto: Adicionar a mesma tarefa repetidamente até aparecer
    - texto: Apagar a função de validação
  feedback: >
    A tarefa nova é pendente e não satisfaz o filtro Concluídas. Conferir outro grupo verifica os dados sem criar cópias desnecessárias ou retirar a validação.
- pergunta: Qual atitude ajuda a localizar uma falha depois de uma melhoria?
  alternativas:
    - texto: Alterar todos os nomes e arquivos de uma vez
    - texto: Conferir somente se a página ficou bonita
    - texto: Mudar uma parte, testar seu comportamento e conferir a função ou ligação correspondente
      correta: true
  feedback: >
    Mudanças pequenas com testes permitem relacionar a alteração ao resultado. Aparência sozinha não verifica entrada, estado, filtros e continuidade.
```

## Fechamento

- Você construiu uma interface com **entrada, validação, dados e apresentação**.
- Funções, eventos, condições e percursos de arrays trabalham juntos no projeto.
- Testar **entrada inválida, limites e mudanças de estado** ajuda a verificar o comportamento.
- Nomes claros e responsabilidades separadas facilitam corrigir e melhorar o código.

Você concluiu esta sequência. Use a lista para apresentar o que aprendeu: escolha uma ação da página e explique seu caminho pelo HTML, pelo JavaScript e pelo CSS.

:::roteiro
0–8 min: reconstruir verbalmente o percurso de uma tarefa. 8–17 min: conferir referência e responsabilidades, sem redigitar todo o projeto. 17–30 min: cenários guiados com diagnóstico de filtro versus dado perdido. 30–43 min: revisão em dupla e melhoria pequena. 43–50 min: apresentação, quiz e fechamento. RCO 96/97 adaptado à consolidação prática do plano. Não acrescentar funcionalidades novas, bibliotecas, persistência ou publicação. A referência é o programa integrado da aula 19; map/reduce continuam como extensão da aula anterior. Aprovação de conteúdo e publicação no acervo continuam separadas desta entrega local.
:::
