---
titulo: "Conhecendo o Spring MVC"
tipo: rco-seed
disciplina: programacao-no-desenvolvimento-de-sistemas
sigla_rco: PDS
trimestre: 3
ordem_rco: 102
serie: 3
aula_rco: "Aula 102"
slides: 23
tem_atividade: false
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/3TRI/102-conhecendo-o-spring-mvc/102-conhecendo-o-spring-mvc.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/3TRI/102-conhecendo-o-spring-mvc/AULA 102_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Conhecendo o Spring MVC

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO NO
- DESENVOLVIMENTO DE
- SISTEMAS
- 3ª SÉRIE
- Conhecendo o Spring MVC
- Aula 102

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
- Aprender como o Spring MVC organiza e facilita o desenvolvimento de aplicações web.

_7 imagem(ns) no slide._

### Slide 5

- DESENVOLVIMENTO DE SISTEMAS
- A aula envolve raciocínio lógico, abstração algorítmica e análise de fluxos de dados, o que dialoga diretamente com descritores do eixo Álgebra e Funções. De acordo com o Caderno de Intervenção Pedagógica, umas das habilidades que grande parte dos estudantes tem dificuldade de aprender é:
- Caso perceba que seus estudantes têm esta dificuldade, que tal relembrar alguns conceitos importantes?
- D18 – Reconhecer expressão algébrica que representa uma função a partir de uma tabela ➝ Analogamente, o Controller representa funções/métodos que transformam dados em saídas.
- D19 – Resolver problema envolvendo uma função do 1º grau ➝ Relaciona-se à modelagem de fluxos simples: entrada de dados (x) → processamento → saída (y).

_6 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Na aula anterior…
- Aprendemos a construir consultas dinâmicas usando Specifications, permitindo a composição de filtros de pesquisa flexíveis.
- Hoje, aplicaremos esse conhecimento para manipular requisições e respostas no Spring MVC.

_4 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- No entanto, ela não sabe como conectar a requisição HTTP à resposta de uma página HTML usando Spring Boot…
- Mariana é uma desenvolvedora iniciante que precisa criar uma página para mostrar a lista de produtos de uma loja virtual.

_4 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Como Mariana pode usar um Controller no Spring MVC para receber a requisição e enviar a lista de produtos para ser exibida na página?
- Quem sabe responde!

_8 imagem(ns) no slide._

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Ela deve criar um Controller que mapeie a URL da página e use um método que retorne um modelo de dados com a lista de produtos.
- Depois de criado, o modelo segue para a visualização (HTML), que transforma essas informações em uma página visível para o usuário!

_5 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- Spring MVC
- É um framework que facilita a construção de aplicações web usando o padrão Model-View-Controller.
- Ele organiza a lógica de controle e apresentação, permitindo desenvolver interfaces interativas e dinâmicas.

_4 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Definição e Aplicação
- Spring MVC com Spring Boot: Usando Spring Boot, o Spring MVC é configurado automaticamente, o que facilita a criação de projetos web e elimina a necessidade de configurações manuais extensas.
- O Primeiro Controller: Um Controller é uma classe que responde a solicitações HTTP e gerencia como esses dados são exibidos para o usuário. Ele atua como intermediário entre o modelo e a visualização.

_5 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- Os Controllers são essenciais para o desenvolvimento de funcionalidades como: formulários, exibição de listas e páginas interativas.
- https://bilder.obi.at/a086bef7-319b-4003-a46b-3d9536653659/prZZH/576880_1265_1.jpg
- Para construir aplicações web robustas e escaláveis.
- Usado é amplamente Spring MVC!

_6 imagem(ns) no slide._

### Slide 13

- DESENVOLVIMENTO DE SISTEMAS
- Exemplo
- Em uma aplicação de loja online, um Controller é responsável por receber a requisição de busca de um produto, acessar o banco de dados e enviar a lista para ser exibida na tela.

_4 imagem(ns) no slide._

### Slide 14

- DESENVOLVIMENTO DE SISTEMAS
- Exemplo
- Neste exemplo, o método mostrarHomePage() mapeia a URL "/home", adiciona uma mensagem ao modelo e retorna o nome da página HTML (home.html) que exibirá a mensagem.

