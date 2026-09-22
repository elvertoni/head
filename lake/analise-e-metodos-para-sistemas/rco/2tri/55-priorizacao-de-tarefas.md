---
titulo: "Priorização de Tarefas"
tipo: rco-seed
disciplina: analise-e-metodos-para-sistemas
sigla_rco: AMS
trimestre: 2
ordem_rco: 55
serie: 1
aula_rco: "Aula 55"
slides: 26
tem_atividade: true
tem_pratica: true
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/AMS/2TRI/55-priorizacao-de-tarefas/55-priorizacao-de-tarefas.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/AMS/2TRI/55-priorizacao-de-tarefas/AULA 55_ATIVIDADE_ANÁLISE E MÉTODO PARA SISTEMAS.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/AMS/2TRI/55-priorizacao-de-tarefas/AULA 55_PRÁTICA_ANÁLISE E MÉTODO PARA SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Priorização de Tarefas

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- ANÁLISE E MÉTODO PARA SISTEMAS
- 1ª Série
- Priorização de Tarefas
- Aula 55

_1 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- COMPETÊNCIA(S) A SER(EM) DESENVOLVIDA(S) NESTA AULA:
- De acordo com o Plano de Curso de Desenvolvimento de Sistemas:
- HABILIDADE(S) A SER(EM) DESENVOLVIDA(S) NESTA AULA:
- Dimensionar requisitos e funcionalidades do sistema.
- Verificar e acompanhar o desenvolvimento do cronograma físico-financeiro.

_1 imagem(ns) no slide._

### Slide 4

- Nesta aula vamos:
- Entender o IMPORTANTE X URGENTE no kanban
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store

_4 imagem(ns) no slide._

### Slide 5

- Este material foi elaborado a partir da análise do plano de curso e reúne os conhecimentos essenciais para o Técnico em Desenvolvimento de Sistemas. As aulas foram organizadas com foco na clareza conceitual, na construção gradual dos conteúdos e na utilização de metodologias ativas que favorecem a compreensão, a participação e o desenvolvimento de habilidades e competências de forma significativa.
- De acordo com a matriz curricular do Curso Técnico em Desenvolvimento de Sistemas, que traz em sua essência componentes estruturados para a realização de aulas práticas, cada unidade curricular deve contemplar, além da abordagem teórica, uma proposta de atividade prática a ser desenvolvida pelo professor. Essa orientação assegura a coerência entre o planejamento didático e o que está estabelecido na matriz, promovendo experiências formativas alinhadas ao perfil profissional previsto.
- O professor tem total autonomia para adaptar o conteúdo conforme o contexto da turma, ajustando exemplos, aprofundamentos e estratégias didáticas para otimizar a aprendizagem e a conexão com a prática profissional.
- Se houver falta de conexão ou indisponibilidade de internet durante a aula, os materiais abaixo podem ser utilizados como apoio para elaborar recursos complementares, garantindo a continuidade da abordagem teórica prevista.
- ATENÇÃO PROFESSOR!
- Agilidade:
- https://cursos.alura.com.br/course/kanban-analises-implementacao/task/104457

_2 imagem(ns) no slide._

### Slide 6

- Aula anterior
- Aprendemos como funciona a gestão visual do kanban.

_1 imagem(ns) no slide._

### Slide 7

- Para pensarmos juntos...
- João, um novato em uma equipe de desenvolvimento de software que usa o quadro kanban para gerenciar suas tarefas. Seus colegas de equipe mencionam a importância das "raias" no quadro kanban, mas você não tem certeza sobre como eles funcionam e para que servem. Além disso, você observa que algumas tarefas parecem ficar presas em certas raias, causando atrasos no fluxo geral do trabalho.

_1 imagem(ns) no slide._

### Slide 8

- Para pensarmos juntos...
- Pesquise e escreva no caderno
- Como posso, utilizar efetivamente as raias para melhorar a fluidez do trabalho no quadro kanban?

_2 imagem(ns) no slide._

### Slide 9

- Resposta
- Como João, você pode aprender a utilizar efetivamente as raias, primeiro entendendo que elas servem para organizar e categorizar as tarefas. Portanto, é essencial que as tarefas sejam alocadas corretamente em cada raia, de acordo com o critério definido pela equipe (como tipo de tarefa, prioridade, entre outros).

_1 imagem(ns) no slide._

### Slide 10

- Resposta
- Além disso, se as tarefas parecem estar presas em certas raias, é um sinal de que vocês precisam revisar o fluxo de trabalho e identificar possíveis gargalos. Esses gargalos podem ser causados por vários fatores, como uma carga de trabalho desequilibrada entre os membros da equipe ou processos ineficientes. Discuta essas observações com a equipe para encontrar soluções colaborativas.

