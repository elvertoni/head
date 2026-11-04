---
titulo: "Jornada do usuário, pontos de contato, frontstage e backstage"
tema: Usabilidade e Design de Serviços
disciplina: analise-e-metodos-para-sistemas
serie: 1ª
prerequisitos: ["Design de Serviços: a tela não é o serviço"]
objetivos:
  - Construir um mapa de jornada com etapas, ações, pontos de contato, sentimentos, dores e oportunidades
  - Classificar pontos de contato em digitais, físicos e humanos
  - Diferenciar frontstage de backstage num serviço
  - Localizar na jornada a etapa onde o serviço quebra e transformá-la em oportunidade
trilha: usabilidade-e-design-de-servicos
ordem: 6
slug: jornada-pontos-de-contato-frontstage-backstage
modo_origem: seed
fontes:
  - lake/analise-e-metodos-para-sistemas/seed-87-95/91-design-de-servicos-aplicacao.pptx
  - lake/analise-e-metodos-para-sistemas/seed-87-95/90-design-de-servicos-introducao.pptx
revisao: true
status: aprovada
versao: 1
atualizado_em: 2026-11-04
---

Pense na última vez que você foi a um show ou a um jogo. A experiência não começou no portão: começou quando você viu o anúncio, tentou comprar o ingresso (e o site caiu), pegou o ônibus lotado, enfrentou a fila da revista, achou o lugar... e terminou com a volta para casa às duas da manhã. Se perguntarem "como foi?", você vai lembrar do show, mas também da fila e do site que caiu. Um serviço é vivido assim: como uma **sequência de momentos**, e basta um deles dar errado para manchar todos os outros. Na aula passada você viu que o serviço é maior que a tela. Hoje você vai aprender a **desenhar** essa sequência para descobrir exatamente onde ela quebra.

## Objetivos

Ao final desta aula, você será capaz de:

- Construir um **mapa de jornada** com etapas, ações, pontos de contato, sentimentos, dores e oportunidades.
- Classificar **pontos de contato** em digitais, físicos e humanos.
- Diferenciar **frontstage** de **backstage** num serviço.
- Localizar na jornada a etapa onde o serviço **quebra** e transformá-la em **oportunidade**.

## Pré-requisitos

Ter visto a **Aula 05**: serviço como conjunto de pessoas, processos, tecnologias e evidências, e os princípios do Design de Serviços.

## Desenvolvimento

### A jornada: o serviço visto no tempo

:::conceito Jornada do usuário
É a sequência de **etapas** que uma pessoa percorre para atingir um objetivo com um serviço, **do antes ao depois**. O **mapa da jornada** é o desenho dessa sequência: em cada etapa, o que a pessoa faz, com o que ela interage, o que sente e o que a atrapalha.
:::

Um mapa de jornada costuma ser uma tabela: as **etapas** nas colunas e, nas linhas, o que se quer observar em cada uma. Veja a jornada de um aluno pegando um livro emprestado na biblioteca da escola:

| | Procurar | Verificar | Reservar | Retirar | Usar | Devolver |
|---|---|---|---|---|---|---|
| **Ação** | pesquisa o título | vê se está disponível | reserva pelo app | vai ao balcão | lê em casa | leva de volta |
| **Ponto de contato** | app | app | app | balcão, bibliotecária | o livro | balcão |
| **Sentimento** | 🙂 | 🙂 | 😀 | 😠 | 🙂 | 😐 |
| **Dor** | — | — | — | fila de 20 min; livro reservado não estava separado | — | não sabe se a devolução foi registrada |
| **Oportunidade** | — | — | — | separar reservas antes do intervalo | — | confirmar a devolução por mensagem |

Repare no que o mapa revela: o app resolve muito bem as três primeiras etapas, e é justamente **depois** dele que a experiência despenca. Olhando só para a tela, ninguém teria visto isso.

### Pontos de contato: onde o usuário encontra o serviço

:::conceito Ponto de contato
É qualquer momento em que a pessoa **interage** com o serviço. Pode ser **digital** (app, site, e-mail, notificação, QR Code), **físico** (balcão, totem, sala, a própria embalagem) ou **humano** (atendente, professor, suporte).
:::

