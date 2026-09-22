---
titulo: "Iniciando a Criação de Formulários"
tipo: rco-seed
disciplina: programacao-front-end
sigla_rco: PFE
trimestre: 1
ordem_rco: 26
serie: 2
aula_rco: "Aula 26"
slides: 19
tem_atividade: true
tem_pratica: true
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/1TRI/26-iniciando-a-criacao-de-formularios/26-iniciando-a-criacao-de-formularios.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/1TRI/26-iniciando-a-criacao-de-formularios/AULA 26 ATIVIDADE_PROGRAMAÇÃO FRONT END I.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/1TRI/26-iniciando-a-criacao-de-formularios/AULA 26_PRÁTICA_PROGRAMAÇÃO FRONT END.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Iniciando a Criação de Formulários

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- Programação Front-End
- 2ª Série
- Iniciando a Criação de Formulários
- Aula 26

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
- Aprender sobre a construção de formulários em HTML
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
- Projeto da aula anterior:
- https://caelum-online-public.s3.amazonaws.com/1309-html5-css3-formulario-tabela/01/aula-1-completa.zip
- Complemento:
- https://cursos.alura.com.br/course/html5-css3-primeiros-passos/task/581966

_2 imagem(ns) no slide._

### Slide 6

- Aula anterior
- Iniciamos a construção de uma nova página HTML, dessa vez, será uma página de contato, onde é utilizado um formulário.

_1 imagem(ns) no slide._

### Slide 7

- Para pensarmos juntos...
- João trabalha como desenvolvedor web em uma empresa que oferece diversos serviços online. Um de seus projetos recentes envolve a criação de um site para um evento de tecnologia. O site precisa incluir um formulário de inscrição para que os participantes possam se registrar no evento, fornecendo informações como nome, e-mail, telefone e opções de pagamento.
- https://www.ionos.com/digitalguide/fileadmin/DigitalGuide/Teaser/html-tagst.jpg

_1 imagem(ns) no slide._

### Slide 8

- Para pensarmos juntos...
- Os formulários HTML são uma parte crucial do desenvolvimento web, pois permitem a coleta de informações dos usuários e a comunicação dessas informações ao servidor para processamento. Essas informações podem ser usadas para fins variados, como registro de usuário, pedidos de produtos, inscrições em eventos, entre outros. Como João pode garantir que os participantes forneçam um endereço de e-mail válido no formulário de inscrição?
- https://www.seobility.net/en/wiki/images/a/a6/HTML-Doctype.png
- Escolhendo alguém para responder essa questão!

_2 imagem(ns) no slide._

### Slide 9

- Resposta
- João pode utilizar o atributo "type" do elemento <input> com o valor "email" para garantir que os usuários forneçam um endereço de e-mail válido. O navegador automaticamente verifica se o valor inserido no campo corresponde ao formato de um endereço de e-mail e, caso contrário, exibe uma mensagem de erro.

_1 imagem(ns) no slide._

### Slide 10

- Conceituando
- Os formulários HTML desempenham um papel fundamental na interação entre os usuários e os sites, permitindo a coleta e envio de informações para os servidores. Eles fornecem uma maneira eficiente e estruturada de coletar dados dos usuários, como informações de contato, preferências, feedback e muito mais. Isso, por sua vez, possibilita aos desenvolvedores criar experiências personalizadas, melhorar a qualidade dos serviços oferecidos e tomar decisões embasadas em informações fornecidas pelos usuários.
- https://ayltoninacio.com.br/img/p/32w1500.jpg

_1 imagem(ns) no slide._

### Slide 11

- Conceituando
- A importância dos formulários HTML vai além da simples coleta de dados, pois também ajudam na acessibilidade e na usabilidade dos sites. Ao utilizar elementos e atributos específicos de formulários, os desenvolvedores podem garantir que os campos sejam preenchidos corretamente e que os dados sejam validados antes de serem enviados, reduzindo a necessidade de intervenção manual e aumentando a eficiência do processamento dessas informações. Além disso, os formulários bem projetados contribuem para uma melhor experiência do usuário, facilitando a navegação e interação com os sites.
- https://dri.es/files/images/blog/wikipedia-timbl-markup.png

_1 imagem(ns) no slide._

### Slide 12

- Link para o curso: https://cursos.alura.com.br/course/html5-css3-formularios-tabelas
- A recomendação é que você continue esse curso extraclasse, pois ele traz um conteúdo essencial para compreender sobre o referido tema.
- Atividade Prática na Plataforma Alura
- Na plataforma Alura vamos acessar o seguinte curso:

