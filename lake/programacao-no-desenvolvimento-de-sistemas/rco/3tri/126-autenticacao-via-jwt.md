---
titulo: "Autenticação via JWT"
tipo: rco-seed
disciplina: programacao-no-desenvolvimento-de-sistemas
sigla_rco: PDS
trimestre: 3
ordem_rco: 126
serie: 3
aula_rco: "Aula 126"
slides: 54
tem_atividade: false
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/3TRI/126-autenticacao-via-jwt/126-autenticacao-via-jwt(1).pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/3TRI/126-autenticacao-via-jwt/126-autenticacao-via-jwt.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/3TRI/126-autenticacao-via-jwt/AULA 126_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Autenticação via JWT

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO NO
- DESENVOLVIMENTO DE
- SISTEMAS
- 3ª SÉRIE
- Autenticação via JWT
- Aula 126

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
- Conhecer o processo de autenticação
- de usuários usando JWT em APIs REST.

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
- Aprendemos como gerar tokens JWT para autenticação Stateless. Você configurou o Spring Boot para emitir tokens e viu como retornar essas credenciais ao cliente.

_4 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Mariana está desenvolvendo uma API para um sistema de biblioteca online. Ela já implementou a geração de tokens JWT, mas agora precisa configurar a aplicação para validar os tokens e autenticar os usuários em cada requisição.

_4 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Pergunta
- Como Mariana pode configurar o Spring Security para recuperar, validar e autenticar usuários com base no token JWT?
- Quem sabe responde!

_5 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Ela deve configurar um filtro que intercepte as requisições, extraia o token do Header Authorization, validá-lo usando uma chave secreta e autenticar o cliente através do Spring Security.

_4 imagem(ns) no slide._

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- JWT (JSON Web Token) é um padrão para autenticação Stateless. Ele armazena informações em formato compactado e assinado, garantindo integridade e autenticidade.

_4 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- A autenticação via JWT é usada para validar o cliente em APIs REST. O processo inclui recuperar o token enviado pelo cliente, validá-lo e garantir o acesso seguro a recursos protegidos.

_4 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Com JWT, eliminamos a necessidade de sessões no servidor, escalando o sistema para atender a muitos clientes. Ele também é essencial para proteger dados sensíveis de APIs.

_4 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- APIs modernas utilizam JWT para autenticação em sistemas como redes sociais, e-commerce e bancos digitais. Cada requisição autenticada carrega o token para acessar recursos.

_4 imagem(ns) no slide._

### Slide 13

- DESENVOLVIMENTO DE SISTEMAS
- Exemplo
- Este código implementa um filtro que intercepta requisições HTTP, recupera o token JWT do header Authorization, valida o token e autentica o usuário no contexto de segurança do Spring.

_4 imagem(ns) no slide._

### Slide 14

- DESENVOLVIMENTO DE SISTEMAS
- Questão de fixação
- Qual o principal objetivo de validar um token JWT na API?
- A) Gerar novos tokens
- B) Garantir que apenas usuários autorizados acessem os recursos
- C) Armazenar dados no token
- D) Bloquear requisições não autenticadas
- Quem sabe responde!

_4 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- Resposta!
- Qual o principal objetivo de validar um token JWT na API?
- A) Gerar novos tokens
- B) Garantir que apenas usuários autorizados acessem os recursos
- C) Armazenar dados no token
- D) Bloquear requisições não autenticadas
- Resposta Correta: B)

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
- Recuperando o token do header Authorization
- 13 minutos
- Link para tarefa: https://cursos.alura.com.br/course/spring-boot-seguranca-cache-monitoramento/task/55848
- Recuperar o token do header Authorization é essencial para identificar e validar o usuário em APIs seguras. O token é extraído da requisição e usado para autenticar o cliente via Spring Security.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- Validando o token
- 9 minutos
- Link para tarefa: https://cursos.alura.com.br/course/spring-boot-seguranca-cache-monitoramento/task/55849
- A validação do token JWT garante sua autenticidade e integridade, verificando a assinatura e os dados como expiração. Isso assegura que apenas requisições legítimas possam acessar a API protegida.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- Autenticando o cliente via Spring Security
- 16 minutos
- Link para tarefa: https://cursos.alura.com.br/course/spring-boot-seguranca-cache-monitoramento/task/55850
- A autenticação do cliente via Spring Security utiliza o token JWT para validar a identidade do usuário, associando-o ao contexto de segurança da aplicação e permitindo acesso controlado a recursos protegidos.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 20

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje
- Aprendemos a recuperar tokens JWT do header Authorization, validá-los e autenticar clientes com Spring Security. Essa abordagem reforça a segurança das APIs REST, garantindo acesso controlado a recursos sensíveis.

_4 imagem(ns) no slide._

### Slide 21

_(sem texto)_

_1 imagem(ns) no slide._

### Slide 22

_(sem texto)_

_1 imagem(ns) no slide._

### Slide 23

