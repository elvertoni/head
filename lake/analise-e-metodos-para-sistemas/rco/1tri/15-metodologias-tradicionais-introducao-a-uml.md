---
titulo: "Metodologias Tradicionais: Introdução à UML"
tipo: rco-seed
disciplina: analise-e-metodos-para-sistemas
sigla_rco: AMS
trimestre: 1
ordem_rco: 15
serie: 1
aula_rco: "Aula 15"
slides: 24
tem_atividade: true
tem_pratica: true
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/AMS/1TRI/15-metodologias-tradicionais-introducao-a-uml/15-metodologias-tradicionais-introducao-a-uml.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/AMS/1TRI/15-metodologias-tradicionais-introducao-a-uml/AULA 15_ATIVIDADE_ANÁLISE E MÉTODO PARA SISTEMAS.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/AMS/1TRI/15-metodologias-tradicionais-introducao-a-uml/AULA 15_PRÁTICA_ANÁLISE E MÉTODO PARA SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Metodologias Tradicionais: Introdução à UML

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- ANÁLISE E MÉTODO PARA SISTEMAS
- 1ª Série
- Metodologias Tradicionais: Introdução à UML
- Aula 15

_1 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- COMPETÊNCIA(S) A SER(EM) DESENVOLVIDA(S) NESTA AULA:
- De acordo com o Plano de Curso de Desenvolvimento de Sistemas:
- HABILIDADE(S) A SER(EM) DESENVOLVIDA(S) NESTA AULA:
- Dimensionar requisitos e funcionalidades do sistema.
- Elaborar diagramas na linguagem de modelagem unificada.

_1 imagem(ns) no slide._

### Slide 4

- Nesta aula vamos:
- Aprender sobre a introdução a linguagem de modelagem UML.
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
- Dicas para elaborar uma boa entrevista:
- https://cursos.alura.com.br/course/engenharia-requisitos/task/75120
- Documento de requisitos:
- https://cursos.alura.com.br/course/engenharia-requisitos/task/69673

_2 imagem(ns) no slide._

### Slide 6

- Na aula anterior…
- Aprendemos o que significa ser ágil ao praticar e vivenciar a própria metodologia ágil.

_1 imagem(ns) no slide._

### Slide 7

- Para pensarmos juntos...
- Ele tinha uma compreensão básica da UML da faculdade, mas nunca a tinha usado em um cenário real. A equipe estava particularmente focada no Diagrama de Classes para entender as relações entre os diferentes componentes do sistema. A equipe também mencionou o uso de Diagramas de Sequência para entender o fluxo de mensagens entre objetos.
- Lucas foi designado para um projeto em andamento e, em sua primeira reunião com a equipe, percebeu que todos estavam discutindo sobre os Diagramas UML.

_1 imagem(ns) no slide._

### Slide 8

- Para pensarmos juntos...
- Lucas sentiu que precisava aprimorar rapidamente seu entendimento sobre UML para contribuir eficazmente para a discussão e para o projeto.
- Lucas ficou confuso sobre a diferença entre Diagrama de Classes e Diagrama de Sequência. Ele questionou:
- 3 minutos
- Pesquise e escreva no seu caderno
- "Qual é a principal diferença entre o Diagrama de Classes e o Diagrama de Sequência na UML, e como eles são utilizados na prática dentro do projeto?"

_3 imagem(ns) no slide._

### Slide 9

- Resposta
- O Diagrama de Classes é utilizado para representar as classes do sistema, suas propriedades, métodos e as relações entre elas, fornecendo uma visão estática da estrutura do sistema.
- Por outro lado, o Diagrama de Sequência é usado para visualizar a interação entre objetos em um período de tempo, mostrando a sequência de mensagens trocadas entre eles, proporcionando uma visão dinâmica do comportamento do sistema.

_1 imagem(ns) no slide._

### Slide 10

