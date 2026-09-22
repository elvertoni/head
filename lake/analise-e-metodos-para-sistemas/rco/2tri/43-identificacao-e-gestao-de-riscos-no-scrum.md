---
titulo: "Identificação e Gestão de Riscos no Scrum"
tipo: rco-seed
disciplina: analise-e-metodos-para-sistemas
sigla_rco: AMS
trimestre: 2
ordem_rco: 43
serie: 1
aula_rco: "Aula 43"
slides: 24
tem_atividade: true
tem_pratica: true
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/AMS/2TRI/43-identificacao-e-gestao-de-riscos-no-scrum/43-identificacao-e-gestao-de-riscos-no-scrum.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/AMS/2TRI/43-identificacao-e-gestao-de-riscos-no-scrum/AULA 43_ATIVIDADE_ANÁLISE E MÉTODO PARA SISTEMAS.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/AMS/2TRI/43-identificacao-e-gestao-de-riscos-no-scrum/AULA 43_PRÁTICA_ANÁLISE E MÉTODO PARA SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Identificação e Gestão de Riscos no Scrum

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- ANÁLISE E MÉTODO PARA SISTEMAS
- 1ª Série
- Identificação e Gestão de Riscos no Scrum
- Aula 43

_1 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- COMPETÊNCIA(S) A SER(EM) DESENVOLVIDA(S) NESTA AULA:
- De acordo com o Plano de Curso de Desenvolvimento de Sistemas:
- HABILIDADE(S) A SER(EM) DESENVOLVIDA(S) NESTA AULA:
- Executar alterações e manutenções em aplicações e rotinas de acordo com as definições estabelecidas.
- Manter registros para análise e refinamento de resultados.

_1 imagem(ns) no slide._

### Slide 4

- Nesta aula vamos:
- Aprender como é feito o gerenciamento de riscos de um projeto em Scrum.
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
- Aprendemos como é feito a decomposição das atividades em Scrum.

_1 imagem(ns) no slide._

### Slide 7

- Para pensarmos juntos...
- Lucas, um desenvolvedor de software recém-formado, acabou de entrar para a equipe de desenvolvimento de uma startup de tecnologia. Eles usam o Scrum como framework de gerenciamento de projetos. Em sua primeira Sprint Planning, Lucas percebeu que nenhum membro da equipe discutiu sobre os possíveis riscos associados ao projeto. Embora Lucas seja novo na área, ele entende que o gerenciamento de riscos é uma parte crucial de qualquer projeto.

### Slide 8

- Para pensarmos juntos...
- Lucas, então, questiona o Scrum Master, "Como o Scrum lida com o gerenciamento de riscos? Devemos discutir sobre isso durante o Sprint Planning?"
- Conversem e apresentem suas visões!!

_2 imagem(ns) no slide._

### Slide 9

- Resposta
- O Scrum Master explica que, no Scrum, o gerenciamento de riscos está embutido no próprio processo. A realização de Sprints curtas permite que a equipe inspecione e se adapte regularmente, o que significa que os riscos podem ser identificados e tratados mais rapidamente. Além disso, o Product Owner é responsável por gerenciar riscos relacionados ao Product Backlog, priorizando itens que reduzem incertezas significativas ou que são de alto risco. Contudo, o Scrum Master concorda que a discussão explícita sobre riscos durante o Sprint Planning pode ser benéfica para garantir que toda a equipe esteja ciente e preparada para lidar com possíveis problemas.

### Slide 10

- Conceituando
- O gerenciamento de riscos é uma parte vital do desenvolvimento de software e, no Scrum, é tratado de uma maneira um pouco diferente dos métodos tradicionais. No contexto do Scrum, um risco é qualquer coisa que possa afetar negativamente o progresso do projeto ou a qualidade do produto.
- https://uploads-ssl.webflow.com/6399c61683700ed8ab159d36/639fb82ee9b4747e103aa877_Base-imagem-destacada-blog.png

_1 imagem(ns) no slide._

### Slide 11

- Impactos positivos do Scrum no planejamento de projetos
- No Scrum, a estrutura de Sprints curtas e iterativas auxilia naturalmente no gerenciamento de riscos. Cada Sprint oferece a oportunidade de inspecionar o progresso do projeto e se adaptar a quaisquer mudanças ou problemas emergentes. Isso significa que os riscos podem ser identificados e tratados mais rapidamente do que em modelos de desenvolvimento mais tradicionais.

_1 imagem(ns) no slide._

### Slide 12

