---
titulo: "Construção do Modelo de Sistema"
tipo: rco-seed
disciplina: analise-e-metodos-para-sistemas
sigla_rco: AMS
trimestre: 1
ordem_rco: 7
serie: 1
aula_rco: "Aula 07"
slides: 21
tem_atividade: true
tem_pratica: true
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/AMS/1TRI/7-construcao-do-modelo-de-sistema/7-construcao-do-modelo-de-sistema.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/AMS/1TRI/7-construcao-do-modelo-de-sistema/AULA 07_ATIVIDADE_ANÁLISE E MÉTODO PARA SISTEMAS.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/AMS/1TRI/7-construcao-do-modelo-de-sistema/AULA 07_PRÁTICA_ANÁLISE E MÉTODO PARA SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Construção do Modelo de Sistema

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- ANÁLISE E MÉTODO PARA SISTEMAS
- 1ª Série
- Construção do Modelo de Sistema
- Aula 07

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
- Elaborar diagramas na linguagem de modelagem unificada.

_1 imagem(ns) no slide._

### Slide 5

- Nesta aula, vamos:
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store
- Construção de um modelo para Análise e Projeto

_4 imagem(ns) no slide._

### Slide 6

- Este material foi elaborado a partir da análise do plano de curso e reúne os conhecimentos essenciais para o Técnico em Desenvolvimento de Sistemas. As aulas foram organizadas com foco na clareza conceitual, na construção gradual dos conteúdos e na utilização de metodologias ativas que favorecem a compreensão, a participação e o desenvolvimento de habilidades e competências de forma significativa.
- De acordo com a matriz curricular do Curso Técnico em Desenvolvimento de Sistemas, que traz em sua essência componentes estruturados para a realização de aulas práticas, cada unidade curricular deve contemplar, além da abordagem teórica, uma proposta de atividade prática a ser desenvolvida pelo professor. Essa orientação assegura a coerência entre o planejamento didático e o que está estabelecido na matriz, promovendo experiências formativas alinhadas ao perfil profissional previsto.
- O professor tem total autonomia para adaptar o conteúdo conforme o contexto da turma, ajustando exemplos, aprofundamentos e estratégias didáticas para otimizar a aprendizagem e a conexão com a prática profissional.
- Se houver falta de conexão ou indisponibilidade de internet durante a aula, os materiais abaixo podem ser utilizados como apoio para elaborar recursos complementares, garantindo a continuidade da abordagem teórica prevista.
- ATENÇÃO PROFESSOR!
- Dicas para elaborar uma boa entrevista:
- https://cursos.alura.com.br/course/engenharia-requisitos/task/75120
- Otimizando o brainstorming
- https://cursos.alura.com.br/course/engenharia-requisitos/task/75123

_2 imagem(ns) no slide._

### Slide 7

- Na aula anterior…
- Introdução a Análise e Projeto e os conceitos relacionados a essa área.

_1 imagem(ns) no slide._

### Slide 8

- Para pensarmos juntos!
- Rafael é um engenheiro de software que foi contratado por uma pequena empresa de tecnologia para desenvolver um aplicativo de gerenciamento de tarefas. Antes de iniciar a programação, ele precisa criar um modelo de análise e projeto para orientar o desenvolvimento do aplicativo.
- https://rockcontent.com/br/blog/modelo-de-projeto/

_1 imagem(ns) no slide._

### Slide 9

- Para pensarmos juntos!
- No entanto, como a equipe é pequena e com prazos apertados, Rafael está preocupado se conseguirá construir um modelo eficiente que possa ser usado por toda a equipe.
- Como Rafael pode criar um modelo de análise e projeto eficiente que atenda às necessidades da equipe e facilite o desenvolvimento do aplicativo de gerenciamento de tarefas?
- https://artia.com/wp-content/uploads/2020/11/O-que-e-um-projeto.png
- Dialogue com o colega e socialize as ideias com a turma no final!

_2 imagem(ns) no slide._

### Slide 10

- Resposta
- Rafael pode seguir estas etapas para criar um modelo de análise e projeto eficiente:
- Definir os requisitos
- Escolher uma metodologia de desenvolvimento
- Modelagem de dados
- Diagramas de projeto
- Revisar e validar o modelo

