---
titulo: "O que é AJAX e Vue.js"
tipo: rco-seed
disciplina: programacao-no-desenvolvimento-de-sistemas
sigla_rco: PDS
trimestre: 3
ordem_rco: 113
serie: 3
aula_rco: "Aula 113"
slides: 28
tem_atividade: false
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/3TRI/113-o-que-e-ajax-e-vue-js/113-o-que-e-ajax-e-vue-js.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/3TRI/113-o-que-e-ajax-e-vue-js/AULA 113_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# O que é AJAX e Vue.js

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO NO
- DESENVOLVIMENTO DE
- SISTEMAS
- 3ª SÉRIE
- O que é AJAX e Vue.js
- Aula 113

_3 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- DESENVOLVIMENTO DE SISTEMAS
- Nesta aula, vamos:
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store
- Entender como AJAX e Vue.js ajudam a criar interatividade em aplicações web.

_7 imagem(ns) no slide._

### Slide 4

- DESENVOLVIMENTO DE SISTEMAS
- ATENÇÃO PROFESSOR!
- O Material aqui apresentado, segue a análise do plano de curso contemplando os componentes curriculares e seus objetos de conhecimento, sendo assim, você tem liberdade para customizar o material conforme seu contexto para maior aproveitamento do conteúdo. Em caso de falta ou indisponibilidade de acesso à internet no local de aula, você poderá utilizar os seguintes artigos para criação de material complementar para auxiliar na aula:
- Leitura/Recursos Adicionais:
- Spring Tool Suite (STS): IDE focada em projetos Spring que facilita a integração de APIs, ideal para configurar AJAX com Spring MVC. Visual Studio Code: Editor de código leve com suporte para JavaScript e Vue.js, tornando o desenvolvimento front-end rápido e acessível. Postman: Ferramenta para testar as APIs e verificar o retorno de dados para AJAX, ajudando a depurar os endpoints com rapidez.

_5 imagem(ns) no slide._

### Slide 5

- DESENVOLVIMENTO DE SISTEMAS
- Na aula anterior…
- Vimos como construir uma API REST com Spring MVC, criando endpoints que permitem acessar e manipular dados.
- Hoje, aplicaremos isso para interagir com esses dados em tempo real, usando AJAX e Vue.js para atualizar as páginas sem recarregar.

_4 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- João está criando uma página de notícias onde os novos artigos apareçam automaticamente, sem que os usuários precisem atualizar a página. Ele busca uma solução para buscar e exibir as novas notícias de maneira dinâmica.

_4 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- tem duas soluções possíveis:
- Usar AJAX com Vue.js e Axios: João pode configurar AJAX para atualizar as notícias automaticamente, sem recarregar a página, melhorando a experiência do usuário.
- Recarregar a página a cada nova notícia: Outra opção é programar a página para recarregar a cada nova notícia, mas isso torna a experiência de navegação mais lenta e menos eficiente.
- Quem sabe responde!

_5 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Resposta correta
- AJAX com Vue.js e Axios permite que apenas a lista de notícias seja atualizada, proporcionando uma experiência mais interativa e eficiente.
- Recarregar a página a cada nova notícia aumenta o consumo de dados e piora a navegação, especialmente em páginas dinâmicas.

_7 imagem(ns) no slide._

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- AJAX e Vue.js são usados para criar páginas web interativas. AJAX permite a comunicação com o servidor em segundo plano, enquanto Vue.js é uma biblioteca JavaScript que ajuda a construir interfaces dinâmicas e reativas.

_4 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- AJAX: Técnica para enviar e receber dados do servidor sem recarregar a página, possibilitando atualizações em tempo real.
- Vue.js: Um framework JavaScript que facilita a construção de interfaces reativas e permite manipular elementos da página de forma dinâmica.
- Axios: Biblioteca JavaScript usada com AJAX para simplificar requisições HTTP, popular em projetos Vue.js para comunicação com APIs.

_4 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Essas tecnologias tornam a navegação fluida e intuitiva, com atualizações de dados em tempo real, o que é essencial para criar uma experiência moderna e envolvente.
- AJAX e Vue.js são amplamente usados em aplicações interativas como redes sociais, sites de notícias e e-commerces.

