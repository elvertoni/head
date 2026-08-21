---
titulo: "Cor e tipografia: a marca em seis linhas de CSS"
tema: Variáveis CSS, paleta e escala tipográfica
disciplina: programacao-front-end
serie: 2ª
prerequisitos: [Landing page estruturada e publicada na Aula 10]
objetivos:
  - Ligar uma folha de estilo externa a uma página HTML
  - Definir uma paleta de quatro cores atribuindo um papel a cada uma
  - Aplicar uma escala tipográfica em vez de escolher tamanhos avulsos
  - Centralizar cor e tipografia em variáveis CSS declaradas em :root
  - Reconhecer contraste insuficiente e prever a falha de carregamento de fonte externa
trilha: landing-page-mvp
ordem: 11
slug: cor-e-tipografia
modo_origem: tema
fontes: []
revisao: false
status: aprovada
versao: 2
atualizado_em: 2026-08-21
---

Sua página está no ar desde a aula passada, e ela está horrível. Tudo Times New Roman, tudo preto no branco, links azuis sublinhados, texto atravessando a tela de ponta a ponta. Não é falta de talento: é o navegador aplicando os padrões dele porque você ainda não disse nada. E aqui vem a parte que surpreende — a distância entre isso e algo que **parece um produto de verdade** não é um mês de CSS. São umas quinze linhas, e a maior parte delas você escreve uma vez só, num lugar só. Hoje é a aula em que o projeto muda de categoria.

## Objetivos

Ao final desta aula, você será capaz de:

- Ligar um arquivo `.css` externo à sua página.
- Escolher **quatro cores** e dar a cada uma um **cargo** — fundo, texto, destaque e apoio.
- Usar uma **escala tipográfica** em vez de chutar tamanhos.
- Guardar tudo isso em **variáveis** dentro de `:root`, e entender por que isso é diferente de escrever a cor direto.
- Identificar **contraste ruim** e proteger a página contra a fonte que não carrega.

## Pré-requisitos

A página da aula 10, estruturada e publicada. Se a sua ficou pelo caminho, termine a estrutura primeiro — CSS aplicado sobre HTML bagunçado só deixa a bagunça colorida.

## Desenvolvimento

### Quatro cores, e cada uma com um cargo

O erro de quem começa não é escolher cor feia. É escolher **cor demais**. A página ganha um azul aqui, um verde ali, um roxo no botão porque ficou bonitinho — e o resultado parece festa de aniversário, não produto.

A saída é parar de pensar "que cores eu gosto" e passar a pensar **cargo**: cada cor tem uma função, e nada entra sem função.

![Duas versões da mesma página lado a lado. Na da esquerda, a cor de destaque aparece no título, nas bordas, nos ícones, nos links e no botão, e nenhum elemento sobressai — o olho não encontra ponto de entrada. Na da direita, a mesma página usa a cor de destaque em um único elemento, o botão, com todo o resto em texto escuro e cinza de apoio, e o botão salta imediatamente.](img/destaque-so-destaca-se-for-raro.png)

| Cargo | Para que serve | Quanto aparece |
|---|---|---|
| **Fundo** | O papel da página | Quase tudo |
| **Texto** | A tinta que se lê | Todo o conteúdo |
| **Destaque** | O botão e os pontos que devem atrair o olho | **Pouquíssimo** |
| **Apoio** | Bordas, linhas, texto secundário | Discreto |

A regra que faz mais diferença é a da linha do destaque: **destaque só destaca se for raro**. Se o botão é laranja e o título é laranja e as bordas são laranja, nada é laranja — o olho não tem para onde ir. Numa landing page com uma ação só, a cor de destaque idealmente aparece **num lugar**: o botão.

### A escala: por que 16, 20, 24 e 40

Mesmo problema, outra dimensão. Quem escolhe tamanho de letra na base do "acho que esse tá bom" acaba com sete tamanhos que quase não se distinguem: 15, 16, 17, 19, 22, 23, 40. O resultado é uma página que parece desalinhada sem que se saiba dizer por quê — os tamanhos são diferentes demais para parecerem iguais e parecidos demais para parecerem intencionais.

:::conceito Escala tipográfica
**Escala tipográfica** é um conjunto pequeno e fixo de tamanhos, com saltos claros entre eles, usado na página inteira. Cinco degraus bastam. A regra é simples: se dois textos têm importância diferente, os tamanhos precisam ser **visivelmente** diferentes; se têm a mesma importância, precisam ser **exatamente** iguais.
:::

Uma escala que funciona para qualquer landing:

| Uso | Tamanho |
|---|---|
| Texto pequeno (rodapé, legenda) | 14px |
| Texto normal (parágrafos) | 16px |
| Subtítulo / subheadline | 20px |
| Título de seção (`h2`) | 28px |
| Headline (`h1`) | 44px |

:::curiosidade O 16 não foi escolhido por você
16px é o tamanho padrão que todo navegador aplica quando ninguém manda nada — resultado de décadas de teste de legibilidade em tela. Ele parece grande na hora de escrever e é exatamente o certo na hora de ler. E existe um motivo forte para nunca fixar texto de leitura abaixo disso: a pessoa que aumentou a fonte do celular fez isso porque **precisa**, e página que ignora essa escolha simplesmente não é lida por ela.
:::

