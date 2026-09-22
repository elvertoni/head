---
titulo: "Métodos PUT, DELETE e tratamento de erro"
tipo: rco-seed
disciplina: programacao-no-desenvolvimento-de-sistemas
sigla_rco: PDS
trimestre: 3
ordem_rco: 121
serie: 3
aula_rco: "Aula 121"
slides: 60
tem_atividade: false
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/3TRI/121-metodos-put-delete-e-tratamento-de-erro/121-metodos-put-delete-e-tratamento-de-erro(1).pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/3TRI/121-metodos-put-delete-e-tratamento-de-erro/121-metodos-put-delete-e-tratamento-de-erro.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/3TRI/121-metodos-put-delete-e-tratamento-de-erro/AULA 121_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Métodos PUT, DELETE e tratamento de erro

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO NO
- DESENVOLVIMENTO DE
- SISTEMAS
- 3ª SÉRIE
- Métodos PUT, DELETE e tratamento de erro
- Aula 121

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
- Aprender a atualizar e remover dados em APIs REST usando os métodos PUT e DELETE.

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
- Aprendemos a validar dados recebidos em APIs REST com Bean Validation. Agora, avançaremos para métodos que permitem atualizar, deletar e tratar erros no uso de endpoints.

_4 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Clara está desenvolvendo uma API de gerenciamento de biblioteca. Ela precisa permitir que os usuários atualizem informações dos livros e removam registros, garantindo mensagens claras em casos de erro.

_4 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Pergunta
- Como Clara pode implementar os métodos PUT e DELETE e tratar o erro 404 para melhorar a experiência dos usuários e a segurança da API?
- Quem sabe responde!

_5 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Clara pode criar endpoints PUT para atualizar os livros e DELETE para removê-los. Além disso, ao usar tratamento de erros com @ExceptionHandler, ela pode retornar mensagens claras para o erro 404.

_4 imagem(ns) no slide._

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- Os métodos PUT e DELETE são usados em APIs REST para atualizar e excluir recursos. O tratamento de erros é essencial para lidar com situações como dados não encontrados, melhorando a experiência do usuário.

_4 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- Definição
- Método PUT: Usado para atualizar recursos existentes, enviando os dados no corpo da requisição.
- Método DELETE: Usado para remover recursos do banco de dados.
- Tratamento de Erros: O erro 404 é retornado quando um recurso não é encontrado. Tratar esse erro é essencial para APIs mais claras e seguras.

_4 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- A capacidade de atualizar e remover dados é fundamental em sistemas dinâmicos, como e-commerces ou CRMs. Tratar erros evita frustrações do usuário e possíveis vulnerabilidades.

_4 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- Em um sistema de loja virtual, o método PUT permite atualizar informações de um produto, enquanto DELETE remove itens indisponíveis. O tratamento de erros garante respostas claras em caso de falhas.

_4 imagem(ns) no slide._

### Slide 13

- DESENVOLVIMENTO DE SISTEMAS
- Exemplo
- Criando o Endpoint PUT para Atualizar Recursos

_4 imagem(ns) no slide._

### Slide 14

- DESENVOLVIMENTO DE SISTEMAS
- Exemplo
- Criando o Endpoint DELETE para Remover Recursos

_4 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- Exemplo
- Tratando o Erro 404 com @ExceptionHandler

_4 imagem(ns) no slide._

### Slide 16

- DESENVOLVIMENTO DE SISTEMAS
- Questão de fixação
- Qual é a principal função do método PUT em uma API REST?
- A) Excluir recursos existentes.
- B) Atualizar recursos existentes.
- C) Criar novos recursos.
- D) Tratar erros 404.
- Quem sabe responde!

_4 imagem(ns) no slide._

### Slide 17

- DESENVOLVIMENTO DE SISTEMAS
- Resposta!
- Qual é a principal função do método PUT em uma API REST?
- A) Excluir recursos existentes.
- B) Atualizar recursos existentes.
- C) Criar novos recursos.
- D) Tratar erros 404.
- Resposta correta: B)

_3 imagem(ns) no slide._

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- Atividade Prática na Plataforma Alura
- Na plataforma Alura vamos acessar o seguinte curso:
- A recomendação é que você continue esse curso extraclasse, pois ele traz um conteúdo essencial para compreender sobre o referido tema.
- Link para o curso: https://cursos.alura.com.br/course/spring-boot-api-rest

