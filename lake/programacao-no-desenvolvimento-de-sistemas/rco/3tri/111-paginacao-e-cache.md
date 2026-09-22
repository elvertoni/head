---
titulo: "Paginação e Cache"
tipo: rco-seed
disciplina: programacao-no-desenvolvimento-de-sistemas
sigla_rco: PDS
trimestre: 3
ordem_rco: 111
serie: 3
aula_rco: "Aula 111"
slides: 30
tem_atividade: false
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/3TRI/111-paginacao-e-cache/111-paginacao-e-cache.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/3TRI/111-paginacao-e-cache/AULA 111_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Paginação e Cache

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO NO
- DESENVOLVIMENTO DE
- SISTEMAS
- 3ª SÉRIE
- Paginação e Cache
- Aula 111

_3 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- DESENVOLVIMENTO DE SISTEMAS
- Nesta aula, vamos:
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store
- Aprender a organizar e otimizar exibições de grandes volumes de dados com paginação.

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
- Conhecemos como funciona um provedor de autenticação para validar usuários em um banco de dados usando JDBC com Spring Security, protegendo e organizando o acesso. Hoje, vamos aprimorar a navegação e o desempenho da aplicação com recursos de paginação e cache.

_4 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- André é responsável pelo desenvolvimento de uma plataforma de streaming que exibe uma grande quantidade de filmes. Ele quer garantir que a navegação entre páginas seja rápida, mesmo com um grande volume de dados, e que as informações mais acessadas sejam exibidas sem necessidade de recarregar tudo do zero.

_4 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Pergunta
- Como André pode implementar a paginação para facilitar a navegação entre dados e o cache para otimizar o carregamento de informações mais acessadas?
- Quem sabe responde!

_5 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- André pode configurar a paginação para dividir a lista de filmes em várias páginas, facilitando o carregamento de dados aos poucos. O cache pode ser habilitado para que dados frequentemente acessados sejam carregados mais rápido, reduzindo a necessidade de novas consultas ao banco.

_4 imagem(ns) no slide._

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- A paginação permite dividir listas grandes em páginas menores, enquanto o cache armazena dados frequentemente acessados para acelerar o carregamento.
- Paginação e cache são técnicas usadas para otimizar a navegação e o desempenho de uma aplicação.

_4 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- Definição e Aplicação
- Controlando os usuários
- Paginação permite que usuários naveguem facilmente entre grandes listas de dados, como listas de produtos ou posts, organizando-os em páginas menores e navegáveis.
- Ajustando a navegação
- Com a paginação, podemos organizar melhor a apresentação de dados em páginas distintas, otimizando a experiência do usuário.

_4 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Definição e Aplicação
- Trabalhando com paginação
- A implementação de paginação no Spring MVC permite carregar apenas uma porção dos dados por vez, otimizando o desempenho.
- Habilitando o cache
- O cache armazena dados frequentemente acessados em uma memória temporária, tornando o carregamento das próximas consultas mais rápido.

_4 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- Paginação e cache são fundamentais para melhorar a experiência do usuário, especialmente em aplicações com muitos dados. Eles permitem que a aplicação responda rapidamente, mesmo em ambientes de grande escala.

_4 imagem(ns) no slide._

### Slide 13

- DESENVOLVIMENTO DE SISTEMAS
- Em uma loja virtual, os produtos são paginados para que o usuário navegue página por página. Além disso, produtos mais populares são armazenados em cache para acelerar o carregamento.

_4 imagem(ns) no slide._

### Slide 14

- DESENVOLVIMENTO DE SISTEMAS
- Exemplo
- exemplo de como implementar paginação e cache no Spring MVC

_4 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- Exemplo
- Esse código de configuração permite ao Spring utilizar cache para armazenar resultados de consultas, otimizando o desempenho da aplicação.

_4 imagem(ns) no slide._

### Slide 16