_1 imagem(ns) no slide._

### Slide 11

- Conceituando
- IMPORTANTE: São tarefas que têm um impacto significativo no alcance dos objetivos do projeto. São atividades que precisam ser feitas para garantir o sucesso do projeto, mas não necessariamente precisam ser feitas imediatamente. Exemplos podem ser a concepção e planejamento de um novo recurso, ou a realização de uma revisão de código.
- No kanban, o conceito de "importante X urgente" é fundamental para gerenciar tarefas e garantir a eficiência do fluxo de trabalho.

_2 imagem(ns) no slide._

### Slide 12

- Conceituando
- URGENTE: São tarefas que exigem atenção imediata. Eles podem não ter um impacto direto e significativo nos objetivos do projeto a longo prazo, mas são necessários para manter o fluxo de trabalho diário. Exemplos de tarefas urgentes podem incluir consertar um bug que está impedindo os usuários de usar um recurso principal, ou responder a uma questão crítica de um cliente.

_1 imagem(ns) no slide._

### Slide 13

- Conceituando
- No kanban, é essencial que haja um equilíbrio entre a execução de tarefas importantes e urgentes. Uma prática comum é estabelecer limites para o número de tarefas urgentes que podem estar em andamento ao mesmo tempo, para garantir que as tarefas importantes não sejam negligenciadas.

_1 imagem(ns) no slide._

### Slide 14

- Conceituando
- Além disso, ao planejar o fluxo de trabalho, é crucial considerar tanto a importância como a urgência de cada tarefa para garantir que o trabalho seja feito de forma eficaz e eficiente!

_1 imagem(ns) no slide._

### Slide 15

- Ainda sobre kanban , vamos conhecer praticando?
- Na plataforma Alura vamos acessar o seguinte curso:
- Link para o curso: https://cursos.alura.com.br/course/kanban-analises-implementacao
- Ao longo das atividades, você vai encontrar alguns quizzes e eles não estão ali por acaso! Eles são oportunidades rápidas para testar seu entendimento, reforçar o que aprendeu e identificar pontos que ainda podem melhorar.

_3 imagem(ns) no slide._

### Slide 16

- Dificuldades no dia a dia
- 7 minutos
- O kanban pode apresentar desafios como a sobrecarga de trabalho se as capacidades de cada etapa não forem bem dimensionadas.
- Link para tarefa: https://cursos.alura.com.br/course/kanban-analises-implementacao/task/104448
- A dificuldade em estabelecer prioridades efetivas, a resistência à mudança por parte da equipe, a tendência à complacência se os limites de trabalho em progresso não forem seguidos, e a perda de eficácia se não houver compromisso com a melhoria contínua.
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 17

- Usando raias
- 6 minutos
- As raias no kanban, também conhecidas como "swimlanes", são usadas para dividir visualmente tarefas, histórias ou questões em categorias distintas no quadro kanban.
- Link para tarefa: https://cursos.alura.com.br/course/kanban-analises-implementacao/task/104449
- Elas podem ser categorizadas por tipo de tarefa, responsabilidade da equipe, prioridade, ou qualquer outra maneira que faça sentido para a equipe. As raias ajudam a simplificar a visualização do trabalho, permitindo que as equipes identifiquem rapidamente os status, bloqueios ou gargalos, e alocar recursos de maneira mais eficiente.
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 18

- Políticas explícitas
- 9 minutos
- As políticas explícitas no kanban referem-se às regras acordadas que governam como o trabalho flui através do sistema.
- Link para tarefa: https://cursos.alura.com.br/course/kanban-analises-implementacao/task/104450
- Isso pode incluir critérios de prontidão para mover itens entre as colunas, regras sobre quem pode puxar o trabalho e quando, e limites de trabalho em andamento (WIP). Tornar essas políticas visíveis e explícitas ajuda a equipe a entender melhor o processo, responsabiliza todos pelos acordos feitos e promove a melhoria contínua.
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 19

- Para Responder
- O que são as "raias" em um quadro kanban e qual a sua função?
- Conversem e troquem opiniões sobre

_5 imagem(ns) no slide._

### Slide 20

- Resposta
- As raias em um quadro kanban, também conhecidas como "swimlanes", são divisões horizontais do quadro que ajudam a organizar e categorizar as tarefas de acordo com seu tipo, prioridade, equipe responsável ou qualquer outro critério definido pela equipe.
- Elas servem para tornar o fluxo de trabalho mais claro e gerenciável, permitindo que a equipe visualize facilmente o status das tarefas e identifique quaisquer gargalos ou atrasos.

