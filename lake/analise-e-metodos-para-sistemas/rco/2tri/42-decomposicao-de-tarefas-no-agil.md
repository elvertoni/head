---
titulo: "Decomposição de Tarefas no Ágil"
tipo: rco-seed
disciplina: analise-e-metodos-para-sistemas
sigla_rco: AMS
trimestre: 2
ordem_rco: 42
serie: 1
aula_rco: "Aula 42"
slides: 23
tem_atividade: true
tem_pratica: true
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/AMS/2TRI/42-decomposicao-de-tarefas-no-agil/42-decomposicao-de-tarefas-no-agil.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/AMS/2TRI/42-decomposicao-de-tarefas-no-agil/AULA 42_PRÁTICA_ANÁLISE E MÉTODO PARA SISTEMAS.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/AMS/2TRI/42-decomposicao-de-tarefas-no-agil/AULA 42_ATIVIDADE_ANÁLISE E MÉTODO PARA SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Decomposição de Tarefas no Ágil

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- ANÁLISE E MÉTODO PARA SISTEMAS
- 1ª Série
- Decomposição de Tarefas no Ágil
- Aula 42

_1 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- COMPETÊNCIA(S) A SER(EM) DESENVOLVIDA(S) NESTA AULA:
- De acordo com o Plano de Curso de Desenvolvimento de Sistemas:
- HABILIDADE(S) A SER(EM) DESENVOLVIDA(S) NESTA AULA:
- Executar alterações e manutenções em aplicações e rotinas de acordo com as definições estabelecidas.
- EM13MAT315 – Representar algoritmos e processos por meio de fluxogramas.

_1 imagem(ns) no slide._

### Slide 4

- Nesta aula vamos:
- Aprender a como decompor as tarefas para utilização em uma sprint.
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
- Scrum e histórias do usuário:
- https://cursos.alura.com.br/course/scrum-parte-4/task/111984
- Manifesto ágil e liderança nos projetos:
- https://www.alura.com.br/conteudo/scrum-parte-2

_2 imagem(ns) no slide._

### Slide 6

- Aula anterior
- Por mais que já conhecemos o Scrum realizamos uma revisão a respeito de alguns aspectos da ferramenta Scrum.

_1 imagem(ns) no slide._

### Slide 7

- Para pensarmos juntos...
- João, um desenvolvedor iniciante, acaba de ingressar em uma equipe de desenvolvimento de software que utiliza o Scrum como metodologia ágil. Ele tem conhecimento limitado sobre o Scrum e está tentando entender como a equipe lida com a decomposição do trabalho e o gerenciamento do Sprint Backlog. Durante o Sprint Planning, João ouve a equipe discutir a criação de tarefas menores para cada história de usuário selecionada para a próxima sprint.
- Conversem e compartilhem

_2 imagem(ns) no slide._

### Slide 8

- Para pensarmos juntos...
- Troque ideias com seus colegas!!
- Como a decomposição de histórias de usuário em tarefas menores ajuda a equipe a gerenciar melhor o Sprint Backlog e a trabalhar de maneira mais eficiente no Scrum?

_2 imagem(ns) no slide._

### Slide 9

- Resposta
- A decomposição de histórias de usuário em tarefas menores ajuda a equipe a gerenciar o Sprint Backlog de maneira mais eficaz porque permite que os membros da equipe dividam o trabalho em partes menores e mais gerenciáveis. Essas tarefas menores são mais fáceis de estimar em termos de esforço e tempo necessários, o que ajuda a equipe a planejar e executar a sprint de forma mais realista e precisa. Além disso, a decomposição facilita a colaboração e a distribuição equilibrada do trabalho entre os membros da equipe, garantindo que todos tenham uma compreensão clara das expectativas e responsabilidades durante a sprint.

_1 imagem(ns) no slide._

### Slide 10

- Conceituando
- A decomposição no Scrum é um processo pelo qual as histórias de usuário, que são descrições de alto nível das funcionalidades desejadas pelos usuários finais, são divididas em tarefas menores e mais detalhadas. Este processo é realizado para facilitar a compreensão do trabalho a ser realizado, permitir estimativas mais precisas e garantir que o progresso seja facilmente rastreado e gerenciado pela equipe. A decomposição é uma parte fundamental do planejamento e execução de projetos ágeis usando o Scrum.

_3 imagem(ns) no slide._

### Slide 11

- Impactos positivos do Scrum no planejamento de projetos
- O Sprint Backlog, por outro lado, é um conjunto de histórias de usuário e tarefas selecionadas para serem trabalhadas durante uma sprint, que é um período de tempo fixo (geralmente de 2 a 4 semanas) no qual a equipe se compromete a concluir um conjunto de trabalho específico. O Sprint Backlog é derivado do Product Backlog, que é uma lista priorizada de histórias de usuário e requisitos de todo o projeto.

