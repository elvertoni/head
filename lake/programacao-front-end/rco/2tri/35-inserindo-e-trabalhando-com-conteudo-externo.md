---
titulo: "Inserindo e Trabalhando com Conteúdo Externo"
tipo: rco-seed
disciplina: programacao-front-end
sigla_rco: PFE
trimestre: 2
ordem_rco: 35
serie: 2
aula_rco: "Aula 35"
slides: 27
tem_atividade: true
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PFE/2TRI/35-inserindo-e-trabalhando-com-conteudo-externo/35-inserindo-e-trabalhando-com-conteudo-externo.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/2TRI/35-inserindo-e-trabalhando-com-conteudo-externo/AULA 35_ATIVIDADE_PROGRAMAÇÃO FRONT END.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Inserindo e Trabalhando com Conteúdo Externo

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- Programação Front-End
- 2ª Série
- Inserindo e Trabalhando com Conteúdo Externo
- Aula 35

_3 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- COMPETÊNCIA(S) A SER(EM) DESENVOLVIDA(S) NESTA AULA:
- De acordo com o Plano de Curso de Desenvolvimento de Sistemas:
- HABILIDADE(S) A SER(EM) DESENVOLVIDA(S) NESTA AULA:
- Desenvolver interfaces gráficas para aplicações computacionais.
- Estruturar arquitetura dos elementos de conteúdo de websites.

_1 imagem(ns) no slide._

### Slide 4

- Nesta aula vamos:
- Adicionar fontes externas a projetos.
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
- Projeto aula anterior:
- https://caelum-online-public.s3.amazonaws.com/1310-html5-css3-parte4/01/html-parte-4-aula-1-completa.zip
- Complemento:
- https://cursos.alura.com.br/course/html5-css3-primeiros-passos/task/581966

_2 imagem(ns) no slide._

### Slide 6

- Aula anterior
- Iniciamos os estudos para uma nova inclusão de elementos e melhorias em páginas HTML realizando adaptações as páginas já criadas.

_1 imagem(ns) no slide._

### Slide 7

- Para pensarmos juntos...
- Lucas é um designer de websites e está trabalhando em um projeto para um cliente que deseja utilizar uma fonte específica e única em seu site. Lucas descobriu que a fonte desejada não está disponível no conjunto padrão de fontes web, então ele precisa encontrar uma maneira de incorporar essa fonte externa no site.

_1 imagem(ns) no slide._

### Slide 8

- Para pensarmos juntos...
- Qual é a melhor abordagem para Lucas incorporar uma fonte externa no site HTML do cliente?
- Conversem e apresentem suas visões

_2 imagem(ns) no slide._

### Slide 9

- Para pensarmos juntos...
- a) Adicionar a fonte diretamente no arquivo HTML usando a tag <font>
- b) Utilizar a tag <link> para vincular a fonte externa no arquivo CSS
- c) Utilizar a propriedade @import no arquivo CSS para importar a fonte
- d) Utilizar a tag <style> no arquivo HTML para incorporar a fonte
- Conversem e apresentem suas visões

_2 imagem(ns) no slide._

### Slide 10

- Resposta
- A resposta correta é a alternativa "c". Para incorporar uma fonte externa em um site HTML, Lucas pode utilizar a propriedade @import no arquivo CSS. Isso permitirá que ele importe a fonte do serviço externo, como o Google Fonts, e a utilize no site do cliente.

_1 imagem(ns) no slide._

### Slide 11

- Resposta
- A alternativa "b" é incorreta, pois a tag <link> não é usada para vincular fontes externas, mas sim para vincular arquivos CSS. A alternativa "a" é incorreta, pois a tag <font> está obsoleta e não deve ser usada. A alternativa "d" também não é a abordagem correta, já que incorporar a fonte usando a tag <style> não é a prática recomendada.

_1 imagem(ns) no slide._

### Slide 12

- Conceituando
- A utilização de conteúdo externo em páginas HTML enriquece a experiência do usuário ao adicionar elementos visuais e interativos ao site, como fontes personalizadas, mapas interativos e vídeos incorporados. O conteúdo externo é geralmente hospedado em serviços especializados, como Google Fonts, Google Maps, YouTube ou Vimeo, e pode ser facilmente integrado ao site por meio de tags específicas, propriedades CSS ou APIs.
- https://i.stack.imgur.com/paa02.jpg

_2 imagem(ns) no slide._

### Slide 13

- Conceituando
- A incorporação desses recursos externos permite que os desenvolvedores criem páginas web mais atraentes e funcionais, sem a necessidade de reinventar a roda ou lidar com problemas técnicos complexos.
- https://i.stack.imgur.com/paa02.jpg

_1 imagem(ns) no slide._

### Slide 14

- Conceituando
- Para adicionar fontes externas, os desenvolvedores podem utilizar serviços como o Google Fonts ou Adobe Fonts, como mencionado anteriormente. A tag <link> ou a propriedade CSS @import são usadas para vincular o arquivo de fonte externa à página HTML, permitindo a aplicação da fonte aos elementos do site por meio das regras CSS.

_1 imagem(ns) no slide._

### Slide 15

- Conceituando
- Além disso, mapas interativos podem ser incorporados usando recursos do Google Maps, OpenStreetMap ou outros serviços semelhantes. A integração desses mapas geralmente envolve a inclusão de um trecho de código JavaScript e a criação de um elemento HTML para exibir o mapa, como um <div> com um identificador específico.

_1 imagem(ns) no slide._

### Slide 16

- Conceituando
- Para incorporar vídeos em uma página HTML, os desenvolvedores podem utilizar serviços de hospedagem de vídeos como YouTube ou Vimeo. Geralmente, esses serviços fornecem um trecho de código HTML que inclui um elemento <iframe> com atributos específicos, como a URL do vídeo e as dimensões desejadas.

