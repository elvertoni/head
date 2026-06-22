---
titulo: História e Evolução dos Sistemas Operacionais
tema: Da era dos cartões perfurados aos sistemas móveis
disciplina: introducao-a-computacao
serie: 1ª
prerequisitos: [Sistema Operacional - Conceito e Estrutura]
objetivos:
  - Reconhecer por que os sistemas operacionais surgiram
  - Identificar as grandes eras da evolução dos SOs
  - Relacionar avanços de hardware a avanços nos sistemas operacionais
  - Perceber o objetivo comum por trás de toda a evolução
trilha: arquitetura-computadores-e-sistemas-operacionais
ordem: 36
slug: historia-e-evolucao-dos-sistemas-operacionais
modo_origem: seed
fontes:
  - lake/introducao-a-computacao/AULA 36_INTRODUÇÃO A COMPUTAÇÃO.pptx
revisao: true
status: aprovada
versao: 1
atualizado_em: 2026-06-21
---

Você desbloqueia o celular e, em **menos de um segundo**, tudo está pronto: apps, mensagens, câmera. Parece o mínimo. Mas nos anos 1950, para rodar **um único** programa, um especialista passava horas conectando fios em painéis ou empilhando cartões de papel perfurado, e qualquer errinho recomeçava tudo. Não existia "gerente" nenhum — a pessoa **era** o gerente, na unha. A distância entre aquele pesadelo e o seu celular instantâneo é a história do sistema operacional. E essa história tem uma direção clara: cada passo existiu para **facilitar a vida de quem usa o computador**.

## Objetivos

Ao final desta aula, você será capaz de:

- Reconhecer **por que** os sistemas operacionais surgiram.
- Identificar as **grandes eras** da evolução dos SOs.
- Relacionar avanços de **hardware** a avanços nos **sistemas operacionais**.
- Perceber o **objetivo comum** por trás de toda a evolução.

## Pré-requisitos

Ter visto a **Aula 35**: o que é um sistema operacional, suas camadas e o kernel.

## Desenvolvimento

### Antes do SO: o trabalho na unha

:::conceito Processamento batch (em lote)
Nos primeiros computadores, os programas eram preparados em **cartões perfurados** e processados em **lotes**, um depois do outro, sem interação. A pessoa entregava a pilha de cartões, esperava, e só depois recebia o resultado. Se houvesse um erro, recomeçava. Era lento, manual e exigia especialistas.
:::

Foi essa dor que criou a necessidade de um sistema operacional: alguém — ou melhor, **algum software** — para automatizar o trabalho repetitivo de preparar, organizar e executar programas.

:::importante O fio que costura toda a história
Cada avanço dos sistemas operacionais teve **um mesmo objetivo**: tornar o computador **mais fácil de usar** e o trabalho de criar e rodar programas **menos penoso**. Guarde isso — é a chave para entender por que cada era surgiu. Não foi tecnologia por tecnologia; foi sempre para facilitar a vida de quem está do outro lado.
:::

### As grandes eras, em movimento

Em vez de decorar datas soltas, entenda o **salto** de cada era — e como cada salto dependeu de um avanço no hardware.

```diagrama-progressivo
titulo: As eras dos sistemas operacionais
camadas:
  - rotulo: Até os anos 1950 — na unha
    conteudo: Programação direta em painéis e cartões perfurados, em lotes (batch). Surge a necessidade de automatizar. Por volta dos anos 1950, aparecem os primeiros sistemas para automatizar tarefas manuais.
  - rotulo: Anos 1960–70 — o chip muda tudo
    conteudo: A invenção do circuito integrado (chip) permite computadores em maior escala. Nascem as empresas que farão o computador pessoal, como Apple e Microsoft.
  - rotulo: Anos 1980 — o computador pessoal
    conteudo: Era intensa: MS-DOS, o primeiro Windows, o Macintosh da Apple, o Unix. O computador começa a sair dos centros de pesquisa e entrar em casas e escritórios.
  - rotulo: Anos 1990 — tudo se conecta
    conteudo: Os SOs ganham recursos de rede. Surge o Linux, criado por Linus Torvalds, de código aberto. A internet começa a moldar os sistemas.
  - rotulo: Anos 2000 até hoje — o SO no bolso
    conteudo: Windows XP, 7, 10, 11; macOS; e a explosão móvel com iOS (iPhone) e Android (2008). O sistema operacional vai parar no seu bolso.
```

### Hardware e software puxam um ao outro

Repare num padrão: cada salto do sistema operacional veio **junto** com um salto do hardware.

:::exemplo
O **chip** (circuito integrado) deixou os computadores menores e mais baratos — e só então fez sentido criar sistemas para computadores **pessoais**, nos anos 1980. Depois, a popularização das **redes** e da **internet**, nos anos 1990, empurrou os SOs a ganharem recursos de conexão. E os **smartphones**, nos anos 2000, exigiram sistemas operacionais pensados para tela de toque e bateria — daí iOS e Android. Hardware novo abre portas; o sistema operacional corre para aproveitá-las.
:::

