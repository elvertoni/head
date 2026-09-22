---
titulo: "Requisitos e UML"
tipo: rco-seed
disciplina: analise-e-metodos-para-sistemas
sigla_rco: AMS
trimestre: 1
ordem_rco: 17
serie: 1
aula_rco: "Aula 17"
slides: 23
tem_atividade: true
tem_pratica: true
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/AMS/1TRI/17-requisitos-e-sua-representacao-na-uml/17-requisitos-e-sua-representacao-na-uml.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/AMS/1TRI/17-requisitos-e-sua-representacao-na-uml/AULA 17_ATIVIDADE_ANÁLISE E MÉTODO PARA SISTEMAS.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/AMS/1TRI/17-requisitos-e-sua-representacao-na-uml/AULA 17_PRÁTICA_ANÁLISE E MÉTODO PARA SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Requisitos e UML

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- ANÁLISE E MÉTODO PARA SISTEMAS
- 1ª Série
- Requisitos e UML
- Aula 17

_1 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- COMPETÊNCIA(S) A SER(EM) DESENVOLVIDA(S) NESTA AULA:
- De acordo com o Plano de Curso de Desenvolvimento de Sistemas:
- HABILIDADE(S) A SER(EM) DESENVOLVIDA(S) NESTA AULA:
- Dimensionar requisitos e funcionalidades do sistema.
- Realizar o levantamento de requisitos de sistemas.

_1 imagem(ns) no slide._

### Slide 4

- Nesta aula vamos:
- Aprender sobre requisitos e Unified Modeling Language (UML).
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store
- https://yuml.me/images/stick_graphic.png

_4 imagem(ns) no slide._

### Slide 5

- Este material foi elaborado a partir da análise do plano de curso e reúne os conhecimentos essenciais para o Técnico em Desenvolvimento de Sistemas. As aulas foram organizadas com foco na clareza conceitual, na construção gradual dos conteúdos e na utilização de metodologias ativas que favorecem a compreensão, a participação e o desenvolvimento de habilidades e competências de forma significativa.
- De acordo com a matriz curricular do Curso Técnico em Desenvolvimento de Sistemas, que traz em sua essência componentes estruturados para a realização de aulas práticas, cada unidade curricular deve contemplar, além da abordagem teórica, uma proposta de atividade prática a ser desenvolvida pelo professor. Essa orientação assegura a coerência entre o planejamento didático e o que está estabelecido na matriz, promovendo experiências formativas alinhadas ao perfil profissional previsto.
- O professor tem total autonomia para adaptar o conteúdo conforme o contexto da turma, ajustando exemplos, aprofundamentos e estratégias didáticas para otimizar a aprendizagem e a conexão com a prática profissional.
- Se houver falta de conexão ou indisponibilidade de internet durante a aula, os materiais abaixo podem ser utilizados como apoio para elaborar recursos complementares, garantindo a continuidade da abordagem teórica prevista.
- ATENÇÃO PROFESSOR!
- DOWNLOAD: Projeto do Curso:
- https://cursos.alura.com.br/course/uml-fundamentos-na-pratica/task/42928

_2 imagem(ns) no slide._

### Slide 6

- Aula anterior
- Iniciamos os estudos sobre UML, abordando os conceitos iniciais da abordagem.

_1 imagem(ns) no slide._

### Slide 7

- Para pensarmos juntos...
- João, um desenvolvedor júnior, foi incumbido de criar um sistema para uma biblioteca. Embora tivesse uma ideia básica das funcionalidades necessárias, ele estava confuso sobre a estrutura do sistema e como as funcionalidades se inter-relacionariam.

_1 imagem(ns) no slide._

### Slide 8

- Para pensarmos juntos...
- Como ele poderia visualizar a estrutura do sistema e suas funcionalidades de uma maneira que fizesse sentido tanto para ele quanto para os stakeholders?
- 3 minutos
- Pesquise e escreva no caderno

_3 imagem(ns) no slide._

### Slide 9

