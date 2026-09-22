---
titulo: "Selecionando qualquer coisa"
tipo: rco-seed
disciplina: programacao-front-end
sigla_rco: PFE
trimestre: 2
ordem_rco: 39
serie: 2
aula_rco: "Aula 39"
slides: 22
tem_atividade: true
tem_pratica: true
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/2TRI/39-selecionando-elementos-com-css/39-selecionando-elementos-com-css.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/2TRI/39-selecionando-elementos-com-css/AULA 39_ATIVIDADE_PROGRAMAÇÃO FRONT END.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/2TRI/39-selecionando-elementos-com-css/AULA 39_PRÁTICA_PROGRAMAÇÃO FRONT END.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Selecionando qualquer coisa

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- Programação Front-End
- 2ª Série
- Selecionando qualquer coisa
- Aula 39

_1 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- COMPETÊNCIA(S) A SER(EM) DESENVOLVIDA(S) NESTA AULA:
- De acordo com o Plano de Curso de Desenvolvimento de Sistemas:
- HABILIDADE(S) A SER(EM) DESENVOLVIDA(S) NESTA AULA:
- Desenvolver interfaces gráficas para aplicações computacionais.
- Criar e estilizar páginas utilizando HTML e CSS.

_1 imagem(ns) no slide._

### Slide 4

- Nesta aula vamos:
- Aprender sobre seletores em páginas HTML.
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
- https://caelum-online-public.s3.amazonaws.com/1310-html5-css3-parte4/03/html-parte-4-aula-3-completa.zip
- Complemento:
- https://cursos.alura.com.br/course/html5-css3-primeiros-passos/task/581966

_2 imagem(ns) no slide._

### Slide 6

- Aula anterior
- Finalizamos os estudos sobre a melhoria do CSS fazendo uso de pseudo-classes, utilizados para aplicar estilos, além de utilizar a aplicação de gradientes em páginas HTML.

_1 imagem(ns) no slide._

### Slide 7

- Para pensarmos juntos...
- Carla é uma desenvolvedora web iniciante que está trabalhando em seu primeiro projeto de site pessoal. Ela quer aplicar estilos específicos a diferentes elementos da página, como títulos, parágrafos e links, mas não tem certeza de como selecionar corretamente esses elementos usando CSS.

_1 imagem(ns) no slide._

### Slide 8

- Para pensarmos juntos...
- Como Carla pode usar seletores CSS para aplicar estilos a diferentes elementos HTML em sua página?
- Conversem e apresentem suas visões

_2 imagem(ns) no slide._

### Slide 9

- Resposta
- Carla pode usar seletores CSS para selecionar e aplicar estilos a diferentes elementos HTML de acordo com seu tipo, classe, ID ou outras características.

_1 imagem(ns) no slide._

### Slide 10

- Conceituando
- Seletores em HTML são utilizados em folhas de estilo CSS para identificar e selecionar elementos específicos no documento HTML, permitindo que estilos sejam aplicados a eles. Os seletores oferecem uma maneira eficiente e flexível de controlar o design e a apresentação visual de páginas web.

_1 imagem(ns) no slide._

### Slide 11

- Conceituando
- Vantagens dos seletores em HTML incluem:
- Flexibilidade: Permite aplicar estilos a diferentes elementos com base em seu tipo, classe, ID, atributos ou relações entre eles.
- Reutilização de código: Seletores de classe, por exemplo, permitem aplicar o mesmo conjunto de estilos a múltiplos elementos, tornando o código CSS mais eficiente e fácil de manter.

_1 imagem(ns) no slide._

### Slide 12

- Conceituando
- Separar conteúdo e apresentação: Ao usar seletores, os desenvolvedores podem separar a estrutura e o conteúdo do HTML da apresentação e design, melhorando a organização do código e facilitando a manutenção do site. Suponha que Carla deseja estilizar todos os títulos <h2> dentro de uma seção de conteúdo com a classe .artigo, aplicando uma cor específica e aumentando o espaçamento entre as letras. Ela pode usar seletores para aplicar esses estilos:

_1 imagem(ns) no slide._

### Slide 13

- Conceituando
- <!-- Exemplo de HTML -->
- <section class="artigo">
- <h2>Título do artigo</h2>
- <p>Texto do artigo...</p>
- </section>
- /* Exemplo de CSS */
- .artigo h2 {
- color: #333;
- letter-spacing: 2px;
- }

