---
titulo: "Gerenciamento de Mudanças em Projetos Ágeis"
tipo: rco-seed
disciplina: analise-e-metodos-para-sistemas
sigla_rco: AMS
trimestre: 2
ordem_rco: 48
serie: 1
aula_rco: "Aula 48"
slides: 23
tem_atividade: true
tem_pratica: true
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/AMS/2TRI/48-gerenciamento-de-mudancas-em-projetos-ageis/48-gerenciamento-de-mudancas-em-projetos-ageis.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/AMS/2TRI/48-gerenciamento-de-mudancas-em-projetos-ageis/AULA 48_ATIVIDADE_ANÁLISE E MÉTODO PARA SISTEMAS.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/AMS/2TRI/48-gerenciamento-de-mudancas-em-projetos-ageis/AULA 48_PRÁTICA_ANÁLISE E MÉTODO PARA SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Gerenciamento de Mudanças em Projetos Ágeis

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- ANÁLISE E MÉTODO PARA SISTEMAS
- 1ª Série
- Gerenciamento de Mudanças em Projetos Ágeis
- Aula 48

_1 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- COMPETÊNCIA(S) A SER(EM) DESENVOLVIDA(S) NESTA AULA:
- De acordo com o Plano de Curso de Desenvolvimento de Sistemas:
- HABILIDADE(S) A SER(EM) DESENVOLVIDA(S) NESTA AULA:
- Executar alterações e manutenções em aplicações e rotinas de acordo com as definições estabelecidas.
- Executar manutenção de programas de computador e suporte técnico.

_1 imagem(ns) no slide._

### Slide 4

- Nesta aula vamos:
- Compreender o gerenciamento de mudanças com Ágil.
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
- Conhecemos quais são os papéis que são utilizados pela ferramenta Scrum.

_1 imagem(ns) no slide._

### Slide 7

- Para pensarmos juntos...
- Tiago foi contratado em uma empresa de tecnologia para gerenciar o desenvolvimento de um novo software de gerenciamento de recursos. No entanto, durante o projeto, a empresa recebeu um feedback significativo dos futuros usuários sobre algumas funcionalidades importantes que gostariam de ver incorporadas no software. Tiago, sendo novo na empresa e inexperiente na aplicação da metodologia ágil, sente-se um pouco perdido. Ele não sabe como implementar essas mudanças no meio do projeto sem causar grandes atrasos ou ultrapassar o orçamento.

_1 imagem(ns) no slide._

### Slide 8

- Para pensarmos juntos...
- Como Tiago pode implementar as mudanças sugeridas sem interromper o andamento do projeto utilizando a metodologia ágil?
- Conversem e apresentem suas visões

_2 imagem(ns) no slide._

### Slide 9

- Resposta
- Utilizando a metodologia ágil, Tiago pode abordar essas mudanças sugeridas de forma iterativa e incremental. Ele não precisa implementar todas as mudanças de uma vez. Em vez disso, ele pode priorizar as mudanças com base na sua importância para os usuários e no esforço necessário para implementá-las. Cada mudança pode ser tratada como um item do backlog do produto a ser trabalhado em futuros sprints.

_1 imagem(ns) no slide._

### Slide 10

- Resposta
- Dessa forma, Tiago pode gerenciar as mudanças de maneira eficaz sem interromper o fluxo de trabalho existente ou ultrapassar o orçamento. Além disso, as reuniões regulares de revisão e retrospectiva ajudarão a equipe a se adaptar e melhorar constantemente.

_1 imagem(ns) no slide._

### Slide 11

- Conceituando
- O gerenciamento de mudanças é uma parte crucial de qualquer projeto, especialmente quando falamos de desenvolvimento de software. Dentro da metodologia ágil, o gerenciamento de mudanças tem um enfoque especial e é um componente fundamental de sua filosofia.

_1 imagem(ns) no slide._

### Slide 12

- Conceituando
- A metodologia ágil valoriza a capacidade de responder às mudanças mais do que seguir um plano rigoroso. Isto é, em vez de resistir às mudanças, as metodologias ágeis acolhem-nas como uma oportunidade de melhorar o produto e de melhor atender às necessidades do usuário. Elas reconhecem que as necessidades dos usuários, o mercado e a tecnologia podem mudar rapidamente e, portanto, o desenvolvimento de software deve ser capaz de se adaptar igualmente rápido.
- https://www.neomind.com.br/wp-content/uploads/2020/01/pratica2.png

_1 imagem(ns) no slide._

### Slide 13

