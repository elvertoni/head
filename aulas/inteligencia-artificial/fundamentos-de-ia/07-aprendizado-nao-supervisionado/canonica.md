---
titulo: Aprendizado Não-Supervisionado
tema: Fundamentos de IA
disciplina: inteligencia-artificial
serie: Extra
prerequisitos: [Tipos de Aprendizado de Máquina]
objetivos:
  - Explicar o que é clustering e como ele acha grupos sem rótulos
  - Reconhecer usos reais da descoberta de padrões ocultos
  - Entender que a máquina agrupa, mas quem interpreta o grupo é o humano
trilha: fundamentos-de-ia
ordem: 7
slug: aprendizado-nao-supervisionado
modo_origem: tema
fontes: []
revisao: false
status: aprovada
versao: 1
atualizado_em: 2026-06-15
---

Imagina que alguém despeja na sua frente 500 músicas sem nome, sem gênero, sem nada — e pede pra você organizar. Você não tem um gabarito dizendo "isto é rock, isto é funk". Mesmo assim, ouvindo, você começa a juntar as parecidas: as agitadas de um lado, as calmas de outro, as eletrônicas num canto. Você acabou de fazer, na mão, o que o [[aprendizado-nao-supervisionado|aprendizado não-supervisionado]] faz: achar grupos e padrões **sem ninguém dizer quais são**. É o tipo de IA que trabalha no escuro — e descobre coisas que nem sabíamos que estavam lá.

## Objetivos

Ao final desta aula, você será capaz de:

- Explicar o que é **clustering** e como ele acha grupos sem rótulos.
- Reconhecer **usos reais** da descoberta de padrões ocultos.
- Entender que a máquina **agrupa**, mas quem **interpreta** o grupo é o humano.

## Pré-requisitos

Ter visto a **Aula 05** (os três tipos; em especial o não-supervisionado).

## Desenvolvimento

### Achar grupos sem gabarito

A marca do não-supervisionado é trabalhar com dados **sem rótulo**. A tarefa mais comum é o agrupamento.

:::conceito Clustering
É a técnica que **agrupa dados parecidos** entre si, sem que ninguém tenha dito antes quais são os grupos. A máquina mede a semelhança entre os exemplos e junta os que ficam "perto". O resultado são **clusters** (grupos) que emergem dos próprios dados — não de categorias definidas por humanos.

:::

É assim que uma loja descobre "perfis de cliente" que ninguém tinha imaginado, ou que um serviço de streaming agrupa músicas e usuários parecidos. Ninguém rotulou nada — os grupos apareceram da semelhança.

:::atencao Erro comum
Achar que os grupos já vêm com **nome e significado**. Não vêm. O clustering diz "estes 80 clientes são parecidos entre si", mas **não** diz "este é o grupo dos jovens gastadores" — esse rótulo quem dá é o **humano**, interpretando depois. A máquina acha a estrutura; o significado é leitura nossa. Confundir isso leva a confiar cegamente em grupos que talvez não queiram dizer nada.

:::

### Para que serve descobrir padrões

```diagrama-progressivo
titulo: Clustering em ação - perfis de clientes
camadas:
  - rotulo: 1. Dados crus, sem rótulo
    conteudo: A loja tem dados de compra de milhares de clientes - o que compram, quando, quanto gastam. Nenhum rótulo de "tipo de cliente".
  - rotulo: 2. A máquina agrupa por semelhança
    conteudo: O clustering junta clientes com comportamento parecido. Surgem, digamos, três grupos distintos - sem ninguém ter definido.
  - rotulo: 3. O humano interpreta
    conteudo: Olhando os grupos, a equipe percebe - "este grupo compra de madrugada", "este só compra promoção". Agora os grupos ganham significado.
  - rotulo: 4. A empresa age
    conteudo: Com os perfis em mãos, dá pra personalizar ofertas para cada grupo. O padrão escondido virou decisão de negócio.
```

