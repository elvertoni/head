---
titulo: "Formulário acessível Parte I"
tipo: rco-seed
disciplina: programacao-front-end
sigla_rco: PFE
trimestre: 3
ordem_rco: 1002
serie: 2
aula_rco: "Aula NIVELAMENTO 2"
slides: 23
tem_atividade: false
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/3TRI/1002-formulario-acessivel-parte-i/1002-formulario-acessivel-parte-i.pptx"
extrator: tools/extrair_rco.py
status: bruto
---

# Formulário acessível Parte I

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- Programação Front-End
- 2ª Série
- Formulário acessível Parte I
- Aula NIVELAMENTO 2

_1 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- COMPETÊNCIA(S) A SER(EM) DESENVOLVIDA(S) NESTA AULA:
- De acordo com o Plano de Curso de Desenvolvimento de Sistemas:
- HABILIDADE(S) A SER(EM) DESENVOLVIDA(S) NESTA AULA:
- Desenvolver interfaces gráficas para aplicações computacionais.
- Aplicar boas práticas de acessibilidade em interfaces web.

_1 imagem(ns) no slide._

### Slide 4

- Nesta aula vamos:
- Compreender acessibilidade a formulários em páginas HTML Parte I.
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store

_4 imagem(ns) no slide._

### Slide 5 (oculto)

- Este material foi elaborado a partir da análise do plano de curso e reúne os conhecimentos essenciais para o Técnico em Desenvolvimento de Sistemas. As aulas foram organizadas com foco na clareza conceitual, na construção gradual dos conteúdos e na utilização de metodologias ativas que favorecem a compreensão, a participação e o desenvolvimento de habilidades e competências de forma significativa.
- De acordo com a matriz curricular do Curso Técnico em Desenvolvimento de Sistemas, que traz em sua essência componentes estruturados para a realização de aulas práticas, cada unidade curricular deve contemplar, além da abordagem teórica, uma proposta de atividade prática a ser desenvolvida pelo professor. Essa orientação assegura a coerência entre o planejamento didático e o que está estabelecido na matriz, promovendo experiências formativas alinhadas ao perfil profissional previsto.
- O professor tem total autonomia para adaptar o conteúdo conforme o contexto da turma, ajustando exemplos, aprofundamentos e estratégias didáticas para otimizar a aprendizagem e a conexão com a prática profissional.
- Se houver falta de conexão ou indisponibilidade de internet durante a aula, os materiais abaixo podem ser utilizados como apoio para elaborar recursos complementares, garantindo a continuidade da abordagem teórica prevista.
- ATENÇÃO PROFESSOR!
- http://www.reinaldoferraz.com.br/acessibilidade-seo-e-svg/
- Lang e Alt:
- https://cursos.alura.com.br/course/acessibilidade-web-front-end/task/36282
- Projeto aula anterior:
- https://github.com/designernatan/curso-acessibilidade-web-front-end-1/archive/74572c8c9f74bcef090239aef30debe31bfeb532.zip

_2 imagem(ns) no slide._

### Slide 6

- Aula anterior
- Concluímos os estudos sobre navegação em páginas HTML via teclado, sua importância para a acessibilidade.

_1 imagem(ns) no slide._

### Slide 7

- Para pensarmos juntos...
- Vamos considerar a situação de Maria. Maria é uma desenvolvedora web iniciante que foi incumbida de criar um formulário de inscrição para um evento online. Após finalizar a tarefa, ela decidiu testar o formulário com o auxílio de um leitor de tela para verificar a acessibilidade.

_1 imagem(ns) no slide._

### Slide 8

- Para pensarmos juntos...
- Enquanto testava, ela notou que o leitor de tela não anunciava os campos de entrada do formulário de maneira correta, tornando confuso o entendimento do que era necessário para preencher cada campo. Ela ficou confusa e se perguntou: "Por que o leitor de tela não está lendo corretamente os rótulos dos campos de entrada?"
- Pesquisem e apresentem suas versões
- https://cryptoid.com.br/wp-content/uploads/2018/01/iStock-838172306.jpg

