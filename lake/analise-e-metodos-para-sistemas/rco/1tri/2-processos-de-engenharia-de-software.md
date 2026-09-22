---
titulo: "Processos de Engenharia de Software"
tipo: rco-seed
disciplina: analise-e-metodos-para-sistemas
sigla_rco: AMS
trimestre: 1
ordem_rco: 2
serie: 1
aula_rco: "Aula 02"
slides: 27
tem_atividade: true
tem_pratica: true
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/AMS/1TRI/2-processos-de-engenharia-de-software/2-processos-de-engenharia-de-software.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/AMS/1TRI/2-processos-de-engenharia-de-software/AULA 02_ATIVIDADE_ANÁLISE E MÉTODO PARA SISTEMAS.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/AMS/1TRI/2-processos-de-engenharia-de-software/AULA 02_PRÁTICA_ANÁLISE E MÉTODO PARA SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Processos de Engenharia de Software

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- ANÁLISE E MÉTODO PARA SISTEMAS
- 1ª Série
- Processos de Engenharia de Software
- Aula 02

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
- Dimensionar requisitos e funcionalidades do sistema
- Documentar Sistemas de Informação

_1 imagem(ns) no slide._

### Slide 5

- Nesta aula, vamos:
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store
- Entender os processos de Engenharia de Software

_5 imagem(ns) no slide._

### Slide 6

- Este material foi elaborado a partir da análise do plano de curso e reúne os conhecimentos essenciais para o Técnico em Desenvolvimento de Sistemas. As aulas foram organizadas com foco na clareza conceitual, na construção gradual dos conteúdos e na utilização de metodologias ativas que favorecem a compreensão, a participação e o desenvolvimento de habilidades e competências de forma significativa.
- De acordo com a matriz curricular do Curso Técnico em Desenvolvimento de Sistemas, que traz em sua essência componentes estruturados para a realização de aulas práticas, cada unidade curricular deve contemplar, além da abordagem teórica, uma proposta de atividade prática a ser desenvolvida pelo professor. Essa orientação assegura a coerência entre o planejamento didático e o que está estabelecido na matriz, promovendo experiências formativas alinhadas ao perfil profissional previsto.
- O professor tem total autonomia para adaptar o conteúdo conforme o contexto da turma, ajustando exemplos, aprofundamentos e estratégias didáticas para otimizar a aprendizagem e a conexão com a prática profissional.
- Se houver falta de conexão ou indisponibilidade de internet durante a aula, os materiais abaixo podem ser utilizados como apoio para elaborar recursos complementares, garantindo a continuidade da abordagem teórica prevista.
- ATENÇÃO PROFESSOR!

_2 imagem(ns) no slide._

### Slide 7

- Na aula anterior…
- Vimos o que é engenharia de software

_2 imagem(ns) no slide._

### Slide 8

- Retomando…
- Se a Engenharia de Software trata da aplicação de abordagens sistemáticas, disciplinadas e quantificáveis para desenvolver, operar, manter e evoluir software, como é trabalhado suas etapas?
- Realizem a atividade em duplas e socializem no final!
- Quais são os processos desempenhados na engenharia de software?
- Se realizarmos uma analogia com a construção de uma casa, quais são os processos utilizados para cada etapa?
- Exemplo: como é construído uma parede do início ao fim, reflita e pesquisem para identificar quais são os processos envolvidos na construção da uma parede de alvenaria por exemplo.

_2 imagem(ns) no slide._

### Slide 9

- Para pensarmos juntos...
- Essa analogia (comparação) da construção da casas serve para apresentar que mesmo um produto sendo abstrato, ou seja, ela foi projetada por meio de um a planta antes de ser construída, também deve existir um modelo de processo definido para a construção de um software.

_2 imagem(ns) no slide._

### Slide 10

- Conceitos sobre processos de engenharia de software
- Ian Sommerville:
- Um processo de software é um conjunto de atividades relacionadas que levam à produção de um produto de software.
- Roger Pressman:
- Processo de software é definido como uma metodologia para as atividades, ações e tarefas necessárias para desenvolver um software de alta qualidade.

_3 imagem(ns) no slide._

### Slide 11

- Conceitos sobre processos de engenharia de software
- Existem diferentes maneiras de organizarmos as atividades que juntas levam a construção de software.
- Sommerville aponta que qualquer que seja esse processo, ele deve incluir quatro atividades fundamentais.

_3 imagem(ns) no slide._

### Slide 12

