---
titulo: Percorrendo as tarefas com for
tema: JavaScript na prática
disciplina: programacao-front-end
serie: 2ª
prerequisitos: [Consultar arrays por índice, Usar length, Comparar números]
objetivos:
  - Percorrer um array com for começando no índice zero
  - Explicar início, condição e avanço do laço
  - Conferir a execução com arrays vazios e com quantidades diferentes de tarefas
trilha: javascript-na-pratica
ordem: 16
slug: for-percorrendo-tarefas
modo_origem: seed
fontes: [docs/plano-apostila-javascript.md]
revisao: true
status: aprovada
versao: 2
atualizado_em: 2026-11-04
---

Sua lista pode ter duas, três ou dez tarefas. Você não quer escrever um console.log novo para cada posição. Hoje vamos repetir uma instrução para percorrer os valores que existem no array. Pense em conferir uma fila de cartões: comece pelo primeiro, leia, avance para o próximo e pare quando não houver outro.

## Objetivos

- Usar `for` para consultar cada tarefa pela sua posição.
- Identificar onde a repetição começa, quando continua e como avança.
- Testar um array vazio e arrays com diferentes quantidades de tarefas.

## Pré-requisitos

Abra a pasta `meus-estudos`, o VSCode e a página com o **Console**. O HTML da aula 15 continua com formulário, campo, mensagem, lista vazia identificada e carregamento de `script.js` após os elementos. Hoje o HTML e o CSS não precisam mudar. Faça um programa de cada vez no `script.js`, substituindo o anterior.

## Desenvolvimento

### 1. Retome as posições do array

Substitua o conteúdo do **`script.js`** por este exemplo:

```javascript
const tarefas = ["Revisar HTML", "Praticar CSS", "Estudar JavaScript"];
console.log(tarefas[0]);
console.log(tarefas[1]);
console.log(tarefas[2]);
```

Salve com **Ctrl + S** e atualize com **Ctrl + R**. Aparecem as três tarefas na ordem. Os índices começam em zero, e `tarefas.length` vale **3**. O último índice ocupado é **2**. O formulário aparece no HTML, mas este teste isolado não trata seu envio.

### 2. Faça a repetição com for

Substitua o conteúdo de **`script.js`** pelo programa abaixo:

```javascript
const tarefas = ["Revisar HTML", "Praticar CSS", "Estudar JavaScript"];

for (let indice = 0; indice < tarefas.length; indice = indice + 1) {
  console.log(tarefas[indice]);
}
```

Salve e atualize. As mesmas três tarefas aparecem. Agora o programa usa `indice` para consultar uma posição por vez.

:::conceito As três partes do for
**`let indice = 0`** define o começo. **`indice < tarefas.length`** é a condição verificada antes de cada execução do bloco. **`indice = indice + 1`** avança uma posição depois de executar o bloco. Quando a condição fica falsa, o laço termina.
:::

Acompanhe o laço uma passagem por vez. Antes de abrir a próxima camada, diga qual tarefa será mostrada e qual valor o índice terá depois.

```diagrama-progressivo
titulo: As passagens do for por um array de três tarefas
camadas:
  - rotulo: Começo
    conteudo: "let indice = 0 cria o contador. Antes da primeira passagem, o programa confere 0 < 3, que é true."
  - rotulo: Primeira passagem
    conteudo: "Com indice valendo 0, o bloco mostra tarefas[0], Revisar HTML. Depois, indice = indice + 1 faz o índice valer 1, e 1 < 3 continua true."
  - rotulo: Segunda passagem
    conteudo: "Com indice valendo 1, o bloco mostra tarefas[1], Praticar CSS. O índice passa a 2, e 2 < 3 continua true."
  - rotulo: Terceira passagem
    conteudo: "Com indice valendo 2, o bloco mostra tarefas[2], Estudar JavaScript. O índice passa a 3."
  - rotulo: Parada
    conteudo: "A condição 3 < 3 é false. O laço termina sem consultar tarefas[3], uma posição que não contém tarefa."
```

`indice = indice + 1` usa a soma da aula 05 e a reatribuição da aula 03. O índice usa `let` porque seu valor muda. Não altere o array dentro deste laço de leitura.

### 3. Confira quantidades diferentes

No mesmo exemplo, acrescente o texto `"Ler história"` como quarto elemento do array, separado por vírgula. Salve e atualize. A repetição deve mostrar as quatro tarefas sem você acrescentar outro `console.log`.

Depois, substitua a declaração por `const tarefas = [];`, mantendo o laço igual. Salve e atualize. **Nenhuma mensagem nova de tarefa aparece**: antes da primeira passagem, `0 < 0` já é falso. Limpe mensagens antigas do console, se necessário, para conferir esse caso.

