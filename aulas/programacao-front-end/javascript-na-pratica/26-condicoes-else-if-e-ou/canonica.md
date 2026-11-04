---
titulo: Mais caminhos e condições com else if, E e OU
tema: JavaScript na prática
disciplina: programacao-front-end
serie: 2ª
prerequisitos: [Comparar números, Usar if e else, Reconhecer booleanos]
objetivos:
  - Escolher entre três caminhos usando else if
  - Exigir duas condições booleanas verdadeiras com &&
  - Aceitar pelo menos uma condição booleana verdadeira com o operador OU
trilha: javascript-na-pratica
ordem: 26
slug: condicoes-else-if-e-ou
modo_origem: seed
fontes: [docs/plano-apostila-javascript.md]
revisao: true
status: aprovada
versao: 2
atualizado_em: 2026-11-04
---

Na aula anterior, chegar à meta e ultrapassar a meta produziam a mesma mensagem. E se você quiser distinguir essas situações? Também há regras com duas perguntas: para encerrar sua revisão, você pode precisar concluir a tarefa E revisar o conteúdo. Hoje vamos ampliar uma decisão de cada vez, como uma lista de conferência em que você precisa saber quais itens são obrigatórios.

## Objetivos

- Usar `else if` para distinguir tempo abaixo, igual e acima da meta.
- Usar `&&` quando duas condições precisam ser verdadeiras.
- Usar `||` quando basta pelo menos uma condição verdadeira.

## Pré-requisitos

Abra `meus-estudos` no VSCode e sua página no navegador com a aba **Console**. Continue usando `index.html` conectado a `script.js`. As mensagens desta aula aparecem no console. O HTML organiza sua página e o CSS define sua aparência, mas não precisam de alteração hoje. Retome o `if`/`else` da aula 25 se ainda tiver dificuldade para localizar os blocos.

## Desenvolvimento

### 1. Retome os dois caminhos

Substitua o conteúdo de **`script.js`** pelo programa abaixo. Execute um exemplo completo de cada vez, sem juntar todos no arquivo. Salve com **Ctrl + S** e atualize a página com **Ctrl + R**.

```javascript
const minutosEstudados = 30;
const metaMinutos = 30;

if (minutosEstudados < metaMinutos) {
  console.log("Ainda falta estudar.");
} else {
  console.log("Meta atingida!");
}
```

A mensagem é **Meta atingida!**. Como vimos, o `else` atende tanto à igualdade quanto ao valor acima da meta. Agora vamos separar esses dois casos.

### 2. Acrescente uma pergunta com else if

Substitua o conteúdo do **`script.js`** pelo programa completo abaixo:

```javascript
const minutosEstudados = 30;
const metaMinutos = 30;

if (minutosEstudados < metaMinutos) {
  console.log("Ainda falta estudar.");
} else if (minutosEstudados === metaMinutos) {
  console.log("Você chegou à meta!");
} else {
  console.log("Você passou da meta!");
}
```

Salve e atualize. Você deve ver **Você chegou à meta!**. Troque os minutos para **20**, salve e atualize: deve aparecer **Ainda falta estudar.**. Repita com **40**: deve aparecer **Você passou da meta!**.

:::conceito Uma sequência de escolhas
`else if` significa “senão, se”. O programa testa o primeiro `if`. Se a condição for falsa, testa a condição do `else if`. Quando encontra uma verdadeira, executa aquele bloco e pula os demais dessa sequência. O `else` final atende quando nenhuma condição anterior foi verdadeira.
:::

Nesta regra, com números válidos, a primeira pergunta verifica se está abaixo; a segunda, se está igual. O caso restante é estar acima. Não coloque outra condição depois do `else` final. Repare que `else if` tem espaço entre as palavras.

### 3. Exija duas respostas verdadeiras com E

Vamos usar outra regra: a revisão só está pronta quando **a tarefa foi concluída E a revisão foi concluída**. Substitua o conteúdo de **`script.js`** pelo programa abaixo.

```javascript
const tarefaConcluida = true;
const revisaoConcluida = false;

if (tarefaConcluida && revisaoConcluida) {
  console.log("Tudo pronto para encerrar.");
} else {
  console.log("Confira o que falta concluir.");
}
```

Salve e atualize. A mensagem é **Confira o que falta concluir.**. Uma informação é `true`, mas a outra é `false`. Troque `revisaoConcluida` para `true`, salve e atualize: agora aparece **Tudo pronto para encerrar.**.

O operador **`&&`** representa **E**. Com as condições booleanas deste exercício, o resultado só é `true` quando **as duas** são verdadeiras. Se qualquer uma for `false`, a condição combinada será falsa. Use dois sinais `&` juntos.

### 4. Aceite pelo menos uma resposta verdadeira com OU

Agora a regra é outra: registrar que você praticou conteúdo web quando **estudou HTML OU estudou CSS**. Substitua o conteúdo de **`script.js`** por este exemplo:

```javascript
const estudouHTML = true;
const estudouCSS = false;

if (estudouHTML || estudouCSS) {
  console.log("Você praticou conteúdo web hoje.");
} else {
  console.log("Escolha um conteúdo para começar.");
}
```

