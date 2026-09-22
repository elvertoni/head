---
titulo: "Iniciando o Projeto em HTML – Parte II"
tipo: rco-seed
disciplina: programacao-front-end
sigla_rco: PFE
trimestre: 2
ordem_rco: 43
serie: 2
aula_rco: "Aula 43"
slides: 24
tem_atividade: true
tem_pratica: true
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/2TRI/43-iniciando-o-projeto-em-html-parte-ii/43-iniciando-o-projeto-em-html-parte-ii.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/2TRI/43-iniciando-o-projeto-em-html-parte-ii/AULA 43_ATIVIDADE_PROGRAMAÇÃO FRONT END.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/2TRI/43-iniciando-o-projeto-em-html-parte-ii/AULA 43_PRÁTICA_PROGRAMAÇÃO FRONT END.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Iniciando o Projeto em HTML – Parte II

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- Programação Front-End
- 2ª Série
- Iniciando o Projeto em HTML – Parte II
- Aula 43

_1 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- COMPETÊNCIA(S) A SER(EM) DESENVOLVIDA(S) NESTA AULA:
- De acordo com o Plano de Curso de Desenvolvimento de Sistemas:
- HABILIDADE(S) A SER(EM) DESENVOLVIDA(S) NESTA AULA:
- Codificar aplicações e rotinas utilizando linguagens de programação específicas.
- Criar páginas estruturadas utilizando HTML.

_1 imagem(ns) no slide._

### Slide 4

- Nesta aula vamos:
- Aprofundar a criação de páginas web utilizando HTML e CSS, explorando a organização visual e estrutural de um projeto real.
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
- Ferramenta Figma:
- https://www.figma.com/
- Imagens do projeto:
- https://github.com/alura-cursos/aluraplus/tree/aula04/img
- VS Code:
- https://code.visualstudio.com/

_2 imagem(ns) no slide._

### Slide 6

- Aula anterior
- Iniciamos a criação de um projeto HTML, revisando conceitos fundamentais de estruturação de páginas, organização de arquivos e utilização básica de HTML e CSS para construir páginas simples e funcionais.

_1 imagem(ns) no slide._

### Slide 7

- Para pensarmos juntos...
- Lucas começou a desenvolver um site para divulgar um campeonato escolar de jogos digitais. Ele criou a estrutura inicial da página, adicionou títulos, textos e imagens, mas percebeu que o site estava desorganizado visualmente e difícil de navegar.

_1 imagem(ns) no slide._

### Slide 8

- Para pensarmos juntos...
- Por que planejar a estrutura visual e organizar corretamente os elementos HTML é importante no desenvolvimento de um site?
- Conversem e apresentem suas visões

_2 imagem(ns) no slide._

### Slide 9

- Resposta
- Planejar a estrutura visual ajuda a criar páginas mais intuitivas, bonitas e fáceis de utilizar. Quando os elementos HTML são organizados corretamente, o usuário encontra informações com facilidade e consegue navegar pelo site sem dificuldades. Além disso, uma boa estrutura facilita futuras atualizações e manutenção do projeto.

_1 imagem(ns) no slide._

### Slide 10

- Conceituando
- O desenvolvimento de projetos em HTML é uma das etapas fundamentais da construção de sites. Nesta fase, os desenvolvedores estruturam conteúdos, organizam imagens, textos e componentes visuais que formarão a interface da página.

_1 imagem(ns) no slide._

### Slide 11

- Conceituando
- HTML é a linguagem responsável pela estrutura das páginas web. Em conjunto com o CSS, é possível criar páginas organizadas, estilizadas e adaptadas para diferentes dispositivos.

_1 imagem(ns) no slide._

### Slide 12

- Conceituando
- Esses conceitos são utilizados em:
- Sites institucionais;
- Lojas virtuais;
- Blogs;
- Plataformas de streaming;
- Sistemas empresariais;
- Redes sociais.

_1 imagem(ns) no slide._

### Slide 13

- Conceituando
- Por Que o Tema é Importante?
- Criar projetos organizados em HTML é importante porque:
- Facilita a manutenção do site;
- Melhora a experiência do usuário;
- Permite expansão futura do projeto;
- Ajuda no trabalho em equipe;
- Torna o desenvolvimento mais profissional.

_1 imagem(ns) no slide._

### Slide 14

- Exemplo Prático: Estrutura Inicial de uma Página
- <!DOCTYPE html>
- <html lang="pt-br">
- <head>
- <meta charset="UTF-8">
- <title>Meu Primeiro Projeto</title>
- </head>
- <body>
- <h1>Bem-vindo ao Meu Site</h1>
- <p>Este é um exemplo simples de estrutura HTML.</p>
- <img src="https://via.placeholder.com/300" alt="Imagem exemplo">
- </body>
- </html>

_1 imagem(ns) no slide._

### Slide 15