Um serviço bom precisa que os pontos de contato **contem a mesma história**. Se o app diz "Seu livro está separado" e, no balcão, a bibliotecária responde "Não tem reserva nenhuma aqui", os dois pontos se contradizem e a confiança no serviço inteiro desaba, inclusive no app que estava certo.

### Frontstage e backstage: o palco e os bastidores

:::conceito Frontstage e backstage
A comparação vem do teatro: a plateia vê o palco, enquanto atrás da cortina uma equipe troca cenário e ajusta a luz; se os bastidores falham, a falha aparece no palco. Num serviço, **frontstage** (palco) é tudo o que o usuário **vê e com que interage**: telas, mensagens, o atendente no balcão. **Backstage** (bastidores) é o que acontece **sem que ele veja**, mas que é necessário para o serviço funcionar: o sistema que registra a reserva, a bibliotecária separando o livro, a atualização do estoque. A divisa entre os dois se chama **linha de visibilidade**.
:::

```diagrama-progressivo
titulo: Reservando um computador do laboratório
camadas:
  - rotulo: Frontstage, a reserva
    conteudo: O aluno escolhe o computador 12 para as 14h no app e recebe a mensagem "Reserva confirmada". Até aqui, tudo perfeito.
  - rotulo: Backstage, o registro
    conteudo: O sistema grava a reserva no banco de dados. Funciona.
  - rotulo: Backstage, o aviso ao monitor
    conteudo: O monitor do laboratório usa uma planilha impressa às 7h da manhã. A reserva feita às 10h não aparece nela. Ninguém percebe.
  - rotulo: Frontstage, a chegada
    conteudo: Às 14h o aluno chega e o computador 12 está ocupado por outra pessoa, liberada pelo monitor. Para o aluno, "o app mentiu".
  - rotulo: A oportunidade
    conteudo: O conserto não está na tela de reserva, e sim no backstage. O monitor precisa ver as reservas em tempo real, numa tela simples do próprio sistema, no lugar da planilha impressa.
```

:::atencao Erro comum: a jornada que começa e termina no app
Quem desenvolve tende a mapear só as telas: abrir o app, buscar, reservar, fim. Essa "jornada" sai sempre bonita, porque deixa de fora as etapas onde o serviço realmente quebra: chegar ao balcão, esperar, devolver, receber (ou não) uma confirmação. Teste rápido para o seu mapa: **ele tem alguma etapa fora da tela?** Se não tem, ele está mostrando a interface, não a jornada.
:::

:::dica Na profissão
Mapas de jornada são uma das ferramentas mais usadas por equipes de produto e UX, e costumam ser feitos em papel e post-it ou em quadros online como o Miro e o FigJam. Para quem programa, o backstage do mapa é um tesouro: cada seta dos bastidores ("o sistema avisa o monitor") vira uma integração, uma notificação ou uma tela interna que precisa entrar no backlog.
:::

## Prática

**Atividade "a jornada da merenda" (grupos de 4, sem computador, ~15 min).** Vocês vão mapear a jornada de um aluno no serviço de **merenda** (ou da **cantina**, se a escola tiver) da própria escola.

1. **Etapas (3 min).** Definam de 5 a 7 etapas, do **antes** (saber o cardápio do dia) ao **depois** (devolver a bandeja, ou sair do refeitório).
2. **Mapa (7 min).** Numa folha deitada, montem a tabela com as linhas **Ação**, **Ponto de contato** (marquem D, F ou H para digital, físico ou humano), **Sentimento** (um emoji basta), **Dor** e **Oportunidade**.
3. **Bastidores (5 min).** Escolham a etapa com o pior sentimento e escrevam, embaixo dela, o que acontece no **backstage** naquele momento. A dor nasce no palco ou nos bastidores?

Os grupos colam os mapas lado a lado no quadro. A turma procura a etapa que aparece como dor em mais de um mapa.

## Avaliação

