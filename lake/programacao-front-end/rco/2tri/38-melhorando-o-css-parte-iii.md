---
titulo: "Melhorando o CSS Parte III"
tipo: rco-seed
disciplina: programacao-front-end
sigla_rco: PFE
trimestre: 2
ordem_rco: 38
serie: 2
aula_rco: "Aula 38"
slides: 21
tem_atividade: true
tem_pratica: true
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/2TRI/38-melhorando-o-css-parte-iii/38-melhorando-o-css-parte-iii.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/2TRI/38-melhorando-o-css-parte-iii/AULA 38_ATIVIDADE_PROGRAMAÇÃO FRONT END.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/2TRI/38-melhorando-o-css-parte-iii/AULA 38_PRÁTICA_PROGRAMAÇÃO FRONT END.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Melhorando o CSS Parte III

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- Programação Front-End
- 2ª Série
- Melhorando o CSS Parte III
- Aula 38

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
- Aprender a melhorar a utilização do CSS em páginas HTML Parte III.
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
- https://caelum-online-public.s3.amazonaws.com/1310-html5-css3-parte4/02/html-parte-4-aula-2-completa.zip
- Complemento:
- https://cursos.alura.com.br/course/html5-css3-primeiros-passos/task/581966

_2 imagem(ns) no slide._

### Slide 6

- Aula anterior
- Iniciamos os estudos sobre a melhoria do CSS fazendo uso de pseudo-classes, utilizados para aplicar estilos, além de utilizar a aplicação de gradientes em páginas HTML.

_1 imagem(ns) no slide._

### Slide 7

- Para pensarmos juntos...
- Fernanda é uma desenvolvedora web que está trabalhando em um projeto de blog para um cliente. O cliente deseja que o design dos artigos do blog seja único e atraente. Fernanda quer estilizar a primeira letra de cada artigo com uma fonte maior e diferente para dar um toque especial ao design e torná-lo mais interessante aos olhos dos leitores.

_1 imagem(ns) no slide._

### Slide 8

- Para pensarmos juntos...
- Como Fernanda pode utilizar pseudo-elementos em CSS para estilizar a primeira letra dos artigos do blog?
- Conversem e apresentem suas visões

_2 imagem(ns) no slide._

### Slide 9

- Resposta
- Fernanda pode utilizar o pseudo-elemento ::first-letter em CSS para selecionar e estilizar a primeira letra de cada artigo do blog. Ao aplicar estilos específicos a esse pseudo-elemento, ela pode dar um toque único ao design dos artigos, tornando-os mais atraentes e interessantes para os leitores.

_1 imagem(ns) no slide._

### Slide 10

- Conceituando
- Pseudo-elementos em páginas HTML são uma funcionalidade do CSS que permite selecionar e estilizar partes específicas de um elemento, sem a necessidade de adicionar elementos HTML adicionais ou alterar a estrutura do documento. Eles são usados para criar efeitos visuais, como estilizar a primeira letra ou a primeira linha de um parágrafo, ou inserir conteúdo antes ou depois de um elemento.

_1 imagem(ns) no slide._

### Slide 11

- Conceituando
- Os pseudo-elementos são adicionados às regras CSS como prefixos aos seletores de elementos, utilizando uma sintaxe de dois-pontos (::) antes do nome. Alguns exemplos comuns de pseudo-elementos incluem:

_1 imagem(ns) no slide._

### Slide 12

- Conceituando
- ::before: Insere conteúdo antes do elemento selecionado. Normalmente, é usado em combinação com a propriedade content para especificar o conteúdo a ser inserido.
- ::after: Insere conteúdo após o elemento selecionado. Assim como o ::before, é usado com a propriedade content para especificar o conteúdo a ser inserido.
- https://slideplayer.com.br/slide/3284708/11/images/5/Exemplo+Form+GET+%3Chtml%3E.jpg

_1 imagem(ns) no slide._

### Slide 13

- Conceituando
- ::first-letter: Seleciona e aplica estilos à primeira letra de um elemento. É útil para criar efeitos tipográficos, como letras capitulares em um parágrafo.
- ::first-line: Seleciona e aplica estilos à primeira linha de um elemento. Pode ser usado para criar efeitos visuais, como alterar a fonte ou a cor da primeira linha de um texto.

_1 imagem(ns) no slide._

### Slide 14