- Resposta
- Na prática, enquanto o Diagrama de Classes ajuda a equipe a entender a organização estrutural e as relações entre os componentes do sistema, o Diagrama de Sequência ajuda a entender o fluxo de comunicação e a sequência de operações que ocorrem ao longo do tempo.
- Ambos os diagramas são cruciais para a equipe compreender tanto a arquitetura estática quanto a dinâmica do sistema em que estão trabalhando.

_1 imagem(ns) no slide._

### Slide 11

- Definição
- A UML (Unified Modeling Language ou Linguagem de Modelagem Unificada) é uma linguagem gráfica utilizada para visualizar, especificar, construir e documentar artefatos de um sistema de software.
- Ela não é uma metodologia de desenvolvimento, mas sim um conjunto de notações gráficas utilizadas para representar conceitualmente diferentes aspectos de um sistema.
- A UML é amplamente utilizada por profissionais da área de desenvolvimento de software e é uma ferramenta essencial para comunicar ideias de forma clara e precisa entre a equipe de projeto.

_1 imagem(ns) no slide._

### Slide 12

- Diagrama de Classes
- O Diagrama de Classes é um dos mais fundamentais na UML e serve para representar as classes do sistema, suas propriedades, métodos e as relações entre elas. É uma forma excelente de entender como os diferentes componentes do sistema se relacionam e interagem entre si.

_1 imagem(ns) no slide._

### Slide 13

- Diagrama de Casos de Uso
- Este diagrama mostra como os usuários externos (atores) interagem com o sistema, através dos casos de uso. Eles são úteis para identificar as principais funcionalidades do sistema e os atores envolvidos.

_1 imagem(ns) no slide._

### Slide 14

- Diagrama de Sequência
- Os Diagramas de Sequência são utilizados para representar as interações entre os objetos ao longo do tempo. Eles são ótimos para visualizar o fluxo de mensagens entre objetos e compreender a sequência de atividades que ocorrem.
- Fonte da imagem: https://miro.medium.com/v2/resize:fit:529/1*HhEy_rUnWj2axLTTVQpy5w.png

_1 imagem(ns) no slide._

### Slide 15

- Diagrama de Estado
- Este diagrama mostra o ciclo de vida de um objeto, representando os estados pelos quais o objeto pode passar e as transições entre estes estados. É útil para entender como um objeto muda de estado em resposta a eventos externos.
- Fonte da imagem: https://support.content.office.net/pt-br/media/3ac1da3e-ab76-41a8-85ba-5e48752138db.png

_1 imagem(ns) no slide._

### Slide 16

- Diagrama de Atividades
- Similar a um fluxograma, o Diagrama de Atividades mostra o fluxo de atividades dentro de um sistema, permitindo uma visualização clara do comportamento do sistema em termos de atividades sequenciais.
- Fonte da imagem: https://support.content.office.net/pt-br/media/3ac1da3e-ab76-41a8-85ba-5e48752138db.png

_1 imagem(ns) no slide._

### Slide 17

- Diagrama de Componentes
- Este diagrama representa os componentes de software físicos presentes no sistema, como bibliotecas, módulos, arquivos, etc., e as relações entre eles.
- Fonte da imagem: https://d2slcw3kip6qmk.cloudfront.net/marketing/pages/chart/component-diagram-for-ATM-system-UML/component_diagram_ATM_system-843x746.PNG

_1 imagem(ns) no slide._

### Slide 18

- Ainda sobre UML, vamos conhecer praticando?
- Na plataforma Alura vamos acessar o seguinte curso:
- Os próximos itens serão para guiá-los nas principais atividades que serão necessárias para o entendimento da aula de hoje, embora existam mais atividades na plataforma Alura, em sala iremos desenvolver as essenciais.
- A recomendação é que você continue esse curso extraclasse, pois ele traz um conteúdo essencial para compreender sobre o referido tema.
- Link para o curso: https://cursos.alura.com.br/course/introducao-a-uml

_3 imagem(ns) no slide._

### Slide 19

