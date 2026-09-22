---
titulo: "Introdução ao Spring Boot"
tipo: rco-seed
disciplina: programacao-no-desenvolvimento-de-sistemas
sigla_rco: PDS
trimestre: 3
ordem_rco: 116
serie: 3
aula_rco: "Aula 116"
slides: 26
tem_atividade: false
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/3TRI/116-introducao-ao-spring-boot/116-introducao-ao-spring-boot.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/3TRI/116-introducao-ao-spring-boot/AULA 116_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Introdução ao Spring Boot

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO NO
- DESENVOLVIMENTO DE
- SISTEMAS
- 3ª SÉRIE
- Introdução ao Spring Boot
- Aula 116

_3 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- DESENVOLVIMENTO DE SISTEMAS
- Nesta aula, vamos:
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store
- Conhecer o Spring Boot, um framework poderoso que simplifica a criação de aplicações Java.

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
- Exploramos interceptadores para monitorar o tempo de resposta das requisições, ajudando a medir e otimizar o desempenho de aplicações. Hoje, com o Spring Boot, vamos simplificar as configurações e iniciar projetos mais rapidamente, garantindo eficiência e praticidade.

_4 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Ana começou um projeto Java e está com dificuldades para configurar dependências e arquivos iniciais. Ela quer uma maneira de iniciar seu projeto com as ferramentas já configuradas e otimizadas, economizando tempo para se concentrar no desenvolvimento das funcionalidades.

_4 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Pergunta
- Como Ana pode usar o Spring Boot para iniciar rapidamente seu projeto, evitando configurações complexas e focando nas partes principais do desenvolvimento?
- Quem sabe responde!

_5 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Ana pode usar o Spring Boot para configurar seu projeto automaticamente, gerando a estrutura inicial e as dependências necessárias com o Spring Initializr. Com isso, ela começa seu desenvolvimento rapidamente e evita configurações manuais demoradas.

_4 imagem(ns) no slide._

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- Spring Boot é uma extensão do Spring Framework que torna o desenvolvimento de aplicações mais rápido e fácil, automatizando muitas das configurações e estruturas básicas, como conexões de banco de dados, servidores e pacotes essenciais.

_4 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- Sobre Spring e Spring Boot: O Spring é um framework Java usado para criar aplicações robustas. Spring Boot é uma ferramenta baseada no Spring que simplifica a criação dessas aplicações, eliminando a necessidade de configurações extensivas.
- Início rápido com Spring Boot: Com o Spring Boot, as configurações são automaticamente geradas, deixando o desenvolvedor livre para se concentrar nas funcionalidades e evitando erros comuns de configuração.

_4 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Spring Boot permite iniciar projetos de forma mais eficiente, o que é fundamental em um cenário de desenvolvimento ágil e iterativo. Ele é amplamente usado para criar APIs e aplicações que precisam de uma estrutura robusta e escalável, oferecendo uma configuração simplificada.

_4 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- Em uma aplicação de gestão escolar, Spring Boot pode ser usado para configurar rapidamente o ambiente, permitindo que a equipe de desenvolvimento se concentre nas funcionalidades, como controle de alunos e professores.

_4 imagem(ns) no slide._

### Slide 13

- DESENVOLVIMENTO DE SISTEMAS
- Exemplo
- 1- Criando o projeto no Spring Initializr:
- Acesse Spring Initializr.
- Selecione Spring Boot 2.7 ou superior, linguagem Java, e escolha dependências como Spring Web.
- Clique em "Generate" para baixar o projeto configurado.
- 2 - Exemplo de Controlador em Spring Boot:

_4 imagem(ns) no slide._

### Slide 14

- DESENVOLVIMENTO DE SISTEMAS
- Exemplo
- 3 - Abra o projeto na IDE e execute-o. O Spring Boot configurará automaticamente o servidor e o endpoint estará disponível em http://localhost:8080/hello.
- Neste exemplo, o Spring Boot cuida da configuração do servidor, permitindo que o desenvolvedor se concentre nas funcionalidades, como a criação de um endpoint de exemplo.

_3 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- Questão de fixação
- Qual é a principal vantagem de usar o Spring Boot?
- A) Evitar o uso do framework Spring.
- B) Simplificar e automatizar as configurações de uma aplicação.
- C) Alterar a linguagem da aplicação para JavaScript.
- D) Substituir o servidor da aplicação por um banco de dados.
- Quem sabe responde!

_4 imagem(ns) no slide._

### Slide 16

- DESENVOLVIMENTO DE SISTEMAS
- Resposta!
- Qual é a principal vantagem de usar o Spring Boot?
- A) Evitar o uso do framework Spring.
- B) Simplificar e automatizar as configurações de uma aplicação.
- C) Alterar a linguagem da aplicação para JavaScript.
- D) Substituir o servidor da aplicação por um banco de dados.
- Resposta correta: B)

