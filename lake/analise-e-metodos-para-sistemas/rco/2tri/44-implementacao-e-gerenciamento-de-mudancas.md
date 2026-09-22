---
titulo: "Implementação e Gerenciamento de Mudanças"
tipo: rco-seed
disciplina: analise-e-metodos-para-sistemas
sigla_rco: AMS
trimestre: 2
ordem_rco: 44
serie: 1
aula_rco: "Aula 44"
slides: 26
tem_atividade: true
tem_pratica: true
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/AMS/2TRI/44-implementacao-e-gerenciamento-de-mudancas/44-implementacao-e-gerenciamento-de-mudancas.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/AMS/2TRI/44-implementacao-e-gerenciamento-de-mudancas/AULA 44_ATIVIDADE_ANÁLISE E MÉTODO PARA SISTEMAS.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/AMS/2TRI/44-implementacao-e-gerenciamento-de-mudancas/AULA 44_PRÁTICA_ANÁLISE E MÉTODO PARA SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Implementação e Gerenciamento de Mudanças

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- ANÁLISE E MÉTODO PARA SISTEMAS
- 1ª Série
- Implementação e Gerenciamento de Mudanças
- Aula 44

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
- Aprender como é feito a implementação e o gerenciamento de mudanças em um projeto em Scrum.
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
- Conhecemos quais os riscos de um projeto e como é feito o gerenciamento desses riscos na ferramenta Scrum.

_1 imagem(ns) no slide._

### Slide 7

- Para pensarmos juntos...
- João está começando sua carreira como Scrum Master em uma empresa de desenvolvimento de software. Em um dos primeiros projetos que ele está liderando, houve uma mudança significativa nas necessidades do cliente, o que exigirá uma série de modificações no produto que está sendo desenvolvido. João está um pouco inseguro sobre como gerenciar essa situação sem prejudicar o fluxo de trabalho da equipe e sem comprometer a entrega do projeto no prazo estabelecido.

_1 imagem(ns) no slide._

### Slide 8

- Para pensarmos juntos...
- Como João, Scrum Master, deve gerenciar as mudanças de requisitos no meio de um Sprint sem afetar negativamente a produtividade da equipe e a entrega do projeto?
- Conversem e apresentem suas visões!!

_2 imagem(ns) no slide._

### Slide 9

- Resposta
- Mudanças durante um Sprint podem ser desafiadoras em Scrum, mas não impossíveis de gerenciar. A primeira coisa que João deve fazer é comunicar a mudança à equipe e ao Product Owner. No Scrum, qualquer mudança significativa no produto deve ser discutida e acordada por todos os membros da equipe.
- Em seguida, é importante que João e a equipe avaliem o impacto da mudança no Sprint atual. Se a mudança for muito grande e exigir muito trabalho adicional, pode ser necessário terminar o Sprint atual, realizar uma nova reunião de planejamento de Sprint (Sprint Planning) e começar um novo Sprint.

### Slide 10

- Resposta
- No entanto, se a mudança for pequena e a equipe acreditar que pode lidar com ela sem afetar o restante do trabalho do Sprint, eles podem simplesmente adicionar a nova tarefa ao Sprint Backlog.
- É importante lembrar que a flexibilidade é uma das principais vantagens do Scrum e que, com uma comunicação eficaz e um bom gerenciamento, é possível lidar com mudanças sem prejudicar o projeto.

### Slide 11

- Conceituando
- O Scrum é um framework ágil para gerenciamento de projetos que valoriza a adaptabilidade e a capacidade de resposta às mudanças. Essa filosofia é particularmente evidente na abordagem do Scrum para a implementação e o gerenciamento de mudanças.

_1 imagem(ns) no slide._

### Slide 12

- Impactos positivos do Scrum no planejamento de projetos
- No Scrum, as mudanças são vistas como oportunidades para melhorar o produto e atender melhor às necessidades do cliente. Em vez de tentar evitar ou resistir a mudanças, como ocorre em alguns métodos de gerenciamento de projetos mais tradicionais, o Scrum encoraja as equipes a acolher as mudanças e a se adaptar de acordo.
- https://www.neomind.com.br/wp-content/uploads/2020/01/pratica2.png

_1 imagem(ns) no slide._

### Slide 13

- Impactos negativos e desafios na utilização do Scrum
- Isso é realizado por meio de uma série de cerimônias e práticas do Scrum. Por exemplo, durante as reuniões de revisão de sprint, a equipe e o cliente discutem o trabalho realizado durante o sprint e identificam quaisquer mudanças necessárias. Em seguida, durante a reunião de planejamento do sprint, a equipe e o cliente concordam com as próximas tarefas a serem realizadas, levando em consideração quaisquer mudanças que foram identificadas.