:::dica Onde isso aparece na sua vida (e carreira)
Recomendações ("quem ouviu isto também ouviu..."), detecção de comportamento estranho (uma compra muito fora do seu padrão dispara alerta de fraude), organização automática de fotos por rosto — tudo isso usa descoberta de padrões. Para quem vai trabalhar com dados, o não-supervisionado é a ferramenta de **explorar o desconhecido**: quando você ainda não sabe o que procurar, ele mostra a estrutura escondida.

:::

## Prática

**Atividade "clustering na mão" (em grupos de 4, sem computador, ~15 min).** Cada grupo recebe a missão de **agrupar os próprios colegas** (ou objetos da mochila) **sem usar categorias óbvias prontas**.

1. Escolham **características** observáveis (ex.: cor da roupa, tipo de calçado, ter ou não fone) — mas **não** usem rótulos prontos como "menino/menina".
2. Formem **2 ou 3 grupos** juntando os mais parecidos pelas características escolhidas.
3. **Só depois** de formar os grupos, deem um **nome** a cada um (aqui vocês são o "humano que interpreta").
4. Outro grupo consegue adivinhar **qual característica** vocês usaram pra agrupar?

Discussão: o mesmo conjunto de pessoas pode gerar grupos diferentes dependendo da característica escolhida. Quem decide o que é "parecido"?

## Avaliação

```quiz
- pergunta: O que o clustering faz?
  alternativas:
    - texto: Prevê um número a partir de exemplos rotulados
    - texto: Agrupa dados parecidos sem que ninguém tenha definido os grupos antes
      correta: true
    - texto: Aprende por tentativa e recompensa
    - texto: Classifica e-mails usando um gabarito
  feedback: >
    Clustering é não-supervisionado: junta o que é parecido sem rótulos prévios. Os
    grupos emergem dos próprios dados.
- pergunta: Depois que o clustering forma os grupos, quem dá significado a eles?
  alternativas:
    - texto: A própria máquina, automaticamente
    - texto: O humano, interpretando os grupos depois
      correta: true
    - texto: Ninguém, os grupos não têm uso
    - texto: O sistema operacional
  feedback: >
    A máquina acha a estrutura ("estes são parecidos"), mas o significado ("grupo dos
    que compram de madrugada") é interpretação humana.
- pergunta: Qual destes é um uso típico de aprendizado não-supervisionado?
  alternativas:
    - texto: Prever o preço exato de uma casa
    - texto: Descobrir perfis de clientes parecidos sem categorias pré-definidas
      correta: true
    - texto: Classificar e-mails já rotulados como spam
    - texto: Estimar a nota de uma prova
  feedback: >
    Descobrir grupos/perfis sem rótulos é a cara do não-supervisionado. Prever preço e
    classificar spam rotulado são supervisionados.
```

## Fechamento

Hoje você descobriu que:

- O **[[aprendizado-nao-supervisionado|não-supervisionado]]** acha grupos e padrões **sem rótulos**.
- O **[[clustering]]** agrupa dados pela **semelhança** — os grupos emergem dos dados.
- A máquina **agrupa**, mas quem **interpreta e nomeia** os grupos é o humano.
- Recomendações, detecção de fraude e organização de fotos usam essa descoberta de padrões.

**Próxima aula:** fechamos o Módulo 2 abrindo a caixa-preta mais famosa da IA: as **redes neurais** — o que são e por que o "deep" do deep learning é profundo.

:::roteiro
Abrir com as 500 músicas sem nome — todos sentem o impulso de agrupar. O conceito de clustering vem daí naturalmente. O erro "os grupos já têm nome" é o mais importante: a máquina acha a estrutura, o humano dá sentido. O diagrama dos perfis de cliente mostra o fluxo completo até a decisão. A prática de agrupar colegas é literal clustering desplugado — a sacada final (grupos diferentes conforme a característica) ensina que "parecido" depende de quem escolhe a régua. Conteúdo estável, sem web. 8 min pro quiz.
:::