_1 imagem(ns) no slide._

### Slide 21

- Saiba +
- Video políticas explícitas no kanban
- https://youtu.be/hiINFGEQ3s8

_2 imagem(ns) no slide._

> **Notas do apresentador:** Link do vídeo: https://youtu.be/hiINFGEQ3s8

### Slide 22

- Vamos praticar?
- Prepare-se, porque nessa atividade, você vai sair do modo aprender e entrar direto no modo praticar.
- A atividade prática vai colocar você diante de um desafio real: sensação de ver seu próprio código aparecer online! Acessível, documentado e pronto para o mundo!

_1 imagem(ns) no slide._

### Slide 23

- O que vimos na aula de hoje:
- Conhecemos como funcionam as raias,
- importante X urgente e políticas explícitas no kanban.

_1 imagem(ns) no slide._

### Slide 24

- Pronto para desbloquear sua carreira de TI?
- Está perdido estudando mas não sabe por onde começar? Se a resposta é sim, você está no lugar certo! Descubra as estratégias e ferramentas essenciais para te ajudar a desbloquear seu potencial em TI e buscar sua primeira vaga de emprego no setor!
- Este e-book é um guia completo para quem busca começar pelos melhores caminhos para se tornar um excelente profissional de TI, ensinando a identificar perfis profissionais, aplicar técnicas de estudo eficazes, transformar teoria em prática, e aumentar a visibilidade de seu trabalho no mercado de trabalho. Ideal para novatos e profissionais em transição.
- E o melhor, ele pode ser seu, inteiramente grátis!
- Basta clicar AQUI e realizar o seu cadastro com o seu @escola!

_3 imagem(ns) no slide._

### Slide 25

- Referências
- AFFONSO DE OLIVEIRA, Maurício. Análise e Projeto de Sistemas de Informação Orientados para a Internet. São Paulo: Érica, 2007.
- BEZERRA, Eduardo. Engenharia de Requisitos: Software Orientado ao Negócio. São Paulo: Novatec, 2010.
- BOOCH, Grady; RUMBAUGH, James; JACOBSON, Ivar. UML - Guia do Usuário. 2ª ed. Rio de Janeiro: Campus, 2005.
- GANE, Chris; SARSON, Trish. Análise Estruturada de Sistemas. Rio de Janeiro: LTC, 1995.
- MAGNO DA SILVA NOVAES, Carlos; SAMPAIO DO PRADO LEITE, Júlio César. Análise e Projeto de Sistemas de Informação com UML e Unified Process. São Paulo: Elsevier, 2003.
- PRESSMAN, Roger S.; MAXIM, Bruce R. Engenharia de Software: Uma Abordagem Profissional. 7ª ed. Porto Alegre: AMGH, 2016.
- PRESSMAN, Roger S. Engenharia de Software: Conceitos e Práticas. São Paulo: McGraw-Hill, 2011.
- RITTER, Tiago. Gerenciamento de Projetos: Como definir e controlar o escopo do projeto. São Paulo: Casa do Código, 2017.
- SOARES, Raphael. Metodologia de Desenvolvimento de Software: Um Guia Prático para Iniciantes. São Paulo: Novatec, 2014.
- SOUSA, André S. C.; GUISSI, Viviane Cristina. Modelagem de Processos de Negócio. São Paulo: Érica, 2012.
- Figuras e Imagens:
- https://www.flaticon.com/br
- https://www.istockphoto.com/br
- https://raw.githubusercontent.com/zbtang/React-Native-ViewPager/HEAD/imgs/dotIndicator.gif
- https://storyset.com

### Slide 26

_(sem texto)_

## Atividade

_Fonte: AULA 55_ATIVIDADE_ANÁLISE E MÉTODO PARA SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

ANÁLISE E MÉTODO PARA SISTEMAS

1ª SÉRIE

ATIVIDADE AULA 55

Questão 1

Qual é a função principal das "raias" em um quadro kanban?

A) Representar as diferentes etapas de um processo.

B) Organizar e categorizar as tarefas conforme movem pelo quadro.

C) Designar tarefas específicas para cada membro da equipe.

D) Mostrar o progresso geral do projeto.

Resposta: B) Organizar e categorizar as tarefas conforme movem pelo quadro.

As raias em um quadro kanban ajudam a organizar e categorizar as tarefas, facilitando o entendimento do fluxo de trabalho e a identificação de gargalos.

