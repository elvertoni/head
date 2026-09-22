---
titulo: "Proteção com Spring Security"
tipo: rco-seed
disciplina: programacao-no-desenvolvimento-de-sistemas
sigla_rco: PDS
trimestre: 3
ordem_rco: 124
serie: 3
aula_rco: "Aula 124"
slides: 27
tem_atividade: false
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/3TRI/124-protecao-com-spring-security/124-protecao-com-spring-security.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/3TRI/124-protecao-com-spring-security/AULA 124_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Proteção com Spring Security

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO NO
- DESENVOLVIMENTO DE
- SISTEMAS
- 3ª SÉRIE
- Proteção com Spring Security
- Aula 124

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
- Aprender como configurar e utilizar o Spring Security para proteger APIs REST

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
- Vimos como usar Spring Cache para melhorar o desempenho das aplicações. Aprendemos a configurar o cache, invalidá-lo de forma estratégica e seguir boas práticas para otimizar os resultados.

_4 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Carolina está desenvolvendo uma API para sua escola. Ela precisa garantir que apenas administradores possam cadastrar alunos, enquanto informações públicas devem ser acessíveis por qualquer pessoa.

_4 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Pergunta
- Como Carolina pode configurar sua API com Spring Security para atender a esses requisitos?
- Quem sabe responde!

_5 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Carolina pode habilitar o Spring Security, definir permissões para endpoints públicos e privados, e configurar autenticação para usuários administradores, utilizando anotações como @EnableWebSecurity e regras em HttpSecurity.

_4 imagem(ns) no slide._

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- Spring Security é uma ferramenta para proteger APIs e aplicações Java. Ela gerencia autenticação e autorização de maneira robusta, garantindo acesso controlado aos recursos.

_4 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- Definição e Aplicação
- Habilitando o Spring Security: Ative com @EnableWebSecurity.
- Liberando Acessos Públicos: Configure permissões para endpoints com permitAll().
- Restringindo Acessos Privados: Use authenticated() e roles para limitar acesso.
- Autenticando Usuários: Configure usuários e credenciais em memória ou banco de dados.

_3 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- A segurança de dados é crítica em qualquer sistema. Proteger endpoints evita acessos não autorizados, protege informações sensíveis e mantém a integridade da aplicação.

_4 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- Um sistema de gerenciamento escolar pode liberar acesso público à lista de cursos e proteger as informações dos alunos. A autenticação garante que apenas funcionários autorizados possam realizar edições.

_4 imagem(ns) no slide._

### Slide 13

- DESENVOLVIMENTO DE SISTEMAS
- Exemplo
- Metódo para configuração de proteção

_4 imagem(ns) no slide._

### Slide 14

- DESENVOLVIMENTO DE SISTEMAS
- Questão de fixação
- Qual a anotação para habilitar o Spring Security?
- A) @SpringBootApplication
- B) @EnableWebSecurity
- C) @EnableSpringSecurity
- D) @EnableSecurity
- Quem sabe responde!

_4 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- Resposta!
- Qual a anotação para habilitar o Spring Security?
- A) @SpringBootApplication
- B) @EnableWebSecurity
- C) @EnableSpringSecurity
- D) @EnableSecurity
- Resposta Correta: B

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
- Habilitando o Spring Security
- 6 minutos
- Link para tarefa: https://cursos.alura.com.br/course/spring-boot-seguranca-cache-monitoramento/task/55840
- Habilitar o Spring Security é essencial para proteger aplicações. Use @EnableWebSecurity para configurar a segurança e gerenciar autenticação e autorização, assegurando controle sobre acessos aos recursos.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- Liberando acesso aos endpoints públicos
- 10 minutos
- Link para tarefa: https://cursos.alura.com.br/course/spring-boot-seguranca-cache-monitoramento/task/55841
- Liberar acesso a endpoints públicos é crucial para recursos abertos, como login ou páginas iniciais. No Spring Security, configure as regras em HttpSecurity com .permitAll(), garantindo acesso livre.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- Restringindo o acesso aos endpoints privados
- 11 minutos
- Link para tarefa: https://cursos.alura.com.br/course/spring-boot-seguranca-cache-monitoramento/task/55842
- Restringir acesso a endpoints privados é essencial para proteger dados sensíveis. No Spring Security, use .authenticated() ou roles específicas em HttpSecurity para limitar o acesso apenas a usuários autorizados.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 20

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje
- Aprendemos sobre o Spring Security para proteger APIs, liberando e restringindo acessos. Entendeu como autenticar usuários e aplicar boas práticas para garantir a segurança das aplicações.

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

_Fonte: AULA 124_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

ATIVIDADE AULA 124

Questão 1

Qual método do HttpSecurity é usado para autenticar todas as solicitações?

A) authenticated()

B) permitAll()

C) hasRole()

D) denyAll()

Resposta Correta: A. O método authenticated() exige autenticação para acessar o endpoint.

Questão 2

Para configurar autenticação básica, qual método é usado?

A) formLogin()

B) httpBasic()

C) csrf()

D) authorizeRequests()

Resposta Correta: B. O método httpBasic() configura autenticação básica.