_1 imagem(ns) no slide._

### Slide 17

- Conceituando
- Ao colar esse código na página HTML, o vídeo será exibido e reproduzido conforme as configurações especificadas. A incorporação de conteúdo externo, como fontes, mapas e vídeos, é uma maneira eficaz de melhorar o design, a interatividade e a funcionalidade das páginas web, ao mesmo tempo em que aproveita os recursos oferecidos por serviços especializados.

_1 imagem(ns) no slide._

### Slide 18

- Exemplo
- <!DOCTYPE html>
- <html lang="en">
- <head>
- <meta charset="UTF-8">
- <meta name="viewport" content="width=device-width, initial-scale=1.0">
- <title>Exemplo de Fonte Externa</title>
- <link rel="stylesheet“ href="https://fonts.googleapis.com/css2?family=Roboto&display=swap">
- </head>
- <body>
- <!-- Seu conteúdo aqui -->
- </body>
- </html>
- https://algol.dev/wp-content/uploads/2020/10/font_code-compressor.jpg

_1 imagem(ns) no slide._

### Slide 19

- Link para o curso: https://cursos.alura.com.br/course/html5-css3-avancando-css
- A recomendação é que você continue esse curso extraclasse, pois ele traz um conteúdo essencial para compreender sobre o referido tema.
- Atividade Prática na Plataforma Alura
- Na plataforma Alura vamos acessar o seguinte curso:

_3 imagem(ns) no slide._

### Slide 20

- Fontes externas
- 8 minutos
- Iremos compreender como utilizar fontes externas para os textos, para o mapa e para vídeos.
- Link para tarefa: https://cursos.alura.com.br/course/html5-css3-avancando-css/task/63320
- Primeiramente precisamos entender quais são as características de fontes preparadas para web: elas funcionam melhor em todos os navegadores, possuem comportamento parecido em todos os sistemas operacionais.
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 21

- Trabalhando com mapas
- 9 minutos
- Agora iremos tratar a área do mapa, aquela que indica a localização da barbearia. Teremos mais um título e subtítulo e o conteúdo do Google Maps.
- Link para tarefa: https://cursos.alura.com.br/course/html5-css3-avancando-css/task/63321
- O espaçamento ainda não está adequado, mas por enquanto focaremos somente no HTML e posteriormente faremos os ajustes necessários na diagramação da página.
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 22

- Importando vídeo
- 4 minutos
- Para finalizar o conteúdo e a importação dos elementos, lidaremos com o vídeo do site.
- Link para tarefa: https://cursos.alura.com.br/course/html5-css3-avancando-css/task/63322
- Para incorporar um vídeo em HTML, utilize a tag <iframe> com a URL do vídeo e as dimensões desejadas.
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 23

- Vamos praticar?
- Prepare-se, porque nessa atividade, você vai sair do modo aprender e entrar direto no modo praticar.
- A atividade prática vai colocar você diante de um desafio real, que faz relação com o conteúdo aprendido até aqui.

_1 imagem(ns) no slide._

### Slide 24

- O que vimos na aula de hoje:
- Aprendemos como incorporar elementos externos em páginas HTML.
- Aprendemos que elementos externos podem ser imagens, vídeos e até mesmo fontes de texto.

_1 imagem(ns) no slide._

### Slide 25

- Pronto para desbloquear sua carreira de TI?
- Está perdido estudando mas não sabe por onde começar? Se a resposta é sim, você está no lugar certo! Descubra as estratégias e ferramentas essenciais para te ajudar a desbloquear seu potencial em TI e buscar sua primeira vaga de emprego no setor!
- Este e-book é um guia completo para quem busca começar pelos melhores caminhos para se tornar um excelente profissional de TI, ensinando a identificar perfis profissionais, aplicar técnicas de estudo eficazes, transformar teoria em prática, e aumentar a visibilidade de seu trabalho no mercado de trabalho. Ideal para novatos e profissionais em transição.
- E o melhor, ele pode ser seu, inteiramente grátis!
- Basta clicar AQUI e realizar o seu cadastro com o seu @escola!

_3 imagem(ns) no slide._

### Slide 26

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

### Slide 27

_(sem texto)_

## Atividade

_Fonte: AULA 35_ATIVIDADE_PROGRAMAÇÃO FRONT END.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação Front-End

2ª SÉRIE

ATIVIDADE AULA 35

Questão 1

Qual método é usado para incorporar um vídeo do YouTube em uma página HTML?

a) Utilizar a tag <video> com a URL do vídeo

b) Utilizar a tag <iframe> com a URL do vídeo

c) Utilizar a tag <embed> com a URL do vídeo

d) Utilizar a tag <object> com a URL do vídeo

Comentário: A resposta correta é a alternativa "b". Para incorporar um vídeo do YouTube em uma página HTML, é comum usar a tag <iframe> com a URL do vídeo. O YouTube fornece o código do <iframe> que já inclui a URL e os atributos necessários para incorporar o vídeo na página.

Questão 2

Como você adiciona um mapa do Google Maps em sua página HTML?

a) Utilizar a tag <map> com a URL do mapa

b) Utilizar a tag <iframe> com a URL do mapa

c) Utilizar a tag <embed> com a URL do mapa

d) Utilizar a tag <object> com a URL do mapa

Comentário: A resposta correta é a alternativa "b". Para adicionar um mapa do Google Maps em sua página HTML, você pode utilizar a tag <iframe> com a URL do mapa. O Google Maps fornece um código de incorporação que inclui a tag <iframe> com a URL e os atributos necessários para exibir o mapa na página.