_2 imagem(ns) no slide._

### Slide 12

- Impactos negativos e desafios na utilização do Scrum
- Essa abordagem permite que a equipe entenda melhor o trabalho a ser realizado e estime com precisão quanto esforço será necessário para concluir cada tarefa.
- Durante o Sprint Planning, a equipe seleciona as histórias de usuário do Product Backlog com base em sua prioridade e capacidade da equipe. Em seguida, essas histórias de usuário são decompostas em tarefas menores que podem ser atribuídas e executadas pelos membros da equipe.

_1 imagem(ns) no slide._

### Slide 13

- Resumo
- A decomposição e o gerenciamento do Sprint Backlog são essenciais para garantir que a equipe de desenvolvimento possa entregar incrementos de software de alta qualidade de maneira consistente e previsível. Ao dividir as histórias de usuário em tarefas menores, a equipe pode monitorar e ajustar seu progresso durante a sprint, identificar e resolver problemas e garantir que o trabalho esteja sendo realizado de forma eficiente e eficaz.

_1 imagem(ns) no slide._

### Slide 14

- Impactos negativos e desafios na utilização do Scrum
- Em resumo, a decomposição no Scrum e o gerenciamento do Sprint Backlog são componentes cruciais para o sucesso de projetos ágeis. Ao dividir histórias de usuário em tarefas menores e gerenciar adequadamente o Sprint Backlog, as equipes podem planejar e executar sprints com maior eficiência e eficácia,
- resultando em produtos de software de maior qualidade entregues no prazo e de acordo com as expectativas dos usuários finais.

_1 imagem(ns) no slide._

### Slide 15

- Ao longo das atividades, você vai encontrar alguns quizzes e eles não estão ali por acaso! Eles são oportunidades rápidas para testar seu entendimento, reforçar o que aprendeu e identificar pontos que ainda podem melhorar.
- Atividade Prática na Plataforma Alura
- Na plataforma Alura vamos acessar o seguinte curso:
- Link para o curso: https://cursos.alura.com.br/course/scrum-parte-4

_3 imagem(ns) no slide._

### Slide 16

- Sprint Backlog
- 9 minutos
- As tarefas listadas pelo Time Scrum são aquelas que a equipe se comprometeu a realizar durante o Sprint atual.
- Link para tarefa: https://cursos.alura.com.br/course/scrum-parte-4/task/22413
- Essas tarefas são importantes, pois vão ajudar o time a executar e entregar aquilo que foi prometido.
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 17

- Hora de praticar!
- Divida os participantes em grupos de 3 a 5 pessoas.
- Forneça a cada grupo uma lista de 3 histórias de usuário simples (por exemplo, "Como usuário, quero pesquisar produtos por categoria", "Como usuário, quero adicionar produtos ao carrinho de compras" e "Como usuário, quero fazer o checkout do meu pedido").
- Peça aos grupos para discutir e decompor cada história de usuário em tarefas menores e mais detalhadas. Por exemplo, a história de usuário "Como usuário, quero pesquisar produtos por categoria" pode ser decomposta em tarefas como "Criar uma página de listagem de produtos", "Implementar filtro por categoria" e "Exibir informações detalhadas do produto".
- Mostre o resultado do trabalho de vocês para os demais colegas!!

_2 imagem(ns) no slide._

> **Notas do apresentador:** Dinâmica: Scrum Puzzle Objetivo: Familiarizar os participantes com a decomposição do Scrum e o Sprint Backlog, ajudando-os a entender como as histórias de usuário são divididas em tarefas menores e como isso se relaciona com o planejamento de uma sprint. Materiais: Papel, canetas, cartões de índice ou post-its.

### Slide 18

- Hora de praticar!
- Peça a cada grupo para escrever as tarefas em cartões de índice ou post-its e organizá-los em uma estrutura de Sprint Backlog, mostrando a sequência de tarefas a serem executadas.
- Defina um tempo limite para a atividade (por exemplo, 20 minutos).
- Quando o tempo acabar, peça a cada grupo para apresentar seu Sprint Backlog e explicar como as tarefas se relacionam com as histórias de usuário.
- Após as apresentações, promova uma discussão sobre as lições aprendidas, desafios enfrentados durante a decomposição e como isso pode ser aplicado em projetos reais usando o Scrum.

_1 imagem(ns) no slide._

> **Notas do apresentador:** Dinâmica: Scrum Puzzle Objetivo: Familiarizar os participantes com a decomposição do Scrum e o Sprint Backlog, ajudando-os a entender como as histórias de usuário são divididas em tarefas menores e como isso se relaciona com o planejamento de uma sprint. Materiais: Papel, canetas, cartões de índice ou post-its.

### Slide 19

