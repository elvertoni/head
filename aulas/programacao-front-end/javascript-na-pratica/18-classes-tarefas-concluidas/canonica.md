---
titulo: Marcando tarefas concluídas com classes CSS
tema: JavaScript na prática
disciplina: programacao-front-end
serie: 2ª
prerequisitos: [Renderizar com forEach, Registrar cliques, Usar booleanos]
objetivos:
  - Guardar texto e estado de conclusão no mesmo registro de tarefa
  - Aplicar uma classe CSS ao texto de uma tarefa concluída
  - Alterar o estado pelo botão e reconstruir a apresentação mantendo as outras tarefas
trilha: javascript-na-pratica
ordem: 18
slug: classes-tarefas-concluidas
modo_origem: seed
fontes: [docs/plano-apostila-javascript.md]
revisao: true
status: aprovada
versao: 2
atualizado_em: 2026-11-04
---

Concluir uma tarefa é diferente de apagá-la: você pode querer enxergar o que já fez. Hoje cada tarefa vai guardar uma resposta de sim ou não para “está concluída?”. Um botão muda essa resposta, e uma classe CSS mostra o progresso com texto riscado. É como marcar um cartão da sua fila sem perder sua descrição.

## Objetivos

- Reunir texto e conclusão em um registro de tarefa.
- Usar a classe `.concluida` para distinguir visualmente o texto concluído.
- Concluir e reabrir uma tarefa pelo botão sem perder o estado das demais.

## Pré-requisitos

Abra a pasta `meus-estudos` no VSCode e no navegador. Vamos retomar a renderização da aula 17, funções, cliques e booleanos. Você vai salvar mudanças no CSS do `index.html` e substituir o `script.js` pelo programa desta aula. Hoje a estrutura dos dados muda: em vez de guardar só textos no array, vamos guardar registros com texto e conclusão.

## Desenvolvimento

### 1. Guarde duas informações na mesma tarefa

Substitua o conteúdo de **`script.js`** pelo teste abaixo:

```javascript
const tarefa = { texto: "Revisar HTML", concluida: false };
console.log(tarefa.texto);
console.log(tarefa.concluida);
```

Salve e atualize. O console mostra **Revisar HTML** e **false**. Esse pequeno teste não trata o formulário ainda.

:::conceito Um objeto como registro
Um **objeto** reúne informações com nomes. Aqui `texto` e `concluida` são propriedades do registro da tarefa. Consultamos com ponto, como em `tarefa.texto`. O texto descreve a tarefa; o booleano informa se ela foi concluída. `false` significa pendente e `true`, concluída.
:::

O array poderá guardar esses registros, um por tarefa. Cada registro carrega seu próprio estado. Alterar `tarefa.concluida` muda essa propriedade do registro, sem precisar trocar o nome da variável nem recriar o array.

### 2. Prepare a aparência de conclusão

No **`index.html`**, dentro de `<style>`, acrescente esta regra depois das que já existem:

```css
.concluida {
  text-decoration: line-through;
  color: darkgreen;
}
```

O ponto antes de `concluida` indica um seletor de **classe CSS**. `text-decoration: line-through` risca o texto, e a cor também muda. Você poderá reconhecer a conclusão pelo risco, não apenas pela cor.

Este é o HTML completo para recuperar a base **somente em arquivo vazio**. Quem já tem a página mantém o formulário e a lista e acrescenta a regra acima.

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
  <ul id="lista-tarefas"></ul>
  <script src="script.js"></script>
</body>
</html>
```

### 3. Ligue estado, aparência e botão

Substitua o conteúdo de **`script.js`** pelo programa completo abaixo. Preserve os ids do HTML.

```javascript
const tarefas = [];

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
  lista.textContent = "";
  tarefas.forEach(mostrarTarefa);
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
renderizarTarefas();
```

Salve os dois arquivos e atualize. Adicione **Revisar HTML** e **Praticar CSS**. Cada item deve ter texto e um botão **Concluir**.

O `span` é um elemento para envolver o trecho de texto do item. `texto.classList.add("concluida")` aplica a classe a esse trecho quando o registro está concluído. No JavaScript, o nome da classe é escrito **sem ponto**; o ponto aparece no seletor CSS.

A função `alternarConclusao` é definida dentro de `mostrarTarefa`. Por isso, cada botão fica ligado ao registro da sua própria tarefa. Acompanhe o que acontece em um clique:

```diagrama-progressivo
titulo: O que acontece ao clicar em Concluir
camadas:
  - rotulo: Clique
    conteudo: "Você ativa o botão Concluir de Revisar HTML. O navegador executa alternarConclusao, a função registrada para esse botão."
  - rotulo: Novo estado
    conteudo: "tarefa.concluida === false pergunta se a tarefa estava pendente. Como estava, a resposta é true, e esse booleano passa a ser o valor de tarefa.concluida."
  - rotulo: Nova renderização
    conteudo: "renderizarTarefas limpa a lista e chama mostrarTarefa para cada registro, inclusive para os que não mudaram."
  - rotulo: Aparência decidida
    conteudo: "No registro concluído, o if aplica a classe concluida ao texto e escreve Reabrir no botão. As outras tarefas continuam com Concluir."
