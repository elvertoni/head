---
titulo: "Implantação de Soluções com UML"
tipo: rco-seed
disciplina: analise-e-metodos-para-sistemas
sigla_rco: AMS
trimestre: 1
ordem_rco: 19
serie: 1
aula_rco: "Aula 19"
slides: 24
tem_atividade: true
tem_pratica: true
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/AMS/1TRI/19-implantacao-de-solucoes-com-uml/19-implantacao-de-solucoes-com-uml.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/AMS/1TRI/19-implantacao-de-solucoes-com-uml/AULA 19_ATIVIDADE_ANÁLISE E MÉTODO PARA SISTEMAS.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/AMS/1TRI/19-implantacao-de-solucoes-com-uml/AULA 19_PRÁTICA_ANÁLISE E MÉTODO PARA SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Implantação de Soluções com UML

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- ANÁLISE E MÉTODO PARA SISTEMAS
- 1ª Série
- Implantação de Soluções com UML
- Aula 19

_1 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- COMPETÊNCIA(S) A SER(EM) DESENVOLVIDA(S) NESTA AULA:
- De acordo com o Plano de Curso de Desenvolvimento de Sistemas:
- HABILIDADE(S) A SER(EM) DESENVOLVIDA(S) NESTA AULA:
- Executar manutenção de programas de computador e suporte técnico.
- Indicar utilização adequada do sistema projetado.

_1 imagem(ns) no slide._

### Slide 4

- Nesta aula vamos:
- Aprender sobre a implantação da solução utilizando UML.
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store
- https://www.codercrunch.com/content/skill/images/uml-f.png

_4 imagem(ns) no slide._

### Slide 5

- Este material foi elaborado a partir da análise do plano de curso e reúne os conhecimentos essenciais para o Técnico em Desenvolvimento de Sistemas. As aulas foram organizadas com foco na clareza conceitual, na construção gradual dos conteúdos e na utilização de metodologias ativas que favorecem a compreensão, a participação e o desenvolvimento de habilidades e competências de forma significativa.
- De acordo com a matriz curricular do Curso Técnico em Desenvolvimento de Sistemas, que traz em sua essência componentes estruturados para a realização de aulas práticas, cada unidade curricular deve contemplar, além da abordagem teórica, uma proposta de atividade prática a ser desenvolvida pelo professor. Essa orientação assegura a coerência entre o planejamento didático e o que está estabelecido na matriz, promovendo experiências formativas alinhadas ao perfil profissional previsto.
- O professor tem total autonomia para adaptar o conteúdo conforme o contexto da turma, ajustando exemplos, aprofundamentos e estratégias didáticas para otimizar a aprendizagem e a conexão com a prática profissional.
- Se houver falta de conexão ou indisponibilidade de internet durante a aula, os materiais abaixo podem ser utilizados como apoio para elaborar recursos complementares, garantindo a continuidade da abordagem teórica prevista.
- ATENÇÃO PROFESSOR!
- DOWNLOAD: Projeto do Curso:
- https://cursos.alura.com.br/course/uml-fundamentos-na-pratica/task/42932

_2 imagem(ns) no slide._

### Slide 6

- Aula anterior
- Aprendemos sobre os diagramas de atividades e sequência da UML

_1 imagem(ns) no slide._

### Slide 7

- Para pensarmos juntos...
- Ela é responsável por modelar o sistema de controle para um portão eletrônico que possui três estados principais: Aberto, Fechado e Trancado. Ana decide usar um Diagrama de Máquina de Estado para modelar o comportamento do portão, mas encontra um desafio:
- https://o.remove.bg/downloads/9cef3e26-b27d-468d-9be9-0fbf579a931d/image-removebg-preview.png

_1 imagem(ns) no slide._

### Slide 8

- Para pensarmos juntos...
- Como Ana pode modelar a transição de estados no Diagrama de Máquina de Estado para garantir que o portão eletrônico funcione conforme os requisitos de segurança?
- 3 minutos
- Responda em seu caderno!
- ela precisa garantir que o portão não vá para o estado Trancado a menos que esteja Fechado e que, ao receber o comando de abrir, ele só transite para o estado Aberto se não estiver Trancado.

_3 imagem(ns) no slide._

### Slide 9

