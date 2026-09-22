---
titulo: "Operações CRUD"
tipo: rco-seed
disciplina: programacao-no-desenvolvimento-de-sistemas
sigla_rco: PDS
trimestre: 3
ordem_rco: 97
serie: 3
aula_rco: "Aula 97"
slides: 29
tem_atividade: false
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/3TRI/97-operacoes-crud/97-operacoes-crud.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/3TRI/97-operacoes-crud/AULA 97_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Operações CRUD

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO NO
- DESENVOLVIMENTO DE
- SISTEMAS
- 3ª SÉRIE
- Operações CRUD
- Aula 97

_3 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- DESENVOLVIMENTO DE SISTEMAS
- Nesta aula, vamos:
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store
- Explorar as operações CRUD usando Spring Data, focando em como salvar, atualizar, visualizar e deletar registros.

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
- Apresentou se o repositório usando Spring Data, configurou o ambiente, gerou um banco de dados e inseriu valores utilizando CrudRepository. Hoje, vamos expandir esse conhecimento para operações completas de manipulação de dados com Spring Data.

_4 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Maria, uma desenvolvedora júnior, está trabalhando em um sistema de gerenciamento de biblioteca. Ela precisa implementar funcionalidades para adicionar novos livros, atualizar informações, visualizar o catálogo e remover livros obsoletos.

_4 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Pergunta
- Como Maria pode utilizar as operações CRUD do Spring Data para implementar essas funcionalidades de forma eficiente e manter o código organizado?
- Quem sabe responde!

_5 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Maria pode aproveitar as operações CRUD do Spring Data implementando um repositório que estenda JpaRepository<Livro, Long>. Isso fornecerá métodos prontos para uso como save() (para adicionar e atualizar livros), findAll() (para visualizar o catálogo), findById() (para buscar um livro específico) e deleteById() (para remover livros). Ela pode criar um serviço que utilize esse repositório, encapsulando a lógica de negócios e mantendo o código organizado.

_3 imagem(ns) no slide._

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- CRUD
- CRUD representa as quatro operações básicas de persistência: Create (Criar), Read (Ler), Update (Atualizar) e Delete (Deletar). O Spring Data simplifica significativamente a implementação dessas operações em aplicações Java, fornecendo uma camada de abstração sobre o JPA (Java Persistence API).

_4 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- Definição e Aplicação
- CRUD com Spring Data refere-se à utilização de interfaces e métodos predefinidos para realizar operações básicas de banco de dados sem a necessidade de escrever consultas SQL manualmente. Isso se aplica em praticamente todos os sistemas que necessitam persistir dados, desde aplicações web até sistemas de gerenciamento empresarial.

_4 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Importância
- Produtividade: Reduz drasticamente o código boilerplate necessário para operações de banco de dados.
- Padronização: Fornece uma abordagem consistente para interagir com diferentes tipos de

_4 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- Importância
- Segurança: Ajuda a prevenir vulnerabilidades de segurança comuns, como injeção de SQL.
- Manutenibilidade: Facilita a manutenção e evolução do código ao longo do tempo.

_4 imagem(ns) no slide._

### Slide 13

- DESENVOLVIMENTO DE SISTEMAS
- Uso
- Na prática, você cria uma interface que estende JpaRepository, especificando a entidade e o tipo do ID. Por exemplo:

_4 imagem(ns) no slide._

### Slide 14

- DESENVOLVIMENTO DE SISTEMAS
- Uso
- Com isso, você ganha acesso a métodos como:save(Livro livro): Para criar ou atualizar um livrofindById(Long id): Para buscar um livro específicofindAll(): Para listar todos os livrosdeleteById(Long id): Para deletar um livro

_4 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- Este exemplo demonstra como implementar operações CRUD básicas usando Spring Data JPA em uma aplicação Spring Boot.
- Utilize o Replit

_5 imagem(ns) no slide._

### Slide 16

- DESENVOLVIMENTO DE SISTEMAS
- Este exemplo demonstra como implementar operações CRUD básicas usando Spring Data JPA em uma aplicação Spring Boot.
- Utilize o Replit

_5 imagem(ns) no slide._

### Slide 17

- DESENVOLVIMENTO DE SISTEMAS
- Este exemplo demonstra como implementar operações CRUD básicas usando Spring Data JPA em uma aplicação Spring Boot.
- Utilize o Replit

_5 imagem(ns) no slide._

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- Este exemplo demonstra como implementar operações CRUD básicas usando Spring Data JPA em uma aplicação Spring Boot.
- Utilize o Replit

_5 imagem(ns) no slide._

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- Questão de fixação
- Qual método do CrudRepository é utilizado para buscar um registro pelo seu ID?
- A) findAll()
- B) findById()
- C) save()
- D) deleteById()
- Quem sabe responde!

_4 imagem(ns) no slide._

### Slide 20

