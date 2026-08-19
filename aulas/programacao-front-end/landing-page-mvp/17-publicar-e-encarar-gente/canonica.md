---
titulo: "Publicar de verdade e encarar gente"
tema: Checklist de publicação e teste com usuários
disciplina: programacao-front-end
serie: 2ª
prerequisitos: [Landing page completa e publicada até a Aula 16, Briefing com a hipótese da Aula 08]
objetivos:
  - Auditar a página com uma lista de verificação de publicação
  - Escrever um README que apresenta o projeto e o link
  - Conduzir um teste de cinco segundos sem contaminar o resultado
  - Registrar as respostas separando o que foi entendido do que foi opinado
  - Reconhecer que o teste avalia a página, e não quem a fez
trilha: landing-page-mvp
ordem: 17
slug: publicar-e-encarar-gente
modo_origem: tema
fontes: []
revisao: false
status: aprovada
versao: 1
atualizado_em: 2026-08-18
---

Hoje ninguém constrói nada. Hoje a página sai da sala pela primeira vez e vai para a mão de gente que não sabe do que se trata, não conhece vocês e não tem paciência nenhuma. Vocês vão entregar o celular para cinco pessoas, dar dez segundos, tirar da frente delas e fazer duas perguntas. E vai doer um pouco — porque quem passou sete aulas dentro do projeto perdeu, sem perceber, a capacidade de olhar para ele com olhos de estranho. É exatamente essa capacidade que a gente aluga de cinco pessoas hoje. Antes disso, meia hora tirando os defeitos que só aparecem depois de publicado.

## Objetivos

Ao final desta aula, você será capaz de:

- Auditar sua página com uma **lista de verificação** de publicação.
- Escrever um **README** que apresenta o projeto e leva ao link.
- Conduzir um **teste de cinco segundos** sem estragar o próprio resultado.
- Registrar as respostas separando **o que foi entendido** do que foi opinado.
- Encarar um resultado ruim como informação, e não como julgamento pessoal.

## Pré-requisitos

A página completa e publicada, e o briefing da aula 08 com a hipótese e o número. Traga celular carregado — hoje ele é o instrumento do teste.

## Desenvolvimento

### O que só quebra depois de publicado

Tem uma categoria de defeito invisível para quem está construindo, porque ela não afeta o que você olha o dia inteiro. São todos pequenos e todos denunciam amadorismo antes de a primeira palavra ser lida:

| Defeito | Onde aparece | Custo |
|---|---|---|
| `<title>` ainda escrito como "Document" | Aba do navegador, link compartilhado | A aba não se identifica; no WhatsApp, o link chega sem nome |
| Imagem sem `alt` | Leitor de tela, e quando a imagem não carrega | Conteúdo some para quem não vê a tela |
| Contraste fraco | Celular sob sol | Texto simplesmente ilegível |
| Link interno apontando para seção inexistente | Ao clicar | Nada acontece, e parece defeito de sistema |
| Última versão não publicada | No teste | Você avalia a página da semana passada |

:::atencao Você testou a versão antiga
O roteiro é sempre o mesmo: o aluno corrige a página, salva, envia para o repositório e abre no celular — e vê a versão de antes. Conclui que a correção não funcionou e sai mexendo em código que estava certo. São duas causas somadas: a publicação leva de um a dois minutos para propagar, e o celular guarda a versão anterior em cache para economizar dados. Diagnóstico em vinte segundos: abra o link numa **aba anônima**, ou acrescente `?v=2` no fim do endereço — se a correção aparece assim, o seu código está certo e o que você estava vendo era cache. Faça essa checagem **antes** de qualquer investigação; ela evita a maior parte do desespero de véspera de entrega.
:::

### A lista de verificação

Lista de verificação não é burocracia escolar — é como se entrega software em qualquer lugar sério, justamente porque memória falha sob pressão e o item esquecido é sempre o óbvio.

```
ANTES DE MOSTRAR PARA ALGUÉM

[ ] <title> com o nome do produto e o que ele resolve
[ ] lang="pt-BR" na tag <html>
[ ] toda imagem com alt descritivo
[ ] nenhum texto de exemplo sobrando (SUA HEADLINE AQUI, Lorem ipsum, Benefício 1)
[ ] todos os links internos levam a alguma seção existente
[ ] a página não desliza para os lados no celular
[ ] dá para ler tudo sem aproximar com os dedos
[ ] o botão é visível sem passar o mouse
[ ] aperta Tab cinco vezes e dá para ver onde está o foco
[ ] README no repositório com uma descrição e o link
[ ] última versão publicada e conferida em aba anônima
```

:::curiosidade O "Document" que entrega tudo
`Document` é o título que os editores de código colocam sozinhos ao criar um arquivo HTML. É tão comum ninguém trocar que dá para descobrir páginas publicadas por aí procurando exatamente por esse título — inclusive de empresas. É o detalhe que revela, antes de qualquer código, que ninguém revisou aquilo antes de publicar. Trocar leva quatro segundos e é a diferença entre um link que chega no WhatsApp com o nome do seu produto e um que chega anônimo.
:::