- Resposta
- Ana deve representar os estados "Aberto", "Fechado" e "Trancado" como nós no diagrama. Para assegurar que o portão não se tranque a menos que esteja fechado, ela pode modelar uma condição de guarda na transição para o estado "Trancado" que verifique se o estado atual é "Fechado".

_1 imagem(ns) no slide._

### Slide 10

- Resposta
- Da mesma forma, a transição para "Aberto" deve ter uma condição que só permita essa ação se o estado atual não for "Trancado". As condições de guarda servirão como verificações lógicas antes das transições de estado acontecerem, assegurando a sequência correta de operações e a integridade do sistema de segurança.

_1 imagem(ns) no slide._

### Slide 11

- Representação Diagramas UML
- Os diagramas de Máquina de Estado e Componentes são duas importantes ferramentas de modelagem dentro da Linguagem de Modelagem Unificada (UML), que é um padrão de modelagem de sistemas complexos, principalmente de software.
- https://images.tcdn.com.br/img/img_prod/436223/controle_remoto_peccinin_para_motor_de_portao_559_2_039cf9f50ecd055b28599a0071c26200.png

_1 imagem(ns) no slide._

### Slide 12

- Diagrama de Máquina de Estado (State Machine Diagram)
- Imagine um objeto "Porta" que pode estar nos estados "Aberta", "Fechada", ou "Trancada". O diagrama de máquina de estado mostrará como e quando a porta muda entre esses estados em resposta a gatilhos como "girar a maçaneta" ou "inserir a chave".
- Este diagrama é usado para modelar o comportamento de entidades que possuem um número finito de estados ou modos. É extremamente útil para representar objetos que precisam responder a eventos externos e mudar de estado como resultado desses eventos.

_1 imagem(ns) no slide._

### Slide 13

- Diagrama de Componentes (Component Diagram)
- Este diagrama oferece uma visão de alto nível do sistema de software, mostrando seus componentes principais e suas relações. Um "componente" na UML é uma parte modular e substituível do sistema que encapsula seu conteúdo e tem uma interface claramente definida. O diagrama de componentes é semelhante a um diagrama de blocos em eletrônica ou um diagrama de arquitetura em construção civil, e é muito útil para entender como diferentes partes de um sistema de software se conectam e interagem entre si, como em um aplicativo com vários serviços que comunicam através de APIs.

_1 imagem(ns) no slide._

### Slide 14

- Aplicação
- Ambos os diagramas são vitais para entender diferentes aspectos do sistema que está sendo modelado. O diagrama de máquina de estado se concentra em descrever os estados possíveis de um objeto e as transições permitidas entre esses estados. Já o diagrama de componentes se preocupa com a estrutura do sistema e como as partes individuais se encaixam e se comunicam para formar um todo funcional.
- https://d2slcw3kip6qmk.cloudfront.net/marketing/pages/chart/UML-state-diagram-tutorial/FeaturedImage.png

_1 imagem(ns) no slide._

### Slide 15

- Aplicação
- Ao projetar um sistema, os diagramas de máquina de estado podem ajudar a prever como um objeto se comportará e a identificar possíveis falhas ou condições de corrida. Os diagramas de componentes ajudam a dividir o sistema em partes gerenciáveis e a definir responsabilidades claras dentro da equipe de desenvolvimento.

_1 imagem(ns) no slide._

### Slide 16

- Ainda sobre UML, vamos conhecer praticando?
- Na plataforma Alura vamos acessar o seguinte curso:
- Os próximos itens serão para guiá-los nas principais atividades que serão necessárias para o entendimento da aula de hoje, embora existam mais atividades na plataforma Alura, em sala iremos desenvolver as essenciais.
- A recomendação é que você continue esse curso extraclasse, pois ele traz um conteúdo essencial para compreender sobre o referido tema.
- Link para o curso: https://cursos.alura.com.br/course/uml-fundamentos-na-pratica

_3 imagem(ns) no slide._

### Slide 17

- Representação Diagramas UML parte 3
- 9 minutos
- O diagrama de implantação UML ilustra a configuração física de hardware e software em um sistema.
- Link para tarefa: https://cursos.alura.com.br/course/uml-fundamentos-na-pratica/task/42582
- Ele mapeia os componentes de software aos dispositivos e mostra a comunicação entre os nós da rede.
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 18