### `:root`: o lugar único onde a marca mora

Você poderia escrever `color: #1a4fa0` toda vez que precisar da cor da marca. Funciona — até o dia em que a cor muda.

```diagrama-progressivo
titulo: A cor escrita à mão, e a conta que ela cobra
camadas:
  - rotulo: Segunda-feira, tudo certo
    conteudo: "Você escolhe o azul da marca e escreve o código dele direto em cada lugar que precisa — no botão, no título, na borda, no link, no rodapé. Quatorze vezes, espalhadas pelo arquivo. Funciona perfeitamente e é rápido de fazer."
  - rotulo: Quinta-feira, o trio muda de ideia
    conteudo: "O grupo decide que o azul ficou apagado e quer trocar por um verde. Agora existem quatorze lugares para achar, e eles não estão juntos — estão espalhados entre regras que você escreveu em dias diferentes."
  - rotulo: A tentativa óbvia, e a armadilha dela
    conteudo: "Você usa substituir tudo. Só que dois daqueles quatorze não eram a cor da marca — era a borda cinza-azulada de uma caixa, que por acaso tinha um código parecido, e uma sombra. Eles viram verde também. O erro fica na página publicada e ninguém percebe na hora."
  - rotulo: A versão com variável
    conteudo: "Se a cor tivesse sido declarada uma vez em root e usada por apelido nos quatorze lugares, a troca seria uma linha — e só os quatorze certos mudariam, porque só eles pediam aquele apelido. Mudar uma vez é o barato; mudar sem quebrar o que não era para mudar é o valioso."
```

:::conceito Variável CSS (custom property)
Uma **variável CSS** é um apelido que você cria para um valor e reutiliza no arquivo inteiro. Declara-se em `:root` — que representa a página toda — com dois hífens na frente do nome, e usa-se com `var()`. Trocar o valor em `:root` muda **todos** os lugares que pedem aquele apelido, e só eles.
:::

```css
:root {
  --cor-fundo: #ffffff;
  --cor-texto: #1f2933;
  --cor-destaque: #2f6f4e;
  --cor-apoio: #d9dee3;

  --fonte-titulo: "Poppins", "Segoe UI", sans-serif;
  --fonte-texto: "Inter", "Segoe UI", sans-serif;
}
```

Repare que a fonte também é variável, e que cada uma traz **três** nomes. Isso não é indecisão:

:::atencao A fonte que não chega — e a página que "quebrou sozinha"
Fontes do Google Fonts são baixadas da internet **no momento em que a página abre**. Na escola, com o wi-fi lotado no início da aula, esse download falha o tempo todo. Aí acontece o clássico: sua página, que estava linda ontem, abre hoje toda em Times New Roman e você jura que quebrou alguma coisa — e o CSS está intacto. Por isso `font-family` leva uma **lista**: o navegador tenta a primeira, e se não conseguir cai para a próxima. Terminar sempre com `sans-serif` garante que o pior caso continue sendo uma fonte sem serifa decente, e não o Times. Diagnóstico: se a página inteira mudou de cara de uma vez, sem você ter mexido, é a fonte que não carregou — recarregue e observe.
:::

:::importante Contraste não é preferência, é se dá para ler
Cinza-claro sobre branco fica elegante no monitor da sala, com a cortina fechada. No celular, no ônibus, com sol na tela, some. A regra prática: **texto de leitura precisa ser escuro sobre fundo claro, ou claro sobre fundo escuro — sem meio-termo.** Cinza médio serve para texto secundário, nunca para o parágrafo principal, e nunca para o texto dentro do botão. Existe medida oficial para isso, e o teste rápido que aproxima bem: olhe a tela do celular com o brilho no mínimo. O que sumir, sumiu.
:::

## Prática

**Vestir a página (~15 min).** Crie `estilo.css` na mesma pasta do `index.html` e ligue os dois. A tag vai dentro do `<head>`, junto com a chamada das fontes:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&family=Poppins:wght@600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="estilo.css">
```

Agora o `estilo.css`. Escreva primeiro o `:root` com **as cores do seu produto** — não copie as do exemplo:

```css
:root {
  --cor-fundo: #ffffff;
  --cor-texto: #1f2933;
  --cor-destaque: #2f6f4e;
  --cor-apoio: #d9dee3;

  --fonte-titulo: "Poppins", "Segoe UI", sans-serif;
  --fonte-texto: "Inter", "Segoe UI", sans-serif;
}

body {
  background-color: var(--cor-fundo);
  color: var(--cor-texto);
  font-family: var(--fonte-texto);
  font-size: 16px;
  line-height: 1.6;
  margin: 0;
}

h1, h2, h3 {
  font-family: var(--fonte-titulo);
  line-height: 1.2;
}

h1 { font-size: 44px; }
h2 { font-size: 28px; }
h3 { font-size: 20px; }

main {
  max-width: 800px;
  margin: 0 auto;
  padding: 0 24px;
}