```

No clique seguinte, a mesma pergunta responde `false`, e a tarefa volta a ficar pendente.

### 4. Confira que o estado pertence aos dados

Conclua **Revisar HTML**. Só seu texto deve ficar riscado, e seu botão deve mudar para **Reabrir**. Adicione uma terceira tarefa. A primeira deve continuar concluída, pois o estado foi guardado no registro antes de renderizar novamente.

Use **Reabrir** na primeira tarefa. O estado volta a pendente, e a nova apresentação não aplica a classe ao texto. Não precisamos retirar a classe do elemento antigo: os elementos foram recriados conforme os dados.

:::atencao O risco some quando adiciono outra tarefa
**Sintoma:** a aparência muda no clique, mas se perde na próxima renderização.

**Solução:** confira se o clique altera `tarefa.concluida` antes de chamar `renderizarTarefas`. Mudar apenas a aparência do elemento antigo não guarda a conclusão nos dados. Use o programa completo com registros, sem misturar com o array de textos da aula 17.
:::

:::atencao A tarefa muda de estado, mas não fica riscada
**Sintoma:** o botão muda para Reabrir, mas o texto não apresenta o risco.

**Solução:** confira a regra `.concluida` dentro de `<style>` e a chamada `texto.classList.add("concluida")`. O ponto é do seletor CSS, não faz parte do nome informado em `classList.add`. Salve os dois arquivos e atualize.
:::

:::dica Mostre o estado de mais de uma forma
Um texto riscado e um botão com a ação “Reabrir” ajudam a entender a conclusão sem depender só de cor. Guarde o estado nos dados e use esses dados para decidir a aparência. Essa mesma separação vai permitir filtrar tarefas na próxima aula.
:::

## Prática

### Conclua, acrescente e reabra

Use o programa completo da etapa 3 e a classe CSS desta aula.

1. Adicione três tarefas e conclua somente a segunda.
2. Confira o risco apenas no segundo texto e o botão Reabrir correspondente. Ative o botão também pelo teclado.
3. Adicione uma quarta tarefa. Confira que a segunda continua concluída e as outras permanecem pendentes.
4. Reabra a segunda e explique à dupla qual propriedade mudou e como a classe foi decidida.

### Confira antes de entregar

Cada botão deve alterar somente sua tarefa. Adicionar outra tarefa não deve apagar conclusões nem duplicar itens. Envios vazios continuam recusados. Atualizar a página ainda reinicia as tarefas desta versão: não há armazenamento permanente. Mostre os testes ao professor.

## Avaliação

```quiz
- pergunta: Onde o programa guarda que uma tarefa está concluída?
  alternativas:
    - texto: Apenas na cor do texto
    - texto: Na propriedade concluida do registro da tarefa
      correta: true
    - texto: No texto digitado no campo
  feedback: >
    O estado booleano está no registro. A cor, o risco e o rótulo do botão são apresentações desse dado.
- pergunta: Qual combinação aplica corretamente a classe ensinada?
  alternativas:
    - texto: Seletor CSS .concluida e classList.add("concluida") no JavaScript
      correta: true
    - texto: Seletor CSS sem ponto e classList.add(".concluida")
    - texto: Escrever concluida apenas no console
  feedback: >
    O ponto faz parte da escrita do seletor CSS. classList.add recebe somente o nome da classe, sem ponto.
- pergunta: Por que a conclusão continua após adicionar outra tarefa?
  alternativas:
    - texto: Porque os elementos antigos nunca são substituídos
    - texto: Porque const impede toda alteração dos registros
    - texto: Porque o estado foi atualizado no registro e usado na nova renderização
      correta: true
  feedback: >
    A renderização recria os elementos conforme os dados. const não impede alterar propriedades do registro; guardar o estado permite reconstruir a aparência corretamente.
```

## Fechamento

- Cada tarefa agora é um **registro com texto e conclusão**.
- O botão altera o **booleano do registro**, não apenas a aparência.
- A **classe CSS** é aplicada conforme esse estado.
- Renderizar novamente **preserva a situação guardada nos dados**, durante esta execução.

Na próxima aula, vamos escolher quais tarefas aparecem: todas, somente pendentes ou somente concluídas.

:::roteiro
0–8 min: ponte de string para registro com duas propriedades. 8–15 min: classe CSS, risco e cor. 15–30 min: acompanhar mostrarTarefa, função de clique ligada à tarefa atual e renderização por estado; disponibilizar código para copiar e explicar por partes. 30–35 min: adicionar outra tarefa sem perder conclusão. 35–46 min: prática. 46–50 min: quiz e fechamento. RCO 92/93 e eventos integrados ao plano. O objeto é o complemento necessário para guardar texto e booleano juntos; não introduzir classes JavaScript, índices como identidade de botões ou sintaxe de função anônima. Cinco focos: registro, propriedade, classe CSS, aplicação de classe e ação por tarefa. Não avaliar mecanismos formais de closures.
:::