- Diagrama de Máquina de Estado
- 8 minutos
- O Diagrama de Máquina de Estado UML é utilizado em caso que.
- Link para tarefa: https://cursos.alura.com.br/course/uml-fundamentos-na-pratica/task/42583
- Precisa modelar o comportamento de entidades que possuem um número finito de estados e transições entre esses estados, muitas vezes desencadeadas por eventos. Esse diagrama é útil para representar os ciclos de vida de objetos.
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 19

- Diagrama de Componentes
- 8 minutos
- O Diagrama de Componentes UML é usado para ilustrar a organização e as dependências entre um conjunto de componentes.
- Link para tarefa: https://cursos.alura.com.br/course/uml-fundamentos-na-pratica/task/42584
- Ele representa os componentes de software, suas interfaces e a relação entre eles, mostrando como o software é dividido em peças reutilizáveis e como essas peças interagem entre si.
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 20

- Vamos praticar?
- Prepare-se, porque nessa atividade, você vai sair do modo aprender e entrar direto no modo praticar.
- A atividade prática vai colocar você diante de um desafio real: sensação de ver seu próprio código aparecer online! Acessível, documentado e pronto para o mundo!

_1 imagem(ns) no slide._

### Slide 21

- O que vimos na aula de hoje:
- Reforçamos o aprendizado em relação aos diagramas de máquina de estado e componentes da UML.

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

_Fonte: AULA 19_ATIVIDADE_ANÁLISE E MÉTODO PARA SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

ANÁLISE E MÉTODO PARA SISTEMAS

1ª SÉRIE

ATIVIDADE AULA 19

Questão 1

Qual é o propósito de um Diagrama de Máquina de Estado na UML?

A) Documentar os diferentes estados de um objeto ao longo do tempo.

B) Representar a estrutura física do sistema.

C) Modelar a interação entre os usuários e o sistema.

D) Descrever a arquitetura de bancos de dados.

Comentário da Resposta Correta:

A alternativa correta é A) Documentar os diferentes estados de um objeto ao longo do tempo. Um Diagrama de Máquina de Estado é usado para modelar os estados pelos quais um objeto pode passar, assim como as transições baseadas em eventos que causam a mudança de um estado para outro.

Questão 2

O que é destacado em um Diagrama de Componentes na UML?

A) As colaborações entre os usuários e o sistema.

B) A distribuição de componentes em tempo de execução.

C) Os aspectos dinâmicos de um sistema como atividades e fluxos.

D) As partes modulares do sistema e suas inter-relações.

Comentário da Resposta Correta:

D) As partes modulares do sistema e suas inter-relações. Um Diagrama de Componentes é utilizado para mostrar como os componentes de um sistema de software estão organizados e interconectados. Ele ilustra a estrutura modular do sistema e como cada componente se relaciona com os outros.

## Prática

_Fonte: AULA 19_PRÁTICA_ANÁLISE E MÉTODO PARA SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

ANÁLISE E MÉTODO PARA SISTEMAS

1ª SÉRIE

ATIVIDADE PRÁTICA AULA 19

##### 1. Objetivo da Aula Prática

Ao final desta aula prática, o estudante deverá:

- Aprender como a UML é utilizada na fase de implantação de sistemas.
- Desenvolver a habilidade prática de modelar o comportamento e a estrutura de um sistema utilizando Diagramas de Máquina de Estado e de Componentes.
- Ser capaz de produzir representações visuais que mostrem estados de um objeto e a organização dos componentes de software.

##### 2. Ferramentas Recomendadas

Caderno ou Folha A4

