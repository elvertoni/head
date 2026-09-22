---
titulo: "Trabalhando com POST"
tipo: rco-seed
disciplina: programacao-no-desenvolvimento-de-sistemas
sigla_rco: PDS
trimestre: 3
ordem_rco: 119
serie: 3
aula_rco: "Aula 119"
slides: 30
tem_atividade: false
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/3TRI/119-trabalhando-com-post/119-trabalhando-com-post.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/3TRI/119-trabalhando-com-post/AULA 119_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Trabalhando com POST

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO NO
- DESENVOLVIMENTO DE
- SISTEMAS
- 3ª SÉRIE
- Trabalhando com POST
- Aula 119

_3 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- DESENVOLVIMENTO DE SISTEMAS
- Nesta aula, vamos:
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store
- Aprender a criar cadastros utilizando o método POST em APIs REST.

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
- Exploramos o Spring Data e vimos como acessar e manipular dados de forma eficiente usando repositórios e filtros. Hoje, avançaremos para implementar cadastros na API REST, com foco no método POST.

_4 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Ana está criando uma aplicação para gerenciar tópicos de um fórum. Ela precisa de um endpoint que permita cadastrar novos tópicos, garantindo que os dados sejam enviados corretamente e com segurança.

_4 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Pergunta
- Como Ana pode criar um endpoint POST em sua API REST para cadastrar tópicos e garantir que os dados sejam validados antes de serem armazenados no banco de dados?
- Quem sabe responde!

_5 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Ana pode criar um endpoint POST no Spring Boot, usando um controlador para processar os dados enviados. Ela pode usar DTOs para validar os dados antes de enviá-los para o repositório.

_4 imagem(ns) no slide._

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- O método POST é usado em APIs REST para criar novos registros no banco de dados. Ele permite que o cliente envie dados no corpo da requisição, que são processados e armazenados pela aplicação.

_4 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- Aplicação
- Cadastrando Tópicos: Criar um endpoint POST para receber dados, validá-los e armazená-los no banco de dados.
- Boas Práticas no Cadastro: Usar DTOs para validar e estruturar os dados enviados, garantindo segurança e clareza.
- Testando com Postman: Validar o funcionamento do endpoint, verificando se os dados são enviados, recebidos e processados corretamente.

_4 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Cadastrar dados é uma funcionalidade central em muitas aplicações, como sistemas de usuários ou gerenciamento de produtos. Usar boas práticas no POST garante segurança, desempenho e facilidade de manutenção.

_4 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- Em um sistema de loja online, o POST permite cadastrar novos produtos, enviando informações como nome, preço e descrição diretamente para a API.

_4 imagem(ns) no slide._

### Slide 13

- DESENVOLVIMENTO DE SISTEMAS
- Exemplo
- Um exemplo simples de criação de um endpoint POST para cadastrar tópicos
- Criando o DTO para validar os dados

_4 imagem(ns) no slide._

### Slide 14

- DESENVOLVIMENTO DE SISTEMAS
- Exemplo
- Um exemplo simples de criação de um endpoint POST para cadastrar tópicos
- Criando o Modelo e Repositório

_4 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- Exemplo
- Um exemplo simples de criação de um endpoint POST para cadastrar tópicos
- Criando o Endpoint POST

_4 imagem(ns) no slide._

### Slide 16

- DESENVOLVIMENTO DE SISTEMAS
- Exemplo
- Um exemplo simples de criação de um endpoint POST para cadastrar tópicos
- Testando com o Postman
- Configure uma requisição POST para http://localhost:8080/topicos.
- No corpo da requisição, envie um JSON como.

_4 imagem(ns) no slide._

### Slide 17

- DESENVOLVIMENTO DE SISTEMAS
- Questão de fixação
- Qual é a função principal do método POST em uma API REST?
- A) Excluir dados do banco de dados.
- B) Atualizar registros existentes.
- C) Criar novos registros no banco de dados.
- D) Recuperar informações.
- Quem sabe responde!

_4 imagem(ns) no slide._

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- Resposta!
- Qual é a função principal do método POST em uma API REST?
- A) Excluir dados do banco de dados.
- B) Atualizar registros existentes.
- C) Criar novos registros no banco de dados.
- D) Recuperar informações.
- Resposta correta: C)

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
- Cadastrando tópicos
- 17 minutos
- Link para tarefa: https://cursos.alura.com.br/course/spring-boot-api-rest/task/55823
- Cadastrar tópicos em uma API REST envolve criar um endpoint POST para receber os dados enviados, validá-los com DTOs e armazená-los no banco de dados usando o Spring Data JPA de forma segura e eficiente.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 21

- DESENVOLVIMENTO DE SISTEMAS
- Boas práticas no cadastro
- 8 minutos
- Link para tarefa: https://cursos.alura.com.br/course/spring-boot-api-rest/task/55824
- Boas práticas no cadastro incluem usar DTOs para validar dados, evitar expor diretamente entidades, tratar exceções, padronizar respostas HTTP e documentar endpoints, garantindo segurança e clareza na API.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 22

- DESENVOLVIMENTO DE SISTEMAS
- Testando o cadastro com Postman
- 7 minutos
- Link para tarefa: https://cursos.alura.com.br/course/spring-boot-api-rest/task/55825
- Testar cadastros com Postman envolve configurar uma requisição POST, definir o endpoint, enviar dados no corpo em formato JSON e verificar a resposta para garantir que o cadastro funcione corretamente.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 23

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje
- Aprendemos o que são endpoints POST em APIs REST usando Spring Boot, exploramos o uso de DTOs para validação e testamos a funcionalidade com Postman.

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

_Fonte: AULA 119_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

ATIVIDADE AULA 119

Questão 1

Qual anotação indica que um método em Spring Boot responde a uma requisição POST?

A) @GetMapping

B) @DeleteMapping

C) @PostMapping

D) @PutMapping

Resposta:

Resposta correta: C)

@PostMapping é usada para definir métodos que respondem a requisições HTTP POST.

Questão 2

Como testar um endpoint POST criado em uma API REST?

A) Usando IDEs como IntelliJ IDEA.

B) Com ferramentas como Postman ou cURL.

C) Escrevendo diretamente no banco de dados.

D) Apenas visualizando o código.

Resposta:

Resposta correta: B)

Ferramentas como Postman ou cURL permitem testar endpoints POST enviando dados no corpo da requisição.
