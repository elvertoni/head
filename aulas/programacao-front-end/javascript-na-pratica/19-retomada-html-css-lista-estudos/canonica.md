---
titulo: Meus estudos — retomando HTML e CSS
tema: JavaScript na prática
disciplina: programacao-front-end
serie: 2ª
prerequisitos: [Usar o teclado e abrir pastas no computador]
objetivos:
  - Criar e abrir uma página HTML local no navegador
  - Identificar o conteúdo no HTML e a aparência no CSS
  - Alterar um texto e uma cor e conferir o resultado após salvar e atualizar
trilha: javascript-na-pratica
ordem: 19
slug: retomada-html-css-lista-estudos
modo_origem: seed
fontes: [docs/plano-apostila-javascript.md]
revisao: true
status: aprovada
versao: 2
atualizado_em: 2026-11-04
---

Você já anotou uma tarefa da escola em um papel e depois esqueceu onde colocou? Nesta sequência, você vai construir uma lista de tarefas de estudo. Hoje, o primeiro passo é pequeno: colocar um título, uma mensagem e duas tarefas em uma página e escolher uma cor para ela. Se você esqueceu como começa um arquivo HTML, vamos retomar juntos.

## Objetivos

- Criar o arquivo `index.html` e abrir sua página no navegador.
- Identificar o que pertence ao HTML e o que pertence ao CSS.
- Alterar um texto e uma cor, salvar e conferir as mudanças.

## Pré-requisitos

Você precisa conseguir digitar e abrir uma pasta. Vamos usar o **Visual Studio Code (VSCode)**, o programa em que você escreve o código, e um **navegador**, como Chrome, Edge ou Firefox, em que você vê a página. Se não encontrar o VSCode no computador da escola, chame o professor antes de começar.

## Desenvolvimento

### 1. Relembre o papel de cada parte

Pense no mural de avisos da sala. Ele tem título, recados e uma lista de atividades. Você pode manter esses mesmos recados e mudar a cor do papel ou a cor do título. O conteúdo continua o mesmo; a aparência muda.

:::conceito HTML e CSS
O **HTML** indica o conteúdo e a organização da página: qual trecho é título, qual é parágrafo e quais são os itens da lista. O **CSS** define a aparência: por exemplo, a cor do título e do fundo.
:::

Neste exemplo, `<h1>` abre o título principal e `</h1>` fecha esse título. O texto entre eles é o que você lê na página. Essas marcações são chamadas de **tags**.

```html
<h1>Meus estudos</h1>
```

Se você trocar apenas `Meus estudos` por `Minha semana`, muda o título que aparece. As tags continuam dizendo ao navegador que aquele texto é o título principal.

### 2. Prepare a pasta e escreva o HTML

No computador, crie uma pasta chamada **`meus-estudos`** em um lugar que consiga encontrar depois, como Documentos. Abra o VSCode e escolha **Arquivo → Abrir Pasta**. Selecione `meus-estudos`. Se aparecer um pedido de confiança, confirme somente se for a pasta que você acabou de criar.

No painel de arquivos do VSCode, clique em **Novo Arquivo** e digite **`index.html`**. O ponto faz parte do nome. A terminação `.html` informa que esse arquivo contém uma página HTML.

**Digite ou copie o código inteiro abaixo no arquivo vazio.** Depois, pressione **Ctrl + S** para salvar.

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>Meus estudos</title>
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

**Agora confira:** abra a pasta `meus-estudos` pelo Explorador de Arquivos do computador. Dê dois cliques em `index.html`. Se o computador pedir um programa, escolha o navegador. Você deve ver o título **Meus estudos**, a frase **Uma tarefa de cada vez.** e dois itens com marcadores. O fundo ainda é branco e a aparência é simples.

Você pode deixar o VSCode e o navegador abertos e alternar entre eles. Não precisa de internet, extensão nem servidor para abrir esta página.

Vamos localizar quatro partes no código que você acabou de usar:

| Parte | Para que serve aqui |
|---|---|
| `<head>...</head>` | Reúne informações sobre a página. O `<title>` dá nome à aba; `charset="UTF-8"` permite interpretar os caracteres do arquivo, incluindo acentos. |
| `<body>...</body>` | Contém o que aparece dentro da página. |
| `<h1>...</h1>` e `<p>...</p>` | Marcam o título principal e um parágrafo. |
| `<ul>...</ul>` e `<li>...</li>` | Marcam uma lista com marcadores e cada item dessa lista. |

O `<!DOCTYPE html>` indica o uso do HTML moderno. O `<html lang="pt-BR">` informa o idioma da página. Hoje, mantenha essas linhas como estão; concentre suas mudanças no título, na mensagem e nas tarefas.

:::atencao A página abriu como texto
**Sintoma:** o navegador mostra o código, incluindo `<h1>`, em vez de mostrar a página pronta.

**Solução:** confira o nome do arquivo. Ele precisa ser `index.html`, e não `index.html.txt`. No Explorador do Windows, ative a opção de mostrar extensões de nomes de arquivos para conferir. Se tiver aberto o próprio arquivo no VSCode, ver o código é esperado; abra também a versão no navegador.
:::

### 3. Coloque uma pequena regra de CSS

Volte ao VSCode. Localize a linha `</head>`. **Insira o bloco abaixo imediatamente antes dela**, sem apagar o restante do arquivo.

```html
<style>
  body {
    background-color: aliceblue;
  }

  h1 {
    color: darkblue;
  }
</style>
```

Tudo que está entre `<style>` e `</style>` é CSS. O `body` escolhe o corpo da página; `background-color: aliceblue;` deixa seu fundo azul bem claro. O `h1` escolhe o título principal; `color: darkblue;` deixa o texto desse título azul-escuro.

Observe o padrão: você escolhe **onde** aplicar a mudança e escreve, entre `{` e `}`, **o que** mudar. O `:` separa a propriedade do valor, e o `;` encerra a declaração. Copie esses sinais com atenção.

**Salve com Ctrl + S.** Volte ao navegador e atualize a página com **Ctrl + R** ou pelo botão de recarregar. Você deve ver o fundo azul bem claro e o título azul-escuro. Os textos e os dois itens continuam os mesmos.

:::dica Como conferir uma alteração no trabalho de front-end
Quem desenvolve páginas alterna entre o editor e o navegador para conferir o resultado. Use esta rotina desde agora: **alterar → salvar → atualizar → observar**. Faça uma mudança de cada vez. Assim fica mais fácil descobrir qual alteração causou um problema.
:::

### 4. Mude uma coisa e observe

No HTML, localize o texto `Uma tarefa de cada vez.` dentro de `<p>`. Troque somente esse texto por `Hoje vou organizar meus estudos.`. Mantenha `<p>` e `</p>`. Salve, atualize e confira se a frase mudou na página.

Depois, no CSS, troque somente `darkblue` por `darkgreen`. Salve, atualize e confira: o título deve ficar verde-escuro. A frase continua sendo a que você escreveu, e o fundo continua azul bem claro.

:::atencao Salvei, mas nada mudou
**Sintoma:** a página continua com a frase ou a cor anterior.

**Solução:** confirme que salvou o arquivo no VSCode e atualizou o navegador. Se continuar igual, confira se o navegador abriu o `index.html` da mesma pasta que está aberta no VSCode. Duas cópias com o mesmo nome podem confundir. Se só a cor falhar, compare a regra com `color: darkgreen;` e confira se ela está dentro das chaves de `h1`.
:::

## Prática

### Sua versão da página

Use **o mesmo `index.html`**. Você tem cerca de 10 minutos para transformar a página na sua lista de estudos. Faça uma mudança por vez e use a rotina de conferência.