Questão 2

O que você deve fazer se notar que as tarefas estão frequentemente ficando presas em uma raia específica no quadro kanban?

A) Mudar todas as tarefas dessa raia para outra.

B) Remover a raia problemática do quadro.

C) Ignorar a situação, pois isso é normal no uso do kanban.

D) Discutir a situação com a equipe e buscar identificar e resolver os gargalos.

Resposta: D) Discutir a situação com a equipe e buscar identificar e resolver os gargalos.

Quando as tarefas estão presas frequentemente em uma raia específica, isso pode ser um indicativo de um problema no fluxo de trabalho. É importante discutir isso com a equipe, identificar a causa desse gargalo e trabalhar juntos para encontrar uma solução.

## Prática

_Fonte: AULA 55_PRÁTICA_ANÁLISE E MÉTODO PARA SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

ANÁLISE E MÉTODO PARA SISTEMAS

1ª SÉRIE

ATIVIDADE PRÁTICA AULA 55

#### 1. Objetivo da Aula Prática

Ao final desta aula prática, o estudante deverá:

- Compreender a diferença entre tarefas importantes e tarefas urgentes no contexto do Kanban.
- Desenvolver a habilidade de priorizar atividades utilizando critérios de importância e urgência.
- Entender a função das raias (swimlanes) na organização visual do trabalho.
- Aplicar políticas explícitas para gerenciamento do fluxo de tarefas.
- Ser capaz de organizar um quadro Kanban utilizando prioridades e categorias para melhorar a eficiência da equipe.

#### 2. Ferramentas Recomendadas

###### Post-its ou Cartões de Papel

Para que serve: Representar tarefas do projeto.

Por que é adequada ao tema: Permite classificar atividades por importância e urgência.

Como facilita o aprendizado: Ajuda a visualizar prioridades de forma prática.

###### Quadro Branco ou Cartolina

Para que serve: Construir o quadro Kanban com raias.

Por que é adequada ao tema: Permite representar visualmente o fluxo de trabalho.

Como facilita o aprendizado: Favorece a identificação de gargalos e prioridades.

###### Trello

Para que serve: Criar um quadro Kanban digital.

Por que é adequada ao tema: Permite organizar tarefas por colunas e etiquetas.

Como facilita o aprendizado: Simula o ambiente utilizado por equipes ágeis.

Link: https://trello.com

###### Google Planilhas

Para que serve: Registrar a classificação das tarefas.

Por que é adequada ao tema: Facilita a documentação das decisões da equipe.

Como facilita o aprendizado: Permite analisar prioridades de forma estruturada.

#### 3. Checklist Inicial

Antes de iniciar a prática, os estudantes devem possuir:

- Post-its ou cartões de papel
- Canetas ou marcadores
- Cartolina ou quadro branco
- Computador ou celular com internet (opcional)
- Conta no Trello (opcional)
- Acesso ao conteúdo da aula
- Equipes organizadas entre 3 e 5 integrantes

#### 4. Passo a Passo do Docente (Aula de até 50 minutos)

##### Como conduzir a aula

- Retome os conceitos da aula anterior sobre gestão visual do Kanban.
- Apresente os conceitos centrais:
- Importante x Urgente
- Raias (Swimlanes)
- Políticas Explícitas
- Explique como a priorização influencia o fluxo de trabalho.
- Demonstre exemplos de tarefas importantes e urgentes.
- Mostre exemplos de raias em um quadro Kanban.
- Explique o conceito de políticas explícitas.
- Apresente a atividade prática.

##### Preparações necessárias

- Organizar os grupos.
- Disponibilizar cartolinas e post-its.
- Preparar um exemplo simples de quadro Kanban.
- Separar cenários para a atividade.

##### Alertas e pontos de atenção

- Os alunos podem confundir importância com urgência.
- Reforce que tarefas urgentes nem sempre são as mais importantes.
- Incentive o debate entre os grupos.
- Oriente a criação de critérios claros para priorização.

##### Dinâmica sugerida

Classificação → Organização → Construção do Quadro → Análise → Apresentação

##### Gerenciamento de Tempo

| Etapa | Tempo |
| --- | --- |
| Revisão dos conceitos | 10 min |
| Explicação da atividade | 5 min |
| Classificação das tarefas | 10 min |
| Construção do quadro | 15 min |
| Apresentações | 5 min |
| Reflexão final | 5 min |

Total: 50 minutos

#### 5. Atividade Prática — Descrição Geral

Os estudantes deverão atuar como uma equipe responsável pelo desenvolvimento de um aplicativo de gerenciamento de eventos escolares.