- DESENVOLVIMENTO DE SISTEMAS
- Questão de fixação
- Qual é a principal função da paginação em uma aplicação web?
- A) Aumentar o número de acessos ao banco de dados.
- B) Dividir grandes listas em páginas menores para facilitar a navegação.
- C) Substituir o cache para otimizar a aplicação.
- D) Exibir todos os dados em uma única página.
- Quem sabe responde!

_4 imagem(ns) no slide._

### Slide 17

- DESENVOLVIMENTO DE SISTEMAS
- Resposta!
- Qual é a principal função da paginação em uma aplicação web?
- A) Aumentar o número de acessos ao banco de dados.
- B) Dividir grandes listas em páginas menores para facilitar a navegação.
- C) Substituir o cache para otimizar a aplicação.
- D) Exibir todos os dados em uma única página.
- Resposta correta: B)

_3 imagem(ns) no slide._

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- Atividade Prática na Plataforma Alura
- Na plataforma Alura vamos acessar o seguinte curso:
- A recomendação é que você continue esse curso extraclasse, pois ele traz um conteúdo essencial para compreender sobre o referido tema.
- Link para o curso: https://cursos.alura.com.br/course/spring-mvc-security-rest-vuejs-ajax

_6 imagem(ns) no slide._

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- Controlando os usuários
- 10 minutos
- Link para tarefa: https://cursos.alura.com.br/course/spring-mvc-security-rest-vuejs-ajax/task/81135
- Controlar os usuários envolve gerenciar o acesso e navegação entre grandes listas de dados. A paginação facilita essa navegação, exibindo os dados de forma organizada e reduzindo o carregamento da página, melhorando a experiência do usuário.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 20

- DESENVOLVIMENTO DE SISTEMAS
- Ajustando a navegação
- 13 minutos
- Link para tarefa: https://cursos.alura.com.br/course/spring-mvc-security-rest-vuejs-ajax/task/81136
- Ajustar a navegação significa organizar a exibição de dados em páginas, usando paginação para que o usuário navegue por seções menores. Isso melhora a usabilidade e evita sobrecarga na interface.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 21

- DESENVOLVIMENTO DE SISTEMAS
- Trabalhando com paginação
- 8 minutos
- Link para tarefa: https://cursos.alura.com.br/course/spring-mvc-security-rest-vuejs-ajax/task/81137
- Trabalhar com paginação no Spring MVC permite dividir grandes listas de dados em páginas menores, facilitando a visualização e reduzindo o tempo de carregamento, o que melhora a experiência do usuário.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 22

- DESENVOLVIMENTO DE SISTEMAS
- Habilitando o cache
- 9 minutos
- Link para tarefa: https://cursos.alura.com.br/course/spring-mvc-security-rest-vuejs-ajax/task/81138
- Habilitar o cache no Spring MVC permite armazenar temporariamente dados acessados com frequência, acelerando o carregamento ao evitar consultas repetidas ao banco. Isso otimiza o desempenho da aplicação.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 23

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje
- Aprendemos a implementar e configurar paginação e cache no Spring MVC, dividindo grandes listas de dados em páginas navegáveis e armazenando consultas em cache para otimizar o desempenho. Esses conceitos são essenciais para melhorar a experiência do usuário, garantindo uma navegação rápida e organizada mesmo com grandes volumes de dados.

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

_Fonte: AULA 111_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

ATIVIDADE AULA 111

Questão 1

Qual anotação é usada para habilitar o cache no Spring?

A) @CacheEnable

B) @EnableCaching

C) @CacheManager

D) @SpringCache

Resposta:

Resposta correta: B)

@EnableCaching habilita o uso de cache na aplicação Spring, otimizando o desempenho ao armazenar dados frequentemente consultados.

Questão 2

Como você pode definir a quantidade de itens por página na paginação do Spring MVC?

A) Usando PageRequest.of() com número de página e itens por página.

B) Configurando @Pageable diretamente no controlador.

C) Definindo @Cacheable na classe de configuração.

D) Usando @EnablePagination.

Resposta:

Resposta correta: A)

PageRequest.of() permite configurar a página atual e o número de itens por página, ajustando a navegação dos dados.
