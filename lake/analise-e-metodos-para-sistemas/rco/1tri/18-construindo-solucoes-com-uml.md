---
titulo: "Construindo Soluções com UML"
tipo: rco-seed
disciplina: analise-e-metodos-para-sistemas
sigla_rco: AMS
trimestre: 1
ordem_rco: 18
serie: 1
aula_rco: "Aula 18"
slides: 24
tem_atividade: true
tem_pratica: true
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/AMS/1TRI/18-construindo-solucoes-com-uml/18-construindo-solucoes-com-uml.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/AMS/1TRI/18-construindo-solucoes-com-uml/AULA 18_ATIVIDADE_ANÁLISE E MÉTODO PARA SISTEMAS.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/AMS/1TRI/18-construindo-solucoes-com-uml/AULA 18_PRÁTICA_ANÁLISE E MÉTODO PARA SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Construindo Soluções com UML

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- ANÁLISE E MÉTODO PARA SISTEMAS
- 1ª Série
- Construindo Soluções com UML
- Aula 18

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
- Aprender sobre construção
- da solução utilizando UML.
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
- DOWNLOAD: Projeto do Curso:
- https://cursos.alura.com.br/course/uml-fundamentos-na-pratica/task/42929

_2 imagem(ns) no slide._

### Slide 6

- Aula anterior
- Estudamos
- sobre as questões de requisitos utilizados na UML.

_1 imagem(ns) no slide._

### Slide 7

- Para pensarmos juntos...
- A equipe anterior havia documentado parte do processo, mas Lucas percebeu que havia lacunas na compreensão das interações entre os componentes do sistema.
- Lucas é um jovem desenvolvedor que acabou de ser contratado por uma startup focada em tecnologia educacional. Em sua primeira semana, foi-lhe pedido que revisasse e melhorasse um sistema de inscrição para cursos online.
- https://joanpaon.files.wordpress.com/2013/05/logo.png

_1 imagem(ns) no slide._

### Slide 8

- Para pensarmos juntos...
- Como são representados no Diagrama de Sequência os processos automáticos, como enviar um email de confirmação após uma ação do usuário?
- 3 minutos
- Pesquise e escreva no caderno
- Decidindo usar um Diagrama de Sequência para mapear a interação dos objetos durante o processo de inscrição, Lucas teve um dilema. Ele se perguntou: "Em um Diagrama de Sequência, como devo representar um processo que ocorre de forma automática após um aluno se inscrever, como o envio de um email de confirmação?”

_2 imagem(ns) no slide._

### Slide 9

- Resposta
- No Diagrama de Sequência, os processos automáticos, como o envio de um email de confirmação, são geralmente representados como uma mensagem (seta) originada do objeto que realiza a ação (por exemplo, "Sistema de Inscrição") para o objeto responsável pela ação automática (por exemplo, "Sistema de E-mail").
- Isso mostra que, após o usuário se inscrever, o sistema automaticamente envia um comando ao Sistema de E-mail para disparar a mensagem de confirmação.
- https://www.showmetech.com.br/wp-content/uploads//2018/12/email_ss_1920-1920x1024.png

### Slide 10

- Diagramas de Atividade
- Estes são uma espécie de diagrama de fluxo que representa o fluxo de controle ou sequência de atividades no sistema. Eles mostram o fluxo de uma atividade para outra, ilustrando como o sistema funciona passo a passo. Em termos simples, imagine um gráfico que mostra todos os passos que um usuário poderia seguir ao utilizar uma aplicação, desde o início até o fim.
- https://d2slcw3kip6qmk.cloudfront.net/marketing/pages/chart/UML-activity-diagram-examples-transparent.png

_1 imagem(ns) no slide._

### Slide 11

- Diagramas de Sequência
- Cada objeto é representado como uma coluna, e as mensagens enviadas entre eles são mostradas como setas.
- Os diagramas de sequência são usados para visualizar interações entre objetos em um sistema ao longo do tempo.
- Eles ilustram a sequência de mensagens e operações em um cenário específico.
- https://d2slcw3kip6qmk.cloudfront.net/marketing/pages/chart/UML-sequence-diagram-featured-image.png

_1 imagem(ns) no slide._

### Slide 12

- Diagramas de Sequência
- Um exemplo simples poderia ser o processo de um cliente fazendo uma compra em uma loja online: desde o momento em que ele escolhe um item até a confirmação de sua compra.

_1 imagem(ns) no slide._

### Slide 13

- Vantagens
- Clareza de Processo: Ambos os diagramas permitem uma representação visual clara de processos complexos, tornando-os mais fáceis de entender.
- Facilita a Comunicação: Permitem que as equipes discutam processos e interações de forma eficaz, garantindo que todos estejam na mesma página.

_1 imagem(ns) no slide._

### Slide 14

- Desvantagens
- Necessidade de Atualização: Como todo modelo, eles precisam ser atualizados frequentemente para refletir mudanças no sistema.
- Complexidade em Grandes Sistemas: Em sistemas muito extensos, pode ser desafiador representar todas as atividades ou sequências sem que o diagrama se torne muito complicado.

