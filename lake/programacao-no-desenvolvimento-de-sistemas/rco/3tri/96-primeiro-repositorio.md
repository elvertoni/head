---
titulo: "Primeiro Repositório"
tipo: rco-seed
disciplina: programacao-no-desenvolvimento-de-sistemas
sigla_rco: PDS
trimestre: 3
ordem_rco: 96
serie: 3
aula_rco: "Aula 96"
slides: 25
tem_atividade: false
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/3TRI/96-primeiro-repositorio/96-primeiro-repositorio.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/3TRI/96-primeiro-repositorio/AULA 96_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Primeiro Repositório

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO NO
- DESENVOLVIMENTO DE
- SISTEMAS
- 3ª SÉRIE
- Primeiro Repositório
- Aula 96

_3 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- DESENVOLVIMENTO DE SISTEMAS
- Nesta aula, vamos:
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store
- Explorar como configurar um ambiente de desenvolvimento Spring Data.

_7 imagem(ns) no slide._

### Slide 4

- DESENVOLVIMENTO DE SISTEMAS
- ATENÇÃO PROFESSOR!
- O Material aqui apresentado, segue a análise do plano de curso contemplando os componentes curriculares e seus objetos de conhecimento, sendo assim, você tem liberdade para customizar o material conforme seu contexto para maior aproveitamento do conteúdo. Em caso de falta ou indisponibilidade de acesso à internet no local de aula, você poderá utilizar os seguintes artigos para criação de material complementar para auxiliar na aula:
- Leitura/Recursos Adicionais:
- Spring Initializr – Ferramenta online para gerar projetos Spring Boot de maneira rápida e eficiente.
- DBeaver – Ferramenta gráfica open-source para gerenciar e visualizar bancos de dados. Postman – Ferramenta para testar APIs e simular requisições, ideal para validar endpoints criados no projeto.

_5 imagem(ns) no slide._

### Slide 5

- DESENVOLVIMENTO DE SISTEMAS
- Na aula anterior…
- Exploramos os conceitos iniciais de frameworks Java e como eles ajudam a organizar o código e aumentar a produtividade no desenvolvimento de aplicações. Discutimos Spring, Hibernate e JavaFX, com exemplos de configuração e uso.

_4 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Bruno é um estudante de desenvolvimento que deseja criar uma aplicação simples para gerenciar uma lista de contatos. Ele precisa salvar os dados em um banco de dados e não quer lidar diretamente com comandos SQL. Após pesquisas, ele descobre que o Spring Data pode facilitar seu trabalho, mas não sabe como implementar essa funcionalidade.

_4 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Pergunta
- Como o Spring Data pode ajudar Bruno a gerenciar sua lista de contatos sem a necessidade de comandos SQL manuais?
- Quem sabe responde!

_5 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- O Spring Data oferece o CrudRepository, uma interface que já possui métodos prontos para inclusão, leitura, atualização e exclusão de dados. Isso permite a Bruno focar na lógica da aplicação e usar métodos simples como save(), findById(), e delete() para manipular as informações no banco.

_4 imagem(ns) no slide._

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- Spring Data
- O Spring Data é um módulo do Spring Framework que simplifica o acesso a dados em aplicações Java, permitindo que os desenvolvedores manipulem informações sem precisar escrever SQL diretamente. Isso é feito por meio de repositórios que interagem com o banco de dados.

_4 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- Definição e Aplicação
- O Spring Data oferece um modelo de repositório para trabalhar com persistência de dados. Interfaces como CrudRepository e JpaRepository permitem implementar operações de CRUD (Create, Read, Update, Delete) facilmente. É utilizado para conectar a aplicação com diversos tipos de bancos, como MySQL, PostgreSQL e MongoDB.

_4 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Importância
- Usar Spring Data aumenta a produtividade, facilita a leitura do código e diminui a quantidade de erros, especialmente para iniciantes. Com ele, desenvolvedores podem criar aplicações robustas e escaláveis sem precisar de conhecimento profundo de SQL.

_4 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- Uso
- Spring Data é amplamente utilizado em projetos que precisam manipular grandes volumes de dados, como sistemas de cadastro e gerenciamento de usuários. Ele também é usado em projetos que requerem consultas personalizadas, integração com APIs REST e operações complexas de banco de dados.

_4 imagem(ns) no slide._

### Slide 13

- DESENVOLVIMENTO DE SISTEMAS
- Exemplo de uso do CrudRepository para criar e listar clientes em uma aplicação Spring Boot.
- Utilize o replit

_5 imagem(ns) no slide._

### Slide 14

- DESENVOLVIMENTO DE SISTEMAS
- Questão de fixação
- Qual interface é utilizada no Spring Data para implementar operações de CRUD de maneira simplificada?
- A) CrudOperations
- B) Repository
- C) CrudRepository
- D) JpaOperations
- Quem sabe responde!

_4 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- Resposta!
- Qual interface é utilizada no Spring Data para implementar operações de CRUD de maneira simplificada?
- A) CrudOperations
- B) Repository
- C) CrudRepository
- D) JpaOperations
- Resposta: C) CrudRepository.