- Resposta
- João pode utilizar o UML para criar, mapeando a estrutura e relacionamentos entre as entidades do sistema. Ele também pode usar Diagramas de Caso de Uso para representar as principais funcionalidades e como os usuários (atores) interagem com o sistema.

_1 imagem(ns) no slide._

### Slide 10

- Diagramas de Classe
- São pilares da modelagem orientada a objetos no UML. Representam as classes (entidades), seus atributos, métodos e como se relacionam com outras classes. Permitem visualizar a estrutura estática do sistema. Ao criar um diagrama de classes, você está basicamente esboçando um esquema do sistema, algo semelhante a um diagrama de banco de dados.
- Fonte da imagem: https://spaceprogrammer.com/wp-content/uploads/2017/09/notacao-de-diagrama-de-classe-3.jpg

_1 imagem(ns) no slide._

### Slide 11

- Diagramas de Caso de Uso
- Concentram-se em representar as funcionalidades do sistema e sua interação com atores externos. Não se aprofundam em detalhes técnicos, mas sim no comportamento e funcionalidades. São essenciais para entender os requisitos do sistema e como os usuários interagem com ele.
- Fonte da imagem: https://images.ctfassets.net/w6r2i5d8q73s/5550PvEga3T2m2FxszitBb/d949e92ec6036b610501b87dc3101a36/M2_2_3_columns_template_picker_UML_diagram_001

_1 imagem(ns) no slide._

### Slide 12

- Finalidade e Utilização
- Enquanto o diagrama de classes se concentra na estrutura e composição do sistema, o diagrama de casos de uso se concentra no comportamento e requisitos do sistema. Juntos, fornecem uma visão completa - estática e dinâmica - de um sistema.
- https://media.istockphoto.com/id/1272853443/pt/vetorial/uml-unified-modeling-language-acronym-business-concept.jpg?s=612x612&w=0&k=20&c=d-SYHqbrbgMu7QDu23h6Ebfd55Jk8K8LNVAI3JNGMBw=

_1 imagem(ns) no slide._

### Slide 13

- Vantagens
- Ambos os diagramas auxiliam na clareza e precisão durante o desenvolvimento, permitindo uma melhor comunicação entre desenvolvedores e stakeholders. Eles ajudam na identificação precoce de erros e no alinhamento das expectativas.

### Slide 14

- Desvantagens
- A precisão excessiva pode levar a diagramas complicados, tornando-os difíceis de entender. Também, a criação de diagramas requer tempo e pode atrasar a fase de codificação.

_1 imagem(ns) no slide._

### Slide 15

- Ainda sobre UML, vamos conhecer praticando?
- Na plataforma Alura vamos acessar o seguinte curso:
- Os próximos itens serão para guiá-los nas principais atividades que serão necessárias para o entendimento da aula de hoje, embora existam mais atividades na plataforma Alura, em sala iremos desenvolver as essenciais.
- A recomendação é que você continue esse curso extraclasse, pois ele traz um conteúdo essencial para compreender sobre o referido tema.
- Link para o curso: https://cursos.alura.com.br/course/uml-fundamentos-na-pratica

_3 imagem(ns) no slide._

### Slide 16

- Representação Diagramas UML parte 1
- 13 minutos
- Diagramas UML oferecem visualizações padronizadas de sistemas.
- Link para tarefa: https://cursos.alura.com.br/course/uml-fundamentos-na-pratica/task/42576
- Diversos diagramas abordam aspectos variados, como estrutura e comportamento.
- Destacam-se diagramas de classes, sequência e atividades.
- Ajudam desenvolvedores a compreender e criar sistemas.
- Indispensáveis em engenharia de software moderna.
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 17

- Diagrama de Classes
- 9 minutos
- Diagrama de Classes é um pilar da UML.
- Link para tarefa: https://cursos.alura.com.br/course/uml-fundamentos-na-pratica/task/42577
- Representa estrutura e relações de classes.
- Mostra atributos, métodos e associações.
- Essencial para modelar sistemas orientados a objetos.
- Facilita o entendimento da arquitetura do software.
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 18