- Ainda sobre o HTML e CSS, vamos conhecer praticando?
- Na plataforma Alura vamos acessar o seguinte curso:
- Link para o curso: https://cursos.alura.com.br/course/html-css-praticando-html-css
- Ao longo das atividades, você vai encontrar alguns quizzes e eles não estão ali por acaso! Eles são oportunidades rápidas para testar seu entendimento, reforçar o que aprendeu e identificar pontos que ainda podem melhorar.

_3 imagem(ns) no slide._

### Slide 16

- Apresentação
- 5 minutos
- Para inicio deste projeto o ideal é que você já tenha uma base de HTML.
- Link para tarefa: https://cursos.alura.com.br/course/html-css-praticando-html-css/task/103157
- Considerando as aulas anteriores, entende-se que você já tenha uma base de HTML e CSS para iniciar esse novo projeto.
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 17

- A base do HTML
- 8 minutos
- Temos um cliente chamado Alura Plus. É uma plataforma de streaming como a Netflix, a Amazon Prime, a Disney Plus. E eles querem que você desenvolva uma página inicial para o site deles.
- Link para tarefa: https://cursos.alura.com.br/course/html-css-praticando-html-css/task/103158
- Os elementos iniciais do projeto foram entregues em layout da ferramenta figma.
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 18

- Começando com CSS
- 12 minutos
- Antes da utilização, detectar os padrões de arquivos e suas características.
- Link para tarefa: https://cursos.alura.com.br/course/html-css-praticando-html-css/task/103159
- Inicialmente a parte estrutural é considerada a importante na criação, após a avaliação dos elementos se define o estilo que será aplicado.
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 19

- Inserindo imagens
- 9 minutos
- Definimos algumas configurações base, como: variáveis, o background-color da página, a cor padrão das letras (branca).
- Link para tarefa: https://cursos.alura.com.br/course/html-css-praticando-html-css/task/103160
- Vamos construir as imagens porque temos dois tipos de imagem no Figma.
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 20

- Vamos praticar?
- Prepare-se, porque nessa atividade, você vai sair do modo aprender e entrar direto no modo praticar.
- A atividade prática vai colocar você diante de um desafio real, que faz relação com o conteúdo aprendido até aqui.

_1 imagem(ns) no slide._

### Slide 21

- O que vimos na aula de hoje:
- Aprofundamos o desenvolvimento de projetos em HTML, compreendendo a importância da organização estrutural, da utilização do CSS e da criação de páginas mais profissionais.

_1 imagem(ns) no slide._

### Slide 22

- Pronto para desbloquear sua carreira de TI?
- Está perdido estudando mas não sabe por onde começar? Se a resposta é sim, você está no lugar certo! Descubra as estratégias e ferramentas essenciais para te ajudar a desbloquear seu potencial em TI e buscar sua primeira vaga de emprego no setor!
- Este e-book é um guia completo para quem busca começar pelos melhores caminhos para se tornar um excelente profissional de TI, ensinando a identificar perfis profissionais, aplicar técnicas de estudo eficazes, transformar teoria em prática, e aumentar a visibilidade de seu trabalho no mercado de trabalho. Ideal para novatos e profissionais em transição.
- E o melhor, ele pode ser seu, inteiramente grátis!
- Basta clicar AQUI e realizar o seu cadastro com o seu @escola!

_3 imagem(ns) no slide._

### Slide 23

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

### Slide 24

_(sem texto)_

## Atividade

_Fonte: AULA 43_ATIVIDADE_PROGRAMAÇÃO FRONT END.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação Front-End

2ª SÉRIE

ATIVIDADE AULA 43

Questão 1

Qual é a vantagem de separar HTML e CSS em arquivos diferentes?

A) Dificultar alterações futuras

B) Melhorar organização e manutenção

C) Impedir funcionamento do site

D) Reduzir imagens automaticamente

Resposta Correta: B

Separar HTML e CSS deixa o projeto mais organizado e facilita alterações futuras.

Questão 2

Qual ferramenta permite criar layouts antes da programação do site?

A) Figma

B) Bloco de Notas

C) Calculadora

D) Paint

Resposta Correta: A

O Figma é utilizado para planejar visualmente interfaces antes do desenvolvimento do código.

## Prática

_Fonte: AULA 43_PRÁTICA_PROGRAMAÇÃO FRONT END.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

PROGRAMAÇÃO FRONT END

2ª SÉRIE

ATIVIDADE PRÁTICA AULA 43

##### 1. Objetivo da Aula Prática

Ao final da aula prática, o estudante será capaz de:

- Organizar corretamente elementos HTML em uma página web.
- Melhorar a estrutura visual e navegacional de um projeto.
- Aplicar CSS para criar páginas mais organizadas e profissionais.
- Inserir textos, imagens e seções de forma estruturada.
- Compreender a importância do planejamento visual em projetos web.
Produto final esperado:

- Página inicial organizada visualmente, contendo estrutura HTML bem definida, imagens, textos e estilização inicial com CSS.

##### 2. Ferramentas Recomendadas

###### VS Code

- Para que serve: desenvolvimento do projeto HTML e CSS.
- Por que é adequado: oferece recursos completos para programação web.
- Como facilita o aprendizado: ajuda na organização do código e dos arquivos.