_1 imagem(ns) no slide._

### Slide 14

- Conceituando
- Neste exemplo, Carla utiliza o seletor .artigo h2 para selecionar todos os elementos <h2> que estão dentro de um elemento com a classe .artigo. Em seguida, ela aplica a cor e o espaçamento entre as letras desejados a esses títulos.

_1 imagem(ns) no slide._

### Slide 15

- Link para o curso: https://cursos.alura.com.br/course/html5-css3-avancando-css
- A recomendação é que você continue esse curso extraclasse, pois ele traz um conteúdo essencial para compreender sobre o referido tema.
- Atividade Prática na Plataforma Alura
- Na plataforma Alura vamos acessar o seguinte curso:

_3 imagem(ns) no slide._

### Slide 16

- Seletores avançados
- 7 minutos
- Nesta aula, estudaremos os seletores avançados, uma forma específica de fazermos seleção de elementos de maneira mais rebuscada.
- Link para tarefa: https://cursos.alura.com.br/course/html5-css3-avancando-css/task/63326
- Suponhamos que no interior da <main>, antes de se iniciar a <section>, nós tenhamos um <p> com um conteúdo qualquer.
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 17

- Cálculos com CSS
- 5 minutos
- Nesta aula,aprenderemos como realizar cálculos dinâmicos de posicionamento de elementos no CSS, como altura e largura.
- Link para tarefa: https://cursos.alura.com.br/course/html5-css3-avancando-css/task/63327
- Nosso site deve estar preparado para dispositivos com diversos tamanhos de tela. Um grande problema enfrentado ao desenvolver um site harmonioso é justamente calcular a proporção das dimensões dos elementos em diferentes dispositivos.
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 18

- Vamos praticar?
- Prepare-se, porque nessa atividade, você vai sair do modo aprender e entrar direto no modo praticar.
- A atividade prática vai colocar você diante de um desafio real, que faz relação com o conteúdo aprendido até aqui.

_1 imagem(ns) no slide._

### Slide 19

- O que vimos na aula de hoje:
- Aprendemos sobre seletores e cálculos em CSS para páginas HTML.

_1 imagem(ns) no slide._

### Slide 20

- Pronto para desbloquear sua carreira de TI?
- Está perdido estudando mas não sabe por onde começar? Se a resposta é sim, você está no lugar certo! Descubra as estratégias e ferramentas essenciais para te ajudar a desbloquear seu potencial em TI e buscar sua primeira vaga de emprego no setor!
- Este e-book é um guia completo para quem busca começar pelos melhores caminhos para se tornar um excelente profissional de TI, ensinando a identificar perfis profissionais, aplicar técnicas de estudo eficazes, transformar teoria em prática, e aumentar a visibilidade de seu trabalho no mercado de trabalho. Ideal para novatos e profissionais em transição.
- E o melhor, ele pode ser seu, inteiramente grátis!
- Basta clicar AQUI e realizar o seu cadastro com o seu @escola!

_3 imagem(ns) no slide._

### Slide 21

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

### Slide 22

_(sem texto)_

## Atividade

_Fonte: AULA 39_ATIVIDADE_PROGRAMAÇÃO FRONT END.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação Front-End

2ª SÉRIE

ATIVIDADE AULA 39

Questão 1

Qual dos seletores abaixo seleciona todos os elementos <p> que são filhos diretos de um elemento <div>?

a) div p

b) div > p

c) div + p

d) div ~ p

Comentário: A resposta correta é a alternativa "b". O seletor "div > p" seleciona todos os elementos <p> que são filhos diretos de um elemento <div>. Os outros seletores têm funções diferentes: "div p" (a) seleciona todos os elementos <p> que estão dentro de um <div>, "div + p" (c) seleciona um elemento <p> que vem imediatamente após um <div>, e "div ~ p" (d) seleciona todos os elementos <p> que são irmãos de um <div> e compartilham o mesmo elemento pai.

Questão 2

Qual propriedade e função CSS permitem realizar cálculos para determinar o valor de uma propriedade?

a) calc() e width

b) compute() e height

c) math() e margin

d) calc() e font-size

