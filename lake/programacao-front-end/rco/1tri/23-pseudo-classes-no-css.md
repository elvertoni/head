---
titulo: "Pseudo-classes no CSS"
tipo: rco-seed
disciplina: programacao-front-end
sigla_rco: PFE
trimestre: 1
ordem_rco: 23
serie: 2
aula_rco: "Aula 23"
slides: 23
tem_atividade: true
tem_pratica: true
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/1TRI/23-pseudo-classes-no-css/23-pseudo-classes-no-css.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/1TRI/23-pseudo-classes-no-css/AULA 23 ATIVIDADE_PROGRAMAÇÃO FRONT END I.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/1TRI/23-pseudo-classes-no-css/AULA 23_PRÁTICA_PROGRAMAÇÃO FRONT END.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Pseudo-classes no CSS

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- Programação Front-End I
- 2ª Série
- Pseudo-classes no CSS
- Aula 23

_1 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- COMPETÊNCIA(S) A SER(EM) DESENVOLVIDA(S) NESTA AULA:
- De acordo com o Plano de Curso de Desenvolvimento de Sistemas:
- HABILIDADE(S) A SER(EM) DESENVOLVIDA(S) NESTA AULA:
- Codificar aplicações e rotinas utilizando linguagens de programação específicas.
- Prototipar as habilidades de design visual.

_1 imagem(ns) no slide._

### Slide 4

- Nesta aula vamos:
- Aprender sobre Pseudo-classe em HTML
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
- https://caelum-online-public.s3.amazonaws.com/1205-html5-css3-parte2/05/aula-5-completa.zip
- Complemento:
- https://cursos.alura.com.br/course/html5-css3-primeiros-passos/task/581966 Link da ferramenta: https://html5-editor.net/

_2 imagem(ns) no slide._

### Slide 6

- Aula anterior
- Aprendemos sobre bordas, onde bordas em HTML são elementos visuais que podem ser adicionados a diferentes tipos de elementos HTML, como tabelas, imagens, caixas de texto e divs.

_1 imagem(ns) no slide._

### Slide 7

- Para pensarmos juntos...
- A utilização de pseudo-classes CSS pode ser uma forma eficaz de tornar a experiência do usuário em uma página web mais agradável e interativa. As pseudo-classes permitem que os desenvolvedores criem estilos dinâmicos para elementos HTML com base em interações específicas, como clicar em um link ou passar o cursor do mouse sobre um botão.

_1 imagem(ns) no slide._

### Slide 8

- Para pensarmos juntos...
- Dessa forma, as pseudo-classes podem melhorar a usabilidade do site e aumentar a interação do usuário com o conteúdo. No entanto, é importante lembrar que a utilização excessiva de pseudo-classes pode tornar a página web pesada e lenta para carregar, especialmente em dispositivos móveis ou com conexões lentas.

_1 imagem(ns) no slide._

### Slide 9

- Para pensarmos juntos...
- Portanto, é importante encontrar um equilíbrio adequado na utilização de pseudo-classes, para que elas sejam úteis e não afetem negativamente o desempenho da página. Como a pseudo-classe: active pode ser usada para melhorar a usabilidade de um site?
- Conversem e apresentem suas visões

_2 imagem(ns) no slide._

### Slide 10

- Resposta
- A pseudo-classe: active pode ser usada para aplicar um estilo diferente a um elemento quando ele está sendo utilizado ativamente pelo usuário, como ao clicar em um link. Isso pode ajudar a tornar a experiência do usuário mais interativa e intuitiva.

_1 imagem(ns) no slide._

### Slide 11

- Conceituando
- As pseudo-classes em CSS são utilizadas para aplicar estilos a elementos HTML com base em estados específicos, tais como o estado de foco, o estado de hover, o estado de link visitado, entre outros. As pseudo-classes são precedidas pelo caractere ":" e são adicionadas ao seletor CSS para especificar o estado que deve ser estilizado.
- https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/CSS_basics/css-declaration-small.png

_1 imagem(ns) no slide._

### Slide 12

- Conceituando
- Por exemplo, a pseudo-classe: “:hover” é usada para definir o estilo de um elemento quando o cursor do mouse passa sobre ele. Algumas das pseudo-classes mais comuns em CSS incluem:

_1 imagem(ns) no slide._

### Slide 13

- Conceituando
- :hover - aplicado quando o cursor do mouse está sobre o elemento
- :active - aplicado quando o elemento está sendo ativamente utilizado, como clicado em um link
- :visited - aplicado a um link que já foi visitado
- https://www.galinhaprogramadora.com.br/wp-content/uploads/2019/07/css-as-authored.png

_1 imagem(ns) no slide._

### Slide 14