1. Troque o texto dentro de `<h1>` por `Estudos de` seguido do seu primeiro nome.
2. Troque o texto de cada `<li>` por uma tarefa real da sua semana. Mantenha os dois itens e as tags.
3. No CSS, escolha `darkgreen` ou `darkred` para a cor do título.
4. Salve, atualize e mostre para uma dupla onde você mudou o conteúdo e onde mudou a aparência.

O exemplo abaixo mostra **apenas o trecho da lista**, caso precise lembrar como escrever. Substitua os dois itens existentes; não cole outra lista inteira no fim do arquivo.

```html
<ul>
  <li>Terminar a atividade de matemática</li>
  <li>Revisar as tags de HTML</li>
</ul>
```

### Confira antes de entregar

A página deve mostrar seu nome no título principal, duas tarefas da sua semana e o título na cor escolhida. O arquivo precisa continuar se chamando `index.html`, dentro de `meus-estudos`. Mostre a página no navegador e o código no VSCode para o professor. Guarde a pasta: vamos usá-la na próxima aula.

## Avaliação

Responda depois de testar sua página. Se errar, volte ao trecho indicado pela situação e faça a mudança no seu arquivo para conferir.

```quiz
- pergunta: Você quer trocar a tarefa que aparece no primeiro item da página. Onde deve mexer?
  alternativas:
    - texto: Na propriedade color do CSS
    - texto: No texto entre as tags do primeiro li
      correta: true
    - texto: No nome da pasta
  feedback: >
    O texto entre as tags do primeiro li é o conteúdo dessa tarefa. A propriedade color altera a cor, e renomear a pasta não reescreve a tarefa.
- pergunta: O título já mostra seu nome. Você quer deixar só o texto desse título verde-escuro. O que deve alterar?
  alternativas:
    - texto: A propriedade background-color de body
    - texto: O texto entre as tags de title
    - texto: O valor da propriedade color na regra de h1
      correta: true
  feedback: >
    A regra h1 seleciona o título principal e color altera a cor do texto. background-color em body muda o fundo; title dá nome à aba.
- pergunta: Você alterou a frase no VSCode, mas o navegador ainda mostra a versão anterior. Qual é a primeira conferência?
  alternativas:
    - texto: Salvar o arquivo e atualizar a página que abriu desse arquivo
      correta: true
    - texto: Apagar as tags de body
    - texto: Criar outra pasta e recomeçar tudo
  feedback: >
    O navegador não acompanha automaticamente o que você digita no editor. Primeiro salve e atualize; apagar tags ou recomeçar não resolve essa rotina de conferência.
```

## Fechamento

- **HTML organiza o conteúdo:** título, mensagem e itens da lista.
- **CSS muda a aparência:** hoje você alterou a cor do título e do fundo.
- **Alterar → salvar → atualizar → observar** permite conferir cada mudança.
- **Sua entrega:** um `index.html` que abre no navegador com sua lista de estudos.

Na próxima aula, vamos conectar um arquivo JavaScript a essa mesma página e usar o console para conferir uma primeira mensagem.

:::roteiro
0–5 min: pergunte o que é conteúdo e o que é aparência em um mural da sala. 5–10 min: ajude a abrir o VSCode e a criar a pasta e o arquivo. 10–20 min: construção guiada do HTML e primeira abertura no navegador. 20–30 min: inserção do CSS, duas alterações guiadas e rotina de conferência. 30–40 min: prática individual com apoio em duplas; observe se cada aluno localiza o texto e a regra CSS. 40–47 min: quiz e diagnóstico coletivo, retomando a página quando houver dúvida. 47–50 min: confira a entrega e a pasta salva. Esta é uma retomada preparatória aprovada no plano, complementando a base necessária antes da introdução ao JavaScript do RCO 78; a contagem regressiva da fonte foi adiada. Se a digitação for lenta, disponibilize o primeiro bloco HTML para copiar e preserve o tempo para o aluno alterar, testar e explicar. Não avance para eventos ou funções nesta aula.
:::
