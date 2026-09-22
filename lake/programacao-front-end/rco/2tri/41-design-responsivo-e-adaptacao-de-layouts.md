---
titulo: "Design Responsivo e Adaptação de Layouts"
tipo: rco-seed
disciplina: programacao-front-end
sigla_rco: PFE
trimestre: 2
ordem_rco: 41
serie: 2
aula_rco: "Aula 41"
slides: 22
tem_atividade: true
tem_pratica: true
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PFE/2TRI/41-design-responsivo-e-adaptacao-de-layouts/41-design-responsivo-e-adaptacao-de-layouts.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/2TRI/41-design-responsivo-e-adaptacao-de-layouts/AULA 41_ATIVIDADE_PROGRAMAÇÃO FRONT END.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/2TRI/41-design-responsivo-e-adaptacao-de-layouts/AULA 41_PRÁTICA_PROGRAMAÇÃO FRONT END.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Design Responsivo e Adaptação de Layouts

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- Programação Front-End
- 2ª Série
- Design Responsivo e Adaptação de Layouts
- Aula 41

_1 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- COMPETÊNCIA(S) A SER(EM) DESENVOLVIDA(S) NESTA AULA:
- De acordo com o Plano de Curso de Desenvolvimento de Sistemas:
- HABILIDADE(S) A SER(EM) DESENVOLVIDA(S) NESTA AULA:
- Desenvolver interfaces gráficas para aplicações computacionais.
- Prototipar interfaces e elementos visuais.

_1 imagem(ns) no slide._

### Slide 4

- Nesta aula vamos:
- Aprender sobre design responsivo em páginas HTML.
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
- https://caelum-online-public.s3.amazonaws.com/1310-html5-css3-parte4/05/html-parte-4-aula-5-completa.zip
- Complemento:
- https://cursos.alura.com.br/course/html5-css3-primeiros-passos/task/581966

_2 imagem(ns) no slide._

### Slide 6

- Aula anterior
- Concluímos os estudos a respeito da utilização de opacidade em páginas HTML, benefícios e formas de utilização.

_1 imagem(ns) no slide._

### Slide 7

- Para pensarmos juntos...
- Juliana é a desenvolvedora web responsável por criar o site de uma loja de roupas online. Para garantir que o site seja acessível e funcione bem em diversos dispositivos, como desktops, tablets e smartphones, ela precisa implementar um design responsivo. Juliana quer garantir que o layout se ajuste automaticamente, proporcionando a melhor experiência de usuário possível, independentemente do tamanho da tela do dispositivo.

_1 imagem(ns) no slide._

### Slide 8

- Para pensarmos juntos...
- Como Juliana pode implementar um design responsivo nas páginas HTML do site da loja de roupas?
- Conversem e apresentem suas visões

_2 imagem(ns) no slide._

### Slide 9

- Resposta
- Juliana pode implementar um design responsivo usando várias técnicas, como:
- Utilizar a meta tag viewport no HTML para controlar o layout em diferentes dispositivos
- Usar regras CSS @media para aplicar estilos específicos com base na largura da tela do dispositivo do usuário

_1 imagem(ns) no slide._

### Slide 10

- Conceituando
- O design responsivo em HTML é uma abordagem de design web que busca garantir que as páginas se adaptem automaticamente ao tamanho e orientação do dispositivo do usuário. Isso é realizado por meio do ajuste dinâmico do layout, redimensionamento de imagens e uso de estilos condicionais, proporcionando uma experiência de usuário otimizada e consistente em diversos dispositivos, como desktops, tablets e smartphones.

_1 imagem(ns) no slide._

### Slide 11

- Conceituando
- O conceito de design responsivo é baseado na ideia de que o design e o desenvolvimento devem responder ao comportamento e ambiente do usuário. Isso significa que, em vez de criar várias versões de um site para diferentes dispositivos, os desenvolvedores podem criar um único site que funcione bem em todos eles.

_1 imagem(ns) no slide._

### Slide 12

- Conceituando
- O design responsivo pode ajudar o usuário de várias maneiras:
- Acessibilidade: Um site responsivo é acessível em uma ampla variedade de dispositivos e navegadores, garantindo que todos os usuários possam acessar o conteúdo e funcionalidades do site, independentemente do dispositivo que estão usando.

_1 imagem(ns) no slide._

### Slide 13

- Conceituando
- Experiência de usuário aprimorada: Como o design responsivo ajusta automaticamente o layout e a aparência do site com base no tamanho da tela do dispositivo, ele garante que os usuários desfrutem de uma experiência consistente e fácil de navegar, seja em um desktop, tablet ou smartphone.
- Manutenção simplificada: Ao criar um único site com design responsivo, os desenvolvedores podem reduzir o tempo e o esforço gastos na manutenção de várias versões de um site para diferentes dispositivos. Isso facilita a atualização e aprimoramento do site ao longo do tempo.
- https://slideplayer.com.br/slide/3284708/11/images/5/Exemplo+Form+GET+%3Chtml%3E.jpg