- Conceituando
- Os pseudo-elementos oferecem uma maneira eficiente e flexível de estilizar partes específicas de elementos HTML, permitindo que os desenvolvedores criem designs mais avançados e interessantes sem a necessidade de adicionar marcação adicional ao documento. Eles facilitam a manutenção do código e melhoram a performance do site, já que menos elementos HTML precisam ser renderizados pelo navegador.

_1 imagem(ns) no slide._

### Slide 15

- Link para o curso: https://cursos.alura.com.br/course/html5-css3-avancando-css
- A recomendação é que você continue esse curso extraclasse, pois ele traz um conteúdo essencial para compreender sobre o referido tema.
- Atividade Prática na Plataforma Alura
- Na plataforma Alura vamos acessar o seguinte curso:

_3 imagem(ns) no slide._

### Slide 16

- Pseudo-elementos
- 7 minutos
- Evoluiremos ainda mais em nosso entendimento do CSS, e um dos tópicos do nosso estudo serão os já referidos pseudo-elementos, que não existem no código HTML e são criados via CSS.
- Link para tarefa: https://cursos.alura.com.br/course/html5-css3-avancando-css/task/63325
- Pseudo-elementos são funcionalidades do CSS que permitem estilizar partes específicas de um elemento HTML, como a primeira letra ou a primeira linha, sem adicionar marcação adicional. Eles facilitam a criação de efeitos visuais e a manutenção do código.
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 17

- Vamos praticar?
- Prepare-se, porque nessa atividade, você vai sair do modo aprender e entrar direto no modo praticar.
- A atividade prática vai colocar você diante de um desafio real, que faz relação com o conteúdo aprendido até aqui.

_1 imagem(ns) no slide._

### Slide 18

- O que vimos na aula de hoje:
- Aprendemos pseudo-elementos em páginas HTML.

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

_Fonte: AULA 38_ATIVIDADE_PROGRAMAÇÃO FRONT END.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação Front-End

2ª SÉRIE

ATIVIDADE AULA 38

Questão 1

Qual pseudoelemento CSS é usado para aplicar estilos à primeira letra de um elemento?

a) ::before

b) ::after

c) ::first-letter

d) ::first-line

Comentário: A resposta correta é a alternativa "c". O pseudoelemento ::first-letter é usado para aplicar estilos à primeira letra de um elemento.

Questão 2

Qual pseudoclasse CSS é usada para aplicar estilos ao primeiro elemento filho de um elemento?

a) :first-child

b) :last-child

c) :nth-child

d) :only-child

Comentário: A resposta correta é a alternativa "a". A pseudoclasse :first-child é usada para aplicar estilos ao primeiro elemento filho de um elemento.

## Prática

_Fonte: AULA 38_PRÁTICA_PROGRAMAÇÃO FRONT END.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

PROGRAMAÇÃO FRONT END

2ª SÉRIE

ATIVIDADE PRÁTICA AULA 38

##### 1. Objetivo da Aula Prática

Ao final da aula prática, o estudante será capaz de:

- Compreender o conceito de pseudo-elementos no CSS.
- Utilizar pseudo-elementos como:
- ::before
- ::after
- ::first-letter
- ::first-line
- Aplicar efeitos visuais sem modificar a estrutura HTML.
- Melhorar a aparência tipográfica e visual de textos e elementos da página.
- Criar estilos mais modernos e organizados utilizando CSS avançado.
Produto final esperado:

- Página HTML estilizada com pseudo-elementos aplicados em títulos, parágrafos e outros elementos visuais.

##### 2. Ferramentas Recomendadas

###### VS Code ou Editor HTML

- Para que serve: editar HTML e CSS do projeto.
- Por que é adequado: permite organizar estilos avançados de forma profissional.
- Como facilita o aprendizado: possibilita visualizar imediatamente os efeitos aplicados.

###### Navegador Web

- Para que serve: testar pseudo-elementos e estilos visuais.
- Por que é adequado: mostra o comportamento real da página.
- Como facilita o aprendizado: permite validar efeitos aplicados sem alterar o HTML.

###### Editor Online HTML5

- Link: https://html5-editor.net/
- Para que serve: realizar testes rápidos de CSS.
- Como facilita o aprendizado: feedback instantâneo das alterações.

##### 3. Checklist Inicial