- Diagrama de Casos de Uso
- 9 minutos
- Diagrama de Casos de Uso destaca interações do sistema.
- Link para tarefa: https://cursos.alura.com.br/course/uml-fundamentos-na-pratica/task/42578
- Mostra atores e suas funcionalidades associadas.
- Representa cenários de uso do sistema.
- Visualiza relações entre atores e casos.
- Essencial para entender requisitos e funcionalidades.
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 19

- Vamos praticar?
- Nesta atividade, você vai assumir o papel de um analista de sistemas que precisa ajudar a modelar um sistema de biblioteca. Para isso, você usará uma das linguagens mais importantes da engenharia de software: a UML (Unified Modeling Language).

_1 imagem(ns) no slide._

### Slide 20

- O que vimos na aula de hoje:
- Aprendemos a representação de diagramas UML.

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

_Fonte: AULA 17_ATIVIDADE_ANÁLISE E MÉTODO PARA SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

ANÁLISE E MÉTODO PARA SISTEMAS

1ª SÉRIE

ATIVIDADE AULA 17

Questão 1

O que o Diagrama de Classe do UML representa primariamente?

a) Funcionalidades do sistema.

b) Estrutura estática do sistema.

c) Comportamento dinâmico do sistema.

d) Relações entre usuários.

Resposta: b) Estrutura estática do sistema.

Questão 2

Qual dos seguintes é um objetivo principal dos Diagramas de Caso de Uso?

a) Detalhar atributos das classes.

b) Mostrar a hierarquia de classes.

c) Representar interações entre objetos durante a execução.

d) Descrever como os atores externos interagem com o sistema.

Resposta: d) Descrever como os atores externos interagem com o sistema.

## Prática

_Fonte: AULA 17_PRÁTICA_ANÁLISE E MÉTODO PARA SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

ANÁLISE E MÉTODO PARA SISTEMAS

1ª SÉRIE

ATIVIDADE PRÁTICA AULA 17

##### 1. Objetivo da Aula Prática

Ao final desta aula prática, o estudante deverá:

- Aprender como a UML é utilizada para representar requisitos e estrutura de sistemas.
- Desenvolver a habilidade prática de diferenciar e aplicar diagramas de classes e diagramas de casos de uso.
- Ser capaz de produzir representações visuais simples de um sistema, mostrando tanto sua estrutura quanto suas funcionalidades.

##### 2. Ferramentas Recomendadas

Caderno ou Folha A4