- Conceituando
- :focus - aplicado a um elemento quando ele está em foco, geralmente quando o usuário o seleciona com o teclado.
- :nth-child - aplicado a elementos específicos em uma lista, com base em sua posição.
- https://marquesfernandes.com/wp-content/uploads/2020/04/pankaj-patel-6JVlSdgMacE-unsplash.jpg

_1 imagem(ns) no slide._

### Slide 15

- Link para o curso: https://cursos.alura.com.br/course/html5-css3-posicionamento-listas-navegacao
- A recomendação é que você continue esse curso extraclasse, pois ele traz um conteúdo essencial para compreender sobre o referido tema.
- Atividade Prática na Plataforma Alura
- Na plataforma Alura vamos acessar o seguinte curso:

_3 imagem(ns) no slide._

### Slide 16

- Pseudo-classes de estado
- 7 minutos
- Na aula passada, a gente finalizou a nossa lista de itens do produto, ou seja, o que a nossa barbearia oferece para os clientes.
- Link para tarefa: https://cursos.alura.com.br/course/html5-css3-posicionamento-listas-navegacao/task/59068
- Corte de cabelo, corte de barba e o corte completo de cabelo mais barba. Para completar o conteúdo dessa página, ainda está faltando adicionarmos o rodapé, mas isso a gente vai ver lá frente.
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 17

- Aplicando hover e active
- 6 minutos
- Agora que começamos a entender como funcionam os comportamentos do CSS, queremos fazer a mesma coisa, mas nos nossos itens dos produtos, do que oferecemos aos nossos clientes.
- Link para tarefa: https://cursos.alura.com.br/course/html5-css3-posicionamento-listas-navegacao/task/59069
- Já temos o nosso comportamento de hover funcionando no cabeçalho e queremos fazer isso nos produtos.
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 18

- Fixando conteúdo
- As pseudo-classes são uma poderosa ferramenta para estilizar elementos HTML com base em estados específicos e podem ser combinadas com outras propriedades CSS, como cor, tamanho, fonte e posicionamento para criar estilos avançados e personalizados.
- https://marquesfernandes.com/wp-content/uploads/2020/04/pankaj-patel-6JVlSdgMacE-unsplash.jpg

_1 imagem(ns) no slide._

### Slide 19

- Vamos praticar?
- Prepare-se, porque agora você vai sair do modo aprender e entrar no modo colocar a mão no código.
- Nesta atividade, você irá aplicar as pseudo-classes do CSS para tornar sua página mais interativa, criando efeitos visuais que respondem às ações do usuário.
- É o momento de transformar o que você aprendeu em experiência prática real.

_1 imagem(ns) no slide._

### Slide 20

- O que vimos na aula de hoje:
- Conhecemos algumas pseudo-classes CSS
- Aprendemos como mudar a cor do texto e/ou da borda de um elemento, quando o usuário passar o cursor sobre o mesmo

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

## Atividade

_Fonte: AULA 23 ATIVIDADE_PROGRAMAÇÃO FRONT END I.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação Front-End

2ª SÉRIE

ATIVIDADE AULA 23

Questão 1

Qual das seguintes pseudo-classes CSS é usada para aplicar um estilo a um elemento quando ele está sendo clicado?

a) :hover

b) :active

c) :visited

d) :focus

Resposta correta: b) :active. A pseudo-classe :active é usada para aplicar um estilo a um elemento quando ele está sendo clicado ou interagido pelo usuário. É comum usar essa pseudo-classe em links, para que o usuário possa ver visualmente quando está clicando no link.

Questão 2

Qual das seguintes pseudo-classes CSS é usada para aplicar um estilo a um elemento quando ele está sendo selecionado pelo usuário, por exemplo, por meio do uso do teclado?

a) :hover

b) :active

c) :visited

d) :focus

Resposta correta: d) :focus. A pseudo-classe :focus é usada para aplicar um estilo a um elemento quando ele está em foco, geralmente quando o usuário o seleciona com o teclado. É comum usar essa pseudo-classe em formulários, para que o usuário possa ver visualmente qual campo está sendo preenchido.

## Prática

_Fonte: AULA 23_PRÁTICA_PROGRAMAÇÃO FRONT END.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

PROGRAMAÇÃO FRONT END

2ª SÉRIE

ATIVIDADE PRÁTICA AULA 23

##### 1. Objetivo da Aula Prática

Ao final da aula prática, o estudante será capaz de:

- Compreender o conceito de pseudo-classes no CSS.
- Aplicar estilos dinâmicos baseados em interação do usuário.
- Utilizar pseudo-classes como :hover, :active, :visited e :focus.
- Melhorar a interatividade e usabilidade da página web.
- Aplicar efeitos visuais em elementos como links e produtos.
Produto final esperado:

- Página web com elementos interativos utilizando pseudo-classes, respondendo às ações do usuário.

