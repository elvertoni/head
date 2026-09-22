---
titulo: "Finalizando nossa página HTML"
tipo: rco-seed
disciplina: programacao-front-end
sigla_rco: PFE
trimestre: 2
ordem_rco: 2001
serie: 2
aula_rco: "Aula RETOMADA 2"
slides: 21
tem_atividade: true
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PFE/2TRI/2001-finalizando-nossa-pagina-html/2001-finalizando-nossa-pagina-html.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/2TRI/2001-finalizando-nossa-pagina-html/AULA R2_ATIVIDADE_PROGRAMAÇÃO FRONT END.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Finalizando nossa página HTML

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- Programação Front-End
- 2ª Série
- Finalizando nossa página HTML
- Aula RETOMADA 2

_1 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- COMPETÊNCIA(S) A SER(EM) DESENVOLVIDA(S) NESTA AULA:
- De acordo com o Plano de Curso de Desenvolvimento de Sistemas:
- HABILIDADE(S) A SER(EM) DESENVOLVIDA(S) NESTA AULA:
- Desenvolver interfaces gráficas para aplicações computacionais.
- Aplicar boas práticas de acessibilidade em interfaces web.

_1 imagem(ns) no slide._

### Slide 4

- Nesta aula vamos:
- Conclusão da mais uma página em HTML.
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
- https://github.com/alura-cursos/aluraplus/archive/refs/heads/aula03.zip
- VS Code:
- https://code.visualstudio.com/

_2 imagem(ns) no slide._

### Slide 6

- Aula anterior
- Dando continuidade ao projeto, realizamos os posicionamentos de elementos para podermos deixar a página funcional.

_1 imagem(ns) no slide._

### Slide 7

- Para pensarmos juntos...
- Juliana é uma desenvolvedora web iniciante que trabalha em um projeto de site para uma pequena empresa. Ela precisa criar uma seção de equipe onde as fotos e informações dos membros da equipe sejam exibidas em uma grade responsiva. Juliana sabia que o Flexbox poderia ser usado para resolver esse problema, mas não sabia como aplicá-lo corretamente.
- https://konia.com.br/wp-content/uploads/2020/02/code-1839406_1920-844x563.jpg

_1 imagem(ns) no slide._

### Slide 8

- Para pensarmos juntos...
- Juliana se pergunta: "Como posso usar o Flexbox para criar uma grade responsiva para a seção de equipe do site?"
- Levante a mão quem sabe responder!

_2 imagem(ns) no slide._

### Slide 9

- Resposta
- Para criar uma grade responsiva usando Flexbox, Juliana pode começar definindo a propriedade CSS display: flex; no container que envolve os itens da equipe. Isso transformará o container em um flex container e permitirá que Juliana controle o layout e o alinhamento dos itens da equipe usando as propriedades flexbox.

_1 imagem(ns) no slide._

### Slide 10

- Resposta
- Depois de criar o flex container, ela pode usar a propriedade flex-wrap: wrap; para permitir que os itens da equipe se ajustem automaticamente às linhas seguintes quando não houver espaço suficiente na linha atual. Além disso, Juliana pode usar a propriedade flex nos itens da equipe para controlar o tamanho e a proporção deles em relação aos outros itens. Com essas configurações, a grade responsiva será criada, e os itens da equipe serão ajustados automaticamente para se adaptar a diferentes tamanhos de tela.

_1 imagem(ns) no slide._

### Slide 11

- Conceituando
- O Flexbox, também conhecido como Flexible Box Layout, é um modelo de layout CSS que facilita a criação de layouts responsivos e dinâmicos para páginas HTML. Ele oferece maior flexibilidade e controle sobre o posicionamento e dimensionamento de elementos dentro de um container, permitindo que os elementos se ajustem automaticamente ao espaço disponível. Flexbox é especialmente útil para criar layouts complexos que precisam se adaptar a diferentes tamanhos de tela e dispositivos.
- https://cdn.pixabay.com/photo/2014/07/08/09/58/html5-386614_1280.jpg

_1 imagem(ns) no slide._

