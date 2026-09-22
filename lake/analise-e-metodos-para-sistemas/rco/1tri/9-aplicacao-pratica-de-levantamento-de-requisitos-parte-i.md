---
titulo: "Aplicação de Levantamento de Requisitos – Parte I"
tipo: rco-seed
disciplina: analise-e-metodos-para-sistemas
sigla_rco: AMS
trimestre: 1
ordem_rco: 9
serie: 1
aula_rco: "Aula 09"
slides: 23
tem_atividade: true
tem_pratica: true
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/AMS/1TRI/9-aplicacao-pratica-de-levantamento-de-requisitos-parte-i/9-aplicacao-pratica-de-levantamento-de-requisitos-parte-i.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/AMS/1TRI/9-aplicacao-pratica-de-levantamento-de-requisitos-parte-i/AULA 09_ATIVIDADE_ANÁLISE E MÉTODO PARA SISTEMAS.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/AMS/1TRI/9-aplicacao-pratica-de-levantamento-de-requisitos-parte-i/AULA 09_PRÁTICA_ANÁLISE E MÉTODO PARA SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Aplicação de Levantamento de Requisitos – Parte I

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- ANÁLISE E MÉTODO PARA SISTEMAS
- 1ª Série
- Aplicação de Levantamento de Requisitos – Parte I
- Aula 09

_1 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- ORGANIZAÇÃO CURRICULAR EPT 2026
- A partir de 2026, para atender as mudanças no Ensino Médio (Lei n.º 14.945/2024) as matrizes da Educação Profissional e Tecnológica (EPT), na oferta INTEGRADA, estarão organizadas da seguinte forma:
- Acesse aqui
- Plano de Curso: TÉCNICO EM DESENVOLVIMENTO DE SISTEMAS _INTEGRADO.docx
- Matriz Curricular: OUTUBRO_Matriz_DesenvolvimentoDeSistemas_Integrado_2026_DiurnoNoturno.docx
- 300h
- 1.800h

|  | 1ª série | 2ª série | 3ª série |
| --- | --- | --- | --- |
| Formação Geral Básica | 600 | 600 | 600 |
| Aprofundamento | 100 | 100 | 100 |
| Itinerário da Formação Técnica e Profissional | 300 | 300 | 300 |

- 900h
- 2.100 horas
- 1.200 horas
- O Aprofundamento traz HABILIDADES dos componentes curriculares da FGB, mas também contabiliza na carga horária da EPT, relacionando essas habilidades às HABILIDADES PROFISSIONAIS do Plano de Curso e do Catálogo Nacional de Cursos Técnicos.
- Desta forma, em algumas aulas, você vai encontrar indicativos da integração direta entre as habilidades dos componentes curriculares da FGB/BNCC e das unidades curriculares da EPT.
- SLIDE DO
- PROFESSOR

_2 imagem(ns) no slide._

### Slide 4

- COMPETÊNCIA(S) A SER(EM) DESENVOLVIDA(S) NESTA AULA:
- De acordo com o Plano de Curso de Desenvolvimento de Sistemas:
- HABILIDADE(S) A SER(EM) DESENVOLVIDA(S) NESTA AULA:
- Dimensionar requisitos e funcionalidades do sistema.
- Realizar o levantamento de requisitos de sistemas.

_1 imagem(ns) no slide._

### Slide 5

- Nesta aula, vamos:
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store
- Compreender como é feito a análise de requisitos inicial Parte I.

_4 imagem(ns) no slide._

### Slide 6

- Este material foi elaborado a partir da análise do plano de curso e reúne os conhecimentos essenciais para o Técnico em Desenvolvimento de Sistemas. As aulas foram organizadas com foco na clareza conceitual, na construção gradual dos conteúdos e na utilização de metodologias ativas que favorecem a compreensão, a participação e o desenvolvimento de habilidades e competências de forma significativa.
- De acordo com a matriz curricular do Curso Técnico em Desenvolvimento de Sistemas, que traz em sua essência componentes estruturados para a realização de aulas práticas, cada unidade curricular deve contemplar, além da abordagem teórica, uma proposta de atividade prática a ser desenvolvida pelo professor. Essa orientação assegura a coerência entre o planejamento didático e o que está estabelecido na matriz, promovendo experiências formativas alinhadas ao perfil profissional previsto.
- O professor tem total autonomia para adaptar o conteúdo conforme o contexto da turma, ajustando exemplos, aprofundamentos e estratégias didáticas para otimizar a aprendizagem e a conexão com a prática profissional.
- Se houver falta de conexão ou indisponibilidade de internet durante a aula, os materiais abaixo podem ser utilizados como apoio para elaborar recursos complementares, garantindo a continuidade da abordagem teórica prevista.
- ATENÇÃO PROFESSOR!
- Dicas para elaborar uma boa entrevista:
- https://cursos.alura.com.br/course/engenharia-requisitos/task/75120
- Documento de requisitos:
- https://cursos.alura.com.br/course/engenharia-requisitos/task/69673

