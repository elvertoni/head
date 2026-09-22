---
titulo: "Usando Spring Data"
tipo: rco-seed
disciplina: programacao-no-desenvolvimento-de-sistemas
sigla_rco: PDS
trimestre: 3
ordem_rco: 118
serie: 3
aula_rco: "Aula 118"
slides: 29
tem_atividade: false
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/3TRI/118-usando-spring-data/118-usando-spring-data.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/3TRI/118-usando-spring-data/AULA 118_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Usando Spring Data

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO NO
- DESENVOLVIMENTO DE
- SISTEMAS
- 3ª SÉRIE
- Usando Spring Data
- Aula 118

_3 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- DESENVOLVIMENTO DE SISTEMAS
- Nesta aula, vamos:
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store
- Conhecer o Spring Data JPA, uma ferramenta que facilita o trabalho com bancos de dados em Java.

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
- Abordamos como publicar endpoints em APIs, permitindo a comunicação de dados entre sistemas usando Spring Boot. Hoje, avançaremos para o Spring Data, explorando formas eficientes de acessar e manipular dados, essencial para construir APIs completas.

_4 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Luana está desenvolvendo uma aplicação para gerenciar os pedidos de uma lanchonete. Ela precisa acessar o banco de dados para listar os pedidos feitos, mas deseja aplicar filtros, como listar apenas pedidos de hoje ou de um cliente específico.

_4 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Pergunta
- Como Luana pode usar o Spring Data JPA para fazer consultas específicas no banco de dados sem escrever SQL manualmente?
- Quem sabe responde!

_5 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Luana pode utilizar o Spring Data JPA e criar um repositório específico para a classe Pedido. Com ele, ela consegue filtrar dados diretamente usando métodos personalizados, como findByData ou findByCliente, sem precisar escrever SQL.

_4 imagem(ns) no slide._

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- Spring Data
- Spring Data JPA é uma extensão que facilita o trabalho com banco de dados em aplicações Java. Ele automatiza operações de busca, atualização e remoção de dados, simplificando o uso de repositórios para consultas avançadas.

_4 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- Definição e Aplicação
- Começando com Spring Data JPA: Spring Data JPA permite criar repositórios para manipulação de dados sem a necessidade de escrever SQL, usando métodos intuitivos que representam consultas comuns.

_4 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Definição e Aplicação
- Utilizando Repository: O Repository é a interface que permite criar e organizar consultas de forma simples, como salvar, buscar e deletar dados.
- Consulta com filtros: Com o Spring Data JPA, é possível criar filtros personalizados diretamente nos métodos do repositório, como findByNome, findByData, ou métodos compostos como findByNomeAndData.

_3 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- O Spring Data JPA simplifica o trabalho com banco de dados, essencial em aplicações que manipulam grandes volumes de dados. Ele oferece uma maneira prática de consultar, filtrar e manipular dados, aumentando a produtividade e a clareza do código.

_4 imagem(ns) no slide._

### Slide 13

- DESENVOLVIMENTO DE SISTEMAS
- Em um sistema de reservas, o Spring Data JPA facilita o acesso e a consulta de reservas por data ou cliente. Com o repositório, basta criar métodos como findByDataReserva para recuperar reservas em uma data específica, sem a complexidade do SQL manual.

_4 imagem(ns) no slide._

### Slide 14

- DESENVOLVIMENTO DE SISTEMAS
- Exemplo
- Um exemplo simples de uso do Spring Data JPA para criar uma consulta que busca produtos com um determinado preço mínimo.
- 1- Criando a Entidade Produto

_4 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- Exemplo
- Um exemplo simples de uso do Spring Data JPA para criar uma consulta que busca produtos com um determinado preço mínimo.
- 2- Criando o Repositório ProdutoRepository

_4 imagem(ns) no slide._

### Slide 16

- DESENVOLVIMENTO DE SISTEMAS
- Exemplo
- Nesse exemplo, o método findByPrecoGreaterThan permite listar produtos com preço acima de um valor específico. O Spring Data JPA cuida do SQL, simplificando o código e a consulta.
- 3- Implementando a Consulta

_4 imagem(ns) no slide._

### Slide 17