_1 imagem(ns) no slide._

### Slide 15

- Ainda sobre UML, vamos conhecer praticando?
- Na plataforma Alura vamos acessar o seguinte curso:
- Os próximos itens serão para guiá-los nas principais atividades que serão necessárias para o entendimento da aula de hoje, embora existam mais atividades na plataforma Alura, em sala iremos desenvolver as essenciais.
- A recomendação é que você continue esse curso extraclasse, pois ele traz um conteúdo essencial para compreender sobre o referido tema.
- Link para o curso: https://cursos.alura.com.br/course/uml-fundamentos-na-pratica

_3 imagem(ns) no slide._

### Slide 16

- Representação Diagramas UML parte 2
- 12 minutos
- A UML (Unified Modeling Language) é uma linguagem padrão para modelar sistemas.
- Link para tarefa: https://cursos.alura.com.br/course/uml-fundamentos-na-pratica/task/42579
- Os diagramas UML ajudam a visualizar e documentar diferentes aspectos de um sistema. Eles abrangem desde requisitos funcionais até componentes concretos. O objetivo é facilitar a compreensão, design e manutenção de sistemas. Eles são essenciais para engenheiros de software e stakeholders.
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 17

- Diagrama de Atividades
- 09 minutos
- O Diagrama de Atividades UML modela fluxos de trabalho e processos.
- Link para tarefa: https://cursos.alura.com.br/course/uml-fundamentos-na-pratica/task/42580
- Ele representa a sequência de atividades e decisões dentro de um sistema. Semelhante a um fluxograma, ele usa símbolos como setas e losangos para indicar fluxos e pontos de decisão. Esse diagrama é vital para visualizar e otimizar processos de negócios ou algoritmos complexos.
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 18

- Diagrama de Sequência
- 10 minutos
- O Diagrama de Sequência UML mostra interações entre objetos em uma sequência temporal específica.
- Link para tarefa: https://cursos.alura.com.br/course/uml-fundamentos-na-pratica/task/42581
- Ele destaca a troca de mensagens e a ordem de eventos entre objetos ao longo do tempo. Com barras de vida verticais e setas horizontais, este diagrama representa a sequência de processos e a comunicação entre entidades em um sistema.
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 19

- Reflexão sobre o modelo
- 8 minutos
- A reflexão sobre um modelo ajuda a entender suas forças e fraquezas.
- Link para tarefa: https://cursos.alura.com.br/course/uml-fundamentos-na-pratica/task/43748
- Avaliando-o, é possível identificar ajustes necessários. O feedback é essencial para sua evolução e eficácia. O modelo em constante revisão adapta-se melhor às mudanças e desafios.
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 20

- Vamos praticar?
- Prepare-se, porque nessa atividade, você vai sair do modo aprender e entrar direto no modo praticar.
- A atividade prática vai colocar você diante de um desafio real: sensação de ver seu próprio código aparecer online! Acessível, documentado e pronto para o mundo!

_1 imagem(ns) no slide._

### Slide 21

- O que vimos na aula de hoje:
- Reforçamos o aprendizado em relação aos diagramas de atividade e sequência UML

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

_Fonte: AULA 18_ATIVIDADE_ANÁLISE E MÉTODO PARA SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

ANÁLISE E MÉTODO PARA SISTEMAS

1ª SÉRIE

ATIVIDADE AULA 18

Questão 1

O que é um Diagrama de Atividade no UML?

A) Uma representação das interações entre objetos em um sistema.

B) Um gráfico que ilustra a sequência de ações que ocorrem em um sistema.

C) Um diagrama que mostra o fluxo de controle ou fluxo de objetos entre atividades em um sistema.

D) Uma representação visual de um banco de dados e suas relações.

Resposta:

C) Um diagrama que mostra o fluxo de controle ou fluxo de objetos entre atividades em um sistema.

Questão 2

Qual é a principal finalidade do Diagrama de Sequência no UML?

A) Descrever a estrutura estática de um sistema.

B) Ilustrar o fluxo de atividades dentro de um sistema.

C) Mostrar a sequência de mensagens trocadas entre objetos e/ou atores em um cenário específico.

D) Mapear as dependências entre os pacotes em um sistema.

Resposta:

C) Mostrar a sequência de mensagens trocadas entre objetos e/ou atores em um cenário específico.

## Prática

_Fonte: AULA 18_PRÁTICA_ANÁLISE E MÉTODO PARA SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

ANÁLISE E MÉTODO PARA SISTEMAS

1ª SÉRIE

ATIVIDADE PRÁTICA AULA 18

##### 1. Objetivo da Aula Prática

Ao final desta aula prática, o estudante deverá:

- Aprender como utilizar diagramas UML para construir soluções e representar o funcionamento de um sistema.
- Desenvolver a habilidade prática de modelar processos e interações utilizando diagramas de atividade e de sequência.
- Ser capaz de produzir representações visuais de um fluxo de sistema completo, incluindo ações do usuário e processos automáticos.