- Impactos negativos e desafios na utilização do Scrum
- O Product Owner, um dos três papéis principais no Scrum, também desempenha um papel importante no gerenciamento de riscos. Eles são responsáveis por gerenciar o Product Backlog, que é a lista de todas as tarefas ou "histórias" que precisam ser concluídas para o projeto. Isso inclui a priorização de tarefas que podem reduzir a incerteza ou que são de alto risco.

_1 imagem(ns) no slide._

### Slide 13

- Resumo
- Além disso, a equipe Scrum como um todo é incentivada a estar ciente dos riscos e a trazer à tona quaisquer preocupações durante as reuniões de Scrum, como a Sprint Planning e a Sprint Retrospective. Isso garante que todos na equipe estejam envolvidos no gerenciamento de riscos e que quaisquer problemas possam ser abordados rapidamente.

_1 imagem(ns) no slide._

### Slide 14

- Impactos negativos e desafios na utilização do Scrum
- Em resumo, o gerenciamento de riscos no Scrum é um esforço colaborativo que está integrado ao próprio processo. Ele promove a identificação rápida de riscos e a tomada de ações imediatas, ajudando a manter o projeto no caminho certo.

_1 imagem(ns) no slide._

### Slide 15

- Ao longo das atividades, você vai encontrar alguns quizzes e eles não estão ali por acaso! Eles são oportunidades rápidas para testar seu entendimento, reforçar o que aprendeu e identificar pontos que ainda podem melhorar.
- Atividade Prática na Plataforma Alura
- Na plataforma Alura vamos acessar o seguinte curso:
- Link para o curso: https://cursos.alura.com.br/course/scrum-parte-4

_3 imagem(ns) no slide._

### Slide 16

- Riscos Scrum
- 12 minutos
- O Risco é um evento incerto, porém quantificável. O Risco pode afetar os objetivos de um projeto e também contribuir para seu sucesso ou fracasso.
- Link para tarefa: https://cursos.alura.com.br/course/scrum-parte-4/task/22415
- Risco pode ser assumido como algo positivo ou negativo, mas ele não deve ser considerado um problema, já que o problema é uma situação com certezas bem definidas, que estão acontecendo atualmente no projeto.
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 17

- Técnicas de identificação de riscos
- 17 minutos
- Nesta aula trabalharemos com técnicas para identificar os riscos.
- Link para tarefa: https://cursos.alura.com.br/course/scrum-parte-4/task/22416
- De maneira a controlá-los evitando maiores perdas. Abaixo são elencadas algumas atitudes para alcançar esses objetivos.
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 18

- Hora de praticar!
- Formação de Equipes: Divida os participantes em pequenas equipes de 3 a 5 pessoas, representando equipes Scrum.
- Definição do Projeto: Cada equipe recebe a descrição de um projeto fictício. Isso pode ser algo como "criar um novo aplicativo de mídia social" ou "desenvolver um sistema de gerenciamento de estoque para uma loja online".
- Identificação de Riscos: Peça para cada equipe passar alguns minutos identificando potenciais riscos que poderiam surgir durante a execução do projeto. Eles devem escrever cada risco em um cartão de índice.
- Troque ideias com seus colegas!

_2 imagem(ns) no slide._

> **Notas do apresentador:** Dinâmica: Gerenciando Riscos com Scrum Objetivo: Compreender e praticar a identificação, priorização e mitigação de riscos em um ambiente Scrum. Materiais necessários: Cartões de índice, canetas, quadro branco ou flip chart.

### Slide 19

- Hora de praticar!
- Priorização de Riscos: As equipes devem, então, priorizar os riscos identificados, considerando a probabilidade de ocorrência e o impacto potencial no projeto.
- Mitigação de Riscos: Em seguida, cada equipe deve desenvolver um plano para mitigar os riscos mais importantes. Elas devem considerar quais ações poderiam ser tomadas para reduzir a probabilidade do risco ou para minimizar o impacto caso o risco se concretize.
- Apresentação: Cada equipe deve, então, apresentar seus riscos prioritários e planos de mitigação para o grupo inteiro. Isto pode ser seguido por uma discussão sobre as diferentes abordagens para o gerenciamento de riscos.

_1 imagem(ns) no slide._

> **Notas do apresentador:** Dinâmica: Scrum Puzzle Objetivo: Familiarizar os participantes com a decomposição do Scrum e o Sprint Backlog, ajudando-os a entender como as histórias de usuário são divididas em tarefas menores e como isso se relaciona com o planejamento de uma sprint. Materiais: Papel, canetas, cartões de índice ou post-its.

### Slide 20

- Vamos praticar?
- Prepare-se, porque nessa atividade, você vai sair do modo aprender e entrar direto no modo praticar.
- A atividade prática vai colocar você diante de um desafio real: sensação de ver seu próprio código aparecer online! Acessível, documentado e pronto para o mundo!

