---
titulo: "Paginação e ordenação de recursos"
tipo: rco-seed
disciplina: programacao-no-desenvolvimento-de-sistemas
sigla_rco: PDS
trimestre: 3
ordem_rco: 122
serie: 3
aula_rco: "Aula 122"
slides: 56
tem_atividade: false
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/3TRI/122-paginacao-e-ordenacao-de-recursos/122-paginacao-e-ordenacao-de-recursos(1).pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/3TRI/122-paginacao-e-ordenacao-de-recursos/122-paginacao-e-ordenacao-de-recursos.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/3TRI/122-paginacao-e-ordenacao-de-recursos/AULA 122_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Paginação e ordenação de recursos

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO NO
- DESENVOLVIMENTO DE
- SISTEMAS
- 3ª SÉRIE
- Paginação e ordenação de recursos
- Aula 122

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
- Vamos aprender como implementar paginação e ordenação em APIs REST usando Spring Boot.

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
- Aprendemos a implementar métodos PUT e DELETE em APIs REST e a tratar erros como o 404. Agora, vamos avançar para organizar grandes volumes de dados com paginação e ordenação.

_4 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Lucas administra uma API para um sistema de biblioteca e precisa listar centenas de livros. Porém, carregar todos os livros de uma vez está prejudicando o desempenho e a segurança da API.

_4 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Pergunta
- Como Lucas pode implementar paginação e ordenação para melhorar a experiência do usuário sem comprometer a segurança da API?
- Quem sabe responde!

_5 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Lucas pode usar o Pageable do Spring Data JPA para dividir os resultados em páginas, enquanto permite ordenação com parâmetros como sort. Para segurança, ele deve validar limites de paginação.

_4 imagem(ns) no slide._

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- Paginação e ordenação permitem dividir e organizar os dados retornados por uma API REST. Esses recursos são essenciais para melhorar o desempenho e a experiência do usuário.

_4 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- Aplicação
- Paginação: Divide grandes conjuntos de dados em partes menores usando parâmetros como page e size.
- Ordenação: Define a ordem dos dados retornados, com base em colunas, usando parâmetros como sort.
- Segurança: Limita o número máximo de registros por página, prevenindo sobrecarga no sistema.

_4 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Paginação e ordenação otimizam a performance e tornam os dados mais acessíveis. Isso é crucial em sistemas que lidam com grandes volumes de informações, como e-commerces ou CRMs.

_4 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- Em uma loja virtual, os produtos são exibidos em páginas, permitindo ao cliente navegar de forma eficiente. Ordenação por preço ou popularidade melhora a experiência do usuário.

_4 imagem(ns) no slide._

### Slide 13

- DESENVOLVIMENTO DE SISTEMAS
- Exemplo
- Implementando Paginação e Ordenação
- Validação de Parâmetros para Segurança

_5 imagem(ns) no slide._

### Slide 14

- DESENVOLVIMENTO DE SISTEMAS
- Exemplo
- Configuração no Repository
- Exemplo de Consulta com Parâmetros no Postman:
- URL: GET /livros?page=0&size=5&sort=titulo,asc

_4 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- Questão de fixação
- Qual é a função da paginação em APIs REST?
- A) Dividir os dados em partes menores para otimizar o desempenho.
- B) Carregar todos os dados de uma só vez.
- C) Proteger a API de acessos não autorizados.
- D) Retornar os dados em ordem aleatória.
- Quem sabe responde!

_4 imagem(ns) no slide._

### Slide 16

- DESENVOLVIMENTO DE SISTEMAS
- Resposta!
- Qual é a função da paginação em APIs REST?
- A) Dividir os dados em partes menores para otimizar o desempenho.
- B) Carregar todos os dados de uma só vez.
- C) Proteger a API de acessos não autorizados.
- D) Retornar os dados em ordem aleatória.
- Resposta: A

_3 imagem(ns) no slide._

### Slide 17

- DESENVOLVIMENTO DE SISTEMAS
- Atividade Prática na Plataforma Alura
- Na plataforma Alura vamos acessar o seguinte curso:
- A recomendação é que você continue esse curso extraclasse, pois ele traz um conteúdo essencial para compreender sobre o referido tema.
- Link para o curso: https://cursos.alura.com.br/course/spring-boot-seguranca-cache-monitoramento

_6 imagem(ns) no slide._

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- Paginação
- 13 minutos
- Link para tarefa: https://cursos.alura.com.br/course/spring-boot-seguranca-cache-monitoramento/task/55834
- Paginação organiza dados em partes menores, melhorando o desempenho e facilitando o consumo de APIs. Usando parâmetros como page e size, ela evita sobrecarga no servidor e melhora a experiência do usuário.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- Ordenação
- 8 minutos
- Link para tarefa: https://cursos.alura.com.br/course/spring-boot-seguranca-cache-monitoramento/task/55835
- A ordenação organiza os dados retornados pela API com base em campos específicos, como nome ou data. Usando o parâmetro sort, facilita a busca de informações relevantes de forma eficiente e estruturada.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 20

- DESENVOLVIMENTO DE SISTEMAS
- Simplificando a paginação e ordenação
- 10 minutos
- Link para tarefa: https://cursos.alura.com.br/course/spring-boot-seguranca-cache-monitoramento/task/55836
- Simplificar paginação e ordenação envolve configurar padrões, como tamanho de página e campo de ordenação, usando @PageableDefault. Isso reduz a necessidade de parâmetros complexos, otimizando o uso da API.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 21

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje
- Exploramos como implementar paginação e ordenação em APIs REST Spring Boot. Aprendemos boas práticas para garantir a segurança e eficiência na manipulação de grandes volumes de dados, otimizando a experiência do usuário.

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

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO NO
- DESENVOLVIMENTO DE
- SISTEMAS
- 3ª SÉRIE
- Paginação e ordenação de recursos
- Aula 122

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
- Vamos aprender como implementar paginação e ordenação em APIs REST usando Spring Boot.

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
- Aprendemos a implementar métodos PUT e DELETE em APIs REST e a tratar erros como o 404. Agora, vamos avançar para organizar grandes volumes de dados com paginação e ordenação.

