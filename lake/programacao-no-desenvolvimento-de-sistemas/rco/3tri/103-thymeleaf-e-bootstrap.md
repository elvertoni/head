---
titulo: "Thymeleaf e Bootstrap"
tipo: rco-seed
disciplina: programacao-no-desenvolvimento-de-sistemas
sigla_rco: PDS
trimestre: 3
ordem_rco: 103
serie: 3
aula_rco: "Aula 103"
slides: 26
tem_atividade: false
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/3TRI/103-thymeleaf-e-bootstrap/103-thymeleaf-e-bootstrap.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/3TRI/103-thymeleaf-e-bootstrap/AULA 103_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Thymeleaf e Bootstrap

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO NO
- DESENVOLVIMENTO DE
- SISTEMAS
- 3ª SÉRIE
- Thymeleaf e Bootstrap
- Aula 103

_3 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- DESENVOLVIMENTO DE SISTEMAS
- Nesta aula, vamos:
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store
- Aprender a integrar o motor de templates Thymeleaf com o framework CSS Bootstrap, construindo uma interface dinâmica e responsiva em uma aplicação Spring MVC.

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
- Exploramos como o Spring MVC organiza o fluxo de dados em uma aplicação web, criando nosso primeiro Controller. Hoje, vamos avançar construindo interfaces web dinâmicas usando Thymeleaf e Bootstrap para melhorar a apresentação visual.

_4 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Lucas está criando uma página de exibição de produtos para um site de vendas, mas percebe que a interface está sem estilo e a lista de produtos não é exibida corretamente.
- Ele quer organizar a página para que os produtos apareçam de forma estilizada e responsiva em diferentes dispositivos, mas não sabe como aplicar o Bootstrap e exibir a lista usando Thymeleaf...

_4 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Lucas poderá…
- Aplicar Bootstrap e usar Thymeleaf para percorrer a lista de produtos no HTML: Lucas pode usar o Bootstrap para criar uma interface responsiva e elegante, e o Thymeleaf para iterar sobre a lista de produtos e exibi-los dinamicamente na página.
- Usar apenas HTML simples sem frameworks: Lucas tenta exibir a lista sem Thymeleaf e não aplica o Bootstrap. Embora a página funcione, ela ficará visualmente pobre e não responsiva em diferentes dispositivos.
- Quem sabe responde!

_6 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Resposta correta
- A solução correta é usar Bootstrap para melhorar a aparência e responsividade da página e Thymeleaf para dinamicamente percorrer e exibir os produtos. Essa abordagem é mais eficiente e moderna.
- Usar HTML sem frameworks pode funcionar, mas resultará em uma interface rígida e não otimizada, sem o apelo visual e responsividade que os usuários esperam.

_5 imagem(ns) no slide._

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- Thymeleaf
- É um motor de templates que permite renderizar dados dinâmicos em páginas HTML, enquanto o Bootstrap é um framework CSS que facilita a criação de interfaces responsivas e estilizadas. Juntos, eles formam uma poderosa combinação para desenvolver interfaces modernas no Spring MVC.

_4 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- Criando o modelo
- No Spring MVC, o modelo contém os dados que serão exibidos na página, enviados do Controller para a visualização (view).
- O Thymeleaf permite iterar sobre listas de dados, como produtos, exibindo-os dinamicamente na página HTML.
- Percorrendo
- a lista na view

_3 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Definição e Aplicação
- Aplicando o Bootstrap: O Bootstrap facilita a criação de layouts responsivos com classes CSS pré-definidas, otimizando a experiência do usuário em diferentes dispositivos.
- Posicionamento com Bootstrap: Usando o sistema de grid do Bootstrap, podemos organizar elementos na página, garantindo que fiquem bem distribuídos e adaptados em telas de vários tamanhos.

_6 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- Saber como integrar Thymeleaf e Bootstrap é essencial para desenvolver aplicações web modernas e responsivas, que oferecem uma experiência de usuário agradável, além de exibir dados de forma eficiente.

_4 imagem(ns) no slide._

### Slide 13

- DESENVOLVIMENTO DE SISTEMAS
- Exemplo
- Em um site de e-commerce, podemos usar Thymeleaf para exibir uma lista de produtos diretamente no HTML e o Bootstrap para garantir que a página se ajuste a diferentes dispositivos, como celulares e tablets.

_4 imagem(ns) no slide._

### Slide 14

- DESENVOLVIMENTO DE SISTEMAS
- Exemplo
- Página de produtos com Thymeleaf e Bootstrap.

_4 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- Questão de fixação
- Qual é a principal função do Thymeleaf no Spring MVC?
- A) Criar consultas SQL dinâmicas.
- B) Renderizar dados dinâmicos em páginas HTML.
- C) Estilizar elementos HTML com CSS.
- D) Conectar o banco de dados à aplicação.
- Quem sabe responde!

_4 imagem(ns) no slide._

