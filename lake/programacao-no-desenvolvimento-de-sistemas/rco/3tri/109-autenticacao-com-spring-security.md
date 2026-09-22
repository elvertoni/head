---
titulo: "Autenticação com Spring Security"
tipo: rco-seed
disciplina: programacao-no-desenvolvimento-de-sistemas
sigla_rco: PDS
trimestre: 3
ordem_rco: 109
serie: 3
aula_rco: "Aula 109"
slides: 23
tem_atividade: false
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/3TRI/109-autenticacao-com-spring-security/109-autenticacao-com-spring-security.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/3TRI/109-autenticacao-com-spring-security/AULA 109_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Autenticação com Spring Security

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO NO
- DESENVOLVIMENTO DE
- SISTEMAS
- 3ª SÉRIE
- Autenticação com Spring Security
- Aula 109

_3 imagem(ns) no slide._

### Slide 2

_(sem texto)_

_1 imagem(ns) no slide._

### Slide 3

- DESENVOLVIMENTO DE SISTEMAS
- Nesta aula, vamos:
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store
- Explorar como implementar autenticação em uma aplicação Spring MVC usando Spring Security.

_7 imagem(ns) no slide._

### Slide 4

- DESENVOLVIMENTO DE SISTEMAS
- ATENÇÃO PROFESSOR!
- O Material aqui apresentado, segue a análise do plano de curso contemplando os componentes curriculares e seus objetos de conhecimento, sendo assim, você tem liberdade para customizar o material conforme seu contexto para maior aproveitamento do conteúdo. Em caso de falta ou indisponibilidade de acesso à internet no local de aula, você poderá utilizar os seguintes artigos para criação de material complementar para auxiliar na aula:
- Leitura/Recursos Adicionais:
- Spring Initializr (start.spring.io): Uma ferramenta online que permite criar projetos Spring Boot rapidamente. Você pode selecionar dependências como Spring Data JPA e H2 Database para começar.

_5 imagem(ns) no slide._

### Slide 5

- DESENVOLVIMENTO DE SISTEMAS
- Na aula anterior…
- Focamos na formatação e finalização de interfaces no Spring MVC, ajustando a apresentação de dados como datas e números para uma exibição clara e padronizada. Hoje, partiremos desse layout refinado para implementar um sistema de autenticação seguro.

_4 imagem(ns) no slide._

### Slide 6

- Para pensarmos juntos!
- Marcos está desenvolvendo uma aplicação de e-commerce e quer proteger a área administrativa, permitindo acesso apenas a usuários autorizados.
- DESENVOLVIMENTO DE SISTEMAS
- Ele não tem certeza de como configurar o login e o controle de permissões para que apenas usuários administradores possam acessar essas rotas.

_4 imagem(ns) no slide._

### Slide 7

- Como Marcos pode usar Spring Security para configurar um sistema de login e controlar o acesso a áreas específicas da aplicação?
- Quem sabe responde!
- DESENVOLVIMENTO DE SISTEMAS
- Pergunta

_5 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Marcos pode usar Spring Security para definir regras de autenticação, criando uma tela de login e configurando permissões para rotas. Ele pode atribuir funções aos usuários, permitindo que apenas administradores tenham acesso a determinadas páginas.

_4 imagem(ns) no slide._

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- A autenticação com Spring Security é um recurso que permite proteger uma aplicação Spring MVC, garantindo que somente usuários autorizados possam acessar certas rotas e dados.
- É fundamental para proteger informações e regular o acesso.

_4 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- Controle de Acesso
- Define permissões para diferentes rotas, permitindo que apenas usuários com funções específicas acessem páginas restritas.
- Autenticação com Spring Security
- Configura o login de usuários e verifica suas credenciais para acessar a aplicação.
- Implementação de Login e Logout
- Configura páginas de login personalizadas e permite que os usuários saiam de suas contas com segurança.

_4 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Em qualquer aplicação com informações sensíveis, é importante ter um sistema de autenticação que impeça o acesso não autorizado.
- O Spring Security facilita essa implementação, garantindo a segurança dos dados e do sistema.

_4 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- Em um portal educacional, apenas administradores podem adicionar novos cursos, enquanto alunos têm acesso restrito ao conteúdo de suas aulas.
- O Spring Security permite implementar essas restrições de forma organizada e segura.

_4 imagem(ns) no slide._

### Slide 13

- DESENVOLVIMENTO DE SISTEMAS
- Exemplo
- Configuração básica de autenticação com Spring Security

_4 imagem(ns) no slide._

### Slide 14

- DESENVOLVIMENTO DE SISTEMAS
- Questão de fixação
- Qual é a principal função do Spring Security em uma aplicação?
- A) Aumentar a velocidade da aplicação.
- B) Proteger a aplicação e controlar o acesso a rotas e dados.
- C) Simplificar a navegação do usuário.
- D) Melhorar a formatação de dados.
- Quem sabe responde!

