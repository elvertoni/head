---
titulo: Fundamentos da Agilidade
tema: Metodologias Ágeis
disciplina: analise-e-metodos-para-sistemas
serie: 1ª
prerequisitos: []
objetivos:
  - Explicar o que é agilidade como filosofia, e não como sinônimo de pressa
  - Reconhecer os valores do Manifesto Ágil e a ideia de entregar valor
  - Diferenciar Scrum e Kanban como ferramentas da mentalidade ágil
trilha: metodologias-ageis
ordem: 33
slug: fundamentos-da-agilidade
modo_origem: seed
fontes:
  - lake/analise-e-metodos-para-sistemas/AULA NIV1_ ANÁLISE E MÉTODO PARA SISTEMAS.pptx
revisao: true
status: aprovada
versao: 2
atualizado_em: 2026-06-21
---

Pensa naquele trabalho em grupo em que vocês fizeram um plano lindo no começo — quem faz o quê, prazo pra tudo — e aí, na véspera da entrega, o professor mudou as regras. Plano todo no lixo, correria, noite mal dormida. O mundo do software vive isso o tempo inteiro: o cliente muda de ideia, o mercado vira, um concorrente lança algo novo. Por décadas, programadores tentaram lutar contra a mudança com planos cada vez mais rígidos — e quebravam a cara. Até que um grupo decidiu fazer o contrário: e se a gente **abraçar** a mudança em vez de fugir dela? Nascia a agilidade. É por aqui que sua trilha de métodos começa.

## Objetivos

Ao final desta aula, você será capaz de:

- Explicar o que é **agilidade** como filosofia de trabalho — e por que ela **não** é sinônimo de "fazer rápido".
- Reconhecer os valores do **Manifesto Ágil** e a ideia central de **entregar valor**.
- Diferenciar **Scrum** e **Kanban** como duas ferramentas da mesma mentalidade ágil.

## Pré-requisitos

Nenhum. Se você já fez trabalho em grupo, já sentiu na pele o problema que a agilidade resolve.

## Desenvolvimento

### Em uma frase

:::importante
Agilidade é entregar valor cedo, aprender com cada entrega e mudar de rota quando a realidade muda.
:::

### Ágil não é correr

Quando alguém diz "fulano é ágil", você pensa em rapidez. No mundo do software, agilidade é outra coisa.

:::conceito Agilidade
É uma **filosofia de trabalho** que valoriza entregar resultado útil em pequenos pedaços, com frequência, e **se adaptar** às mudanças em vez de seguir um plano fixo a qualquer custo. Não é sobre velocidade bruta — é sobre **direção certa** e capacidade de mudar de rota.

:::

:::atencao Erro comum
"Ser ágil é trabalhar mais rápido, correndo." Errado. Um time pode correr muito e entregar algo que o cliente nem queria — esforço desperdiçado. Ágil é entregar **cedo** o que tem **valor** e ajustar com o retorno de quem usa. Velocidade sem direção é só pressa.

:::

### O Manifesto Ágil

Em 2001, dezessete profissionais cansados de projetos que fracassavam escreveram o **Manifesto Ágil** — um documento curtíssimo que virou a base de tudo. A ideia central:

:::conceito Entregar valor
**Valor** é aquilo que o cliente ou usuário realmente deseja e que resolve o problema dele. O objetivo do time ágil não é "terminar tarefas", é **entregar valor** o quanto antes — e em pedaços que já funcionam, em vez de um pacote gigante só no final.

:::

Na prática, a agilidade preza por três coisas: **entrega contínua** (pedaços prontos com frequência), **transparência no processo** (todo mundo enxerga o andamento) e **alta qualidade** nas entregas.

### Uma filosofia, várias ferramentas

Agilidade é a mentalidade. Em cima dela nasceram **ferramentas** diferentes que seguem a mesma ideia:

```diagrama-progressivo
titulo: Da filosofia às ferramentas
camadas:
  - rotulo: 1. A mentalidade ágil
    conteudo: Entregar valor cedo, em pedaços, e se adaptar à mudança. É a base que todas as ferramentas seguem.
  - rotulo: 2. Scrum
    conteudo: Organiza o trabalho em ciclos fixos (sprints), com papéis e reuniões definidas. É o foco desta trilha.
  - rotulo: 3. Kanban
    conteudo: Organiza o trabalho num quadro visual de colunas (a fazer / fazendo / feito), com foco no fluxo contínuo.
```