- Conceitos sobre processos de engenharia de software
- Especificação do software: A funcionalidade do software e as restrições a seu funcionamento devem ser definidas.
- Projeto e implementação de software: O software deve ser produzido para atender às especificações
- Validação de software: O software deve ser validado para garantir que atenda às demandas do cliente
- Evolução de software: O software deve evoluir para atender às necessidades de mudança dos clientes.

_2 imagem(ns) no slide._

### Slide 13

- Startups e planos de negócio
- Link:https://drive.google.com/file/d/13wOMPC0ayHVGUjKhG8nVoL1Evb9S54yy/view?usp=share_link
- OBS: link do vídeo deve ser atualizado caso a apresentação mude de pasta junto com os vídeos

_4 imagem(ns) no slide._

> **Notas do apresentador:** Link do vídeo:https://drive.google.com/file/d/13wOMPC0ayHVGUjKhG8nVoL1Evb9S54yy/view?usp=share_link

### Slide 14

- Para responder:
- Quando se trata de escolher um processo de desenvolvimento de software, você tem algumas boas opções, incluindo o modelo em cascata, a metodologia ágil e a metodologia de espiral interativa. Escolher a melhor metodologia para o seu projeto e segui-la estritamente levará a um maior sucesso. Quais são as etapas do processo básico de desenvolvimento de software?
- a) Falta de pesquisa, requisitos pouco claros, não está na moda e falta de gerente com experiência em tecnologia.
- b) Documentação, código, implementação, testes e iteração.
- c) Pesquisa, ideação, design, desenvolvimento e iteração.
- d) Testes, consistência e revisão de código.
- Responda em seu caderno!

_2 imagem(ns) no slide._

### Slide 15

- Resposta
- DESENVOLVIMENTO DE SISTEMAS
- a) Falta de pesquisa, requisitos pouco claros, não está na moda e falta de gerente com experiência em tecnologia.
- b) Documentação, código, implementação, testes e iteração.
- c) Pesquisa, ideação, design, desenvolvimento e iteração.
- d) Testes, consistência e revisão de código.

_1 imagem(ns) no slide._

### Slide 16

- Resposta comentada: No nível mais básico, empregamos cinco estágios durante o processo de design de software: pesquisa, ideação, design, desenvolvimento e iteração. A alternativa A está errada, porque fazer pesquisa são etapas do processo de desenvolvimento de software. A alternativa B está errada, porque a documentação não é uma das etapas do processo de desenvolvimento de software. A alternativa D está errada, porque consistência e revisão de código não é uma das etapas do processo de desenvolvimento de software.

_2 imagem(ns) no slide._

### Slide 17

- Uso de boas práticas no desenvolvimento
- Link: https://drive.google.com/file/d/1bPDIuNh06FDQU2EHBKAeacxPVeJ6aOna/view?usp=share_link
- OBS: link do vídeo deve ser atualizado caso a apresentação mude de pasta junto com os vídeos

_3 imagem(ns) no slide._

### Slide 18

- Atividade em sala!
- Ao longo das aulas, aprendemos sobre os conceitos de Engenharia de Software e como aplicar os conhecimentos na criação de estruturas, dispositivos e processos de sistemas.
- Os processos de sistemas são compostos por desenvolvimento, operação e manutenção de software que envolve o planejamento e a execução de atividades, como operar aplicativos de software de produção, monitorar o desempenho do sistema, fazer reparos de defeitos, testar o aplicativo depois que quaisquer alterações forem feitas e ajustar um sistema de lançamento de software.

_1 imagem(ns) no slide._

### Slide 19

- Atividade em sala!
- Atividade:
- Considerando essas informações e os conteúdos estudados, construa uma história em quadrinhos em que existam personagens como cliente, desenvolvedor, um produto e o uso de processo de resolução de problemas em Engenharia de Software.
- Orientações:
- Usando umas das ferramentas gratuitas abaixo, você deve construir sua história em quadrinhos, que deve possuir personagens, como, cliente, desenvolvedor, um produto de software e o uso de processo de resolução de problemas em Engenharia de Software.
- Registre a sua resposta e compartilhe!

_4 imagem(ns) no slide._

### Slide 20

- Atividade em sala!
- Ferramentas:
- Pixton - https://www.pixton.com/
- StoryboardThat - https://www.storyboardthat.com/
- GoAnimate - https://www.vyond.com/
- Stripcreator - http://www.stripcreator.com/make.php
- 5. Pencil -https://pencil.evolus.vn/Downloads.html