- Vamos praticar?
- Prepare-se, porque nessa atividade, você vai sair do modo aprender e entrar direto no modo praticar.
- A atividade prática vai colocar você diante de um desafio real: sensação de ver seu próprio código aparecer online! Acessível, documentado e pronto para o mundo!

_1 imagem(ns) no slide._

### Slide 20

- O que vimos na aula de hoje:
- Compreendemos como é feito a decomposição das atividades do Product Backlog para o Sprint Backlog.

_1 imagem(ns) no slide._

### Slide 21

- Pronto para desbloquear sua carreira de TI?
- Está perdido estudando mas não sabe por onde começar? Se a resposta é sim, você está no lugar certo! Descubra as estratégias e ferramentas essenciais para te ajudar a desbloquear seu potencial em TI e buscar sua primeira vaga de emprego no setor!
- Este e-book é um guia completo para quem busca começar pelos melhores caminhos para se tornar um excelente profissional de TI, ensinando a identificar perfis profissionais, aplicar técnicas de estudo eficazes, transformar teoria em prática, e aumentar a visibilidade de seu trabalho no mercado de trabalho. Ideal para novatos e profissionais em transição.
- E o melhor, ele pode ser seu, inteiramente grátis!
- Basta clicar AQUI e realizar o seu cadastro com o seu @escola!

_3 imagem(ns) no slide._

### Slide 22

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

### Slide 23

_(sem texto)_

## Atividade

_Fonte: AULA 42_ATIVIDADE_ANÁLISE E MÉTODO PARA SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

ANÁLISE E MÉTODO PARA SISTEMAS

1ª SÉRIE

ATIVIDADE AULA 42

Questão 1

No contexto do Scrum, o que é o Sprint Backlog?

a) Uma lista completa de todas as histórias de usuário do projeto.

b) Um conjunto de itens selecionados do Product Backlog que serão trabalhados durante a próxima Sprint.

c) Um registro das tarefas concluídas durante a Sprint atual.

d) Um gráfico que mostra o progresso do projeto ao longo do tempo.

Resposta correta: b) Um conjunto de itens selecionados do Product Backlog que serão trabalhados durante a próxima Sprint. O Sprint Backlog é composto pelos itens que a equipe escolheu para trabalhar durante a próxima Sprint, a partir do Product Backlog.

Questão 2

Qual é o principal propósito do Sprint Backlog no Scrum?

a) Determinar a duração da Sprint.

b) Atribuir tarefas aos membros da equipe.

c) Fornecer uma visão geral dos itens planejados para a Sprint atual e permitir o acompanhamento do progresso da equipe.

d) Avaliar o desempenho da equipe ao longo do tempo.

Resposta correta: c) Fornecer uma visão geral dos itens planejados para a Sprint atual e permitir o acompanhamento do progresso da equipe. O Sprint Backlog ajuda a equipe a ter uma compreensão clara do trabalho a ser realizado durante a Sprint e a acompanhar o progresso das tarefas.

## Prática

_Fonte: AULA 42_PRÁTICA_ANÁLISE E MÉTODO PARA SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

ANÁLISE E MÉTODO PARA SISTEMAS

1ª SÉRIE

ATIVIDADE PRÁTICA AULA 42

##### 1. Objetivo da Aula Prática

Ao final desta aula prática, o estudante deverá:

- Aprender como funciona a decomposição de histórias de usuário em tarefas menores no Scrum.
- Desenvolver a habilidade prática de organizar tarefas em um Sprint Backlog.
- Ser capaz de dividir funcionalidades complexas em atividades menores, organizadas e executáveis dentro de uma Sprint.

##### 2. Ferramentas Recomendadas

Cartões de índice ou post-its

- Para que serve: Registro das histórias de usuário e tarefas da Sprint.
- Por que é adequada ao tema: Facilita divisão e reorganização das tarefas.
- Como facilita o aprendizado: Ajuda na visualização da decomposição do trabalho.
Quadro branco ou cartolina