- DESENVOLVIMENTO DE SISTEMAS
- Questão de fixação
- Qual é a principal função do Spring Data JPA?
- A) Gerar gráficos para relatórios.
- B) Facilitar o trabalho com bancos de dados em Java.
- C) Criar interfaces de usuário interativas.
- D) Fazer backup de dados automaticamente.
- Quem sabe responde!

_4 imagem(ns) no slide._

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- Resposta!
- Qual é a principal função do Spring Data JPA?
- A) Gerar gráficos para relatórios.
- B) Facilitar o trabalho com bancos de dados em Java.
- C) Criar interfaces de usuário interativas.
- D) Fazer backup de dados automaticamente.
- Resposta correta: B)

_3 imagem(ns) no slide._

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- Atividade Prática na Plataforma Alura
- Na plataforma Alura vamos acessar o seguinte curso:
- A recomendação é que você continue esse curso extraclasse, pois ele traz um conteúdo essencial para compreender sobre o referido tema.
- Link para o curso: https://cursos.alura.com.br/course/spring-boot-api-rest

_6 imagem(ns) no slide._

### Slide 20

- DESENVOLVIMENTO DE SISTEMAS
- Começando com Spring Data JPA
- 13 minutos
- Link para tarefa: https://cursos.alura.com.br/course/spring-boot-api-rest/task/55820
- Spring Data JPA simplifica o acesso a bancos de dados em Java, automatizando operações como salvar, buscar e deletar dados. Ele permite criar repositórios com métodos prontos para consultas comuns, sem SQL complexo.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 21

- DESENVOLVIMENTO DE SISTEMAS
- Utilizando Repository
- 8 minutos
- Link para tarefa: https://cursos.alura.com.br/course/spring-boot-api-rest/task/55821
- O Repository no Spring Data JPA é uma interface que facilita o acesso ao banco de dados, oferecendo métodos prontos como salvar, buscar e deletar. Ele permite criar consultas personalizadas de forma simples e eficiente.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 22

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje
- Aprendemos a usar o Spring Data JPA com Spring Boot para facilitar o acesso e manipulação de dados em aplicações Java. Com repositórios e filtros, é possível criar consultas rápidas e eficientes, simplificando o trabalho com banco de dados e mantendo o código limpo e organizado.

_4 imagem(ns) no slide._

### Slide 23

_(sem texto)_

_1 imagem(ns) no slide._

### Slide 24

_(sem texto)_

_1 imagem(ns) no slide._

### Slide 25

- DESENVOLVIMENTO DE SISTEMAS
- Pronto para desbloquear sua carreira de TI?
- Está perdido estudando mas não sabe por onde começar? Se a resposta é sim, você está no lugar certo! Descubra as estratégias e ferramentas essenciais para te ajudar a desbloquear seu potencial em TI e buscar sua primeira vaga de emprego no setor!
- Este e-book é um guia completo para quem busca começar pelos melhores caminhos para se tornar um excelente profissional de TI, ensinando a identificar perfis profissionais, aplicar técnicas de estudo eficazes, transformar teoria em prática, e aumentar a visibilidade de seu trabalho no mercado de trabalho. Ideal para novatos e profissionais em transição.
- E o melhor, ele pode ser seu, inteiramente grátis!
- Basta clicar AQUI e realizar o seu cadastro com o seu @escola!

_5 imagem(ns) no slide._

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

_5 imagem(ns) no slide._

## Outros documentos

_Fonte: AULA 118_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

ATIVIDADE AULA 118

Questão 1

Como o Spring Data JPA facilita a criação de consultas personalizadas?

A) Utilizando SQL direto em cada método.

B) Definindo métodos no Repository com base nos nomes de parâmetros.

C) Criando tabelas automaticamente.

D) Conectando-se a servidores de backup.

Resposta:

Resposta correta: B)

O Spring Data JPA permite criar consultas personalizadas com métodos no Repository, baseados em convenções de nomenclatura, sem necessidade de SQL.

Questão 2

Qual a vantagem de usar filtros em consultas com Spring Data?

A) Reduz o número de tabelas.

B) Aumenta a segurança dos dados.

C) Permite buscar dados específicos facilmente.

D) Remove dados automaticamente.

Resposta:

Resposta correta: C)

Usar filtros facilita a recuperação de dados específicos, permitindo que a aplicação encontre exatamente o que precisa, de forma simples e rápida.
