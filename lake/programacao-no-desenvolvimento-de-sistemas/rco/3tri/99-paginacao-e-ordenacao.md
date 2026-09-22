---
titulo: "Paginação e Ordenação"
tipo: rco-seed
disciplina: programacao-no-desenvolvimento-de-sistemas
sigla_rco: PDS
trimestre: 3
ordem_rco: 99
serie: 3
aula_rco: "Aula 99"
slides: 24
tem_atividade: false
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/3TRI/99-paginacao-e-ordenacao/99-paginacao-e-ordenacao.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/3TRI/99-paginacao-e-ordenacao/AULA 99_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Paginação e Ordenação

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO NO
- DESENVOLVIMENTO DE
- SISTEMAS
- 3ª SÉRIE
- Paginação e Ordenação
- Aula 99

_3 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- DESENVOLVIMENTO DE SISTEMAS
- Nesta aula, vamos:
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store
- Aprender como usar paginação e ordenação para organizar a exibição de dados em aplicações.

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
- Exploramos consultas derivadas, JPQL e consultas nativas no Spring Data, aprendendo como buscar dados de maneira eficiente e personalizada, utilizando diferentes abordagens de recuperação de informações.

_4 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- O problema é que há centenas de registros, e a interface está lenta e difícil de usar. Ele não sabe como organizar melhor a exibição dos dados.
- Marcos é um desenvolvedor júnior que precisa criar um painel de controle para visualizar dados de clientes.

_4 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Pergunta…
- Como Marcos pode aplicar paginação e ordenação no Spring Data para melhorar a experiência de navegação no painel?
- Quem sabe responde!

_5 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Resposta correta
- Ele deve usar a funcionalidade de paginação (Pageable) para dividir a exibição de registros em várias páginas menores e aplicar ordenação (Sort) para organizar os dados em uma sequência específica, como por nome ou data.

_4 imagem(ns) no slide._

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- Paginação
- Paginação e ordenação são técnicas usadas para controlar como os dados são exibidos em aplicações, dividindo grandes volumes de informações em partes menores e organizando-os de maneira lógica.

_4 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- Paginação
- Técnica para dividir a exibição de dados em múltiplas páginas, facilitando a navegação e carregamento de registros grandes.
- Ordenação
- Definição de critérios que determinam a sequência de exibição dos dados (por exemplo, ordem alfabética ou por data).

_4 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Importância
- Essas técnicas são essenciais em projetos reais para evitar sobrecarga de dados e garantir uma navegação mais fluida e eficiente, melhorando a experiência do usuário e a performance do sistema.

_4 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- Uso
- Exemplo: Em uma loja online, é comum ver resultados de pesquisa organizados por preço (ordenação) e exibidos em várias páginas com 10 ou 20 itens por vez (paginação).

_4 imagem(ns) no slide._

### Slide 13

- DESENVOLVIMENTO DE SISTEMAS
- Exemplo
- Neste exemplo, a consulta retornará a primeira página de clientes que contêm o nome "Silva" e os ordenará por idade, com um limite de 5 registros por página.

_4 imagem(ns) no slide._

### Slide 14

- DESENVOLVIMENTO DE SISTEMAS
- Questão de fixação
- Qual é o objetivo principal de aplicar paginação em uma aplicação?
- A) Diminuir o tamanho do banco de dados.
- B) Facilitar a navegação em grandes volumes de dados.
- C) Aumentar a segurança das informações.
- D) Melhorar a estética da interface.
- Quem sabe responde!

_4 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- Resposta!
- Qual é o objetivo principal de aplicar paginação em uma aplicação?
- A) Diminuir o tamanho do banco de dados.
- B) Facilitar a navegação em grandes volumes de dados.
- C) Aumentar a segurança das informações.
- D) Melhorar a estética da interface.
- Resposta correta: B)

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
- Paginação
- 14 minutos
- Link para tarefa: https://cursos.alura.com.br/course/spring-data-jpa/task/83427
- Paginação é a técnica que divide a exibição de grandes volumes de dados em páginas menores, facilitando a navegação e evitando sobrecarga de informações, melhorando a performance e a experiência do usuário.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- Tipos de repositórios
- 4 minutos
- Link para tarefa: https://cursos.alura.com.br/course/spring-data-jpa/task/83428
- Os tipos de repositórios no Spring Data incluem CrudRepository (operações básicas), JpaRepository (recursos avançados como paginação) e PagingAndSortingRepository (focado em paginação e ordenação).
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- Ordenação
- 7 minutos
- Link para tarefa: https://cursos.alura.com.br/course/spring-data-jpa/task/83429
- Ordenação é a técnica que organiza a exibição de dados com base em critérios definidos, como nome, data ou preço. Ela facilita a leitura, destacando informações importantes e tornando a análise mais intuitiva.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 20

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje
- Aprendemos como implementar paginação e ordenação no Spring Data para organizar e exibir informações de maneira eficiente.

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

_Fonte: AULA 99_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

ATIVIDADE AULA 99

Questão 1

Quando é mais indicado usar ordenação em uma consulta?

A) Quando os dados são atualizados constantemente.

B) Quando é necessário exibir informações em uma sequência específica.

C) Quando não se deseja exibir todos os registros.

D) Quando o banco de dados está em modo offline.

Resposta:

Resposta correta: B)

A ordenação organiza a sequência de exibição dos registros, facilitando a compreensão e análise dos dados.

Questão 2

Qual é a melhor abordagem para exibir um grande volume de registros sem afetar a performance?

A) Criar um arquivo separado para cada consulta.

B) Exibir todos os registros de uma vez.

C) Usar paginação para dividir os registros em várias partes.

D) Remover registros para reduzir o volume.

Resposta:

Resposta correta: C)

A paginação divide os dados em páginas menores, permitindo carregamento gradual e melhorando a performance.
