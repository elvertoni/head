---
titulo: "Validação com Bean Validation"
tipo: rco-seed
disciplina: programacao-no-desenvolvimento-de-sistemas
sigla_rco: PDS
trimestre: 3
ordem_rco: 120
serie: 3
aula_rco: "Aula 120"
slides: 28
tem_atividade: false
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/3TRI/120-validacao-com-bean-validation/120-validacao-com-bean-validation.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/3TRI/120-validacao-com-bean-validation/AULA 120_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Validação com Bean Validation

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO NO
- DESENVOLVIMENTO DE
- SISTEMAS
- 3ª SÉRIE
- Validação com Bean Validation
- Aula 120

_3 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- DESENVOLVIMENTO DE SISTEMAS
- Nesta aula, vamos:
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store
- Exploraremos como validar dados recebidos em uma API REST usando Bean Validation.

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
- Entendemos o que são endpoints POST para cadastrar dados em uma API REST, utilizando DTOs e boas práticas. Hoje, avançaremos para validar os dados recebidos, garantindo a integridade e clareza do que é processado.

_4 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Lucas está desenvolvendo uma API para cadastro de eventos. Ele precisa garantir que os dados recebidos sejam válidos, como o título do evento não sendo vazio e a data no formato correto.

_4 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Pergunta
- Como Lucas pode usar Bean Validation no Spring Boot para validar automaticamente os dados recebidos no endpoint de cadastro?
- Quem sabe responde!

_5 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Lucas pode adicionar anotações de validação, como @NotBlank para campos obrigatórios ou @PastOrPresent para datas, diretamente no DTO. O Spring Boot verifica automaticamente os dados e retorna erros, caso estejam inválidos.

_4 imagem(ns) no slide._

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- Bean Validation é uma especificação do Java para validar dados de forma declarativa. Ele permite adicionar regras diretamente às classes de modelo ou DTO, facilitando a validação de dados recebidos em APIs REST.

_4 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- Aplicação
- Validações com Bean Validation: Permite aplicar validações, como garantir que um campo não seja vazio (@NotBlank), ou que números estejam dentro de um intervalo (@Min e @Max).
- Simplificando o JSON: Ao validar e organizar os dados recebidos, o JSON enviado e recebido na API torna-se mais legível e funcional.

_4 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Validar dados é crucial para evitar erros e garantir que apenas informações corretas sejam processadas. Isso aumenta a segurança e previne falhas na aplicação.

_4 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- Em uma API de cadastro de usuários, Bean Validation impede que registros sejam salvos com campos vazios, garantindo que todos os dados necessários estejam presentes e corretos.

_4 imagem(ns) no slide._

### Slide 13

- DESENVOLVIMENTO DE SISTEMAS
- Exemplo
- Criando o DTO com Validações

_4 imagem(ns) no slide._

### Slide 14

- DESENVOLVIMENTO DE SISTEMAS
- Exemplo
- Configurando o Endpoint com Validações

_4 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- Exemplo
- Testando com Postman
- Envie uma requisição POST para http://localhost:8080/eventos.
- Teste enviar um JSON com campos inválidos e observe as mensagens de erro retornadas.
- Exemplo de JSON inválido
- Erro retornado

_5 imagem(ns) no slide._

### Slide 16

- DESENVOLVIMENTO DE SISTEMAS
- Questão de fixação
- Qual é a principal função do Bean Validation em APIs REST?
- A) Melhorar o desempenho da aplicação.
- B) Validar automaticamente os dados recebidos na API.
- C) Criar interfaces gráficas interativas.
- D) Gerar relatórios de validação.
- Quem sabe responde!

_4 imagem(ns) no slide._

### Slide 17

- DESENVOLVIMENTO DE SISTEMAS
- Resposta!
- Qual é a principal função do Bean Validation em APIs REST?
- A) Melhorar o desempenho da aplicação.
- B) Validar automaticamente os dados recebidos na API.
- C) Criar interfaces gráficas interativas.
- D) Gerar relatórios de validação.
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
- Validações com Bean Validation
- 9 minutos
- Link para tarefa: https://cursos.alura.com.br/course/spring-boot-api-rest/task/55826
- As validações com Bean Validation automatizam a verificação de dados em APIs REST usando anotações como @NotBlank e @Size, garantindo que os dados enviados estejam corretos antes de serem processados.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 20

- DESENVOLVIMENTO DE SISTEMAS
- Simplificando o JSON
- 16 minutos
- Link para tarefa: https://cursos.alura.com.br/course/spring-boot-api-rest/task/55827
- Simplificar o JSON envolve estruturar dados claros e consistentes, reduzindo redundâncias. Usar DTOs e validações com Bean Validation garante que apenas informações relevantes e corretas sejam enviadas e recebidas.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 21

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje
- Aprendemos como usar o Bean Validation para validar dados em APIs REST Spring Boot, garantindo segurança e organização nos cadastros. Ao aplicar validações no DTO e testar com ferramentas como o Postman, podemos construir APIs robustas e confiáveis, essenciais para aplicações modernas.

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

_Fonte: AULA 120_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

ATIVIDADE AULA 120

Questão 1

Como Bean Validation simplifica a validação em APIs?

A) Eliminando a necessidade de validação no cliente.

B) Usando anotações que automatizam as validações diretamente nas classes.

C) Garantindo que o banco de dados fique vazio.

D) Criando interfaces gráficas automáticas.

Resposta:

Resposta correta: B)

O Bean Validation usa anotações para definir regras de validação, automatizando o processo e reduzindo o código manual.

Questão 2

Qual é o principal benefício de retornar mensagens de erro claras em validações?

A) Melhorar o SEO da aplicação.

B) Facilitar o uso e a correção de erros por parte do cliente.

C) Aumentar o tráfego da API.

D) Criar mais complexidade no código.

Resposta:

Resposta correta: B)

Mensagens claras ajudam o cliente a entender e corrigir erros, tornando a API mais amigável e confiável.
