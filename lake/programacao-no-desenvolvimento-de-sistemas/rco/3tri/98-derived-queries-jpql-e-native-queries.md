---
titulo: "Derived Queries, JPQL e Native Queries"
tipo: rco-seed
disciplina: programacao-no-desenvolvimento-de-sistemas
sigla_rco: PDS
trimestre: 3
ordem_rco: 98
serie: 3
aula_rco: "Aula 98"
slides: 24
tem_atividade: false
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/3TRI/98-derived-queries-jpql-e-native-queries/98-derived-queries-jpql-e-native-queries.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/3TRI/98-derived-queries-jpql-e-native-queries/AULA 98_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Derived Queries, JPQL e Native Queries

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO NO
- DESENVOLVIMENTO DE
- SISTEMAS
- 3ª SÉRIE
- Derived Queries, JPQL e Native Queries
- Aula 98

_3 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- DESENVOLVIMENTO DE SISTEMAS
- Nesta aula, vamos:
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store
- Explorar como criar diferentes tipos de consultas em projetos Spring Data.

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
- Na última aula, aprendemos sobre as operações CRUD (Create, Read, Update e Delete) usando Spring Data, entendendo como manipular informações no banco de dados por meio de métodos padrão de repositório.

_4 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Laura é uma desenvolvedora que precisa criar um relatório customizado para seu gerente, mas o método padrão findAll() não permite filtrar os dados conforme necessário. Ela tenta criar uma Derived Query, mas não consegue incluir filtros complexos. Laura está confusa sobre quando usar JPQL ou uma consulta nativa.

_4 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Pergunta
- Quando é mais apropriado usar uma consulta derivada, JPQL ou uma consulta nativa para recuperar dados no Spring Data?
- Quem sabe responde!

_5 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Derived Queries são úteis para consultas simples baseadas na convenção de nomes dos métodos.
- JPQL permite personalizar consultas com sintaxe orientada a objetos e trabalhar com relacionamentos.
- Native Queries são recomendadas quando você precisa de consultas complexas ou específicas de um banco de dados.

_4 imagem(ns) no slide._

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- JPQL
- Consultas derivadas, JPQL e consultas nativas são maneiras de buscar informações personalizadas no banco de dados usando Spring Data. Cada uma tem uma finalidade específica e, juntas, ajudam a otimizar o acesso a dados.

_4 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- Definição e Aplicação
- Derived Queries: Criadas automaticamente com base no nome do método (ex.: findByNome), facilitando consultas básicas.
- JPQL (Java Persistence Query Language): Uma versão orientada a objetos do SQL que permite consultas mais sofisticadas, utilizando a linguagem específica do JPA.

_4 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Definição e Aplicação
- Native Queries: Usam a sintaxe SQL diretamente e são úteis quando JPQL não atende às necessidades específicas.

_4 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- Abordagem
- Escolher a abordagem correta para consultas no Spring Data permite que desenvolvedores escrevam código mais eficiente e personalizável, aumentando a produtividade e reduzindo erros na manipulação de dados.

_4 imagem(ns) no slide._

### Slide 13

- DESENVOLVIMENTO DE SISTEMAS
- Uso
- Derived Queries para consultas simples: Exemplo, findById.
- JPQL para juntar informações de múltiplas tabelas.
- Native Queries para executar funções complexas ou específicas do banco, como GROUP BY e HAVING.

_4 imagem(ns) no slide._

### Slide 14

- DESENVOLVIMENTO DE SISTEMAS
- Questão de fixação
- Qual é a principal vantagem das Derived Queries no Spring Data?
- A) São mais fáceis de ler e escrever.
- B) Oferecem consultas complexas com poucas linhas de código.
- C) Suportam cálculos matemáticos avançados.
- D) Não possuem suporte a JPQL.
- Quem sabe responde!