_2 imagem(ns) no slide._

> **Notas do apresentador:** Parâmetros avaliativos Para a atividade ser considerada ótima, a história deve apresentar uma aplicação correta dos conceitos teóricos apresentados em aula. Além disso, a atividade deve demonstrar corretamente o processo de resolução de problemas em Engenharia de software.

### Slide 21

- Quem quer compartilhar?
- LEIA O RESTANTE DA HISTÓRIA EM: https://inspiradanacomputacao.wordpress.com/2014/05/16/fundamentos-do-software-livre-em-quadrinhos-como-voce-nunca-viu/

_4 imagem(ns) no slide._

> **Notas do apresentador:** Parâmetros avaliativos Para a atividade ser considerada ótima, a história deve apresentar uma aplicação correta dos conceitos teóricos apresentados em aula. Além disso, a atividade deve demonstrar corretamente o processo de resolução de problemas em Engenharia de software.

### Slide 22

- TAREFA PARA CASA!
- Das atividades que você desenvolve no ambiente escolar, qual delas você considera a mais importante?
- Responda em seu caderno!

_2 imagem(ns) no slide._

### Slide 23

- Vamos praticar?
- Usando ferramentas simples como Pixton, StoryboardThat ou Stripcreator, você vai representar, passo a passo, as etapas fundamentais da Engenharia de Software: entender o problema, planejar, desenvolver, testar e evoluir a solução.
- O desafio não é desenhar bonito! É pensar com lógica, organizar processos e contar uma história que faça sentido, exatamente como acontece no mundo profissional da tecnologia.

_2 imagem(ns) no slide._

### Slide 24

- O que vimos na aula de hoje
- Que os processos da engenharia de software podem ser considerados como conjunto de etapas da construção do produto e que elas podem incluir algumas atividades que podem ser consideradas fundamentais

_2 imagem(ns) no slide._

### Slide 25

- Pronto para desbloquear sua carreira de TI?
- Está perdido estudando mas não sabe por onde começar? Se a resposta é sim, você está no lugar certo! Descubra as estratégias e ferramentas essenciais para te ajudar a desbloquear seu potencial em TI e buscar sua primeira vaga de emprego no setor!
- Este e-book é um guia completo para quem busca começar pelos melhores caminhos para se tornar um excelente profissional de TI, ensinando a identificar perfis profissionais, aplicar técnicas de estudo eficazes, transformar teoria em prática, e aumentar a visibilidade de seu trabalho no mercado de trabalho. Ideal para novatos e profissionais em transição.
- E o melhor, ele pode ser seu, inteiramente grátis!
- Basta clicar AQUI e realizar o seu cadastro com o seu @escola!

_4 imagem(ns) no slide._

### Slide 26

- Referências
- AFFONSO DE OLIVEIRA, Maurício. Análise e Projeto de Sistemas de Informação Orientados para a Internet. São Paulo: Érica, 2007.
- BEZERRA, Eduardo. Engenharia de Requisitos: Software Orientado ao Negócio. São Paulo: Novatec, 2010.
- BOOCH, Grady; RUMBAUGH, James; JACOBSON, Ivar. UML - Guia do Usuário. 2ª ed. Rio de Janeiro: Campus, 2005.
- GANE, Chris; SARSON, Trish. Análise Estruturada de Sistemas. Rio de Janeiro: LTC, 1995.
- MAGNO DA SILVA NOVAES, Carlos; SAMPAIO DO PRADO LEITE, Júlio César. Análise e Projeto de Sistemas de Informação com UML e Unified Process. São Paulo: Elsevier, 2003.
- PRESSMAN, Roger S.; MAXIM, Bruce R. Engenharia de Software: Uma Abordagem Profissional. 7ª ed. Porto Alegre: AMGH, 2016.
- PRESSMAN, Roger S. Engenharia de Software: Conceitos e Práticas. São Paulo: McGraw-Hill, 2011.
- REZENDE, Denis Alcides. Engenharia de software e sistemas de informação. Brasport, 2006.
- RITTER, Tiago. Gerenciamento de Projetos: Como definir e controlar o escopo do projeto. São Paulo: Casa do Código, 2017.
- SOARES, Raphael. Metodologia de Desenvolvimento de Software: Um Guia Prático para Iniciantes. São Paulo: Novatec, 2014.
- SOUSA, André S. C.; GUISSI, Viviane Cristina. Modelagem de Processos de Negócio. São Paulo: Érica, 2012.
- Figuras e Imagens:
- https://www.flaticon.com/br
- https://www.istockphoto.com/br
- https://raw.githubusercontent.com/zbtang/React-Native-ViewPager/HEAD/imgs/dotIndicator.gif
- https://storyset.com

