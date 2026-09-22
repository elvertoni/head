---
titulo: "Melhorando desempenho com Spring Cache"
tipo: rco-seed
disciplina: programacao-no-desenvolvimento-de-sistemas
sigla_rco: PDS
trimestre: 3
ordem_rco: 123
serie: 3
aula_rco: "Aula 123"
slides: 54
tem_atividade: false
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/3TRI/123-melhorando-desempenho-com-spring-cache/123-melhorando-desempenho-com-spring-cache(1).pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/3TRI/123-melhorando-desempenho-com-spring-cache/123-melhorando-desempenho-com-spring-cache.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/3TRI/123-melhorando-desempenho-com-spring-cache/AULA 123_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Melhorando desempenho com Spring Cache

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO NO
- DESENVOLVIMENTO DE
- SISTEMAS
- 3ª SÉRIE
- Melhorando desempenho com Spring Cache
- Aula 123

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
- Compreender como o cache pode melhorar significativamente o desempenho de APIs REST.

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
- Aprendemos a implementar paginação e ordenação em APIs REST, simplificando o acesso a grandes volumes de dados e organizando respostas de forma eficiente para o usuário.

_4 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Mariana está gerenciando uma API REST que atende milhares de requisições diárias. Ela percebe que algumas consultas, como listagens completas, estão ficando lentas e prejudicando a experiência do usuário.

_4 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Pergunta
- Como Mariana pode melhorar a performance da API sem alterar drasticamente o código?
- Quem sabe responde!

_5 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Mariana pode implementar caching para armazenar resultados frequentes, reduzindo consultas repetidas ao banco de dados e otimizando o tempo de resposta.

_4 imagem(ns) no slide._

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- O Spring Cache é uma ferramenta que armazena respostas de APIs ou consultas em memória ou sistemas como Redis. Isso reduz a carga do banco de dados e melhora o desempenho.

_4 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- Caching consiste em salvar temporariamente informações que serão frequentemente acessadas, para evitar processamentos repetidos.
- No Spring Boot, o cache é configurado com anotações simples, como @Cacheable.

_4 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Importância
- APIs rápidas garantem melhor experiência para o usuário e otimizam recursos do servidor. O cache evita gargalos de performance em cenários com alta demanda de dados.

_6 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- Imagine uma API de produtos
- em uma loja online.
- A lista de produtos raramente muda, então, ao invés de consultar o banco em todas as requisições, você armazena a lista em cache.

_4 imagem(ns) no slide._

### Slide 13

- DESENVOLVIMENTO DE SISTEMAS
- Exemplo
- No método para listar tópicos
- Para invalidar o cache quando algo for atualizado

_5 imagem(ns) no slide._

### Slide 14

- DESENVOLVIMENTO DE SISTEMAS
- Questão de fixação
- O que faz a anotação @Cacheable em uma API Spring Boot?
- A. Salva resultados de consultas frequentemente usados.
- B. Atualiza o banco de dados automaticamente.
- C. Bloqueia acessos concorrentes.
- D. Gera logs de performance.
- Quem sabe responde!

_4 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- Resposta!
- O que faz a anotação @Cacheable em uma API Spring Boot?
- A. Salva resultados de consultas frequentemente usados.
- B. Atualiza o banco de dados automaticamente.
- C. Bloqueia acessos concorrentes.
- D. Gera logs de performance.
- Resposta: A

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
- Utilizando cache
- 11 minutos
- Link para tarefa: https://cursos.alura.com.br/course/spring-boot-seguranca-cache-monitoramento/task/55837
- Utilizar cache em APIs REST com Spring Boot melhora o desempenho, armazenando resultados de consultas frequentes em memória. Isso reduz o acesso ao banco de dados e acelera a resposta às requisições.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- Invalidando o cache
- 8 minutos
- Link para tarefa: https://cursos.alura.com.br/course/spring-boot-seguranca-cache-monitoramento/task/55838
- Invalidar o cache garante que os dados armazenados em memória sejam atualizados após alterações. Em Spring Boot, isso pode ser feito com @CacheEvict, removendo entradas específicas ou todo o cache.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- Boas práticas no uso de cache
- 4 minutos
- Link para tarefa: https://cursos.alura.com.br/course/spring-boot-seguranca-cache-monitoramento/task/55839
- Utilize cache para dados estáticos ou acessados frequentemente. Evite armazenar informações sensíveis e defina TTL (Time to Live) adequado. Monitore o desempenho para evitar impactos negativos no sistema.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 20

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje
- Aprendemos como o cache melhora o desempenho de APIs REST ao armazenar resultados temporários, reduzindo a carga do banco de dados. Exploramos práticas como invalidar e simplificar o uso de cache no Spring Boot.

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
- Melhorando desempenho com Spring Cache
- Aula 123

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
- Compreender como o cache pode melhorar significativamente o desempenho de APIs REST.

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
- Aprendemos a implementar paginação e ordenação em APIs REST, simplificando o acesso a grandes volumes de dados e organizando respostas de forma eficiente para o usuário.