- Conceituando
- No gerenciamento ágil de mudanças, a flexibilidade é fundamental. Em vez de longos ciclos de planejamento e desenvolvimento, o trabalho é dividido em pequenas partes chamadas sprints, geralmente de duas semanas. Ao final de cada sprint, a equipe revisa o trabalho realizado, reflete sobre o que pode ser melhorado e se ajusta conforme necessário para o próximo sprint. Esta abordagem permite que a equipe responda rapidamente às mudanças.
- https://uploads-ssl.webflow.com/6399c61683700ed8ab159d36/639fb82ee9b4747e103aa877_Base-imagem-destacada-blog.png

_1 imagem(ns) no slide._

### Slide 14

- Conceituando
- Além disso, a comunicação constante e a colaboração também são importantes no gerenciamento de mudanças ágil. A equipe de desenvolvimento, o proprietário do produto (Product Owner) e as partes interessadas se reúnem regularmente para discutir o progresso, as preocupações e as mudanças propostas. Este feedback contínuo permite que a equipe ajuste o curso conforme necessário, melhorando assim a capacidade de gerenciar a mudança.
- http://s2.glbimg.com/qZnvqfl-n5LE6OIe8jpoog3JpIc=/e.glbimg.com/og/ed/f/original/2015/08/19/vida_pessoal_trabalho_equilibrio_empreendedor.jpg

_1 imagem(ns) no slide._

### Slide 15

- Resumo
- Em resumo, o gerenciamento de mudanças na metodologia ágil é um processo contínuo e flexível que acolhe a mudança, em vez de resistir a ela. Ele incentiva a colaboração, a comunicação e a capacidade de resposta para melhorar constantemente o produto e atender às necessidades dos usuários.
- https://uploads-ssl.webflow.com/6399c61683700ed8ab159d36/639fb82ee9b4747e103aa877_Base-imagem-destacada-blog.png

_1 imagem(ns) no slide._

### Slide 16

- Link para o curso: https://cursos.alura.com.br/course/scrum-parte-5
- Ao longo das atividades, você vai encontrar alguns quizzes e eles não estão ali por acaso! Eles são oportunidades rápidas para testar seu entendimento, reforçar o que aprendeu e identificar pontos que ainda podem melhorar.
- Atividade Prática na Plataforma Alura
- Na plataforma Alura vamos acessar o seguinte curso:

_3 imagem(ns) no slide._

### Slide 17

- Mudanças parte 1
- 11 minutos
- O Time Scrum deve compreender que processos de desenvolvimento Scrum são projetados para aceitarem mudanças.
- Link para tarefa: https://cursos.alura.com.br/course/scrum-parte-5/task/22459
- Sem que elas causem grandes problemas para a equipe, já que o projeto é dividido dentro das Sprints e as mudanças podem ocorrer após uma entrega e antes da próxima.
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 18

- Mudanças parte 2
- 10 minutos
- A flexibilidade é uma importante característica.
- Link para tarefa: https://cursos.alura.com.br/course/scrum-parte-5/task/22460
- O Backlog do Produto permite a incorporação de modificações e a adição de novos requisitos, quando necessário, e isso ocorre por meio da integração contínua. O Time Scrum pode incorporar funcionalidades novas e modificadas nas entregas.
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 19

- O que vimos na aula de hoje:
- Aprendemos o gerenciamento de mudanças no ágil.

_1 imagem(ns) no slide._

### Slide 20

- Vamos praticar?
- Prepare-se, porque nessa atividade, você vai sair do modo aprender e entrar direto no modo praticar.
- A atividade prática vai colocar você diante de um desafio real: sensação de ver seu próprio código aparecer online! Acessível, documentado e pronto para o mundo!

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

_Fonte: AULA 48_ATIVIDADE_ANÁLISE E MÉTODO PARA SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

ANÁLISE E MÉTODO PARA SISTEMAS

1ª SÉRIE

ATIVIDADE AULA 48

Questão 1

No gerenciamento de mudanças no Ágil, o que normalmente é feito quando uma nova funcionalidade é sugerida no meio do desenvolvimento do projeto?

A) A nova funcionalidade é imediatamente adicionada ao produto em desenvolvimento.

B) A mudança é recusada, pois o escopo do projeto já foi definido.

C) A nova funcionalidade é avaliada e, se aprovada, é adicionada ao backlog do produto para ser trabalhada em futuros sprints.

D) O projeto é interrompido até que a nova funcionalidade seja completamente desenvolvida e testada.

