---
titulo: "Conceitos Fundamentais da UML"
tipo: rco-seed
disciplina: analise-e-metodos-para-sistemas
sigla_rco: AMS
trimestre: 1
ordem_rco: 16
serie: 1
aula_rco: "Aula 16"
slides: 30
tem_atividade: true
tem_pratica: true
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/AMS/1TRI/16-conceitos-fundamentais-da-uml/16-conceitos-fundamentais-da-uml.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/AMS/1TRI/16-conceitos-fundamentais-da-uml/AULA 16_ATIVIDADE_ANÁLISE E MÉTODO PARA SISTEMAS.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/AMS/1TRI/16-conceitos-fundamentais-da-uml/AULA 16_PRÁTICA_ANÁLISE E MÉTODO PARA SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Conceitos Fundamentais da UML

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- ANÁLISE E MÉTODO PARA SISTEMAS
- 1ª Série
- Conceitos Fundamentais da UML
- Aula 16

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

- Esta aula integra conhecimentos da Formação Geral
- Básica, articulando saberes da área de Linguagens e suas
- Tecnologias com a área técnica em Desenvolvimento de Sistemas.
- Nesta aula, os estudantes planejam e organizam as etapas do desenvolvimento de um sistema, utilizando tabelas e critérios de comparação (tempo, custo e qualidade) para analisar diferentes modelos de ciclo de vida do software e tomar decisões fundamentadas sobre o método mais adequado a um projeto.
- De acordo com o Currículo para o Ensino Médio do Paraná (Formação Geral Básica, 2022, temos:

| COMPETÊNCIA | HABILIDADES | OBJETIVOS DE APRENDIZAGEM | OBJETOS DO CONHECIMENTO | POSSIBILIDADES DE CONTEÚDOS |
| --- | --- | --- | --- | --- |
| Utilizar conceitos matemáticos e raciocínio lógico para investigar situações-problema, organizar procedimentos e comunicar soluções de forma estruturada, incluindo representações gráficas e simbólicas. | Investigar e registrar, por meio de um fluxograma, quando possível, um algoritmo que resolve um problema. | Compreender o conceito de algoritmo como sequência de passos para resolver um problema Identificar ações e decisões dentro de um processo Organizar procedimentos de forma lógica e ordenada Representar algoritmos por meio de fluxogramas Interpretar fluxogramas como modelos de solução Reconhecer a utilidade dessa representação em contextos tecnológicos | Algoritmos  Sequência lógica de ações  Tomada de decisão em processos  Representação gráfica de algoritmos  Fluxogramas e seus elementos  Modelagem de procedimentos | Raciocínio lógico  Estrutura sequencial  Estruturas condicionais (decisão)  Representação de processos  Algoritmos em linguagem natural  Interpretação de fluxogramas |

_1 imagem(ns) no slide._

### Slide 5

- COMPETÊNCIA(S) A SER(EM) DESENVOLVIDA(S) NESTA AULA:
- De acordo com o Plano de Curso de Desenvolvimento de Sistemas:
- HABILIDADE(S) A SER(EM) DESENVOLVIDA(S) NESTA AULA:
- Manter registros para análise e refinamento de resultados.
- MATEMÁTICA (FGB: EM13MAT315) Investigar e registrar, por meio de um fluxograma, quando possível, um algoritmo que resolve um problema.

_1 imagem(ns) no slide._

### Slide 6

- Nesta aula vamos:
- Aprender sobre os conceitos do
- Unified Modeling Language (UML).
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store
- https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR0AZ77SKhvtOzULHqJijV7ZJmcLuBoH_MKim-DXQQqHVOFI-R0Z5UuOTpg9SVEp58QPEw&usqp=CAU

_4 imagem(ns) no slide._

### Slide 7

- Este material foi elaborado a partir da análise do plano de curso e reúne os conhecimentos essenciais para o Técnico em Desenvolvimento de Sistemas. As aulas foram organizadas com foco na clareza conceitual, na construção gradual dos conteúdos e na utilização de metodologias ativas que favorecem a compreensão, a participação e o desenvolvimento de habilidades e competências de forma significativa.
- De acordo com a matriz curricular do Curso Técnico em Desenvolvimento de Sistemas, que traz em sua essência componentes estruturados para a realização de aulas práticas, cada unidade curricular deve contemplar, além da abordagem teórica, uma proposta de atividade prática a ser desenvolvida pelo professor. Essa orientação assegura a coerência entre o planejamento didático e o que está estabelecido na matriz, promovendo experiências formativas alinhadas ao perfil profissional previsto.
- O professor tem total autonomia para adaptar o conteúdo conforme o contexto da turma, ajustando exemplos, aprofundamentos e estratégias didáticas para otimizar a aprendizagem e a conexão com a prática profissional.
- Se houver falta de conexão ou indisponibilidade de internet durante a aula, os materiais abaixo podem ser utilizados como apoio para elaborar recursos complementares, garantindo a continuidade da abordagem teórica prevista.
- ATENÇÃO PROFESSOR!
- DOWNLOAD: Projeto do Curso:
- https://cursos.alura.com.br/course/uml-fundamentos-na-pratica/task/42926

_2 imagem(ns) no slide._

### Slide 8

- Aula anterior
- Iniciamos os estudos sobre UML
- abordando os conceitos iniciais da abordagem

_1 imagem(ns) no slide._

### Slide 9

- Para pensarmos juntos...
- João, recém-formado em sistemas de informação, foi contratado por uma startup para desenvolver uma plataforma de e-commerce.
- Ele queria utilizar a UML para representar uma funcionalidade onde os usuários poderiam tanto comprar como vender produtos, mas estava inseguro sobre a melhor forma de fazê-lo em um Diagrama de Caso de Uso.

_1 imagem(ns) no slide._

### Slide 10

- Para pensarmos juntos...
- Como João deveria representar em um Diagrama de Caso de Uso da UML a funcionalidade onde os usuários podem tanto comprar como vender produtos?
- 3 minutos
- Pesquise e escreva no caderno
- https://media.istockphoto.com/id/1272853458/vector/uml-unified-modeling-language-acronym-business-concept.jpg?s=170667a&w=0&k=20&c=wU9ztQp_3-seKQlVH_kDKE0Q41zubwUYl_7OWtUwyQo=

_3 imagem(ns) no slide._

### Slide 11

- Resposta
- João deve desenhar dois casos de uso distintos:
- "Comprar Produto" e "Vender Produto", conectando ambos ao ator "Usuário".
- Isso indica que um único tipo de usuário pode realizar ambas as ações na plataforma!

_1 imagem(ns) no slide._

### Slide 12

- Elementos UML: Uma Introdução
- A Linguagem de Modelagem Unificada, mais conhecida como UML (do inglês "Unified Modeling Language"), é uma linguagem padrão para especificar, visualizar, construir e documentar os artefatos de um sistema de software. Ela é amplamente utilizada por desenvolvedores e analistas de sistema para esboçar soluções antes de mergulhar na codificação.
- https://yuml.me/images/stick_graphic.png

_1 imagem(ns) no slide._

### Slide 13

- Classes e Objetos
- No núcleo da UML estão as classes, que representam tipos de objetos ou entidades, e os objetos, que são instâncias dessas classes.
- Uma classe é normalmente ilustrada como um retângulo com o nome da classe, enquanto os objetos podem ser representados por retângulos com nomes e estados.
- Fonte da imagem: https://images.ctfassets.net/w6r2i5d8q73s/5550PvEga3T2m2FxszitBb/d949e92ec6036b610501b87dc3101a36/M2_2_3_columns_template_picker_UML_diagram_001

_1 imagem(ns) no slide._

### Slide 14

- Relacionamentos
- A UML possui diversos tipos de relacionamentos, incluindo associação (ligação geral entre classes), agregação (relação "todo-parte") e herança (quando uma classe é derivada de outra).
- Fonte da imagem: https://i.stack.imgur.com/hb5y7.png

_1 imagem(ns) no slide._

### Slide 15

- Diagramas
- A UML é composta por vários tipos de diagramas, cada um focado em diferentes aspectos do sistema.
- Os mais populares incluem o Diagrama de Classes, Diagrama de Caso de Uso, Diagrama de Atividades e Diagrama de Sequência.
- Fonte da imagem: https://miro.medium.com/v2/resize:fit:529/1*HhEy_rUnWj2axLTTVQpy5w.png

_1 imagem(ns) no slide._

### Slide 16

- Atividades e Estados
- A UML permite representar o comportamento de um sistema através de Diagramas de Atividades (semelhante a um fluxograma) e Diagramas de Estados, que mostram as mudanças de estado de um objeto.
- Fonte da imagem: https://support.content.office.net/pt-br/media/3ac1da3e-ab76-41a8-85ba-5e48752138db.png

_1 imagem(ns) no slide._

### Slide 17

- Casos de Uso
- Em resumo, a UML oferece uma maneira estruturada de visualizar e entender sistemas complexos, tornando mais simples a comunicação entre as equipes e a transição da fase de design para a codificação.
- Estes representam funcionalidades específicas que um sistema pode realizar, geralmente do ponto de vista do usuário. Eles são essenciais para entender o que os stakeholders esperam do sistema.

_1 imagem(ns) no slide._

### Slide 18

- Vamos para mais um caso?
- Uma escola deseja informatizar o processo de empréstimo de livros da biblioteca.
- Sempre que um aluno solicita um livro, o sistema deve:
- Verificar se o livro está disponível
- Registrar o empréstimo
- Informar a data de devolução
- Caso o livro não esteja disponível, avisar ao aluno
- Ana, estudante de Desenvolvimento de Sistemas, foi encarregada de representar esse processo de forma clara para a equipe utilizando um fluxograma.
- 👉 Como Ana pode organizar esse processo em um algoritmo representado por fluxograma?
- Responda em seu caderno!

_2 imagem(ns) no slide._

### Slide 19

- Resposta:
- O fluxograma deve representar a sequência lógica do processo:
- Início
- Solicitar livro
- Verificar disponibilidade
- Decisão: livro disponível?
- Sim:
- Registrar empréstimo
- Informar data de devolução
- Não:
- Informar indisponibilidade
- Fim
- Esse algoritmo organiza o processo de forma clara, permitindo compreender as etapas e as decisões envolvidas.

_1 imagem(ns) no slide._

### Slide 20

- Para responder no seu caderno!
- Qual alternativa representa corretamente a função de um fluxograma na resolução de problemas?
- A) Mostrar apenas o resultado final de um processo.
- B) Representar visualmente a sequência de ações e decisões de um algoritmo.
- C) Substituir completamente a programação de um sistema.
- D) Registrar informações sem necessidade de ordem lógica.
- Responda em seu caderno!