###### Navegador Web

- Para que serve: visualizar a página criada.
- Por que é adequado: permite validar aparência e funcionamento.
- Como facilita o aprendizado: mostra o resultado em tempo real.

###### Figma

- Link: https://www.figma.com/
- Para que serve: visualizar o layout do projeto.
- Por que é adequado: apresenta o design-base da interface.
- Como facilita o aprendizado: auxilia no planejamento visual da página.

###### GitHub — Imagens do Projeto

- Link: https://github.com/alura-cursos/aluraplus/tree/aula04/img
- Para que serve: disponibilizar imagens utilizadas no projeto.
- Como facilita o aprendizado: permite trabalhar com elementos reais de interface.

##### 3. Checklist Inicial

Antes de iniciar a prática, o estudante deve ter:

- Projeto da aula anterior criado
- Arquivos:
- index.html
- style.css
- pasta img
- Imagens do projeto disponíveis
- Navegador atualizado
- Conexão com internet
Material de apoio indicado na aula: https://cursos.alura.com.br/course/html-css-praticando-html-css

##### 4. Passo a Passo do Docente (Aula de até 50 minutos)

###### Preparações necessárias

- Garantir que todos tenham o projeto da Aula 42 aberto.
- Revisar rapidamente:
- Estrutura HTML
- CSS externo
- Organização de arquivos

###### Condução da aula

###### Contextualização (5 minutos)

Apresentar cenário:

- Um site visualmente desorganizado dificulta navegação.
Perguntar:

- Como organizar uma página para melhorar a experiência do usuário?

###### Organização estrutural do HTML (10 minutos)

Demonstrar:

- Organização de:
- títulos
- textos
- imagens
- seções
Explicar:

- Hierarquia visual.
- Estrutura semântica.

###### Trabalhando com CSS (10 minutos)

Demonstrar:

- Ajustar:
- espaçamentos
- alinhamentos
- largura de elementos
- tipografia
Explicar importância da consistência visual.

###### Inserindo e organizando imagens (10 minutos)

Demonstrar:

- Inserção correta de imagens.
- Ajuste de tamanho.
- Organização visual das imagens na página.

###### Prática guiada (10 minutos)

Alunos devem:

- Melhorar layout.
- Ajustar organização dos elementos.
- Aplicar CSS na estrutura criada.
- Testar visual da página.

###### Revisão e fechamento (5 minutos)

- Conferir:
- alinhamentos
- organização visual
- carregamento das imagens

###### Pontos de atenção

- Manter indentação organizada.
- Não exagerar nos estilos.
- Verificar caminhos das imagens.
- Testar frequentemente no navegador.

##### 5. Atividade Prática — Descrição Geral

O estudante deverá:

- Evoluir o projeto iniciado anteriormente.
- Melhorar organização visual da página.
- Inserir imagens corretamente.
- Aplicar estilos utilizando CSS.
Problema real simulado: Desenvolvimento inicial de uma página institucional profissional.

Habilidade desenvolvida: Estruturação visual e organização de interfaces web.

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

- Abra o projeto iniciado na aula anterior.
- Verifique a organização da pasta:
- HTML
- CSS
- imagens
- Abra o arquivo index.html.
- Organize:
- títulos
- parágrafos
- imagens
- Crie seções para separar conteúdos.
- No style.css, aplique:
- espaçamento
- alinhamento
- tipografia
- Ajuste tamanho das imagens.
- Centralize ou alinhe elementos conforme necessário.
- Salve os arquivos.
- Abra no navegador.
- Verifique:
- visual da página
- alinhamentos
- carregamento das imagens
- Ajuste detalhes finais.

##### 8. Exemplo ou Demonstração

###### Estrutura básica organizada

- <section>
- <h1>Bem-vindo</h1>
- <p>Texto da página.</p>
- </section>

###### Inserindo imagem

- <img src="img/banner.png" alt="Banner do projeto">

###### CSS inicial

- body {
- background-color: #000;
- color: white;
- font-family: Arial, sans-serif;
- }

###### Conceitos reforçados

- HTML organiza conteúdo.
- CSS melhora apresentação visual.
- Estrutura organizada facilita manutenção.

##### 9. Resultado Esperado

O estudante deverá apresentar:

- Página HTML organizada.
- Estrutura visual mais profissional.
- CSS aplicado corretamente.
- Imagens alinhadas e funcionando.
- Código organizado.
O professor verifica:

- Organização estrutural do HTML.
- Funcionamento das imagens.
- Aplicação do CSS.
- Qualidade visual da interface.

##### 10. Formato de Entrega da Atividade

- Formato: Pasta compactada contendo:
- index.html
- style.css
- pasta img
- Entrega: ao final da aula.
- Prazo sugerido: imediato.

##### 11. Encerramento e Reflexão

Perguntas orientadoras:

- Por que organização visual é importante?
- Como o CSS melhora a navegação?
- O que torna uma página mais profissional?