- Para que serve: Esboço manual dos diagramas UML.
- Por que é adequada ao tema: Permite experimentar a modelagem de forma rápida e sem dependência tecnológica.
- Como facilita o aprendizado: Ajuda na compreensão dos elementos e símbolos.
draw.io / diagrams.net (https://app.diagrams.net)

- Para que serve: Criação digital de diagramas UML.
- Por que é adequada ao tema: Possui biblioteca específica para diagramas de classes e casos de uso.
- Como facilita o aprendizado: Permite gerar diagramas claros e organizados.
Google Docs ou Slides (https://docs.google.com / https://slides.google.com)

- Para que serve: Organização e apresentação do trabalho produzido.
- Por que é adequada ao tema: Facilita registro e compartilhamento.
- Como facilita o aprendizado: Permite revisão e explicitação do raciocínio.
(Ferramentas gratuitas, online ou open source.)

##### 3. Checklist Inicial

Antes de iniciar a prática, o estudante deve ter:

- Caderno ou folhas para anotações
- Caneta ou lápis
- Computador ou notebook (opcional para versão digital)
- Conexão com a internet
- Acesso ao material da aula
- Ambiente: sala de aula ou laboratório de informática

##### 4. Passo a Passo do Docente (Aula de até 50 minutos)

###### Como conduzir a aula

- Retome a aula anterior sobre conceitos fundamentais da UML.
- Apresente o cenário do material: João precisa modelar um sistema para uma biblioteca, mas não sabe como visualizar a estrutura e funcionalidades.
- Explique que a UML permite representar o sistema sob duas perspectivas principais:
- Estrutura (diagramas de classes)
- Comportamento e funcionalidades (diagramas de casos de uso)
- Destaque a finalidade e complementaridade desses diagramas.
- Apresente a atividade prática.

###### Preparações necessárias

- Preparar um cenário simples (ex.: sistema de biblioteca escolar)
- Disponibilizar exemplos visuais de diagramas
- Garantir acesso às ferramentas, se necessário

###### Alertas e pontos de atenção

- Alunos podem misturar estrutura e funcionalidades no mesmo diagrama
- Reforce a diferença entre classe (estrutura) e caso de uso (funcionalidade)
- Oriente para diagramas simples e claros

###### Dinâmica sugerida

Situação-problema → explicação → prática guiada → socialização

###### Gerenciamento de tempo (50 minutos)

- Revisão e contextualização: 10 minutos
- Explicação conceitual: 10 minutos
- Execução da prática: 20 minutos
- Apresentação e fechamento: 10 minutos

##### 5. Atividade Prática — Descrição Geral

O estudante deverá modelar um sistema simples utilizando dois tipos de diagramas UML:

- Diagrama de Classes (estrutura do sistema)
- Diagrama de Casos de Uso (funcionalidades e interação com usuários)
Sugestão de sistema: biblioteca escolar, conforme o cenário apresentado.

A atividade simula a fase de análise e projeto inicial de software.

A habilidade desenvolvida será a capacidade de representar um sistema sob diferentes perspectivas utilizando UML.

##### 6. Metodologia Ativa Utilizada

- Aprendizagem baseada em problemas (PBL)
- Ensino por descoberta
- Aprendizagem prática
Elementos de Lemov aplicados:

- Objetivo claro
- Participação ativa
- Produção visível
- Estruturação do pensamento

##### 7. Passo a Passo da Atividade Prática (para os alunos)

- Leia o cenário apresentado pelo professor.
- Identifique as principais entidades do sistema (ex.: Livro, Usuário, Empréstimo).
- Defina atributos básicos dessas entidades.
- Desenhe um diagrama de classes simples mostrando as relações entre elas.
- Identifique os atores do sistema (ex.: Aluno, Bibliotecário).
- Liste as funcionalidades principais (ex.: emprestar livro, devolver livro, consultar catálogo).
- Desenhe um diagrama de casos de uso representando essas interações.
- Revise ambos os diagramas para verificar coerência.
- Prepare-se para explicar seu modelo.

##### 8. Exemplo ou Demonstração

Exemplo — Sistema de Biblioteca

Diagrama de Classes:

- Classe Livro
- Classe Usuário
- Classe Empréstimo
- Relações entre essas classes
Diagrama de Casos de Uso:

Ator: Aluno

Casos de uso:

- Consultar livro
- Emprestar livro
- Devolver livro

##### 9. Resultado Esperado

O estudante deverá apresentar:

- Um diagrama de classes simples
- Um diagrama de casos de uso correspondente
- Coerência entre estrutura e funcionalidades
O professor poderá verificar o aprendizado observando:

- Uso correto dos conceitos da UML
- Clareza visual dos diagramas
- Adequação ao cenário proposto

##### 10. Formato de Entrega da Atividade

- Formato: Desenho no caderno, folha ou arquivo digital
- Nome do arquivo (se digital): UML_Biblioteca_NomeAluno
- Local de entrega: Avaliação em sala ou envio digital, conforme orientação
- Prazo sugerido: Durante a aula

##### 11. Encerramento e Reflexão

Finalize a aula conduzindo uma reflexão orientada:

- Por que representar estrutura e funcionalidades separadamente é importante?
- Como a UML facilita a comunicação entre equipe técnica e stakeholders?
- Em que situações diagramas detalhados são mais necessários?