_1 imagem(ns) no slide._

### Slide 21

- O que vimos na aula de hoje:
- Compreendemos a importância do gerenciamento de riscos com a ferramenta Scrum.

_1 imagem(ns) no slide._

### Slide 22

- Pronto para desbloquear sua carreira de TI?
- Está perdido estudando mas não sabe por onde começar? Se a resposta é sim, você está no lugar certo! Descubra as estratégias e ferramentas essenciais para te ajudar a desbloquear seu potencial em TI e buscar sua primeira vaga de emprego no setor!
- Este e-book é um guia completo para quem busca começar pelos melhores caminhos para se tornar um excelente profissional de TI, ensinando a identificar perfis profissionais, aplicar técnicas de estudo eficazes, transformar teoria em prática, e aumentar a visibilidade de seu trabalho no mercado de trabalho. Ideal para novatos e profissionais em transição.
- E o melhor, ele pode ser seu, inteiramente grátis!
- Basta clicar AQUI e realizar o seu cadastro com o seu @escola!

_3 imagem(ns) no slide._

### Slide 23

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

### Slide 24

_(sem texto)_

## Atividade

_Fonte: AULA 43_ATIVIDADE_ANÁLISE E MÉTODO PARA SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

ANÁLISE E MÉTODO PARA SISTEMAS

1ª SÉRIE

ATIVIDADE AULA 43

Questão 1

No Scrum, qual é a melhor maneira de lidar com os riscos do projeto?

a) Ignorar os riscos até que eles realmente aconteçam.

b) Identificar os riscos no início do projeto e depois esquecê-los.

c) Identificar, priorizar e mitigar os riscos de forma contínua durante todo o projeto.

d) Apenas o Scrum Master deve lidar com os riscos.

Resposta correta: c) Identificar, priorizar e mitigar os riscos de forma contínua durante todo o projeto.

Comentário: Em Scrum, o gerenciamento de riscos é um processo contínuo. Os riscos devem ser identificados, priorizados e mitigados ao longo do projeto, e todos os membros da equipe devem estar envolvidos nesse processo.

Questão 2

No contexto do Scrum, o que significa mitigar um risco?

a) Ignorar o risco.

b) Tomar medidas para reduzir a probabilidade do risco ou minimizar o impacto caso ele ocorra.

c) Aumentar a probabilidade de o risco ocorrer.

d) Transferir o risco para outra equipe.

Resposta correta: b) Tomar medidas para reduzir a probabilidade do risco ou minimizar o impacto caso ele ocorra.

Comentário: Mitigar um risco significa tomar medidas para reduzir a probabilidade de o risco ocorrer ou para minimizar o impacto caso ele se concretize. Isso pode envolver várias estratégias, dependendo do risco específico.

## Prática

_Fonte: AULA 43_PRÁTICA_ANÁLISE E MÉTODO PARA SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

ANÁLISE E MÉTODO PARA SISTEMAS

1ª SÉRIE

ATIVIDADE PRÁTICA AULA 43

##### 1. Objetivo da Aula Prática

Ao final desta aula prática, o estudante deverá:

- Aprender como o Scrum realiza a identificação e o gerenciamento de riscos em projetos.
- Desenvolver a habilidade prática de identificar riscos, avaliar impactos e propor ações de mitigação.
- Ser capaz de aplicar técnicas simples de gerenciamento de riscos em cenários simulados de projetos Scrum.

##### 2. Ferramentas Recomendadas

Cartões de índice ou post-its

- Para que serve: Registro dos riscos identificados pela equipe.
- Por que é adequada ao tema: Permite organização rápida e visual dos riscos.
- Como facilita o aprendizado: Ajuda na priorização e análise colaborativa.
Quadro branco ou flip chart

- Para que serve: Organização visual dos riscos e planos de mitigação.
- Por que é adequada ao tema: Simula reuniões Scrum reais.
- Como facilita o aprendizado: Facilita análise coletiva dos impactos.
Planilhas Google ou Google Docs