_4 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- Em uma plataforma de vendas, AJAX e Vue.js podem ser usados para atualizar automaticamente o status do estoque sem recarregar a página, permitindo que o cliente veja informações precisas em tempo real.

_4 imagem(ns) no slide._

### Slide 13

- DESENVOLVIMENTO DE SISTEMAS
- Exemplo
- exemplo básico de Vue.js com AJAX usando Axios para buscar e exibir dados de uma API de produtos

_4 imagem(ns) no slide._

### Slide 14

- DESENVOLVIMENTO DE SISTEMAS
- Exemplo
- No JavaScript, configurar o Vue.js e o Axios para buscar dados

_4 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- Questão de fixação
- Qual é a função do AJAX em uma aplicação web?
- A) Recarregar a página a cada atualização.
- B) Enviar e receber dados do servidor sem recarregar a página.
- C) Substituir HTML por JavaScript.
- D) Criar rotas para a aplicação.
- Quem sabe responde!

_4 imagem(ns) no slide._

### Slide 16

- DESENVOLVIMENTO DE SISTEMAS
- Resposta!
- Qual é a função do AJAX em uma aplicação web?
- A) Recarregar a página a cada atualização.
- B) Enviar e receber dados do servidor sem recarregar a página.
- C) Substituir HTML por JavaScript.
- D) Criar rotas para a aplicação.
- Resposta correta: B)

_3 imagem(ns) no slide._

### Slide 17

- DESENVOLVIMENTO DE SISTEMAS
- Atividade Prática na Plataforma Alura
- Na plataforma Alura vamos acessar o seguinte curso:
- A recomendação é que você continue esse curso extraclasse, pois ele traz um conteúdo essencial para compreender sobre o referido tema.
- Link para o curso: https://cursos.alura.com.br/course/spring-mvc-security-rest-vuejs-ajax

_6 imagem(ns) no slide._

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- Introdução ao Vue.js
- 5 minutos
- Link para tarefa: https://cursos.alura.com.br/course/spring-mvc-security-rest-vuejs-ajax/task/81141
- Vue.js é um framework JavaScript que facilita a criação de interfaces dinâmicas e reativas. Ele permite desenvolver componentes que atualizam automaticamente conforme os dados mudam, tornando a experiência do usuário mais interativa e fluida.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- Usando Vue.js
- 13 minutos
- Link para tarefa: https://cursos.alura.com.br/course/spring-mvc-security-rest-vuejs-ajax/task/81142
- Usar Vue.js permite criar componentes visuais interativos e reativos na página. Com ele, é possível desenvolver interfaces que respondem rapidamente às ações do usuário, tornando a navegação intuitiva e dinâmica.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 20

- DESENVOLVIMENTO DE SISTEMAS
- AJAX com Axios
- 7 minutos
- Link para tarefa: https://cursos.alura.com.br/course/spring-mvc-security-rest-vuejs-ajax/task/81143
- AJAX com Axios facilita o envio e recebimento de dados entre o cliente e o servidor sem recarregar a página. Axios simplifica requisições HTTP, tornando a integração com APIs rápida e eficiente, ideal para dados dinâmicos.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 21

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje
- Vimos como AJAX e Vue.js trabalham juntos para criar páginas interativas e atualizadas em tempo real, integrando-se com a API REST que desenvolvemos anteriormente. Com Axios, é fácil buscar dados do servidor e exibi-los na interface sem recarregar, melhorando a fluidez e a experiência do usuário. Esses conceitos são fundamentais para construir aplicações web modernas e responsivas.

_4 imagem(ns) no slide._

### Slide 22

_(sem texto)_

_1 imagem(ns) no slide._

### Slide 23

_(sem texto)_

_1 imagem(ns) no slide._

### Slide 24

- DESENVOLVIMENTO DE SISTEMAS
- Pronto para desbloquear sua carreira de TI?
- Está perdido estudando mas não sabe por onde começar? Se a resposta é sim, você está no lugar certo! Descubra as estratégias e ferramentas essenciais para te ajudar a desbloquear seu potencial em TI e buscar sua primeira vaga de emprego no setor!
- Este e-book é um guia completo para quem busca começar pelos melhores caminhos para se tornar um excelente profissional de TI, ensinando a identificar perfis profissionais, aplicar técnicas de estudo eficazes, transformar teoria em prática, e aumentar a visibilidade de seu trabalho no mercado de trabalho. Ideal para novatos e profissionais em transição.
- E o melhor, ele pode ser seu, inteiramente grátis!
- Basta clicar AQUI e realizar o seu cadastro com o seu @escola!

