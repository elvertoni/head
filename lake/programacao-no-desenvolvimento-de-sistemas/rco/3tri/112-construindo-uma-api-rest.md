---
titulo: "Construindo uma API REST"
tipo: rco-seed
disciplina: programacao-no-desenvolvimento-de-sistemas
sigla_rco: PDS
trimestre: 3
ordem_rco: 112
serie: 3
aula_rco: "Aula 112"
slides: 25
tem_atividade: false
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/3TRI/112-construindo-uma-api-rest/112-construindo-uma-api-rest.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/3TRI/112-construindo-uma-api-rest/AULA 112_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Construindo uma API REST

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO NO
- DESENVOLVIMENTO DE
- SISTEMAS
- 3ª SÉRIE
- Construindo uma API REST
- Aula 112

_3 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- DESENVOLVIMENTO DE SISTEMAS
- ATENÇÃO PROFESSOR!
- O Material aqui apresentado, segue a análise do plano de curso contemplando os componentes curriculares e seus objetos de conhecimento, sendo assim, você tem liberdade para customizar o material conforme seu contexto para maior aproveitamento do conteúdo. Em caso de falta ou indisponibilidade de acesso à internet no local de aula, você poderá utilizar os seguintes artigos para criação de material complementar para auxiliar na aula:
- Leitura/Recursos Adicionais:
- Spring Initializr (start.spring.io): Uma ferramenta online que permite criar projetos Spring Boot rapidamente. Você pode selecionar dependências como Spring Data JPA e H2 Database para começar.

_5 imagem(ns) no slide._

### Slide 4

- DESENVOLVIMENTO DE SISTEMAS
- Nesta aula, vamos:
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store
- Aprender os princípios das APIs REST e como criar um RestController usando Spring MVC.

_7 imagem(ns) no slide._

### Slide 5

- DESENVOLVIMENTO DE SISTEMAS
- Na aula anterior…
- Exploramos a paginação e cache, duas técnicas que ajudam a organizar grandes volumes de dados e a otimizar a performance da aplicação.
- Hoje, vamos aplicar esses conhecimentos para construir uma API REST, estruturando o acesso aos dados.

_4 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Sofia está desenvolvendo uma aplicação de gestão de tarefas e quer criar uma API para que o aplicativo móvel e a versão web possam compartilhar os mesmos dados.
- Ela precisa estruturar uma API REST para fornecer acesso às tarefas e receber novas…

_4 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Pergunta
- Como Sofia pode construir uma API REST com Spring MVC para que ambos os sistemas acessem e manipulem os dados de maneira eficiente e segura?
- Quem sabe responde!

_6 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Sofia pode criar uma API REST usando RestController no Spring MVC, definindo endpoints para operações de CRUD (criar, ler, atualizar e deletar) que permitirão ao aplicativo móvel e à versão web interagirem com os dados de tarefas.

_5 imagem(ns) no slide._

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- APIs REST permitem que diferentes aplicações se comuniquem de maneira padronizada, enviando e recebendo dados.
- No Spring MVC, o RestController facilita a criação de endpoints REST, essencial para conectar o backend a diferentes interfaces.

_4 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- Definição e Aplicação
- Criando o RestController
- No Spring MVC, RestController é a classe que define os endpoints da API, facilitando a criação de rotas que acessam, manipulam e exibem dados em formato JSON.
- Introdução ao REST
- REST é um padrão de arquitetura que permite a troca de informações entre sistemas de forma padronizada, geralmente usando HTTP como protocolo de comunicação.

_5 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- As APIs REST são fundamentais para integrar o backend com interfaces diferentes, como aplicativos móveis e web, permitindo a troca eficiente de informações e promovendo a expansão da aplicação para diferentes plataformas.

_4 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- Em um sistema de e-commerce, a API REST permite que o aplicativo móvel e o site compartilhem informações de produtos, carrinho de compras e histórico de pedidos de maneira sincronizada.

_4 imagem(ns) no slide._

### Slide 13

- DESENVOLVIMENTO DE SISTEMAS
- Exemplo
- Este controlador define endpoints para listar todos os produtos (GET), adicionar um novo produto (POST) e deletar um produto específico (DELETE), oferecendo uma estrutura simples e prática para manipular dados.

_4 imagem(ns) no slide._

### Slide 14

- DESENVOLVIMENTO DE SISTEMAS
- Questão para fixação
- Qual é o papel de uma API REST em uma aplicação?
- A) Melhorar a segurança do sistema.
- B) Permitir a comunicação e troca de dados entre diferentes sistemas.
- C) Organizar a estrutura de diretórios.
- D) Exibir dados diretamente na interface.
- Troque ideias com seus colegas!

_4 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- Resposta!
- Qual é o papel de uma API REST em uma aplicação?
- A) Melhorar a segurança do sistema.
- B) Permitir a comunicação e troca de dados entre diferentes sistemas.
- C) Organizar a estrutura de diretórios.
- D) Exibir dados diretamente na interface.
- Resposta correta: B)

_4 imagem(ns) no slide._

### Slide 16

- DESENVOLVIMENTO DE SISTEMAS
- Atividade Prática na Plataforma Alura
- Na plataforma Alura vamos acessar o seguinte curso:
- Atividade no portal Alura! Ela vai te ajudar a explorar o tema de um jeito ainda mais claro e interessante, ampliando seus conhecimentos.
- Link para o curso: https://cursos.alura.com.br/course/spring-mvc-security-rest-vuejs-ajax