### Slide 12

- Conceituando
- Para começar a usar o Flexbox, primeiro você precisa definir um container como um flex container, aplicando a propriedade CSS display: flex;. Ao fazer isso, todos os elementos filhos diretos desse container se tornam itens flexíveis e podem ser posicionados e dimensionados usando as propriedades do Flexbox. Algumas propriedades importantes do Flexbox incluem justify-content, align-items e flex-direction, que controlam o alinhamento e a direção dos itens flexíveis dentro do container.
- https://slideplayer.com.br/slide/3284708/11/images/5/Exemplo+Form+GET+%3Chtml%3E.jpg

_1 imagem(ns) no slide._

### Slide 13

- Conceituando
- Um dos principais benefícios do Flexbox é a capacidade de criar layouts responsivos sem a necessidade de usar técnicas complicadas, como floats ou posicionamento absoluto. Com o Flexbox, você pode criar layouts que se ajustam automaticamente ao tamanho da tela, garantindo que seu site seja adaptável e fácil de usar em uma variedade de dispositivos e tamanhos de tela.
- https://www.seobility.net/en/wiki/images/7/72/HTML-Sitemap.png

_1 imagem(ns) no slide._

### Slide 14

- Conceituando
- Em resumo, o Flexbox é uma poderosa ferramenta CSS que facilita a criação de layouts responsivos e adaptáveis para páginas HTML. Ao usar um flex container e aplicar as propriedades apropriadas do Flexbox, você pode criar layouts complexos e flexíveis que se adaptam automaticamente aos diferentes tamanhos de tela e dispositivos, melhorando a experiência do usuário e facilitando a manutenção do código.
- https://www.seobility.net/en/wiki/images/c/ca/HTML-Special-Characters.png

_1 imagem(ns) no slide._

### Slide 15

- Ainda sobre o HTML e CSS, vamos conhecer praticando?
- Na plataforma Alura vamos acessar o seguinte curso:
- Link para o curso: https://cursos.alura.com.br/course/html-css-praticando-html-css
- Ao longo das atividades, você vai encontrar alguns quizzes e eles não estão ali por acaso! Eles são oportunidades rápidas para testar seu entendimento, reforçar o que aprendeu e identificar pontos que ainda podem melhorar.

_3 imagem(ns) no slide._

### Slide 16

- Flexbox
- 16 minutos
- O que falta fazermos em nossa página? O que vamos fazer nessa aula?
- Link para tarefa: https://cursos.alura.com.br/course/html-css-praticando-html-css/task/103168
- Criar os layouts flexíveis para dispositivos diferentes, com o flexbox temos uma utilidade em criar layouts complexos que precisam se adaptar.
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 17

- Vamos praticar?
- Prepare-se, porque nessa atividade, você vai sair do modo aprender e entrar direto no modo praticar.
- A atividade prática vai colocar você diante de um desafio real, que faz relação com o conteúdo aprendido até aqui.

_1 imagem(ns) no slide._

### Slide 18

- O que vimos na aula de hoje:
- Aprendemos o flexbox em páginas HTML e CSS.

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

_Fonte: AULA R2_ATIVIDADE_PROGRAMAÇÃO FRONT END.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação Front-End

2ª SÉRIE

ATIVIDADE AULA RETOMADA 2

Questão 1

Qual elemento HTML é geralmente usado para representar o footer de um site?

a) <div>

b) <section>

c) <footer>

d) <nav>

Resposta correta: c) <footer>

O elemento <footer> é usado para representar a parte inferior de uma página, onde informações adicionais, como direitos autorais, informações de contato e links úteis são geralmente colocados.

Questão 2

Qual das seguintes pseudo-classes CSS é usada para aplicar estilos a um link quando o cursor do mouse está sobre ele?

a) :active

b) :focus

c) :visited

d) :hover

Resposta correta: d) :hover

A pseudo-classe :hover é usada para aplicar estilos a um elemento (como um link) quando o cursor do mouse está sobre ele. Isso ajuda a fornecer feedback visual e a melhorar a usabilidade do site.
