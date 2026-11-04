---
titulo: Calculando seus minutos de estudo
tema: JavaScript na prática
disciplina: programacao-front-end
serie: 2ª
prerequisitos: [Consultar variáveis no console, Distinguir string e number]
objetivos:
  - Calcular totais e diferenças com valores numéricos
  - Distinguir soma de números e junção de textos com o operador +
  - Converter textos numéricos com Number antes de somar
trilha: javascript-na-pratica
ordem: 23
slug: calculos-conversoes-minutos-estudo
modo_origem: seed
fontes: [docs/plano-apostila-javascript.md]
revisao: true
status: aprovada
versao: 2
atualizado_em: 2026-11-04
---

Você estudou 20 minutos antes do intervalo e mais 15 depois. Quanto tempo estudou ao todo? E quanto falta para uma meta de 60 minutos? Hoje vamos transformar essas contas em instruções do seu projeto. Também vamos investigar um resultado estranho: por que uma tentativa de somar 20 com 15 pode mostrar 2015?

## Objetivos

- Somar minutos de estudo e calcular quantos faltam para uma meta.
- Prever quando `+` soma números e quando junta textos.
- Usar `Number` para converter um texto numérico antes de calcular.

## Pré-requisitos

Abra a pasta `meus-estudos` no VSCode e o `index.html` no navegador, com a aba **Console** aberta. O HTML deve continuar carregando `script.js`, como na aula 20. Vamos escrever nesse mesmo arquivo e reutilizar `const`, `console.log` e `typeof`. Mantenha o HTML e o CSS: hoje vamos conferir os cálculos no console.

## Desenvolvimento

### 1. Retome o valor e seu tipo

No **`script.js`**, substitua o conteúdo anterior pelo exemplo abaixo. Em cada exemplo completo desta aula, faça essa substituição em vez de juntar os programas. Salve com **Ctrl + S** e atualize a página com **Ctrl + R**.

```javascript
const minutos = 20;
console.log(minutos);
console.log(typeof minutos);
```

O console mostra **20** e depois **number**. Como vimos na aula 22, `20` sem aspas é número; `"20"` entre aspas é texto. O nome da variável não decide o tipo. Vamos usar números para calcular quantidades de minutos.

### 2. Some os períodos e calcule o que falta

Substitua o conteúdo de **`script.js`** por este programa. Antes de executar, faça a conta mentalmente.

```javascript
const primeiroPeriodo = 20;
const segundoPeriodo = 15;
const metaMinutos = 60;

const totalMinutos = primeiroPeriodo + segundoPeriodo;
const minutosRestantes = metaMinutos - totalMinutos;

console.log(totalMinutos);
console.log(minutosRestantes);
```

Salve e atualize. O resultado é **35** e depois **25**. O sinal `+` somou os dois números. O sinal `-` calculou a diferença entre a meta e o total. Cada resultado foi guardado em uma nova variável antes de ser mostrado.

:::conceito Operação e resultado
Uma operação usa valores para produzir um resultado. Em `const totalMinutos = primeiroPeriodo + segundoPeriodo;`, o JavaScript consulta os dois valores, soma e guarda o resultado em `totalMinutos`. O `=` atribui esse resultado ao nome; o `+` realiza a soma.
:::

Você também pode multiplicar com `*` e dividir com `/`. Por exemplo, em um planejamento com dois períodos de 20 minutos, `20 * 2` resulta em **40**. Dividir 40 minutos em dois períodos iguais com `40 / 2` resulta em **20**. Nosso foco prático hoje será somar e calcular a diferença para a meta.

Se o total ultrapassar a meta, essa subtração produzirá um número negativo. Com uma meta de 60 e um total de 70, o resultado será **-10**: você passou 10 minutos da meta. Mais adiante vamos usar condições para escolher uma mensagem adequada a cada caso.

### 3. Descubra por que apareceu 2015

Substitua o conteúdo de **`script.js`** pelo exemplo abaixo. Desta vez os dois valores estão entre aspas.

```javascript
const primeiroPeriodo = "20";
const segundoPeriodo = "15";
const resultado = primeiroPeriodo + segundoPeriodo;

console.log(resultado);
console.log(typeof resultado);
```

Salve e atualize. O console mostra **2015** e depois **string**. Você juntou os textos `20` e `15`, um depois do outro. Essa junção é chamada de **concatenação**.

:::atencao O sinal é o mesmo, mas os valores são diferentes
**Sintoma:** você esperava a soma 35 e recebeu o texto 2015.

**Solução:** confira o tipo dos valores. Com números, `+` soma; com textos, junta. Se uma das partes for um texto e a outra for um número, `+` também pode formar um texto: `"20" + 15` resulta em `"2015"`. Para somar quantidades, converta os textos numéricos antes da operação.
:::

### 4. Converta antes de somar

Substitua o conteúdo de **`script.js`** por este programa. Os valores de origem continuam sendo textos; agora vamos criar as versões numéricas antes de somá-las.

```javascript
const primeiroTexto = "20";
const segundoTexto = "15";

const primeiroNumero = Number(primeiroTexto);
const segundoNumero = Number(segundoTexto);
const totalMinutos = primeiroNumero + segundoNumero;

console.log(totalMinutos);
console.log(typeof totalMinutos);
```

