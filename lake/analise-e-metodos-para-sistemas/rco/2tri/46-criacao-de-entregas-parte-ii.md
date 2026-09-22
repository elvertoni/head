---
titulo: "Criação de Entregas – Parte II"
tipo: rco-seed
disciplina: analise-e-metodos-para-sistemas
sigla_rco: AMS
trimestre: 2
ordem_rco: 46
serie: 1
aula_rco: "Aula 46"
slides: 23
tem_atividade: true
tem_pratica: true
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/AMS/2TRI/46-criacao-de-entregas-parte-ii/46-criacao-de-entregas-parte-ii.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/AMS/2TRI/46-criacao-de-entregas-parte-ii/AULA 46_ATIVIDADE_ANÁLISE E MÉTODO PARA SISTEMAS.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/AMS/2TRI/46-criacao-de-entregas-parte-ii/AULA 46_PRÁTICA_ANÁLISE E MÉTODO PARA SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Criação de Entregas – Parte II

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- ANÁLISE E MÉTODO PARA SISTEMAS
- 1ª Série
- Criação de Entregas – Parte II
- Aula 46

_1 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- COMPETÊNCIA(S) A SER(EM) DESENVOLVIDA(S) NESTA AULA:
- De acordo com o Plano de Curso de Desenvolvimento de Sistemas:
- HABILIDADE(S) A SER(EM) DESENVOLVIDA(S) NESTA AULA:
- Executar alterações e manutenções em aplicações e rotinas de acordo com as definições estabelecidas.
- Redigir relatórios sobre o desenvolvimento do projeto.

_1 imagem(ns) no slide._

### Slide 4

- Nesta aula vamos:
- Aprender como criado as entregas om a ferramentas Scrum Parte II.
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
- Iniciamos os estudos a respeito de entregáveis em Scrum.

_1 imagem(ns) no slide._

### Slide 7

- Para pensarmos juntos...
- Laura acabou de ingressar em uma nova empresa como desenvolvedora júnior. Esta é a primeira vez que ela trabalha em um ambiente que adota a metodologia Scrum. Nos primeiros dias, ela percebe que todas as manhãs a equipe se reúne para uma breve reunião chamada de "Reunião Diária". Laura, não familiarizada com essa prática, fica confusa sobre o propósito e a importância dessa reunião.

_1 imagem(ns) no slide._

### Slide 8

- Para pensarmos juntos...
- 3 minutos
- Levante a mão quem souber responder!
- Por que as reuniões diárias são importantes em um ambiente de Scrum?

_3 imagem(ns) no slide._

### Slide 9

- Resposta
- As reuniões diárias são uma parte vital da metodologia Scrum. Elas são conduzidas para garantir que todos os membros da equipe estejam na mesma página sobre o andamento do projeto. Durante essas reuniões, cada membro da equipe compartilha o que fez no dia anterior, o que planeja fazer naquele dia e se está enfrentando algum bloqueio ou impedimento. Isso promove a comunicação transparente, a colaboração e ajuda a equipe a identificar e resolver problemas em tempo hábil. Além disso, permite que a equipe se adapte rapidamente às mudanças, que é um dos princípios chave do Scrum.

_1 imagem(ns) no slide._

### Slide 10

- Conceituando
- As ferramentas que auxiliam os entregáveis é também parte integrante da ferramenta Scrum, vejamos a seguir alguns desses componentes que compõem o Scrum.

_1 imagem(ns) no slide._

### Slide 11

- Conceituando
- Reuniões diárias: Também conhecidas como Daily Scrum, são reuniões curtas (geralmente cerca de 15 minutos) realizadas todos os dias pela equipe de Scrum. Essas reuniões têm como objetivo compartilhar atualizações, discutir bloqueios e coordenar esforços para o dia. Cada membro da equipe normalmente responde a três perguntas: o que eu fiz ontem, o que vou fazer hoje e há algum obstáculo no meu caminho?

_1 imagem(ns) no slide._

### Slide 12