_3 imagem(ns) no slide._

### Slide 21

- Veja se você acertou…
- Alternativa correta: B
- O fluxograma é uma representação visual que descreve passo a passo um algoritmo, incluindo ações e decisões necessárias para resolver um problema.
- Essa prática atende à habilidade EM13MAT315, pois envolve investigar, organizar e registrar um processo lógico por meio de representação gráfica.

_2 imagem(ns) no slide._

### Slide 22

- Ainda sobre UML, vamos conhecer praticando?
- Na plataforma Alura vamos acessar o seguinte curso:
- Os próximos itens serão para guiá-los nas principais atividades que serão necessárias para o entendimento da aula de hoje, embora existam mais atividades na plataforma Alura, em sala iremos desenvolver as essenciais.
- A recomendação é que você continue esse curso extraclasse, pois ele traz um conteúdo essencial para compreender sobre o referido tema.
- Link para o curso: https://cursos.alura.com.br/course/uml-fundamentos-na-pratica

_3 imagem(ns) no slide._

### Slide 23

- Introdução
- 8 minutos
- A UML (Unified Modeling Language) é uma linguagem padrão para modelar sistemas de software.
- Link para tarefa: https://cursos.alura.com.br/course/uml-fundamentos-na-pratica/task/42573
- Ela fornece uma série de diagramas para representar visualmente arquiteturas e processos. A UML ajuda desenvolvedores a comunicar ideias e projetar sistemas de maneira eficaz. É uma ferramenta essencial na engenharia de software moderna..
- Atividade no portal Alura