:::curiosidade
O **Linux**, que hoje roda na maioria dos servidores da internet, em supercomputadores e por dentro de **todo aparelho Android**, nasceu como um projeto de estudante. Linus Torvalds o criou e o liberou como **código aberto** — qualquer um pode ver, usar e melhorar. Por isso existem tantas "distribuições" diferentes de Linux: a liberdade do código aberto fez o sistema se ramificar em incontáveis versões. Provavelmente você usa Linux todos os dias sem saber, cada vez que abre um app no celular ou acessa um site.
:::

:::atencao Cuidado com a precisão histórica
Datas e "primeiros" em história da computação variam conforme a fonte — diferentes autores apontam diferentes sistemas como "o primeiro SO", e os anos são aproximados. O que **não** muda, e é o que importa nesta aula, é a **direção** da evolução: do trabalho manual com cartões rumo a sistemas cada vez mais automáticos, conectados e fáceis de usar. Foque no movimento, não na decoreba de datas.
:::

## Prática

**Atividade "linha do tempo viva" (desplugada, 12 a 15 min).** A turma reconstrói a evolução e descobre a lógica por trás dela.

O professor entrega cartões embaralhados, cada um com um marco (ex.: *"cartões perfurados e processamento em lote"*, *"invenção do chip"*, *"primeiro Windows e MS-DOS"*, *"surgimento do Linux e das redes"*, *"iPhone e Android"*).

Em grupos, os alunos devem:

1. **Ordenar** os cartões na linha do tempo (do mais antigo ao mais recente).
2. Escrever, ao lado de cada um, **que dificuldade aquela era resolveu** (o que ficou mais fácil).

Depois, discutam em turma:

- Qual é o **fio comum** que liga todas as eras? (Facilitar o uso e o desenvolvimento.)
- Como cada avanço de **hardware** (chip, rede, smartphone) puxou um avanço no **sistema operacional**?
- Se você fosse imaginar a **próxima** era dos SOs, o que ela tornaria mais fácil?

**Extensão opcional (pesquisa rápida):** escolha um sistema operacional atual (Windows, Android, iOS, Linux) e descubra o ano aproximado em que surgiu. Em 2 linhas, posicione-o em uma das eras vistas na aula.

## Avaliação

```quiz
- pergunta: Por que os sistemas operacionais surgiram?
  alternativas:
    - texto: Para deixar os computadores mais bonitos
    - texto: Para automatizar o trabalho manual e tornar o uso e o desenvolvimento mais fáceis
      correta: true
    - texto: Para aumentar o preço dos computadores
    - texto: Para substituir a internet
  feedback: >
    A dor do trabalho manual (painéis, cartões, lotes) criou a necessidade de
    automatizar. O fio comum de toda a evolução é facilitar o uso e o desenvolvimento.
- pergunta: Como o avanço do hardware se relaciona com a evolução dos sistemas operacionais?
  alternativas:
    - texto: Não há relação; são coisas independentes
    - texto: Cada salto de hardware (chip, redes, smartphone) abriu portas que os SOs correram para aproveitar
      correta: true
    - texto: O hardware sempre atrapalhou os SOs
    - texto: Os SOs surgiram antes de qualquer hardware
  feedback: >
    O chip viabilizou o computador pessoal; as redes empurraram recursos de
    conexão; os smartphones exigiram SOs de toque e bateria. Hardware abre portas.
- pergunta: O que torna o Linux capaz de existir em tantas versões (distribuições) diferentes?
  alternativas:
    - texto: Ele é pago e fechado
    - texto: Ele é de código aberto, então qualquer um pode ver, usar e melhorar
      correta: true
    - texto: Ele só funciona em supercomputadores
    - texto: Ele foi criado por uma única empresa secreta
  feedback: >
    O Linux é de código aberto: o código é livre para ver e modificar. Por isso se
    ramificou em incontáveis distribuições — e roda por dentro do Android.
```

## Fechamento

Hoje você percorreu décadas em uma aula:

- Antes do SO, programar era **manual**: painéis, **cartões perfurados** e processamento em **lote**.
- Os SOs evoluíram em **eras**: automação inicial → computador pessoal → redes → era móvel.
- Cada avanço de **hardware** (chip, internet, smartphone) puxou um avanço no **sistema operacional**.
- O **objetivo comum** sempre foi o mesmo: **facilitar** o uso e o desenvolvimento.

Você viu o que o SO é (Aula 35) e de onde ele veio (hoje). Na próxima aula, a gente foca no que ele **faz por você no dia a dia** — as funções concretas que transformam um amontoado de hardware em algo que você usa sem nem pensar.

:::roteiro
Abrir pelo contraste celular instantâneo × horas com cartões nos anos 50 — é o gancho que dá escala. Insistir no fio condutor (facilitar a vida) acima das datas; o :::importante e o :::atencao existem justamente para evitar que a aula vire decoreba cronológica. Usar o diagrama de eras como espinha e o exemplo hardware-puxa-software para dar causalidade. A curiosidade do Linux costuma surpreender ("uso Linux todo dia?"). Corrigir mentalmente o slide: é Torvalds, não "Tolvalds", e as datas são aproximadas. Na prática, ordenar + dizer "o que ficou mais fácil" é o que cristaliza a lógica. Fechar ganchando as funções do SO (Aula 37).
:::