Salve e atualize. Agora o resultado é **35** e **number**. `Number(primeiroTexto)` converteu o texto `"20"` em número. O resultado da conversão foi guardado em `primeiroNumero`. A variável `primeiroTexto` continua guardando o texto original.

Escreva **`Number` com N maiúsculo** e coloque entre parênteses o valor que pretende converter. Essa função de conversão já existe no JavaScript; você não precisa criá-la.

:::atencao A conversão mostrou NaN
**Sintoma:** você tentou converter `"20 minutos"` e recebeu `NaN` no cálculo.

**Solução:** neste exercício, use um texto contendo apenas o número, como `"20"`. `Number("20 minutos")` não converte essa frase em um número válido; `NaN` indica esse resultado inválido para uma quantidade numérica. Para decimais no código, use ponto, como em `"2.5"`. Salve e atualize depois de corrigir.
:::

:::dica Confira os dados antes da conta
Em uma aplicação, números podem chegar escritos como texto. Quem desenvolve precisa conferir os valores e seus tipos antes de calcular. Nesta aula você controla os textos usados no exemplo; quando chegarmos aos formulários, vamos retomar a conversão e a verificação dos dados recebidos.
:::

## Prática

### Seu planejamento em minutos

Substitua o conteúdo de **`script.js`** pelo programa completo abaixo. Ele converte dois textos, soma os períodos e calcula a diferença para a meta.

```javascript
const primeiroTexto = "20";
const segundoTexto = "15";
const metaMinutos = 60;

const totalMinutos = Number(primeiroTexto) + Number(segundoTexto);
const minutosRestantes = metaMinutos - totalMinutos;

console.log(totalMinutos);
console.log(minutosRestantes);
console.log(typeof totalMinutos);
```

1. Execute o exemplo original. Confira as mensagens **35**, **25** e **number**, nessa ordem.
2. Troque os textos de origem por `"10"` e `"25"`. Antes de executar, preveja o total e a diferença para a meta.
3. Escolha dois períodos e uma meta para seus estudos. Para este teste, escolha um total menor que a meta. Mantenha os períodos entre aspas e a meta sem aspas.
4. Salve, atualize e explique à sua dupla onde a conversão acontece e onde a soma é feita.

### Confira antes de entregar

Mostre seu código e as três mensagens no console para o professor. O total deve ser a soma dos seus períodos, a diferença deve ser a meta menos esse total e o tipo do total deve ser `number`. Guarde a pasta para a aula 24. A lista visível no HTML ainda permanece como você a escreveu; os cálculos desta aula aparecem no console.

## Avaliação

Tente prever o resultado antes de testar no arquivo. Ao terminar a conferência, restaure sua versão da prática.

```quiz
- pergunta: Você tem dois períodos numéricos de 20 e 15 minutos e uma meta de 60. Quais são o total e a diferença da meta para o total?
  alternativas:
    - texto: Total 35 e diferença 25
      correta: true
    - texto: Total 2015 e diferença 60
    - texto: Total 35 e diferença 95
  feedback: >
    A soma 20 + 15 produz 35. A subtração 60 - 35 produz 25. Juntar textos produziria 2015; somar meta e total produziria 95, mas não a diferença solicitada.
- pergunta: Qual é o resultado de "20" + "15" neste exemplo?
  alternativas:
    - texto: O número 35
    - texto: O texto 2015
      correta: true
    - texto: O número 5
  feedback: >
    Os valores entre aspas são textos e o operador + os concatena. A soma numérica exigiria valores numéricos; 5 seria uma diferença entre os números, não essa operação.
- pergunta: primeiroTexto guarda "20" e segundoTexto guarda "15". Qual expressão produz o número 35?
  alternativas:
    - texto: primeiroTexto + segundoTexto
    - texto: Number(primeiroTexto + segundoTexto)
    - texto: Number(primeiroTexto) + Number(segundoTexto)
      correta: true
  feedback: >
    É preciso converter cada texto antes de somar. Somar os textos primeiro produz 2015; converter essa junção depois produz o número 2015, não 35.
```

## Fechamento

- Com valores numéricos, **`+` soma** e **`-` calcula a diferença**.
- Com textos, **`+` pode juntar valores** em vez de somar quantidades.
- **`Number` converte** um texto numérico; converta cada parcela antes da soma.
- **`typeof` ajuda a conferir** se o resultado tem o tipo esperado.

Na próxima aula, vamos comparar o total estudado com a meta e observar respostas `true` e `false`.

:::roteiro
0–6 min: retomar número, texto, console e arquivo conectado. 6–17 min: soma e diferença com períodos de estudo; multiplicação e divisão apenas como reconhecimento, sem atividade adicional. 17–27 min: prever e executar a junção de textos. 27–35 min: Number aplicado a cada parcela antes de somar; mostrar que converter o resultado da junção não resolve a soma pretendida. 35–45 min: prática. 45–50 min: avaliação e fechamento. Adaptação das conversões do RCO 80 e operações do RCO 90: prioridade para conversão explícita de textos numéricos; coerção geral e validação de entrada ficam para etapas posteriores. Não introduzir parseInt, formulários, condições, precedência complexa ou arredondamento. A meta e os valores são literais controlados; a advertência sobre NaN evita prometer conversão de qualquer frase.
:::