_6 imagem(ns) no slide._

### Slide 24

- Instalação da Ferramenta de Apoio
- 10 minutos
- A instalação de ferramentas UML facilita a modelagem de sistemas. Softwares como StarUML, Lucidchart e PlantUML são populares.
- Link para tarefa: https://cursos.alura.com.br/course/uml-fundamentos-na-pratica/task/42574
- Após o download, siga as instruções do assistente de instalação. Uma vez instalado, é possível começar a desenhar diagramas UML. Mantenha a ferramenta atualizada para funcionalidades otimizadas.
- Atividade no portal Alura

_6 imagem(ns) no slide._

### Slide 25

- Conceitos OO e UML
- 12 minutos
- A Orientação a Objetos (OO) é uma abordagem de programação baseada em "objetos", que combinam dados e funções.
- Link para tarefa: https://cursos.alura.com.br/course/uml-fundamentos-na-pratica/task/42575
- Conceitos chave incluem classe, herança e polimorfismo. A UML (Unified Modeling Language) é uma linguagem padrão para visualizar e documentar sistemas OO. Ela oferece diversos diagramas para representar diferentes aspectos de um sistema.
- Atividade no portal Alura

_6 imagem(ns) no slide._

### Slide 26

- Vamos praticar?
- Prepare-se, porque nessa atividade, você vai sair do modo aprender e entrar direto no modo praticar.
- A atividade prática vai colocar você diante de um desafio real: sensação de ver seu próprio código aparecer online! Acessível, documentado e pronto para o mundo!

