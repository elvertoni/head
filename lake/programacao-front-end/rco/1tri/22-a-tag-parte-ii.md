---
titulo: "A Tag <section> – Parte II"
tipo: rco-seed
disciplina: programacao-front-end
sigla_rco: PFE
trimestre: 1
ordem_rco: 22
serie: 2
aula_rco: "Aula 22"
slides: 20
tem_atividade: true
tem_pratica: true
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/1TRI/22-a-tag-parte-ii/22-a-tag-parte-ii.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/1TRI/22-a-tag-parte-ii/AULA 22_ATIVIDADE_PROGRAMAÇÃO FRONT END.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/1TRI/22-a-tag-parte-ii/AULA 22_PRÁTICA_PROGRAMAÇÃO FRONT END.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# A Tag <section> – Parte II

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- Programação Front-End
- 2° Série
- A Tag <section> – Parte II
- Aula 22

_1 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- COMPETÊNCIA(S) A SER(EM) DESENVOLVIDA(S) NESTA AULA:
- De acordo com o Plano de Curso de Desenvolvimento de Sistemas:
- HABILIDADE(S) A SER(EM) DESENVOLVIDA(S) NESTA AULA:
- Codificar aplicações e rotinas utilizando linguagens de programação específicas.
- Estruturar arquitetura dos elementos de conteúdo de websites.

_1 imagem(ns) no slide._

### Slide 4

- Nesta aula vamos:
- Aprender sobre a utilização de tag section em HTML Parte II
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
- Projeto inicial do treinamento:
- https://caelum-online-public.s3.amazonaws.com/1205-html5-css3-parte2/03/aula-3-completa.zip
- Complemento:
- https://cursos.alura.com.br/course/html5-css3-primeiros-passos/task/581966

_2 imagem(ns) no slide._

### Slide 6

- Aula anterior
- Iniciamos os estudos sobre tag section em HTML, e sua importância para a criação de listas complexas e divisões semânticas.

_1 imagem(ns) no slide._

### Slide 7

- Para pensarmos juntos...
- O posicionamento de elementos em HTML também pode ser afetado por fatores como o tamanho da tela do dispositivo que está sendo usado para visualizar a página. Por exemplo, um elemento que é posicionado no canto inferior direito da página em um monitor grande pode ficar oculto em um dispositivo móvel menor.

### Slide 8

- Para pensarmos juntos...
- É importante considerar esses fatores ao criar páginas HTML para garantir que os elementos sejam posicionados de maneira adequada e visível em diferentes dispositivos. Como garantir que os elementos em uma página HTML sejam posicionados corretamente em diferentes dispositivos?
- 3 minutos
- Conversem e apresentem suas visões

_3 imagem(ns) no slide._

### Slide 9

- Resposta
- Para garantir que os elementos em uma página HTML sejam posicionados corretamente em diferentes dispositivos, é importante usar técnicas de design responsivo, como o uso de media queries em CSS. As media queries permitem que a página HTML seja exibida de maneira diferente com base nas características do dispositivo, como tamanho de tela e orientação. Além disso, é importante testar a página em diferentes dispositivos para garantir que os elementos sejam posicionados adequadamente em todas as situações.

_3 imagem(ns) no slide._

### Slide 10

- Conceituando
- Uma dúvida comum relacionada à tag section é em relação à diferença entre ela e a tag div. Enquanto a div é utilizada para agrupar elementos de forma genérica, sem uma semântica específica, a section é utilizada para agrupar conteúdos relacionados e definir seções lógicas na página.

_1 imagem(ns) no slide._

### Slide 11

- Conceituando
- Outra dúvida comum é em relação ao uso adequado da tag section em relação a outras tags como article e main. Enquanto a section é utilizada para agrupar conteúdos relacionados dentro de uma página, a article é utilizada para representar um conteúdo autônomo e independente dentro de uma página, como uma notícia ou um post de blog.

_1 imagem(ns) no slide._

### Slide 12

- Conceituando
- Já a tag main é utilizada para representar o conteúdo principal de uma página. Em resumo, a tag section é utilizada para agrupar conteúdos relacionados em uma página, permitindo uma melhor organização e estruturação do conteúdo.

_1 imagem(ns) no slide._

### Slide 13

- Ainda sobre o HTML, vamos conhecer praticando?
- Na plataforma Alura vamos acessar o seguinte curso:
- Link para o curso: https://cursos.alura.com.br/course/html5-css3-posicionamento-listas-navegacao
- Para melhor entendimento do conteúdo é recomendado que se responda aos quiz que estiverem entre as atividades propostas