Antes de iniciar a prática, o estudante deve ter:

- Projeto HTML funcionando
- Arquivo CSS externo configurado
- Página com textos, títulos e parágrafos
- Navegador atualizado
- Conexão com internet
Material de apoio indicado na aula: https://cursos.alura.com.br/course/html5-css3-avancando-css

##### 4. Passo a Passo do Docente (Aula de até 50 minutos)

###### Preparações necessárias

- Garantir que todos tenham o projeto aberto.
- Revisar rapidamente:
- Seletores CSS
- Pseudo-classes
- Estrutura HTML

###### Condução da aula

###### Contextualização (5 minutos)

Apresentar cenário:

- Sites modernos utilizam detalhes visuais para melhorar leitura e design.
Perguntar:

- Como destacar a primeira letra de um texto sem alterar o HTML?
- Como inserir símbolos decorativos usando apenas CSS?

###### Conceituando pseudo-elementos (10 minutos)

Explicar:

Pseudo-elementos permitem estilizar partes específicas de um elemento.

Apresentar:

- ::before
- ::after
- ::first-letter
- ::first-line
Destacar:

- Não é necessário alterar a estrutura HTML.
- O CSS cria o efeito visual.

###### Demonstração do professor (15 minutos)

Demonstrar:

###### ::first-letter

- Aumentar tamanho da primeira letra.
- Alterar cor e fonte.

###### ::first-line

- Alterar estilo da primeira linha.

###### ::before

- Inserir símbolo antes de títulos.

###### ::after

- Inserir conteúdo decorativo após elementos.
Explicar uso da propriedade content.

###### Prática guiada (15 minutos)

Alunos devem:

- Aplicar ::first-letter em parágrafos.
- Inserir ícones ou símbolos usando ::before.
- Utilizar ::after para complementar títulos.
- Ajustar visual dos efeitos.

###### Revisão e fechamento (5 minutos)

- Testar visual.
- Ajustar exageros visuais.
- Reforçar organização do CSS.

###### Pontos de atenção

- Pseudo-elementos usam ::.
- ::before e ::after precisam da propriedade content.
- Evitar excesso de efeitos decorativos.

##### 5. Atividade Prática — Descrição Geral

O estudante deverá:

- Aplicar pseudo-elementos em textos e títulos.
- Criar efeitos tipográficos.
- Inserir elementos decorativos utilizando CSS.
- Melhorar visualmente a página sem alterar o HTML.
Problema real simulado: Melhorar a identidade visual de artigos de um blog.

Habilidade desenvolvida: Criação de efeitos visuais avançados utilizando CSS.

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
- Escolha um parágrafo da página.
- No CSS, aplique:
- ::first-letter
- Ajuste:
- tamanho
- cor
- espaçamento
- Escolha um título.
- Utilize:
- ::before
- Adicione conteúdo decorativo usando:
- content
- Aplique:
- ::after
- Teste no navegador.
- Ajuste alinhamentos e estilos.
- Salve o projeto.

##### 8. Exemplo ou Demonstração

###### Exemplo conceitual — Primeira letra

- p::first-letter {
- font-size: 32px;
- color: blue;
- }


###### Exemplo conceitual — Before

- h2::before {
- content: "★ ";
- }


###### Exemplo conceitual — After

- h2::after {
- content: " ✔";
- }


###### Conceitos reforçados

- Pseudo-elementos criam efeitos visuais sem alterar HTML.
- content é obrigatório em before e after.
- CSS pode adicionar detalhes visuais avançados.

##### 9. Resultado Esperado

O estudante deverá apresentar:

- Uso correto de:
- ::before
- ::after
- ::first-letter
- ::first-line
- Página visualmente aprimorada.
- Código CSS organizado.
- Efeitos aplicados corretamente.
O professor verifica:

- Funcionamento dos pseudo-elementos.
- Organização do CSS.
- Qualidade visual dos efeitos.

##### 10. Formato de Entrega da Atividade

- Formato: Pasta do projeto contendo:
- index.html
- style.css
- imagens utilizadas (se houver)
- Entrega: ao final da aula.
- Prazo sugerido: imediato.

##### 11. Encerramento e Reflexão

Perguntas orientadoras:

- Qual a vantagem dos pseudo-elementos?
- Quando usar ::before e ::after?
- Como pequenos detalhes melhoram a experiência visual?