_6 imagem(ns) no slide._

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- Detalhando tópicos
- 15 minutos
- Link para tarefa: https://cursos.alura.com.br/course/spring-boot-api-rest/task/55828
- Detalhar tópicos envolve criar endpoints GET para buscar informações específicas no banco de dados, retornando detalhes claros e precisos sobre um recurso com base no seu identificador único (ID).
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 20

- DESENVOLVIMENTO DE SISTEMAS
- Atualizando tópicos
- 14 minutos
- Link para tarefa: https://cursos.alura.com.br/course/spring-boot-api-rest/task/55829
- Atualizar tópicos requer um endpoint PUT que recebe os dados atualizados no corpo da requisição, valida as informações e altera o recurso correspondente no banco de dados de forma segura e eficiente.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 21

- DESENVOLVIMENTO DE SISTEMAS
- Removendo tópicos
- 6 minutos
- Link para tarefa: https://cursos.alura.com.br/course/spring-boot-api-rest/task/55830
- Remover tópicos utiliza o método DELETE, permitindo excluir recursos específicos com base no ID. É importante validar a existência do recurso antes de deletar para evitar erros e garantir a integridade da API.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 22

- DESENVOLVIMENTO DE SISTEMAS
- Tratando o erro 404
- 9 minutos
- Link para tarefa: https://cursos.alura.com.br/course/spring-boot-api-rest/task/55831
- Tratar o erro 404 é essencial para APIs REST. Indica que o recurso solicitado não foi encontrado. Usando @ExceptionHandler, podemos retornar mensagens claras, melhorando a experiência do usuário e a segurança.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 23

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje
- Aprendemos a implementar métodos PUT e DELETE para atualizar e remover recursos em APIs REST Spring Boot. Exploramos também como tratar erros 404, garantindo mensagens claras e respostas precisas para os usuários, contribuindo para uma experiência eficiente e confiável.

_4 imagem(ns) no slide._

### Slide 24

_(sem texto)_

_1 imagem(ns) no slide._

### Slide 25

_(sem texto)_

_1 imagem(ns) no slide._

### Slide 26

- DESENVOLVIMENTO DE SISTEMAS
- Pronto para desbloquear sua carreira de TI?
- Está perdido estudando mas não sabe por onde começar? Se a resposta é sim, você está no lugar certo! Descubra as estratégias e ferramentas essenciais para te ajudar a desbloquear seu potencial em TI e buscar sua primeira vaga de emprego no setor!
- Este e-book é um guia completo para quem busca começar pelos melhores caminhos para se tornar um excelente profissional de TI, ensinando a identificar perfis profissionais, aplicar técnicas de estudo eficazes, transformar teoria em prática, e aumentar a visibilidade de seu trabalho no mercado de trabalho. Ideal para novatos e profissionais em transição.
- E o melhor, ele pode ser seu, inteiramente grátis!
- Basta clicar AQUI e realizar o seu cadastro com o seu @escola!

_5 imagem(ns) no slide._

### Slide 27

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

### Slide 28

- DESENVOLVIMENTO DE SISTEMAS
- Referências (Imagens)
- Figuras e Imagens:
- https://www.flaticon.com/br
- https://www.istockphoto.com/br
- https://raw.githubusercontent.com/zbtang/React-Native-ViewPager/HEAD/imgs/dotIndicator.gif
- https://storyset.com

_3 imagem(ns) no slide._

### Slide 29

- DESENVOLVIMENTO DE SISTEMAS
- O RCO+Aulas é um projeto da Secretaria de Estado da Educação do Paraná e está em constante revisão. Todos os slides são de uso exclusivo dos professores da Rede Pública de Ensino, com a finalidade específica de aplicação em sala de aula, sendo totalmente vedada a publicização, reutilização, reprodução total ou parcial para quaisquer outros fins.

_4 imagem(ns) no slide._

### Slide 30

- DESENVOLVIMENTO DE SISTEMAS
- Esta publicação tem a cooperação entre a UNESCO e a Secretaria de Estado da Educação e do Esporte do Paraná no âmbito da parceria PRODOC 914BRZ1091, cujo objetivo é trazer soluções inovadoras de gestão da rede pública estadual de educação do Paraná para a melhoria da aprendizagem dos alunos. As indicações de nomes e a apresentação do material ao longo desta publicação não implicam a manifestação de qualquer opinião por parte da UNESCO a respeito da condição jurídica de qualquer país, território, cidade, região ou de suas autoridades, tampouco da delimitação de suas fronteiras ou limites As ideias e opiniões expressas nesta publicação são as dos autores e não refletem obrigatoriamente as da UNESCO nem comprometem a Organização.
- Cooperação Técnica