_1 imagem(ns) no slide._

### Slide 11

- Conceituando
- A construção de um modelo de análise e projeto é um processo crucial no desenvolvimento de software que envolve a criação de uma representação abstrata e visual do sistema a ser desenvolvido. O objetivo é compreender e documentar os requisitos, a estrutura e as funcionalidades do sistema, facilitando a comunicação entre os membros da equipe e os stakeholders, e orientando a implementação e a manutenção do software.
- https://ericlemes.files.wordpress.com/2009/05/usecase.jpg?w=640

_1 imagem(ns) no slide._

### Slide 12

- Conceituando
- Os modelos de análise e projeto geralmente incluem diagramas e documentos que ilustram os componentes do sistema, suas interações e a arquitetura geral do software. Técnicas de modelagem, como a Linguagem de Modelagem Unificada (UML), são comumente usadas para criar esses diagramas. Eles podem incluir diagramas de casos de uso, diagramas de classes, diagramas de sequência, diagramas de atividades, entre outros, que ajudam a equipe a visualizar e entender o fluxo e a organização do sistema.
- https://treinamentowaei.files.wordpress.com/2014/07/brainstorming.jpg?w=405&h=261

_1 imagem(ns) no slide._

### Slide 13

- Conceituando
- A construção de um modelo de análise e projeto eficiente requer colaboração e comunicação entre os membros da equipe e os stakeholders para identificar e documentar os requisitos funcionais e não funcionais do projeto. O modelo deve ser iterativo e adaptável às mudanças de requisitos, facilitando a evolução do projeto e garantindo que o software desenvolvido atenda às expectativas e necessidades dos usuários finais.
- https://www.escoladnc.com.br/blog/wp-content/webp-express/webp-images/uploads/2019/09/gestao_projetos-scaled.jpg.webp

_1 imagem(ns) no slide._

### Slide 14

- Ainda sobre a Engenharia de Requisitos, vamos conhecer praticando?
- Na plataforma Alura, vamos acessar o seguinte curso:
- Link para o curso: https://cursos.alura.com.br/course/engenharia-requisitos
- Para melhor entendimento do conteúdo é recomendado que se responda aos quiz que estiverem entre as atividades propostas

_2 imagem(ns) no slide._

### Slide 15

- Brainstorming
- O brainstorming é um processo criativo em grupo para gerar ideias e soluções, onde os participantes compartilham livremente suas sugestões, estimulando a criatividade e a inovação.
- Link para tarefa: https://cursos.alura.com.br/course/engenharia-requisitos/task/67770
- O brainstorming estimula a criatividade e a colaboração, permitindo a geração de diversas ideias e soluções, além de promover o engajamento e a participação de todos os membros do grupo.
- Atividade no portal Alura

_3 imagem(ns) no slide._

### Slide 16

- Prototipação
- A prototipação é um processo de criação de modelos preliminares de um produto ou sistema, permitindo testar e validar ideias, funcionalidades e design antes da implementação final.
- Link para tarefa: https://cursos.alura.com.br/course/engenharia-requisitos/task/67771
- A prototipação economiza tempo e recursos, permitindo identificar problemas e melhorias antes do desenvolvimento completo, além de facilitar a comunicação e a validação de ideias com stakeholders e usuários.
- Atividade no portal Alura

_3 imagem(ns) no slide._

### Slide 17

- Vamos praticar?
- Prepare-se, porque nessa atividade, você vai sair do modo aprender e entrar direto no modo praticar.
- A atividade prática vai colocar você diante de um desafio real: sensação de ver seu próprio código aparecer online! Acessível, documentado e pronto para o mundo!

_1 imagem(ns) no slide._

### Slide 18

- O que vimos na aula de hoje
- Compreendemos a importância da criação de protótipos para validar requisitos e assegurar que um requisito foi entendido da maneira correta.

_1 imagem(ns) no slide._

### Slide 19