_4 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Lucas administra uma API para um sistema de biblioteca e precisa listar centenas de livros. Porém, carregar todos os livros de uma vez está prejudicando o desempenho e a segurança da API.

_4 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Pergunta
- Como Lucas pode implementar paginação e ordenação para melhorar a experiência do usuário sem comprometer a segurança da API?
- Quem sabe responde!

_5 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Lucas pode usar o Pageable do Spring Data JPA para dividir os resultados em páginas, enquanto permite ordenação com parâmetros como sort. Para segurança, ele deve validar limites de paginação.

_4 imagem(ns) no slide._

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- Paginação e ordenação permitem dividir e organizar os dados retornados por uma API REST. Esses recursos são essenciais para melhorar o desempenho e a experiência do usuário.

_4 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- Aplicação
- Paginação: Divide grandes conjuntos de dados em partes menores usando parâmetros como page e size.
- Ordenação: Define a ordem dos dados retornados, com base em colunas, usando parâmetros como sort.
- Segurança: Limita o número máximo de registros por página, prevenindo sobrecarga no sistema.

_4 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Paginação e ordenação otimizam a performance e tornam os dados mais acessíveis. Isso é crucial em sistemas que lidam com grandes volumes de informações, como e-commerces ou CRMs.

_4 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- Em uma loja virtual, os produtos são exibidos em páginas, permitindo ao cliente navegar de forma eficiente. Ordenação por preço ou popularidade melhora a experiência do usuário.

_4 imagem(ns) no slide._

### Slide 13

- DESENVOLVIMENTO DE SISTEMAS
- Exemplo
- Implementando Paginação e Ordenação
- Validação de Parâmetros para Segurança

_5 imagem(ns) no slide._

### Slide 14

- DESENVOLVIMENTO DE SISTEMAS
- Exemplo
- Configuração no Repository
- Exemplo de Consulta com Parâmetros no Postman:
- URL: GET /livros?page=0&size=5&sort=titulo,asc

_4 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- Questão de fixação
- Qual é a função da paginação em APIs REST?
- A) Dividir os dados em partes menores para otimizar o desempenho.
- B) Carregar todos os dados de uma só vez.
- C) Proteger a API de acessos não autorizados.
- D) Retornar os dados em ordem aleatória.
- Quem sabe responde!

_4 imagem(ns) no slide._

### Slide 16

- DESENVOLVIMENTO DE SISTEMAS
- Resposta!
- Qual é a função da paginação em APIs REST?
- A) Dividir os dados em partes menores para otimizar o desempenho.
- B) Carregar todos os dados de uma só vez.
- C) Proteger a API de acessos não autorizados.
- D) Retornar os dados em ordem aleatória.
- Resposta: A

_3 imagem(ns) no slide._

### Slide 17

- DESENVOLVIMENTO DE SISTEMAS
- Atividade Prática na Plataforma Alura
- Na plataforma Alura vamos acessar o seguinte curso:
- A recomendação é que você continue esse curso extraclasse, pois ele traz um conteúdo essencial para compreender sobre o referido tema.
- Link para o curso: https://cursos.alura.com.br/course/spring-boot-seguranca-cache-monitoramento

_6 imagem(ns) no slide._

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- Paginação
- 13 minutos
- Link para tarefa: https://cursos.alura.com.br/course/spring-boot-seguranca-cache-monitoramento/task/55834
- Paginação organiza dados em partes menores, melhorando o desempenho e facilitando o consumo de APIs. Usando parâmetros como page e size, ela evita sobrecarga no servidor e melhora a experiência do usuário.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- Ordenação
- 8 minutos
- Link para tarefa: https://cursos.alura.com.br/course/spring-boot-seguranca-cache-monitoramento/task/55835
- A ordenação organiza os dados retornados pela API com base em campos específicos, como nome ou data. Usando o parâmetro sort, facilita a busca de informações relevantes de forma eficiente e estruturada.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 20

- DESENVOLVIMENTO DE SISTEMAS
- Simplificando a paginação e ordenação
- 10 minutos
- Link para tarefa: https://cursos.alura.com.br/course/spring-boot-seguranca-cache-monitoramento/task/55836
- Simplificar paginação e ordenação envolve configurar padrões, como tamanho de página e campo de ordenação, usando @PageableDefault. Isso reduz a necessidade de parâmetros complexos, otimizando o uso da API.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 21

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje
- Exploramos como implementar paginação e ordenação em APIs REST Spring Boot. Aprendemos boas práticas para garantir a segurança e eficiência na manipulação de grandes volumes de dados, otimizando a experiência do usuário.

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

_Fonte: AULA 122_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

ATIVIDADE AULA 122

Questão 1

Qual parâmetro é usado para definir o tamanho da página na paginação?

A) limit

B) size

C) rows

D) per_page

Resposta:

B) O parâmetro size é usado para determinar o número de registros por página.

Questão 2

O que o parâmetro sort faz em uma API REST?

A) Limita o número de páginas.

B) Ordena os resultados com base em uma coluna específica.

C) Divide os dados em páginas menores.

D) Remove registros duplicados.

Resposta:

B) sort organiza os dados em ordem crescente ou decrescente com base em uma coluna especificada.