- Conceituando
- Refinando o Produto: O Refinamento do Produto (anteriormente conhecido como grooming do backlog) é um processo contínuo no qual a equipe de Scrum e o Product Owner colaboram para garantir que as histórias de usuários no backlog do produto sejam relevantes, detalhadas e estimadas. Esse processo ajuda a equipe a entender melhor o que precisa ser feito e a planejar adequadamente para sprints futuras.

_1 imagem(ns) no slide._

### Slide 13

- Conceituando
- Gráfico Burndown: O gráfico Burndown é uma representação visual do trabalho restante no backlog versus tempo. Normalmente, o eixo Y representa o trabalho restante (como em horas de trabalho ou pontos de história), e o eixo X representa o tempo (geralmente dias em uma sprint). O propósito desse gráfico é fornecer uma visão rápida do progresso da equipe durante a sprint. Se a equipe estiver no ritmo certo para completar todo o trabalho, a linha no gráfico deve estar consistentemente descendo para chegar a zero no último dia da sprint.

_1 imagem(ns) no slide._

### Slide 14

- Resumo
- Esses três componentes são partes vitais de qualquer implementação de Scrum. As reuniões diárias mantêm a equipe sincronizada, o refinamento do produto garante que o trabalho mais valioso está pronto para ser puxado para a próxima sprint, e o gráfico Burndown dá uma visão clara do progresso da sprint.

_1 imagem(ns) no slide._

### Slide 15

- Link para o curso: https://cursos.alura.com.br/course/scrum-parte-5
- Ao longo das atividades, você vai encontrar alguns quizzes e eles não estão ali por acaso! Eles são oportunidades rápidas para testar seu entendimento, reforçar o que aprendeu e identificar pontos que ainda podem melhorar.
- Atividade Prática na Plataforma Alura
- Na plataforma Alura vamos acessar o seguinte curso:

_3 imagem(ns) no slide._

### Slide 16

- Reunião Diária
- 9 minutos
- Daremos foco nesta aula para a Reunião Diária prevista no guia Scrum.
- Link para tarefa: https://cursos.alura.com.br/course/scrum-parte-5/task/22456
- Ela é uma ferramenta essencial para qualquer projeto em Scrum, abaixo são citadas algumas das características específicas desse tipo de reunião.
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 17

- Refinando o Backlog Priorizado do Produto
- 5 minutos
- Quaisquer mudanças ou atualizações no backlog devem ser discutidas e incorporadas no Backlog Priorizado do Produto.
- Link para tarefa: https://cursos.alura.com.br/course/scrum-parte-5/task/22457
- Por exemplo, se uma Sprint foi terminada, mas uma entrega não foi aceita, ela vai retornar para o Backlog do Produto e, posteriormente, se o dono do produto achar importante, ele vai entrar na próxima Sprint.
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 18

- O Gráfico Burndown
- 7 minutos
- O Gráfico Burndown é uma ferramenta simples e nele relacionamos o ideal com o desempenho real da equipe.
- Link para tarefa: https://cursos.alura.com.br/course/scrum-parte-5/task/22586
- No gráfico o objetivo é zerar os pontos e alcançamos isso quando as tarefas delimitadas são concluídas. Portanto, considerando as semanas, temos um "ideal".
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 19

- Vamos praticar?
- Prepare-se, porque nessa atividade, você vai sair do modo aprender e entrar direto no modo praticar.
- A atividade prática vai colocar você diante de um desafio real: sensação de ver seu próprio código aparecer online! Acessível, documentado e pronto para o mundo!

_1 imagem(ns) no slide._

### Slide 20

- O que vimos na aula de hoje:
- Aprendemos sobre reunião diária, refinando o produto e o gráfico burndown em Scrum.

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

_Fonte: AULA 46_ATIVIDADE_ANÁLISE E MÉTODO PARA SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

ANÁLISE E MÉTODO PARA SISTEMAS

1ª SÉRIE

ATIVIDADE AULA 46

Questão 1

O que é discutido durante as reuniões diárias em Scrum?

a) Problemas pessoais dos membros da equipe.

b) Planos de férias da equipe.

c) O que cada membro da equipe fez ontem, o que fará hoje e se há algum impedimento.

d) Discussões técnicas profundas sobre a implementação de certos recursos.