_2 imagem(ns) no slide._

### Slide 7

- Na aula anterior…
- Compreendemos a parte inicial de levantamento de requisitos e sua importância, hoje iniciamos uma nova fase para acompanhar a aplicação do levantamento de requisitos.

_1 imagem(ns) no slide._

### Slide 8

- Para pensarmos juntos!
- João é um analista de requisitos que foi contratado por uma empresa de desenvolvimento de software para ajudar na coleta de requisitos de um novo sistema de gerenciamento de estoque para uma loja de varejo. Ele está conduzindo a primeira reunião com os stakeholders do projeto, mas percebe que há uma grande diferença nas expectativas de cada parte interessada.
- https://certificacaoiso.com.br/wp-content/uploads/2019/11/lancamento-do-projeto-de-desenvolvimento-em-desenvolvimento_82574-7825.jpg

_1 imagem(ns) no slide._

### Slide 9

- Para pensarmos juntos!
- O que João pode fazer para lidar com as diferenças nas expectativas dos stakeholders?
- Conversem e apresentem suas visões
- https://www.flowup.me/blog/wp-content/uploads/2019/09/gest%C3%A3o-de-projetos-01.png

_2 imagem(ns) no slide._

### Slide 10

- Resposta
- Para lidar com as diferenças nas expectativas dos stakeholders, João pode começar definindo o escopo do projeto e definindo claramente os objetivos e metas do sistema de gerenciamento de estoque. Ele também pode incentivar a participação ativa dos stakeholders na coleta de requisitos, permitindo que eles compartilhem suas perspectivas e ideias para o sistema.

_1 imagem(ns) no slide._

### Slide 11

- Resposta
- Além disso, é importante que João mantenha uma comunicação clara e transparente com os stakeholders durante todo o processo de levantamento de requisitos, para que todos estejam alinhados quanto às necessidades e expectativas do sistema de software a ser desenvolvido.

_1 imagem(ns) no slide._

### Slide 12

- Conceituando
- A primeira fase do levantamento de requisitos é uma etapa crucial no processo de desenvolvimento de software. Nessa fase, é importante coletar informações detalhadas sobre as necessidades e expectativas do cliente em relação ao sistema de software a ser desenvolvido. Isso é feito por meio de uma variedade de técnicas de coleta de requisitos, incluindo entrevistas, questionários, observação e análise de documentos existentes.
- https://www.escoladnc.com.br/blog/wp-content/webp-express/webp-images/uploads/2019/09/gestao_projetos-scaled.jpg.webp

_1 imagem(ns) no slide._

### Slide 13

- Conceituando
- Durante a primeira fase do levantamento de requisitos, é importante definir o escopo do projeto, ou seja, quais são as metas e objetivos do sistema de software a ser desenvolvido. Isso ajuda a garantir que a equipe de desenvolvimento esteja alinhada em relação aos objetivos e que possa trabalhar de forma mais eficiente para alcançá-los.
- https://blog.even3.com.br/wp-content/uploads/2021/12/imagem_destaque_projetodepesquisa.png

_1 imagem(ns) no slide._

### Slide 14

- Conceituando
- Uma das principais atividades na primeira fase do levantamento de requisitos é a identificação dos stakeholders envolvidos no projeto. Isso inclui o cliente, usuários finais, gerentes de negócios e outras partes interessadas que possam ser afetadas pelo sistema de software. Ao identificar todos os stakeholders, a equipe de desenvolvimento pode garantir que as necessidades de todas as partes sejam consideradas no processo de levantamento de requisitos.
- https://www.novida.com.br/wp-content/uploads/2019/01/Gestao-de-Projetos.png

_1 imagem(ns) no slide._

### Slide 15

- Ainda sobre a Engenharia de Requisitos, vamos conhecer praticando?
- Na plataforma Alura, vamos acessar o seguinte curso:
- Link para o curso: https://cursos.alura.com.br/course/engenharia-requisitos-demanda-gerenciamento
- Para melhor entendimento do conteúdo é recomendado que se responda aos quiz que estiverem entre as atividades propostas

_2 imagem(ns) no slide._

### Slide 16

