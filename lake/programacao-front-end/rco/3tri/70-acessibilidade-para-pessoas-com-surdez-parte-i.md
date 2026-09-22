---
titulo: "Acessibilidade para Pessoas com Surdez – Parte I"
tipo: rco-seed
disciplina: programacao-front-end
sigla_rco: PFE
trimestre: 3
ordem_rco: 70
serie: 2
aula_rco: "Aula 70"
slides: 23
tem_atividade: false
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/3TRI/70-acessibilidade-para-pessoas-com-surdez-parte-i/70-acessibilidade-para-pessoas-com-surdez-parte-i.pptx"
extrator: tools/extrair_rco.py
status: bruto
---

# Acessibilidade para Pessoas com Surdez – Parte I

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- Programação Front-End
- 2ª Série
- Acessibilidade para Pessoas com Surdez – Parte I
- Aula 70

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
- Compreender como atender a pessoas com capacidade auditiva reduzida.
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
- https://cursos.alura.com.br/course/acessibilidade-web-design-inclusivos/task/34010
- Projeto aula:
- https://www.figma.com/file/qfVRdijn8pPG6UVLkeXKs2/Apeperia-1-5-Autismo

_2 imagem(ns) no slide._

### Slide 6

- Aula anterior
- Concluímos os estudos sobre acessibilidade de formulários em páginas HTML com foco em autismo.

_1 imagem(ns) no slide._

### Slide 7

- Para pensarmos juntos...
- Carlos é um desenvolvedor front-end iniciante que está trabalhando em um site para uma conferência de tecnologia. O site contém vários vídeos de palestras de conferências anteriores, cada um com áudio relevante. Carlos recebeu um feedback de um usuário surdo que não foi capaz de aproveitar plenamente o conteúdo desses vídeos devido à falta de legendas.
- 3 minutos

_2 imagem(ns) no slide._

### Slide 8

- Para pensarmos juntos...
- O desafio de Carlos é: "Como posso tornar esses vídeos acessíveis para usuários surdos ou com deficiência auditiva?"
- 3 minutos
- Pesquise uma possível solução e apresente

_3 imagem(ns) no slide._

### Slide 9

- Resposta
- Carlos então realiza algumas pesquisas e descobre que a melhor maneira de tornar os vídeos acessíveis para esses usuários é através da adição de legendas. Ao adicionar legendas aos vídeos, Carlos está garantindo que os usuários surdos ou com deficiência auditiva possam entender o conteúdo do vídeo.

_1 imagem(ns) no slide._

### Slide 10

- Resposta
- Além disso, ele também percebe a necessidade de garantir que todas as notificações sonoras na página da web sejam acompanhadas por notificações visuais. Dessa forma, os usuários surdos não perderão informações importantes apenas porque não conseguem ouvir o som associado.

_1 imagem(ns) no slide._

### Slide 11

- Conceituando
- O conceito de acessibilidade no desenvolvimento front-end para pessoas surdas é uma parte vital da criação de um site ou aplicativo inclusivo e acessível. Aqui está uma explicação fácil de entender sobre isso:

_1 imagem(ns) no slide._

### Slide 12

- Conceituando
- O que é acessibilidade para surdos no front-end?: Acessibilidade para surdos no front-end refere-se ao design e desenvolvimento de páginas da web e aplicações que consideram a experiência de usuários com deficiência auditiva. Isso significa garantir que as informações não sejam transmitidas apenas por meio de áudio, mas também por texto ou imagens, permitindo que as pessoas com deficiência auditiva interajam e entendam o conteúdo de forma igual.

_1 imagem(ns) no slide._

### Slide 13

- Conceituando
- Por que é importante?: Cerca de 5% da população mundial tem deficiência auditiva, e eles utilizam a internet como qualquer outra pessoa. Tornar seu site ou aplicativo acessível para esse público não é apenas uma questão de direitos humanos, mas também pode expandir seu público e potencialmente melhorar seu desempenho no mercado.
- https://triangulo.dev/posts/paleta-de-cores-perfeita-para-seu-projeto/escala-de-cores-radix-colors-light.png

_1 imagem(ns) no slide._

### Slide 14

- Conceituando
- Como podemos fazer isso?: Existem muitas maneiras de tornar seu site ou aplicativo mais acessível para pessoas surdas. Algumas das mais comuns incluem: fornecer legendas para vídeos, transcrições para podcasts, e assegurar que todas as informações sonoras importantes também sejam apresentadas visualmente, como mensagens de erro em formulários, notificações, etc.

_1 imagem(ns) no slide._

### Slide 15

- Conceituando
- Existem padrões?: Sim, existem vários padrões e diretrizes para a acessibilidade na web, incluindo as Diretrizes de Acessibilidade para Conteúdo Web (WCAG) do W3C. Essas diretrizes fornecem uma estrutura para tornar o conteúdo da web mais acessível para pessoas com várias deficiências, incluindo a deficiência auditiva.

_6 imagem(ns) no slide._

### Slide 16

- Conceituando
- Considerações finais: Em resumo, a acessibilidade para surdos no front-end é uma parte importante do design e desenvolvimento web. Ao seguir as práticas recomendadas e padrões de acessibilidade, você pode criar uma experiência mais inclusiva e melhor para todos os seus usuários.
- https://watplast.com.br/conheca-os-simbolos-da-acessibilidade-comunicacional-e-sua-importancia-em-ambientes-comerciais/

_1 imagem(ns) no slide._

### Slide 17

- Ainda sobre acessibilidade, vamos conhecer praticando?
- Na plataforma Alura vamos acessar o seguinte curso:
- Link para o curso: https://cursos.alura.com.br/course/acessibilidade-web-design-inclusivos
- Ao longo das atividades, você vai encontrar alguns quizzes e eles não estão ali por acaso! Eles são oportunidades rápidas para testar seu entendimento, reforçar o que aprendeu e identificar pontos que ainda podem melhorar.

_2 imagem(ns) no slide._

### Slide 18

- Um pouco sobre a surdez
- 15 minutos
- A acessibilidade para pessoas surdas no desenvolvimento front-end é crucial e envolve o uso de legendas em vídeos.
- Link para tarefa: https://cursos.alura.com.br/course/acessibilidade-web-design-inclusivos/task/32568
- A inclusão de transcrições para áudios e a garantia de que todas as informações transmitidas por som também sejam apresentadas visualmente. Essas práticas garantem que os conteúdos digitais sejam acessíveis a todos, independentemente de suas habilidades auditivas.
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 19

- Vamos praticar?
- Prepare-se, porque nessa atividade, você vai sair do modo aprender e entrar direto no modo praticar.
- A atividade prática vai colocar você diante de um desafio real, que faz relação com o conteúdo aprendido até aqui.

_1 imagem(ns) no slide._

### Slide 20

- O que vimos na aula de hoje:
- Conhecemos os pontos relevantes sobre acessibilidade em páginas HTML para pessoas com capacidade auditiva reduzida.

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