_1 imagem(ns) no slide._

### Slide 14

- Conceituando
- Melhor desempenho nos mecanismos de busca: O design responsivo também é benéfico para a otimização de mecanismos de busca (SEO), pois os mecanismos de busca, como o Google, tendem a favorecer sites responsivos em seus resultados de pesquisa.
- Em resumo, o design responsivo em HTML é uma abordagem importante e eficaz para criar sites que ofereçam uma experiência de usuário otimizada e acessível em uma ampla variedade de dispositivos e navegadores.
- https://slideplayer.com.br/slide/3284708/11/images/5/Exemplo+Form+GET+%3Chtml%3E.jpg

_1 imagem(ns) no slide._

### Slide 15

- Ainda sobre o HTML, vamos conhecer praticando?
- Na plataforma Alura vamos acessar o seguinte curso:
- Link para o curso: https://cursos.alura.com.br/course/html5-css3-avancando-css
- Ao longo das atividades, você vai encontrar alguns quizzes e eles não estão ali por acaso! Eles são oportunidades rápidas para testar seu entendimento, reforçar o que aprendeu e identificar pontos que ainda podem melhorar.

_3 imagem(ns) no slide._

### Slide 16

- Meta tag de Viewport
- 8 minutos
- Nesta aula, discutiremos sobre as versões mobile do nosso site, isto é, as adaptações necessárias para que o site seja visualizado corretamente em dispositivos móveis.
- Link para tarefa: https://cursos.alura.com.br/course/html5-css3-avancando-css/task/63330
- Hoje em dia, a maior parte do fluxo de usuários na internet é proveniente de celulares, portanto um site não responsivo a tal necessidade é um problema.
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 17

- Adaptar uma página para celular
- 6 minutos
- Adaptar cenários web para mobile é de extrema importância para seus usuários.
- Link para tarefa: https://cursos.alura.com.br/course/html5-css3-avancando-css/task/63331
- De maneira bem objetiva e dinâmica, adaptaremos nosso site para que ele se torne responsivo, ou seja, que se comporte de maneira adequada no desktop e em dispositivos móveis.
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 18

- Vamos praticar?
- Prepare-se, porque nessa atividade, você vai sair do modo aprender e entrar direto no modo praticar.
- A atividade prática vai colocar você diante de um desafio real, que faz relação com o conteúdo aprendido até aqui.

_1 imagem(ns) no slide._

### Slide 19

- O que vimos na aula de hoje:
- Aprendemos sobre design responsivo: como ajustar o estilo da nossa página de acordo com o tamanho da tela do dispositivo que a acesse.

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

_Fonte: AULA 41_ATIVIDADE_PROGRAMAÇÃO FRONT END.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação Front-End

2ª SÉRIE

ATIVIDADE AULA 41

Questão 1

O que é design responsivo em páginas HTML?

a) Um design que usa apenas imagens vetoriais para melhor qualidade.

b) Um design que se adapta automaticamente ao tamanho e orientação do dispositivo do usuário.

c) Um design que utiliza apenas um tipo de fonte para melhor legibilidade.

d) Um design que prioriza a velocidade de carregamento em detrimento da estética.

Comentário: A resposta correta é a alternativa "b". O design responsivo é uma abordagem de design web que faz com que as páginas HTML se adaptem automaticamente ao tamanho e à orientação do dispositivo do usuário, proporcionando uma experiência de usuário otimizada em diferentes dispositivos, como desktops, tablets e smartphones.

Questão 2

Qual é a propriedade CSS usada para aplicar estilos condicionais com base na largura da tela do dispositivo do usuário?

a) @device

b) @screen

c) @viewport

d) @media

Comentário: A resposta correta é a alternativa "d". A regra @media é usada para aplicar estilos condicionais com base na largura da tela do dispositivo do usuário. Essa regra permite que os desenvolvedores criem designs responsivos, ajustando o layout e a aparência das páginas HTML de acordo com as características do dispositivo em uso. As outras alternativas não são regras CSS válidas para estilização condicional baseada na largura da tela.

## Prática

_Fonte: AULA 41_PRÁTICA_PROGRAMAÇÃO FRONT END.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

PROGRAMAÇÃO FRONT END

2ª SÉRIE

ATIVIDADE PRÁTICA AULA 41

##### 1. Objetivo da Aula Prática

Ao final da aula prática, o estudante será capaz de:

- Compreender o conceito de design responsivo.
- Adaptar páginas HTML para diferentes tamanhos de tela.
- Utilizar a meta tag viewport corretamente.
- Aplicar regras CSS com @media.
- Ajustar elementos para visualização em dispositivos móveis.
Produto final esperado:

- Página HTML adaptada para desktop e dispositivos móveis, com layout responsivo funcional.

##### 2. Ferramentas Recomendadas

###### VS Code ou Editor HTML

- Para que serve: editar HTML e CSS da página.
- Por que é adequado: permite testar rapidamente alterações responsivas.
- Como facilita o aprendizado: possibilita organizar estilos desktop e mobile.