_2 imagem(ns) no slide._

### Slide 9

- Resposta
- A resposta é que Maria esqueceu de ligar os rótulos dos campos de entrada aos respectivos elementos de entrada através do uso do atributo 'for' em tags <label>. Quando a tag <label> é usada corretamente, ela fornece uma descrição para o campo de entrada correspondente, o que é essencial para que os leitores de tela possam interpretar e anunciar corretamente os campos de entrada para os usuários.

_1 imagem(ns) no slide._

### Slide 10

- Resposta
- Portanto, Maria precisa corrigir esse problema, associando cada <label> ao campo de entrada correspondente, para melhorar a acessibilidade do seu formulário.

_1 imagem(ns) no slide._

### Slide 11

- Conceituando
- A acessibilidade em formulários HTML é de extrema importância para garantir a inclusão digital e proporcionar uma experiência de usuário satisfatória para todos, incluindo pessoas com deficiências. Formulários são elementos comuns em websites, usados para uma série de funções, como coletar informações de contato, realizar pesquisas e receber feedback.
- https://www.al.sp.gov.br/repositorio/noticia/N-03-2021/fg263796.jpg

_1 imagem(ns) no slide._

### Slide 12

- Conceituando
- Formulários acessíveis garantem que todas as pessoas, independente de suas habilidades ou limitações, possam interagir de maneira eficaz com o site. Isso envolve garantir que o formulário possa ser facilmente navegado e preenchido usando apenas o teclado, um aspecto crucial para usuários com deficiências motoras ou visual.
- https://www.deficienteciente.com.br/nova-tecnologia-ajuda-deficientes-auditivos-a-usar-o-computador.html

_1 imagem(ns) no slide._

### Slide 13

- Conceituando
- Outro ponto fundamental para a acessibilidade é garantir que todos os elementos do formulário sejam claramente rotulados e possam ser lidos por leitores de tela. Isso significa usar corretamente os elementos e atributos HTML, como rótulos (<label>) ligados explicitamente aos campos de entrada e fornecer descrições de texto alternativo para quaisquer elementos visuais.

_1 imagem(ns) no slide._

### Slide 14

- Conceituando
- Além disso, é importante fornecer feedback claro e imediato quando os usuários cometem erros ao preencher o formulário. Mensagens de erro devem ser claramente associadas aos campos de entrada relevantes e devem ser comunicadas de maneira eficaz a leitores de tela e outras tecnologias assistivas.
- https://classic.exame.com/wp-content/uploads/2022/11/pessoa-deficiencia-acessibilidade.jpg?quality=70&strip=info&w=1024

_1 imagem(ns) no slide._

### Slide 15

- Conceituando
- Finalmente, ter formulários acessíveis não é apenas uma questão de inclusão e ética, mas também tem benefícios práticos e legais. A acessibilidade pode melhorar a experiência do usuário para todos, não apenas para pessoas com deficiência, e em muitas jurisdições, a acessibilidade na web é uma exigência legal. Portanto, priorizar a acessibilidade é uma prática recomendada para todos os desenvolvedores web.
- https://www.deficienteciente.com.br/nova-tecnologia-ajuda-deficientes-auditivos-a-usar-o-computador.html

_1 imagem(ns) no slide._

### Slide 16

- Ainda sobre acessibilidade, vamos conhecer praticando?
- Na plataforma Alura, vamos acessar o seguinte curso:
- Link para o curso: https://cursos.alura.com.br/course/acessibilidade-web-front-end
- Ao longo das atividades, você vai encontrar alguns quizzes e eles não estão ali por acaso! Eles são oportunidades rápidas para testar seu entendimento, reforçar o que aprendeu e identificar pontos que ainda podem melhorar.

_2 imagem(ns) no slide._

### Slide 17