_2 imagem(ns) no slide._

### Slide 14

- Reforçando o inline-block
- O nosso objetivo agora é mexer na parte visual desta página.
- Link para tarefa: https://cursos.alura.com.br/course/html5-css3-posicionamento-listas-navegacao/task/59064
- Quando a gente tem uma lista, a lista é um elemento de bloco, ou seja, ele ocupa 100% da largura e cada um dos itens da lista também é um bloco, ele ocupa 100% da largura e o próximo item começa na linha de baixo.
- 11 minutos
- Atividade no portal Alura

_3 imagem(ns) no slide._

### Slide 15

- Ajustando o tamanho dos elementos
- A ideia é mexer nos elementos do espaçamento para a página ficar o mais perfeita possível.
- Link para tarefa: https://cursos.alura.com.br/course/html5-css3-posicionamento-listas-navegacao/task/59065
- Tamanho e posição dos elementos garantem atratividade a uma página HTML, você deve focar um acabamento que seja leve, encontrando uma dose equilibrada de minimalismo.
- 5 minutos
- Atividade no portal Alura

_3 imagem(ns) no slide._

### Slide 16

- Vamos praticar?
- Prepare-se, porque nessa atividade, você vai sair do modo aprender e entrar direto no modo praticar.
- A atividade prática vai colocar você diante de um desafio real, que faz relação com o conteúdo aprendido até aqui.

_1 imagem(ns) no slide._

### Slide 17

- O que vimos na aula de hoje:
- A tag main, para o conteúdo principal da nossa página.
- Criação de listas complexas, com títulos, imagens e parágrafos
- Como utilizar o inline-block

_1 imagem(ns) no slide._

### Slide 18

- Pronto para desbloquear sua carreira de TI?
- Está perdido estudando mas não sabe por onde começar? Se a resposta é sim, você está no lugar certo! Descubra as estratégias e ferramentas essenciais para te ajudar a desbloquear seu potencial em TI e buscar sua primeira vaga de emprego no setor!
- Este e-book é um guia completo para quem busca começar pelos melhores caminhos para se tornar um excelente profissional de TI, ensinando a identificar perfis profissionais, aplicar técnicas de estudo eficazes, transformar teoria em prática, e aumentar a visibilidade de seu trabalho no mercado de trabalho. Ideal para novatos e profissionais em transição.
- E o melhor, ele pode ser seu, inteiramente grátis!
- Basta clicar AQUI e realizar o seu cadastro com o seu @escola!

_3 imagem(ns) no slide._

### Slide 19

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

### Slide 20

_(sem texto)_

## Atividade

_Fonte: AULA 22_ATIVIDADE_PROGRAMAÇÃO FRONT END.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação Front-End

2ª SÉRIE

ATIVIDADE AULA 21

Questão 1

É possível aninhar uma tag <section> dentro de outra tag <section> em HTML?

a) Sim, é possível

b) Não, não é possível

c) Depende da versão do HTML utilizada

d) Nenhuma das alternativas anteriores

Resposta correta: a) Sim, é possível.

Questão 2

Qual é a diferença entre as tags <section> e <div> em HTML?

a) Não há diferença, as duas têm a mesma função

b) A tag <section> é utilizada para agrupar conteúdo relacionado, enquanto a tag <div> é utilizada para agrupar elementos semânticos

c) A tag <section> é utilizada para agrupar elementos semânticos, enquanto a tag <div> é utilizada para agrupar conteúdo relacionado

d) Nenhuma das alternativas anteriores

Resposta correta: b) A tag <section> é utilizada para agrupar conteúdo relacionado, enquanto a tag <div> é utilizada para agrupar elementos semânticos.

## Prática

_Fonte: AULA 22_PRÁTICA_PROGRAMAÇÃO FRONT END.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

PROGRAMAÇÃO FRONT END

2ª SÉRIE

ATIVIDADE PRÁTICA AULA 22

##### 1. Objetivo da Aula Prática

Ao final da aula prática, o estudante será capaz de:

- Consolidar o uso da tag <section> para organização semântica.
- Diferenciar corretamente <section>, <div>, <article> e <main>.
- Aplicar display: inline-block de forma adequada.
- Ajustar tamanho e espaçamento dos elementos.
- Organizar visualmente uma lista complexa de produtos.
- Compreender princípios básicos de design responsivo.
Produto final esperado:

- Página com seção de produtos organizada, alinhada e visualmente equilibrada.

##### 2. Ferramentas Recomendadas

###### VS Code ou Editor HTML

