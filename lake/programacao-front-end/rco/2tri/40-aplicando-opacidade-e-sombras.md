---
titulo: "Opacidade e sombra"
tipo: rco-seed
disciplina: programacao-front-end
sigla_rco: PFE
trimestre: 2
ordem_rco: 40
serie: 2
aula_rco: "Aula 40"
slides: 25
tem_atividade: true
tem_pratica: true
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PFE/2TRI/40-aplicando-opacidade-e-sombras/40-aplicando-opacidade-e-sombras.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/2TRI/40-aplicando-opacidade-e-sombras/AULA 40_ATIVIDADE_PROGRAMAÇÃO FRONT END.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/2TRI/40-aplicando-opacidade-e-sombras/AULA 40_PRÁTICA_PROGRAMAÇÃO FRONT END.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Opacidade e sombra

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- Programação Front-End
- 2ª Série
- Opacidade e sombra
- Aula 40

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
- Aprender sobre opacidade e sombra em páginas HTML Parte I.
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
- https://caelum-online-public.s3.amazonaws.com/1310-html5-css3-parte4/04/html-parte-4-aula-4-completa.zip
- Complemento:
- https://cursos.alura.com.br/course/html5-css3-primeiros-passos/task/581966

_2 imagem(ns) no slide._

### Slide 6

- Aula anterior
- Finalizamos os estudos sobre as opções de seleção de itens em páginas HTML.

_1 imagem(ns) no slide._

### Slide 7

- Para pensarmos juntos...
- Roberto é um desenvolvedor web que está trabalhando em um projeto de site para uma empresa. O cliente deseja que os botões do site tenham um efeito de sombra e que a opacidade desses botões seja reduzida ao passar o mouse sobre eles, para dar uma sensação de interatividade e melhorar a experiência do usuário.

_2 imagem(ns) no slide._

### Slide 8

- Para pensarmos juntos...
- Como Roberto pode utilizar CSS para aplicar sombra e alterar a opacidade dos botões ao passar o mouse sobre eles?
- Conversem e apresentem suas visões

_2 imagem(ns) no slide._

### Slide 9

- Resposta
- Roberto pode utilizar as propriedades CSS box-shadow e opacity, juntamente com o seletor de pseudo-classe :hover, para criar os efeitos desejados nos botões. A propriedade box-shadow permite adicionar uma sombra ao redor do elemento, enquanto a propriedade opacity controla a transparência do elemento.

_1 imagem(ns) no slide._

### Slide 10

- Conceituando
- Sombra e opacidade são propriedades CSS usadas para melhorar a estética e a experiência do usuário em páginas HTML, adicionando efeitos visuais aos elementos da página.
- Sombra: A propriedade box-shadow permite adicionar uma sombra ao redor de um elemento, criando a ilusão de profundidade e destacando o elemento no layout. A sombra pode ser ajustada em termos de cor, deslocamento horizontal e vertical, desfoque e propagação. Geralmente, sombras são usadas em botões, caixas de texto, cartões e outros elementos que precisam se destacar ou parecer interativos.

_1 imagem(ns) no slide._

### Slide 11

- Conceituando
- Exemplo de uso da propriedade box-shadow:
- .element {
- box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
- }

_1 imagem(ns) no slide._

### Slide 12

- Conceituando
- Opacidade: A propriedade opacity controla a transparência de um elemento, com valores que variam de 0 (totalmente transparente) a 1 (totalmente opaco). A opacidade é frequentemente usada em combinação com pseudo-classes, como :hover, para criar efeitos interativos que respondem às ações do usuário, como destacar um botão ou mostrar conteúdo adicional.

_1 imagem(ns) no slide._

### Slide 13

- Conceituando
- Exemplo de uso da propriedade opacity:
- .element:hover { opacity: 0.8;}

_1 imagem(ns) no slide._

### Slide 14

- Conceituando
- Ambas as propriedades, sombra e opacidade, podem ser aplicadas a diversos elementos HTML para melhorar a aparência geral das páginas e proporcionar uma experiência mais envolvente e dinâmica aos usuários. Essas propriedades são especialmente úteis para destacar áreas importantes, melhorar a legibilidade, fornecer feedback visual e criar um design mais atraente e moderno.

_1 imagem(ns) no slide._

### Slide 15

- Conceituando
- Suponhamos que você queira aplicar uma sombra em um botão na sua página HTML. Primeiro, defina o HTML do botão:
- <button class="my-button">Clique aqui</button>
- Em seguida, use CSS para aplicar a sombra ao botão:
- .my-button {
- background-color: #007BFF;
- color: white;
- padding: 10px 20px;
- border: none;
- cursor: pointer;
- box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
- }

_1 imagem(ns) no slide._

### Slide 16

