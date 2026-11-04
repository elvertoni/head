---
titulo: Escolhendo mensagens com if e else
tema: JavaScript na prática
disciplina: programacao-front-end
serie: 2ª
prerequisitos: [Comparar números com <, Reconhecer true e false]
objetivos:
  - Usar uma comparação como condição de um if
  - Escolher entre duas mensagens usando if e else
  - Testar a decisão com valores abaixo da meta e com a meta atingida ou ultrapassada
trilha: javascript-na-pratica
ordem: 25
slug: decisoes-if-else-meta-estudos
modo_origem: seed
fontes: [docs/plano-apostila-javascript.md]
revisao: true
status: aprovada
versao: 2
atualizado_em: 2026-11-04
---

Se você ainda não chegou ao tempo de estudo planejado, sua lista pode avisar “Ainda falta estudar”. Quando chegar à meta, pode comemorar “Meta atingida!”. Hoje você vai programar essa escolha. É como conferir o horário antes de sair: dependendo da resposta à pergunta, você escolhe o que fazer. Nossa primeira decisão terá apenas dois caminhos e será conferida no console.

## Objetivos

- Colocar uma comparação dentro de um `if`.
- Usar `if` e `else` para mostrar uma entre duas mensagens.
- Conferir a decisão abaixo da meta, exatamente na meta e acima dela.

## Pré-requisitos

Abra a pasta `meus-estudos` no VSCode, a página `index.html` no navegador e a aba **Console**. O `script.js` deve continuar conectado ao HTML. Vamos reutilizar `const`, `console.log`, números e o operador `<` da aula 24. O conteúdo HTML e a aparência CSS da sua página permanecem; hoje a mensagem escolhida aparecerá no console.

## Desenvolvimento

### 1. Retome a pergunta que produz um booleano

Substitua o conteúdo de **`script.js`** pelo exemplo abaixo. Nesta aula, execute um programa completo de cada vez; não acumule declarações copiando todos os exemplos juntos.

```javascript
const minutosEstudados = 20;
const metaMinutos = 30;

console.log(minutosEstudados < metaMinutos);
```

Salve com **Ctrl + S** e atualize o navegador com **Ctrl + R**. O resultado é **true**: 20 é menor que 30. Se o tempo estudado for 30 ou 40, essa mesma comparação será **false**. Retome a aula 24 se precisar conferir esses casos antes de seguir.

Naquela aula, você mostrou a resposta da comparação. Agora vamos usar essa resposta para escolher qual mensagem executar.

### 2. Execute uma mensagem se a condição for verdadeira

Substitua o conteúdo de **`script.js`** por este programa:

```javascript
const minutosEstudados = 20;
const metaMinutos = 30;

if (minutosEstudados < metaMinutos) {
  console.log("Ainda falta estudar.");
}
```

Salve e atualize. O console mostra **Ainda falta estudar.**. Leia o trecho assim: **se os minutos estudados forem menores que a meta, execute esta mensagem**.

:::conceito Condição e bloco
**`if`** significa “se”. A comparação entre parênteses é a **condição**, a pergunta que o programa verifica. O código entre `{` e `}` é o **bloco** controlado por esse `if`. Neste exemplo, quando a condição produz `true`, o programa executa a mensagem do bloco; quando produz `false`, pula esse bloco.
:::

Troque o valor inicial de `minutosEstudados` para **30**, salve e atualize. Neste programa, nenhum comando escreve uma mensagem para esse caso: a condição é falsa e o bloco é pulado. Se mensagens antigas permanecerem no console, observe as novas ou use o botão de limpar do próprio console antes de atualizar.

A falta dessa mensagem nova não significa, por si só, um erro. Falta programar o outro caminho.

### 3. Dê uma alternativa com else

Substitua o conteúdo de **`script.js`** pelo programa completo abaixo. Ele volta a começar com 20 minutos para você conferir o primeiro caminho.