Resposta correta: C. No gerenciamento ágil de mudanças, a mudança é vista como algo natural e é bem-vinda. Quando uma nova funcionalidade é sugerida, ela é avaliada e, se for considerada valiosa, é adicionada ao backlog do produto. Posteriormente, ela será trabalhada em um dos próximos sprints, não interrompendo o trabalho atual.

Questão 2

Qual é a melhor prática no gerenciamento ágil de mudanças quando surge uma nova mudança que impactará significativamente o escopo do projeto?

A) Ignorar a mudança, pois é importante manter o escopo original do projeto.

B) Parar todo o desenvolvimento até que a mudança seja completamente implementada.

C) Priorizar a mudança e começar a trabalhar nela imediatamente, mesmo que outras tarefas tenham que ser postergadas.

D) Avaliar o impacto da mudança, discuti-la com a equipe e stakeholders, e, se aceita, incorporá-la no planejamento dos próximos sprints.

Resposta correta: D. Em um ambiente ágil, é importante avaliar completamente o impacto das mudanças e comunicá-las a todos os interessados. Se a mudança for aceita, ela será incorporada no planejamento dos próximos sprints. A flexibilidade é uma característica chave da metodologia ágil, mas é sempre importante manter uma comunicação aberta e clara com todos os envolvidos.

## Prática

_Fonte: AULA 48_PRÁTICA_ANÁLISE E MÉTODO PARA SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

ANÁLISE E MÉTODO PARA SISTEMAS

1ª SÉRIE

ATIVIDADE PRÁTICA AULA 48

#### 1. Objetivo da Aula Prática

Ao final desta aula prática, o estudante deverá:

- Compreender como as metodologias ágeis lidam com mudanças durante o desenvolvimento de projetos.
- Desenvolver a habilidade de analisar solicitações de mudança e priorizá-las dentro de um Product Backlog.
- Ser capaz de propor adaptações em um projeto sem interromper o andamento da Sprint atual.
- Entender a importância da comunicação, colaboração e feedback contínuo no gerenciamento de mudanças ágil.

#### 2. Ferramentas Recomendadas

###### Post-its ou Cartões de Papel

Para que serve: Registrar funcionalidades, mudanças solicitadas e prioridades.

Por que é adequada ao tema: Permite reorganizar rapidamente requisitos e simular alterações no backlog.

Como facilita o aprendizado: Torna visível o processo de adaptação contínua do Scrum.

###### Quadro Branco ou Cartolina

Para que serve: Organizar Product Backlog, Sprint Atual e Próximas Sprints.

Por que é adequada ao tema: Facilita a visualização das mudanças no projeto.

Como facilita o aprendizado: Ajuda os estudantes a compreenderem o impacto das alterações.

###### Trello (Opcional)

Para que serve: Simular um Product Backlog digital.

Por que é adequada ao tema: É uma ferramenta amplamente utilizada em projetos ágeis.

Como facilita o aprendizado: Permite reorganizar tarefas rapidamente durante a atividade.

###### Google Planilhas

Para que serve: Registrar solicitações de mudança e suas prioridades.

Por que é adequada ao tema: Ajuda na documentação das decisões tomadas.

Como facilita o aprendizado: Permite acompanhar as alterações realizadas ao longo da dinâmica.

#### 3. Checklist Inicial

Antes de iniciar a prática, os estudantes devem possuir:

- Papel ou post-its
- Canetas ou marcadores
- Quadro ou cartolina
- Computador ou celular (opcional)
- Acesso ao conteúdo da aula
- Equipes organizadas entre 3 e 5 integrantes
- Espaço para discussão em grupo

#### 4. Passo a Passo do Docente (Aula de até 50 minutos)

##### Como conduzir a aula

- Retome o conceito de Scrum estudado nas aulas anteriores.
- Explique o conceito de gerenciamento de mudanças em projetos ágeis.
- Apresente o cenário de Tiago descrito na aula.
- Mostre como mudanças podem ser adicionadas ao Product Backlog.
- Explique que mudanças normalmente são incorporadas em futuras Sprints.
- Organize os grupos.
- Apresente a atividade prática.

##### Preparações necessárias

- Separar os materiais da dinâmica.
- Preparar os cenários de mudança.
- Organizar os grupos.
- Disponibilizar quadro ou cartolina para cada equipe.

##### Alertas e pontos de atenção

- Os alunos podem querer alterar toda a Sprint atual.
- Reforce que mudanças são avaliadas e priorizadas.
- Incentive a análise de impacto antes de aceitar uma alteração.
- Oriente para decisões colaborativas.

##### Dinâmica sugerida

Planejamento Inicial → Recebimento de Mudanças → Replanejamento → Apresentação