- Entendimento inicial da UML
- 35 minutos
- Links das principais aulas práticas sobre os diagramas citados anteriormente.
- Visão Diagrama casos de uso:
- https://cursos.alura.com.br/course/introducao-a-uml/task/4399
- Visão Diagrama de classes:
- https://cursos.alura.com.br/course/introducao-a-uml/task/4406
- Visão Diagrama de sequência:
- https://cursos.alura.com.br/course/introducao-a-uml/task/4413
- Visão Diagrama de atividades:
- https://cursos.alura.com.br/course/introducao-a-uml/task/4420
- Atividade no portal Alura

_3 imagem(ns) no slide._

### Slide 20

- Vamos praticar?
- Prepare-se, porque nessa atividade, você vai sair do modo aprender e entrar direto no modo praticar.
- A atividade prática vai colocar você diante de um desafio real: sensação de ver seu próprio código aparecer online! Acessível, documentado e pronto para o mundo!

_1 imagem(ns) no slide._

### Slide 21

- O que vimos na aula de hoje:
- Aprendemos de forma introdutória o que é a UML e para que serve.

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

_Fonte: AULA 15_ATIVIDADE_ANÁLISE E MÉTODO PARA SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

ANÁLISE E MÉTODO PARA SISTEMAS

1ª SÉRIE

ATIVIDADE AULA 15

Questão 1

Qual dos seguintes diagramas UML é mais apropriado para visualizar o fluxo de processos através de componentes do sistema?

a) Diagrama de Classes

b) Diagrama de Objetos

c) Diagrama de Atividades

d) Diagrama de Implantação

Resposta Correta: c) Diagrama de Atividades

O Diagrama de Atividades é utilizado para visualizar o fluxo de processos através de componentes do sistema, mostrando a sequência de atividades e as condições para a transição entre elas.

Questão 2

O que o Diagrama de Casos de Uso UML é projetado principalmente para representar?

a) A estrutura interna das classes.

b) A sequência de mensagens entre objetos.

c) As relações entre os requisitos do sistema e os atores externos.

d) O fluxo de atividades dentro do sistema.

Resposta Correta: c) As relações entre os requisitos do sistema e os atores externos.

O Diagrama de Casos de Uso é utilizado para representar as funcionalidades do sistema a partir da perspectiva dos atores externos, mostrando as interações entre eles e o sistema através de vários cenários ou casos de uso.

## Prática

_Fonte: AULA 15_PRÁTICA_ANÁLISE E MÉTODO PARA SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

ANÁLISE E MÉTODO PARA SISTEMAS

1ª SÉRIE

ATIVIDADE PRÁTICA AULA 15

##### 1. Objetivo da Aula Prática

Ao final desta aula prática, o estudante deverá:

- Aprender o que é a UML e para que ela é utilizada no desenvolvimento de software.
- Desenvolver a habilidade prática de identificar e diferenciar os principais diagramas UML.
- Ser capaz de produzir um esboço de diagrama UML simples representando um sistema.

##### 2. Ferramentas Recomendadas

Caderno ou Folha A4