_5 imagem(ns) no slide._

### Slide 25

- DESENVOLVIMENTO DE SISTEMAS
- Referências
- Bibliografia
- PUREWAL, Semmy. Aprendendo a Desenvolver Aplicações Web. Desenvolva rapidamente com as tecnologias JavaScript mais modernas. São Paulo: Novatec, 2014.
- SILVA, L. F.; OLIVEIRA, A. D. de. Desenvolvimento de Software II C#: programação em camadas. [S. l.]: CBL Edição do Autor, 2017. E-book.
- MARTIN, R. C. Arquitetura limpa: o guia do artesão para estrutura e design de software. Rio de Janeiro: Alta Books, 2019. E-book.
- GALOTTI, G. M. A. Qualidade de software. São Paulo: Pearson Education do Brasil, 2016. E-book.
- VAZQUEZ, C. E.; SIMÕES, G. S. Engenharia de requisitos: software orientado ao negócio. São Paulo: Brasport, 2016. E-book.
- Softwares
- Java Netbeans; WebStorm; Sublime Text; Intellij IDEA; Astah Software; Netbeans; Python; Ccharp; Colab; PyCharm; Jupyter Notebook.

_3 imagem(ns) no slide._

### Slide 26

- DESENVOLVIMENTO DE SISTEMAS
- Referências (Imagens)
- Figuras e Imagens:
- https://www.flaticon.com/br
- https://www.istockphoto.com/br
- https://raw.githubusercontent.com/zbtang/React-Native-ViewPager/HEAD/imgs/dotIndicator.gif
- https://storyset.com

_3 imagem(ns) no slide._

### Slide 27

- DESENVOLVIMENTO DE SISTEMAS
- O RCO+Aulas é um projeto da Secretaria de Estado da Educação do Paraná e está em constante revisão. Todos os slides são de uso exclusivo dos professores da Rede Pública de Ensino, com a finalidade específica de aplicação em sala de aula, sendo totalmente vedada a publicização, reutilização, reprodução total ou parcial para quaisquer outros fins.

_4 imagem(ns) no slide._

### Slide 28

- DESENVOLVIMENTO DE SISTEMAS
- Esta publicação tem a cooperação entre a UNESCO e a Secretaria de Estado da Educação e do Esporte do Paraná no âmbito da parceria PRODOC 914BRZ1091, cujo objetivo é trazer soluções inovadoras de gestão da rede pública estadual de educação do Paraná para a melhoria da aprendizagem dos alunos. As indicações de nomes e a apresentação do material ao longo desta publicação não implicam a manifestação de qualquer opinião por parte da UNESCO a respeito da condição jurídica de qualquer país, território, cidade, região ou de suas autoridades, tampouco da delimitação de suas fronteiras ou limites As ideias e opiniões expressas nesta publicação são as dos autores e não refletem obrigatoriamente as da UNESCO nem comprometem a Organização.
- Cooperação Técnica

_5 imagem(ns) no slide._

## Outros documentos

_Fonte: AULA 113_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

ATIVIDADE AULA 113

Questão 1

Qual biblioteca é comumente usada para fazer requisições AJAX no Vue.js?

A) Fetch

B) HTTPRequest

C) Axios

D) jQuery

Resposta:

Resposta correta: C)

Axios é a biblioteca popular para fazer requisições HTTP no Vue.js, simplificando o uso de AJAX para comunicação com APIs.

Questão 2

Qual é a vantagem de usar AJAX e Vue.js juntos em uma aplicação web?

A) Reduzir a segurança da aplicação.

B) Atualizar apenas partes específicas da página sem recarregá-la totalmente.

C) Evitar o uso de JavaScript na página.

D) Aumentar o tempo de carregamento da página.

Resposta:

Resposta correta: B)

AJAX com Vue.js permite atualizar seções específicas da página, o que melhora a experiência do usuário com uma navegação fluida.
