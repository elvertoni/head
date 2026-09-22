---
titulo: "Melhorando a Semântica do HTML"
tipo: rco-seed
disciplina: programacao-front-end
sigla_rco: PFE
trimestre: 1
ordem_rco: 29
serie: 2
aula_rco: "Aula 29"
slides: 21
tem_atividade: true
tem_pratica: true
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/1TRI/29-melhorando-a-semantica-do-html/29-melhorando-a-semantica-do-html.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/1TRI/29-melhorando-a-semantica-do-html/AULA 29 ATIVIDADE PROGRAMAÇÃO FRONT END I.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/1TRI/29-melhorando-a-semantica-do-html/AULA 29_PRÁTICA_PROGRAMAÇÃO FRONT END.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Melhorando a Semântica do HTML

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- Programação Front-End
- 2ª Série
- Melhorando a Semântica do HTML
- Aula 29

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
- Aprimorar e melhorar a semântica em páginas HTML.
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
- https://caelum-online-public.s3.amazonaws.com/1309-html5-css3-formulario-tabela/03/aula-3-completa.zip
- Complemento:
- https://cursos.alura.com.br/course/html5-css3-primeiros-passos/task/581966

_2 imagem(ns) no slide._

### Slide 6

- Aula anterior
- Implementamos recursos avançados nos formulários HTML, vimos os diferentes campos que podem ser utilizados em um form.

_1 imagem(ns) no slide._

### Slide 7

- Para pensarmos juntos...
- Joana, uma desenvolvedora web júnior, recebeu a tarefa de criar a página inicial de um site de comércio eletrônico chamado "Bazar das Plantas". Ela estava empolgada para aplicar seus conhecimentos de HTML e CSS, mas não tinha muita experiência com semântica aplicada em páginas HTML.

_1 imagem(ns) no slide._

### Slide 8

- Para pensarmos juntos...
- Ao criar a página, Joana usou principalmente as tags HTML padrão, como <div>, <span> e <table>, para organizar o conteúdo e a estrutura da página. No entanto, ao analisar a página, seu mentor percebeu que faltava uma estrutura semântica clara, o que dificultaria a acessibilidade e a indexação pelos mecanismos de busca. Como Joana poderia melhorar a semântica da página HTML para torná-la mais acessível e amigável aos mecanismos de busca?
- Dialogue com o colega e socialize as ideias com a turma no final!

_3 imagem(ns) no slide._

### Slide 9

- Resposta
- Joana poderia melhorar a semântica da página HTML utilizando as tags semânticas adequadas, que fornecem informações claras sobre o propósito de cada seção do conteúdo. Exemplo:
- <header> <nav> <main> <article> <section>

_1 imagem(ns) no slide._

### Slide 10

- Conceituando
- Semântica, em páginas HTML, refere-se ao uso de elementos e atributos específicos para transmitir significado e estrutura ao conteúdo da página. O uso adequado de elementos semânticos ajuda a tornar o conteúdo mais claro e acessível, tanto para os usuários, quanto para os mecanismos de busca, facilitando a manutenção e a estilização das páginas.
- https://i.stack.imgur.com/paa02.jpg

_1 imagem(ns) no slide._

### Slide 11

- Conceituando
- Os elementos semânticos do HTML5, como <header>, <nav>, <main>, <article> e <footer>, fornecem contexto e informações sobre o propósito de diferentes seções do conteúdo. Ao utilizar esses elementos, os desenvolvedores podem criar páginas com uma estrutura lógica e compreensível, melhorando a acessibilidade para pessoas com deficiências e otimizando a indexação pelos mecanismos de busca.
- https://slideplayer.com.br/slide/3284708/11/images/5/Exemplo+Form+GET+%3Chtml%3E.jpg

_1 imagem(ns) no slide._

### Slide 12

- Conceituando
- Além de melhorar a acessibilidade e a otimização para mecanismos de busca, a semântica em páginas HTML também facilita o trabalho de outros desenvolvedores, permitindo que compreendam e modifiquem o código com mais facilidade. O uso de elementos semânticos contribui para a construção de páginas web mais eficientes, funcionais e fáceis de manter.
- https://algol.dev/wp-content/uploads/2020/10/font_code-compressor.jpg

_1 imagem(ns) no slide._

### Slide 13

- Link para o curso: https://cursos.alura.com.br/course/html5-css3-formularios-tabelas
- A recomendação é que você continue esse curso extraclasse, pois ele traz um conteúdo essencial para compreender sobre o referido tema.
- Atividade Prática na Plataforma Alura
- Na plataforma Alura vamos acessar o seguinte curso:

_3 imagem(ns) no slide._

### Slide 14

- Inputs para celulares
- Seguindo na criação do nosso formulário, não se esqueça da acessibilidade e de facilitar a vida do usuário.
- Link para tarefa: https://cursos.alura.com.br/course/html5-css3-formularios-tabelas/task/60676
- Quando falamos de formulário, existem algumas coisas muito importantes que o HTML5 criou para facilitar a vida de quem está usando o celular, por exemplo. É importante falar disso, porque hoje a maioria do acesso à internet é via celular.
- Atividade no portal Alura
- 5 minutos
- Atividade no portal Alura