### Slide 16

- DESENVOLVIMENTO DE SISTEMAS
- Resposta!
- Qual é a principal função do Thymeleaf no Spring MVC?
- A) Criar consultas SQL dinâmicas.
- B) Renderizar dados dinâmicos em páginas HTML.
- C) Estilizar elementos HTML com CSS.
- D) Conectar o banco de dados à aplicação.
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
- Criando o modelo
- 6 minutos
- Link para tarefa: https://cursos.alura.com.br/course/spring-mvc-thymeleaf-bootstrap/task/80867
- Criar o modelo no Spring MVC envolve definir classes que representam os dados da aplicação. O modelo é preenchido no Controller e enviado para a view (página HTML), onde será exibido dinamicamente.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- Percorrendo a lista na view
- 8 minutos
- Link para tarefa: https://cursos.alura.com.br/course/spring-mvc-thymeleaf-bootstrap/task/80868
- No Thymeleaf, para percorrer uma lista na view, usa-se o atributo th:each, que permite iterar sobre uma coleção de objetos e exibir seus dados dinamicamente em elementos HTML, como tabelas ou cards.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 20

- DESENVOLVIMENTO DE SISTEMAS
- Aplicando o Bootstrap
- 9 minutos
- Link para tarefa: https://cursos.alura.com.br/course/spring-mvc-thymeleaf-bootstrap/task/80869
- Aplicar o Bootstrap em uma página web envolve usar suas classes CSS pré-definidas para criar layouts responsivos, estilizar elementos como botões e formulários, e garantir uma interface adaptável em diferentes dispositivos.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 21

- DESENVOLVIMENTO DE SISTEMAS
- Posicionamento com Bootstrap
- 14 minutos
- Link para tarefa: https://cursos.alura.com.br/course/spring-mvc-thymeleaf-bootstrap/task/80870
- O posicionamento com Bootstrap é feito usando seu sistema de grid, que divide a página em colunas. Classes como container, row e col permitem organizar elementos de forma responsiva e alinhada em qualquer tela.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 22

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje
- Como integrar Thymeleaf e Bootstrap no Spring MVC, a criar interfaces responsivas e a exibir dados dinâmicos de forma estilizada. Com isso, demos um passo importante na construção de aplicações web modernas e eficientes.

_4 imagem(ns) no slide._

### Slide 23

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

### Slide 24

- DESENVOLVIMENTO DE SISTEMAS
- Referências (Imagens)
- Figuras e Imagens:
- https://www.flaticon.com/br
- https://www.istockphoto.com/br
- https://raw.githubusercontent.com/zbtang/React-Native-ViewPager/HEAD/imgs/dotIndicator.gif
- https://storyset.com

_3 imagem(ns) no slide._

### Slide 25

- DESENVOLVIMENTO DE SISTEMAS
- O RCO+Aulas é um projeto da Secretaria de Estado da Educação do Paraná e está em constante revisão. Todos os slides são de uso exclusivo dos professores da Rede Pública de Ensino, com a finalidade específica de aplicação em sala de aula, sendo totalmente vedada a publicização, reutilização, reprodução total ou parcial para quaisquer outros fins.

_4 imagem(ns) no slide._

### Slide 26

- DESENVOLVIMENTO DE SISTEMAS
- Esta publicação tem a cooperação entre a UNESCO e a Secretaria de Estado da Educação e do Esporte do Paraná no âmbito da parceria PRODOC 914BRZ1091, cujo objetivo é trazer soluções inovadoras de gestão da rede pública estadual de educação do Paraná para a melhoria da aprendizagem dos alunos. As indicações de nomes e a apresentação do material ao longo desta publicação não implicam a manifestação de qualquer opinião por parte da UNESCO a respeito da condição jurídica de qualquer país, território, cidade, região ou de suas autoridades, tampouco da delimitação de suas fronteiras ou limites As ideias e opiniões expressas nesta publicação são as dos autores e não refletem obrigatoriamente as da UNESCO nem comprometem a Organização.
- Cooperação Técnica

_4 imagem(ns) no slide._

## Outros documentos

_Fonte: AULA 103_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

ATIVIDADE AULA 103

Questão 1

Como você percorre uma lista de objetos usando Thymeleaf em uma página HTML?

A) th:text="*".

B) th:for.

C) th:each.

D) th:list.

Resposta:

Resposta correta: C)

O atributo th:each é usado para iterar sobre uma coleção de objetos em Thymeleaf, permitindo exibir cada item individualmente na página HTML.

Questão 2

Qual é a função da classe container no Bootstrap?

A) Ajustar o conteúdo a uma largura fixa e centralizada na página.

B) Criar animações com CSS.

C) Definir cores personalizadas.

D) Carregar imagens de forma responsiva.

Resposta:

Resposta correta: A)

A classe container no Bootstrap é usada para centralizar o conteúdo e ajustar a largura da página de forma responsiva.
