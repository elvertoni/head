---
titulo: Comparando seus minutos com a meta
tema: JavaScript na prática
disciplina: programacao-front-end
serie: 2ª
prerequisitos: [Calcular valores numéricos, Reconhecer booleanos e conferir tipos]
objetivos:
  - Comparar quantidades numéricas com os operadores > e <
  - Verificar igualdade de valores e tipos com ===
  - Prever e conferir o resultado booleano de comparações simples
trilha: javascript-na-pratica
ordem: 24
slug: comparando-minutos-e-meta
modo_origem: seed
fontes: [docs/plano-apostila-javascript.md]
revisao: true
status: aprovada
versao: 2
atualizado_em: 2026-11-04
---

Você combinou estudar 30 minutos e já estudou 20. Seu tempo está abaixo da meta, acima dela ou exatamente igual? Você consegue responder olhando os números. Hoje vai escrever essas perguntas em JavaScript e conferir as respostas no console. O programa vai responder com os booleanos que você já conhece: `true` e `false`.

## Objetivos

- Usar `>` e `<` para comparar quantidades numéricas.
- Usar `===` para conferir igualdade de valor e tipo.
- Prever uma resposta `true` ou `false` e conferir a execução no console.

## Pré-requisitos

Abra a pasta `meus-estudos` no VSCode, o `index.html` no navegador e a aba **Console**. O HTML continua conectado a `script.js`. Você vai reutilizar números, textos, booleanos e `console.log`. Quando precisar conferir um tipo, retome `typeof` da aula 22. O HTML e o CSS permanecem como estão; as comparações aparecerão no console.

## Desenvolvimento

### 1. Retome os valores antes de perguntar

No **`script.js`**, substitua o conteúdo anterior por este exemplo completo. Salve com **Ctrl + S**, atualize a página com **Ctrl + R** e confira os valores.

```javascript
const minutosEstudados = 20;
const metaMinutos = 30;

console.log(minutosEstudados);
console.log(metaMinutos);
```

O console mostra **20** e depois **30**. Os dois valores são números, sem aspas. Imagine uma régua de tempo: 20 fica antes de 30. A pergunta “20 é menor que 30?” tem resposta **sim**. Vamos escrever essa pergunta com um operador de comparação.

### 2. Pergunte se é menor ou maior

Substitua o conteúdo de **`script.js`** pelo programa abaixo. Primeiro, leia cada comparação como uma pergunta.

```javascript
const minutosEstudados = 20;
const metaMinutos = 30;

console.log(minutosEstudados < metaMinutos);
console.log(minutosEstudados > metaMinutos);
```

Salve e atualize. O console mostra **true** e depois **false**. A primeira pergunta é “20 é menor que 30?”, que é verdadeira. A segunda é “20 é maior que 30?”, que é falsa.

:::conceito Comparação
Uma **comparação** verifica uma relação entre valores e produz uma resposta booleana. Para números, `<` significa **menor que** e `>` significa **maior que**. Leia da esquerda para a direita: `20 < 30` pergunta se 20 é menor que 30; `20 > 30` pergunta se 20 é maior que 30.
:::

Esses símbolos não são tags HTML neste trecho. No `script.js`, estão entre dois valores e fazem comparações. As tags, como `<h1>`, continuam no arquivo HTML.

Agora troque o valor inicial de `minutosEstudados` para **40**, mantendo a meta em **30**. Antes de executar, preveja as respostas. Salve e atualize: a primeira comparação deve mostrar **false**, e a segunda, **true**.

`false` não indica que o programa falhou. É uma resposta válida: por exemplo, a afirmação “40 é menor que 30” é falsa. Ao contrário de uma reatribuição, uma comparação não muda os números que está verificando.

### 3. Confira se é exatamente igual

Substitua o conteúdo de **`script.js`** pelo exemplo abaixo:

```javascript
const minutosEstudados = 30;
const metaMinutos = 30;

console.log(minutosEstudados === metaMinutos);
console.log(minutosEstudados < metaMinutos);
console.log(minutosEstudados > metaMinutos);
```

Salve e atualize. O resultado é **true**, **false** e **false**. Os números são iguais; nenhum é menor ou maior que o outro. Com `>` e `<`, a igualdade não está incluída.

O operador **`===`**, com três sinais de igual, verifica a igualdade sem converter um tipo em outro. Para os textos, números e booleanos que estudamos, os valores precisam ter o mesmo tipo e ser iguais para o resultado ser `true`.

:::atencao Atribuir é diferente de comparar
**Sintoma:** você queria perguntar se os valores são iguais, mas escreveu uma linha com apenas `=`, como `minutosEstudados = metaMinutos;`.

**Solução:** use `===` para a comparação de igualdade desta aula. Um `=` faz atribuição, como na criação de uma variável. Se você tentar reatribuir uma variável criada com `const`, ainda receberá um erro de reatribuição. Confira a quantidade de sinais, salve e atualize.
:::

### 4. Compare também os tipos

Substitua o conteúdo de **`script.js`** pelo exemplo abaixo. Os dois valores parecem representar 30 minutos, mas só um foi escrito como número.