- Apresentação
- Nesta parte do conteúdo será feito um acompanhamento a um projeto.
- Link para tarefa: https://cursos.alura.com.br/course/engenharia-requisitos-demanda-gerenciamento/task/82121
- Vamos acompanhar o desenvolvimento de um projeto. Vamos acompanhar uma analista de requisitos, todas as etapas do projeto dela, desde a abertura do projeto.
- Atividade no portal Alura

_3 imagem(ns) no slide._

### Slide 17

- O que faz um engenheiro de requisitos
- Um engenheiro de requisitos é responsável por coletar, analisar, documentar e gerenciar os requisitos de um sistema de software durante todo o ciclo de vida do projeto.
- Link para tarefa: https://cursos.alura.com.br/course/engenharia-requisitos-demanda-gerenciamento/task/82122
- Vamos conhecer um pouco quais são os perfis e as habilidades que um analista de requisitos precisa ter para desempenhar bem o seu papel ao longo do projeto.
- Atividade no portal Alura

_3 imagem(ns) no slide._

### Slide 18

- O início: Recebemos uma demanda
- Demanda de requisitos se refere ao processo de identificar, coletar e priorizar as necessidades e expectativas do cliente e outras partes interessadas em relação a um sistema de software.
- Link para tarefa: https://cursos.alura.com.br/course/engenharia-requisitos-demanda-gerenciamento/task/82123
- Vamos entender como nasce uma demanda, por onde surge, como chega a necessidade de um desenvolvimento de um sistema.
- Atividade no portal Alura

_3 imagem(ns) no slide._

### Slide 19

- Vamos praticar?
- Prepare-se, porque nessa atividade, você vai sair do modo aprender e entrar direto no modo praticar.
- A atividade prática vai colocar você diante de um desafio real: sensação de ver seu próprio código aparecer online! Acessível, documentado e pronto para o mundo!

_1 imagem(ns) no slide._

### Slide 20

- O que vimos na aula de hoje
- Como se inicia um processo de levantamento de requisitos

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

_Fonte: AULA 09_ATIVIDADE_ANÁLISE E MÉTODO PARA SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

ANÁLISE E MÉTODO PARA SISTEMAS

1ª SÉRIE

ATIVIDADE AULA 09

Questão 1

Qual é o objetivo da aplicação do levantamento de requisitos no início do processo de desenvolvimento de software?

A) Definir as tarefas da equipe de desenvolvimento.

B) Garantir que o software tenha uma boa aparência.

C) Identificar as necessidades e expectativas do cliente.

D) Estabelecer as datas de entrega do projeto.

Resposta correta: C) Identificar as necessidades e expectativas do cliente. O objetivo do levantamento de requisitos é identificar as necessidades e expectativas do cliente em relação ao sistema de software a ser desenvolvido. Isso ajuda a garantir que o produto final atenda às expectativas do cliente e possa fornecer valor para o negócio.

Questão 2

Qual é a principal atividade envolvida no início do processo de levantamento de requisitos?

A) Coleta de informações sobre os desenvolvedores do software.

B) Definição do escopo do projeto.

C) Seleção da linguagem de programação a ser usada.

D) Elaboração do plano de testes de software.

Resposta correta: B) Definição do escopo do projeto. A definição do escopo do projeto é uma das principais atividades na fase de levantamento de requisitos. Isso ajuda a garantir que a equipe de desenvolvimento esteja alinhada em relação aos objetivos e que possa trabalhar de forma mais eficiente para alcançá-los.

## Prática

_Fonte: AULA 09_PRÁTICA_ANÁLISE E MÉTODO PARA SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

ANÁLISE E MÉTODO PARA SISTEMAS

1ª SÉRIE

ATIVIDADE PRÁTICA AULA 09

##### 1. Objetivo da Aula Prática

Ao final desta aula prática, o estudante deverá:

- Aprender como se inicia, na prática, o processo de levantamento de requisitos de um sistema.
- Desenvolver a habilidade prática de identificar stakeholders, compreender necessidades e definir o escopo inicial de um projeto de software.
- Ser capaz de executar um levantamento inicial de requisitos, registrando informações coletadas a partir de um cenário realista de projeto.

##### 2. Ferramentas Recomendadas

Caderno ou Folha A4