O **README** é o arquivo que o GitHub mostra na página inicial do repositório. Ele é a vitrine do projeto para quem chega pelo código — e esse link vai poder entrar no seu currículo daqui a um tempo.

```markdown
# NomeDoProduto

Landing page de validação do MVP — Curso Técnico em Desenvolvimento de Sistemas, 2A.

**Acesse:** https://seuusuario.github.io/nomedoproduto/

## O problema
Uma ou duas frases: quem não consegue o quê, e por quê.

## Hipótese testada
Pelo menos X de cada 5 pessoas ... depois de ver a página.

## Feito com
HTML, CSS (Flexbox e Grid) e JavaScript, publicado no GitHub Pages.

## Equipe
Nome, Nome e Nome.
```

### O teste de cinco segundos, sem estragar o resultado

:::conceito Teste dos cinco segundos
Um método real de avaliação de interface: mostra-se a página por poucos segundos, retira-se da vista e pergunta-se o que a pessoa entendeu. Ele mede a única coisa que a landing precisa acertar — se a mensagem passa **na primeira olhada**, que é a única que a maioria dos visitantes dá.
:::

O método é simples e frágil: quem aplica estraga o próprio teste com uma facilidade impressionante, e sempre por boa intenção.

```diagrama-progressivo
titulo: Quatro maneiras de estragar o seu próprio teste
camadas:
  - rotulo: Explicar antes
    conteudo: "Entregar o celular dizendo é um app pra organizar as provas da escola, dá uma olhada. Pronto, acabou o teste. Você acabou de dar a resposta que era justamente o que a página precisava provar sozinha. Entregue dizendo apenas olha essa página por dez segundos."
  - rotulo: Ficar olhando por cima do ombro
    conteudo: "Com o autor ao lado observando, a pessoa deixa de avaliar e passa a tentar acertar. Ela vai procurar a resposta que agrada, e vai encontrar. Entregue o aparelho e desvie o olhar."
  - rotulo: Perguntar se ficou bom
    conteudo: "Ficou legal é uma pergunta sobre você, e ninguém diz na sua cara que ficou ruim. As duas perguntas certas são sobre a página — o que esse produto faz, e você clicaria. Nenhuma delas pede uma nota."
  - rotulo: Defender quando a pessoa erra
    conteudo: "Ela diz uma coisa errada e vem o impulso de corrigir — na verdade é assim, você não viu o botão embaixo. Nesse instante a informação mais valiosa do dia foi destruída. Se ela entendeu errado, a página comunicou errado. Anote exatamente o que ela disse, com as palavras dela, e agradeça."
  - rotulo: O que sobra quando você não estraga nada
    conteudo: "Cinco frases ditas por estranhos sobre o que a sua página comunica. É pouco, é constrangedor e é mais informação do que qualquer opinião de quem já conhece o projeto. É isso que vocês levam para a última aula da trilha."
```

:::importante O teste avalia a página, não você
Isso precisa ficar claro antes de a primeira pessoa pegar o celular: se três das cinco não entenderem, **não** significa que o trabalho foi ruim nem que vocês são ruins. Significa que a página está comunicando mal — e isso é conserto de texto, do kit de copy da aula 09, não conserto de CSS. É informação barata sobre um problema caro. O trio que descobre isso hoje conserta em uma semana; o que só descobrisse na apresentação final não consertaria nunca.
:::

:::dica O que o mercado faz com esses mesmos cinco minutos
Todo produto sério passa por teste com usuário antes de ser lançado, e a regra prática mais conhecida da área diz que cinco pessoas já revelam a maior parte dos problemas de uma interface — depois disso, começam a se repetir. É por isso que cinco, e não cinquenta. E existe uma coisa que você acabou de fazer e que já vale como experiência: rodar uma sessão de teste sem induzir a resposta é uma habilidade que muita gente formada não tem, porque exige a disciplina de ficar calado enquanto alguém não entende o seu trabalho.
:::

## Prática

**Parte 1 — Auditoria (~12 min).** Rode a lista de verificação inteira. Depois **troque de link com o trio vizinho** e rode a lista na página deles: olho de fora acha o que o seu já não vê. Corrija, publique e confira em **aba anônima**.

**Parte 2 — Teste de corredor (~15 min).** Cinco pessoas, **de fora da sua equipe** — de preferência de outra turma. Para cada uma, na ordem:

1. Diga só: *"Olha essa página por dez segundos, por favor."*
2. Entregue o celular e **desvie o olhar**.
3. Aos dez segundos, **tire o aparelho da vista** dela.
4. Pergunte, sem completar nem sugerir:
   - *"O que esse produto faz?"*
   - *"Você clicaria no botão?"*
5. **Anote as palavras dela**, não o seu resumo. Se ela errar, agradeça e passe para a próxima.