- DESENVOLVIMENTO DE SISTEMAS
- Pronto para desbloquear sua carreira de TI?
- Está perdido estudando mas não sabe por onde começar? Se a resposta é sim, você está no lugar certo! Descubra as estratégias e ferramentas essenciais para te ajudar a desbloquear seu potencial em TI e buscar sua primeira vaga de emprego no setor!
- Este e-book é um guia completo para quem busca começar pelos melhores caminhos para se tornar um excelente profissional de TI, ensinando a identificar perfis profissionais, aplicar técnicas de estudo eficazes, transformar teoria em prática, e aumentar a visibilidade de seu trabalho no mercado de trabalho. Ideal para novatos e profissionais em transição.
- E o melhor, ele pode ser seu, inteiramente grátis!
- Basta clicar AQUI e realizar o seu cadastro com o seu @escola!

_5 imagem(ns) no slide._

### Slide 24

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

### Slide 25

- DESENVOLVIMENTO DE SISTEMAS
- Referências (Imagens)
- Figuras e Imagens:
- https://www.flaticon.com/br
- https://www.istockphoto.com/br
- https://raw.githubusercontent.com/zbtang/React-Native-ViewPager/HEAD/imgs/dotIndicator.gif
- https://storyset.com

_3 imagem(ns) no slide._

### Slide 26

- DESENVOLVIMENTO DE SISTEMAS
- O RCO+Aulas é um projeto da Secretaria de Estado da Educação do Paraná e está em constante revisão. Todos os slides são de uso exclusivo dos professores da Rede Pública de Ensino, com a finalidade específica de aplicação em sala de aula, sendo totalmente vedada a publicização, reutilização, reprodução total ou parcial para quaisquer outros fins.

_4 imagem(ns) no slide._

### Slide 27

- DESENVOLVIMENTO DE SISTEMAS
- Esta publicação tem a cooperação entre a UNESCO e a Secretaria de Estado da Educação e do Esporte do Paraná no âmbito da parceria PRODOC 914BRZ1091, cujo objetivo é trazer soluções inovadoras de gestão da rede pública estadual de educação do Paraná para a melhoria da aprendizagem dos alunos. As indicações de nomes e a apresentação do material ao longo desta publicação não implicam a manifestação de qualquer opinião por parte da UNESCO a respeito da condição jurídica de qualquer país, território, cidade, região ou de suas autoridades, tampouco da delimitação de suas fronteiras ou limites As ideias e opiniões expressas nesta publicação são as dos autores e não refletem obrigatoriamente as da UNESCO nem comprometem a Organização.
- Cooperação Técnica

_5 imagem(ns) no slide._

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO NO
- DESENVOLVIMENTO DE
- SISTEMAS
- 3ª SÉRIE
- Autenticação via JWT
- Aula 126

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
- Conhecer o processo de autenticação
- de usuários usando JWT em APIs REST.

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
- Aprendemos como gerar tokens JWT para autenticação Stateless. Você configurou o Spring Boot para emitir tokens e viu como retornar essas credenciais ao cliente.

_4 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Mariana está desenvolvendo uma API para um sistema de biblioteca online. Ela já implementou a geração de tokens JWT, mas agora precisa configurar a aplicação para validar os tokens e autenticar os usuários em cada requisição.

_4 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Pergunta
- Como Mariana pode configurar o Spring Security para recuperar, validar e autenticar usuários com base no token JWT?
- Quem sabe responde!

_5 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Ela deve configurar um filtro que intercepte as requisições, extraia o token do Header Authorization, validá-lo usando uma chave secreta e autenticar o cliente através do Spring Security.

_4 imagem(ns) no slide._

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- JWT (JSON Web Token) é um padrão para autenticação Stateless. Ele armazena informações em formato compactado e assinado, garantindo integridade e autenticidade.

_4 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- A autenticação via JWT é usada para validar o cliente em APIs REST. O processo inclui recuperar o token enviado pelo cliente, validá-lo e garantir o acesso seguro a recursos protegidos.

_4 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Com JWT, eliminamos a necessidade de sessões no servidor, escalando o sistema para atender a muitos clientes. Ele também é essencial para proteger dados sensíveis de APIs.

_4 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- APIs modernas utilizam JWT para autenticação em sistemas como redes sociais, e-commerce e bancos digitais. Cada requisição autenticada carrega o token para acessar recursos.

_4 imagem(ns) no slide._

### Slide 13

- DESENVOLVIMENTO DE SISTEMAS
- Exemplo
- Este código implementa um filtro que intercepta requisições HTTP, recupera o token JWT do header Authorization, valida o token e autentica o usuário no contexto de segurança do Spring.

_4 imagem(ns) no slide._

### Slide 14

- DESENVOLVIMENTO DE SISTEMAS
- Questão de fixação
- Qual o principal objetivo de validar um token JWT na API?
- A) Gerar novos tokens
- B) Garantir que apenas usuários autorizados acessem os recursos
- C) Armazenar dados no token
- D) Bloquear requisições não autenticadas
- Quem sabe responde!