```javascript
const minutosComoTexto = "30";
const metaMinutos = 30;

console.log(typeof minutosComoTexto);
console.log(typeof metaMinutos);
console.log(minutosComoTexto === metaMinutos);
console.log(Number(minutosComoTexto) === metaMinutos);
```

Salve e atualize. O console mostra **string**, **number**, **false** e **true**. O texto `"30"` não é igual ao número `30` na comparação com `===`. Na última linha, você converteu o texto para número antes de comparar: agora os dois lados são o número 30.

:::atencao Parece o mesmo número, mas a igualdade deu false
**Sintoma:** você vê 30 nos dados e esperava igualdade, mas `===` retorna `false`.

**Solução:** confira os tipos com `typeof`. Se uma quantidade estiver guardada como texto numérico, use a conversão explícita com `Number` antes da comparação. Nos exemplos de maior e menor desta aula, mantenha os dois lados como números. Escrever somente algarismos dentro de aspas ainda produz texto.
:::

:::dica Escreva a pergunta antes do operador
Ao desenvolver uma regra, diga primeiro o que quer descobrir: “o tempo estudado é menor que a meta?”. Depois escolha o operador e confira com valores conhecidos. Teste um valor abaixo, um igual e um acima. Essa rotina ajuda a encontrar erros de limite antes de usar a comparação em uma decisão.
:::

## Prática

### Três testes para a mesma meta

Substitua o conteúdo de **`script.js`** pelo programa completo abaixo. A ordem das mensagens será sempre **menor**, **igual** e **maior**.

```javascript
const minutosEstudados = 20;
const metaMinutos = 30;

console.log(minutosEstudados < metaMinutos);
console.log(minutosEstudados === metaMinutos);
console.log(minutosEstudados > metaMinutos);
```

1. Execute com **20** minutos e meta **30**. Confira **true**, **false**, **false**.
2. Troque somente o valor inicial de `minutosEstudados` para **30**. Antes de executar, preveja as três respostas. Salve e atualize.
3. Repita com **40** minutos. Mantenha os valores numéricos, sem aspas, e a meta em **30**.
4. Escolha uma meta sua e um tempo estudado. Explique à dupla o significado de cada resposta, na ordem em que aparece.

### Confira antes de entregar

Para **30** e **30**, as respostas devem ser **false**, **true**, **false**. Para **40** e **30**, devem ser **false**, **false**, **true**. Mostre os três testes para o professor e diga por que, quando os números são iguais, tanto `<` quanto `>` respondem `false`. Guarde a pasta: vamos usar essa comparação na próxima aula para escolher uma mensagem.

## Avaliação

Leia a comparação como uma pergunta e confira qual relação está sendo testada.

```quiz
- pergunta: minutosEstudados vale 20 e metaMinutos vale 30. Qual resposta minutosEstudados < metaMinutos produz?
  alternativas:
    - texto: true, porque 20 é menor que 30
      correta: true
    - texto: false, porque 20 não é igual a 30
    - texto: O número 10
  feedback: >
    O operador < verifica se o primeiro número é menor que o segundo. A igualdade é outra pergunta. Calcular 30 - 20 daria 10, mas uma comparação produz um booleano.
- pergunta: minutosEstudados e metaMinutos valem 30. Quais são os resultados de <, === e >, nessa ordem?
  alternativas:
    - texto: true, true, true
    - texto: false, true, false
      correta: true
    - texto: false, false, false
  feedback: >
    Dois números iguais satisfazem ===. Nenhum é menor nem maior que o outro, por isso < e > respondem false. A igualdade não está incluída nesses dois operadores.
- pergunta: minutosComoTexto guarda "30" e metaMinutos guarda 30. Qual expressão retorna true para a igualdade numérica após uma conversão explícita?
  alternativas:
    - texto: minutosComoTexto === metaMinutos
    - texto: minutosComoTexto = metaMinutos
    - texto: Number(minutosComoTexto) === metaMinutos
      correta: true
  feedback: >
    Number converte o texto numérico antes de ===. Sem conversão, os tipos são diferentes. Um único = faz atribuição, não a comparação solicitada.
```

## Fechamento

- **`<` pergunta se é menor** e **`>` pergunta se é maior**; números iguais não satisfazem essas duas relações.
- **`===` verifica igualdade** de valor e tipo nos dados estudados.
- Uma comparação produz **`true` ou `false`** e não troca o valor das variáveis.
- Teste sempre **abaixo, igual e acima** do limite que sua regra utiliza.

Na próxima aula, vamos usar uma comparação dentro de `if` e escolher entre duas mensagens com `else`.

:::roteiro
0–6 min: retomar valores numéricos e booleanos. 6–18 min: executar < e >, ler da esquerda para a direita e trocar 20 por 40. 18–27 min: comparar valores iguais com === e verificar os limites estritos. 27–35 min: texto numérico, typeof e conversão explícita. 35–45 min: prática com abaixo, igual e acima. 45–50 min: quiz e fechamento. Adaptação dos operadores do RCO 91 ao plano: apenas <, > e === nesta etapa; demais comparações e operadores lógicos ficam para retomadas futuras. As advertências distinguem atribuição de comparação e evitam depender de conversão implícita. Não ensinar == nem condições nesta aula. Priorizar a justificativa das respostas em vez da memorização de símbolos.
:::