- Para que serve: Esboço inicial dos diagramas UML.
- Por que é adequada ao tema: Permite compreender os conceitos antes da formalização digital.
- Como facilita o aprendizado: Ajuda na visualização dos estados e das relações entre componentes.
draw.io / diagrams.net (https://app.diagrams.net)

- Para que serve: Criação digital de diagramas UML.
- Por que é adequada ao tema: Possui bibliotecas específicas para diagramas de máquina de estado e componentes.
- Como facilita o aprendizado: Permite produzir modelos claros e organizados.
Google Slides ou Docs (https://slides.google.com / https://docs.google.com)

- Para que serve: Organização e apresentação da atividade.
- Por que é adequada ao tema: Facilita compartilhamento e revisão.
- Como facilita o aprendizado: Permite documentar a solução proposta.
(Ferramentas gratuitas, online ou open source.)

##### 3. Checklist Inicial

Antes de iniciar a prática, o estudante deve ter:

- Caderno ou folhas para rascunho
- Caneta ou lápis
- Computador ou notebook (preferencial)
- Conexão com a internet
- Acesso ao material da aula
- Ambiente adequado (sala ou laboratório)

##### 4. Passo a Passo do Docente (Aula de até 50 minutos)

###### Como conduzir a aula

- Retome rapidamente os diagramas de atividades e sequência estudados anteriormente.
- Apresente o novo foco: implantação da solução utilizando UML.
- Contextualize com o exemplo do material: sistema de controle de portão eletrônico com estados “Aberto”, “Fechado” e “Trancado”.
- Explique o papel dos diagramas abordados:
- Diagrama de Máquina de Estado: modela o comportamento ao longo do tempo
- Diagrama de Componentes: mostra a estrutura do sistema e suas partes
- Destaque a importância das condições de guarda para garantir funcionamento seguro.
- Apresente a atividade prática.

###### Preparações necessárias

- Preparar um cenário simples para modelagem
- Disponibilizar exemplos visuais
- Verificar acesso às ferramentas

###### Alertas e pontos de atenção

- Alunos podem confundir estados com ações
- Reforce que estado é uma condição do objeto
- Oriente sobre a lógica das transições
- Evite diagramas excessivamente complexos

###### Dinâmica sugerida

Situação-problema → explicação → prática guiada → discussão

###### Gerenciamento de tempo (50 minutos)

- Introdução e contextualização: 10 minutos
- Explicação dos diagramas: 10 minutos
- Execução da atividade: 20 minutos
- Apresentação e fechamento: 10 minutos

##### 5. Atividade Prática — Descrição Geral

O estudante deverá modelar um sistema simples utilizando dois tipos de diagramas UML:

- Diagrama de Máquina de Estado
- Diagrama de Componentes
Sugestão de cenário: sistema de controle de portão eletrônico ou sistema equivalente.

A atividade simula a fase de implantação e verificação do funcionamento de um sistema.

A habilidade desenvolvida será a capacidade de representar comportamento dinâmico e estrutura modular de software.

##### 6. Metodologia Ativa Utilizada

- Aprendizagem baseada em problemas (PBL)
- Experimentação prática
- Ensino por descoberta
Elementos de Lemov aplicados:

- Objetivo claro
- Produção visível
- Engajamento ativo
- Verificação de compreensão

##### 7. Passo a Passo da Atividade Prática (para os alunos)

- Leia o cenário apresentado pelo professor.
- Identifique os estados possíveis do objeto principal (ex.: portão).
- Desenhe um Diagrama de Máquina de Estado com:
- Estados principais
- Eventos de transição
- Condições de guarda (se necessário)
- Identifique os principais módulos ou partes do sistema.
- Desenhe um Diagrama de Componentes mostrando:
- Componentes de software
- Interfaces ou conexões
- Relações entre as partes
- Revise ambos os diagramas para garantir coerência.
- Prepare-se para apresentar sua solução.

##### 8. Exemplo ou Demonstração

Exemplo — Portão Eletrônico

Estados possíveis:

- Aberto
- Fechado
- Trancado
Transições:

- Comando de abrir
- Comando de fechar
- Comando de trancar
Componentes possíveis do sistema:

- Controle remoto
- Central eletrônica
- Motor do portão
- Sensores de segurança

##### 9. Resultado Esperado

O estudante deverá apresentar:

- Um Diagrama de Máquina de Estado completo
- Um Diagrama de Componentes correspondente
- Representação clara das transições e da estrutura do sistema
O professor poderá verificar o aprendizado observando:

- Uso correto dos conceitos da UML
- Coerência lógica do funcionamento do sistema
- Clareza visual dos diagramas

##### 10. Formato de Entrega da Atividade

- Formato: Desenho manual ou arquivo digital
- Nome do arquivo (se digital): UML_Implantacao_NomeAluno
- Local de entrega: Em sala ou envio digital, conforme orientação
- Prazo sugerido: Durante a aula

##### 11. Encerramento e Reflexão

Finalize a aula conduzindo uma reflexão orientada:

- Como os diagramas ajudam a prever o comportamento do sistema?
- Por que é importante modelar estados antes da implementação?
- Como a divisão em componentes facilita o desenvolvimento?
