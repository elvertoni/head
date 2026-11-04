---
titulo: Organizando ações com funções
tema: JavaScript na prática
disciplina: programacao-front-end
serie: 2ª
prerequisitos: [Mostrar mensagens no console, Usar variáveis e if com else]
objetivos:
  - Definir uma função sem parâmetros com um nome que descreva a ação
  - Executar e reutilizar a função por meio de chamadas
  - Prever a ordem das mensagens ao chamar uma função com uma decisão
trilha: javascript-na-pratica
ordem: 27
slug: funcoes-organizando-acoes-estudo
modo_origem: seed
fontes: [docs/plano-apostila-javascript.md]
revisao: true
status: aprovada
versao: 2
atualizado_em: 2026-11-04
---

Você já tem uma regra que confere sua meta de estudo. Em vez de copiar essa regra toda vez que precisar dela, pode reunir as instruções e dar um nome à ação, como “conferir meta”. Pense em uma receita curta: escrever os passos não prepara o lanche; é preciso seguir os passos quando quiser o resultado. Hoje vamos fazer essa diferença aparecer no console.

## Objetivos

- Criar uma função sem parâmetros usando `function` e um nome claro.
- Chamar a função para executar suas instruções e reutilizá-las.
- Prever a ordem das mensagens em um programa que chama uma função.

## Pré-requisitos

Abra `meus-estudos` no VSCode e sua página no navegador, com o **Console** aberto. Vamos trabalhar no mesmo `script.js`, conectado ao HTML. Você vai retomar mensagens e o `if`/`else` da aula 25. Os testes continuam no console; o HTML e o CSS não precisam de alterações nesta aula.

## Desenvolvimento

### 1. Retome uma ação que você já conhece

Substitua o conteúdo de **`script.js`** por este programa. Salve com **Ctrl + S** e atualize com **Ctrl + R**.

```javascript
console.log("Hora de estudar!");
console.log("Escolha uma tarefa da sua lista.");
```

O console mostra as duas mensagens, nessa ordem. Essas linhas formam um lembrete. Vamos organizar o lembrete como uma ação com nome. Execute um exemplo completo de cada vez, substituindo o conteúdo do arquivo em cada etapa.

### 2. Dê um nome à ação

Substitua o conteúdo de **`script.js`** pelo programa abaixo:

```javascript
function mostrarLembrete() {
  console.log("Hora de estudar!");
  console.log("Escolha uma tarefa da sua lista.");
}
```

Salve e atualize. **Nenhuma mensagem nova desse lembrete deve aparecer ainda.** Se o console mantiver registros antigos, limpe-os pelo botão de limpar e atualize novamente.

:::conceito Definir uma função
Uma **função** reúne instruções que podem ser executadas por uma chamada. `function` inicia a definição; `mostrarLembrete` é o nome que escolhemos; as chaves delimitam suas instruções. Nesta aula, os parênteses ficam vazios porque as funções não recebem informações por parâmetros.
:::

Escrever a definição guarda a ação para poder chamá-la. É como ter a receita escrita: os passos estão organizados, mas ainda não foram executados. Vamos usar nomes que descrevam uma ação, como `mostrarLembrete` e `conferirMeta`.

### 3. Chame e reutilize a função

Substitua o conteúdo de **`script.js`** pelo exemplo completo abaixo. As duas linhas depois da chave de fechamento são **chamadas** da função.

```javascript
function mostrarLembrete() {
  console.log("Hora de estudar!");
  console.log("Escolha uma tarefa da sua lista.");
}

mostrarLembrete();
mostrarLembrete();
```

Salve e atualize. O par de mensagens aparece **duas vezes**:

```txt
Hora de estudar!
Escolha uma tarefa da sua lista.
Hora de estudar!
Escolha uma tarefa da sua lista.
```

Em cada chamada, `mostrarLembrete();`, o programa executa as instruções da função e depois continua na linha seguinte à chamada. Você escreveu as instruções uma vez e pediu a execução duas vezes. Se mudar o texto dentro da função, todas as chamadas usarão essa definição na próxima execução do arquivo.

:::atencao A função existe, mas nada aconteceu
**Sintoma:** não aparece mensagem nova, embora a definição de `mostrarLembrete` esteja no arquivo.

**Solução:** confira se existe uma chamada `mostrarLembrete();` fora das chaves da função. Escrever somente `mostrarLembrete;` não faz a chamada; faltam os parênteses. Não coloque a chamada dentro da própria função nesta atividade. Salve e atualize.
:::

### 4. Organize a conferência da meta

Vamos colocar uma decisão conhecida dentro de uma função. Substitua o conteúdo de **`script.js`** por este programa:

```javascript
function conferirMeta() {
  const minutosEstudados = 20;
  const metaMinutos = 30;

  if (minutosEstudados < metaMinutos) {
    console.log("Ainda falta estudar.");
  } else {
    console.log("Meta atingida!");
  }
}

console.log("Iniciando conferência.");
conferirMeta();
console.log("Conferência encerrada.");
```

Salve e atualize. O resultado é:

```txt
Iniciando conferência.
Ainda falta estudar.
Conferência encerrada.
```