_5 imagem(ns) no slide._

### Slide 15

- Dados importantes nos inputs
- Agora que já melhoramos os tipos dos inputs do nosso formulário, vamos deixá-lo ainda mais completo e mais fácil de ser preenchido.
- Link para tarefa: https://cursos.alura.com.br/course/html5-css3-formularios-tabelas/task/60677
- Uma das coisas que sempre acontecem no formulário, são os campos obrigatórios. Quando o usuário está preenchendo o formulário para envio de um contato ou mensagem, é importante conhecer os dados da mensagem que ele está enviando.
- 6 minutos
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 16

- Melhorando a semântica do formulário
- Nosso formulário já está ficando bem completo e com uma semântica excelente!
- Link para tarefa: https://cursos.alura.com.br/course/html5-css3-formularios-tabelas/task/60678
- Precisamos corrigir na semântica do nosso formulário, para que fique ainda melhor, é a criação do campo de input e do campo select e para uma melhor organização do nosso código, utiliza-se a tag da div e a tag do parágrafo.
- 5 minutos
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 17

- Vamos praticar?
- Prepare-se, porque agora você vai sair do modo aprender e entrar no modo organizar seu código como um profissional.
- Nesta atividade, você irá melhorar a estrutura da sua página utilizando tags semânticas e aprimorar o formulário com recursos que facilitam o uso e a leitura.
- É o momento de transformar seu projeto em um código mais claro, acessível e bem estruturado.

_1 imagem(ns) no slide._

### Slide 18

- O que vimos na aula de hoje:
- Aprendemos alguns tipos de inputs para celular: email, tel, number, password, date, datetime, month e search.
- Aprendemos como não permitir que um campo não seja preenchido, através do atributo required.
- Aprendemos Como exibir uma sugestão de preenchimento para os campos, através do atributo placeholder.

_1 imagem(ns) no slide._

### Slide 19

- Pronto para desbloquear sua carreira de TI?
- Está perdido estudando mas não sabe por onde começar? Se a resposta é sim, você está no lugar certo! Descubra as estratégias e ferramentas essenciais para te ajudar a desbloquear seu potencial em TI e buscar sua primeira vaga de emprego no setor!
- Este e-book é um guia completo para quem busca começar pelos melhores caminhos para se tornar um excelente profissional de TI, ensinando a identificar perfis profissionais, aplicar técnicas de estudo eficazes, transformar teoria em prática, e aumentar a visibilidade de seu trabalho no mercado de trabalho. Ideal para novatos e profissionais em transição.
- E o melhor, ele pode ser seu, inteiramente grátis!
- Basta clicar AQUI e realizar o seu cadastro com o seu @escola!

_3 imagem(ns) no slide._

### Slide 20

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

### Slide 21

_(sem texto)_

## Atividade

_Fonte: AULA 29 ATIVIDADE PROGRAMAÇÃO FRONT END I.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação Front-End

2ª SÉRIE

ATIVIDADE AULA 29

Questão 1

Qual elemento HTML deve ser usado para associar um rótulo a um campo de entrada em um formulário, melhorando a semântica e a acessibilidade?

a) label

b) legend

c) caption

d) title

Resposta correta: a) label

Comentário: O elemento "label" deve ser usado para associar um rótulo a um campo de entrada em um formulário. Isso melhora a semântica e a acessibilidade, pois permite que os usuários cliquem no rótulo para focar no campo de entrada associado, e também fornece informações contextuais adicionais para tecnologias assistivas, como leitores de tela.

Questão 2

Qual elemento HTML pode ser utilizado para agrupar logicamente campos de entrada relacionados em um formulário, aprimorando a organização e a semântica do código?

a) group

b) fieldset

c) section

d) container

Resposta correta: b) fieldset

Comentário: O elemento "fieldset" pode ser usado para agrupar logicamente campos de entrada relacionados em um formulário. Isso melhora a organização e a semântica do código, facilitando a compreensão da estrutura do formulário e fornecendo um contexto adicional aos usuários e tecnologias assistivas. O elemento "legend" pode ser usado em conjunto com "fieldset" para fornecer um rótulo ao grupo de campos.

## Prática

_Fonte: AULA 29_PRÁTICA_PROGRAMAÇÃO FRONT END.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

PROGRAMAÇÃO FRONT END

2ª SÉRIE

ATIVIDADE PRÁTICA AULA 29

##### 1. Objetivo da Aula Prática

Ao final da aula prática, o estudante será capaz de:

- Aplicar corretamente tags semânticas do HTML5 (<header>, <nav>, <main>, <section>, <article>, <footer>).
- Melhorar a estrutura de uma página substituindo <div> genéricas por elementos semânticos.
- Utilizar atributos como required e placeholder em formulários.
- Compreender a importância da semântica para acessibilidade e SEO.
- Organizar melhor o código HTML para facilitar manutenção e leitura.
Produto final esperado:

- Página HTML com estrutura semântica aprimorada e formulário mais completo e acessível.

##### 2. Ferramentas Recomendadas

###### VS Code ou Editor HTML

- Para que serve: editar e reorganizar a estrutura HTML.
- Por que é adequado: permite refatoração do código.
- Como facilita o aprendizado: visualização clara da organização semântica.

###### Navegador Web

- Para que serve: testar funcionamento da página.
- Por que é adequado: simula experiência real do usuário.
- Como facilita o aprendizado: valida preenchimento e estrutura visual.

###### Editor Online (HTML5 Editor)

- Link: https://html5-editor.net/
- Para que serve: testes rápidos.
- Como facilita o aprendizado: feedback imediato.

##### 3. Checklist Inicial

Antes de iniciar a prática, o estudante deve ter:

- Projeto com páginas HTML (index, produtos, contato)
- Formulário já estruturado (Aula 28)
- CSS funcional
- Navegador atualizado
- Conexão com internet
Material de apoio indicado na aula: https://cursos.alura.com.br/course/html5-css3-formularios-tabelas

##### 4. Passo a Passo do Docente (Aula de até 50 minutos)

###### Preparações necessárias

- Garantir que todos tenham o projeto aberto.
- Revisar rapidamente:
- Estrutura HTML atual
- Uso de <div>

###### Condução da aula

###### Contextualização (5 minutos)

Apresentar o problema:

- Código funcional, mas difícil de entender.
- Falta de organização semântica.
Perguntar:

- Como melhorar a estrutura do site?

###### Conceituando semântica (10 minutos)

Explicar:

- Semântica = significado do conteúdo.
- Importância para:
- Acessibilidade
- SEO
- Organização do código
Apresentar tags semânticas:

- <header>
- <nav>
- <main>
- <section>
- <article>
- <footer>

###### Demonstração do professor (15 minutos)

Demonstrar:

- Substituir <div> por:
- <header> para topo
- <nav> para menu
- <main> para conteúdo
- <section> para agrupamentos
- <footer> para rodapé
Melhorar formulário:

- Adicionar required
- Adicionar placeholder
- Ajustar organização dos campos

###### Prática guiada (15 minutos)

Alunos devem:

- Refatorar estrutura HTML
- Aplicar tags semânticas
- Melhorar formulário
- Testar funcionamento

###### Revisão e fechamento (5 minutos)

- Validar estrutura
- Conferir formulário
- Reforçar boas práticas

###### Pontos de atenção

- Não usar <div> sem necessidade.
- Usar cada tag no contexto correto.
- Garantir clareza na estrutura.

##### 5. Atividade Prática — Descrição Geral

O estudante deverá:

- Melhorar a estrutura semântica da página.
- Substituir <div> por tags adequadas.
- Melhorar formulário com:
- required
- placeholder
- Organizar melhor o código.
Problema real simulado: Refatoração de um site para torná-lo mais acessível e profissional.

Habilidade desenvolvida: Estruturação semântica e organização de código.

##### 6. Metodologia Ativa Utilizada

- Aprendizagem baseada em projeto
- Refatoração prática
- Ensino por descoberta
- Elementos de Lemov:
- Modelagem
- Prática guiada
- Checagem de compreensão
- Feedback imediato

##### 7. Passo a Passo da Atividade Prática (para os alunos)

- Abra seu projeto.
- Localize todas as <div> da página.
- Substitua por:
- <header> no topo
- <nav> no menu
- <main> no conteúdo
- <section> para agrupamentos
- <footer> no rodapé
- Acesse o formulário.
- Adicione required nos campos obrigatórios.
- Adicione placeholder para sugestões.
- Revise organização do HTML.
- Salve o arquivo.
- Teste no navegador.
- Ajuste se necessário.

##### 8. Exemplo ou Demonstração

Estrutura esperada:

Página:

- Header (cabeçalho)
- Nav (menu)
- Main (conteúdo principal)
- Section (conteúdo)
- Footer (rodapé)
Formulário:

- Campos com placeholder
- Campos obrigatórios com required
Conceitos reforçados:

- HTML semântico melhora organização
- Código limpo facilita manutenção
- Acessibilidade melhora experiência

##### 9. Resultado Esperado

O estudante deverá apresentar:

- Página com estrutura semântica correta.
- Uso adequado de:
- <header>
- <nav>
- <main>
- <section>
- <footer>
- Formulário com:
- required
- placeholder
- Código organizado e legível.
O professor verifica:

- Estrutura semântica correta.
- Funcionamento do formulário.
- Clareza e organização do código.

##### 10. Formato de Entrega da Atividade

- Formato: Pasta do projeto contendo:
- index.html
- produtos.html
- contato.html
- style.css
- Entrega: ao final da aula.
- Prazo sugerido: imediato.

##### 11. Encerramento e Reflexão

Perguntas orientadoras:

- Qual a vantagem de usar HTML semântico?
- Como isso impacta acessibilidade?
- Por que isso é importante no mercado?