_1 imagem(ns) no slide._

### Slide 27

- O que vimos na aula de hoje:
- Aprendemos de forma introdutória o que é a UML e para que ela serve.

_1 imagem(ns) no slide._

### Slide 28

- Pronto para desbloquear sua carreira de TI?
- Está perdido estudando mas não sabe por onde começar? Se a resposta é sim, você está no lugar certo! Descubra as estratégias e ferramentas essenciais para te ajudar a desbloquear seu potencial em TI e buscar sua primeira vaga de emprego no setor!
- Este e-book é um guia completo para quem busca começar pelos melhores caminhos para se tornar um excelente profissional de TI, ensinando a identificar perfis profissionais, aplicar técnicas de estudo eficazes, transformar teoria em prática, e aumentar a visibilidade de seu trabalho no mercado de trabalho. Ideal para novatos e profissionais em transição.
- E o melhor, ele pode ser seu, inteiramente grátis!
- Basta clicar AQUI e realizar o seu cadastro com o seu @escola!

_3 imagem(ns) no slide._

### Slide 29

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

### Slide 30

_(sem texto)_

## Atividade

_Fonte: AULA 16_ATIVIDADE_ANÁLISE E MÉTODO PARA SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

ANÁLISE E MÉTODO PARA SISTEMAS

1ª SÉRIE

ATIVIDADE AULA 16

Questão 1

Qual dos seguintes é um elemento fundamental da UML utilizado para representar a funcionalidade do sistema do ponto de vista do usuário?

a) Diagrama de Atividade

b) Diagrama de Caso de Uso

c) Diagrama de Sequência

d) Diagrama de Classe

Resposta: b) Diagrama de Caso de Uso.

Comentário: O Diagrama de Caso de Uso representa as ações que um sistema pode executar em resposta às solicitações de um ator externo.

Questão 2

Em UML, qual elemento é tipicamente utilizado para representar um objeto ou entidade, juntamente com seus atributos e operações?

a) Atores

b) Use Cases (Casos de Uso)

c) Classes

d) Atividades

Resposta: c) Classes

Comentário: As classes são a espinha dorsal da maioria dos sistemas orientados a objetos e são representadas em Diagramas de Classe, mostrando atributos, operações e as relações com outras classes.

## Prática

_Fonte: AULA 16_PRÁTICA_ANÁLISE E MÉTODO PARA SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

ANÁLISE E MÉTODO PARA SISTEMAS

1ª SÉRIE

ATIVIDADE PRÁTICA AULA 16

##### 1. Objetivo da Aula Prática

Ao final desta aula prática, o estudante deverá:

- Aprender os elementos fundamentais da UML e sua aplicação na modelagem de sistemas orientados a objetos.
- Desenvolver a habilidade prática de identificar classes, objetos, relacionamentos e casos de uso.
- Ser capaz de produzir representações simples utilizando conceitos básicos da UML, especialmente diagramas de caso de uso.

##### 2. Ferramentas Recomendadas

Caderno ou Folha A4