_3 imagem(ns) no slide._

### Slide 16

- DESENVOLVIMENTO DE SISTEMAS
- Atividade Prática na Plataforma Alura
- Na plataforma Alura vamos acessar o seguinte curso:
- A recomendação é que você continue esse curso extraclasse, pois ele traz um conteúdo essencial para compreender sobre o referido tema.
- Link para o curso: https://cursos.alura.com.br/course/spring-data-jpa

_6 imagem(ns) no slide._

### Slide 17

- DESENVOLVIMENTO DE SISTEMAS
- Configuração de ambiente
- 3 minutos
- Link para tarefa: https://cursos.alura.com.br/course/spring-data-jpa/task/83450
- A configuração de ambiente no Spring Data envolve definir o arquivo application.properties com detalhes de conexão ao banco de dados, como URL, usuário, senha, e ativar o suporte a JPA com spring-boot-starter-data-jpa.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- Criando a aplicação
- 7 minutos
- Link para tarefa: https://cursos.alura.com.br/course/spring-data-jpa/task/83451
- Criar a aplicação em Spring Data envolve definir a classe principal com @SpringBootApplication, configurar as entidades com @Entity e criar interfaces de repositório com CrudRepository para operações básicas.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- Configurando o banco
- 8 minutos
- Link para tarefa: https://cursos.alura.com.br/course/spring-data-jpa/task/83452
- Configurar o banco em Spring Data envolve definir a conexão no application.properties (URL, usuário e senha), usar @Entity para as classes e @Table para mapear as tabelas no banco de dados.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 20

- DESENVOLVIMENTO DE SISTEMAS
- Gerando o banco de dados
- 10 minutos
- Link para tarefa: https://cursos.alura.com.br/course/spring-data-jpa/task/83453
- Gerar o banco de dados no Spring Data envolve configurar spring.jpa.hibernate.ddl-auto para update ou create no application.properties, permitindo que o JPA crie automaticamente as tabelas.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 21

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje
- Aprendemos a configurar e utilizar o Spring Data em uma aplicação Java. Exploramos como os repositórios simplificam a manipulação de dados e criamos um exemplo prático para salvar e listar informações no banco de dados, focando em produtividade e simplicidade no desenvolvimento.

_4 imagem(ns) no slide._

### Slide 22

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

### Slide 23

- DESENVOLVIMENTO DE SISTEMAS
- Referências (Imagens)
- Figuras e Imagens:
- https://www.flaticon.com/br
- https://www.istockphoto.com/br
- https://raw.githubusercontent.com/zbtang/React-Native-ViewPager/HEAD/imgs/dotIndicator.gif
- https://storyset.com

_3 imagem(ns) no slide._

### Slide 24

- DESENVOLVIMENTO DE SISTEMAS
- O RCO+Aulas é um projeto da Secretaria de Estado da Educação do Paraná e está em constante revisão. Todos os slides são de uso exclusivo dos professores da Rede Pública de Ensino, com a finalidade específica de aplicação em sala de aula, sendo totalmente vedada a publicização, reutilização, reprodução total ou parcial para quaisquer outros fins.

_4 imagem(ns) no slide._

### Slide 25

- DESENVOLVIMENTO DE SISTEMAS
- Esta publicação tem a cooperação entre a UNESCO e a Secretaria de Estado da Educação e do Esporte do Paraná no âmbito da parceria PRODOC 914BRZ1091, cujo objetivo é trazer soluções inovadoras de gestão da rede pública estadual de educação do Paraná para a melhoria da aprendizagem dos alunos. As indicações de nomes e a apresentação do material ao longo desta publicação não implicam a manifestação de qualquer opinião por parte da UNESCO a respeito da condição jurídica de qualquer país, território, cidade, região ou de suas autoridades, tampouco da delimitação de suas fronteiras ou limites As ideias e opiniões expressas nesta publicação são as dos autores e não refletem obrigatoriamente as da UNESCO nem comprometem a Organização.
- Cooperação Técnica

_4 imagem(ns) no slide._

## Outros documentos

_Fonte: AULA 96_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

ATIVIDADE AULA 96

Questão 1

Qual é a função principal do método save() no CrudRepository?

A) Apagar registros duplicados.

B) Atualizar ou inserir um registro no banco de dados.

C) Realizar buscas complexas.

D) Estabelecer uma conexão com o banco de dados.

Resposta:

B) Atualizar ou inserir um registro no banco de dados.

Explicação: O método save() é utilizado para inserir um novo registro ou atualizar um existente, se a entidade já estiver presente no banco.

Questão 2

Qual é o papel da anotação @Autowired no Spring?

A) Definir uma variável global.

B) Executar testes unitários.

C) Injetar dependências automaticamente em uma classe.

D) Configurar transações em bancos de dados.

Resposta:

C) Injetar dependências automaticamente em uma classe.

Explicação: A anotação @Autowired é usada para injetar instâncias de componentes Spring (como serviços ou repositórios) de forma automática.