###### Navegador Web

- Para que serve: visualizar e testar responsividade.
- Por que é adequado: permite simular telas diferentes.
- Como facilita o aprendizado: possibilita testar comportamento real do layout.

###### Ferramenta DevTools do Navegador

- Para que serve: simular celulares e tablets.
- Por que é adequado: facilita testes responsivos sem precisar de vários dispositivos.
- Como facilita o aprendizado: mostra alterações em tempo real.

##### 3. Checklist Inicial

Antes de iniciar a prática, o estudante deve ter:

- Projeto HTML funcionando
- Arquivo CSS externo configurado
- Página estilizada das aulas anteriores
- Navegador atualizado
- Conexão com internet
Material de apoio indicado na aula: https://cursos.alura.com.br/course/html5-css3-avancando-css

##### 4. Passo a Passo do Docente (Aula de até 50 minutos)

###### Preparações necessárias

- Garantir que todos tenham o projeto aberto.
- Revisar rapidamente:
- Estrutura HTML
- CSS externo
- Largura de elementos

###### Condução da aula

###### Contextualização (5 minutos)

Apresentar cenário:

- Grande parte dos acessos hoje ocorre pelo celular.
Perguntar:

- O que acontece quando um site não funciona bem no celular?

###### Conceituando design responsivo (10 minutos)

Explicar:

- Responsividade = adaptação automática do layout.
Apresentar:

###### Meta viewport

- <meta name="viewport" content="width=device-width, initial-scale=1.0">
Explicar função:

- Ajustar escala da página no dispositivo.

###### Trabalhando com media queries (15 minutos)

Explicar:

###### @media

Permite aplicar estilos específicos conforme tamanho da tela.

Exemplo conceitual:

- @media screen and (max-width: 768px) {
- body {
- background-color: lightgray;
- }
- }
Demonstrar:

- Alteração de:
- largura
- menu
- imagens
- fontes

###### Prática guiada (15 minutos)

Alunos devem:

- Inserir meta viewport.
- Criar media query.
- Ajustar layout para celular.
- Testar no DevTools.

###### Revisão e fechamento (5 minutos)

- Testar versão mobile.
- Ajustar elementos quebrados.
- Verificar legibilidade.

###### Pontos de atenção

- Evitar elementos muito largos.
- Garantir leitura em telas pequenas.
- Testar constantemente em diferentes tamanhos.

##### 5. Atividade Prática — Descrição Geral

O estudante deverá:

- Adaptar a página criada anteriormente para dispositivos móveis.
- Inserir a meta tag viewport.
- Criar regras responsivas usando media query.
- Ajustar:
- menu
- imagens
- textos
- espaçamentos
Problema real simulado: Adaptação de um site desktop para uso em smartphones.

Habilidade desenvolvida: Desenvolvimento de layouts responsivos.

##### 6. Metodologia Ativa Utilizada

- Aprendizagem baseada em projeto
- Experimentação prática
- Ensino por descoberta
- Elementos de Lemov:
- Modelagem
- Prática guiada
- Verificação de entendimento
- Feedback imediato

##### 7. Passo a Passo da Atividade Prática (para os alunos)

- Abra seu projeto HTML.
- Localize a tag <head>.
- Adicione a meta viewport.
- Abra o arquivo style.css.
- Crie uma media query:
- max-width: 768px
- Dentro da media query:
- reduza larguras fixas
- ajuste tamanho das fontes
- reorganize elementos
- Ajuste imagens:
- largura máxima
- Ajuste menu para telas pequenas.
- Salve os arquivos.
- Abra o navegador.
- Utilize o modo responsivo do DevTools.
- Teste diferentes tamanhos de tela.
- Ajuste o layout, se necessário.

##### 8. Exemplo ou Demonstração

###### Exemplo de viewport

- <meta name="viewport" content="width=device-width, initial-scale=1.0">

###### Exemplo de media query

- @media screen and (max-width: 768px) {
- .menu {
- width: 100%;
- }
- }

###### Conceitos reforçados

- Responsividade melhora experiência do usuário.
- Um único site pode funcionar em vários dispositivos.
- CSS adapta layout dinamicamente.

##### 9. Resultado Esperado

O estudante deverá apresentar:

- Página funcionando em desktop e mobile.
- Uso correto de:
- meta viewport
- media query
- Layout adaptado para telas menores.
- Código organizado.
O professor verifica:

- Funcionamento responsivo.
- Legibilidade em telas pequenas.
- Organização visual da página.

##### 10. Formato de Entrega da Atividade

- Formato: Pasta do projeto contendo:
- index.html
- style.css
- demais arquivos do projeto
- Entrega: ao final da aula.
- Prazo sugerido: imediato.

##### 11. Encerramento e Reflexão

Perguntas orientadoras:

- Por que responsividade é importante hoje?
- O que muda entre desktop e celular?
- Como o CSS ajuda a adaptar layouts?