_4 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- Resposta!
- Qual o principal objetivo de validar um token JWT na API?
- A) Gerar novos tokens
- B) Garantir que apenas usuários autorizados acessem os recursos
- C) Armazenar dados no token
- D) Bloquear requisições não autenticadas
- Resposta Correta: B)

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
- Recuperando o token do header Authorization
- 13 minutos
- Link para tarefa: https://cursos.alura.com.br/course/spring-boot-seguranca-cache-monitoramento/task/55848
- Recuperar o token do header Authorization é essencial para identificar e validar o usuário em APIs seguras. O token é extraído da requisição e usado para autenticar o cliente via Spring Security.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- Validando o token
- 9 minutos
- Link para tarefa: https://cursos.alura.com.br/course/spring-boot-seguranca-cache-monitoramento/task/55849
- A validação do token JWT garante sua autenticidade e integridade, verificando a assinatura e os dados como expiração. Isso assegura que apenas requisições legítimas possam acessar a API protegida.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- Autenticando o cliente via Spring Security
- 16 minutos
- Link para tarefa: https://cursos.alura.com.br/course/spring-boot-seguranca-cache-monitoramento/task/55850
- A autenticação do cliente via Spring Security utiliza o token JWT para validar a identidade do usuário, associando-o ao contexto de segurança da aplicação e permitindo acesso controlado a recursos protegidos.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 20

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje
- Aprendemos a recuperar tokens JWT do header Authorization, validá-los e autenticar clientes com Spring Security. Essa abordagem reforça a segurança das APIs REST, garantindo acesso controlado a recursos sensíveis.

_4 imagem(ns) no slide._

### Slide 21

_(sem texto)_

_1 imagem(ns) no slide._

### Slide 22

_(sem texto)_

_1 imagem(ns) no slide._

### Slide 23

- DESENVOLVIMENTO DE SISTEMAS
- Pronto para desbloquear sua carreira de TI?
- Está perdido estudando mas não sabe por onde começar? Se a resposta é sim, você está no lugar certo! Descubra as estratégias e ferramentas essenciais para te ajudar a desbloquear seu potencial em TI e buscar sua primeira vaga de emprego no setor!
- Este e-book é um guia completo para quem busca começar pelos melhores caminhos para se tornar um excelente profissional de TI, ensinando a identificar perfis profissionais, aplicar técnicas de estudo eficazes, transformar teoria em prática, e aumentar a visibilidade de seu trabalho no mercado de trabalho. Ideal para novatos e profissionais em transição.
- E o melhor, ele pode ser seu, inteiramente grátis!
- Basta clicar AQUI e realizar o seu cadastro com o seu @escola!

_5 imagem(ns) no slide._

### Slide 24

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

### Slide 25

- DESENVOLVIMENTO DE SISTEMAS
- Referências (Imagens)
- Figuras e Imagens:
- https://www.flaticon.com/br
- https://www.istockphoto.com/br
- https://raw.githubusercontent.com/zbtang/React-Native-ViewPager/HEAD/imgs/dotIndicator.gif
- https://storyset.com

_3 imagem(ns) no slide._

### Slide 26

- DESENVOLVIMENTO DE SISTEMAS
- O RCO+Aulas é um projeto da Secretaria de Estado da Educação do Paraná e está em constante revisão. Todos os slides são de uso exclusivo dos professores da Rede Pública de Ensino, com a finalidade específica de aplicação em sala de aula, sendo totalmente vedada a publicização, reutilização, reprodução total ou parcial para quaisquer outros fins.

_4 imagem(ns) no slide._

### Slide 27

- DESENVOLVIMENTO DE SISTEMAS
- Esta publicação tem a cooperação entre a UNESCO e a Secretaria de Estado da Educação e do Esporte do Paraná no âmbito da parceria PRODOC 914BRZ1091, cujo objetivo é trazer soluções inovadoras de gestão da rede pública estadual de educação do Paraná para a melhoria da aprendizagem dos alunos. As indicações de nomes e a apresentação do material ao longo desta publicação não implicam a manifestação de qualquer opinião por parte da UNESCO a respeito da condição jurídica de qualquer país, território, cidade, região ou de suas autoridades, tampouco da delimitação de suas fronteiras ou limites As ideias e opiniões expressas nesta publicação são as dos autores e não refletem obrigatoriamente as da UNESCO nem comprometem a Organização.
- Cooperação Técnica

_5 imagem(ns) no slide._

## Outros documentos

_Fonte: AULA 126_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

ATIVIDADE AULA 126

Questão 1

Qual classe no Spring é usada para interceptar requisições e validar tokens JWT?

A) AuthenticationManager

B) JwtFilter

C) SecurityContext

D) RestController

Resposta Correta: B) JwtFilter.

Questão 2

O que acontece se o token JWT expirar durante uma requisição?

A) O servidor gera um novo token automaticamente

B) A requisição é negada com um erro 401

C) O servidor ignora o token

D) O token é atualizado no cache

Resposta Correta: B) A requisição é negada com um erro 401.
