---
titulo: "Formulário acessível Parte II"
tipo: rco-seed
disciplina: programacao-front-end
sigla_rco: PFE
trimestre: 3
ordem_rco: 66
serie: 2
aula_rco: "Aula 66"
slides: 23
tem_atividade: false
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/3TRI/66-formulario-acessivel-parte-ii/66-formulario-acessivel-parte-ii.pptx"
extrator: tools/extrair_rco.py
status: bruto
---

# Formulário acessível Parte II

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- Programação Front-End
- 2ª Série
- Formulário acessível Parte II
- Aula 66

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
- Compreender acessibilidade a formulários em páginas HTML Parte II.
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
- https://github.com/designernatan/curso-acessibilidade-web-front-end-1/archive/0115ab16629f4f264184beb291ece993b7246f8c.zip

_2 imagem(ns) no slide._

### Slide 6

- Aula anterior
- Iniciamos os estudos sobre acessibilidade de formulários em páginas HTML.

_1 imagem(ns) no slide._

### Slide 7

- Para pensarmos juntos...
- Em sua primeira semana como desenvolvedor web júnior em uma startup, Lucas foi designado para trabalhar em um novo projeto de site de ensino online. A plataforma tinha uma grande quantidade de vídeos educacionais e uma de suas principais tarefas era garantir que esses vídeos fossem acessíveis a todos os usuários, incluindo aqueles com deficiências auditivas.
- 3 minutos

_2 imagem(ns) no slide._

### Slide 8

- Para pensarmos juntos...
- Lucas sabia sobre a importância das legendas, mas não tinha certeza de como implementá-las de maneira eficiente. Ele questionou: "Como posso garantir que as legendas dos vídeos sejam exibidas corretamente para todos os usuários, especialmente para aqueles que dependem desses recursos de acessibilidade?"
- 3 minutos
- Pesquise e apresente suas versões

_3 imagem(ns) no slide._

### Slide 9

- Resposta
- A resposta para o questionamento de Lucas seria: As legendas podem ser adicionadas a vídeos usando a tag <track> em HTML. Este elemento é usado para especificar faixas de texto para vídeo e áudio, como legendas, legendas, descrições, capítulos ou metadados.

_1 imagem(ns) no slide._

### Slide 10

- Resposta
- Essas legendas não apenas tornam os vídeos acessíveis para usuários com deficiência auditiva, mas também para usuários que não podem reproduzir som ou preferem assistir ao vídeo sem som.
- 3 minutos
- Além disso, as legendas também podem ser úteis para usuários que não falam a língua do vídeo e precisam de traduções. É importante lembrar que as legendas devem ser precisas, claras e sincronizadas com o áudio.

_2 imagem(ns) no slide._

### Slide 11

- Conceituando
- A acessibilidade em páginas HTML envolve a criação de sites que podem ser usados por todos, incluindo pessoas com deficiências. Vários recursos de acessibilidade podem ser incorporados ao desenvolver páginas da web para torná-las mais acessíveis.
- https://www.al.sp.gov.br/repositorio/noticia/N-03-2021/fg263796.jpg

_1 imagem(ns) no slide._

### Slide 12

- Conceituando
- Legendas e transcrições de áudio/vídeo: As legendas são indispensáveis para pessoas com deficiência auditiva e também úteis para quem assiste a vídeos em ambientes barulhentos. As transcrições de áudio são úteis para pessoas que preferem ler o conteúdo do áudio ou vídeo.
- https://herospark.com/blog/wp-content/uploads/sites/6/2021/04/legendas-de-videos.jpeg

_1 imagem(ns) no slide._

### Slide 13

- Conceituando
- Alt text para imagens: Este é um recurso importante que descreve imagens para usuários de leitores de tela e para aqueles que desativaram imagens em seus navegadores.
- Contraste de cores apropriado: Para pessoas com deficiência visual ou daltonismo, é crucial que haja um contraste adequado entre a cor do texto e a cor do fundo.
- https://triangulo.dev/posts/paleta-de-cores-perfeita-para-seu-projeto/escala-de-cores-radix-colors-light.png

_1 imagem(ns) no slide._

### Slide 14

- Conceituando
- Acessibilidade do teclado: Certifique-se de que todos os elementos interativos da página possam ser acessados e usados apenas com o teclado. Isso é especialmente importante para pessoas que não conseguem usar um mouse.
- https://blog.elgscreen.com/wp-content/uploads/2017/07/teclados-para-deficientes-visuais.jpg

_1 imagem(ns) no slide._

### Slide 15

- Conceituando
- Uso adequado de cabeçalhos e estrutura: A estrutura correta da página usando cabeçalhos ajuda os usuários de leitores de tela a navegar no conteúdo da página de maneira mais eficiente.
- Ao incorporar esses recursos de acessibilidade, os desenvolvedores podem criar sites mais inclusivos que podem ser usados por todos, independentemente de suas habilidades físicas ou sensoriais.
- https://www.deficienteciente.com.br/nova-tecnologia-ajuda-deficientes-auditivos-a-usar-o-computador.html

_1 imagem(ns) no slide._

### Slide 16

- Ainda sobre acessibilidade, vamos conhecer praticando?
- Na plataforma Alura vamos acessar o seguinte curso:
- Link para o curso: https://cursos.alura.com.br/course/acessibilidade-web-front-end
- Ao longo das atividades, você vai encontrar alguns quizzes e eles não estão ali por acaso! Eles são oportunidades rápidas para testar seu entendimento, reforçar o que aprendeu e identificar pontos que ainda podem melhorar.

_2 imagem(ns) no slide._

### Slide 17

- Legendas em vídeo
- 10 minutos
- A inclusão de legendas em vídeos HTML é crucial para a acessibilidade, pois permite que pessoas com deficiências auditivas entendam o conteúdo.
- Link para tarefa: https://cursos.alura.com.br/course/acessibilidade-web-front-end/task/36251
- Também é útil para quem está assistindo em ambientes barulhentos ou silenciosos. As legendas devem ser claras, sincronizadas com o áudio e incluir informações sonoras relevantes. Além disso, é aconselhável disponibilizar uma transcrição do vídeo para referência posterior.
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 18

- Conclusão
- 5 minutos
- As aulas foram focadas em usuários que fazem uso dos leitores de tela, especificamente o NVDA que está se tornando a ferramenta mais popular entre os usuários.
- Link para tarefa: https://cursos.alura.com.br/course/acessibilidade-web-front-end/task/36252
- No que diz respeita à acessibilidade, é interessante que nosso código possua apenas um <h1>, para hierarquizarmos a informação.
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
