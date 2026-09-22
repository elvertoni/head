---
titulo: "Tipos de campos diferentes Parte I"
tipo: rco-seed
disciplina: programacao-front-end
sigla_rco: PFE
trimestre: 1
ordem_rco: 27
serie: 2
aula_rco: "Aula 27"
slides: 19
tem_atividade: true
tem_pratica: true
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/1TRI/27-tipos-de-campos-em-formularios-parte-i/27-tipos-de-campos-em-formularios-parte-i.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/1TRI/27-tipos-de-campos-em-formularios-parte-i/AULA 27 ATIVIDADE_PROGRAMAÇÃO FRONT END I.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/1TRI/27-tipos-de-campos-em-formularios-parte-i/AULA 27_PRÁTICA_PROGRAMAÇÃO FRONT END.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Tipos de campos diferentes Parte I

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- Programação Front-End
- 2ª Série
- Tipos de campos diferentes Parte I
- Aula 27

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
- Aprimorar os formulários criados na aula anterior e entender a diferença entre campos Parte I.
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
- https://caelum-online-public.s3.amazonaws.com/1309-html5-css3-formulario-tabela/02/aula-2-completa.zip
- Complemento:
- https://cursos.alura.com.br/course/html5-css3-primeiros-passos/task/581966

_2 imagem(ns) no slide._

### Slide 6

- Aula anterior
- Iniciamos uma nova página em HTML destinada a um formulário de contato para o projeto da página, nesse caso criamos apenas o projeto, agora iremos aprimorar os recursos.

_1 imagem(ns) no slide._

### Slide 7

- Para pensarmos juntos...
- Joana é a desenvolvedora responsável por criar um site de inscrição para uma conferência online. Ela precisa criar um formulário que colete informações relevantes dos participantes, como nome, e-mail, data de nascimento e se eles gostariam de receber atualizações por e-mail sobre futuros eventos.
- Qual tipo de campo de entrada HTML Joana deve usar para coletar o endereço de e-mail dos participantes?
- Realizem a atividade em duplas e socializem no final!

_2 imagem(ns) no slide._

### Slide 8

- Resposta
- Joana deve usar o tipo de campo de entrada "email" para coletar o endereço de e-mail dos participantes. Esse tipo de campo verifica se o valor inserido é um endereço de e-mail válido e, geralmente, exibe um teclado específico para e-mails nos dispositivos móveis.

_1 imagem(ns) no slide._

### Slide 9

- Conceituando
- Os formulários HTML são uma parte fundamental da interação entre usuários e websites, permitindo que os visitantes insiram informações e façam escolhas que podem ser coletadas e processadas pelos servidores. Esses formulários são compostos por diferentes tipos de campos de entrada, cada um projetado para lidar com informações específicas, como texto, números, datas, arquivos e seleções.
- http://www.hiperbytes.com.br/wp-content/uploads/2014/01/Cap7Exercicio.jpg

_1 imagem(ns) no slide._

### Slide 10

- Conceituando
- A escolha correta do tipo de campo de entrada é crucial para garantir a qualidade e a integridade dos dados coletados, bem como para proporcionar uma experiência de usuário mais amigável e acessível.

_1 imagem(ns) no slide._

### Slide 11

- Link para o curso: https://cursos.alura.com.br/course/html5-css3-formularios-tabelas
- A recomendação é que você continue esse curso extraclasse, pois ele traz um conteúdo essencial para compreender sobre o referido tema.
- Atividade Prática na Plataforma Alura
- Na plataforma Alura vamos acessar o seguinte curso:

_3 imagem(ns) no slide._

### Slide 12

- Formulários mais complexos
- Seguindo na criação do nosso formulário, já temos os campos básicos de nome e sobrenome, e-mail e telefone.
- Link para tarefa: https://cursos.alura.com.br/course/html5-css3-formularios-tabelas/task/60672
- No nosso exemplo, temos campos bem mais complexos. Por exemplo, o campo de mensagem, onde é possível escrever qualquer coisa. E, em outras situações, como receber um contato por e-mail, ligação ou WhatsApp.
- 14 minutos
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 13

- CSS para formulários complexos
- Agora que já temos os campos mais complexos, vamos trabalhar no CSS deles.
- Link para tarefa: https://cursos.alura.com.br/course/html5-css3-formularios-tabelas/task/60673
- Vamos configurar para que o nosso textarea seja do mesmo tamanho do nosso input. Modificamos a quantidade de colunas do textarea para que ele tenha um tamanho maior e que ele possa ter mais conteúdo escrito.
- 7 minutos
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 14

- Fixando conteúdo
- Cada tipo de campo de entrada tem seu próprio conjunto de atributos e comportamentos. Por exemplo, campos do tipo "e-mail" validam automaticamente se o valor inserido corresponde a um formato de endereço de e-mail válido, enquanto campos do tipo "password" ocultam os caracteres digitados pelos usuários. Além disso, alguns campos, como "date" e "color", podem exibir um seletor específico no navegador, facilitando a escolha do usuário e garantindo que os dados inseridos estejam no formato correto.
- https://s3-us-west-2.amazonaws.com/staticresources123/site/other/landings/php-contact-form/contact-form.png

_1 imagem(ns) no slide._

### Slide 15

- Vamos praticar?
- Prepare-se, porque agora você vai sair do modo aprender e entrar no modo evoluir seu formulário.
- Nesta atividade, você irá adicionar novos tipos de campos, como senha, data e mensagem, tornando o formulário mais completo e próximo de aplicações reais.
- É o momento de entender como escolher o campo certo para cada tipo de informação e melhorar a experiência do usuário.

_1 imagem(ns) no slide._

### Slide 16

- O que vimos na aula de hoje:
- Aprendemos que o textarea, para entradas de texto de mais de uma linha

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