Salve e atualize. O console mostra **Você praticou conteúdo web hoje.**. O operador **`||`** representa **OU**: com os booleanos do exemplo, basta **pelo menos uma** condição verdadeira. Se as duas forem verdadeiras, também conta. A condição só será falsa quando as duas forem `false`.

O símbolo `|` é a barra vertical, diferente de `/`. Se tiver dificuldade para localizá-lo no teclado do laboratório, copie `||` do exemplo e peça ao professor para mostrar a tecla correspondente.

:::atencao E e OU não fazem a mesma pergunta
**Sintoma:** seu programa libera “Tudo pronto” mesmo com uma parte da revisão pendente.

**Solução:** releia a regra. Se exige as duas partes concluídas, use `&&`. Com `||`, uma só já basta. Escreva os operadores completos, com dois símbolos, e use valores `true` ou `false` sem aspas nesses exemplos. Salve e teste novamente.
:::

:::dica Escreva a regra em português antes do código
Quem desenvolve precisa traduzir uma regra em uma condição. “Preciso concluir a tarefa E a revisão” indica `&&`. “Aceito estudar HTML OU CSS” indica `||`. Teste também as combinações que não devem passar. Nesta etapa, use uma combinação por vez, sem misturar os dois operadores na mesma condição.
:::

## Prática

### Confira as três regras

Comece pelo programa completo de **`else if` da etapa 2**, substituindo o conteúdo do `script.js`. Depois use os programas das etapas 3 e 4, um de cada vez. Você tem cerca de 12 minutos para estes testes.

1. Com meta **30**, teste **20**, **30** e **40** no programa com `else if`. Antes de cada execução, preveja a única mensagem escolhida.
2. No programa com `&&`, teste as combinações **true/true**, **true/false**, **false/true** e **false/false**. Diga em qual delas a mensagem “Tudo pronto” deve aparecer.
3. Faça os mesmos quatro testes no programa com `||`. Diga em qual combinação aparece “Escolha um conteúdo para começar”.
4. Escolha uma das regras e personalize suas mensagens, mantendo o significado. Mostre o teste que passa e um que não passa para uma dupla.

### Confira antes de entregar

No programa de três caminhos, as mensagens devem indicar **abaixo**, **igual** e **acima** da meta. Para o programa com `&&`, apenas **true/true** libera “Tudo pronto”. Para o programa com `||`, apenas **false/false** pede para escolher um conteúdo. Mostre ao professor seus testes e explique uma diferença entre E e OU. Termine com o último programa salvo e guarde a pasta.

## Avaliação

Use os valores booleanos e as regras trabalhadas nos exemplos.

```quiz
- pergunta: Com minutosEstudados igual a 30 e metaMinutos igual a 30, qual caminho da etapa 2 é escolhido?
  alternativas:
    - texto: O primeiro if, pois 30 é menor que 30
    - texto: O else if, pois 30 é igual a 30
      correta: true
    - texto: O else final, sem testar a igualdade
  feedback: >
    A primeira condição é falsa. A igualdade do else if é verdadeira, então seu bloco é executado e o else final é pulado.
- pergunta: Uma revisão exige tarefaConcluida E revisaoConcluida. Os valores são true e false. O que a condição com && produz?
  alternativas:
    - texto: false, porque as duas precisariam ser verdadeiras
      correta: true
    - texto: true, porque uma delas é verdadeira
    - texto: true, porque a primeira é verdadeira
  feedback: >
    Com booleanos, && exige as duas condições verdadeiras. Uma resposta falsa impede atender a essa regra. Uma só verdadeira seria suficiente para OU, mas não para E.
- pergunta: Na regra estudouHTML OU estudouCSS, com ||, o que acontece se as duas informações forem true?
  alternativas:
    - texto: A condição fica false porque só uma poderia ser true
    - texto: O programa executa os dois blocos de if e else
    - texto: A condição fica true porque pelo menos uma é verdadeira
      correta: true
  feedback: >
    OU aceita uma ou as duas condições verdadeiras. Não é uma regra de exatamente uma. O par if/else continua executando apenas o bloco correspondente à condição.
```

## Fechamento

- **`else if` acrescenta uma condição** à sequência de escolhas; um bloco dessa sequência é escolhido.
- Com booleanos, **`&&` exige duas respostas verdadeiras**.
- Com booleanos, **`||` aceita pelo menos uma resposta verdadeira**, inclusive as duas.
- Teste **cada caminho e cada combinação**, sem juntar várias regras de uma vez.

Na próxima aula, vamos dar um nome a uma ação e executar seu código usando uma função.

:::roteiro
0–5 min: retomar if/else e igualdade na meta. 5–18 min: três caminhos com else if e testes 20/30/40. 18–27 min: E com dois booleanos; deixar a turma prever antes de testar. 27–35 min: OU nas mesmas quatro combinações. 35–47 min: prática com uma regra por vez; priorizar a explicação das condições sobre a digitação. 47–50 min: quiz e fechamento. Adaptação do RCO 85/91 ao plano: else if e operadores lógicos graduais; somente operandos booleanos, sem ensinar que && e || sempre retornam booleanos em qualquer uso da linguagem. Não introduzir precedência entre operadores lógicos, negação, validação geral ou funções nesta aula.
:::
