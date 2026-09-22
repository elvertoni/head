---
titulo: "Integração com Spring Data"
tipo: rco-seed
disciplina: programacao-no-desenvolvimento-de-sistemas
sigla_rco: PDS
trimestre: 3
ordem_rco: 104
serie: 3
aula_rco: "Aula 104"
slides: 25
tem_atividade: false
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/3TRI/104-integracao-com-spring-data/104-integracao-com-spring-data.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/3TRI/104-integracao-com-spring-data/AULA 104_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Integração com Spring Data

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO NO
- DESENVOLVIMENTO DE
- SISTEMAS
- 3ª SÉRIE
- Integração com Spring Data
- Aula 104

_3 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- DESENVOLVIMENTO DE SISTEMAS
- Nesta aula, vamos:
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store
- Integrar o Spring Data em suas aplicações, utilizando JPA puro, injeção de dependências e o poder do Spring Data.

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
- Exploramos como usar Thymeleaf e Bootstrap para criar interfaces dinâmicas e responsivas em aplicações Spring MVC. Agora, vamos integrar essas interfaces com os dados armazenados no banco de dados, facilitando a manipulação e apresentação dos dados com Spring Data.

_4 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Julia está criando uma aplicação de cadastro de clientes e precisa armazenar, consultar e atualizar esses dados em um banco de dados.
- Ela tem dúvidas sobre a melhor forma de integrar sua aplicação ao banco.
- Julia deve escolher entre usar JPA puro ou aproveitar a facilidade do Spring Data JPA…

_5 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Existem 2 opções para ela…
- Usar Spring Data JPA com injeção de dependências: Julia pode usar Spring Data JPA, que já fornece repositórios prontos para facilitar operações como salvar, buscar e deletar dados, com pouca necessidade de código manual.
- Usar JPA puro sem Spring Data: Julia poderia usar JPA manualmente, mas precisaria escrever muito mais código para implementar funcionalidades que o Spring Data já oferece prontas.
- Quem sabe responde!

_6 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Resposta correta
- Spring Data JPA com injeção de dependências é a escolha mais eficiente, pois reduz a quantidade de código, automatiza tarefas comuns e oferece flexibilidade para consultas mais avançadas.
- Usar JPA puro pode funcionar, mas exige mais código manual para implementar funcionalidades que o Spring Data já oferece automaticamente, tornando o desenvolvimento mais lento e propenso a erros.

_4 imagem(ns) no slide._

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- A integração com Spring Data JPA permite que as aplicações interajam de forma eficiente com bancos de dados, abstraindo operações comuns como salvar, buscar e atualizar dados, facilitando o desenvolvimento de sistemas robustos e escaláveis.

_4 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- Injeção de dependências
- É uma técnica do Spring para automatizar a criação e o gerenciamento de objetos, como repositórios, facilitando a interação entre a aplicação e o banco de dados.
- Usando JPA puro
- O JPA (Java Persistence API) é uma especificação que define como gerenciar dados relacionais em Java, permitindo que desenvolvedores escrevam consultas e transações para bancos de dados.

_4 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Usando Spring Data JPA:
- Spring Data JPA simplifica ainda mais o JPA, fornecendo repositórios prontos que eliminam a necessidade de escrever consultas SQL manuais para operações básicas de banco de dados.

_6 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- A integração com o banco de dados é uma parte essencial de muitas aplicações web.
- Usar Spring Data JPA reduz significativamente o tempo de desenvolvimento, aumenta a produtividade e facilita a manutenção do código.

_4 imagem(ns) no slide._

### Slide 13

- DESENVOLVIMENTO DE SISTEMAS
- Na prática
- Em uma aplicação de cadastro de clientes, Spring Data JPA permite que você use métodos prontos como save(), findById(), e delete() para gerenciar clientes sem precisar escrever SQL manualmente.

_4 imagem(ns) no slide._

### Slide 14

- DESENVOLVIMENTO DE SISTEMAS
- Exemplo
- Exemplo básico de como usar Spring Data JPA em uma aplicação.

_4 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- Questão de fixação
- Qual é a principal vantagem de usar Spring Data JPA em vez de JPA puro?
- A) Exige mais código para configurar.
- B) Facilita as operações de banco de dados, eliminando consultas SQL manuais para funções básicas.
- C) Não suporta consultas personalizadas.
- D) Substitui o JPA completamente.
- Quem sabe responde!

_4 imagem(ns) no slide._

### Slide 16

- DESENVOLVIMENTO DE SISTEMAS
- Resposta!
- Qual é a principal vantagem de usar Spring Data JPA em vez de JPA puro?
- A) Exige mais código para configurar.
- B) Facilita as operações de banco de dados, eliminando consultas SQL manuais para funções básicas.
- C) Não suporta consultas personalizadas.
- D) Substitui o JPA completamente.
- Resposta correta: B

_3 imagem(ns) no slide._

### Slide 17

- DESENVOLVIMENTO DE SISTEMAS
- Atividade Prática na Plataforma Alura
- Na plataforma Alura vamos acessar o seguinte curso:
- A recomendação é que você continue esse curso extraclasse, pois ele traz um conteúdo essencial para compreender sobre o referido tema.
- Link para o curso: https://cursos.alura.com.br/course/spring-mvc-thymeleaf-bootstrap

_6 imagem(ns) no slide._

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- Usando JPA puro
- 9 minutos
- Link para tarefa: https://cursos.alura.com.br/course/spring-mvc-thymeleaf-bootstrap/task/80871
- Usar JPA puro envolve escrever manualmente as operações de persistência, como consultas e transações. Embora ofereça flexibilidade, exige mais código para funções básicas como salvar, buscar e atualizar dados.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- Injeção de dependências
- 11 minutos
- Link para tarefa: https://cursos.alura.com.br/course/spring-mvc-thymeleaf-bootstrap/task/80872
- Injeção de dependências é uma técnica usada no Spring para automatizar a criação e gerenciamento de objetos, permitindo que o framework injete componentes necessários nas classes, simplificando o desenvolvimento.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 20

- DESENVOLVIMENTO DE SISTEMAS
- Usando Spring Data JPA
- 6 minutos
- Link para tarefa: https://cursos.alura.com.br/course/spring-mvc-thymeleaf-bootstrap/task/80873
- Spring Data JPA simplifica o acesso ao banco de dados, fornecendo repositórios prontos para operações como salvar, buscar e deletar. Ele elimina a necessidade de escrever consultas SQL manuais para funções básicas.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 21

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje
- Aprendemos a integrar uma aplicação com o banco de dados usando JPA e Spring Data JPA. Com essa integração, conseguimos realizar operações com os dados de forma simplificada e eficiente, automatizando tarefas que normalmente demandam mais tempo e código, e garantindo uma conexão perfeita entre a lógica da aplicação e a manipulação de dados.

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

_Fonte: AULA 104_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

ATIVIDADE AULA 104

Questão 1

Qual é o papel do repositório no Spring Data JPA?

A) Definir a lógica de apresentação da aplicação.

B) Criar interfaces gráficas para o usuário.

C) Executar operações de banco de dados, como salvar, buscar e deletar registros.

D) Armazenar arquivos de configuração.

Resposta:

Resposta correta: C)

O repositório no Spring Data JPA é responsável por realizar operações com o banco de dados, como salvar, buscar e deletar registros.

Questão 2

Qual classe você usaria para definir uma entidade no Spring Data JPA?

A) @Repository

B) @Entity

C) @Service

D) @Component

Resposta:

Resposta correta: B)

A anotação @Entity é usada para definir uma classe como uma entidade que será mapeada para uma tabela no banco de dados.