```javascript
const minutosEstudados = 20;
const metaMinutos = 30;

if (minutosEstudados < metaMinutos) {
  console.log("Ainda falta estudar.");
} else {
  console.log("Meta atingida!");
}
```

Salve e atualize. Você deve ver **Ainda falta estudar.**. Agora troque os minutos estudados para **30**, salve e atualize: deve aparecer **Meta atingida!**. Repita com **40**: a mensagem também será **Meta atingida!**.

O **`else`** significa “senão”. Ele apresenta a alternativa quando a condição do `if` é falsa. Aqui a pergunta é “o tempo está abaixo da meta?”. Para os números usados no exercício, se não está abaixo, está na meta ou acima dela. Por isso o `else` atende aos dois casos.

Nesse par `if`/`else`, **só um dos dois blocos é executado a cada passagem pela decisão**. Você não precisa escrever outra comparação após `else` nesta estrutura.

:::atencao A mensagem de meta atingida não aparece no valor exato
**Sintoma:** com 30 minutos estudados e meta 30, seu código não mostra a mensagem esperada.

**Solução:** compare a condição com o modelo `minutosEstudados < metaMinutos`. Quando os números são iguais, `<` responde `false`, e o programa entra no `else`. Não troque a regra por uma verificação apenas de “maior que” para anunciar a meta: chegar exatamente à meta também precisa contar. Salve e teste novamente com 20, 30 e 40.
:::

### 4. Acompanhe o que acontece depois da escolha

Substitua o conteúdo de **`script.js`** pelo exemplo abaixo. Observe que a última mensagem está **depois da chave que fecha o `else`**, fora dos dois blocos.

```javascript
const minutosEstudados = 30;
const metaMinutos = 30;

if (minutosEstudados < metaMinutos) {
  console.log("Ainda falta estudar.");
} else {
  console.log("Meta atingida!");
}

console.log("Conferência encerrada.");
```

Salve e atualize. O console mostra:

```txt
Meta atingida!
Conferência encerrada.
```

O programa verificou a condição, executou apenas o `else` e depois continuou na linha que vem após a decisão. A mensagem final não pertence a nenhum dos dois blocos; neste programa ela aparece nos dois caminhos.

Troque os minutos estudados para **20**, salve e atualize. Agora a primeira mensagem será **Ainda falta estudar.**, seguida de **Conferência encerrada.**. Duas mensagens aparecerem não significa que os dois blocos foram executados: a segunda vem de fora da escolha.

:::atencao Chaves e ponto e vírgula no lugar errado
**Sintoma:** aparece um erro perto de `else`, ou o código deixa de seguir a escolha esperada.

**Solução:** confira cada `{` com sua `}`. O `else` vem logo depois da chave que fecha o bloco do `if`, como no modelo. Não coloque `;` entre a condição e a chave de abertura. O ponto e vírgula continua ao final de cada `console.log`. Mantenha as mensagens dos blocos com dois espaços de recuo para enxergar a organização, salve e atualize.
:::

:::dica Teste a regra nas bordas
Ao programar avisos de uma aplicação, escreva primeiro a regra em uma frase e confira seu limite. Para “atingir 30 minutos”, teste 20, 30 e 40. O caso exatamente igual ajuda a descobrir uma escolha errada de operador. Confira também se cada mensagem está dentro do bloco ao qual deveria pertencer.
:::

## Prática

### Um aviso para sua meta de estudo

Substitua o conteúdo de **`script.js`** pelo programa abaixo. Sua tarefa é prever o caminho antes de cada execução e depois personalizar a meta e as mensagens.

```javascript
const minutosEstudados = 20;
const metaMinutos = 30;

if (minutosEstudados < metaMinutos) {
  console.log("Ainda falta estudar.");
} else {
  console.log("Meta atingida!");
}

console.log("Conferência encerrada.");
```