_5 imagem(ns) no slide._

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO NO
- DESENVOLVIMENTO DE
- SISTEMAS
- 3ª SÉRIE
- Métodos PUT, DELETE e tratamento de erro
- Aula 121

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
- Aprender a atualizar e remover dados em APIs REST usando os métodos PUT e DELETE.

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
- Aprendemos a validar dados recebidos em APIs REST com Bean Validation. Agora, avançaremos para métodos que permitem atualizar, deletar e tratar erros no uso de endpoints.

_4 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Clara está desenvolvendo uma API de gerenciamento de biblioteca. Ela precisa permitir que os usuários atualizem informações dos livros e removam registros, garantindo mensagens claras em casos de erro.

_4 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Pergunta
- Como Clara pode implementar os métodos PUT e DELETE e tratar o erro 404 para melhorar a experiência dos usuários e a segurança da API?
- Quem sabe responde!

_5 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Clara pode criar endpoints PUT para atualizar os livros e DELETE para removê-los. Além disso, ao usar tratamento de erros com @ExceptionHandler, ela pode retornar mensagens claras para o erro 404.

_4 imagem(ns) no slide._

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- Os métodos PUT e DELETE são usados em APIs REST para atualizar e excluir recursos. O tratamento de erros é essencial para lidar com situações como dados não encontrados, melhorando a experiência do usuário.

_4 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- Definição
- Método PUT: Usado para atualizar recursos existentes, enviando os dados no corpo da requisição.
- Método DELETE: Usado para remover recursos do banco de dados.
- Tratamento de Erros: O erro 404 é retornado quando um recurso não é encontrado. Tratar esse erro é essencial para APIs mais claras e seguras.

_4 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- A capacidade de atualizar e remover dados é fundamental em sistemas dinâmicos, como e-commerces ou CRMs. Tratar erros evita frustrações do usuário e possíveis vulnerabilidades.

_4 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- Em um sistema de loja virtual, o método PUT permite atualizar informações de um produto, enquanto DELETE remove itens indisponíveis. O tratamento de erros garante respostas claras em caso de falhas.

_4 imagem(ns) no slide._

### Slide 13

- DESENVOLVIMENTO DE SISTEMAS
- Exemplo
- Criando o Endpoint PUT para Atualizar Recursos

_4 imagem(ns) no slide._

### Slide 14

- DESENVOLVIMENTO DE SISTEMAS
- Exemplo
- Criando o Endpoint DELETE para Remover Recursos

_4 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- Exemplo
- Tratando o Erro 404 com @ExceptionHandler

_4 imagem(ns) no slide._

### Slide 16

- DESENVOLVIMENTO DE SISTEMAS
- Questão de fixação
- Qual é a principal função do método PUT em uma API REST?
- A) Excluir recursos existentes.
- B) Atualizar recursos existentes.
- C) Criar novos recursos.
- D) Tratar erros 404.
- Quem sabe responde!

_4 imagem(ns) no slide._

### Slide 17

- DESENVOLVIMENTO DE SISTEMAS
- Resposta!
- Qual é a principal função do método PUT em uma API REST?
- A) Excluir recursos existentes.
- B) Atualizar recursos existentes.
- C) Criar novos recursos.
- D) Tratar erros 404.
- Resposta correta: B)

_3 imagem(ns) no slide._

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- Atividade Prática na Plataforma Alura
- Na plataforma Alura vamos acessar o seguinte curso:
- A recomendação é que você continue esse curso extraclasse, pois ele traz um conteúdo essencial para compreender sobre o referido tema.
- Link para o curso: https://cursos.alura.com.br/course/spring-boot-api-rest

_6 imagem(ns) no slide._

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- Detalhando tópicos
- 15 minutos
- Link para tarefa: https://cursos.alura.com.br/course/spring-boot-api-rest/task/55828
- Detalhar tópicos envolve criar endpoints GET para buscar informações específicas no banco de dados, retornando detalhes claros e precisos sobre um recurso com base no seu identificador único (ID).
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 20

- DESENVOLVIMENTO DE SISTEMAS
- Atualizando tópicos
- 14 minutos
- Link para tarefa: https://cursos.alura.com.br/course/spring-boot-api-rest/task/55829
- Atualizar tópicos requer um endpoint PUT que recebe os dados atualizados no corpo da requisição, valida as informações e altera o recurso correspondente no banco de dados de forma segura e eficiente.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 21

