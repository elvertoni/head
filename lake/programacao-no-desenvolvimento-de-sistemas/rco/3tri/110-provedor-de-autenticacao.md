---
titulo: "Provedor de autenticação"
tipo: rco-seed
disciplina: programacao-no-desenvolvimento-de-sistemas
sigla_rco: PDS
trimestre: 3
ordem_rco: 110
serie: 3
aula_rco: "Aula 110"
slides: 23
tem_atividade: false
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/3TRI/110-provedor-de-autenticacao/110-provedor-de-autenticacao.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/3TRI/110-provedor-de-autenticacao/AULA 110_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Provedor de autenticação

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO NO
- DESENVOLVIMENTO DE
- SISTEMAS
- 3ª SÉRIE
- Provedor de autenticação
- Aula 110

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
- Aprender a configurar um provedor de autenticação no Spring MVC usando JDBC e Spring Security.

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
- Vimos como implementar autenticação com Spring Security, criando rotas e protegendo dados. Hoje, vamos conectar essa autenticação a um banco de dados, usando JDBC como provedor para validar e gerenciar os usuários.

_4 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Lívia está criando uma aplicação de gerenciamento de biblioteca e quer que o login seja feito com base nas informações de um banco de dados de usuários. Ela precisa configurar um sistema que permita autenticar os usuários com segurança e garantir que apenas aqueles com conta válida possam acessar o sistema.

_4 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Pergunta
- Duas Soluções Possíveis:
- Usar JDBC Authentication: Permite verificar logins diretamente no banco de dados, facilitando a gestão de usuários sem alterar o código.
- Criar uma lista manual de usuários no código: Exige modificar o código para atualizar usuários, tornando a manutenção mais difícil.
- Quem sabe responde!

_4 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Correta: JDBC Authentication permite flexibilidade e segurança ao verificar usuários diretamente no banco de dados, facilitando a gestão de contas sem alterar o código.
- Falsa: Manter usuários em uma lista no código é inviável para aplicações reais, pois torna a atualização de usuários difícil e menos segura.

_5 imagem(ns) no slide._

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- Autenticação
- Um provedor de autenticação em Spring MVC define como o sistema verificará as credenciais dos usuários. Com JDBC Authentication, o Spring Security consulta um banco de dados, garantindo uma gestão flexível e segura.

_4 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- Aplicações
- Usando JDBC Authentication: Conecta o Spring Security a um banco de dados usando JDBC para validar usuários, permitindo que as credenciais sejam gerenciadas diretamente nas tabelas do banco.
- Spring Security: O Spring Security facilita a criação de mecanismos de segurança, como autenticação, com configurações prontas e proteção de rotas.

_4 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- A autenticação baseada em banco de dados oferece flexibilidade para gerenciar usuários sem modificar o código, o que torna o sistema mais seguro e fácil de manter, especialmente em aplicações com muitos usuários.

_4 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- Em um sistema de escola online, as contas dos alunos e professores são armazenadas no banco de dados. A autenticação com JDBC permite que o sistema valide automaticamente as credenciais e atualize permissões, se necessário.

_4 imagem(ns) no slide._

### Slide 13

- DESENVOLVIMENTO DE SISTEMAS
- Exemplo
- configuração de JDBC Authentication com Spring Security

_4 imagem(ns) no slide._

### Slide 14

- DESENVOLVIMENTO DE SISTEMAS
- Questão de fixação
- Qual é a principal vantagem de usar JDBC Authentication em uma aplicação?
- A) Simplifica o código ao não precisar de banco de dados.
- B) Permite que o Spring Security autentique usuários diretamente de um banco de dados.
- C) Torna o acesso mais rápido por não verificar credenciais.
- D) Elimina a necessidade de configuração de segurança.
- Quem sabe responde!

_4 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- Resposta!
- Qual é a principal vantagem de usar JDBC Authentication em uma aplicação?
- A) Simplifica o código ao não precisar de banco de dados.
- B) Permite que o Spring Security autentique usuários diretamente de um banco de dados.
- C) Torna o acesso mais rápido por não verificar credenciais.
- D) Elimina a necessidade de configuração de segurança.
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
- Usando JDBC Authentication
- 10 minutos
- Link para tarefa: https://cursos.alura.com.br/course/spring-mvc-security-rest-vuejs-ajax/task/81129
- Usar JDBC Authentication conecta o Spring Security a um banco de dados para autenticar usuários. As credenciais são verificadas nas tabelas do banco, facilitando o gerenciamento e a atualização de usuários sem modificar o código.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje
- Aprendemos como configurar um provedor de autenticação usando Spring Security e JDBC no Spring MVC. Essa abordagem permite que as credenciais dos usuários sejam validadas diretamente no banco de dados, tornando o sistema seguro e facilmente gerenciável.

_4 imagem(ns) no slide._

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- Pronto para desbloquear sua carreira de TI?
- Está perdido estudando mas não sabe por onde começar? Se a resposta é sim, você está no lugar certo! Descubra as estratégias e ferramentas essenciais para te ajudar a desbloquear seu potencial em TI e buscar sua primeira vaga de emprego no setor!
- Este e-book é um guia completo para quem busca começar pelos melhores caminhos para se tornar um excelente profissional de TI, ensinando a identificar perfis profissionais, aplicar técnicas de estudo eficazes, transformar teoria em prática, e aumentar a visibilidade de seu trabalho no mercado de trabalho. Ideal para novatos e profissionais em transição.
- E o melhor, ele pode ser seu, inteiramente grátis!
- Basta clicar AQUI e realizar o seu cadastro com o seu @escola!

_5 imagem(ns) no slide._

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

_Fonte: AULA 110_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

ATIVIDADE AULA 110

Questão 1

Qual consulta SQL é usada para definir permissões no JDBC Authentication?

A) permissionsByUsernameQuery

B) usersByUsernameQuery

C) authoritiesByUsernameQuery

D) rolesByUsernameQuery

Resposta:

Resposta correta: C)

A consulta authoritiesByUsernameQuery define como o Spring Security buscará as permissões do usuário no banco de dados.

Questão 2

Por que é recomendado armazenar usuários em um banco de dados em vez de uma lista fixa?

A) Para permitir atualizações rápidas sem mudar o código.

B) Para reduzir o número de consultas SQL.

C) Para excluir a necessidade de login.

D) Para definir funções fixas no código.

Resposta:

Resposta correta: A)

Armazenar usuários em um banco permite atualizações dinâmicas, como criar ou modificar contas sem alterar o código da aplicação.
