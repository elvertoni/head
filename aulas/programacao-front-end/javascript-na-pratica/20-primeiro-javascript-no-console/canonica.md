---
titulo: Primeiro JavaScript — uma mensagem no console
tema: JavaScript na prática
disciplina: programacao-front-end
serie: 2ª
prerequisitos: [Criar e abrir um arquivo HTML, Salvar e atualizar a página]
objetivos:
  - Conectar um arquivo JavaScript externo à página HTML
  - Exibir e alterar mensagens com console.log
  - Conferir a execução no console e localizar erros de nome de arquivo ou de escrita do comando
trilha: javascript-na-pratica
ordem: 20
slug: primeiro-javascript-no-console
modo_origem: seed
fontes: [docs/plano-apostila-javascript.md]
revisao: true
status: aprovada
versao: 2
atualizado_em: 2026-11-04
---

Sua página “Meus estudos” já mostra um título e uma lista. Hoje você vai fazer o navegador executar uma primeira instrução em JavaScript. Para conferir se funcionou, vamos usar um espaço de mensagens chamado console. É como testar o microfone antes de uma apresentação: primeiro você confirma que a mensagem chegou; depois fica mais fácil construir o restante.

## Objetivos

- Conectar `script.js` ao `index.html` da sua página.
- Mostrar uma mensagem com `console.log` e trocar seu texto.
- Abrir o console, conferir o resultado e verificar nomes de arquivos e sinais do comando quando algo falhar.

## Pré-requisitos

Você vai usar o **VSCode para escrever e salvar** e o **navegador para abrir a página e conferir**. Retome a pasta `meus-estudos` da aula 19. Não precisa instalar um programa novo, usar o terminal nem ter internet para fazer esta atividade.

## Desenvolvimento

### 1. Retome sua página e a rotina de conferência

Abra o VSCode e escolha **Arquivo → Abrir Pasta → meus-estudos**. Abra o arquivo `index.html`. Pelo Explorador de Arquivos do computador, abra esse mesmo `index.html` no navegador. Confira se sua página de estudos aparece.

Na aula anterior, você mudou o conteúdo com HTML e as cores com CSS. **HTML organiza, CSS dá aparência e JavaScript permite programar ações.** Por exemplo, em outras etapas da sequência você vai programar o que acontece ao adicionar uma tarefa. Hoje, a ação será somente escrever uma mensagem no console.

Para relembrar a rotina, troque um texto de tarefa dentro de um `<li>`, salve com **Ctrl + S** e atualize o navegador com **Ctrl + R**. Confira a mudança antes de seguir.

Se você está sem o arquivo da aula anterior, crie a pasta `meus-estudos`, abra essa pasta no VSCode e crie `index.html`. Copie o código abaixo **somente se estiver começando com um arquivo vazio**. Se já tem sua página, continue usando a sua.

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>Meus estudos</title>
  <style>
    body {
      background-color: aliceblue;
    }
    h1 {
      color: darkgreen;
    }
  </style>
</head>
<body>
  <h1>Meus estudos</h1>
  <p>Uma tarefa de cada vez.</p>
  <ul>
    <li>Revisar HTML</li>
    <li>Praticar CSS</li>
  </ul>
</body>
</html>
```

### 2. Crie o arquivo JavaScript

No painel de arquivos do VSCode, crie **um novo arquivo dentro de `meus-estudos`**, ao lado de `index.html`. Dê o nome **`script.js`**. A terminação `.js` identifica um arquivo JavaScript.

Sua pasta deve ficar assim. Os dois arquivos estão no mesmo nível, sem uma pasta entre eles:

```txt
meus-estudos/
  index.html
  script.js
