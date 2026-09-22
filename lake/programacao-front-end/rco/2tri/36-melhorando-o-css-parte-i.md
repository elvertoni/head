---
titulo: "Melhorando o CSS Parte I"
tipo: rco-seed
disciplina: programacao-front-end
sigla_rco: PFE
trimestre: 2
ordem_rco: 36
serie: 2
aula_rco: "Aula 36"
slides: 21
tem_atividade: true
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PFE/2TRI/36-melhorando-o-css-parte-i/36-melhorando-o-css-parte-i.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/2TRI/36-melhorando-o-css-parte-i/AULA 36_ATIVIDADE_PROGRAMAÇÃO FRONT END.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Melhorando o CSS Parte I

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- Programação Front-End
- 2ª Série
- Melhorando o CSS Parte I
- Aula 36

_1 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- COMPETÊNCIA(S) A SER(EM) DESENVOLVIDA(S) NESTA AULA:
- De acordo com o Plano de Curso de Desenvolvimento de Sistemas:
- HABILIDADE(S) A SER(EM) DESENVOLVIDA(S) NESTA AULA:
- Desenvolver interfaces gráficas para aplicações computacionais.
- Prototipar interfaces e elementos visuais.

_1 imagem(ns) no slide._

### Slide 4

- Nesta aula vamos:
- Aprender a melhorar a utilização do CSS em páginas HTML Parte I.
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store

_4 imagem(ns) no slide._

### Slide 5 (oculto)

- Este material foi elaborado a partir da análise do plano de curso e reúne os conhecimentos essenciais para o Técnico em Desenvolvimento de Sistemas. As aulas foram organizadas com foco na clareza conceitual, na construção gradual dos conteúdos e na utilização de metodologias ativas que favorecem a compreensão, a participação e o desenvolvimento de habilidades e competências de forma significativa.
- De acordo com a matriz curricular do Curso Técnico em Desenvolvimento de Sistemas, que traz em sua essência componentes estruturados para a realização de aulas práticas, cada unidade curricular deve contemplar, além da abordagem teórica, uma proposta de atividade prática a ser desenvolvida pelo professor. Essa orientação assegura a coerência entre o planejamento didático e o que está estabelecido na matriz, promovendo experiências formativas alinhadas ao perfil profissional previsto.
- O professor tem total autonomia para adaptar o conteúdo conforme o contexto da turma, ajustando exemplos, aprofundamentos e estratégias didáticas para otimizar a aprendizagem e a conexão com a prática profissional.
- Se houver falta de conexão ou indisponibilidade de internet durante a aula, os materiais abaixo podem ser utilizados como apoio para elaborar recursos complementares, garantindo a continuidade da abordagem teórica prevista.
- ATENÇÃO PROFESSOR!
- Projeto aula anterior:
- https://caelum-online-public.s3.amazonaws.com/1310-html5-css3-parte4/02/html-parte-4-aula-2-completa.zip
- Complemento:
- https://cursos.alura.com.br/course/html5-css3-primeiros-passos/task/581966

_2 imagem(ns) no slide._

### Slide 6

- Aula anterior
- DESENVOLVIMENTO DE SISTEMAS
- Aprendemos a utilizar conteúdos externos em páginas HTML, como por exemplo, imagens, vídeos e fontes de texto.

_5 imagem(ns) no slide._

### Slide 7

- Para pensarmos juntos...
- Carla é uma desenvolvedora web trabalhando em um projeto de site para um cliente que deseja destacar os links do menu de navegação. O cliente quer que os links do menu mudem de cor quando o ponteiro do mouse passar sobre eles e que tenham um plano de fundo com gradiente linear.

_1 imagem(ns) no slide._

### Slide 8

- Para pensarmos juntos...
- Como Carla pode aplicar um gradiente linear no plano de fundo dos links do menu e fazer com que eles mudem de cor quando o ponteiro do mouse passar sobre eles, usando pseudo-classes em CSS?
- Conversem e apresentem suas visões

_2 imagem(ns) no slide._

### Slide 9

- Resposta
- Carla deve utilizar a pseudo-classe :hover, para aplicar estilos aos links do menu quando o ponteiro do mouse estiver sobre eles. Para aplicar o gradiente linear desejado como plano de fundo, ela deve usar a propriedade background-image com a função linear-gradient(). A combinação dessas duas técnicas ajudará Carla a criar o efeito visual desejado pelo cliente.

_1 imagem(ns) no slide._

### Slide 10

- Conceituando
- Gradientes em CSS:
- Gradientes são transições suaves entre duas ou mais cores, criando um efeito visual atraente e moderno. Em CSS, os gradientes podem ser aplicados como imagens de fundo usando a propriedade background-image. Existem dois tipos principais de gradientes: lineares e radiais. A função linear-gradient() cria um gradiente linear, enquanto a função radial-gradient() cria um gradiente radial. Ao utilizar essas funções, você pode especificar a direção, as cores e a progressão do gradiente.

_1 imagem(ns) no slide._

### Slide 11

- Conceituando
- Pseudo-classes em CSS:
- Pseudo-classes são usadas para aplicar estilos a elementos HTML com base em seu estado ou posição relativa na estrutura do documento. Elas são adicionadas às regras CSS como prefixos aos seletores de elementos, permitindo a seleção dinâmica de elementos sem a necessidade de adicionar classes ou IDs adicionais.
- https://slideplayer.com.br/slide/3284708/11/images/5/Exemplo+Form+GET+%3Chtml%3E.jpg