_4 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- Resposta!
- Qual é a principal vantagem das Derived Queries no Spring Data?
- A) São mais fáceis de ler e escrever.
- B) Oferecem consultas complexas com poucas linhas de código.
- C) Suportam cálculos matemáticos avançados.
- D) Não possuem suporte a JPQL.
- Resposta correta: A)

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
- Derived Query
- 14 minutos
- Link para tarefa: https://cursos.alura.com.br/course/spring-data-jpa/task/83436
- Derived Query é um tipo de consulta no Spring Data criada com base no nome do método. Permite filtrar e recuperar dados de forma automática, seguindo convenções de nomenclatura, sem precisar escrever SQL.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- Usando JPQL
- 8 minutos
- Link para tarefa: https://cursos.alura.com.br/course/spring-data-jpa/task/83437
- JPQL é uma linguagem de consulta para JPA que usa sintaxe orientada a objetos para buscar dados de entidades. Permite criar consultas mais flexíveis e complexas, como junções e filtros, usando nomes de atributos.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- Native Query
- 9 minutos
- Link para tarefa: https://cursos.alura.com.br/course/spring-data-jpa/task/83439
- Native Query permite executar consultas SQL diretamente no banco de dados, ignorando abstrações do JPA. É ideal para operações complexas, específicas do banco ou quando o JPQL não atende às necessidades.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 20

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje
- Exploramos hoje como usar consultas derivadas, JPQL e consultas nativas para recuperar dados no Spring Data. Vimos exemplos práticos e discutimos os melhores cenários para cada abordagem, dando continuidade ao tema CRUD da aula anterior.

_4 imagem(ns) no slide._

### Slide 21

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

### Slide 22

- DESENVOLVIMENTO DE SISTEMAS
- Referências (Imagens)
- Figuras e Imagens:
- https://www.flaticon.com/br
- https://www.istockphoto.com/br
- https://raw.githubusercontent.com/zbtang/React-Native-ViewPager/HEAD/imgs/dotIndicator.gif
- https://storyset.com

_3 imagem(ns) no slide._

### Slide 23

- DESENVOLVIMENTO DE SISTEMAS
- O RCO+Aulas é um projeto da Secretaria de Estado da Educação do Paraná e está em constante revisão. Todos os slides são de uso exclusivo dos professores da Rede Pública de Ensino, com a finalidade específica de aplicação em sala de aula, sendo totalmente vedada a publicização, reutilização, reprodução total ou parcial para quaisquer outros fins.

_4 imagem(ns) no slide._

### Slide 24

- DESENVOLVIMENTO DE SISTEMAS
- Esta publicação tem a cooperação entre a UNESCO e a Secretaria de Estado da Educação e do Esporte do Paraná no âmbito da parceria PRODOC 914BRZ1091, cujo objetivo é trazer soluções inovadoras de gestão da rede pública estadual de educação do Paraná para a melhoria da aprendizagem dos alunos. As indicações de nomes e a apresentação do material ao longo desta publicação não implicam a manifestação de qualquer opinião por parte da UNESCO a respeito da condição jurídica de qualquer país, território, cidade, região ou de suas autoridades, tampouco da delimitação de suas fronteiras ou limites As ideias e opiniões expressas nesta publicação são as dos autores e não refletem obrigatoriamente as da UNESCO nem comprometem a Organização.
- Cooperação Técnica

_4 imagem(ns) no slide._

## Outros documentos

_Fonte: AULA 98_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

ATIVIDADE AULA 98

Questão 1

O que a anotação @Query faz no Spring Data?

A) Define um filtro para entidades mapeadas.

B) Permite a execução de consultas personalizadas.

C) Configura o cache de entidades.

D) Automatiza a geração de identificadores únicos.

Resposta:

Resposta correta: B)

A anotação @Query é usada para definir consultas JPQL ou SQL nativas, personalizando a recuperação de dados.

Questão 2

Qual é a sintaxe básica para criar uma consulta JPQL?

A) SELECT * FROM Tabela

B) INSERT INTO Tabela VALUES (...)

C) SELECT entidade FROM Classe entidade

D) DELETE FROM Tabela WHERE ...

Resposta:

Resposta correta: C)

A sintaxe JPQL é orientada a objetos e utiliza classes e atributos em vez de tabelas e colunas diretamente.