```quiz
- pergunta: Num mapa de jornada da biblioteca, as etapas no app têm sentimento positivo, mas a etapa "retirar no balcão" aparece com fila e irritação. O que o mapa está mostrando?
  alternativas:
    - texto: Que o app precisa de uma interface nova
    - texto: Que a experiência quebra numa etapa fora da tela, e é ali que está a oportunidade
      correta: true
    - texto: Que o mapa está errado, porque só as telas importam
    - texto: Que os alunos não sabem usar o app
  feedback: >
    O mapa de jornada serve justamente para mostrar onde a experiência despenca,
    inclusive nas etapas que acontecem longe do aplicativo.
- pergunta: Qual alternativa traz um ponto de contato digital, um físico e um humano, nessa ordem?
  alternativas:
    - texto: Notificação no celular, balcão de retirada, atendente da secretaria
      correta: true
    - texto: Atendente, site, totem
    - texto: Banco de dados, servidor, planilha
    - texto: Balcão, e-mail, QR Code
  feedback: >
    Notificação é digital, balcão é físico, atendente é humano. Banco de dados e
    servidor não são pontos de contato: o usuário não interage com eles, são backstage.
- pergunta: No serviço de reserva do laboratório, o que é backstage?
  alternativas:
    - texto: A mensagem "Reserva confirmada" que aparece no app
    - texto: O aluno chegando ao laboratório
    - texto: O registro da reserva no banco de dados e o aviso ao monitor
      correta: true
    - texto: A tela onde o aluno escolhe o horário
  feedback: >
    Backstage é o que acontece sem o usuário ver, mas sustenta o serviço. A mensagem
    e a tela de escolha estão no palco.
- pergunta: O app diz "Seu livro está separado", mas no balcão a bibliotecária diz que não há reserva. Que problema isso revela?
  alternativas:
    - texto: Um erro de digitação na mensagem do app
    - texto: Pontos de contato que contam histórias diferentes, porque o backstage não está integrado
      correta: true
    - texto: Falta de cor no botão de reservar
    - texto: Um problema que só a bibliotecária pode resolver, sem relação com o sistema
  feedback: >
    Os pontos de contato precisam ser coerentes. Quando se contradizem, o problema
    costuma estar na ligação entre os bastidores.
- pergunta: Uma equipe mapeou a jornada assim, abrir o app, buscar, reservar e fim. Qual o principal problema desse mapa?
  alternativas:
    - texto: Tem etapas demais
    - texto: Não usa emojis nos sentimentos
    - texto: Só mostra as telas e deixa de fora as etapas fora do app, onde o serviço costuma quebrar
      correta: true
    - texto: Deveria começar pelo banco de dados
  feedback: >
    Uma jornada vai do antes ao depois. Se não tem nenhuma etapa fora da tela,
    está mostrando a interface, não o serviço.
```

## Fechamento

Hoje você descobriu que:

- A **jornada** é o serviço visto no tempo, do antes ao depois, e o **mapa** mostra em que etapa a experiência despenca.
- **Pontos de contato** podem ser digitais, físicos ou humanos, e precisam contar a mesma história.
- **Frontstage** é o que o usuário vê; **backstage** é o que acontece nos bastidores para sustentar o serviço.
- Muitas dores do palco nascem nos bastidores, e é lá que mora a oportunidade.

**Próxima aula:** até aqui, quem preencheu os sentimentos e as dores do mapa foi você, imaginando. Na vida real, quem sabe a resposta é o usuário. Vamos aprender a **entrevistar** de um jeito que traga a verdade, e não a resposta que você queria ouvir.

:::roteiro
Abrir com a pergunta do show ou do jogo e anotar no quadro, em ordem, os momentos que a turma lembrar; quando aparecer "o site caiu" ou "a fila", destaque que isso também é o serviço. Monte a tabela da biblioteca no quadro com a turma antes de mostrar a pronta, se der tempo. No diagrama do laboratório (é o desafio do deck 91 da SEED), pare antes da camada "A chegada" e pergunte "o que vai acontecer às 14h?". Diferença em relação à origem: os decks 90 e 91 apresentavam jornada e frontstage/backstage repetindo o caso da cantina; aqui a jornada ganhou formato de mapa (tabela), os pontos de contato ganharam o requisito de coerência e o conceito de linha de visibilidade foi nomeado, porque ele volta no Service Blueprint (aula 10). Na prática, se a escola não tiver cantina nem merenda com etapas claras, use a entrada e saída da escola ou o empréstimo de livro.
:::
