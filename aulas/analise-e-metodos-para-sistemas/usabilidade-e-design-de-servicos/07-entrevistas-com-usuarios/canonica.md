---
titulo: "Entrevistas com usuários: perguntar para descobrir"
tema: Usabilidade e Design de Serviços
disciplina: analise-e-metodos-para-sistemas
serie: 1ª
prerequisitos: ["Jornada do usuário, pontos de contato, frontstage e backstage"]
objetivos:
  - Explicar para que serve a entrevista com usuários no Design de Serviços
  - Planejar uma entrevista definindo objetivo, público, tópicos, roteiro e registro
  - Diferenciar perguntas abertas de fechadas e reconhecer perguntas que induzem a resposta
  - Reescrever perguntas ruins pedindo experiências reais do passado
trilha: usabilidade-e-design-de-servicos
ordem: 7
slug: entrevistas-com-usuarios
modo_origem: seed
fontes:
  - lake/analise-e-metodos-para-sistemas/seed-87-95/92-entrevistas-no-design-de-servicos.pptx
revisao: true
status: aprovada
versao: 1
atualizado_em: 2026-11-04
---

Imagine que você criou um app e pergunta para um amigo: "E aí, você usaria?". Ele responde "Claro, muito massa!". Você fica feliz, passa três meses programando, lança... e ele nunca abre o app. Ele mentiu? Não exatamente. Ele foi gentil, respondeu sobre um futuro imaginário e deu a resposta que a sua pergunta pedia. O problema estava na **pergunta**. Na aula passada você desenhou mapas de jornada imaginando o que o usuário sente. Hoje você vai aprender a perguntar para quem realmente sabe, de um jeito que traga a verdade, e não o elogio que você queria ouvir.

## Objetivos

Ao final desta aula, você será capaz de:

- Explicar para que serve a **entrevista com usuários** no Design de Serviços.
- **Planejar** uma entrevista definindo objetivo, público, tópicos, roteiro e registro.
- Diferenciar perguntas **abertas** de **fechadas** e reconhecer perguntas que **induzem** a resposta.
- Reescrever perguntas ruins pedindo **experiências reais do passado**.

## Pré-requisitos

Ter visto as **Aulas 05 e 06**: serviço, mapa de jornada, pontos de contato, frontstage e backstage.

## Desenvolvimento

### Por que entrevistar

Toda equipe começa um projeto cheia de certezas: "os alunos querem pesquisar livros mais rápido", "o problema da secretaria é a fila". Algumas certezas estão certas; muitas não. A entrevista existe para trocar **suposição** por **evidência** antes de gastar meses programando.

:::conceito Entrevista com usuários
É uma **conversa planejada**, com objetivo de pesquisa, em que você ouve uma pessoa contar como ela vive um serviço: o que precisa fazer, como faz hoje, onde trava, o que sente e que "gambiarras" inventou para dar conta. O foco é **entender experiências e necessidades**, não colher opinião sobre a sua ideia.
:::

:::dica Na profissão
Entrevista com usuário é rotina em equipes de produto e é uma das técnicas clássicas de **levantamento de requisitos** em Análise de Sistemas. Em projeto de TCC, cinco entrevistas bem feitas com o público real valem mais na banca do que cinquenta respostas num formulário cheio de perguntas de "sim ou não".
:::

### Planejar antes de conversar

Entrevista boa parece uma conversa solta, mas foi planejada. Antes de falar com alguém, a equipe define:

1. **Objetivo:** o que queremos descobrir? Exemplo: "entender por que os alunos desistem de pedir documentos na secretaria".
2. **Público:** quem tem essa experiência? Alunos que já pediram documento, a secretária, um responsável. Não adianta entrevistar só quem nunca usou.
3. **Tópicos:** os assuntos que não podem faltar (como pede, quanto espera, como fica sabendo que está pronto).
4. **Roteiro:** uma abertura, as perguntas principais de cada tópico e algumas perguntas de aprofundamento. Teste o roteiro com um colega antes e corte o que ficar confuso.
5. **Registro:** quem anota, se vai gravar, e o **consentimento**: avise o objetivo, peça autorização para anotar ou gravar e combine que o nome não vai aparecer.