- Para que serve: Esboço manual de diagramas e registros conceituais.
- Por que é adequada ao tema: Permite experimentar a modelagem antes do uso de ferramentas digitais.
- Como facilita o aprendizado: Ajuda a compreender os símbolos e estruturas da UML.
draw.io / diagrams.net (https://app.diagrams.net)

- Para que serve: Criação digital de diagramas UML.
- Por que é adequada ao tema: Possui biblioteca de elementos UML prontos.
- Como facilita o aprendizado: Permite construir diagramas claros e organizados.
Lucidchart (plano gratuito)

- Para que serve: Modelagem visual colaborativa de diagramas.
- Por que é adequada ao tema: Amplamente utilizada na indústria.
- Como facilita o aprendizado: Aproxima o estudante do contexto profissional.
(Ferramentas gratuitas, online ou open source.)

##### 3. Checklist Inicial

Antes de iniciar a prática, o estudante deve ter:

- Caderno ou folhas para anotações
- Caneta ou lápis
- Computador ou notebook (opcional para versão digital)
- Conexão com a internet
- Acesso ao material da aula
- Ambiente: sala de aula ou laboratório

##### 4. Passo a Passo do Docente (Aula de até 50 minutos)

###### Como conduzir a aula

- Retome a aula anterior sobre introdução à UML.
- Apresente o problema proposto no material: modelar funcionalidades de compra e venda em uma plataforma de e-commerce.
- Explique os elementos fundamentais da UML apresentados na aula:
- Classes e objetos
- Relacionamentos (associação, agregação, herança)
- Tipos de diagramas
- Casos de uso
- Atividades e estados
- Destaque a solução proposta no material: representar “Comprar Produto” e “Vender Produto” como casos de uso distintos conectados ao ator “Usuário”.
- Apresente a atividade prática.

###### Preparações necessárias

- Preparar um cenário simples de sistema (ex.: plataforma de vendas, biblioteca, aplicativo escolar)
- Disponibilizar exemplos visuais de diagramas
- Garantir acesso às ferramentas, se necessário

###### Alertas e pontos de atenção

- Alunos podem confundir classes com objetos
- Reforce que caso de uso representa funcionalidades do sistema
- Oriente para não detalhar excessivamente

###### Dinâmica sugerida

Problema inicial → explicação conceitual → prática guiada → validação coletiva

###### Gerenciamento de tempo (50 minutos)

- Revisão e explicação: 15 minutos
- Demonstração: 10 minutos
- Execução da prática: 15 minutos
- Socialização e fechamento: 10 minutos

##### 5. Atividade Prática — Descrição Geral

O estudante deverá modelar funcionalidades básicas de um sistema utilizando conceitos fundamentais da UML.

Sugestão de cenário: sistema de e-commerce onde um usuário pode comprar e vender produtos.

A atividade simula a fase inicial de análise e modelagem de requisitos de um software.

A habilidade desenvolvida será a capacidade de representar funcionalidades do sistema do ponto de vista do usuário.

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

- Leia o cenário apresentado pelo professor.
- Identifique quem é o ator principal do sistema.
- Liste as funcionalidades que o sistema deve oferecer ao usuário.
- Separe essas funcionalidades em casos de uso distintos.
- Desenhe um Diagrama de Caso de Uso simples.
- Revise se as conexões entre ator e funcionalidades estão corretas.
- Prepare-se para apresentar o diagrama.

##### 8. Exemplo ou Demonstração

Exemplo — Plataforma de e-commerce

Ator: Usuário

Casos de uso:

- Comprar Produto
- Vender Produto
Ambos conectados ao mesmo ator, indicando que o usuário pode realizar as duas ações.

Esse exemplo corresponde ao problema apresentado no material da aula.

##### 9. Resultado Esperado

O estudante deverá apresentar:

- Um diagrama de caso de uso simples e coerente
- Identificação correta do ator e das funcionalidades
- Organização clara dos elementos UML
O professor poderá verificar o aprendizado observando:

- Uso correto do conceito de caso de uso
- Clareza visual do diagrama
- Coerência com o cenário

##### 10. Formato de Entrega da Atividade

- Formato: Desenho no caderno, folha ou arquivo digital
- Nome do arquivo (se digital): CasoDeUso_UML_NomeAluno
- Local de entrega: Avaliação em sala ou envio digital, conforme orientação
- Prazo sugerido: Durante a aula

##### 11. Encerramento e Reflexão

Finalize a aula conduzindo uma reflexão orientada:

- Por que representar funcionalidades do ponto de vista do usuário é importante?
- Como a UML facilita a comunicação entre desenvolvedores e clientes?
- Qual a utilidade dos diagramas antes da implementação do sistema?