_4 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- Questão de fixação
- Qual é a principal função de um Controller no Spring MVC?
- A) Gerar código JavaScript.
- B) Manipular interações de banco de dados.
- C) Receber requisições HTTP e definir a resposta.
- D) Executar operações de CRUD.
- Realizem a atividade em duplas e socializem no final!

_4 imagem(ns) no slide._

### Slide 16

- DESENVOLVIMENTO DE SISTEMAS
- Resposta!
- Qual é a principal função de um Controller no Spring MVC?
- A) Gerar código JavaScript.
- B) Manipular interações de banco de dados.
- C) Receber requisições HTTP e definir a resposta.
- D) Executar operações de CRUD.
- Resposta correta: C)

_3 imagem(ns) no slide._

### Slide 17

- DESENVOLVIMENTO DE SISTEMAS
- Atividade Prática na Plataforma Alura
- Na plataforma Alura vamos acessar o seguinte curso:
- Link para o curso: https://cursos.alura.com.br/course/spring-mvc-thymeleaf-bootstrap
- Atividade no portal Alura! Ela vai te ajudar a explorar o tema de um jeito ainda mais claro e interessante, ampliando seus conhecimentos.

_7 imagem(ns) no slide._

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- Spring MVC com Spring Boot
- 11 minutos
- Link para tarefa: https://cursos.alura.com.br/course/spring-mvc-thymeleaf-bootstrap/task/80865
- Spring MVC com Spring Boot facilita o desenvolvimento de aplicações web, fornecendo configurações automáticas e integração com controladores, modelos e visualizações, simplificando a criação de APIs e páginas dinâmicas.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- O primeiro Controller
- 10 minutos
- Link para tarefa: https://cursos.alura.com.br/course/spring-mvc-thymeleaf-bootstrap/task/80866
- O primeiro Controller no Spring MVC é responsável por mapear URLs para métodos que manipulam requisições e definem as respostas, como páginas HTML ou dados JSON. Ele atua como intermediário no fluxo da aplicação.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 20

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje
- Aprendemos como o Spring MVC organiza o fluxo de dados em uma aplicação web, explorando como criar um primeiro Controller.
- Essa base permite criar páginas interativas e responder a solicitações HTTP, ligando o conhecimento de consultas dinâmicas visto na aula anterior ao desenvolvimento web interativo.

_4 imagem(ns) no slide._

### Slide 21

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

### Slide 22

- DESENVOLVIMENTO DE SISTEMAS
- Referências (Imagens)
- https://www.flaticon.com/br
- https://www.istockphoto.com/br
- https://raw.githubusercontent.com/zbtang/React-Native-ViewPager/HEAD/imgs/dotIndicator.gif
- https://storyset.com

_3 imagem(ns) no slide._

### Slide 23

- DESENVOLVIMENTO DE SISTEMAS
- O RCO+Aulas é um projeto da Secretaria de Estado da Educação do Paraná e está em constante revisão. Todos os slides são de uso exclusivo dos professores da Rede Pública de Ensino, com a finalidade específica de aplicação em sala de aula, sendo totalmente vedada a publicização, reutilização, reprodução total ou parcial para quaisquer outros fins.

_4 imagem(ns) no slide._

## Outros documentos

_Fonte: AULA 102_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

ATIVIDADE AULA 102

Questão 1

Qual método é usado para mapear uma URL em um Controller Spring MVC?

A) @GetMapping

B) @RequestModel

C) @SetPath

D) @ControlRoute

Resposta:

Resposta correta: A)

@GetMapping mapeia uma URL a um método do Controller, indicando que ele deve responder a requisições GET.

Questão 2

Quando devemos usar @RestController em vez de @Controller?

A) Quando queremos retornar páginas HTML.

B) Quando a classe realiza operações de banco de dados.

C) Quando queremos retornar dados JSON ou XML.

D) Quando mapeamos URLs dinâmicas.

Resposta:

Resposta correta: C)

@RestController é usado para criar APIs RESTful, retornando respostas em formato JSON ou XML, em vez de páginas HTML.