footer {
  border-top: 1px solid var(--cor-apoio);
  font-size: 14px;
}
```

Duas linhas aí fazem mais pela aparência do que qualquer cor: `line-height: 1.6`, que afasta as linhas do parágrafo e é a diferença entre "texto" e "parede de texto"; e `max-width: 800px` com `margin: 0 auto`, que impede a frase de atravessar a tela inteira e centraliza o conteúdo. Linha longa demais cansa porque o olho se perde ao voltar para a esquerda.

**Desafio final (2 min).** Troque **só** o valor de `--cor-destaque` em `:root` e recarregue. A marca inteira muda de uma vez. Foi por isso que fizemos assim.

**Entrega:** página publicada de novo (mesmo link), com paleta de quatro cores e escala aplicada. Envie e confira **no celular**, não só no monitor.

## Avaliação

```quiz
- pergunta: Por que declarar a cor da marca em :root e usar var() é melhor que escrever o código da cor em cada lugar?
  alternativas:
    - texto: Porque variáveis fazem a página carregar mais rápido
    - texto: "Porque a troca passa a ser feita em um lugar só, e atinge exatamente os lugares que pediram aquela variável — nem mais, nem menos"
      correta: true
    - texto: Porque o CSS não aceita códigos de cor escritos diretamente nas regras
    - texto: Porque assim as cores ficam protegidas contra alteração
  feedback: >
    O ganho não é de desempenho nem de segurança. É de precisão na hora de mudar:
    substituir texto no arquivo inteiro atinge também o que só era parecido, e
    esse tipo de erro passa despercebido por semanas.
- pergunta: Por que font-family leva vários nomes separados por vírgula, terminando em sans-serif?
  alternativas:
    - texto: Para o navegador misturar as fontes e criar uma aparência própria
    - texto: "Porque é uma lista de alternativas — se a primeira não carregar, o navegador usa a seguinte, e a última garante um resultado aceitável"
      correta: true
    - texto: Porque cada navegador exige uma fonte diferente
    - texto: Porque a primeira fonte é usada nos títulos e a segunda nos parágrafos
  feedback: >
    Fonte externa depende de download, e download falha — especialmente no wi-fi
    da escola. A lista é o plano B: sem ela, o navegador cai no padrão dele e a
    página inteira aparece em Times New Roman.
- pergunta: Qual destas escolhas de contraste está adequada para o parágrafo principal?
  alternativas:
    - texto: Cinza-claro sobre fundo branco, porque fica mais elegante
    - texto: "Texto escuro sobre fundo claro, deixando o cinza médio só para informação secundária"
      correta: true
    - texto: Texto na cor de destaque, para reforçar a identidade da marca
    - texto: Cinza-claro sobre cinza-médio, para um visual mais suave
  feedback: >
    Contraste não é gosto: é a diferença entre ler e não ler no celular com sol na
    tela. Cinza-claro sobre branco some, e a cor de destaque no texto todo mata o
    destaque — se tudo é destaque, o botão deixa de chamar atenção.
```

## Fechamento

O que ficou de hoje:

- **Quatro cores, cada uma com um cargo.** Destaque só destaca se for raro — de preferência, só no botão.
- **Cinco tamanhos de letra, e só eles.** Importância diferente pede tamanho visivelmente diferente; importância igual pede tamanho idêntico.
- **`:root` é onde a marca mora.** Uma linha muda a página inteira, sem atingir o que não devia.
- **`font-family` é uma lista**, porque fonte da internet falha — e sem plano B a página vira Times New Roman.
- **Contraste é legibilidade**, não estética. O teste é o celular no sol.

**Próxima aula:** o conteúdo já está bonito, mas continua tudo empilhado numa coluna só — o menu embaixo do nome, o botão embaixo do texto. Falta **alinhar**. Vamos ao Flexbox, que é como se põe coisa lado a lado sem gambiarra, e resolver de uma vez o topo e o hero.

:::roteiro
Abra a aula com um "antes e depois" no projetor: a mesma página sem CSS e com as quinze linhas. O impacto visual é o que compra a atenção para uma aula que, no fundo, é sobre disciplina.

Deixe claro logo cedo que hoje ninguém escolhe cor por gosto — escolhe por cargo. Se a turma cair no "qual cor é mais bonita", devolva sempre a mesma pergunta: "qual é o cargo dessa cor?".

O diagrama da cor à mão funciona melhor se você fizer o substituir-tudo ao vivo e quebrar de propósito uma borda que tinha código parecido. Ver a página estragar sozinha vale mais que a explicação.

A fonte que não carrega vai acontecer de verdade na sala — o wi-fi trabalha a seu favor aqui. Quando o primeiro aluno chamar dizendo que quebrou tudo, mostre para a turma inteira: é o momento em que o fallback deixa de ser detalhe chato.

No fim, faça a turma trocar --cor-destaque toda junta e recarregar ao mesmo tempo. Trinta alunos vendo a própria marca mudar numa linha é o que fixa o conceito de variável melhor que qualquer definição.

Cobre o teste no celular antes de liberar. Sempre tem paleta que só funciona no monitor da sala.
:::