Comentário: A resposta correta é a alternativa "a". A função calc() é usada para realizar cálculos em CSS e pode ser aplicada a várias propriedades, incluindo "width". As outras alternativas apresentam funções inexistentes no CSS (compute() e math()) e, portanto, são incorretas. A função calc() também pode ser aplicada a outras propriedades além de "width", como "height", "margin", "font-size" e muitas outras.

## Prática

_Fonte: AULA 39_PRÁTICA_PROGRAMAÇÃO FRONT END.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

PROGRAMAÇÃO FRONT END

2ª SÉRIE

ATIVIDADE PRÁTICA AULA 39

##### 1. Objetivo da Aula Prática

Ao final da aula prática, o estudante será capaz de:

- Compreender o papel dos seletores CSS na estilização de páginas HTML.
- Aplicar estilos a elementos usando seletores por tag, classe, ID e relação entre elementos.
- Utilizar seletores avançados para estilizar partes específicas da página.
- Aplicar cálculos com CSS para ajustar medidas de forma dinâmica.
- Melhorar a organização visual e a manutenção do código CSS.
Produto final esperado:

- Página HTML com seletores CSS aplicados corretamente e ajustes de largura/altura usando cálculos simples em CSS.

##### 2. Ferramentas Recomendadas

###### VS Code ou Editor HTML

- Para que serve: editar os arquivos HTML e CSS do projeto.
- Por que é adequado: permite visualizar e organizar melhor seletores e regras CSS.
- Como facilita o aprendizado: possibilita testar seletores diferentes e observar o efeito no navegador.

###### Navegador Web

- Para que serve: testar a aplicação dos estilos.
- Por que é adequado: mostra o resultado real da página.
- Como facilita o aprendizado: permite verificar se o seletor atingiu o elemento correto.

###### Editor Online HTML5

- Link: https://html5-editor.net/
- Para que serve: testar pequenos trechos de HTML e CSS.
- Por que é adequado: funciona diretamente no navegador.
- Como facilita o aprendizado: permite feedback visual rápido.

##### 3. Checklist Inicial

Antes de iniciar a prática, o estudante deve ter:

- Projeto HTML das aulas anteriores aberto
- Arquivo CSS externo funcionando
- Estrutura com <main>, <section>, títulos, parágrafos e links
- Navegador atualizado
- Conexão com internet
- Acesso ao curso de apoio da Alura
Material de apoio indicado na aula: https://cursos.alura.com.br/course/html5-css3-avancando-css

##### 4. Passo a Passo do Docente (Aula de até 50 minutos)

###### Preparações necessárias

- Garantir que os alunos tenham o projeto da aula anterior aberto.
- Revisar rapidamente o uso de classes e IDs.
- Preparar exemplos simples de seletores CSS:
- seletor por tag
- seletor por classe
- seletor por ID
- seletor descendente
- seletor avançado

###### Condução da aula

###### 1. Contextualização inicial — 5 minutos

Apresente o problema:

- A página tem vários elementos.
- Nem sempre queremos estilizar todos.
- Às vezes precisamos selecionar apenas um elemento específico.
Pergunta para a turma:

Como aplicar estilo apenas em um título dentro de uma seção, sem afetar os outros títulos da página?

###### 2. Demonstração de seletores CSS — 15 minutos

Explique e demonstre:

- Seletor por tag:
- aplica em todos os elementos daquele tipo.
- Seletor por classe:
- reutilizável em vários elementos.
- Seletor por ID:
- usado para um elemento específico.
- Seletor descendente:
- seleciona elementos dentro de outro elemento.
Exemplo conceitual:

- .artigo h2 {
- color: #333;
- letter-spacing: 2px;
- }
Explique que esse seletor altera somente os <h2> que estão dentro de elementos com a classe .artigo.

###### 3. Seletores avançados — 10 minutos

Demonstre seletores que permitem maior precisão:

- Selecionar parágrafos dentro de uma seção.
- Selecionar links dentro do menu.
- Selecionar apenas elementos dentro do <main>.
Mostre que seletores bem usados evitam excesso de classes e deixam o CSS mais organizado.

###### 4. Cálculos com CSS — 10 minutos

Explique que o CSS permite calcular larguras e alturas de forma dinâmica usando calc().

Exemplo conceitual:

- .caixa {
- width: calc(100% - 40px);
- }
Relacione com a necessidade de adaptar o site a diferentes tamanhos de tela.