- DESENVOLVIMENTO DE SISTEMAS
- Removendo tópicos
- 6 minutos
- Link para tarefa: https://cursos.alura.com.br/course/spring-boot-api-rest/task/55830
- Remover tópicos utiliza o método DELETE, permitindo excluir recursos específicos com base no ID. É importante validar a existência do recurso antes de deletar para evitar erros e garantir a integridade da API.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 22

- DESENVOLVIMENTO DE SISTEMAS
- Tratando o erro 404
- 9 minutos
- Link para tarefa: https://cursos.alura.com.br/course/spring-boot-api-rest/task/55831
- Tratar o erro 404 é essencial para APIs REST. Indica que o recurso solicitado não foi encontrado. Usando @ExceptionHandler, podemos retornar mensagens claras, melhorando a experiência do usuário e a segurança.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 23

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje
- Aprendemos a implementar métodos PUT e DELETE para atualizar e remover recursos em APIs REST Spring Boot. Exploramos também como tratar erros 404, garantindo mensagens claras e respostas precisas para os usuários, contribuindo para uma experiência eficiente e confiável.

_4 imagem(ns) no slide._

### Slide 24

_(sem texto)_

_1 imagem(ns) no slide._

### Slide 25

_(sem texto)_

_1 imagem(ns) no slide._

### Slide 26

- DESENVOLVIMENTO DE SISTEMAS
- Pronto para desbloquear sua carreira de TI?
- Está perdido estudando mas não sabe por onde começar? Se a resposta é sim, você está no lugar certo! Descubra as estratégias e ferramentas essenciais para te ajudar a desbloquear seu potencial em TI e buscar sua primeira vaga de emprego no setor!
- Este e-book é um guia completo para quem busca começar pelos melhores caminhos para se tornar um excelente profissional de TI, ensinando a identificar perfis profissionais, aplicar técnicas de estudo eficazes, transformar teoria em prática, e aumentar a visibilidade de seu trabalho no mercado de trabalho. Ideal para novatos e profissionais em transição.
- E o melhor, ele pode ser seu, inteiramente grátis!
- Basta clicar AQUI e realizar o seu cadastro com o seu @escola!

_5 imagem(ns) no slide._

### Slide 27

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

### Slide 28

- DESENVOLVIMENTO DE SISTEMAS
- Referências (Imagens)
- Figuras e Imagens:
- https://www.flaticon.com/br
- https://www.istockphoto.com/br
- https://raw.githubusercontent.com/zbtang/React-Native-ViewPager/HEAD/imgs/dotIndicator.gif
- https://storyset.com

_3 imagem(ns) no slide._

### Slide 29

- DESENVOLVIMENTO DE SISTEMAS
- O RCO+Aulas é um projeto da Secretaria de Estado da Educação do Paraná e está em constante revisão. Todos os slides são de uso exclusivo dos professores da Rede Pública de Ensino, com a finalidade específica de aplicação em sala de aula, sendo totalmente vedada a publicização, reutilização, reprodução total ou parcial para quaisquer outros fins.

_4 imagem(ns) no slide._

### Slide 30

- DESENVOLVIMENTO DE SISTEMAS
- Esta publicação tem a cooperação entre a UNESCO e a Secretaria de Estado da Educação e do Esporte do Paraná no âmbito da parceria PRODOC 914BRZ1091, cujo objetivo é trazer soluções inovadoras de gestão da rede pública estadual de educação do Paraná para a melhoria da aprendizagem dos alunos. As indicações de nomes e a apresentação do material ao longo desta publicação não implicam a manifestação de qualquer opinião por parte da UNESCO a respeito da condição jurídica de qualquer país, território, cidade, região ou de suas autoridades, tampouco da delimitação de suas fronteiras ou limites As ideias e opiniões expressas nesta publicação são as dos autores e não refletem obrigatoriamente as da UNESCO nem comprometem a Organização.
- Cooperação Técnica

_5 imagem(ns) no slide._

## Outros documentos

_Fonte: AULA 121_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

ATIVIDADE AULA 121

Questão 1

Qual código de status HTTP é retornado ao excluir um recurso com sucesso?

A) 200 OK

B) 201 Created

C) 204 No Content

D) 404 Not Found

Resposta:

Resposta correta: C)

O código 204 indica que a operação foi bem-sucedida, mas não há conteúdo a ser retornado.

Questão 2

O que acontece se um recurso não for encontrado em um endpoint DELETE?

A) O recurso é criado.

B) É retornado o código 404.

C) O recurso é atualizado.

D) Nenhuma ação é realizada.

Resposta:

Resposta correta: B)

Um código 404 é retornado para indicar que o recurso não foi encontrado.