- DESENVOLVIMENTO DE SISTEMAS
- Resposta!
- Qual método do CrudRepository é utilizado para buscar um registro pelo seu ID?
- A) findAll()
- B) findById()
- C) save()
- D) deleteById()
- Resposta: B) findById()

_3 imagem(ns) no slide._

### Slide 21

- DESENVOLVIMENTO DE SISTEMAS
- Atividade Prática na Plataforma Alura
- Na plataforma Alura vamos acessar o seguinte curso:
- A recomendação é que você continue esse curso extraclasse, pois ele traz um conteúdo essencial para compreender sobre o referido tema.
- Link para o curso: https://cursos.alura.com.br/course/spring-data-jpa

_6 imagem(ns) no slide._

### Slide 22

- DESENVOLVIMENTO DE SISTEMAS
- Salvando o registro
- 12 minutos
- Link para tarefa: https://cursos.alura.com.br/course/spring-data-jpa/task/83440
- O método para salvar um registro no Spring Data utiliza save(), que adiciona um novo registro ao banco ou atualiza um existente. É uma forma eficiente de gerenciar dados sem precisar escrever SQL manualmente.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 23

- DESENVOLVIMENTO DE SISTEMAS
- Atualizando o registro
- 9 minutos
- Link para tarefa: https://cursos.alura.com.br/course/spring-data-jpa/task/83441
- A atualização de registros no Spring Data é feita usando o método save() com um objeto que já possui um ID existente. Ele identifica o registro no banco e atualiza os campos com novos valores.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 24

- DESENVOLVIMENTO DE SISTEMAS
- Visualizar e deletar
- 10 minutos
- Link para tarefa: https://cursos.alura.com.br/course/spring-data-jpa/task/83443
- Para visualizar, utilizamos métodos como findById() ou findAll() do Spring Data para buscar dados. Para deletar, usamos deleteById() para remover um registro específico com base no ID fornecido.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 25

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje
- Discutimos como realizar operações CRUD (Salvar, Visualizar, Atualizar e Excluir) no Spring Data, utilizando métodos prontos do CrudRepository. Você aprendeu a importância dessas operações e como aplicá-las para gerenciar um banco de dados em um sistema Spring.

_4 imagem(ns) no slide._

### Slide 26

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

### Slide 27

- DESENVOLVIMENTO DE SISTEMAS
- Referências (Imagens)
- Figuras e Imagens:
- https://www.flaticon.com/br
- https://www.istockphoto.com/br
- https://raw.githubusercontent.com/zbtang/React-Native-ViewPager/HEAD/imgs/dotIndicator.gif
- https://storyset.com

_3 imagem(ns) no slide._

### Slide 28

- DESENVOLVIMENTO DE SISTEMAS
- O RCO+Aulas é um projeto da Secretaria de Estado da Educação do Paraná e está em constante revisão. Todos os slides são de uso exclusivo dos professores da Rede Pública de Ensino, com a finalidade específica de aplicação em sala de aula, sendo totalmente vedada a publicização, reutilização, reprodução total ou parcial para quaisquer outros fins.

_4 imagem(ns) no slide._

### Slide 29

- DESENVOLVIMENTO DE SISTEMAS
- Esta publicação tem a cooperação entre a UNESCO e a Secretaria de Estado da Educação e do Esporte do Paraná no âmbito da parceria PRODOC 914BRZ1091, cujo objetivo é trazer soluções inovadoras de gestão da rede pública estadual de educação do Paraná para a melhoria da aprendizagem dos alunos. As indicações de nomes e a apresentação do material ao longo desta publicação não implicam a manifestação de qualquer opinião por parte da UNESCO a respeito da condição jurídica de qualquer país, território, cidade, região ou de suas autoridades, tampouco da delimitação de suas fronteiras ou limites As ideias e opiniões expressas nesta publicação são as dos autores e não refletem obrigatoriamente as da UNESCO nem comprometem a Organização.
- Cooperação Técnica

_4 imagem(ns) no slide._

## Outros documentos

_Fonte: AULA 97_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

ATIVIDADE AULA 97

Questão 1

Qual é o principal benefício de usar o CrudRepository no Spring Data?

A) Evita a necessidade de configuração de banco de dados.

B) Simplifica operações básicas com banco de dados.

C) Substitui o uso de SQL.

D) Facilita a edição de arquivos front-end.

Resposta: B) Simplifica operações básicas com banco de dados

Explicação: O CrudRepository já implementa métodos como save() e delete(), facilitando a manipulação de dados.

Questão 2

Qual anotação é usada para marcar uma classe como repositório no Spring Data?

A) @Entity

B) @Service

C) @Controller

D) @Repository

Resposta: D) @Repository

Explicação: A anotação @Repository é usada para indicar que a classe é um componente de acesso a dados, responsável por gerenciar as operações CRUD.