- Para que serve: Esboço manual dos diagramas.
- Por que é adequada ao tema: Permite desenhar rapidamente modelos conceituais.
- Como facilita o aprendizado: Ajuda a compreender os elementos gráficos da UML.
draw.io / diagrams.net (https://app.diagrams.net)

- Para que serve: Criação de diagramas UML digitais.
- Por que é adequada ao tema: Possui biblioteca específica para UML.
- Como facilita o aprendizado: Permite visualizar diagramas profissionais de forma simples.
Google Slides (https://slides.google.com)

- Para que serve: Representação visual organizada dos diagramas.
- Por que é adequada ao tema: Facilita apresentação e compartilhamento.
- Como facilita o aprendizado: Torna o conteúdo mais visual e estruturado.
(Ferramentas gratuitas, online ou open source.)

##### 3. Checklist Inicial

Antes de iniciar a prática, o estudante deve ter:

- Caderno ou folhas para anotações
- Caneta ou lápis
- Computador ou notebook (se for usar ferramenta digital)
- Conexão com a internet
- Acesso ao material da aula (slides ou PDF)
- Ambiente: sala de aula ou laboratório de informática

##### 4. Passo a Passo do Docente (Aula de até 50 minutos)

###### Como conduzir a aula

- Retome a aula anterior sobre metodologias de desenvolvimento.
- Apresente a UML como uma linguagem gráfica para modelagem de sistemas.
- Destaque que a UML não é uma metodologia, mas um conjunto de notações.
- Explique os principais diagramas apresentados na aula:
- Diagrama de Classes
- Diagrama de Casos de Uso
- Diagrama de Sequência
- Diagrama de Atividades
- Diagrama de Estados
- Diagrama de Componentes
- Mostre exemplos simples de cada tipo.
- Apresente a atividade prática.

###### Preparações necessárias

- Disponibilizar exemplos visuais de diagramas
- Preparar um cenário simples de sistema (ex.: sistema escolar, loja online etc.)
- Garantir acesso às ferramentas digitais, se utilizadas

###### Alertas e pontos de atenção

- Alunos podem confundir tipos de diagramas
- Reforce a função específica de cada um
- Oriente para foco na compreensão conceitual, não na perfeição gráfica

###### Dinâmica sugerida

Explicação → demonstração → prática guiada → apresentação

###### Gerenciamento de tempo (50 minutos)

- Revisão conceitual: 15 minutos
- Demonstração dos diagramas: 10 minutos
- Execução da atividade: 15 minutos
- Socialização e fechamento: 10 minutos

##### 5. Atividade Prática — Descrição Geral

O estudante deverá escolher um sistema simples e criar um diagrama UML representando algum aspecto desse sistema.

Sugestões de sistemas:

- Sistema de biblioteca
- Aplicativo de tarefas
- Loja virtual
- Sistema escolar
O tipo de diagrama pode ser definido pelo professor ou escolhido pelo aluno (ex.: casos de uso ou classes).

A atividade simula a etapa inicial de modelagem conceitual de um software.

A habilidade desenvolvida será a capacidade de representar sistemas por meio de modelos visuais padronizados.

##### 6. Metodologia Ativa Utilizada

- Aprendizagem baseada em problemas (PBL)
- Ensino por descoberta
- Aprendizagem prática
Elementos de Lemov aplicados:

- Objetivo claro
- Participação ativa
- Produção visível
- Estruturação do raciocínio

##### 7. Passo a Passo da Atividade Prática (para os alunos)

- Escolha um sistema simples para modelar.
- Identifique os principais elementos desse sistema (usuários, funcionalidades, componentes etc.).
- Escolha um tipo de diagrama UML adequado.
- Organize as informações necessárias para o diagrama.
- Desenhe o diagrama no caderno ou em ferramenta digital.
- Revise o diagrama para verificar clareza e coerência.
- Prepare-se para apresentar sua solução.

##### 8. Exemplo ou Demonstração

Exemplo — Sistema de Biblioteca

Diagrama de Casos de Uso:

Ator: Aluno

Casos de uso:

- Consultar livro
- Emprestar livro
- Devolver livro
Esse diagrama mostra como o usuário interage com o sistema.

##### 9. Resultado Esperado

O estudante deverá apresentar:

- Um diagrama UML simples e organizado
- Identificação correta dos elementos do sistema
- Coerência entre o sistema escolhido e o tipo de diagrama
O professor poderá verificar o aprendizado observando:

- Compreensão do propósito da UML
- Clareza visual do diagrama
- Uso adequado dos conceitos

##### 10. Formato de Entrega da Atividade

- Formato: Desenho no caderno, folha ou arquivo digital
- Nome do arquivo (se digital): Diagrama_UML_NomeAluno
- Local de entrega: Avaliação em sala ou envio via Google Classroom/Drive
- Prazo sugerido: Durante a aula

##### 11. Encerramento e Reflexão

Finalize a aula conduzindo uma reflexão orientada:

- Por que diagramas são importantes no desenvolvimento de software?
- Qual diagrama foi mais fácil de entender? Por quê?
- Como a modelagem ajuda a comunicação entre membros da equipe?