_1 imagem(ns) no slide._

### Slide 12

- Conceituando
- Algumas pseudo-classes comuns incluem :hover (aplica estilos quando o ponteiro do mouse está sobre um elemento), :active (aplica estilos a um elemento que está sendo ativado, como um botão sendo pressionado), :visited (aplica estilos a links já visitados) e :nth-child() (aplica estilos a elementos com base em sua posição numérica entre seus irmãos).

_1 imagem(ns) no slide._

### Slide 13

- Conceituando
- Pseudo-elementos em CSS:
- Pseudo-elementos são usados para selecionar e aplicar estilos a partes específicas de um elemento HTML, como a primeira letra ou a primeira linha de um parágrafo. Eles são adicionados às regras CSS como prefixos aos seletores de elementos, permitindo estilizar partes de um elemento sem a necessidade de adicionar elementos HTML adicionais.

_1 imagem(ns) no slide._

### Slide 14

- Conceituando
- Os pseudo-elementos usam uma sintaxe de dois-pontos (::) antes do nome, como ::before (insere conteúdo antes do elemento selecionado), ::after (insere conteúdo após o elemento selecionado), ::first-letter (aplica estilos à primeira letra de um elemento) e ::first-line (aplica estilos à primeira linha de um elemento).
- https://algol.dev/wp-content/uploads/2020/10/font_code-compressor.jpg

_1 imagem(ns) no slide._

### Slide 15

- Link para o curso: https://cursos.alura.com.br/course/html5-css3-avancando-css
- A recomendação é que você continue esse curso extraclasse, pois ele traz um conteúdo essencial para compreender sobre o referido tema.
- Atividade Prática na Plataforma Alura
- Na plataforma Alura vamos acessar o seguinte curso:

_3 imagem(ns) no slide._

### Slide 16

- Pseudo-classes
- 12 minutos
- No CSS temos algo chamado pseudo-elementos. Conhecemos alguns deles, como :hover, :active, :visited, :required.
- Link para tarefa: https://cursos.alura.com.br/course/html5-css3-avancando-css/task/63323
- Tais recursos são utilizados para marcar melhor nossos elementos e gerar um comportamento mais interessante em nosso site.
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 17

- Vamos praticar?
- Prepare-se, porque nessa atividade, você vai sair do modo aprender e entrar direto no modo praticar.
- A atividade prática vai colocar você diante de um desafio real, que faz relação com o conteúdo aprendido até aqui.

_1 imagem(ns) no slide._

### Slide 18

- O que vimos na aula de hoje:
- Aprendemos a melhorar mais ainda a semântica da página principal, com novas divisões, classes, entre outros.

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
- BEAULIEU, Alan. SQL: Guia Prático Para Manipulação de Dados. São Paulo: O'Reilly, 2008.
- CHACON, Scott; STRAUB, Ben. Pro Git. 2ª ed. Berkeley: Apress, 2014.
- DELISLE, Marc. MySQL: Guia do Programador. São Paulo: Novatec, 2010.
- FURGERI, Sérgio. SQL - Curso Prático. São Paulo: Novatec, 2018.
- LOELIGER, Jon; MCCULLOUGH, Matthew. Version Control with Git: Powerful Tools and Techniques for Collaborative Software Development. 2ª ed. Sebastopol: O'Reilly Media, 2012.
- SAMPAIO, Cleuton. Banco de Dados SQL: Aprenda a Construir um Banco de Dados do Zero. São Paulo: Novatec, 2018.
- SANTOS, Rafael. Administração de Banco de Dados: SQL Server 2017. São Paulo: Novatec, 2018.
- SILVERMAN, Richard E. Git Pocket Guide: A Working Introduction. Sebastopol: O'Reilly Media, 2013.
- STANEK, William. SQL Server 2019: Guia Completo do Administrador de Banco de Dados. São Paulo: Novatec, 2019.
- Figuras e Imagens:
- https://www.flaticon.com/br
- https://www.istockphoto.com/br
- https://raw.githubusercontent.com/zbtang/React-Native-ViewPager/HEAD/imgs/dotIndicator.gif
- https://storyset.com

### Slide 21

_(sem texto)_

## Atividade

_Fonte: AULA 36_ATIVIDADE_PROGRAMAÇÃO FRONT END.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação Front-End

2ª SÉRIE

ATIVIDADE AULA 36

Questão 1

Qual pseudoclasse CSS é usada para aplicar estilos a um elemento quando o ponteiro do mouse está sobre ele?

a) :hover

b) :active

c) :focus

d) :visited

Comentário: A resposta correta é a alternativa "a". A pseudoclasse :hover é usada para aplicar estilos a um elemento quando o ponteiro do mouse está sobre ele.

Questão 2

Qual pseudoclasse CSS é usada para aplicar estilos a um link que já foi visitado pelo usuário?

a) :hover

b) :active

c) :focus

d) :visited

Comentário: A resposta correta é a alternativa "d". A pseudoclasse :visited é usada para aplicar estilos a um link que já foi visitado pelo usuário.