_3 imagem(ns) no slide._

### Slide 13

- Campos básicos
- amos então começar a criação do nosso formulário. Nosso formulário tem sempre uma estrutura que é algo para agrupar todas as informações que o usuário está inserindo.
- Link para tarefa: https://cursos.alura.com.br/course/html5-css3-formularios-tabelas/task/60670
- Se olharmos no nosso HTML, dentro do main, a primeira tag que nós precisamos criar é a tag do formulário.
- 8 minutos
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 14

- Estilos para o formulário
- Seguindo a estrutura que fizemos nos módulos anteriores, nós fizemos um pouco de HTML e um pouco do CSS.
- Link para tarefa: https://cursos.alura.com.br/course/html5-css3-formularios-tabelas/task/60671
- Verificar se está tudo certo, conferir o CSS para saber se estará minimamente aceitável. Testes sempre serão válidos.
- 7 minutos
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 15

- Vamos praticar?
- Prepare-se, porque agora você vai sair do modo aprender e entrar no modo construir formulários de verdade.
- Nesta atividade, você irá criar campos de entrada como nome, e-mail, telefone e mensagem, estruturando um formulário funcional e aplicando validações básicas.
- É o momento de desenvolver uma parte essencial de qualquer sistema: a coleta de dados do usuário.

_1 imagem(ns) no slide._

### Slide 16

- O que vimos na aula de hoje:
- Aprendemos a criar um formulário HTML
- Aprendemos que a tag que o representa o formulário é a tag <form> .
- Aprendemos a estilizar o nosso formulário.

_1 imagem(ns) no slide._

### Slide 17

- Pronto para desbloquear sua carreira de TI?
- Está perdido estudando mas não sabe por onde começar? Se a resposta é sim, você está no lugar certo! Descubra as estratégias e ferramentas essenciais para te ajudar a desbloquear seu potencial em TI e buscar sua primeira vaga de emprego no setor!
- Este e-book é um guia completo para quem busca começar pelos melhores caminhos para se tornar um excelente profissional de TI, ensinando a identificar perfis profissionais, aplicar técnicas de estudo eficazes, transformar teoria em prática, e aumentar a visibilidade de seu trabalho no mercado de trabalho. Ideal para novatos e profissionais em transição.
- E o melhor, ele pode ser seu, inteiramente grátis!
- Basta clicar AQUI e realizar o seu cadastro com o seu @escola!

_3 imagem(ns) no slide._

### Slide 18

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

### Slide 19

_(sem texto)_

## Atividade

_Fonte: AULA 26 ATIVIDADE_PROGRAMAÇÃO FRONT END I.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação Front-End

2ª SÉRIE

ATIVIDADE AULA 26

Questão 1

Qual elemento HTML é utilizado para criar um campo de entrada de texto em um formulário?

a) <input type="textbox">

b) <input type="text">

c) <textfield>

d) <textinput>

Resposta correta: b) <input type="text">

Comentário: O elemento <input type="text"> é usado para criar um campo de entrada de texto em um formulário HTML. Ele permite que os usuários insiram informações em texto, como nome, endereço de e-mail, etc.

Questão 2

Qual elemento HTML é usado para criar um botão de envio que submete o formulário?

a) <button type="submit">

b) <input type="submit">

c) <submitbutton>

d) <formbutton>

Resposta correta: b) <input type="submit">

Comentário: O elemento <input type="submit"> é usado para criar um botão de envio em um formulário HTML. Quando o usuário clica neste botão, os dados do formulário são enviados ao servidor para processamento. O elemento <button type="submit"> também pode ser usado, mas <input type="submit"> é mais comum em conteúdo para iniciantes.

## Prática

_Fonte: AULA 26_PRÁTICA_PROGRAMAÇÃO FRONT END.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

PROGRAMAÇÃO FRONT END

2ª SÉRIE

ATIVIDADE PRÁTICA AULA 26

##### 1. Objetivo da Aula Prática

Ao final da aula prática, o estudante será capaz de:

- Compreender a estrutura básica de um formulário HTML.
- Utilizar corretamente a tag <form> para agrupar campos.
- Criar campos de entrada utilizando <input> com diferentes tipos.
- Aplicar validação básica utilizando atributos como type="email".
- Estruturar um formulário inicial funcional e organizado.
Produto final esperado:

- Página de contato contendo formulário com campos básicos (nome, e-mail, telefone e mensagem) com validação simples.