1. Execute com **20** e meta **30**. Confira **Ainda falta estudar.** e **Conferência encerrada.**.
2. Troque somente os minutos estudados para **30**. Preveja a saída, salve, atualize e confira. Repita com **40**.
3. Escolha uma meta positiva para seus estudos e teste um valor abaixo dela, um igual e um acima. Use números sem aspas.
4. Personalize somente os textos entre aspas dos dois blocos. Mostre à dupla qual mensagem será escolhida em cada caso e por que a mensagem final aparece nos dois caminhos.

### Confira antes de entregar

Com a meta original de **30**, os testes **30** e **40** devem mostrar **Meta atingida!**, seguida de **Conferência encerrada.**. O teste **20** deve mostrar a mensagem de que ainda falta estudar, seguida da mesma mensagem final. Na sua versão, as mensagens podem ser personalizadas, mas devem representar esses mesmos casos. Mostre os três testes e a posição das chaves para o professor. Guarde a pasta para a próxima aula.

## Avaliação

Use a condição `minutosEstudados < metaMinutos` e a meta de 30 minutos como referência. As mensagens são as do programa completo desta aula.

```quiz
- pergunta: Com 20 minutos estudados e meta 30, qual bloco é executado na decisão?
  alternativas:
    - texto: O bloco do if, porque a condição 20 < 30 é verdadeira
      correta: true
    - texto: O bloco do else, porque ainda falta estudar
    - texto: Os dois blocos, porque o arquivo é lido de cima para baixo
  feedback: >
    A comparação é verdadeira, então o programa executa o bloco do if. O else só é executado quando essa condição é falsa. Seguir a execução de cima para baixo inclui respeitar a escolha dos blocos.
- pergunta: Com exatamente 30 minutos estudados e meta 30, qual mensagem o bloco escolhido mostra?
  alternativas:
    - texto: Ainda falta estudar.
    - texto: Meta atingida!
      correta: true
    - texto: Nenhuma, porque dois números iguais não podem ser comparados
  feedback: >
    A comparação 30 < 30 é falsa, então o else mostra Meta atingida!. Os números podem ser comparados; não estar abaixo inclui estar exatamente na meta neste exercício.
- pergunta: Por que Conferência encerrada. aparece tanto no teste com 20 quanto no teste com 40 minutos?
  alternativas:
    - texto: Porque o if sempre executa todos os blocos
    - texto: Porque o navegador ignora as chaves
    - texto: Porque esse console.log está após a decisão e fora dos dois blocos
      correta: true
  feedback: >
    Depois do bloco escolhido, a execução continua na linha após a decisão. As chaves delimitam os blocos e só um deles é executado por passagem; a mensagem final está fora de ambos.
```

## Fechamento

- O **`if` verifica uma condição** e executa seu bloco quando a resposta é `true`.
- O **`else` apresenta a alternativa** quando essa condição é `false`.
- As **chaves delimitam os blocos**; o código após a decisão pode executar nos dois caminhos.
- Confira sempre **abaixo, igual e acima da meta**, explicando a mensagem escolhida.

Na próxima aula, vamos ampliar as decisões com `else if` e combinar condições em situações simples.

:::roteiro
0–6 min: retomar comparação < e casos 20/30/40. 6–17 min: if sem else e diferença entre não haver mensagem e haver erro. 17–29 min: acrescentar alternativa e testar igualdade e valor acima. 29–35 min: fluxo após o bloco e organização das chaves. 35–45 min: prática com três testes e mensagens personalizadas. 45–50 min: quiz e fechamento. Adaptação das condicionais do RCO 84 ao plano: apenas uma condição booleana produzida por comparação e duas alternativas. else if e operadores lógicos ficam para a aula 26. Dados numéricos controlados e meta positiva; não apresentar a decisão como validação de dados arbitrários. As advertências esclarecem limite e delimitação dos blocos. Não introduzir DOM, eventos, funções ou formulário.
:::