_4 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Mariana está gerenciando uma API REST que atende milhares de requisições diárias. Ela percebe que algumas consultas, como listagens completas, estão ficando lentas e prejudicando a experiência do usuário.

_4 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Pergunta
- Como Mariana pode melhorar a performance da API sem alterar drasticamente o código?
- Quem sabe responde!

_5 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Mariana pode implementar caching para armazenar resultados frequentes, reduzindo consultas repetidas ao banco de dados e otimizando o tempo de resposta.

_4 imagem(ns) no slide._

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- O Spring Cache é uma ferramenta que armazena respostas de APIs ou consultas em memória ou sistemas como Redis. Isso reduz a carga do banco de dados e melhora o desempenho.

_4 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- Caching consiste em salvar temporariamente informações que serão frequentemente acessadas, para evitar processamentos repetidos.
- No Spring Boot, o cache é configurado com anotações simples, como @Cacheable.

_4 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Importância
- APIs rápidas garantem melhor experiência para o usuário e otimizam recursos do servidor. O cache evita gargalos de performance em cenários com alta demanda de dados.

_6 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- Imagine uma API de produtos
- em uma loja online.
- A lista de produtos raramente muda, então, ao invés de consultar o banco em todas as requisições, você armazena a lista em cache.

_4 imagem(ns) no slide._

### Slide 13

- DESENVOLVIMENTO DE SISTEMAS
- Exemplo
- No método para listar tópicos
- Para invalidar o cache quando algo for atualizado

_5 imagem(ns) no slide._

### Slide 14

- DESENVOLVIMENTO DE SISTEMAS
- Questão de fixação
- O que faz a anotação @Cacheable em uma API Spring Boot?
- A. Salva resultados de consultas frequentemente usados.
- B. Atualiza o banco de dados automaticamente.
- C. Bloqueia acessos concorrentes.
- D. Gera logs de performance.
- Quem sabe responde!

_4 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- Resposta!
- O que faz a anotação @Cacheable em uma API Spring Boot?
- A. Salva resultados de consultas frequentemente usados.
- B. Atualiza o banco de dados automaticamente.
- C. Bloqueia acessos concorrentes.
- D. Gera logs de performance.
- Resposta: A

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
- Utilizando cache
- 11 minutos
- Link para tarefa: https://cursos.alura.com.br/course/spring-boot-seguranca-cache-monitoramento/task/55837
- Utilizar cache em APIs REST com Spring Boot melhora o desempenho, armazenando resultados de consultas frequentes em memória. Isso reduz o acesso ao banco de dados e acelera a resposta às requisições.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- Invalidando o cache
- 8 minutos
- Link para tarefa: https://cursos.alura.com.br/course/spring-boot-seguranca-cache-monitoramento/task/55838
- Invalidar o cache garante que os dados armazenados em memória sejam atualizados após alterações. Em Spring Boot, isso pode ser feito com @CacheEvict, removendo entradas específicas ou todo o cache.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- Boas práticas no uso de cache
- 4 minutos
- Link para tarefa: https://cursos.alura.com.br/course/spring-boot-seguranca-cache-monitoramento/task/55839
- Utilize cache para dados estáticos ou acessados frequentemente. Evite armazenar informações sensíveis e defina TTL (Time to Live) adequado. Monitore o desempenho para evitar impactos negativos no sistema.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 20

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje
- Aprendemos como o cache melhora o desempenho de APIs REST ao armazenar resultados temporários, reduzindo a carga do banco de dados. Exploramos práticas como invalidar e simplificar o uso de cache no Spring Boot.

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

_Fonte: AULA 123_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

ATIVIDADE AULA 123

Questão 1

Qual o principal benefício do uso de cache?

A. Reduz o tamanho do banco de dados.

B. Melhora o tempo de resposta da aplicação.

C. Garante a segurança da API.

D. Facilita a configuração de rotas.

Resposta: B. Explicação: Cache armazena resultados temporários, acelerando consultas frequentes.

Questão 2

O que acontece se o cache não for invalidado corretamente?

A. A API pode retornar dados desatualizados.

B. O servidor não salva as informações.

C. O banco de dados será bloqueado.

D. O cache será excluído automaticamente.

Resposta: A. Explicação: Dados desatualizados no cache podem causar inconsistências.
