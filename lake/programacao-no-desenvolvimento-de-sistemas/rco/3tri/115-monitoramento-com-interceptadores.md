---
titulo: "Monitoramento com Interceptadores"
tipo: rco-seed
disciplina: programacao-no-desenvolvimento-de-sistemas
sigla_rco: PDS
trimestre: 3
ordem_rco: 115
serie: 3
aula_rco: "Aula 115"
slides: 26
tem_atividade: false
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/3TRI/115-monitoramento-com-interceptadores/115-monitoramento-com-interceptadores.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/3TRI/115-monitoramento-com-interceptadores/AULA 115_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Monitoramento com Interceptadores

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO NO
- DESENVOLVIMENTO DE
- SISTEMAS
- 3ª SÉRIE
- Monitoramento com Interceptadores
- Aula 115

_3 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- DESENVOLVIMENTO DE SISTEMAS
- Nesta aula, vamos:
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store
- Aprender como os interceptadores ajudam a monitorar e medir o tempo de processamento em aplicações.

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
- Exploramos como validar formulários com Vue.js, aplicando validadores e exibindo mensagens de erro em tempo real. Hoje, vamos além, monitorando as respostas de nossa aplicação e medindo o tempo de cada processo com interceptadores.

_4 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Lucas desenvolveu uma API para um e-commerce e quer entender quanto tempo cada requisição demora para ser processada, especialmente em datas de alta demanda. Ele precisa de uma maneira de medir o tempo de resposta de cada requisição para identificar e melhorar a performance.

_4 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Duas Soluções Possíveis:
- Usar Interceptadores para medir o tempo de cada requisição: Lucas pode implementar um interceptador para registrar o tempo inicial e final de cada requisição e, assim, calcular o tempo total.
- Revisar manualmente os tempos nas configurações do servidor: Lucas também poderia verificar diretamente no servidor, mas isso seria mais demorado e menos preciso, pois exige várias configurações externas.
- Quem sabe responde!

_6 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Os interceptadores oferecem uma maneira precisa e automatizada de monitorar o tempo de cada requisição diretamente no código, o que facilita o acompanhamento em tempo real.
- A verificação manual no servidor é trabalhosa, demorada e menos prática, pois depende de relatórios que não são gerados automaticamente em cada requisição.

_5 imagem(ns) no slide._

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- Os interceptadores são usados para monitorar e manipular requisições e respostas em aplicações, fornecendo controle adicional sobre processos.
- Em monitoramento, ajudam a medir tempos de resposta, identificando gargalos e otimizando o desempenho.

_4 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- Definição e Aplicação
- Introdução ao Interceptador
- Um interceptador é um recurso que captura o início e o fim de uma requisição HTTP. Ele pode adicionar lógica para registrar tempos e analisar respostas.
- Medindo o Tempo de Processamento
- Esse monitoramento ajuda a entender quanto tempo a aplicação leva para processar cada requisição. Ele é útil para verificar se o desempenho está dentro do esperado ou se precisa de ajustes.

_3 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Saber o tempo de processamento de uma aplicação é fundamental para oferecer uma experiência eficiente e garantir que os recursos do servidor sejam bem utilizados. Interceptadores são essenciais para detectar áreas que precisam de otimização e manter a aplicação responsiva.

_4 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- Em uma aplicação de streaming, interceptadores são usados para monitorar o tempo que o sistema leva para enviar dados de vídeos ao usuário. Isso ajuda a equipe de desenvolvimento a identificar e ajustar qualquer lentidão, garantindo que o streaming seja fluido.

_5 imagem(ns) no slide._

### Slide 13

- DESENVOLVIMENTO DE SISTEMAS
- Exemplo
- exemplo básico de implementação de um interceptador que mede o tempo de cada requisição, Criação do Interceptador

_4 imagem(ns) no slide._

### Slide 14

- DESENVOLVIMENTO DE SISTEMAS
- Exemplo
- exemplo básico de implementação de um interceptador que mede o tempo de cada requisição, Configuração do Interceptador no Spring

_4 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- Questão de fixação
- Qual é o principal objetivo de um interceptador em uma aplicação?
- A) Manipular apenas os dados de resposta.
- B) Monitorar e registrar informações sobre requisições e respostas.
- C) Alterar diretamente o HTML da aplicação.
- D) Definir regras de autenticação.
- Quem sabe responde!

_4 imagem(ns) no slide._

### Slide 16

- DESENVOLVIMENTO DE SISTEMAS
- Resposta!
- Qual é o principal objetivo de um interceptador em uma aplicação?
- A) Manipular apenas os dados de resposta.
- B) Monitorar e registrar informações sobre requisições e respostas.
- C) Alterar diretamente o HTML da aplicação.
- D) Definir regras de autenticação.
- Resposta correta: B)

_3 imagem(ns) no slide._

### Slide 17

- DESENVOLVIMENTO DE SISTEMAS
- Atividade Prática na Plataforma Alura
- Na plataforma Alura vamos acessar o seguinte curso:
- A recomendação é que você continue esse curso extraclasse, pois ele traz um conteúdo essencial para compreender sobre o referido tema.
- Link para o curso: https://cursos.alura.com.br/course/spring-mvc-security-rest-vuejs-ajax

_6 imagem(ns) no slide._

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- Recuperando valores com JavaScript
- 10 minutos
- Link para tarefa: https://cursos.alura.com.br/course/spring-mvc-security-rest-vuejs-ajax/task/81147
- Recuperar valores com JavaScript permite capturar dados inseridos em campos de formulários de forma dinâmica. Com Vue.js, o v-model facilita essa tarefa, sincronizando os valores diretamente com variáveis, o que agiliza a validação e manipulação de dados.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje
- Exploramos como usar interceptadores para monitorar o tempo de processamento de cada requisição em uma aplicação, criando uma maneira eficaz de medir a performance e identificar pontos de melhoria.
- Essas técnicas ajudam a garantir que a aplicação funcione de forma rápida e eficiente, o que é essencial para proporcionar uma experiência positiva aos usuários e otimizar o uso dos recursos do servidor.

_3 imagem(ns) no slide._

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

_5 imagem(ns) no slide._

## Outros documentos

_Fonte: AULA 115_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

ATIVIDADE AULA 115

Questão 1

Qual método do interceptador armazena o tempo de início da requisição?

A) preHandle

B) postHandle

C) afterCompletion

D) preCompletion

Resposta:

Resposta correta: A)

O método preHandle é responsável por armazenar o tempo de início da requisição, possibilitando o cálculo do tempo total no final.

Questão 2

Qual é a vantagem de medir o tempo de processamento com interceptadores?

A) Reduzir o tamanho do código.

B) Verificar a eficiência e identificar áreas de lentidão no sistema.

C) Aumentar o tráfego na rede.

D) Melhorar a estética da interface.

Resposta:

Resposta correta: B)

Medir o tempo de processamento permite verificar a eficiência da aplicação e identificar áreas de lentidão para futuras otimizações.