### Slide 27

_(sem texto)_

## Atividade

_Fonte: AULA 02_ATIVIDADE_ANÁLISE E MÉTODO PARA SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

ANÁLISE E MÉTODO PARA SISTEMAS

1ª SÉRIE

ATIVIDADE AULA 02

Questão 1

Existem diretrizes rígidas e diferentes metodologias de práticas recomendadas de desenvolvimento de software, como scrum ou programação extrema. Existe um "projeto de desenvolvimento de software ideal" e, em caso afirmativo, quais são as etapas que você deve seguir para atingir esse estado ideal?

a) Etapa de aquisição ou atualização do código e etapa de codificação.

b) Etapa de aquisição ou atualização do código, etapa de codificação, etapa de validação do código desenvolvido, etapa de integração do novo código e fase de testes.

c) Fase de integração do novo código, que é um processo de desenvolvimento de software inicialmente e, em seguida, atualizá-lo em tempo hábil por vários motivos.

d) Fase de testes, em que os engenheiros de teste verificam se o software atende às especificações exigidas.

Resposta comentada: A Engenharia de Software, especificamente, usa uma abordagem organizada e regulamentada para o design, o desenvolvimento, o teste, a documentação e a manutenção de software, aplicando princípios e boas práticas. A alternativa A está errada, porque temos apenas duas práticas recomendadas de desenvolvimento de software não enriquecendo a resposta. A alternativa C está errada, porque temos apenas uma das etapas. A alternativa D está errada, porque temos apenas a etapa de testes.

Questão 2

Nessa etapa, identifica-se os stakeholders e seus diferentes pontos de vista sobre o problema e as influências. Qual é a definição da etapa Processo Definido em Engenharia de Software?

a) Estabelecer o “Produto Mínimo Viável” que os projetos de software precisam alcançar.

b) O código simples, às vezes chamado código limpo, é mais fácil de ler e gerenciar.

c) Os testes de ponta a ponta contínuos darão mais confiança na qualidade do código.

d) Prazos curtos e orçamentos apertados criam estresse.

Resposta comentada: Fase de aquisição ou atualização do código. Esta etapa também é conhecida como etapa de ''coleta de requisitos''. É tudo uma questão de se comunicar com o cliente antes de construir um Software, para se conhecer os requisitos por completo. A alternativa B está errada, porque o código não é uma etapa Processo Definido. A alternativa C está errada, porque testes não é uma etapa Processo Definido. A alternativa D está errada, porque prazos não é uma etapa Processo Definido.

## Prática

_Fonte: AULA 02_PRÁTICA_ANÁLISE E MÉTODO PARA SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

ANÁLISE E MÉTODO PARA SISTEMAS

1ª SÉRIE

ATIVIDADE PRÁTICA AULA 02

##### 1. Objetivo da Aula Prática

Ao final desta aula prática, o estudante deverá:

- Aprender como funcionam os processos da Engenharia de Software e suas etapas fundamentais.
- Desenvolver a habilidade prática de compreender e representar visualmente o processo de resolução de problemas em Engenharia de Software.
- Ser capaz de produzir uma história em quadrinhos que represente a interação entre cliente, desenvolvedor, produto de software e o uso de processos de Engenharia de Software.

##### 2. Ferramentas Recomendadas