_1 imagem(ns) no slide._

### Slide 14

- Resumo
- O Scrum também promove a transparência e a comunicação aberta, o que é fundamental para o gerenciamento eficaz de mudanças. Todos os membros da equipe devem estar cientes das mudanças e ter a oportunidade de discutir e entender suas implicações.

_1 imagem(ns) no slide._

### Slide 15

- Impactos negativos e desafios na utilização do Scrum
- No entanto, embora o Scrum seja projetado para ser adaptável, também reconhece a importância da estabilidade durante um sprint. Portanto, as mudanças que surgem durante um sprint são geralmente implementadas no próximo sprint, a menos que sejam tão críticas que justifiquem a interrupção do sprint atual. Isso permite que a equipe se concentre em completar o trabalho planejado para o sprint atual, enquanto ainda se prepara para se adaptar às mudanças no futuro.

_1 imagem(ns) no slide._

### Slide 16

- Link para o curso: https://cursos.alura.com.br/course/scrum-parte-5
- Ao longo das atividades, você vai encontrar alguns quizzes e eles não estão ali por acaso! Eles são oportunidades rápidas para testar seu entendimento, reforçar o que aprendeu e identificar pontos que ainda podem melhorar.
- Atividade Prática na Plataforma Alura
- Na plataforma Alura vamos acessar o seguinte curso:

_3 imagem(ns) no slide._

### Slide 17

- Iterativo incremental
- 7 minutos
- Vamos entender como funciona e como devemos fazer a Implementação e o gerenciamento de mudanças em Scrum.
- Link para tarefa: https://cursos.alura.com.br/course/scrum-parte-5/task/22452
- O risco pode ser assumido como algo positivo ou negativo, mas ele não deve ser considerado um problema, já que o problema é uma situação com certezas bem definidas, que estão acontecendo atualmente no projeto.
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 18

- Iterativo incremental
- 13 minutos
- O desenvolvimento iterativo permite a correção de curso na medida que o Time Scrum adquire um melhor entendimento.
- Link para tarefa: https://cursos.alura.com.br/course/scrum-parte-5/task/22453
- A iteração não deve ser confundida com interação, embora ela pressuponha interatividade, é mais do que isso, ela é a interatividade em momentos específicos.
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 19

- Hora de praticar!
- Divida o grupo em equipes de 3 a 5 pessoas.
- Cada equipe recebe uma pilha de cartões de índice e canetas.
- O objetivo é que cada equipe construa a maior torre possível com os cartões de índice em um período de 10 minutos.
- Troque ideias com seus colegas!

_2 imagem(ns) no slide._

> **Notas do apresentador:** Nome da Dinâmica: "O Vento Mudou" Objetivo: Essa atividade tem como objetivo ilustrar a necessidade de adaptabilidade em um ambiente Scrum, onde mudanças são uma constante. Materiais Necessários: Cartões de índice, canetas, um relógio ou timer.

### Slide 20

- Hora de praticar!
- OBSERVAÇÃO PARA O PROFESSOR:
- Quando as equipes começarem a construir suas torres, espere 3 minutos e então anuncie uma mudança: as torres agora devem ser capazes de suportar um peso (um pequeno objeto que você forneceu). As equipes devem adaptar sua estratégia para acomodar essa mudança.
- Após mais 3 minutos, anuncie outra mudança: as torres agora devem ser construídas de forma que possam ser facilmente desmontadas e remontadas. Novamente, as equipes precisarão adaptar-se à nova exigência.
- Troque ideias com seus colegas!

_1 imagem(ns) no slide._

> **Notas do apresentador:** Dinâmica: Scrum Puzzle Objetivo: Familiarizar os participantes com a decomposição do Scrum e o Sprint Backlog, ajudando-os a entender como as histórias de usuário são divididas em tarefas menores e como isso se relaciona com o planejamento de uma sprint. Materiais: Papel, canetas, cartões de índice ou post-its.

### Slide 21

- Hora de praticar!
- Depois que a atividade terminar, reúna o grupo para discutir o que aconteceu. Pergunte como eles reagiram às mudanças.
- Eles foram capazes de se adaptar rapidamente?
- O que poderiam ter feito de diferente?
- Isso os ajudará a entender a importância de estar aberto e receptivo às mudanças em um ambiente Scrum.
- Troque ideias com seus colegas!