- Formulário acessível
- 8 minutos
- Um formulário acessível é projetado com inclusão em mente.
- Link para tarefa: https://cursos.alura.com.br/course/acessibilidade-web-front-end/task/36249
- Ele apresenta elementos como rótulos associados explicitamente a campos de entrada, mensagens de erro claramente comunicadas, e campos de entrada que são navegáveis e interativos através do teclado. Além disso, assegura-se de que seja compatível com leitores de tela, garantindo que todas as pessoas, incluindo aquelas com deficiências, possam usá-lo sem problemas.
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 18

- Zoom no celular
- 4 minutos
- Ao abrirmos o site Apeperia em nosso navegador Firefox conseguimos facilmente diminuir e aumentar o zoom da página.
- Link para tarefa: https://cursos.alura.com.br/course/acessibilidade-web-front-end/task/36250
- Em um celular, para realizarmos um zoom fazemos um movimento de pinça com os dedos na superfície da tela. Quando testamos nosso site no mobile, não conseguimos realizar o zoom. Nessa aula vamos verificar em nosso código o porquê isso ocorre.
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 19

- Vamos praticar?
- Prepare-se, porque nessa atividade, você vai sair do modo aprender e entrar direto no modo praticar.
- A atividade prática vai colocar você diante de um desafio real, que faz relação com o conteúdo aprendido até aqui.

_1 imagem(ns) no slide._

### Slide 20

- O que vimos na aula de hoje:
- Aprendemos a importância de termos formulários acessíveis em nossos sistemas ou websites em HTML.

_1 imagem(ns) no slide._

### Slide 21

- Pronto para desbloquear sua carreira de TI?
- Está perdido estudando mas não sabe por onde começar? Se a resposta é sim, você está no lugar certo! Descubra as estratégias e ferramentas essenciais para te ajudar a desbloquear seu potencial em TI e buscar sua primeira vaga de emprego no setor!
- Este e-book é um guia completo para quem busca começar pelos melhores caminhos para se tornar um excelente profissional de TI, ensinando a identificar perfis profissionais, aplicar técnicas de estudo eficazes, transformar teoria em prática, e aumentar a visibilidade de seu trabalho no mercado de trabalho. Ideal para novatos e profissionais em transição.
- E o melhor, ele pode ser seu, inteiramente grátis!
- Basta clicar AQUI e realizar o seu cadastro com o seu @escola!

_3 imagem(ns) no slide._

### Slide 22

- Referências
- BEAULIEU, Alan. SQL: Guia Prático Para Manipulação de Dados. São Paulo: O'Reilly, 2008.
- CHACON, Scott; STRAUB, Ben. Pro Git. 2ª ed. Berkeley: Apress, 2014.
- DELISLE, Marc. MySQL: Guia do Programador. São Paulo: Novatec, 2010.
- FURGERI, Sérgio. SQL - Curso Prático. São Paulo: Novatec, 2018.
- LOELIGER, Jon; MCCULLOUGH, Matthew. Version Control with Git: Powerful Tools and Techniques for Collaborative Software Development. 2ª ed. Sebastopol: O'Reilly Media, 2012.
- SAMPAIO, Cleuton. Banco de Dados SQL: Aprenda a Construir um Banco de Dados do Zero. São Paulo: Novatec, 2018.
- SANTOS, Rafael. Administração de Banco de Dados: SQL Server 2017. São Paulo: Novatec, 2018.
- SILVERMAN, Richard E. Git Pocket Guide: A Working Introduction. Sebastopol: O'Reilly Media, 2013.
- STANEK, William. SQL Server 2019: Guia Completo do Administrador de Banco de Dados. São Paulo: Novatec, 2019.
- Figuras e Imagens:
- https://www.flaticon.com/br
- https://www.istockphoto.com/br
- https://raw.githubusercontent.com/zbtang/React-Native-ViewPager/HEAD/imgs/dotIndicator.gif
- https://storyset.com

### Slide 23

_(sem texto)_