:::dica Por que isto vale ouro pra sua carreira
Agilidade não é teoria de escola — é como **a maioria das empresas de software trabalha hoje**. Saber Scrum e Kanban é um dos primeiros itens que recrutadores procuram em quem busca a primeira vaga. Você está começando a trilha pelo conceito que vai aparecer na sua primeira entrevista.

:::

## Prática

**Atividade "priorizar e fluir" (em duplas, sem computador, ~15 min).** A turma vai organizar a **festa junina da escola**. No caderno, a partir desta lista solta de tarefas — *comprar comida, montar barracas, divulgar nas redes, definir data, contratar som, decorar, vender ingressos* —:

1. **Priorize**: qual tarefa tem que vir **primeiro** e por quê? (dica: o que as outras dependem?)
2. **Fluxo**: coloque as 7 tarefas numa ordem que faça sentido — como construir uma casa, alicerce antes do telhado.
3. **Valor**: se faltasse tempo e só desse pra fazer 3, quais entregariam mais **valor** (uma festa que acontece)?

Cada dupla apresenta sua ordem. A turma compara: todo mundo priorizou igual? Onde divergiu, quem justificou melhor?

## Avaliação

```quiz
- pergunta: O que significa "ser ágil" no desenvolvimento de software?
  alternativas:
    - texto: Trabalhar o mais rápido possível, sem parar
    - texto: Entregar valor em pequenos pedaços e se adaptar às mudanças
      correta: true
    - texto: Seguir o plano inicial sem nunca mudar
    - texto: Evitar qualquer tipo de reunião
  feedback: >
    Agilidade é filosofia de adaptação e entrega de valor, não velocidade bruta.
    Correr na direção errada não é ser ágil.
- pergunta: O que o Manifesto Ágil propôs como mudança central?
  alternativas:
    - texto: Abraçar a mudança em vez de lutar contra ela com planos rígidos
      correta: true
    - texto: Eliminar o cliente do processo
    - texto: Documentar tudo antes de começar a programar
    - texto: Trabalhar sempre sozinho
  feedback: >
    A virada foi aceitar que requisitos mudam — e construir um jeito de trabalhar
    que se adapta, entregando valor aos poucos.
- pergunta: Qual a relação entre agilidade, Scrum e Kanban?
  alternativas:
    - texto: São três coisas sem relação entre si
    - texto: Agilidade é a mentalidade; Scrum e Kanban são ferramentas que a seguem
      correta: true
    - texto: Scrum e Kanban são contrários à agilidade
    - texto: Kanban substitui a agilidade
  feedback: >
    Agilidade é a filosofia. Scrum (ciclos e papéis) e Kanban (quadro de fluxo) são
    duas formas práticas de colocá-la em ação.
```

## Fechamento

Hoje você descobriu que:

- **Agilidade** é uma filosofia de entregar valor em pedaços e se adaptar — **não** é trabalhar correndo.
- O **Manifesto Ágil** (2001) propôs abraçar a mudança em vez de lutar contra ela com planos rígidos.
- O foco é sempre **entregar valor**: o que o usuário realmente quer, o quanto antes.
- **Scrum** e **Kanban** são ferramentas diferentes da mesma mentalidade ágil.

**Próxima aula:** a partir de agora a gente mergulha no **Scrum** — a ferramenta ágil mais usada. Começamos montando o time: quem faz o quê num projeto Scrum.

:::roteiro
Abrir com a dor concreta do trabalho em grupo que mudou na véspera — todos viveram isso. O erro "ágil = correr" é o ponto central: provoque ("então quem faz mais rápido é mais ágil?") e desmonte com o exemplo de entregar algo que o cliente não queria. O diagrama filosofia→ferramentas prepara o terreno pro resto da trilha; cite Kanban de leve (não é o foco). A prática da festa junina é puro desplugado de priorização/fluxo — deixe-os divergir, o valor está na justificativa. Tarefa de casa opcional do slide (pesquisar um caso de uso de ágil) pode virar gancho da próxima. Alura ("Fundamentos da agilidade") opcional. 8 min pro quiz.
:::