##### 2. Ferramentas Recomendadas

Caderno ou Folha A4

- Para que serve: Esboço inicial dos diagramas UML.
- Por que é adequada ao tema: Permite planejamento antes da formalização digital.
- Como facilita o aprendizado: Ajuda na compreensão dos fluxos e interações.
draw.io / diagrams.net (https://app.diagrams.net)

- Para que serve: Criação digital de diagramas de atividade e sequência.
- Por que é adequada ao tema: Possui bibliotecas específicas de UML.
- Como facilita o aprendizado: Permite construir diagramas claros e profissionais.
Google Slides ou Docs (https://slides.google.com / https://docs.google.com)

- Para que serve: Organização e apresentação dos diagramas produzidos.
- Por que é adequada ao tema: Facilita compartilhamento e revisão.
- Como facilita o aprendizado: Ajuda na comunicação das soluções modeladas.
(Ferramentas gratuitas, online ou open source.)

##### 3. Checklist Inicial

Antes de iniciar a prática, o estudante deve ter:

- Caderno ou folhas para rascunho
- Caneta ou lápis
- Computador ou notebook
- Conexão com a internet
- Acesso ao material da aula
- Ambiente: sala de aula ou laboratório de informática

##### 4. Passo a Passo do Docente (Aula de até 50 minutos)

###### Como conduzir a aula

- Retome a aula anterior sobre requisitos e UML.
- Apresente o cenário da aula: Lucas revisando um sistema de inscrição para cursos online.
- Explique a necessidade de compreender as interações entre componentes do sistema.
- Destaque os diagramas abordados no material:
- Diagrama de Atividades — fluxo de processos
- Diagrama de Sequência — interação entre objetos ao longo do tempo
- Explique como processos automáticos (ex.: envio de e-mail de confirmação) são representados como mensagens entre objetos.
- Apresente a atividade prática.

###### Preparações necessárias

- Preparar um cenário simples (ex.: sistema de inscrição online)
- Disponibilizar exemplos visuais de diagramas
- Garantir acesso às ferramentas digitais

###### Alertas e pontos de atenção

- Alunos podem confundir fluxo de atividades com sequência temporal
- Reforce que:
- Atividade = fluxo de ações
- Sequência = troca de mensagens entre objetos
- Oriente para diagramas simples e legíveis

###### Dinâmica sugerida

Situação-problema → explicação → prática guiada → socialização

###### Gerenciamento de tempo (50 minutos)

- Contextualização e explicação: 15 minutos
- Demonstração dos diagramas: 10 minutos
- Execução da prática: 15 minutos
- Discussão e fechamento: 10 minutos

##### 5. Atividade Prática — Descrição Geral

O estudante deverá modelar um sistema de inscrição online utilizando dois diagramas UML complementares:

- Diagrama de Atividades — representando o fluxo do processo
- Diagrama de Sequência — representando as interações entre objetos
O cenário simula um sistema em que um usuário se inscreve e recebe automaticamente um e-mail de confirmação.

A habilidade desenvolvida será a capacidade de representar o comportamento e a dinâmica de um sistema de software.

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
- Identifique as etapas do processo de inscrição no sistema.
- Desenhe um Diagrama de Atividades representando esse fluxo.
- Identifique os objetos envolvidos (ex.: Usuário, Sistema de Inscrição, Sistema de E-mail).
- Desenhe um Diagrama de Sequência mostrando a comunicação entre esses objetos.
- Inclua no diagrama o envio automático de e-mail de confirmação.
- Revise os diagramas para verificar coerência e clareza.
- Prepare-se para apresentar sua solução.

##### 8. Exemplo ou Demonstração

Exemplo — Sistema de Inscrição Online

Diagrama de Atividades:

Início → Preencher formulário → Confirmar inscrição → Processar dados → Enviar confirmação → Fim

Diagrama de Sequência:

Usuário → Sistema de Inscrição → Sistema de E-mail → Usuário

O envio automático de e-mail é representado como uma mensagem entre sistemas.

##### 9. Resultado Esperado

O estudante deverá apresentar:

- Um diagrama de atividades completo
- Um diagrama de sequência correspondente
- Coerência entre fluxo e interações
O professor poderá verificar o aprendizado observando:

- Uso correto dos conceitos de UML
- Clareza visual dos diagramas
- Representação adequada do processo automático

##### 10. Formato de Entrega da Atividade

- Formato: Desenho no caderno, folha ou arquivo digital
- Nome do arquivo (se digital): UML_Inscricao_NomeAluno
- Local de entrega: Avaliação em sala ou envio digital, conforme orientação
- Prazo sugerido: Durante a aula

##### 11. Encerramento e Reflexão

Finalize a aula promovendo uma reflexão orientada:

- Por que usar diferentes diagramas para representar o mesmo sistema?
- Qual diagrama foi mais fácil de entender? Por quê?
- Como esses modelos ajudam no desenvolvimento real de software?