```

Dentro do arquivo **`script.js`**, digite ou copie esta linha. Salve com **Ctrl + S**.

```javascript
console.log("Meu JavaScript está funcionando!");
```

:::conceito Uma instrução, uma mensagem
`console.log` é um comando usado para mostrar informações no console do navegador. Os parênteses contêm o que você quer mostrar. Neste exemplo, o texto fica entre aspas duplas, e o `;` encerra a instrução. Mantenha os sinais como no modelo e mude apenas o texto quando for solicitado.
:::

Observe que `console` e `log` estão em letras minúsculas e são separados por um ponto. As aspas marcam o começo e o fim da mensagem; elas não aparecem como parte do texto exibido. Escreva o comando no VSCode, dentro de `script.js`.

Por enquanto, você apenas criou e salvou o arquivo. O próximo passo é informar ao HTML que ele deve carregar esse JavaScript.

### 3. Conecte os dois arquivos

Volte à aba **`index.html` no VSCode**. Encontre `</body>`, perto do fim do arquivo. Insira **somente a linha abaixo imediatamente antes de `</body>`**, mantendo as outras linhas:

```html
<script src="script.js"></script>
```

O `src="script.js"` informa o nome do arquivo que o navegador deve carregar. Como o HTML e o JavaScript estão na mesma pasta, basta esse nome. A tag de fechamento `</script>` também precisa estar presente.

O final do seu HTML ficará assim. Este é um **trecho para comparar**, não uma segunda lista para colar no fim do arquivo. Os textos das tarefas podem continuar personalizados:

```html
  <ul>
    <li>Revisar HTML</li>
    <li>Praticar CSS</li>
  </ul>
  <script src="script.js"></script>
</body>
</html>
```

Salve o **`index.html`**. Confira também se salvou o **`script.js`**. Volte ao navegador e atualize a página.

**O título e a lista continuam com a mesma aparência.** A mensagem de `console.log` vai para o console, não para o conteúdo visível da página. Vamos abrir esse espaço agora.

### 4. Abra o console e confira a mensagem

Com a sua página aberta no navegador, pressione **F12**. Em alguns notebooks é necessário **Fn + F12**. Nas ferramentas que abrirem, clique na aba **Console**. Ela também pode aparecer com esse nome em um menu de abas ocultas.

Se preferir usar o menu do navegador, no Chrome ou Edge procure **Mais ferramentas → Ferramentas do desenvolvedor** e depois **Console**. No Firefox, procure **Mais ferramentas → Ferramentas de desenvolvimento web** e a aba **Console**. Os nomes podem variar um pouco conforme o idioma.

Com o console aberto, atualize a página novamente. Você deve encontrar esta mensagem; o navegador também pode mostrar o nome do arquivo e o número da linha ao lado:

```txt
Meu JavaScript está funcionando!
```

Você não precisa digitar nada no console. Ele será usado para **ler o resultado**. O código desta aula é escrito e salvo em `script.js`, no VSCode.

Agora volte ao **`script.js`**, troque apenas o texto entre aspas por `Hoje vou estudar JavaScript.` e salve. Atualize a página com o console aberto. A nova mensagem deve aparecer. Se mensagens antigas permanecerem, procure a mais recente; cada atualização executa o arquivo novamente.

:::atencao Não apareceu a mensagem
**Sintoma:** a página abre, mas você não encontra a mensagem no console.

**Solução:** confira se os dois arquivos foram salvos e se você atualizou o `index.html` correto. Compare o nome do arquivo `script.js` com o nome em `src="script.js"`: precisam ser iguais, inclusive nas letras maiúsculas e minúsculas. Confira se estão na mesma pasta e se o arquivo não se chama `script.js.txt`. Verifique também se o console está sem filtro de texto e permite mostrar mensagens de informação. Se continuar sem a mensagem, peça ajuda ao professor para ler o erro que aparecer.
:::

:::atencao Apareceu um erro ao executar
**Sintoma:** o console aponta um erro relacionado a `script.js`, às vezes em vermelho, em vez de mostrar a mensagem esperada.

**Solução:** volte ao VSCode e compare a linha com `console.log("Meu JavaScript está funcionando!");`. Confira letras minúsculas, ponto, parênteses e as duas aspas retas. Uma aspa que ficou aberta pode impedir a execução. Corrija, salve e atualize. Use o nome do arquivo e a linha indicados no console para localizar o problema; eles são pistas, não uma nota sobre sua capacidade.
:::

:::dica Uma ferramenta de trabalho de quem desenvolve
O console ajuda quem desenvolve a verificar se uma parte do código foi executada e a encontrar erros. Comece conferindo mensagens pequenas. Você vai continuar usando a mesma rotina da aula 19: **alterar → salvar → atualizar → observar**. Hoje, a observação acontece na aba Console.
:::

## Prática

### Duas mensagens sobre seus estudos

No **`script.js`**, substitua a linha anterior pelas duas linhas abaixo. Troque `Ana` pelo seu primeiro nome e escreva uma tarefa real na segunda mensagem. Mude somente os textos entre aspas.

```javascript
console.log("Estudante: Ana");
console.log("Minha tarefa de hoje é revisar HTML.");
```

1. Salve o `script.js` e atualize sua página com o console aberto.
2. Confira se as duas mensagens aparecem na mesma ordem das linhas do arquivo.
3. Troque somente a tarefa da segunda linha por outra tarefa. Antes de atualizar, diga à sua dupla qual mensagem vai mudar.
4. Salve, atualize e compare o resultado com sua previsão. Mostre para a dupla a linha do HTML que conecta o JavaScript.

### Confira antes de entregar

Sua pasta deve conter `index.html` e `script.js` no mesmo nível. A página deve continuar mostrando a lista de estudos; no console, as duas mensagens devem mostrar seu nome e sua tarefa. Mostre os dois arquivos no VSCode e o resultado no navegador para o professor. Guarde a pasta para a aula 21.

Se você precisar de uma referência para comparar o resultado do exemplo, as mensagens serão estas. O seu nome e a sua tarefa podem ser diferentes:

```txt
Estudante: Ana
Minha tarefa de hoje é revisar HTML.
```

## Avaliação

Responda pensando no que você acabou de executar. Quando ficar em dúvida, volte ao arquivo e confira em vez de tentar decorar o comando inteiro.

```quiz
- pergunta: O index.html e o script.js estão na mesma pasta. Qual linha, inserida antes do fechamento de body, conecta os arquivos?
  alternativas:
    - texto: '<style src="script.js"></style>'
    - texto: '<script src="script.js"></script>'
      correta: true
    - texto: '<script src="index.html"></script>'
  feedback: >
    A tag script com src apontando para script.js carrega o arquivo JavaScript. style é usado para CSS, e apontar para index.html não seleciona o arquivo JavaScript.