##### 2. Ferramentas Recomendadas

###### VS Code ou Editor HTML

- Para que serve: criar e editar formulários em HTML.
- Por que é adequado: permite organização do código e prática profissional.
- Como facilita o aprendizado: visualização clara da estrutura do formulário.

###### Navegador Web

- Para que serve: testar funcionamento e validação dos campos.
- Por que é adequado: simula interação real do usuário.
- Como facilita o aprendizado: permite observar erros e validações automáticas.

###### Editor Online (HTML5 Editor)

- Link: https://html5-editor.net/
- Para que serve: testes rápidos.
- Como facilita o aprendizado: feedback imediato.

##### 3. Checklist Inicial

Antes de iniciar a prática, o estudante deve ter:

- Página contato.html criada na aula anterior
- Estrutura HTML básica pronta
- CSS externo vinculado
- Navegador atualizado
- Conexão com internet
Material de apoio indicado na aula: https://cursos.alura.com.br/course/html5-css3-formularios-tabelas

##### 4. Passo a Passo do Docente (Aula de até 50 minutos)

###### Preparações necessárias

- Garantir que todos tenham a página de contato criada.
- Revisar rapidamente:
- Estrutura HTML
- Tag <form>

###### Condução da aula

###### Contextualização (5 minutos)

Apresentar o cenário:

- Cadastro em eventos
- Inscrição em sites
- Coleta de dados do usuário
Perguntar:

- Como garantir que o usuário digite um e-mail válido?

###### Conceituação (10 minutos)

Explicar:

- <form> → agrupa os dados
- <input> → campo de entrada
- type → define tipo do dado
Apresentar exemplos:

- text
- email
- tel
Destacar validação automática do navegador.

###### Demonstração do professor (15 minutos)

Demonstrar:

- Inserir <form> dentro do <main>
- Criar campos:
- Nome
- E-mail
- Telefone
- Associar <label> aos campos
- Inserir botão de envio
Testar validação de e-mail no navegador.

###### Prática guiada (15 minutos)

Alunos devem:

- Criar formulário completo
- Inserir campos básicos
- Aplicar tipo correto em cada campo
- Testar validação

###### Revisão e fechamento (5 minutos)

- Testar formulário
- Corrigir erros
- Reforçar boas práticas

###### Pontos de atenção

- Verificar uso correto do atributo type.
- Conferir associação entre <label> e <input>.
- Garantir organização visual.

##### 5. Atividade Prática — Descrição Geral

O estudante deverá:

- Criar ou completar um formulário na página de contato.
- Inserir campos:
- Nome
- E-mail
- Telefone
- Mensagem
- Aplicar validação básica (email).
- Testar funcionamento no navegador.
Problema real simulado: Criar formulário de inscrição para evento.

Habilidade desenvolvida: Construção de interfaces interativas com validação básica.

##### 6. Metodologia Ativa Utilizada

- Aprendizagem baseada em projeto
- Ensino por descoberta
- Experimentação prática
- Elementos de Lemov:
- Modelagem
- Prática guiada
- Checagem de compreensão
- Feedback imediato

##### 7. Passo a Passo da Atividade Prática (para os alunos)

- Abra a página contato.html.
- Localize a área do conteúdo principal.
- Crie a tag <form>.
- Adicione um campo de nome (input type="text").
- Adicione um campo de e-mail (input type="email").
- Adicione um campo de telefone (input type="tel").
- Adicione um campo de mensagem (textarea).
- Crie <label> para cada campo.
- Adicione botão de envio.
- Salve e abra no navegador.
- Teste a validação do campo e-mail.
- Ajuste se necessário.

##### 8. Exemplo ou Demonstração

Estrutura esperada:

Formulário:

- Nome → texto
- E-mail → validação automática
- Telefone → entrada numérica
- Mensagem → campo maior
- Botão → envio
Conceitos reforçados:

- HTML coleta dados
- Navegador valida dados
- Formulário conecta usuário ao sistema

##### 9. Resultado Esperado

O estudante deverá apresentar:

- Formulário completo na página.
- Uso correto de:
- <form>
- <input>
- <label>
- Validação funcionando no campo de e-mail.
- Código organizado.
O professor verifica:

- Funcionamento do formulário.
- Estrutura correta.
- Uso adequado dos tipos de input.

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

- Por que usar type="email"?
- O que acontece se o usuário digitar errado?
- Como formulários são usados em sistemas reais?