_3 imagem(ns) no slide._

### Slide 17

- DESENVOLVIMENTO DE SISTEMAS
- Atividade Prática na Plataforma Alura
- Na plataforma Alura vamos acessar o seguinte curso:
- A recomendação é que você continue esse curso extraclasse, pois ele traz um conteúdo essencial para compreender sobre o referido tema.
- Link para o curso: https://cursos.alura.com.br/course/spring-boot-api-rest

_6 imagem(ns) no slide._

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- Recuperando valores com JavaScript
- 9 minutos
- Link para tarefa: https://cursos.alura.com.br/course/spring-boot-api-rest/task/55815
- Spring é um framework Java robusto para construir aplicações complexas. Spring Boot é uma extensão que simplifica o uso do Spring, automatizando configurações e permitindo um desenvolvimento mais rápido e eficiente.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje
- Conhecemos o Spring Boot e como ele facilita o desenvolvimento, eliminando configurações complexas e automatizando o setup do projeto. Com ele, desenvolvedores podem começar rapidamente, focando nas funcionalidades principais.

_4 imagem(ns) no slide._

### Slide 20

_(sem texto)_

_1 imagem(ns) no slide._

### Slide 21

_(sem texto)_

_1 imagem(ns) no slide._

### Slide 22

- DESENVOLVIMENTO DE SISTEMAS
- Pronto para desbloquear sua carreira de TI?
- Está perdido estudando mas não sabe por onde começar? Se a resposta é sim, você está no lugar certo! Descubra as estratégias e ferramentas essenciais para te ajudar a desbloquear seu potencial em TI e buscar sua primeira vaga de emprego no setor!
- Este e-book é um guia completo para quem busca começar pelos melhores caminhos para se tornar um excelente profissional de TI, ensinando a identificar perfis profissionais, aplicar técnicas de estudo eficazes, transformar teoria em prática, e aumentar a visibilidade de seu trabalho no mercado de trabalho. Ideal para novatos e profissionais em transição.
- E o melhor, ele pode ser seu, inteiramente grátis!
- Basta clicar AQUI e realizar o seu cadastro com o seu @escola!

_5 imagem(ns) no slide._

### Slide 23

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

### Slide 24

- DESENVOLVIMENTO DE SISTEMAS
- Referências (Imagens)
- Figuras e Imagens:
- https://www.flaticon.com/br
- https://www.istockphoto.com/br
- https://raw.githubusercontent.com/zbtang/React-Native-ViewPager/HEAD/imgs/dotIndicator.gif
- https://storyset.com

_3 imagem(ns) no slide._

### Slide 25

- DESENVOLVIMENTO DE SISTEMAS
- O RCO+Aulas é um projeto da Secretaria de Estado da Educação do Paraná e está em constante revisão. Todos os slides são de uso exclusivo dos professores da Rede Pública de Ensino, com a finalidade específica de aplicação em sala de aula, sendo totalmente vedada a publicização, reutilização, reprodução total ou parcial para quaisquer outros fins.

_4 imagem(ns) no slide._

### Slide 26

- DESENVOLVIMENTO DE SISTEMAS
- Esta publicação tem a cooperação entre a UNESCO e a Secretaria de Estado da Educação e do Esporte do Paraná no âmbito da parceria PRODOC 914BRZ1091, cujo objetivo é trazer soluções inovadoras de gestão da rede pública estadual de educação do Paraná para a melhoria da aprendizagem dos alunos. As indicações de nomes e a apresentação do material ao longo desta publicação não implicam a manifestação de qualquer opinião por parte da UNESCO a respeito da condição jurídica de qualquer país, território, cidade, região ou de suas autoridades, tampouco da delimitação de suas fronteiras ou limites As ideias e opiniões expressas nesta publicação são as dos autores e não refletem obrigatoriamente as da UNESCO nem comprometem a Organização.
- Cooperação Técnica

_5 imagem(ns) no slide._

## Outros documentos

_Fonte: AULA 116_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

ATIVIDADE AULA 116

Questão 1

Qual anotação é usada para definir um controlador REST em Spring Boot?

A) @Service

B) @Component

C) @RestController

D) @BootController

Resposta:

Resposta correta: C)

@RestController define uma classe como um controlador REST, permitindo responder a requisições HTTP com JSON, texto, etc.

Questão 2

Qual ferramenta online permite gerar um projeto Spring Boot pré-configurado?

A) Spring Monitor

B) Spring Initializr

C) Spring Inspector

D) Spring Start

Resposta:

Resposta correta: B)

O Spring Initializr é uma ferramenta para criar projetos Spring Boot com dependências e configurações pré-selecionadas.