- pergunta: Você salvou console.log("Olá, turma!"); em script.js e atualizou a página que carrega esse arquivo. Onde deve procurar a mensagem?
  alternativas:
    - texto: No título principal da página
    - texto: No nome da aba do navegador
    - texto: No console das ferramentas do desenvolvedor
      correta: true
  feedback: >
    console.log mostra a mensagem no console. Esse comando não muda o título principal nem o nome da aba. A aparência da página pode continuar igual mesmo com o JavaScript funcionando.
- pergunta: O arquivo está salvo como script.js, mas o HTML aponta para scripts.js. Qual correção você deve fazer?
  alternativas:
    - texto: Trocar no HTML o nome scripts.js por script.js, salvar e atualizar a página
      correta: true
    - texto: Mudar a cor do título no CSS
    - texto: Digitar uma mensagem no console e deixar o nome errado no HTML
  feedback: >
    O nome indicado em src precisa corresponder ao arquivo existente. Mudar a cor não corrige o caminho, e digitar no console não conserta a conexão entre os arquivos salvos.
```

## Fechamento

- O **`index.html`** carrega o JavaScript pela tag `<script src="script.js"></script>`.
- O **`script.js`** guarda as instruções que você escreveu em JavaScript.
- **`console.log`** mostra uma mensagem no console; a página pode continuar com a mesma aparência.
- **Alterar → salvar → atualizar → observar** continua sendo sua rotina de conferência.

Na próxima aula, vamos guardar informações com nomes usando `let` e `const`. Você vai reutilizar os mesmos arquivos e o console para conferir os valores.

:::roteiro
0–7 min: retome pasta, HTML/CSS e rotina de salvar e atualizar; a recuperação do HTML é alternativa para quem perdeu o arquivo, não uma segunda tarefa para toda a turma. 7–15 min: criar script.js e escrever uma única mensagem. 15–23 min: conectar pela tag script antes de body; pedir que apontem o nome do arquivo nas duas telas. 23–32 min: abrir o console e trocar a mensagem, explicitando por que a página não muda. 32–42 min: prática em duplas com previsão da alteração. 42–48 min: quiz e diagnóstico de src com um nome incorreto. 48–50 min: conferir pasta e guardar os arquivos. Adaptação da introdução do RCO 78 ao plano aprovado: a prática de contagem regressiva foi adiada porque pressupõe variáveis, condicionais e funções; esta aula verifica a conexão e a execução antes desses assuntos. Não introduzir variáveis, DOM ou eventos. Mensagem no console é a evidência principal; não exigir terminal nem Node.js dos alunos.
:::