- Conceituando
- Neste exemplo, a propriedade box-shadow é usada para adicionar uma sombra ao botão com a classe .my-button.
- Exemplo de utilização de opacidade:
- Suponhamos que você queira alterar a opacidade de uma imagem ao passar o mouse sobre ela. Primeiro, defina o HTML da imagem:
- <img class="my-image" src="image.jpg" alt="Exemplo de imagem">

_1 imagem(ns) no slide._

### Slide 17

- Conceituando
- Em seguida, use CSS para aplicar a opacidade e criar um efeito de transição suave:
- .my-image {
- opacity: 1;
- transition: opacity 0.3s ease;
- }
- .my-image:hover {
- opacity: 0.6;
- }

_1 imagem(ns) no slide._

### Slide 18

- Conceituando
- Neste exemplo, a propriedade opacity é usada para alterar a opacidade da imagem com a classe .my-image quando o usuário passa o mouse sobre ela. A propriedade transition garante uma transição suave entre os estados de opacidade.

_1 imagem(ns) no slide._

### Slide 19

- Link para o curso: https://cursos.alura.com.br/course/html5-css3-avancando-css
- A recomendação é que você continue esse curso extraclasse, pois ele traz um conteúdo essencial para compreender sobre o referido tema.
- Atividade Prática na Plataforma Alura
- Na plataforma Alura vamos acessar o seguinte curso:

_3 imagem(ns) no slide._

### Slide 20

- Opacidade nos elementos
- 6 minutos
- Nesta aula, aprenderemos a gerar opacidade em nossos elementos.
- Link para tarefa: https://cursos.alura.com.br/course/html5-css3-avancando-css/task/63328
- A opacidade é uma camada a mais posta sobre a imagem, como um insulfilme para a janela de carro, que oferece níveis diferentes de proteção contra o Sol.
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 21

- O que vimos na aula de hoje:
- Aprendemos sobre opacidade para páginas HTML.

_1 imagem(ns) no slide._

### Slide 22

- Vamos praticar?
- Prepare-se, porque nessa atividade, você vai sair do modo aprender e entrar direto no modo praticar.
- A atividade prática vai colocar você diante de um desafio real, que faz relação com o conteúdo aprendido até aqui.

_1 imagem(ns) no slide._

### Slide 23

- Pronto para desbloquear sua carreira de TI?
- Está perdido estudando mas não sabe por onde começar? Se a resposta é sim, você está no lugar certo! Descubra as estratégias e ferramentas essenciais para te ajudar a desbloquear seu potencial em TI e buscar sua primeira vaga de emprego no setor!
- Este e-book é um guia completo para quem busca começar pelos melhores caminhos para se tornar um excelente profissional de TI, ensinando a identificar perfis profissionais, aplicar técnicas de estudo eficazes, transformar teoria em prática, e aumentar a visibilidade de seu trabalho no mercado de trabalho. Ideal para novatos e profissionais em transição.
- E o melhor, ele pode ser seu, inteiramente grátis!
- Basta clicar AQUI e realizar o seu cadastro com o seu @escola!

_3 imagem(ns) no slide._

### Slide 24

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

### Slide 25

_(sem texto)_

## Atividade

_Fonte: AULA 40_ATIVIDADE_PROGRAMAÇÃO FRONT END.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação Front-End

2ª SÉRIE

ATIVIDADE AULA 40

Questão 1

Qual propriedade CSS é usada para controlar a transparência de um elemento HTML?

a) transparency

b) alpha

c) opacity

d) clear

Comentário: A resposta correta é a alternativa "c". A propriedade opacity é usada para controlar a transparência de um elemento HTML, com valores que variam de 0 (totalmente transparente) a 1 (totalmente opaco). As outras alternativas não são propriedades CSS válidas para controlar a transparência.

Questão 2

Qual o valor da propriedade opacity que torna um elemento HTML completamente opaco?

a) 0

b) 0.5

c) 1

d) 100

Comentário: A resposta correta é a alternativa "c". O valor 1 para a propriedade opacity torna um elemento HTML completamente opaco. Valores menores que 1 tornam o elemento progressivamente mais transparente, com 0 representando total transparência. As outras alternativas não representam a opacidade completa de um elemento.

## Prática

_Fonte: AULA 40_PRÁTICA_PROGRAMAÇÃO FRONT END.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

PROGRAMAÇÃO FRONT END

2ª SÉRIE

ATIVIDADE PRÁTICA AULA 40

##### 1. Objetivo da Aula Prática

Ao final da aula prática, o estudante será capaz de:

- Aplicar efeitos visuais utilizando as propriedades CSS box-shadow e opacity.
- Utilizar pseudo-classes como :hover para criar interatividade.
- Criar botões e imagens com aparência mais moderna e dinâmica.
- Compreender como sombras e transparência melhoram a experiência visual do usuário.
- Aplicar transições suaves utilizando transition.
Produto final esperado:

- Página HTML contendo botões e imagens com efeitos de sombra, opacidade e interação ao passar o mouse.

##### 2. Ferramentas Recomendadas

###### VS Code ou Editor HTML

- Para que serve: editar HTML e CSS do projeto.
- Por que é adequado: facilita organização e testes visuais.
- Como facilita o aprendizado: permite visualizar mudanças em tempo real.

###### Navegador Web

- Para que serve: testar interatividade e efeitos visuais.
- Por que é adequado: simula experiência real do usuário.
- Como facilita o aprendizado: permite validar animações e transições.

###### Editor Online (HTML5 Editor)

- Link: https://html5-editor.net/
- Para que serve: testes rápidos de CSS.
- Como facilita o aprendizado: feedback imediato das alterações.

##### 3. Checklist Inicial

Antes de iniciar a prática, o estudante deve ter:

- Projeto HTML funcionando
- CSS externo configurado
- Botões e imagens já inseridos na página
- Navegador atualizado
- Conexão com internet
Material de apoio indicado na aula: https://cursos.alura.com.br/course/html5-css3-avancando-css

##### 4. Passo a Passo do Docente (Aula de até 50 minutos)

###### Preparações necessárias

- Garantir que todos tenham o projeto aberto.
- Revisar rapidamente:
- Pseudo-classes (:hover)
- CSS básico
- Seletores

###### Condução da aula

###### Contextualização (5 minutos)

Apresentar cenário:

- Sites modernos usam efeitos visuais para destacar elementos.
Perguntar:

- O que torna um botão mais interativo?
- Como destacar elementos importantes?

###### Conceituando sombra e opacidade (10 minutos)

Explicar:

###### box-shadow

- Adiciona profundidade visual.
- Destaca elementos.

###### opacity

- Controla transparência.
- Valores:
- 0 → transparente
- 1 → totalmente visível
Mostrar exemplos simples.

###### Demonstração do professor (15 minutos)

Demonstrar:

###### Aplicando sombra:

- Botão com box-shadow

###### Aplicando opacidade:

- Imagem alterando transparência no :hover

###### Aplicando transição:

- transition: opacity 0.3s ease
Explicar efeito visual suave.

###### Prática guiada (15 minutos)

Alunos devem:

- Aplicar sombra em botões.
- Aplicar opacidade em imagens.
- Criar efeito hover.
- Ajustar intensidade dos efeitos.

###### Revisão e fechamento (5 minutos)

- Testar interações.
- Ajustar exageros.
- Reforçar equilíbrio visual.

###### Pontos de atenção

- Não exagerar na sombra.
- Garantir legibilidade dos elementos.
- Utilizar transições suaves.

##### 5. Atividade Prática — Descrição Geral

O estudante deverá:

- Aplicar sombra em botões ou caixas.
- Criar efeito de opacidade em imagens.
- Utilizar pseudo-classe :hover.
- Aplicar transição suave.
Problema real simulado: Melhorar a aparência visual e a interatividade de um site institucional.

Habilidade desenvolvida: Criação de interfaces modernas utilizando CSS avançado.

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
- Localize um botão existente.
- No CSS, aplique:
- box-shadow
- Ajuste:
- deslocamento
- desfoque
- intensidade da sombra
- Escolha uma imagem da página.
- Defina:
- opacity: 1
- Crie efeito :hover:
- opacity: 0.6
- Adicione:
- transition
- Teste no navegador.
- Ajuste os efeitos para equilíbrio visual.
- Salve o projeto.

##### 8. Exemplo ou Demonstração

###### Exemplo conceitual — Sombra

Botão:

- Sem sombra → aparência simples
- Com sombra → aparência destacada

###### Exemplo conceitual — Opacidade

Imagem:

- Normal → totalmente visível
- Hover → parcialmente transparente

###### Conceitos reforçados

- box-shadow cria profundidade
- opacity cria transparência
- transition suaviza mudanças

##### 9. Resultado Esperado

O estudante deverá apresentar:

- Botão com sombra aplicada.
- Imagem com efeito de opacidade.
- Uso correto de:
- box-shadow
- opacity
- transition
- :hover
- Página visualmente mais moderna.
O professor verifica:

- Funcionamento dos efeitos.
- Aplicação correta do CSS.
- Qualidade visual e organização.

##### 10. Formato de Entrega da Atividade

- Formato: Pasta do projeto contendo:
- index.html
- style.css
- imagens utilizadas
- Entrega: ao final da aula.
- Prazo sugerido: imediato.

##### 11. Encerramento e Reflexão

Perguntas orientadoras:

- Como sombras ajudam no design?
- Quando usar opacidade?
- O que acontece se exagerarmos nos efeitos?