Pixton (https://www.pixton.com/)

- Para que serve: Criação de histórias em quadrinhos digitais.
- Por que é adequada ao tema: Permite representar situações reais de desenvolvimento de software com personagens e diálogos.
- Como facilita o aprendizado: Ajuda o aluno a transformar conceitos abstratos em narrativas visuais.
StoryboardThat (https://www.storyboardthat.com/)

- Para que serve: Criação de storyboards e HQs educativas.
- Por que é adequada ao tema: Facilita a organização das etapas do processo de software em sequência lógica.
- Como facilita o aprendizado: Estimula o raciocínio sequencial e a compreensão de processos.
Stripcreator (http://www.stripcreator.com/make.php)

- Para que serve: Criação simples de tirinhas em quadrinhos.
- Por que é adequada ao tema: Interface simples, ideal para alunos iniciantes.
- Como facilita o aprendizado: Reduz a complexidade técnica, focando no conteúdo.
(Todas as ferramentas são gratuitas, online ou open source, conforme o material da aula.)

##### 3. Checklist Inicial

Antes de iniciar a prática, o estudante deve ter:

- Computador, notebook ou tablet
- Conexão com a internet
- Navegador atualizado
- Acesso a pelo menos uma das ferramentas indicadas
- Ambiente: laboratório de informática ou sala com internet
- Material da aula (slides ou PDF disponibilizados pelo professor)

##### 4. Passo a Passo do Docente (Aula de até 50 minutos)

###### Como conduzir a aula

- Retome rapidamente o conceito de Engenharia de Software visto na aula anterior.
- Apresente a analogia da construção de uma casa para explicar processos (conforme slides da aula).
- Explique o conceito de processo de software segundo Sommerville e Pressman.
- Destaque as quatro atividades fundamentais:
- Especificação
- Projeto e implementação
- Validação
- Evolução
- Apresente a atividade prática e mostre um exemplo simples de HQ.

###### Preparações necessárias

- Testar previamente as ferramentas de criação de HQ
- Ter um exemplo de história em quadrinhos pronto
- Garantir acesso à internet ou plano alternativo em caso de falha

###### Alertas e pontos de atenção

- Alguns alunos podem focar apenas no visual e esquecer o processo
- Reforce que a história deve mostrar etapas do processo de software
- Oriente para diálogos simples e objetivos

###### Dinâmica sugerida

- Explanação curta → demonstração → prática orientada → compartilhamento

###### Gerenciamento de tempo (50 minutos)

- Retomada e contextualização: 10 minutos
- Explicação do processo e da atividade: 10 minutos
- Produção da HQ: 20 minutos
- Compartilhamento e fechamento: 10 minutos

##### 5. Atividade Prática — Descrição Geral

O estudante deverá construir uma história em quadrinhos que represente:

- Um cliente com um problema
- Um desenvolvedor
- Um produto de software
- O uso de processos de Engenharia de Software para resolver o problema
A atividade simula uma situação real do mercado, onde problemas precisam ser compreendidos, planejados, desenvolvidos, testados e evoluídos.

A habilidade desenvolvida será a compreensão prática dos processos da Engenharia de Software.

##### 6. Metodologia Ativa Utilizada

- Aprendizagem baseada em projetos (PBL)
- Ensino por descoberta
- Experimentação prática
- Colaboração (quando realizada em dupla ou grupo)
Elementos de Lemov aplicados:

- Objetivo claro
- Produção visível
- Pensamento estruturado
- Responsabilização pelo resultado

##### 7. Passo a Passo da Atividade Prática (para os alunos)

- Acesse uma das ferramentas indicadas pelo professor.
- Escolha um modelo de história em quadrinhos.
- Crie personagens representando:
- Cliente
- Desenvolvedor
- Produto de software
- Construa a narrativa mostrando:
- O problema apresentado pelo cliente
- A análise do desenvolvedor
- O uso do processo de software
- A solução entregue
- Utilize diálogos curtos e claros.
- Revise a história verificando se o processo está bem representado.
- Salve ou exporte o trabalho conforme orientação do professor.

##### 8. Exemplo ou Demonstração

Estrutura sugerida da HQ:

- Quadro 1: Cliente apresenta um problema
- Quadro 2: Desenvolvedor analisa e levanta requisitos
- Quadro 3: Planejamento e desenvolvimento do software
- Quadro 4: Testes e validação
- Quadro 5: Entrega e evolução do sistema

##### 9. Resultado Esperado

O estudante deverá entregar:

- Uma história em quadrinhos completa
- Com personagens definidos
- Representando corretamente os processos da Engenharia de Software
O professor poderá verificar o aprendizado observando:

- Sequência lógica da história
- Clareza na representação do processo
- Conexão com os conceitos apresentados na aula

##### 10. Formato de Entrega da Atividade

- Formato: Link da ferramenta utilizada ou arquivo em PDF/imagem
- Nome do arquivo (se aplicável): HQ_Processos_ES_NomeAluno
- Local de entrega: Google Classroom, Drive ou plataforma institucional
- Prazo sugerido: Ao final da aula ou como tarefa complementar

##### 11. Encerramento e Reflexão

Encerrar a aula com uma reflexão orientada pelo professor:

- Qual etapa do processo de Engenharia de Software você considera mais importante?
- O que acontece quando um processo não é seguido corretamente?
- Como essa aula se conecta com conteúdos futuros sobre requisitos, modelagem e desenvolvimento?