###### 5. Prática guiada — 5 minutos

Oriente os alunos a:

- Selecionar uma seção específica.
- Estilizar apenas títulos dentro dela.
- Ajustar largura de um bloco usando calc().

###### 6. Revisão e fechamento — 5 minutos

Solicite que os alunos testem:

- Se o seletor alterou apenas o elemento esperado.
- Se o cálculo CSS funcionou.
- Se a página continua organizada visualmente.

###### Pontos de atenção

- Evitar seletores muito genéricos quando o objetivo for estilizar algo específico.
- Não usar IDs em excesso.
- Testar cada seletor antes de continuar.
- Conferir se o CSS não afetou outras partes da página.

##### 5. Atividade Prática — Descrição Geral

O estudante deverá aplicar seletores CSS em uma página HTML existente para estilizar elementos específicos sem alterar toda a página.

Durante a atividade, ele deverá:

- Criar ou identificar uma seção de conteúdo.
- Aplicar estilos apenas em elementos internos dessa seção.
- Utilizar seletor de classe e seletor descendente.
- Usar calc() para ajustar largura de um elemento.
Problema real simulado: Ajustar o visual de uma parte específica de um site sem comprometer o restante do layout.

Habilidade desenvolvida: Controle preciso de estilos CSS e organização visual de interfaces.

##### 6. Metodologia Ativa Utilizada

- Aprendizagem baseada em projeto
- Experimentação prática
- Ensino por descoberta
- Prática guiada
- Elementos de Lemov:
- Modelagem
- Checagem de compreensão
- Feedback imediato
- Todos escrevem

##### 7. Passo a Passo da Atividade Prática (para os alunos)

- Abra o projeto HTML utilizado nas aulas anteriores.
- Localize uma seção da página, como <section> ou <main>.
- Adicione uma classe à seção, por exemplo: class="artigo".
- Dentro dessa seção, verifique se existem títulos, parágrafos ou links.
- No arquivo CSS, crie um seletor para estilizar apenas os títulos dentro da seção.
- Crie outro seletor para estilizar apenas os parágrafos dentro da seção.
- Aplique uma cor diferente, espaçamento ou tamanho de fonte.
- Crie uma caixa ou bloco de conteúdo.
- Use calc() para definir a largura desse bloco.
- Salve os arquivos.
- Abra no navegador.
- Verifique se os estilos foram aplicados apenas nos elementos desejados.
- Ajuste o código, se necessário.

##### 8. Exemplo ou Demonstração

###### Exemplo de estrutura HTML

- <section class="artigo">
- <h2>Título do artigo</h2>
- <p>Texto do artigo...</p>
- </section>

###### Exemplo de CSS

- .artigo h2 {
- color: #333;
- letter-spacing: 2px;
- }
- .artigo p {
- width: calc(100% - 40px);
- }

###### Explicação

- .artigo h2 seleciona apenas os títulos <h2> dentro da seção com classe artigo.
- .artigo p seleciona apenas os parágrafos dentro da seção.
- calc(100% - 40px) ajusta a largura do parágrafo de forma dinâmica.

##### 9. Resultado Esperado

O estudante deverá apresentar:

- Página com seletores CSS aplicados corretamente.
- Pelo menos um seletor por classe.
- Pelo menos um seletor descendente.
- Pelo menos um uso de calc().
- Código organizado e funcional.
O professor poderá verificar se o objetivo foi atingido observando:

- Se os estilos não afetaram elementos fora da seção.
- Se o CSS está claro e bem organizado.
- Se o layout continua coerente após os ajustes.

##### 10. Formato de Entrega da Atividade

- Formato: pasta do projeto ou print da página final.
- Arquivos esperados:
- index.html
- style.css
- demais arquivos do projeto, se houver.
- Nomeação sugerida: aula39_nomeAluno
- Local de entrega: Google Drive, AVA, Classroom ou repositório indicado pelo professor.
- Prazo sugerido: ao final da aula ou até a próxima aula.

##### 11. Encerramento e Reflexão

Finalize com uma conversa orientada:

- Por que seletores bem definidos evitam problemas no CSS?
- Quando é melhor usar classe em vez de ID?
- Como o calc() pode ajudar em páginas responsivas?
- O que pode acontecer se um seletor for muito genérico?