:::atencao Apareceu undefined depois das tarefas
**Sintoma:** o programa mostra as tarefas e mais uma consulta sem tarefa no final.

**Solução:** confira se a condição é `indice < tarefas.length`. A quantidade não é um índice ocupado. O programa deve parar quando o índice chegar à quantidade, sem executar mais uma passagem.
:::

:::atencao A página ficou sem responder
**Sintoma:** depois de editar o laço, a execução não termina.

**Solução:** encerre a aba se necessário e corrija o arquivo antes de reabrir a página. Confira se o avanço é `indice = indice + 1` e se a condição usa `<`. Sem avanço, o mesmo índice pode manter a condição verdadeira indefinidamente. Use o modelo completo e não teste laços sem condição de parada.
:::

### 4. Confira todas as tarefas após cada envio

Vamos retomar o formulário da aula 15. Mantenha o HTML daquela aula e substitua o conteúdo de **`script.js`** pelo programa completo abaixo:

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
    campo.value = "";

    for (let indice = 0; indice < tarefas.length; indice = indice + 1) {
      console.log(tarefas[indice]);
    }
  }
}

const formulario = document.getElementById("formulario-tarefa");
formulario.addEventListener("submit", adicionarTarefa);
```

Salve e atualize. Após o primeiro envio válido, o console mostra a primeira tarefa. Após o segundo, mostra **a primeira e a segunda** novamente. Isso é esperado: cada envio percorre o array inteiro. A lista visual continua ganhando apenas um item por envio; o laço está somente conferindo os dados no console.

:::dica Use uma repetição que acompanhe os dados
Ao programar uma lista, usar sua quantidade como limite evita depender de um número fixo de itens. Conferir o array vazio e depois acrescentar um elemento ajuda a verificar se o laço realmente acompanha os dados.
:::

## Prática

### Percorra sua lista

Use o programa completo da etapa 4 com o HTML da aula 15.

1. Atualize e envie três tarefas, uma por vez.
2. Confira a lista visual com três itens. No último envio, observe a sequência das três tarefas no console.
3. Envie texto vazio e só com espaços. Confira que os dados e a lista não crescem.
4. Explique à dupla os valores do índice nas três passagens e a condição que encerra o laço.

### Confira antes de entregar

Mostre ao professor a primeira posição **0**, a última posição **2** e a quantidade **3** no seu exemplo com três tarefas. Explique por que mensagens do console se repetem entre envios sem significar duplicação de itens na página. Guarde a pasta.

## Avaliação

```quiz
- pergunta: Um array tem três tarefas. Quais índices o laço do modelo consulta?
  alternativas:
    - texto: 1, 2 e 3
    - texto: 0, 1 e 2
      correta: true
    - texto: 0, 1, 2 e 3
  feedback: >
    Os índices começam em zero e a condição usa indice < tarefas.length. O índice 3 encerra o laço antes da consulta.
- pergunta: Qual parte faz o laço avançar para a próxima posição?
  alternativas:
    - texto: indice = indice + 1
      correta: true
    - texto: const tarefas = []
    - texto: console.log(tarefas[indice])
  feedback: >
    A reatribuição aumenta o índice após cada passagem. Criar o array e consultar um valor não fazem esse avanço.
- pergunta: Com um array vazio, quantas vezes o bloco do laço do modelo é executado?
  alternativas:
    - texto: Uma vez para mostrar undefined
    - texto: Repetidamente até adicionar uma tarefa
    - texto: Nenhuma, pois 0 < 0 é falso
      correta: true
  feedback: >
    A condição é conferida antes do bloco. Com quantidade zero, não há primeira passagem.
```

## Fechamento

- O **`for` repete um bloco** enquanto sua condição permite.
- O índice começa em **0** e avança uma posição por passagem.
- **`indice < tarefas.length`** evita consultar além dos elementos existentes.
- Teste **array vazio e quantidades diferentes** antes de confiar no laço.

Na próxima aula, vamos percorrer as tarefas com `forEach` e montar a lista visual a partir dos dados.

:::roteiro
0–6 min: índices e quantidade. 6–20 min: acompanhar as passagens do for pelo diagrama progressivo, pedindo a previsão da turma antes de cada camada e anotando o índice no quadro. 20–30 min: quatro tarefas e array vazio; diagnóstico do limite e avanço. 30–36 min: integrar a conferência ao formulário conhecido. 36–46 min: prática. 46–50 min: quiz e fechamento. RCO 86/92 reorganizado pelo plano: for com avanço explícito, sem ++, break, continue ou alterações do array durante a leitura. O exemplo final percorre dados no console, não reconstrói o DOM ainda.
:::