```
PESSOA 1 — o que ela disse que o produto faz: ........................
           clicaria? ( ) sim  ( ) não  ( ) não sei
PESSOA 2 — ...
PESSOA 3 — ...
PESSOA 4 — ...
PESSOA 5 — ...

TOTAL entenderam: ...... de 5
TOTAL clicariam (só entre quem entendeu): ...... de ......
A palavra ou ideia errada que mais se repetiu: ......................
```

**Entrega:** o papel com as cinco respostas, mais o link publicado e auditado. Esse papel é o insumo da aula 18 — sem ele, não há o que analisar lá.

## Avaliação

```quiz
- pergunta: Você entrega o celular dizendo "é um app pra organizar as provas, dá uma olhada". Qual é o problema?
  alternativas:
    - texto: Nenhum, contextualizar ajuda a pessoa a avaliar melhor
    - texto: "Você entregou a resposta que a página precisava provar sozinha, e o teste deixou de medir qualquer coisa"
      correta: true
    - texto: O problema é o tempo, que deveria ser maior que dez segundos
    - texto: Deveria ter mostrado a página no computador em vez do celular
  feedback: >
    O que está sendo testado é se a página se explica sem ajuda. Qualquer
    introdução sua responde antecipadamente a primeira pergunta e invalida o
    resultado. A única fala permitida é o pedido para olhar.
- pergunta: Quatro das cinco pessoas entenderam errado o que o produto faz. Como registrar?
  alternativas:
    - texto: "Anotar como acerto parcial, já que chegaram perto"
    - texto: "Anotar exatamente o que cada uma disse, com as palavras delas, e usar o erro mais repetido como pista do que reescrever"
      correta: true
    - texto: Explicar o produto e perguntar de novo
    - texto: Trocar as pessoas por outras que conheçam melhor o assunto
  feedback: >
    Se entenderam errado, a página comunicou errado — e a palavra errada que mais
    se repete costuma apontar exatamente qual trecho reescrever. Corrigir a pessoa
    destrói a informação mais valiosa do teste.
- pergunta: A correção foi publicada mas o celular continua mostrando a versão antiga. Qual é a primeira checagem?
  alternativas:
    - texto: Reescrever o CSS que não surtiu efeito
    - texto: "Abrir o link em aba anônima ou acrescentar ?v=2 no fim do endereço, para descartar cache e propagação"
      correta: true
    - texto: Recriar o repositório do zero
    - texto: Trocar o navegador do celular
  feedback: >
    Publicação leva um ou dois minutos para propagar e o celular guarda a versão
    anterior. Aba anônima elimina as duas hipóteses em vinte segundos, antes de
    você mexer em código que provavelmente já estava certo.
```

## Fechamento

O que ficou do projeto inteiro:

- Vocês têm um **endereço público** que abre no celular de qualquer pessoa, construído por vocês do zero em oito aulas.
- Ele está **estruturado com semântica**, tem **identidade visual** definida em um lugar só, **layout que se adapta** a qualquer tela, **movimento com propósito** e o **JavaScript necessário** — nem uma linha a mais.
- Vocês rodaram uma **lista de verificação de publicação**, que é o mesmo tipo de disciplina que se pratica no trabalho.
- E, o mais raro: vocês têm **cinco frases ditas por estranhos** sobre o que a sua página comunica. Não é achismo, é evidência.

**Na próxima aula:** esses cinco resultados encontram o número que vocês escreveram na aula 08. Aí se descobre se a hipótese passou ou reprovou — e, mais importante, o que fazer com a resposta. As duas saem valendo.

:::roteiro
Estabeleça o clima nos dois primeiros minutos, antes de qualquer coisa técnica: resultado ruim hoje vale nota igual a resultado bom, porque o que se avalia é a condução do teste e a honestidade do registro. Sem isso, metade da turma vai explicar a página antes de entregar o celular, e os dados chegam contaminados na aula 18.

A auditoria cruzada entre trios rende muito mais que a autoavaliação. Sorteie os pares para evitar que amigos passem a mão na cabeça um do outro.

Combine antecipadamente com um colega professor de outra turma para ceder cinco minutos, ou libere a turma para o corredor no intervalo. Testar com a própria turma funciona pior, porque metade já viu o projeto do outro nascer.

Circule vigiando as quatro maneiras de estragar o teste — a mais frequente e mais difícil de conter é defender quando a pessoa erra. Se pegar alguém corrigindo o testador, interrompa na hora e use como exemplo público, sem constranger: "olha, esse aqui é o momento em que a informação mais valiosa some".

Cobre a anotação com as palavras da pessoa, não o resumo do aluno. É onde a evidência se perde.

Recolha os papéis no fim da aula ou fotografe. Papel de teste some de uma semana para a outra, e sem ele a aula 18 não acontece.

Se sobrar tempo, leia dois ou três resultados em voz alta — inclusive um ruim, com o consentimento do trio. Terminar a trilha com a turma vendo que reprovar cedo é útil vale mais que terminar com todo mundo achando que acertou.
:::