_2 imagem(ns) no slide._

> **Notas do apresentador:** Dinâmica: Scrum Puzzle Objetivo: Familiarizar os participantes com a decomposição do Scrum e o Sprint Backlog, ajudando-os a entender como as histórias de usuário são divididas em tarefas menores e como isso se relaciona com o planejamento de uma sprint. Materiais: Papel, canetas, cartões de índice ou post-its.

### Slide 22

- Vamos praticar?
- Prepare-se, porque nessa atividade, você vai sair do modo aprender e entrar direto no modo praticar.
- A atividade prática vai colocar você diante de um desafio real: sensação de ver seu próprio código aparecer online! Acessível, documentado e pronto para o mundo!

_1 imagem(ns) no slide._

### Slide 23

- O que vimos na aula de hoje:
- Aprendemos sobre a implementação de mudanças em projetos com Scrum.

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

_Fonte: AULA 44_ATIVIDADE_ANÁLISE E MÉTODO PARA SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

ANÁLISE E MÉTODO PARA SISTEMAS

1ª SÉRIE

ATIVIDADE AULA 44

Questão 1

Como as mudanças são acomodadas no Scrum?

A) As mudanças não são permitidas no Scrum.

B) As mudanças são aceitas durante o Sprint e devem ser trabalhadas imediatamente.

C) As mudanças são aceitas, mas entram no Product Backlog e são priorizadas para futuros Sprints.

D) As mudanças são evitadas a todo custo para não atrapalhar o fluxo de trabalho.

Resposta correta: C) As mudanças são aceitas, mas entram no Product Backlog e são priorizadas para futuros Sprints. No Scrum, as mudanças são bem-vindas. No entanto, para evitar interrupções durante um Sprint em andamento, as mudanças normalmente entram no Product Backlog e são consideradas para inclusão em futuros Sprints.

Questão 2

uem é responsável por gerenciar as mudanças em um projeto Scrum?

A) O Product Owner

B) O Scrum Master

C) O time de desenvolvimento

D) Todos os membros do time Scrum

Resposta correta: A) O Product Owner. É responsabilidade do Product Owner gerenciar o Product Backlog, o que inclui acomodar e priorizar as mudanças que surgem.

## Prática

_Fonte: AULA 44_PRÁTICA_ANÁLISE E MÉTODO PARA SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

ANÁLISE E MÉTODO PARA SISTEMAS

1ª SÉRIE

ATIVIDADE PRÁTICA AULA 44

##### 1. Objetivo da Aula Prática

Ao final desta aula prática, o estudante deverá:

- Aprender como o Scrum lida com mudanças durante o desenvolvimento de projetos.
- Desenvolver a habilidade prática de adaptação rápida diante de mudanças de requisitos.
- Ser capaz de aplicar estratégias de comunicação, reorganização e planejamento em cenários de mudança dentro de uma Sprint.

##### 2. Ferramentas Recomendadas

Cartões de índice ou post-its

- Para que serve: Construção da dinâmica prática e organização das tarefas.
- Por que é adequada ao tema: Permite alterar rapidamente regras e estruturas durante a atividade.
- Como facilita o aprendizado: Simula mudanças frequentes em projetos Scrum.
Quadro branco ou cartolina

- Para que serve: Organização visual das tarefas e mudanças da Sprint.
- Por que é adequada ao tema: Facilita visualização das adaptações do projeto.
- Como facilita o aprendizado: Ajuda a compreender impactos das mudanças.
Cronômetro (celular)