- Para que serve: Registro digital dos riscos e estratégias.
- Por que é adequada ao tema: Facilita documentação e acompanhamento.
- Como facilita o aprendizado: Ajuda a estruturar o raciocínio da equipe.
Trello (https://trello.com) — opcional

- Para que serve: Organização das tarefas e riscos do projeto.
- Por que é adequada ao tema: Ferramenta utilizada em ambientes ágeis reais.
- Como facilita o aprendizado: Permite visualizar riscos por prioridade.

##### 3. Checklist Inicial

Antes de iniciar a prática, o estudante deve ter:

- Papel, cartões ou post-its
- Caneta ou marcador
- Quadro ou superfície para organização
- Computador ou celular com internet (opcional)
- Espaço para trabalho em grupo
- Acesso ao material da aula

##### 4. Passo a Passo do Docente (Aula de até 50 minutos)

###### Como conduzir a aula

- Retome a aula anterior sobre decomposição das atividades em Scrum.
- Apresente o tema da aula: identificação e gestão de riscos no Scrum.
- Explique os conceitos abordados no material:
- Risco em projetos
- Probabilidade e impacto
- Mitigação de riscos
- Product Backlog
- Sprint Planning
- Inspeção e adaptação
- Apresente o cenário da aula: Lucas questionando como o Scrum trata riscos.
- Explique que o gerenciamento de riscos está integrado ao próprio framework Scrum.
- Destaque a importância das Sprints curtas para identificação rápida de problemas.
- Explique a dinâmica prática.

###### Preparações necessárias

- Separar cartões e materiais
- Organizar as equipes
- Definir exemplos de projetos fictícios
- Preparar espaço para apresentações

###### Alertas e pontos de atenção

- Alunos podem confundir risco com problema já existente
- Reforce que risco é algo incerto que pode acontecer
- Incentive pensamento estratégico
- Oriente para análise de impacto e probabilidade

###### Dinâmica sugerida

Identificação → priorização → mitigação → apresentação

###### Gerenciamento de tempo (50 minutos)

- Introdução e explicação: 15 minutos
- Identificação e priorização dos riscos: 15 minutos
- Construção do plano de mitigação: 10 minutos
- Apresentação e reflexão: 10 minutos

##### 5. Atividade Prática — Descrição Geral

Os estudantes deverão simular o gerenciamento de riscos em um projeto Scrum fictício.

Cada equipe irá:

- Receber um cenário de projeto
- Identificar riscos possíveis
- Priorizar os riscos considerando impacto e probabilidade
- Criar estratégias de mitigação
A atividade simula situações reais enfrentadas em projetos de desenvolvimento de software.

A habilidade desenvolvida será a capacidade de antecipar problemas, avaliar riscos e criar estratégias preventivas em ambientes ágeis.

##### 6. Metodologia Ativa Utilizada

- Aprendizagem baseada em problemas (PBL)
- Simulação profissional
- Aprendizagem colaborativa
- Análise de cenários
Elementos de Lemov aplicados:

- Objetivo claro
- Produção visível
- Participação ativa
- Pensamento crítico
- Feedback contínuo

##### 7. Passo a Passo da Atividade Prática (para os alunos)

- Formem equipes de 3 a 5 integrantes.
- Recebam a descrição de um projeto fictício.
- Leiam o cenário apresentado pela equipe/professor.
- Identifiquem possíveis riscos do projeto.
- Registrem cada risco em um cartão ou post-it.
- Classifiquem os riscos considerando:
- Probabilidade de ocorrência
- Impacto no projeto
- Organizem os riscos do mais crítico para o menos crítico.
- Criem estratégias para reduzir ou minimizar os riscos principais.
- Organizem as informações no quadro ou documento digital.
- Preparem uma apresentação explicando os riscos e as soluções propostas.

##### 8. Exemplo ou Demonstração

Exemplo — Projeto: Aplicativo de mídia social

Riscos identificados:

- Atraso no desenvolvimento
- Falta de comunicação da equipe
- Mudanças frequentes de requisitos
- Problemas de integração
Priorização:

| Risco | Probabilidade | Impacto |
| --- | --- | --- |
| Mudança de requisitos | Alta | Alto |
| Falta de comunicação | Média | Alto |
| Problemas técnicos | Média | Médio |

Mitigações:

- Reuniões frequentes
- Revisão constante do backlog
- Divisão clara de tarefas

##### 9. Resultado Esperado

O estudante deverá apresentar:

- Lista organizada de riscos
- Priorização coerente
- Estratégias de mitigação definidas
- Análise básica de impacto e probabilidade
O professor poderá verificar o aprendizado observando:

- Clareza na identificação dos riscos
- Capacidade de análise crítica
- Qualidade das soluções propostas
- Participação da equipe

##### 10. Formato de Entrega da Atividade

- Formato: Quadro físico, cartolina ou documento digital
- Registro: Foto, print ou arquivo digital
- Nome do arquivo (se necessário): GestaoRiscosScrum_NomeGrupo
- Local de entrega: Em sala ou via plataforma digital
- Prazo sugerido: Durante a aula

##### 11. Encerramento e Reflexão

Finalize conduzindo uma reflexão orientada:

- Por que identificar riscos antecipadamente é importante?
- O Scrum ajuda a reduzir riscos? Como?
- Qual foi o risco mais difícil de analisar?
