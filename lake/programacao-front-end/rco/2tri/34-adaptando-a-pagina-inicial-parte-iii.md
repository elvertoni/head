---
titulo: "Adaptando a página inicial Parte III"
tipo: rco-seed
disciplina: programacao-front-end
sigla_rco: PFE
trimestre: 2
ordem_rco: 34
serie: 2
aula_rco: "Aula 34"
slides: 22
tem_atividade: true
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PFE/2TRI/34-adaptando-a-pagina-inicial-parte-iii/34-adaptando-a-pagina-inicial-parte-iii.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/2TRI/34-adaptando-a-pagina-inicial-parte-iii/AULA 34_ATIVIDADE_PROGRAMAÇÃO FRONT END.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Adaptando a página inicial Parte III

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- Programação Front-End
- 2ª Série
- Adaptando a página inicial Parte III
- Aula 34

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
- Aprender a incluir novos elementos em páginas HTML Parte III.
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
- Projeto inicial:
- https://caelum-online-public.s3.amazonaws.com/1310-html5-css3-parte4/01/html-parte-4-projeto-inicial.zip
- Complemento:
- https://cursos.alura.com.br/course/html5-css3-primeiros-passos/task/581966

_2 imagem(ns) no slide._

### Slide 6

- Aula anterior
- Iniciamos os estudos para uma nova inclusão de elementos e melhorias em páginas HTML que daremos continuidade nessa aula.

_1 imagem(ns) no slide._

### Slide 7

- Para pensarmos juntos...
- Júlia é uma desenvolvedora web iniciante e está trabalhando na modificação de uma página HTML para um projeto pessoal. Ela quer personalizar o estilo da página, incluindo a cor do plano de fundo e a fonte do texto. Entretanto, Júlia está enfrentando dificuldades para encontrar a maneira correta de fazer isso.

_1 imagem(ns) no slide._

### Slide 8

- Para pensarmos juntos...
- Qual elemento HTML e qual arquivo Júlia deve criar para personalizar a cor do plano de fundo e a fonte do texto em sua página?
- Conversem e apresentem suas visões

_2 imagem(ns) no slide._

### Slide 9

- Para pensarmos juntos...
- a) Criar um arquivo .css e utilizar a tag <css> no HTML
- b) Criar um arquivo .css e utilizar a tag <style> no HTML
- c) Criar um arquivo .html e utilizar a tag <style> no HTML
- d) Criar um arquivo .js e utilizar a tag <script> no HTML
- Conversem e apresentem suas visões

_2 imagem(ns) no slide._

### Slide 10

- Resposta
- A resposta correta é a alternativa "b". Para personalizar o estilo da página, Júlia deve criar um arquivo .css (Cascading Style Sheets) separado, que será usado para definir a cor do plano de fundo, a fonte do texto e outros estilos. Para vincular esse arquivo .

_1 imagem(ns) no slide._

### Slide 11

- Resposta
- css à sua página HTML, ela deve usar a tag <link> (não <style>, como mencionado na opção) com o atributo "rel" definido como "stylesheet" e o atributo "href" apontando para o caminho do arquivo .css. A tag <link> deve ser colocada dentro da tag <head> do documento HTML. As outras alternativas não são apropriadas para essa finalidade.

_1 imagem(ns) no slide._

### Slide 12

- Conceituando
- As alterações iniciais em páginas HTML são etapas fundamentais no processo de desenvolvimento web e envolvem a personalização e aprimoramento de páginas recém-criadas. Essas modificações podem incluir a adição de elementos como texto, imagens, links, listas e tabelas, bem como a formatação desses elementos usando estilos e a organização da estrutura geral do documento. O objetivo dessas alterações iniciais é criar uma base sólida para a funcionalidade e o design da página, facilitando futuras atualizações e expansões.

_1 imagem(ns) no slide._

### Slide 13

- Conceituando
- Uma das primeiras alterações a serem realizadas em uma página HTML é a adição de conteúdo e a estruturação da informação. Isso pode incluir a criação de cabeçalhos, parágrafos, listas, tabelas e outros elementos HTML para organizar e apresentar o conteúdo de maneira eficaz.

_1 imagem(ns) no slide._

### Slide 14