:::importante Com quem tem menos de 18 anos
Se o entrevistado for menor de idade (seus colegas, por exemplo), mantenha as respostas **anônimas**, não grave voz nem imagem sem autorização, e não peça dados pessoais que não sejam necessários para a pesquisa. Isso não é burocracia: é respeito, e é o que a LGPD (Lei Geral de Proteção de Dados) espera de quem trata dado de pessoas.
:::

### A arte da pergunta

**Pergunta fechada** se responde com "sim", "não" ou uma palavra: "Você acha o app difícil?". **Pergunta aberta** pede uma história: "Como foi a última vez que você usou o app?". A aberta traz detalhes que você nem sabia que existiam; a fechada só confirma ou nega o que você já pensava. Pior que a fechada é a **pergunta que induz**: ela já carrega a resposta que você quer. "Nosso sistema atual é ruim, não é?" ou "Você concorda que deveria ter notificação?" empurram o entrevistado, que, por educação, costuma concordar.

A regra de ouro cabe em três verbos: **pergunte, escute, aprofunde**. Depois de uma resposta, em vez de pular para a próxima pergunta do roteiro, puxe o fio: "E o que aconteceu depois?", "Por que isso foi importante?", "Como você resolveu?".

```diagrama-progressivo
titulo: Puxando o fio numa entrevista sobre a secretaria
camadas:
  - rotulo: A pergunta de abertura
    conteudo: "Entrevistador: \"Me conta como foi a última vez que você precisou de um documento da escola.\""
  - rotulo: A primeira resposta
    conteudo: "Aluna: \"Pedi uma declaração de matrícula pro estágio. Demorou.\" Uma resposta curta. A tentação é anotar \"demora\" e seguir."
  - rotulo: O aprofundamento
    conteudo: "Entrevistador: \"Demorou quanto? E como você ficou sabendo que estava pronta?\""
  - rotulo: A descoberta
    conteudo: "Aluna: \"Uns três dias. Mas ninguém avisou. Eu passava na secretaria todo intervalo pra perguntar, e quase perdi o prazo do estágio.\""
  - rotulo: O que a equipe aprendeu
    conteudo: O problema principal não é a demora de três dias, e sim não saber quando o documento fica pronto. Sem o aprofundamento, a equipe teria tentado acelerar a secretaria e resolvido o problema errado.
```

:::atencao Erro comum: perguntar sobre o futuro imaginário
"Você usaria um app que avisa quando o documento fica pronto?" Quase todo mundo responde que sim, porque dizer sim é fácil e educado, e não custa nada. Esse "sim" vale pouquíssimo como evidência. Pergunte sobre o **passado real**: "Da última vez, como você soube que estava pronto?". O que a pessoa **fez** de verdade diz muito mais do que o que ela **diz que faria**.
:::

## Prática

**Atividade "conserta essa pergunta" (duplas, sem computador, ~15 min).** A equipe do app **Secretaria Digital** quer entender como os alunos pedem documentos (declaração de matrícula, histórico, carteirinha).

1. **Conserte (5 min).** Reescrevam as perguntas abaixo como perguntas abertas, sem indução, sobre experiências reais:

```text
1. "Você acha que pedir documento é difícil?"
2. "Nosso app novo vai facilitar sua vida, não vai?"
3. "Você usaria notificação no celular?"
4. "Você prefere o botão azul ou verde?"
5. "A secretaria demora muito, né?"
```

2. **Planeje (5 min).** Escrevam o **objetivo** da entrevista em uma frase e um **roteiro** de 5 perguntas: uma de abertura, três principais e uma de aprofundamento.
3. **Ensaie (5 min).** Um da dupla entrevista o outro por 2 minutos usando o roteiro; depois invertem. Quem entrevista anota **uma descoberta** que não estava prevista no roteiro.

## Avaliação