##### 2. Ferramentas Recomendadas

###### VS Code ou Editor HTML

- Para que serve: editar HTML e CSS.
- Por que é adequado: permite aplicar pseudo-classes com organização.
- Como facilita o aprendizado: visualização prática dos efeitos.

###### Navegador Web

- Para que serve: testar interações (hover, clique, foco).
- Por que é adequado: simula experiência real do usuário.
- Como facilita o aprendizado: permite observar comportamento dinâmico.

###### Editor Online (HTML5 Editor)

- Para que serve: testar rapidamente mudanças.
- Link: https://html5-editor.net/
- Como facilita o aprendizado: feedback imediato.

##### 3. Checklist Inicial

Antes de iniciar a prática, o estudante deve ter:

- Projeto com página de produtos criada
- CSS funcionando corretamente
- Lista de produtos estruturada
- Navegador atualizado
- Conexão com internet
Material de apoio indicado na aula: https://cursos.alura.com.br/course/html5-css3-posicionamento-listas-navegacao

##### 4. Passo a Passo do Docente (Aula de até 50 minutos)

###### Preparações necessárias

- Garantir que todos tenham a página de produtos pronta.
- Revisar rapidamente:
- Seletores CSS
- Estilização básica

###### Condução da aula

###### Contextualização (5 minutos)

Perguntar:

- Como podemos tornar um site mais interativo?
- O que acontece quando passamos o mouse sobre um botão?
Introduzir conceito de interação do usuário.

###### Conceituando pseudo-classes (10 minutos)

Explicar:

- Pseudo-classes representam estados de um elemento.
- São utilizadas com : no CSS.
Apresentar exemplos:

- :hover → quando o mouse passa
- :active → quando o elemento é clicado
- :visited → link visitado
- :focus → elemento selecionado

###### Demonstração do professor (10 minutos)

Aplicar:

- Alteração de cor ao passar o mouse.
- Alteração de borda ao clicar.
- Mudança de estilo em links visitados.
Mostrar resultado em tempo real.

###### Prática guiada (20 minutos)

Alunos devem:

- Aplicar :hover nos produtos.
- Aplicar :active nos itens clicáveis.
- Ajustar cores e bordas.
- Melhorar visual da interação.

###### Revisão e fechamento (5 minutos)

- Testar interações.
- Ajustar exageros visuais.
- Reforçar equilíbrio no uso.

###### Pontos de atenção

- Evitar excesso de efeitos.
- Garantir legibilidade.
- Testar em diferentes elementos.

##### 5. Atividade Prática — Descrição Geral

O estudante deverá:

- Aplicar pseudo-classes na página de produtos.
- Criar efeitos visuais ao passar o mouse e clicar.
- Melhorar a interação do usuário com a página.
Problema real simulado: Melhorar a experiência do usuário em um site institucional.

Habilidade desenvolvida: Criação de interfaces interativas com CSS.

##### 6. Metodologia Ativa Utilizada

- Aprendizagem baseada em projeto
- Experimentação prática
- Ensino por descoberta
- Elementos de Lemov:
- Modelagem
- Prática guiada
- Checagem de entendimento
- Feedback imediato

##### 7. Passo a Passo da Atividade Prática (para os alunos)

- Abra seu projeto.
- Localize a lista de produtos.
- No CSS, selecione os itens da lista.
- Crie um estilo com :hover:
- Alterar cor de fundo ou texto.
- Crie um estilo com :active:
- Alterar borda ou cor ao clicar.
- Aplique :visited nos links.
- Teste cada interação no navegador.
- Ajuste cores e efeitos.
- Garanta que a página continua legível.
- Salve o projeto.

##### 8. Exemplo ou Demonstração

Conceitos aplicados:

- Elemento padrão → estilo normal
- Elemento com :hover → muda ao passar o mouse
- Elemento com :active → muda ao clicar
Exemplo conceitual:

Produto:

- Normal → fundo branco
- Hover → fundo destacado
- Active → borda diferente

##### 9. Resultado Esperado

O estudante deverá apresentar:

- Uso correto de pseudo-classes:
- :hover
- :active
- (opcional) :visited ou :focus
- Interação visual funcionando.
- Código organizado.
- Página funcional e legível.
O professor verifica:

- Funcionamento dos efeitos.
- Aplicação correta das pseudo-classes.
- Equilíbrio visual.

##### 10. Formato de Entrega da Atividade

- Formato: Pasta do projeto contendo:
- index.html
- produtos.html
- style.css
- Entrega: ao final da aula.
- Prazo sugerido: imediato.

##### 11. Encerramento e Reflexão

Perguntas orientadoras:

- Como pseudo-classes melhoram a experiência do usuário?
- O que acontece se exagerarmos nos efeitos?
- Qual a importância da interação visual?