##### Gerenciamento de Tempo

| Etapa | Tempo |
| --- | --- |
| Revisão do conteúdo | 10 min |
| Explicação da atividade | 5 min |
| Planejamento inicial | 10 min |
| Inclusão das mudanças | 15 min |
| Apresentações | 5 min |
| Reflexão final | 5 min |

Total: 50 minutos

#### 5. Atividade Prática — Descrição Geral

Os estudantes deverão simular o gerenciamento de mudanças em um projeto ágil.

Cada equipe receberá um projeto fictício contendo funcionalidades já planejadas.

Durante a atividade, o professor entregará novas solicitações de mudança que deverão ser analisadas pela equipe.

Os estudantes precisarão:

- Avaliar o impacto da mudança.
- Decidir se a alteração será realizada imediatamente ou em Sprint futura.
- Atualizar o Product Backlog.
- Justificar suas decisões.
A atividade simula situações reais enfrentadas por equipes Scrum.

#### 6. Metodologia Ativa Utilizada

###### Aprendizagem Baseada em Problemas (PBL)

Os estudantes resolvem um problema real de gerenciamento de mudanças.

###### Simulação Profissional

A atividade reproduz situações comuns em equipes ágeis.

###### Aprendizagem Colaborativa

As decisões são tomadas coletivamente.

###### Elementos de Lemov Aplicados

- Objetivo Claro
- Produção Visível
- Participação Ativa
- Discussão Estruturada
- Feedback Imediato

#### 7. Passo a Passo da Atividade Prática (para os alunos)

###### Cenário

Uma equipe está desenvolvendo um aplicativo de gerenciamento financeiro pessoal.

###### Etapa 1 – Planejamento Inicial

- Formem grupos de 3 a 5 integrantes.
- Criem um Product Backlog inicial com pelo menos 6 funcionalidades.
Exemplo:

- Cadastro de usuários
- Login
- Registro de despesas
- Relatórios financeiros
- Notificações
- Perfil do usuário

###### Etapa 2 – Organização da Sprint

- Escolham 3 funcionalidades para a Sprint atual.

###### Etapa 3 – Mudanças Inesperadas

O professor entregará novas solicitações como:

- Adicionar autenticação por biometria.
- Criar modo escuro.
- Exportar relatórios para PDF.
- Adicionar metas financeiras.

###### Etapa 4 – Análise

- Avaliem cada mudança.
- Classifiquem como:
- Alta prioridade
- Média prioridade
- Baixa prioridade
- Decidam se a mudança entra:
- Na Sprint atual
- Na próxima Sprint
- No backlog futuro

###### Etapa 5 – Apresentação

- Apresentem as decisões tomadas e suas justificativas.

#### 8. Exemplo ou Demonstração

##### Product Backlog Inicial

| Prioridade | Funcionalidade |
| --- | --- |
| Alta | Cadastro |
| Alta | Login |
| Alta | Registro de despesas |
| Média | Relatórios |
| Média | Notificações |
| Baixa | Perfil |

##### Nova Solicitação

"Exportar relatórios para PDF"

###### Decisão

- Prioridade: Média
- Inserção: Próxima Sprint

###### Justificativa

A funcionalidade agrega valor, mas não impacta diretamente o funcionamento principal do sistema.

#### 9. Resultado Esperado

O estudante deverá apresentar:

- Product Backlog organizado.
- Mudanças analisadas.
- Prioridades definidas.
- Justificativas para cada decisão.
O professor poderá verificar o aprendizado observando:

- Compreensão do gerenciamento de mudanças.
- Capacidade de priorização.
- Coerência das decisões.
- Participação dos integrantes.

#### 10. Formato de Entrega da Atividade

###### O que deve ser entregue

- Cartolina, quadro ou documento digital contendo:
- Backlog inicial
- Mudanças recebidas
- Priorização realizada
- Decisões tomadas

###### Nome do arquivo

- MudancasAgil_Aula48_NomeGrupo

###### Local de entrega

- Sala de aula
- Plataforma utilizada pelo professor

###### Prazo sugerido

Ao final da aula.

#### 11. Encerramento e Reflexão

Conduza uma discussão com a turma utilizando as perguntas:

- Foi difícil decidir quais mudanças deveriam ser priorizadas?
- Como o Scrum ajuda a lidar com mudanças inesperadas?
- Todas as solicitações dos usuários devem ser implementadas imediatamente?
- Como o Product Backlog auxilia na organização das mudanças?
- O que aconteceria se a equipe aceitasse todas as mudanças sem planejamento?