- Para que serve: Registro inicial das informações coletadas durante o levantamento de requisitos.
- Por que é adequada ao tema: O material da aula enfatiza entrevistas, conversas e registros iniciais.
- Como facilita o aprendizado: Ajuda o aluno a organizar ideias e estruturar informações.
Google Docs (https://docs.google.com)

- Para que serve: Documentação digital dos requisitos levantados.
- Por que é adequada ao tema: Permite registrar requisitos de forma clara e organizada.
- Como facilita o aprendizado: Facilita revisões, complementações e validações.
Google Sheets (https://sheets.google.com)

- Para que serve: Organização de stakeholders, requisitos e observações.
- Por que é adequada ao tema: Auxilia na visualização e classificação das informações coletadas.
- Como facilita o aprendizado: Torna o processo de análise mais estruturado.
(Ferramentas gratuitas, online ou de uso livre.)

##### 3. Checklist Inicial

Antes de iniciar a prática, o estudante deve ter:

- Caderno ou folhas para anotações
- Caneta ou lápis
- Computador ou notebook
- Conexão com a internet
- Acesso ao material da aula (PDF ou slides)
- Ambiente: sala de aula ou laboratório de informática

##### 4. Passo a Passo do Docente (Aula de até 50 minutos)

###### Como conduzir a aula

- Retome a aula anterior, reforçando o conceito de reunião e validação de requisitos.
- Apresente o cenário do material: João, analista de requisitos, em sua primeira reunião com stakeholders de um sistema de gerenciamento de estoque.
- Provoque a reflexão inicial: diferenças de expectativas entre stakeholders.
- Explique que esta aula representa a primeira fase prática do levantamento de requisitos.
- Apresente a atividade prática e os critérios de execução.

###### Preparações necessárias

- Definir se a atividade será individual ou em duplas
- Preparar quadro ou slide para síntese coletiva
- Garantir que os alunos tenham acesso ao cenário apresentado

###### Alertas e pontos de atenção

- Alunos podem tentar “resolver” o sistema em vez de levantar requisitos
- Reforce que o foco é entender o problema, não criar a solução
- Oriente para escuta, registro e clareza

###### Dinâmica sugerida

- Situação-problema → discussão orientada → prática guiada → socialização

###### Gerenciamento de tempo (50 minutos)

- Contextualização e cenário: 10 minutos
- Explicação do levantamento inicial: 10 minutos
- Execução da atividade prática: 20 minutos
- Discussão e fechamento: 10 minutos

##### 5. Atividade Prática — Descrição Geral

O estudante deverá realizar a aplicação inicial do levantamento de requisitos, considerando o seguinte cenário:

Um sistema de gerenciamento de estoque será desenvolvido para uma loja de varejo, e existem diferentes expectativas entre os stakeholders envolvidos.

A atividade simula a primeira reunião de levantamento de requisitos, em que o analista precisa compreender necessidades, alinhar expectativas e definir o escopo inicial.

A habilidade desenvolvida será a capacidade de analisar demandas reais e registrar requisitos iniciais de forma estruturada.

##### 6. Metodologia Ativa Utilizada

- Aprendizagem baseada em problemas (PBL)
- Aprendizagem colaborativa
- Ensino por descoberta
Elementos de Lemov aplicados:

- Objetivo claro
- Participação ativa
- Produção visível
- Pensamento estruturado

##### 7. Passo a Passo da Atividade Prática (para os alunos)

- Leia atentamente o cenário apresentado pelo professor.
- Identifique quem são os possíveis stakeholders do sistema.
- Registre quais podem ser as necessidades e expectativas de cada stakeholder.
- Liste informações que precisam ser esclarecidas na primeira reunião.
- Defina, de forma inicial, o escopo do sistema (o que está e o que não está incluído).
- Organize os registros de forma clara e objetiva.
- Prepare-se para compartilhar suas conclusões com a turma.

##### 8. Exemplo ou Demonstração

Exemplo de identificação inicial:

- Stakeholders:
- Dono da loja
- Funcionários
- Gerente
- Necessidades:
- Controle de entrada e saída de produtos
- Relatórios de estoque
- Redução de perdas
- Escopo inicial:
- Cadastro de produtos
- Controle de estoque
- Relatórios básicos
(O professor pode construir esse exemplo no quadro como demonstração.)

##### 9. Resultado Esperado

O estudante deverá apresentar:

- Identificação clara dos stakeholders
- Lista organizada de necessidades e expectativas
- Definição inicial de escopo do sistema
O professor poderá verificar o aprendizado observando:

- Clareza dos registros
- Coerência com o cenário apresentado
- Capacidade de análise do problema

##### 10. Formato de Entrega da Atividade

- Formato: Registro no caderno, folha ou arquivo digital
- Nome do arquivo (se digital): Levantamento_Inicial_Requisitos_NomeAluno
- Local de entrega: Avaliação em sala ou envio via Google Classroom/Drive
- Prazo sugerido: Durante a aula

##### 11. Encerramento e Reflexão

Finalize a aula conduzindo uma reflexão orientada:

- Por que alinhar expectativas dos stakeholders é importante logo no início?
- O que pode acontecer se o escopo não for bem definido?
- Como essa atividade se conecta com as próximas etapas do levantamento de requisitos?