Cada equipe receberá uma lista de tarefas e deverá:

- Classificar as atividades em importantes e urgentes.
- Criar raias para organizar o fluxo de trabalho.
- Definir políticas explícitas para movimentação dos cartões.
- Construir um quadro Kanban completo.
- Identificar possíveis gargalos e propor melhorias.
A atividade simula situações reais de priorização e organização do trabalho em equipes ágeis.

#### 6. Metodologia Ativa Utilizada

###### Aprendizagem Baseada em Problemas (PBL)

Os estudantes deverão resolver problemas relacionados à priorização de tarefas.

###### Simulação Profissional

A atividade reproduz o uso do Kanban em equipes de desenvolvimento.

###### Aprendizagem Colaborativa

As decisões serão tomadas em grupo.

###### Elementos de Lemov Aplicados

- Objetivo Claro
- Produção Visível
- Participação Ativa
- Discussão Estruturada
- Feedback Imediato

#### 7. Passo a Passo da Atividade Prática (para os alunos)

##### Cenário

Sua equipe está desenvolvendo um sistema para gerenciamento de eventos escolares.

##### Etapa 1 – Classificação das Tarefas

- Formem grupos de 3 a 5 integrantes.
- Recebam a lista de tarefas do projeto.
Exemplos:

- Corrigir erro crítico no login.
- Desenvolver relatório de participantes.
- Atualizar identidade visual.
- Corrigir falha no cadastro de usuários.
- Criar painel administrativo.
- Responder solicitação urgente da coordenação.
- Classifiquem cada tarefa como:
- Importante
- Urgente
- Importante e Urgente

##### Etapa 2 – Construção das Raias

- Criem um quadro Kanban contendo as colunas:
- A Fazer
- Em Andamento
- Em Revisão
- Concluído
- Criem as seguintes raias:
- Importante
- Urgente
- Importante e Urgente

##### Etapa 3 – Definição das Políticas Explícitas

- Definam regras para movimentação das tarefas.
Exemplos:

- Nenhuma tarefa pode avançar sem revisão.
- Máximo de 3 tarefas simultâneas em andamento.
- Tarefas urgentes têm prioridade de execução.

##### Etapa 4 – Simulação

- Movimentem os cartões pelo quadro.
- Simulem atrasos e gargalos.
- Identifiquem possíveis melhorias.

##### Etapa 5 – Apresentação

- Apresentem o quadro para a turma.
- Expliquem:
- Como classificaram as tarefas.
- Quais políticas criaram.
- Quais gargalos encontraram.

#### 8. Exemplo ou Demonstração

##### Tarefas

| Tarefa | Classificação |
| --- | --- |
| Corrigir bug de login | Importante e Urgente |
| Atualizar layout | Importante |
| Responder cliente | Urgente |

##### Exemplo de Política Explícita

- Nenhum cartão pode permanecer mais de uma rodada em "Em Revisão".
- O limite de WIP é 3 tarefas por equipe.

##### Exemplo de Raia

| Raia | Objetivo |
| --- | --- |
| Importante | Atividades estratégicas |
| Urgente | Problemas que exigem ação imediata |
| Importante e Urgente | Itens críticos do projeto |

#### 9. Resultado Esperado

O estudante deverá apresentar:

- Quadro Kanban estruturado.
- Tarefas corretamente classificadas.
- Raias organizadas.
- Políticas explícitas definidas.
- Gargalos identificados e analisados.
O professor poderá verificar o aprendizado observando:

- Correta aplicação dos conceitos.
- Qualidade da priorização.
- Clareza das políticas criadas.
- Capacidade de análise crítica.
- Participação dos integrantes.

#### 10. Formato de Entrega da Atividade

###### O que deve ser entregue

- Foto do quadro Kanban ou link do Trello.
- Documento contendo:
- Lista de tarefas classificadas
- Raias criadas
- Políticas explícitas
- Gargalos identificados

###### Nome do arquivo

- PriorizacaoKanban_Aula55_NomeGrupo

###### Local de entrega

- Sala de aula
- Ambiente virtual definido pelo professor

###### Prazo sugerido

Ao final da aula.

#### 11. Encerramento e Reflexão

Conduza a reflexão utilizando as perguntas:

- Qual a diferença entre uma tarefa importante e uma tarefa urgente?
- Como as raias ajudaram a organizar o trabalho?
- Quais gargalos foram identificados durante a simulação?
- As políticas explícitas facilitaram a organização da equipe?
- Como a priorização adequada impacta o sucesso de um projeto?
