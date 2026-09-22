---
titulo: "Monitoramento com Spring Boot Actuator"
tipo: rco-seed
disciplina: programacao-no-desenvolvimento-de-sistemas
sigla_rco: PDS
trimestre: 3
ordem_rco: 2003
serie: 3
aula_rco: "Aula Retomada 03"
slides: 26
tem_atividade: false
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/3TRI/2003-monitoramento-com-spring-boot-actuator/2003-monitoramento-com-spring-boot-actuator.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/3TRI/2003-monitoramento-com-spring-boot-actuator/AULA R3_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Monitoramento com Spring Boot Actuator

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO NO
- DESENVOLVIMENTO DE
- SISTEMAS
- 3ª SÉRIE
- Monitoramento com Spring Boot Actuator
- Aula Retomada 03

_3 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- DESENVOLVIMENTO DE SISTEMAS
- Nesta aula, vamos:
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store
- Configurar o Spring Boot Actuator
- para monitorar APIs REST.

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
- Vimos como autenticar clientes usando JWT. Aprendemos a recuperar tokens do header Authorization, validá-los e integrá-los ao Spring Security para proteger APIs.

_4 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Mariana é desenvolvedora de uma API de gestão de pedidos. A equipe de TI precisa monitorar as métricas, como tempo de resposta e uso de memória, para manter o sistema eficiente e seguro.

_4 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Pergunta
- Como Mariana pode monitorar as métricas da API de forma prática, centralizando dados e garantindo visibilidade contínua?
- Quem sabe responde!

_5 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Ela pode usar o
- Spring Boot Actuator
- para obter métricas da API e integrá-lo ao Spring Boot Admin para visualizar essas informações de forma centralizada, com alertas em tempo real.

_4 imagem(ns) no slide._

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- Spring Boot Actuator é uma ferramenta para monitoramento de métricas em aplicações Spring Boot. Quando combinado com Spring Boot Admin, permite uma visualização centralizada e prática.

_4 imagem(ns) no slide._

### Slide 10

- Definição e Aplicação
- Actuator expõe endpoints para monitorar e gerenciar a aplicação, como métricas de desempenho e informações de sistema.
- O Admin facilita o monitoramento de várias aplicações em um painel único.
- DESENVOLVIMENTO DE SISTEMAS

_4 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Importância
- Monitorar o desempenho é essencial para manter a saúde da aplicação, identificar gargalos e prevenir falhas. O Actuator e o Admin simplificam esse processo com dados ricos e centralizados.

_4 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- Organizações usam Actuator para obter métricas de memória, threads e tempo de resposta. O Admin centraliza essas métricas, permitindo ações rápidas em caso de problemas.

_4 imagem(ns) no slide._

### Slide 13

- DESENVOLVIMENTO DE SISTEMAS
- Exemplo
- Configurando Spring Boot Actuator
- Monitorando com Spring Boot Admin

_5 imagem(ns) no slide._

### Slide 14

- DESENVOLVIMENTO DE SISTEMAS
- Questão de fixação
- Qual a principal função do Spring Boot Actuator?
- A) Monitorar métricas e gerenciar endpoints.
- B) Realizar autenticação via JWT.
- C) Configurar segurança da aplicação.
- D) Gerenciar conexões com banco de dados.
- Quem sabe responde!

_4 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- Resposta!
- Qual a principal função do Spring Boot Actuator?
- A) Monitorar métricas e gerenciar endpoints.
- B) Realizar autenticação via JWT.
- C) Configurar segurança da aplicação.
- D) Gerenciar conexões com banco de dados.
- Resposta Correta: A)

_3 imagem(ns) no slide._

### Slide 16

- DESENVOLVIMENTO DE SISTEMAS
- Atividade Prática na Plataforma Alura
- Na plataforma Alura vamos acessar o seguinte curso:
- A recomendação é que você continue esse curso extraclasse, pois ele traz um conteúdo essencial para compreender sobre o referido tema.
- Link para o curso: https://cursos.alura.com.br/course/spring-boot-seguranca-cache-monitoramento

_6 imagem(ns) no slide._

### Slide 17

- DESENVOLVIMENTO DE SISTEMAS
- Monitoramento com Spring Boot Actuator
- 11 minutos
- Link para tarefa: https://cursos.alura.com.br/course/spring-boot-seguranca-cache-monitoramento/task/55851
- O Spring Boot Actuator permite monitorar e gerenciar aplicações por meio de endpoints como /health e /metrics. Ele fornece informações sobre o desempenho, estado da aplicação e métricas importantes.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- Conhecendo Spring Boot Admin
- 8 minutos
- Link para tarefa: https://cursos.alura.com.br/course/spring-boot-seguranca-cache-monitoramento/task/55852
- O Spring Boot Admin é uma ferramenta para monitorar múltiplas aplicações Spring Boot. Ele exibe métricas, logs e status em um painel centralizado, facilitando a gestão e o desempenho do sistema.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje
- Conhecemos o Spring Boot Actuator e o Spring Boot Admin para monitorar APIs REST. Exploramos como visualizar métricas e gerenciar o desempenho em um ambiente centralizado.

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

_Fonte: AULA R3_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

ATIVIDADE AULA RETOMADA 03

Questão 1

Qual endpoint do Spring Boot Actuator é usado para verificar o status da aplicação?

A) /metrics

B) /health

C) /info

D) /env

Resposta Correta:

B) /health

Comentário: O endpoint /health fornece informações sobre o status da aplicação, permitindo monitorar sua disponibilidade e funcionamento.

Questão 2

O que é necessário para habilitar o Spring Boot Admin em um projeto?

A) Adicionar dependências específicas no arquivo pom.xml ou build.gradle.

B) Configurar o banco de dados do Actuator.

C) Habilitar autenticação Stateless.

D) Criar um token JWT para cada usuário.

Resposta Correta:

A) Adicionar dependências específicas no arquivo pom.xml ou build.gradle.

Comentário: Para usar o Spring Boot Admin, é necessário incluir as dependências adequadas no projeto para configurar o servidor e os clientes.