Resposta correta: c) O que cada membro da equipe fez ontem, o que fará hoje e se há algum impedimento. As reuniões diárias em Scrum são curtas e destinadas a atualizar rapidamente a equipe sobre o progresso e quaisquer bloqueios que possam existir. Elas não são destinadas a discussões técnicas profundas ou problemas pessoais.

Questão 2

O que é o gráfico de Burndown em Scrum?

a) Um gráfico que mostra a quantidade de café consumida pela equipe durante a sprint.

b) Um gráfico que mostra a quantidade de trabalho restante em relação ao tempo.

c) Um gráfico que mostra o número de bugs encontrados durante a sprint.

d) Um gráfico que mostra a quantidade de dinheiro gasto durante a sprint.

Resposta correta: b) Um gráfico que mostra a quantidade de trabalho restante em relação ao tempo. O gráfico de Burndown é uma ferramenta visual utilizada em Scrum para rastrear o progresso da equipe ao longo de uma sprint. Ele mostra a quantidade de trabalho restante (geralmente em termos de horas ou pontos de história) no eixo vertical, e o tempo (geralmente dias de sprint) no eixo horizontal. O objetivo é que a linha do gráfico esteja descendo constantemente, chegando a zero no final da sprint.

## Prática

_Fonte: AULA 46_PRÁTICA_ANÁLISE E MÉTODO PARA SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

ANÁLISE E MÉTODO PARA SISTEMAS

1ª SÉRIE

ATIVIDADE PRÁTICA AULA 46

##### 1. Objetivo da Aula Prática

Ao final desta aula prática, o estudante deverá:

- Aprender como funcionam as reuniões diárias, o refinamento do backlog e o gráfico Burndown no Scrum.
- Desenvolver a habilidade prática de acompanhar o progresso de uma Sprint utilizando ferramentas de monitoramento ágil.
- Ser capaz de simular uma Daily Scrum, refinar backlog e interpretar um gráfico Burndown para acompanhamento do projeto.

##### 2. Ferramentas Recomendadas

Post-its ou cartões de papel

- Para que serve: Representar tarefas do backlog e andamento da Sprint.
- Por que é adequada ao tema: Facilita movimentação e atualização das atividades.
- Como facilita o aprendizado: Ajuda a visualizar o fluxo de trabalho.
Quadro branco ou cartolina (Kanban simples)

- Para que serve: Organização visual das tarefas da Sprint.
- Por que é adequada ao tema: Simula o ambiente de equipes Scrum reais.
- Como facilita o aprendizado: Permite acompanhar o progresso do projeto.
Planilhas Google ou Excel Online