_4 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- Resposta!
- Qual é a principal função do Spring Security em uma aplicação?
- A) Aumentar a velocidade da aplicação.
- B) Proteger a aplicação e controlar o acesso a rotas e dados.
- C) Simplificar a navegação do usuário.
- D) Melhorar a formatação de dados.
- Resposta correta: B)

_3 imagem(ns) no slide._

### Slide 16

- DESENVOLVIMENTO DE SISTEMAS
- Atividade Prática na Plataforma Alura
- Na plataforma Alura vamos acessar o seguinte curso:
- A recomendação é que você continue esse curso extraclasse, pois ele traz um conteúdo essencial para compreender sobre o referido tema.
- Link para o curso: https://cursos.alura.com.br/course/spring-mvc-security-rest-vuejs-ajax

_6 imagem(ns) no slide._

### Slide 17

- DESENVOLVIMENTO DE SISTEMAS
- Implementando o Login
- 15 minutos
- Link para tarefa: https://cursos.alura.com.br/course/spring-mvc-security-rest-vuejs-ajax/task/81125
- Implementar o login com Spring Security envolve configurar uma página de autenticação, onde os usuários inserem suas credenciais. O Spring verifica essas informações e permite o acesso com base nas permissões.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje
- Exploramos como proteger uma aplicação com autenticação usando Spring Security no Spring MVC. Aprendemos a configurar rotas seguras e a definir permissões, garantindo que usuários autorizados acessem apenas o conteúdo apropriado. Esse conhecimento aumenta a segurança e a confiabilidade de uma aplicação, criando uma experiência de uso mais controlada e profissional.

_4 imagem(ns) no slide._

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- Pronto para desbloquear sua carreira em TI?
- Está perdido estudando mas não sabe por onde começar? Se a resposta é sim, você está no lugar certo! Descubra as estratégias e ferramentas essenciais para te ajudar a desbloquear seu potencial em TI e buscar sua primeira vaga de emprego no setor!
- Este e-book é um guia completo para quem busca começar pelos melhores caminhos para se tornar um excelente profissional de TI, ensinando a identificar perfis profissionais, aplicar técnicas de estudo eficazes, transformar teoria em prática, e aumentar a visibilidade de seu trabalho no mercado de trabalho. Ideal para novatos e profissionais em transição.
- E o melhor, ele pode ser seu, inteiramente grátis!

_7 imagem(ns) no slide._

### Slide 20

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

### Slide 21

- DESENVOLVIMENTO DE SISTEMAS
- Referências (Imagens)
- Figuras e Imagens:
- https://www.flaticon.com/br
- https://www.istockphoto.com/br
- https://raw.githubusercontent.com/zbtang/React-Native-ViewPager/HEAD/imgs/dotIndicator.gif
- https://storyset.com

_3 imagem(ns) no slide._

### Slide 22

- DESENVOLVIMENTO DE SISTEMAS
- O RCO+Aulas é um projeto da Secretaria de Estado da Educação do Paraná e está em constante revisão. Todos os slides são de uso exclusivo dos professores da Rede Pública de Ensino, com a finalidade específica de aplicação em sala de aula, sendo totalmente vedada a publicização, reutilização, reprodução total ou parcial para quaisquer outros fins.

_4 imagem(ns) no slide._

### Slide 23

- DESENVOLVIMENTO DE SISTEMAS
- Esta publicação tem a cooperação entre a UNESCO e a Secretaria de Estado da Educação e do Esporte do Paraná no âmbito da parceria PRODOC 914BRZ1091, cujo objetivo é trazer soluções inovadoras de gestão da rede pública estadual de educação do Paraná para a melhoria da aprendizagem dos alunos. As indicações de nomes e a apresentação do material ao longo desta publicação não implicam a manifestação de qualquer opinião por parte da UNESCO a respeito da condição jurídica de qualquer país, território, cidade, região ou de suas autoridades, tampouco da delimitação de suas fronteiras ou limites As ideias e opiniões expressas nesta publicação são as dos autores e não refletem obrigatoriamente as da UNESCO nem comprometem a Organização.
- Cooperação Técnica

_5 imagem(ns) no slide._

## Outros documentos

_Fonte: AULA 109_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

ATIVIDADE AULA 109

Questão 1

Qual anotação permite habilitar o uso do Spring Security em um projeto?

A) @EnableSecurity

B) @EnableWebSecurity

C) @SpringSecurity

D) @SecurityConfig

Resposta:

Resposta correta: B)

A anotação @EnableWebSecurity permite que o Spring Security seja configurado e utilizado em um projeto Spring MVC.

Questão 2

Por que é importante proteger rotas administrativas em uma aplicação?

A) Para limitar a quantidade de dados exibidos.

B) Para evitar acesso não autorizado e proteger informações sensíveis.

C) Para simplificar o layout da aplicação.

D) Para aumentar a velocidade de carregamento das páginas.

Resposta:

Resposta correta: B)

Proteger rotas administrativas impede o acesso de usuários não autorizados, garantindo que informações confidenciais e funcionalidades críticas estejam seguras.