_7 imagem(ns) no slide._

### Slide 17

- DESENVOLVIMENTO DE SISTEMAS
- Introdução ao REST
- 7 minutos
- Link para tarefa: https://cursos.alura.com.br/course/spring-mvc-security-rest-vuejs-ajax/task/81139
- REST (Representational State Transfer) é uma arquitetura que padroniza a comunicação entre sistemas, usando métodos HTTP (como GET, POST, PUT e DELETE). É amplamente usado para criar APIs, facilitando o acesso e a troca de dados.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- Criando o RestController
- 7 minutos
- Link para tarefa: https://cursos.alura.com.br/course/spring-mvc-security-rest-vuejs-ajax/task/81140
- Criar um RestController no Spring MVC permite definir endpoints de API para operações de dados, como consulta e atualização. Usando @RestController, o Spring gera respostas em JSON, facilitando a comunicação com clientes front-end e mobile.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje
- Aprendemos como construir uma API REST no Spring MVC usando RestController, possibilitando que a aplicação se comunique com outras interfaces e sistemas.
- Vimos como definir endpoints para operações de CRUD, proporcionando um sistema organizado e eficiente para gerenciar dados.

_4 imagem(ns) no slide._

### Slide 20

_(sem texto)_

_1 imagem(ns) no slide._

### Slide 21

_(sem texto)_

_1 imagem(ns) no slide._

### Slide 22

- DESENVOLVIMENTO DE SISTEMAS
- Pronto para desbloquear sua carreira de TI?
- Está perdido estudando mas não sabe por onde começar? Se a resposta é sim, você está no lugar certo! Descubra as estratégias e ferramentas essenciais para te ajudar a desbloquear seu potencial em TI e buscar sua primeira vaga de emprego no setor!
- Este e-book é um guia completo para quem busca começar pelos melhores caminhos para se tornar um excelente profissional de TI, ensinando a identificar perfis profissionais, aplicar técnicas de estudo eficazes, transformar teoria em prática, e aumentar a visibilidade de seu trabalho no mercado de trabalho. Ideal para novatos e profissionais em transição.
- E o melhor, ele pode ser seu, inteiramente grátis!
- Basta clicar AQUI e realizar o seu cadastro com o seu @escola!

_5 imagem(ns) no slide._

### Slide 23

- DESENVOLVIMENTO DE SISTEMAS
- Referências
- PUREWAL, Semmy. Aprendendo a Desenvolver Aplicações Web. Desenvolva rapidamente com as tecnologias JavaScript mais modernas. São Paulo: Novatec, 2014.
- SILVA, L. F.; OLIVEIRA, A. D. de. Desenvolvimento de Software II C#: programação em camadas. [S. l.]: CBL Edição do Autor, 2017. E-book.
- MARTIN, R. C. Arquitetura limpa: o guia do artesão para estrutura e design de software. Rio de Janeiro: Alta Books, 2019. E-book.
- GALOTTI, G. M. A. Qualidade de software. São Paulo: Pearson Education do Brasil, 2016. E-book.
- VAZQUEZ, C. E.; SIMÕES, G. S. Engenharia de requisitos: software orientado ao negócio. São Paulo: Brasport, 2016. E-book.
- Softwares
- Java Netbeans; WebStorm; Sublime Text; Intellij IDEA; Astah Software; Netbeans; Python; Ccharp; Colab; PyCharm; Jupyter Notebook.

_3 imagem(ns) no slide._

### Slide 24

- DESENVOLVIMENTO DE SISTEMAS
- Referências (Imagens)
- https://www.flaticon.com/br
- https://www.istockphoto.com/br
- https://raw.githubusercontent.com/zbtang/React-Native-ViewPager/HEAD/imgs/dotIndicator.gif
- https://storyset.com

_3 imagem(ns) no slide._

### Slide 25

- DESENVOLVIMENTO DE SISTEMAS
- O RCO+Aulas é um projeto da Secretaria de Estado da Educação do Paraná e está em constante revisão. Todos os slides são de uso exclusivo dos professores da Rede Pública de Ensino, com a finalidade específica de aplicação em sala de aula, sendo totalmente vedada a publicização, reutilização, reprodução total ou parcial para quaisquer outros fins.

_4 imagem(ns) no slide._

## Outros documentos

_Fonte: AULA 112_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

ATIVIDADE AULA 112

Questão 1

Qual método HTTP é mais adequado para buscar dados em uma API REST?

A) POST

B) GET

C) DELETE

D) PUT

Resposta:

Resposta correta: B)

GET é o método HTTP ideal para buscar dados, enquanto POST é usado para criar, PUT para atualizar e DELETE para remover.

Questão 2

Qual é a função do @RequestBody em um método POST?

A) Retornar uma resposta em JSON.

B) Ler dados do cabeçalho HTTP.

C) Receber dados enviados no corpo da requisição.

D) Definir o tipo de resposta.

Resposta:

Resposta correta: C)

@RequestBody é usado para receber dados enviados no corpo da requisição, necessário em métodos POST e PUT para criar ou atualizar recursos.