- Conceituando
- Adicionalmente, é importante garantir que a estrutura do documento seja semântica e acessível, utilizando as tags adequadas, como <header>, <nav>, <main>, <article>, <section>, <aside> e <footer>, para descrever o propósito de cada seção.

_1 imagem(ns) no slide._

### Slide 15

- Link para o curso: https://cursos.alura.com.br/course/html5-css3-avancando-css
- A recomendação é que você continue esse curso extraclasse, pois ele traz um conteúdo essencial para compreender sobre o referido tema.
- Atividade Prática na Plataforma Alura
- Na plataforma Alura vamos acessar o seguinte curso:

_3 imagem(ns) no slide._

### Slide 16

- Adaptando o CSS
- 11 minutos
- Temos o HTML, mas resta criarmos o CSS de cada um dos elementos. Em nossa página inicial temos o banner que criamos o id para ele.
- Link para tarefa: https://cursos.alura.com.br/course/html5-css3-avancando-css/task/63318
- No universo HTML e CSS, ao falarmos de estilo, usamos uma classe, quando falamos de comportamento, usamos o identificador.
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 17

- Usando o float
- 11 minutos
- Esse recurso é utilizado caso a imagem não seja carregada ou para pessoas que utilizam leitores de tela.
- Link para tarefa: https://cursos.alura.com.br/course/html5-css3-avancando-css/task/63319
- Ao carregarmos o navegador, a imagem já estará disponível no site, mas ainda precisamos regular seu tamanho em style.css: O próximo passo é fazer com que o texto englobe essa imagem.
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 18

- Vamos praticar?
- Prepare-se, porque nessa atividade, você vai sair do modo aprender e entrar direto no modo praticar.
- A atividade prática vai colocar você diante de um desafio real, que faz relação com o conteúdo aprendido até aqui.

_1 imagem(ns) no slide._

### Slide 19

- O que vimos na aula de hoje:
- Aprendemos como adaptar elementos básicos de páginas HTML.

_1 imagem(ns) no slide._

### Slide 20

- Pronto para desbloquear sua carreira de TI?
- Está perdido estudando mas não sabe por onde começar? Se a resposta é sim, você está no lugar certo! Descubra as estratégias e ferramentas essenciais para te ajudar a desbloquear seu potencial em TI e buscar sua primeira vaga de emprego no setor!
- Este e-book é um guia completo para quem busca começar pelos melhores caminhos para se tornar um excelente profissional de TI, ensinando a identificar perfis profissionais, aplicar técnicas de estudo eficazes, transformar teoria em prática, e aumentar a visibilidade de seu trabalho no mercado de trabalho. Ideal para novatos e profissionais em transição.
- E o melhor, ele pode ser seu, inteiramente grátis!
- Basta clicar AQUI e realizar o seu cadastro com o seu @escola!

_3 imagem(ns) no slide._

### Slide 21

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

### Slide 22

_(sem texto)_

## Atividade

_Fonte: AULA 34_ATIVIDADE_PROGRAMAÇÃO FRONT END.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação Front-End

2ª SÉRIE

ATIVIDADE AULA 34

Questão 1

Qual é a estrutura básica de um documento HTML?

a) <!DOCTYPE html><html><body></body></html>

b) <!DOCTYPE html><html><header></header><body></body></html>

c) <!DOCTYPE html><head><body></body></head>

d) <html><head></head><body></body></html>

Comentário: A resposta correta é a alternativa "a". A estrutura básica de um documento HTML começa com a declaração <!DOCTYPE html>, seguida pelas tags <html>, <head> e <body>. A tag <head> foi omitida nessa opção, mas a estrutura ainda é válida. As outras alternativas apresentam erros de estrutura ou falta de elementos importantes.

Questão 2

Qual elemento HTML é usado para criar um link?

a) <a href="url">Texto do link</a>

b) <link src="url">Texto do link</link>

c) <url="url">Texto do link</url>

d) <hyperlink url="url">Texto do link</hyperlink>

Comentário: A resposta correta é a alternativa "a". O elemento HTML usado para criar um link é a tag <a> com o atributo "href" para especificar a URL. As outras alternativas apresentam elementos HTML incorretos ou mal formatados para criar um link.