- Para que serve: editar HTML e CSS.
- Por que é adequado: permite estruturação profissional.
- Como facilita o aprendizado: visualização em tempo real do layout.

###### Navegador Web

- Para que serve: testar ajustes visuais.
- Por que é adequado: simula experiência real do usuário.
- Como facilita o aprendizado: permite verificar responsividade.

###### Plataforma Alura

- Para que serve: complementar atividades práticas.
- Por que é adequada: reforça conteúdo com exercícios.
- Como facilita o aprendizado: amplia fixação dos conceitos.

##### 3. Checklist Inicial

Antes de iniciar a prática, o estudante deve ter:

- Página com <main> e <section> criadas
- Lista de produtos estruturada
- CSS aplicado
- Navegador atualizado
- Conexão com internet
Material de apoio indicado na aula: https://cursos.alura.com.br/course/html5-css3-posicionamento-listas-navegacao

##### 4. Passo a Passo do Docente (Aula de até 50 minutos)

###### Preparações necessárias

- Garantir que todos tenham a estrutura da Aula 21.
- Revisar rapidamente:
- Diferença entre <section> e <div>
- Conceito de inline-block

###### Condução da aula

###### Contextualização (5 minutos)

Perguntar:

- O que acontece quando a tela diminui?
- Por que elementos podem ficar desalinhados?
Introduzir conceito básico de responsividade.

###### Revisão semântica (10 minutos)

Explicar:

- <main> → conteúdo principal
- <section> → agrupamento temático
- <article> → conteúdo independente
- <div> → agrupamento genérico
Mostrar diferença prática.

###### Reforçando inline-block (10 minutos)

Explicar:

- Elementos de bloco ocupam 100%.
- display: inline-block permite elementos lado a lado.
Aplicar nos itens da lista de produtos.

###### Ajustando tamanho e espaçamento (15 minutos)

Alunos devem:

- Ajustar largura dos produtos.
- Trabalhar margens externas.
- Ajustar padding interno.
- Centralizar conteúdo.
Foco em acabamento leve e minimalista.

###### Testando visual em diferentes tamanhos (5 minutos)

Reduzir tamanho da janela do navegador.

Observar:

- Quebras de linha.
- Ajustes necessários.
- Organização visual.

###### Pontos de atenção

- Não exagerar nos espaçamentos.
- Manter harmonia visual.
- Conferir alinhamento vertical.

##### 5. Atividade Prática — Descrição Geral

O estudante deverá:

- Ajustar visual da seção de produtos.
- Aplicar inline-block corretamente.
- Definir largura adequada.
- Trabalhar margens e padding.
- Garantir organização visual limpa.
Problema real simulado: Aprimoramento visual da área de produtos de um site institucional.

Habilidade desenvolvida: Prototipação visual e organização semântica responsiva.

##### 6. Metodologia Ativa Utilizada

- Aprendizagem baseada em projeto
- Ensino por descoberta
- Experimentação prática
- Elementos de Lemov:
- Modelagem
- Prática guiada
- Checagem de entendimento
- Feedback imediato

##### 7. Passo a Passo da Atividade Prática (para os alunos)

- Abra seu projeto.
- Localize a <section> de produtos.
- No CSS, aplique display: inline-block nos itens.
- Defina largura aproximada para cada item.
- Ajuste margens externas.
- Ajuste padding interno.
- Centralize o conteúdo.
- Reduza o tamanho da tela do navegador.
- Observe o comportamento.
- Ajuste se necessário.
- Salve o projeto.

##### 8. Exemplo ou Demonstração

Estrutura esperada:

Main └── Section (Produtos) └── Lista com 3 itens lado a lado

Conceitos reforçados:

- Elementos de bloco x inline-block
- Organização semântica
- Ajuste fino de layout

##### 9. Resultado Esperado

O estudante deverá apresentar:

- Uso correto da tag <section>.
- Lista complexa visualmente organizada.
- Elementos lado a lado.
- Espaçamento equilibrado.
- Código limpo e funcional.
O professor verifica:

- Organização semântica.
- Aplicação correta do inline-block.
- Equilíbrio visual.
- Responsividade básica.

##### 10. Formato de Entrega da Atividade

- Formato: Pasta do projeto contendo:
- index.html
- produtos.html
- style.css
- Entrega: ao final da aula.
- Prazo sugerido: imediato.

##### 11. Encerramento e Reflexão

Perguntas orientadoras:

- Qual a diferença entre <section> e <div>?
- Por que inline-block foi necessário?
- O que acontece quando a tela diminui?
- Como o layout pode impactar experiência do usuário?