- Pronto para desbloquear sua carreira de TI?
- Está perdido estudando mas não sabe por onde começar? Se a resposta é sim, você está no lugar certo! Descubra as estratégias e ferramentas essenciais para te ajudar a desbloquear seu potencial em TI e buscar sua primeira vaga de emprego no setor!
- Este e-book é um guia completo para quem busca começar pelos melhores caminhos para se tornar um excelente profissional de TI, ensinando a identificar perfis profissionais, aplicar técnicas de estudo eficazes, transformar teoria em prática, e aumentar a visibilidade de seu trabalho no mercado de trabalho. Ideal para novatos e profissionais em transição.
- E o melhor, ele pode ser seu, inteiramente grátis!
- Basta clicar AQUI e realizar o seu cadastro com o seu @escola!

_3 imagem(ns) no slide._

### Slide 20

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

### Slide 21

_(sem texto)_

## Atividade

_Fonte: AULA 07_ATIVIDADE_ANÁLISE E MÉTODO PARA SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

ANÁLISE E MÉTODO PARA SISTEMAS

1ª SÉRIE

ATIVIDADE AULA 07

Questão 1

Qual é a principal finalidade de criar um modelo de análise e projeto durante o desenvolvimento de software?

a) Criar uma representação visual do código-fonte.

b) Escolher a melhor linguagem de programação para o projeto.

c) Compreender e documentar os requisitos, a estrutura e as funcionalidades do sistema.

d) Testar o desempenho do software final.

Comentário: A resposta correta é a alternativa (c). A principal finalidade de criar um modelo de análise e projeto é compreender e documentar os requisitos, a estrutura e as funcionalidades do sistema, facilitando a comunicação entre os membros da equipe e orientando a implementação e a manutenção do software.

Questão 2

Qual técnica de modelagem é comumente usada para criar diagramas que ilustram os componentes do sistema, suas interações e a arquitetura geral do software?

a) Desenho técnico

b) Mapa mental

c) Linguagem de Modelagem Unificada (UML)

d) Fluxograma

Comentário: A resposta correta é a alternativa (c). A Linguagem de Modelagem Unificada (UML) é uma técnica de modelagem amplamente utilizada para criar diagramas que ilustram os componentes do sistema, suas interações e a arquitetura geral do software, facilitando a visualização e a compreensão do projeto.

## Prática

_Fonte: AULA 07_PRÁTICA_ANÁLISE E MÉTODO PARA SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

ANÁLISE E MÉTODO PARA SISTEMAS

1ª SÉRIE

ATIVIDADE PRÁTICA AULA 07

##### 1. Objetivo da Aula Prática

Ao final desta aula prática, o estudante deverá:

- Aprender o que é a construção de um modelo de análise e projeto de sistemas e sua importância no desenvolvimento de software.
- Desenvolver a habilidade prática de organizar requisitos e funcionalidades por meio de um modelo de sistema.
- Ser capaz de produzir um modelo inicial de sistema, representando requisitos, funcionalidades e elementos básicos de um aplicativo de gerenciamento de tarefas.

##### 2. Ferramentas Recomendadas

Caderno ou Folha A4