- Para que serve: Organização visual do Sprint Backlog.
- Por que é adequada ao tema: Simula ambientes Scrum reais.
- Como facilita o aprendizado: Permite acompanhar a sequência das tarefas.
Trello (https://trello.com) — opcional

- Para que serve: Gestão digital do Sprint Backlog.
- Por que é adequada ao tema: Ferramenta utilizada em projetos ágeis reais.
- Como facilita o aprendizado: Permite visualizar tarefas e progresso da Sprint.
Google Docs ou Planilhas Google

- Para que serve: Registro das histórias e tarefas detalhadas.
- Por que é adequada ao tema: Facilita documentação e compartilhamento.
- Como facilita o aprendizado: Ajuda na organização lógica das atividades.

##### 3. Checklist Inicial

Antes de iniciar a prática, o estudante deve ter:

- Papel, cartões ou post-its
- Caneta ou marcador
- Quadro ou superfície para organização
- Espaço para trabalho em grupo
- Computador ou celular com internet (opcional)
- Acesso ao material da aula

##### 4. Passo a Passo do Docente (Aula de até 50 minutos)

###### Como conduzir a aula

- Retome a aula anterior sobre revisão dos conceitos Scrum.
- Apresente o tema central: decomposição de tarefas no ágil.
- Explique os conceitos abordados no material:
- Histórias de usuário
- Product Backlog
- Sprint Backlog
- Decomposição de tarefas
- Sprint Planning
- Apresente o cenário da aula: João aprendendo como dividir histórias em tarefas menores.
- Explique que a decomposição facilita:
- Estimativas mais precisas
- Distribuição equilibrada do trabalho
- Melhor acompanhamento da Sprint
- Demonstre rapidamente como transformar uma história de usuário em tarefas menores.
- Explique a dinâmica prática “Scrum Puzzle”.

###### Preparações necessárias

- Organizar cartões e post-its
- Preparar exemplos de histórias de usuário
- Organizar espaço para trabalho em grupo

###### Alertas e pontos de atenção

- Alunos podem criar tarefas muito grandes
- Oriente para tarefas simples e objetivas
- Reforce que cada tarefa deve representar uma ação clara
- Incentive colaboração entre os membros

###### Dinâmica sugerida

Leitura da história → decomposição → organização do Sprint Backlog → apresentação

###### Gerenciamento de tempo (50 minutos)

- Introdução e explicação: 15 minutos
- Decomposição das histórias: 15 minutos
- Organização do Sprint Backlog: 10 minutos
- Apresentação e reflexão: 10 minutos

##### 5. Atividade Prática — Descrição Geral

Os estudantes deverão simular o processo de decomposição de histórias de usuário em tarefas menores para composição de um Sprint Backlog.

Cada equipe irá:

- Receber histórias de usuário simples
- Dividir as histórias em tarefas menores
- Organizar as tarefas em sequência lógica
- Construir um Sprint Backlog visual
A atividade simula o planejamento inicial de uma Sprint em projetos Scrum.

A habilidade desenvolvida será a capacidade de organizar trabalho colaborativo em tarefas menores, claras e executáveis.

##### 6. Metodologia Ativa Utilizada

- Aprendizagem baseada em problemas (PBL)
- Simulação profissional
- Aprendizagem colaborativa
- Experimentação prática
Elementos de Lemov aplicados:

- Objetivo claro
- Produção visível
- Participação ativa
- Pensamento estruturado
- Feedback contínuo

##### 7. Passo a Passo da Atividade Prática (para os alunos)

- Formem equipes de 3 a 5 integrantes.
- Recebam 3 histórias de usuário fornecidas pelo professor.
- Leiam atentamente cada história de usuário.
- Identifiquem quais atividades precisam ser realizadas para implementar cada funcionalidade.
- Dividam as histórias em tarefas menores e objetivas.
- Registrem cada tarefa em cartões ou post-its.
- Organizem as tarefas em sequência lógica no Sprint Backlog.
- Verifiquem se todas as tarefas necessárias foram incluídas.
- Preparem uma apresentação explicando como a equipe realizou a decomposição.

##### 8. Exemplo ou Demonstração

História de usuário:

“Como usuário, quero pesquisar produtos por categoria.”

Tarefas menores:

- Criar página de produtos
- Implementar filtro por categoria
- Criar campo de pesquisa
- Exibir resultados filtrados
- Testar funcionalidade
Sprint Backlog:

| Ordem | Tarefa |
| --- | --- |
| 1 | Criar página |
| 2 | Implementar filtro |
| 3 | Criar busca |
| 4 | Testar sistema |

##### 9. Resultado Esperado

O estudante deverá apresentar:

- Histórias de usuário decompostas corretamente
- Tarefas organizadas em Sprint Backlog
- Sequência lógica de execução
- Distribuição clara do trabalho
O professor poderá verificar o aprendizado observando:

- Clareza das tarefas
- Organização do Sprint Backlog
- Capacidade de decomposição
- Participação da equipe

##### 10. Formato de Entrega da Atividade

- Formato: Quadro físico, cartolina ou documento digital
- Registro: Foto, print ou arquivo digital
- Nome do arquivo (se necessário): DecomposicaoSprint_NomeGrupo
- Local de entrega: Em sala ou via plataforma digital
- Prazo sugerido: Durante a aula

##### 11. Encerramento e Reflexão

Finalize conduzindo uma reflexão orientada:

- Foi mais fácil trabalhar após dividir as tarefas?
- Como a decomposição ajuda na organização da Sprint?
- O que pode acontecer quando uma tarefa é muito grande?