- Para que serve: Construção simples do gráfico Burndown.
- Por que é adequada ao tema: Facilita representação visual do progresso da Sprint.
- Como facilita o aprendizado: Ajuda na análise de desempenho da equipe.
Trello (https://trello.com) — opcional

- Para que serve: Gestão digital do backlog e Sprint.
- Por que é adequada ao tema: Ferramenta amplamente utilizada em ambientes ágeis.
- Como facilita o aprendizado: Permite atualização colaborativa das tarefas.

##### 3. Checklist Inicial

Antes de iniciar a prática, o estudante deve ter:

- Papel, cartões ou post-its
- Caneta ou marcador
- Quadro ou superfície para organização
- Computador ou celular com internet (opcional)
- Planilha digital (opcional)
- Espaço para trabalho em grupo
- Acesso ao material da aula

##### 4. Passo a Passo do Docente (Aula de até 50 minutos)

###### Como conduzir a aula

- Retome a aula anterior sobre entregáveis em Scrum.
- Apresente os três conceitos centrais da aula:
- Reunião Diária (Daily Scrum)
- Refinamento do Produto (Backlog Refinement)
- Gráfico Burndown
- Explique o objetivo das reuniões diárias:
- Compartilhar progresso
- Identificar impedimentos
- Organizar o trabalho do dia
- Explique como ocorre o refinamento do backlog.
- Demonstre o funcionamento de um gráfico Burndown simples.
- Apresente o cenário da aula: equipe acompanhando uma Sprint de desenvolvimento.
- Explique a atividade prática.

###### Preparações necessárias

- Organizar materiais para trabalho em grupo
- Preparar modelo simples de quadro Kanban
- Disponibilizar modelo simples de gráfico Burndown (manual ou digital)

###### Alertas e pontos de atenção

- Alunos podem transformar a Daily em reunião longa
- Reforce o limite curto das reuniões Scrum
- Oriente para foco em objetividade
- Evite backlog excessivamente detalhado

###### Dinâmica sugerida

Daily Scrum → refinamento → atualização do Burndown → análise

###### Gerenciamento de tempo (50 minutos)

- Introdução e explicação: 15 minutos
- Simulação da Daily Scrum: 10 minutos
- Refinamento do backlog: 10 minutos
- Construção/análise do Burndown: 10 minutos
- Reflexão final: 5 minutos

##### 5. Atividade Prática — Descrição Geral

Os estudantes deverão simular o acompanhamento de uma Sprint Scrum utilizando Daily Scrum, refinamento do backlog e gráfico Burndown.

Cada equipe irá:

- Organizar tarefas da Sprint
- Realizar uma reunião diária
- Refinar itens do backlog
- Atualizar um gráfico Burndown simples
A atividade simula o acompanhamento contínuo de entregas em projetos ágeis reais.

A habilidade desenvolvida será a capacidade de monitorar progresso, organizar entregas e adaptar o planejamento em Scrum.

##### 6. Metodologia Ativa Utilizada

- Aprendizagem baseada em projetos (PBL)
- Simulação profissional
- Aprendizagem colaborativa
Elementos de Lemov aplicados:

- Objetivo claro
- Produção visível
- Participação ativa
- Feedback contínuo

##### 7. Passo a Passo da Atividade Prática (para os alunos)

- Formem equipes de 3 a 5 integrantes.
- Escolham um projeto simples (ex.: aplicativo escolar, sistema financeiro ou agenda de tarefas).
- Criem um conjunto inicial de tarefas para a Sprint.
- Organizem as tarefas no quadro:
- A fazer
- Em andamento
- Concluído
- Simulem uma Daily Scrum respondendo:
- O que fiz ontem?
- O que farei hoje?
- Existe algum impedimento?
- Revisem o backlog e identifiquem ajustes necessários.
- Atualizem o quadro conforme o progresso da equipe.
- Criem um gráfico Burndown simples registrando:
- Trabalho ideal
- Trabalho realizado
- Preparem uma apresentação explicando o acompanhamento da Sprint.

##### 8. Exemplo ou Demonstração

Exemplo — Projeto: Aplicativo Escolar

Sprint Backlog:

- Criar login
- Cadastro de usuários
- Lista de tarefas
Daily Scrum:

Aluno A:

- Finalizou login
- Vai iniciar cadastro
- Sem impedimentos
Aluno B:

- Trabalhando na lista de tarefas
- Encontrou dificuldade técnica
Burndown:

Dia 1 → 20 pontos restantes Dia 2 → 15 pontos restantes Dia 3 → 10 pontos restantes

##### 9. Resultado Esperado

O estudante deverá apresentar:

- Quadro da Sprint atualizado
- Simulação da Daily Scrum
- Backlog refinado
- Gráfico Burndown simples
O professor poderá verificar o aprendizado observando:

- Clareza na comunicação da equipe
- Organização das tarefas
- Coerência do acompanhamento da Sprint
- Compreensão do gráfico Burndown

##### 10. Formato de Entrega da Atividade

- Formato: Quadro físico, cartolina, planilha ou documento digital
- Registro: Foto, print ou arquivo digital
- Nome do arquivo (se necessário): EntregasScrum_NomeGrupo
- Local de entrega: Em sala ou via plataforma digital
- Prazo sugerido: Durante a aula

##### 11. Encerramento e Reflexão

Finalize conduzindo uma reflexão orientada:

- Como as reuniões diárias ajudam no andamento do projeto?
- O refinamento do backlog melhorou a organização da Sprint?
- O gráfico Burndown facilitou a visualização do progresso?