- Para que serve: Controle do tempo da dinâmica.
- Por que é adequada ao tema: Simula o time-box das Sprints Scrum.
- Como facilita o aprendizado: Mantém foco e pressão semelhante ao ambiente real.
Trello (https://trello.com) — opcional

- Para que serve: Organização digital do Sprint Backlog.
- Por que é adequada ao tema: Simula ferramentas reais de gerenciamento ágil.
- Como facilita o aprendizado: Permite reorganização rápida das tarefas.

##### 3. Checklist Inicial

Antes de iniciar a prática, o estudante deve ter:

- Cartões de índice, papel ou post-its
- Caneta ou marcador
- Quadro ou superfície para montagem das atividades
- Espaço para trabalho em grupo
- Celular com cronômetro
- Computador ou celular com internet (opcional)
- Acesso ao material da aula

##### 4. Passo a Passo do Docente (Aula de até 50 minutos)

###### Como conduzir a aula

- Retome a aula anterior sobre gerenciamento de riscos no Scrum.
- Apresente o tema da aula: implementação e gerenciamento de mudanças.
- Explique os conceitos abordados no material:
- Mudanças em Scrum
- Adaptabilidade
- Sprint Planning
- Sprint Review
- Comunicação e transparência
- Desenvolvimento iterativo incremental
- Apresente o cenário da aula: João, Scrum Master iniciante, enfrentando mudanças de requisitos durante a Sprint.
- Explique que mudanças fazem parte do ambiente ágil e devem ser gerenciadas com comunicação e adaptação.
- Apresente a dinâmica “O Vento Mudou”.

###### Preparações necessárias

- Separar cartões e materiais
- Organizar as equipes
- Preparar pequenos objetos para a dinâmica (peso para as torres)
- Definir cronômetro visível

###### Alertas e pontos de atenção

- Alunos podem ficar frustrados com mudanças repentinas
- Reforce que o objetivo é justamente adaptação
- Incentive comunicação rápida e colaboração
- Oriente para reorganização estratégica das tarefas

###### Dinâmica sugerida

Construção inicial → mudança de requisito → adaptação → reflexão

###### Gerenciamento de tempo (50 minutos)

- Introdução e explicação: 15 minutos
- Dinâmica prática “O Vento Mudou”: 20 minutos
- Discussão e análise: 10 minutos
- Reflexão final: 5 minutos

##### 5. Atividade Prática — Descrição Geral

Os estudantes deverão participar de uma dinâmica baseada em mudanças contínuas de requisitos durante uma Sprint Scrum.

Cada equipe irá:

- Construir uma torre utilizando cartões de índice
- Adaptar o projeto conforme novas exigências surgirem
- Reorganizar estratégias rapidamente
- Trabalhar comunicação e colaboração
A atividade simula mudanças reais de requisitos em projetos ágeis.

A habilidade desenvolvida será a capacidade de adaptação rápida, reorganização de tarefas e comunicação eficiente em ambientes Scrum.

##### 6. Metodologia Ativa Utilizada

- Aprendizagem baseada em problemas (PBL)
- Simulação prática
- Aprendizagem colaborativa
- Experimentação ativa
Elementos de Lemov aplicados:

- Objetivo claro
- Participação ativa
- Produção visível
- Feedback imediato
- Cultura de erro como aprendizado

##### 7. Passo a Passo da Atividade Prática (para os alunos)

- Formem equipes de 3 a 5 integrantes.
- Recebam cartões de índice e iniciem a construção da maior torre possível.
- Trabalhem durante os primeiros 3 minutos normalmente.
- Após o aviso do professor, adaptem a torre para suportar um pequeno peso.
- Reorganizem a estrutura rapidamente sem reiniciar o projeto.
- Após novo aviso do professor, adaptem novamente a torre para que ela possa ser desmontada e remontada facilmente.
- Discutam rapidamente estratégias de adaptação dentro da equipe.
- Finalizem a construção dentro do tempo estabelecido.
- Preparem uma breve explicação sobre como lidaram com as mudanças.

##### 8. Exemplo ou Demonstração

Situação inicial:

Objetivo:

- Construir a maior torre possível.
Mudança 1:

- Torre deve suportar um objeto leve.
Mudança 2:

- Torre deve ser desmontável e remontável rapidamente.
Adaptações possíveis:

- Reforço da base
- Redução da altura
- Redistribuição das peças
- Melhor comunicação entre membros

##### 9. Resultado Esperado

O estudante deverá apresentar:

- Torre adaptada às mudanças propostas
- Estratégias utilizadas pela equipe
- Explicação sobre as decisões tomadas durante as mudanças
O professor poderá verificar o aprendizado observando:

- Capacidade de adaptação
- Comunicação da equipe
- Organização durante as mudanças
- Aplicação dos conceitos Scrum

##### 10. Formato de Entrega da Atividade

- Formato: Dinâmica prática presencial
- Registro: Foto da torre ou pequeno relatório reflexivo
- Nome do arquivo (se necessário): GerenciamentoMudancas_NomeGrupo
- Local de entrega: Em sala ou via plataforma digital
- Prazo sugerido: Durante a aula

##### 11. Encerramento e Reflexão

Finalize conduzindo uma reflexão orientada:

- Como a equipe reagiu às mudanças inesperadas?
- Foi difícil adaptar o planejamento inicial?
- O que ajudou mais: comunicação, organização ou rapidez?
- Como isso se relaciona com projetos reais em Scrum?