_Fonte: AULA 27 ATIVIDADE_PROGRAMAÇÃO FRONT END I.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação Front-End

2ª SÉRIE

ATIVIDADE AULA 27

Questão 1

Qual atributo HTML é usado para especificar o tipo de entrada de um campo de formulário?

a) type

b) input

c) field

d) form

Resposta correta: a) type

Comentário: O atributo "type" é usado para especificar o tipo de entrada de um campo de formulário, como "text", "password", "email", "radio", "checkbox" etc.

Questão 2

Qual é o tipo de campo de entrada HTML usado para permitir que os usuários selecionem uma data?

a) time

b) date

c) calendar

d) datetime

Resposta correta: b) date

Comentário: O tipo de campo de entrada "date" é usado para permitir que os usuários selecionem uma data. Ele geralmente exibe um seletor de datas no navegador.

## Prática

_Fonte: AULA 27_PRÁTICA_PROGRAMAÇÃO FRONT END.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

PROGRAMAÇÃO FRONT END

2ª SÉRIE

ATIVIDADE PRÁTICA AULA 27

##### 1. Objetivo da Aula Prática

Ao final da aula prática, o estudante será capaz de:

- Compreender a importância dos diferentes tipos de campos em formulários HTML.
- Utilizar corretamente tipos como email, tel, date, password e textarea.
- Diferenciar quando usar cada tipo de campo.
- Aprimorar o formulário de contato criado anteriormente.
- Melhorar a experiência do usuário através da escolha adequada dos inputs.
Produto final esperado:

- Formulário de contato aprimorado com diferentes tipos de campos e melhor organização dos dados.

##### 2. Ferramentas Recomendadas

###### VS Code ou Editor HTML

- Para que serve: editar e aprimorar formulários.
- Por que é adequado: permite organização e expansão do projeto.
- Como facilita o aprendizado: facilita testes e ajustes contínuos.

###### Navegador Web

- Para que serve: testar comportamento dos campos.
- Por que é adequado: permite observar validações automáticas.
- Como facilita o aprendizado: mostra funcionamento real dos inputs.

###### Editor Online (HTML5 Editor)

- Link: https://html5-editor.net/
- Para que serve: testes rápidos.
- Como facilita o aprendizado: feedback imediato.

##### 3. Checklist Inicial

Antes de iniciar a prática, o estudante deve ter:

- Página contato.html com formulário básico
- Campos de nome, e-mail e telefone já criados
- CSS funcional
- Navegador atualizado
- Conexão com internet
Material de apoio indicado na aula: https://cursos.alura.com.br/course/html5-css3-formularios-tabelas

##### 4. Passo a Passo do Docente (Aula de até 50 minutos)

###### Preparações necessárias

- Garantir que todos tenham o formulário básico pronto.
- Revisar rapidamente:
- Tag <form>
- Tipos de input já utilizados

###### Condução da aula

###### Contextualização (5 minutos)

Apresentar o cenário:

- Formulário de inscrição em evento
- Coleta de diferentes tipos de dados
Perguntar:

- Todos os dados são iguais?
- Podemos usar apenas text para tudo?

###### Conceituando tipos de campos (10 minutos)

Explicar:

Cada tipo de campo atende um tipo de dado:

- text → texto simples
- email → valida e-mail
- tel → telefone
- password → oculta caracteres
- date → seleciona data
- textarea → texto longo
Destacar:

- Validação automática
- Experiência do usuário

###### Demonstração do professor (15 minutos)

Demonstrar:

- Adicionar novos campos ao formulário:
- Data de nascimento (date)
- Senha (password)
- Campo de mensagem (textarea)
- Ajustar tamanho do textarea
- Testar comportamento no navegador

###### Prática guiada (15 minutos)

Alunos devem:

- Inserir novos campos no formulário
- Ajustar tipos corretamente
- Testar validações
- Melhorar organização

###### Revisão e fechamento (5 minutos)

- Testar todos os campos
- Corrigir erros
- Reforçar boas práticas

###### Pontos de atenção

- Escolher tipo correto para cada dado.
- Evitar usar apenas text.
- Garantir legibilidade do formulário.

##### 5. Atividade Prática — Descrição Geral

O estudante deverá:

- Aprimorar o formulário de contato.
- Inserir novos campos com tipos diferentes.
- Ajustar layout básico do formulário.
- Testar comportamento dos campos.
Problema real simulado: Criar formulário completo de inscrição em evento.

Habilidade desenvolvida: Estruturação de formulários complexos e validação de dados.

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
- Localize o formulário existente.
- Adicione um campo de senha (input type="password").
- Adicione um campo de data (input type="date").
- Ajuste o campo de mensagem usando <textarea>.
- Configure tamanho do textarea.
- Verifique labels para todos os campos.
- Teste preenchimento no navegador.
- Observe validações automáticas.
- Ajuste organização visual.
- Salve o projeto.

##### 8. Exemplo ou Demonstração

Estrutura esperada:

Formulário:

- Nome → texto
- E-mail → validação automática
- Telefone → número
- Data → seletor
- Senha → oculto
- Mensagem → texto longo
Conceitos reforçados:

- Cada campo tem função específica
- Melhor escolha → melhor experiência
- Validação reduz erros

##### 9. Resultado Esperado

O estudante deverá apresentar:

- Formulário com múltiplos tipos de campos.
- Uso correto de:
- email
- password
- date
- textarea
- Organização clara dos campos.
- Código funcional e legível.
O professor verifica:

- Aplicação correta dos tipos.
- Funcionamento no navegador.
- Estrutura organizada.

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

- Por que não usar apenas text para tudo?
- Qual campo melhora mais a experiência do usuário?
- Como isso impacta sistemas reais?