- Para que serve: Rascunho inicial do modelo do sistema.
- Por que é adequada ao tema: O material da aula enfatiza a construção conceitual antes da implementação.
- Como facilita o aprendizado: Estimula o planejamento e a organização do raciocínio.
Google Desenhos (https://drawings.google.com)

- Para que serve: Criação de diagramas simples do modelo de sistema.
- Por que é adequada ao tema: Permite representar visualmente funcionalidades e relações do sistema.
- Como facilita o aprendizado: Ajuda a transformar conceitos abstratos em representações visuais claras.
Draw.io / diagrams.net (https://app.diagrams.net/)

- Para que serve: Criação de diagramas de casos de uso e fluxos simples.
- Por que é adequada ao tema: Compatível com UML básica, conforme indicado no material.
- Como facilita o aprendizado: Facilita a compreensão da estrutura e do funcionamento do sistema.
(Ferramentas gratuitas, online ou open source.)

##### 3. Checklist Inicial

Antes de iniciar a prática, o estudante deve ter:

- Caderno ou folhas para rascunho
- Caneta ou lápis
- Computador ou notebook
- Conexão com a internet
- Acesso ao material da aula (PDF ou slides)
- Ambiente: sala de aula ou laboratório de informática

##### 4. Passo a Passo do Docente (Aula de até 50 minutos)

###### Como conduzir a aula

- Retome brevemente a aula anterior, destacando a importância do levantamento de requisitos.
- Apresente o cenário do material: Rafael, engenheiro de software, desenvolvendo um aplicativo de gerenciamento de tarefas.
- Explique o conceito de modelo de análise e projeto, conforme definido nos slides.
- Mostre que o modelo serve para organizar requisitos, funcionalidades e comunicação da equipe.
- Apresente a atividade prática: construção de um modelo simples de sistema.

###### Preparações necessárias

- Definir se a atividade será individual ou em duplas
- Ter um exemplo simples de modelo de sistema (quadro ou slide)
- Testar previamente as ferramentas digitais

###### Alertas e pontos de atenção

- Alunos podem confundir modelo com código
- Reforce que não haverá programação, apenas modelagem
- Oriente para modelos simples, claros e objetivos

###### Dinâmica sugerida

- Explanação → análise do cenário → prática guiada → socialização

###### Gerenciamento de tempo (50 minutos)

- Contextualização e conceitos: 15 minutos
- Explicação da atividade: 10 minutos
- Execução da prática: 15 minutos
- Apresentação e fechamento: 10 minutos

##### 5. Atividade Prática — Descrição Geral

O estudante deverá construir um modelo inicial de sistema para um aplicativo de gerenciamento de tarefas, considerando:

- Necessidades do usuário
- Funcionalidades principais
- Organização lógica do sistema
A atividade simula uma situação real de projeto, em que o desenvolvedor precisa planejar o sistema antes da implementação.

A habilidade desenvolvida será a capacidade de estruturar e representar um sistema de forma visual e organizada.

##### 6. Metodologia Ativa Utilizada

- Aprendizagem baseada em problemas (PBL)
- Ensino por descoberta
- Experimentação prática
- Colaboração (quando realizada em duplas)
Elementos de Lemov aplicados:

- Objetivo claro
- Produção visível
- Pensamento estruturado
- Explicitação do raciocínio

##### 7. Passo a Passo da Atividade Prática (para os alunos)

- Leia atentamente o cenário apresentado pelo professor.
- Identifique quem são os usuários do sistema.
- Liste as principais funcionalidades do aplicativo de tarefas.
- Organize essas funcionalidades em um modelo visual (diagrama simples).
- Relacione usuário e funcionalidades (ex.: usuário cria tarefa, edita tarefa, remove tarefa).
- Revise o modelo para verificar clareza e lógica.
- Prepare-se para explicar seu modelo à turma.

##### 8. Exemplo ou Demonstração

Exemplo de funcionalidades do modelo:

- Cadastrar tarefa
- Editar tarefa
- Excluir tarefa
- Marcar tarefa como concluída
- Visualizar lista de tarefas
Exemplo de representação:

- Usuário → Gerenciar tarefas
- Sistema → Cadastro, edição, exclusão e visualização
(O professor pode desenhar um modelo simples no quadro.)

##### 9. Resultado Esperado

O estudante deverá apresentar:

- Um modelo de sistema organizado
- Funcionalidades claramente identificadas
- Relação lógica entre usuário e sistema
O professor poderá verificar o aprendizado observando:

- Clareza do modelo
- Coerência das funcionalidades
- Adequação ao cenário proposto

##### 10. Formato de Entrega da Atividade

- Formato: Desenho no caderno, folha ou arquivo digital
- Nome do arquivo (se digital): Modelo_Sistema_Tarefas_NomeAluno
- Local de entrega: Avaliação em sala ou envio via Google Classroom/Drive
- Prazo sugerido: Durante a aula

##### 11. Encerramento e Reflexão

Finalize a aula promovendo uma reflexão orientada:

- Por que criar um modelo antes de desenvolver um sistema?
- Como o modelo ajuda a equipe a entender o sistema?
- O que pode acontecer se um sistema for desenvolvido sem modelagem?