```quiz
- pergunta: Uma equipe quer melhorar o sistema de solicitação de documentos da escola. Qual pergunta é a melhor para começar uma entrevista?
  alternativas:
    - texto: Você concorda que nosso sistema deveria ter notificações?
    - texto: Você prefere notificações azuis ou verdes?
    - texto: Conte como foi a última vez que você precisou pedir um documento na escola.
      correta: true
    - texto: Nosso sistema atual é ruim, não é?
  feedback: >
    É aberta, pede uma experiência real e não sugere solução. As outras induzem
    a resposta ou limitam a conversa a um detalhe.
- pergunta: Por que a pergunta "Você usaria um app que avisa quando o documento fica pronto?" é fraca como evidência?
  alternativas:
    - texto: Porque é longa demais
    - texto: Porque fala de um futuro imaginário, e dizer "sim" é fácil e não custa nada
      correta: true
    - texto: Porque menciona um aplicativo
    - texto: Porque deveria ser feita por escrito
  feedback: >
    Respostas sobre o que a pessoa faria são pouco confiáveis. O que ela fez de
    verdade, no passado, é evidência muito mais forte.
- pergunta: Antes das entrevistas, o que a equipe precisa definir primeiro?
  alternativas:
    - texto: As cores do aplicativo
    - texto: O objetivo da pesquisa, ou seja, o que queremos descobrir
      correta: true
    - texto: A linguagem de programação
    - texto: Quantas telas o sistema vai ter
  feedback: >
    O objetivo orienta tudo o que vem depois, inclusive o público, os tópicos e o
    roteiro. Sem ele, a entrevista vira conversa sem rumo.
- pergunta: "A aluna responde \"Demorou\". O que um bom entrevistador faz em seguida?"
  alternativas:
    - texto: Anota "demora" e passa para a próxima pergunta do roteiro
    - texto: Explica que a demora não é culpa do sistema
    - texto: Aprofunda, perguntando quanto demorou e como ela ficou sabendo que estava pronto
      correta: true
    - texto: Pergunta se ela concorda que um app resolveria
  feedback: >
    Pergunte, escute, aprofunde. É no aprofundamento que aparece o problema real,
    que muitas vezes não é o primeiro que a pessoa cita.
- pergunta: Você vai entrevistar colegas de 15 anos sobre a cantina. Qual cuidado é adequado?
  alternativas:
    - texto: Gravar o vídeo da entrevista e publicar no grupo da turma
    - texto: Pedir CPF e endereço para identificar cada resposta
    - texto: Explicar o objetivo, pedir autorização para anotar e manter as respostas anônimas
      correta: true
    - texto: Não avisar que é uma pesquisa, para a resposta ser mais natural
  feedback: >
    Consentimento e anonimato são parte do planejamento, ainda mais com menores
    de idade. Dado pessoal desnecessário não se coleta.
```

## Fechamento

Hoje você descobriu que:

- A entrevista troca **suposição** da equipe por **evidência** de quem vive o serviço.
- Planejar é definir **objetivo, público, tópicos, roteiro e registro**, com consentimento.
- Perguntas **abertas** trazem histórias; perguntas **fechadas** e **indutoras** só confirmam o que você já pensava.
- Pergunte sobre o **passado real**, não sobre o futuro imaginário, e sempre **aprofunde**.

**Próxima aula:** depois de cinco ou dez entrevistas, você tem páginas e páginas de falas. E agora? Vamos aprender a **analisar** esse material: separar fala de interpretação, agrupar, achar padrões e transformar tudo isso em requisitos.

:::roteiro
Abrir com a cena do "você usaria?" e perguntar quem já recebeu um "sim" que não se confirmou (rifa, festa, grupo de estudo). Para a pergunta indutora, faça a demonstração ao vivo: pergunte a um aluno "a merenda de hoje estava boa, né?" e depois, a outro, "como foi a merenda hoje?"; compare as respostas. No diagrama, pare em "A primeira resposta" e pergunte "o que vocês perguntariam agora?". Acréscimos em relação ao deck 92 da SEED: o erro do futuro imaginário (a ideia é popularizada pelo livro "The Mom Test", de Rob Fitzpatrick) e o cuidado com consentimento e LGPD para menores de idade; o deck não tratava de ética de pesquisa. O desafio do deck (as quatro perguntas sobre documentos) virou a primeira questão do quiz. Na prática, o ensaio da etapa 3 é a parte mais valiosa; se o tempo apertar, encurte a etapa 2.
:::