O programa chegou à mensagem inicial, chamou `conferirMeta`, executou a decisão e voltou para continuar após a chamada. As duas variáveis deste exemplo são criadas dentro da função e usadas ali. Para testar outra quantidade, altere o número nessa definição, salve e atualize.

Observe as chaves: há um par para a função e outros para `if` e `else`. O recuo ajuda você a enxergar quais instruções pertencem a cada bloco. O `if` continua fazendo a mesma pergunta da aula 25; apenas organizamos a ação em uma função.

:::atencao O nome chamado não é o nome definido
**Sintoma:** o console aponta que uma função não foi definida.

**Solução:** compare o nome na definição e na chamada. `conferirMeta` e `ConferirMeta` são nomes diferentes. Use o mesmo nome, com as mesmas letras, e confira os parênteses da chamada. Salve e atualize.
:::

:::dica Uma ação com nome fica mais fácil de encontrar
Em uma aplicação, funções ajudam a organizar ações e reutilizar instruções. Quando você lê `conferirMeta();`, o nome já indica o propósito. Comece com uma responsabilidade por função. Nas próximas aulas, uma função vai reunir a ação que será executada quando o usuário clicar em um botão.
:::

## Prática

### Seu lembrete de estudos

Substitua o conteúdo de **`script.js`** pelo programa completo abaixo:

```javascript
function mostrarPlano() {
  const tarefa = "Revisar HTML";
  console.log("Minha próxima tarefa:");
  console.log(tarefa);
}

console.log("Abrindo meu plano.");
mostrarPlano();
console.log("Plano conferido.");
```

1. Antes de executar, preveja as quatro mensagens. Salve, atualize e confira a ordem.
2. Troque o texto da tarefa por uma atividade sua e execute novamente.
3. Acrescente **mais uma chamada `mostrarPlano();` depois da primeira chamada**, fora da função. Preveja quantas mensagens aparecerão e confira.
4. Retire a chamada extra. Explique à sua dupla a diferença entre o trecho que define a função e a linha que a executa.

### Confira antes de entregar

Com uma chamada e a tarefa original, o console deve mostrar **Abrindo meu plano.**, **Minha próxima tarefa:**, **Revisar HTML** e **Plano conferido.**, nessa ordem. Com duas chamadas, as duas mensagens da função se repetem e o total passa a seis mensagens. Termine com uma chamada, mostre o código ao professor e guarde a pasta.

## Avaliação

Pense em quando o programa chega à chamada e no que pertence ao bloco da função.

```quiz
- pergunta: Você escreveu a definição de mostrarLembrete, mas não chamou essa função. O que acontece com as mensagens dentro dela?
  alternativas:
    - texto: Aparecem automaticamente duas vezes
    - texto: Não são executadas apenas por definir a função
      correta: true
    - texto: Aparecem ao trocar a cor no CSS
  feedback: >
    Definir a função organiza as instruções. A execução do corpo depende de uma chamada nesse programa; mudar CSS não chama essa função.
- pergunta: Qual linha chama a função mostrarPlano sem parâmetros?
  alternativas:
    - texto: mostrarPlano();
      correta: true
    - texto: mostrarPlano;
    - texto: 'console.log("mostrarPlano");'
  feedback: >
    Os parênteses fazem a chamada. O nome sozinho não a executa, e mostrar o texto mostrarPlano no console não executa as instruções da função.
- pergunta: No exemplo conferirMeta com 20 minutos e meta 30, qual mensagem aparece entre Iniciando conferência. e Conferência encerrada.?
  alternativas:
    - texto: Meta atingida!
    - texto: As duas mensagens dos blocos if e else
    - texto: Ainda falta estudar.
      correta: true
  feedback: >
    A chamada executa a função; a condição 20 < 30 é verdadeira e escolhe Ainda falta estudar. Depois a execução continua na mensagem após a chamada.
```

## Fechamento

- **Definir** uma função dá nome e organiza as instruções entre chaves.
- **Chamar** a função com `nomeDaFuncao();` executa suas instruções.
- Você pode **reutilizar a ação** chamando a mesma função mais de uma vez.
- Depois da execução da função, o programa **continua após a chamada** nesses exemplos.

Na próxima aula, vamos localizar um elemento do HTML pelo JavaScript e mudar o texto que aparece na página.

:::roteiro
0–6 min: retomar duas mensagens conhecidas. 6–17 min: definir sem chamar e observar a ausência de novas mensagens; explicar que esse é um resultado esperado. 17–27 min: chamada e duas execuções com previsão das saídas. 27–35 min: organizar if/else em conferirMeta e acompanhar o caminho de volta após a chamada. 35–45 min: prática. 45–50 min: quiz e fechamento. Complemento pedagógico aprovado no plano para preparar DOM e eventos do RCO: funções nomeadas sem parâmetros, sem retorno e com uma ação principal. Não introduzir arrow functions, recursão, callbacks, escopo formal ou passagem de argumentos. Todas as instruções essenciais ao aluno estão no corpo, incluindo não chamar a função dentro dela mesma nesta atividade.
:::
