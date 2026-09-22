---
titulo: "Posicionando Elementos na Página – Parte I"
tipo: rco-seed
disciplina: programacao-front-end
sigla_rco: PFE
trimestre: 2
ordem_rco: 46
serie: 2
aula_rco: "Aula 46"
slides: 21
tem_atividade: true
tem_pratica: true
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/2TRI/46-posicionando-elementos-na-pagina-parte-i/46-posicionando-elementos-na-pagina-parte-i.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/2TRI/46-posicionando-elementos-na-pagina-parte-i/AULA 46_ATIVIDADE_PROGRAMAÇÃO FRONT END.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/2TRI/46-posicionando-elementos-na-pagina-parte-i/AULA 46_PRÁTICA_PROGRAMAÇÃO FRONT END.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Posicionando Elementos na Página – Parte I

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- Programação Front-End
- 2ª Série
- Posicionando Elementos na Página – Parte I
- Aula 46

_1 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- COMPETÊNCIA(S) A SER(EM) DESENVOLVIDA(S) NESTA AULA:
- De acordo com o Plano de Curso de Desenvolvimento de Sistemas:
- HABILIDADE(S) A SER(EM) DESENVOLVIDA(S) NESTA AULA:
- Desenvolver interfaces gráficas para aplicações computacionais.
- Organizar layout de páginas web.

_1 imagem(ns) no slide._

### Slide 4

- Nesta aula vamos:
- Colocar em prática posicionamento de elementos em HTML Parte I.
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
- rojeto aula anterior:
- https://github.com/alura-cursos/aluraplus/archive/refs/heads/aula02.zip
- VS Code:
- https://code.visualstudio.com/

_2 imagem(ns) no slide._

### Slide 6

- Aula anterior
- Concluímos os estudos práticos sobre criação de páginas com uso de HTML e CSS, conceitos sobre criação de botões.

_1 imagem(ns) no slide._

### Slide 7

- Para pensarmos juntos...
- Luiza é uma desenvolvedora web iniciante e está trabalhando em um projeto HTML para criar um site pessoal. Ela percebe que o texto dentro de suas caixas de conteúdo está muito próximo das bordas e que os elementos adjacentes também estão muito próximos uns dos outros, tornando a página confusa e difícil de ler.

_1 imagem(ns) no slide._

### Slide 8

- Para pensarmos juntos...
- Ela se pergunta: "Como posso adicionar espaço entre o conteúdo e as bordas das caixas e entre os elementos adjacentes para melhorar a legibilidade e a aparência do meu site?"
- Conversem e apresentem suas visões

_2 imagem(ns) no slide._

### Slide 9

- Resposta
- Luiza pode usar as propriedades CSS padding e margin para adicionar espaço entre o conteúdo e as bordas das caixas e entre os elementos adjacentes, respectivamente. O padding ajudará a criar espaço interno entre o conteúdo e as bordas das caixas, enquanto o margin ajudará a separar os elementos adjacentes, proporcionando uma aparência mais organizada e legível para o site.

_1 imagem(ns) no slide._

### Slide 10

- Conceituando
- As propriedades CSS margin e padding são ferramentas fundamentais para a organização e o layout de elementos em páginas HTML. Elas ajudam a separar os elementos de maneira eficaz, melhorando a legibilidade e a aparência geral do site.

_1 imagem(ns) no slide._

### Slide 11

- Conceituando
- A propriedade margin é usada para controlar o espaço externo ao redor de um elemento, separando-o de seus elementos adjacentes. Ajustar a margem permite posicionar os elementos em relação uns aos outros de forma mais precisa e criar espaçamentos consistentes e equilibrados entre eles.

_1 imagem(ns) no slide._

### Slide 12

- Conceituando
- Por outro lado, a propriedade padding é usada para controlar o espaço interno entre o conteúdo de um elemento e sua borda. O padding ajuda a garantir que o conteúdo não fique muito próximo das bordas, tornando a apresentação mais organizada e legível.

_1 imagem(ns) no slide._

### Slide 13

- Conceituando
- Tanto a margin quanto o padding são fundamentais na criação de layouts atraentes e funcionais em páginas HTML. Eles permitem que os desenvolvedores controlem a disposição dos elementos na página e garanta que o conteúdo seja apresentado de maneira clara e agradável aos usuários.

_1 imagem(ns) no slide._

### Slide 14

- Ainda sobre o HTML e CSS, vamos conhecer praticando?
- DESENVOLVIMENTO DE SISTEMAS
- Na plataforma Alura vamos acessar o seguinte curso:
- Link para o curso: https://cursos.alura.com.br/course/html-css-praticando-html-css
- Ao longo das atividades, você vai encontrar alguns quizzes e eles não estão ali por acaso! Eles são oportunidades rápidas para testar seu entendimento, reforçar o que aprendeu e identificar pontos que ainda podem melhorar.

_5 imagem(ns) no slide._

### Slide 15

- Margins e paddings
- 7 minutos
- Nas últimas aulas construímos todos os elementos HTML e estilizamos eles
- Link para tarefa: https://cursos.alura.com.br/course/html-css-praticando-html-css/task/103164
- Apesar de já ter criado muita coisa, precisamos criar mais elementos e ajustar também.
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 16

- Alinhamentos
- 3 minutos
- Então já temos nas últimas aulas que criamos os elementos HTML, estilizamos eles com CSS e fizemos na última atividade os espaçamentos.
- Link para tarefa: https://cursos.alura.com.br/course/html-css-praticando-html-css/task/103165
- Nesse caso temos que centralizar a página, iremos realizar alinhamentos.
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 17

- Vamos praticar?
- Prepare-se, porque nessa atividade, você vai sair do modo aprender e entrar direto no modo praticar.
- A atividade prática vai colocar você diante de um desafio real, que faz relação com o conteúdo aprendido até aqui.

_1 imagem(ns) no slide._

### Slide 18

- O que vimos na aula de hoje:
- Aprendemos utilizar elementos margin pads e alinhamento de elementos em páginas HTML e CSS.

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

_Fonte: AULA 46_ATIVIDADE_PROGRAMAÇÃO FRONT END.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação Front-End

2ª SÉRIE

ATIVIDADE AULA 46

Questão 1

Qual propriedade CSS é usada para definir o espaço entre a borda de um elemento e seu conteúdo?

a) margin

b) padding

c) border

d) spacing

Resposta correta: b) padding

Comentário: A propriedade CSS padding é usada para definir o espaço entre a borda de um elemento e seu conteúdo. O padding é um espaço interno que proporciona uma separação entre o conteúdo do elemento e sua borda, tornando a apresentação mais organizada e legível.

Questão 2

Qual propriedade CSS é usada para definir o espaço entre a borda de um elemento e os elementos adjacentes?

a) margin

b) padding

c) border

d) spacing

Resposta correta: a) margin

Comentário: A propriedade CSS margin é usada para definir o espaço entre a borda de um elemento e os elementos adjacentes. A margem é um espaço externo que proporciona uma separação entre elementos adjacentes, ajudando a organizar o layout e a garantir que os elementos não fiquem muito próximos uns dos outros.

## Prática

_Fonte: AULA 46_PRÁTICA_PROGRAMAÇÃO FRONT END.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

PROGRAMAÇÃO FRONT END

2ª SÉRIE

ATIVIDADE PRÁTICA AULA 46

##### 1. Objetivo da Aula Prática

Ao final da aula prática, o estudante será capaz de:

- Utilizar corretamente as propriedades CSS:
- margin
- padding
- Aplicar espaçamentos internos e externos em elementos HTML.
- Organizar visualmente os elementos da página.
- Melhorar legibilidade e alinhamento de conteúdos.
- Centralizar elementos utilizando CSS.
Produto final esperado:

- Página HTML organizada visualmente, com espaçamentos adequados e elementos alinhados corretamente.

##### 2. Ferramentas Recomendadas

###### VS Code

- Para que serve: edição dos arquivos HTML e CSS.
- Por que é adequado: facilita organização e visualização do código.
- Como facilita o aprendizado: permite testar rapidamente alterações no layout.

###### Navegador Web

- Para que serve: visualizar os resultados dos ajustes visuais.
- Por que é adequado: mostra o comportamento real da página.
- Como facilita o aprendizado: possibilita validar alinhamentos e espaçamentos.

###### DevTools do Navegador

- Para que serve: inspecionar elementos e visualizar margens/paddings.
- Por que é adequado: ajuda a compreender o espaço ocupado pelos elementos.
- Como facilita o aprendizado: demonstra visualmente diferenças entre margin e padding.

##### 3. Checklist Inicial

Antes de iniciar a prática, o estudante deve ter:

- Projeto das aulas anteriores aberto
- Arquivos:
- index.html
- style.css
- Estrutura HTML criada
- Navegador atualizado
- VS Code instalado
- Conexão com internet
Material de apoio indicado na aula: https://cursos.alura.com.br/course/html-css-praticando-html-css

##### 4. Passo a Passo do Docente (Aula de até 50 minutos)

###### Preparações necessárias

- Garantir que todos tenham o projeto funcionando.
- Revisar rapidamente:
- Box model
- Estrutura HTML
- CSS externo

###### Condução da aula

###### Contextualização (5 minutos)

Apresentar cenário:

- Uma página com elementos muito próximos gera confusão visual.
Perguntar:

- Como melhorar a organização e a leitura de uma página?

###### Conceituando Margin e Padding (10 minutos)

Explicar:

###### Margin

- Espaço externo do elemento.

###### Padding

- Espaço interno entre conteúdo e borda.
Demonstrar diferença visual.

Exemplo conceitual:

- .caixa {
- margin: 20px;
- padding: 20px;
- }

###### Trabalhando alinhamento (10 minutos)

Demonstrar:

- Centralização de elementos.
- Ajuste de largura.
- Uso de:
- margin: auto
- text-align
Mostrar diferença antes/depois.

###### Demonstração prática (10 minutos)

Demonstrar:

- Ajustar botão e caixas da página.
- Melhorar espaçamento entre elementos.
- Organizar layout visualmente.

###### Prática guiada (10 minutos)

Alunos devem:

- Aplicar margens.
- Aplicar paddings.
- Centralizar elementos.
- Melhorar alinhamento da página.

###### Revisão e fechamento (5 minutos)

- Conferir organização visual.
- Ajustar exageros de espaçamento.
- Validar alinhamentos.

###### Pontos de atenção

- Não exagerar nos espaçamentos.
- Diferenciar margin e padding.
- Verificar alinhamento no navegador.

##### 5. Atividade Prática — Descrição Geral

O estudante deverá:

- Ajustar espaçamentos da página utilizando margin e padding.
- Melhorar a organização visual dos elementos.
- Centralizar áreas do layout.
- Ajustar aparência geral da interface.
Problema real simulado: Melhoria visual e organização de uma landing page profissional.

Habilidade desenvolvida: Organização de layouts utilizando CSS.

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

- Abra o projeto desenvolvido anteriormente.
- Localize:
- botões
- caixas
- textos
- imagens
- No CSS, aplique:
- padding
- Ajuste o espaço interno dos elementos.
- Depois aplique:
- margin
- Ajuste o espaço entre elementos.
- Centralize uma seção usando:
- margin: auto
- Ajuste alinhamento de textos.
- Salve os arquivos.
- Abra no navegador.
- Verifique:
- organização visual
- espaçamentos
- alinhamentos
- Ajuste detalhes finais.

##### 8. Exemplo ou Demonstração

###### Exemplo de padding

- .botao {
- padding: 15px;
- }

###### Exemplo de margin

- .caixa {
- margin: 20px;
- }

###### Exemplo de centralização

- .container {
- width: 80%;
- margin: auto;
- }

###### Conceitos reforçados

- Padding organiza conteúdo interno.
- Margin separa elementos.
- Espaçamento melhora legibilidade.

##### 9. Resultado Esperado

O estudante deverá apresentar:

- Página visualmente organizada.
- Uso correto de:
- margin
- padding
- Elementos centralizados.
- Melhor alinhamento visual.
O professor verifica:

- Aplicação correta dos espaçamentos.
- Organização visual da interface.
- Funcionamento do layout.

##### 10. Formato de Entrega da Atividade

- Formato: Pasta compactada contendo:
- index.html
- style.css
- imagens utilizadas
- Entrega: ao final da aula.
- Prazo sugerido: imediato.

##### 11. Encerramento e Reflexão

Perguntas orientadoras:

- Qual a diferença entre margin e padding?
- Como o espaçamento melhora a experiência visual?
- O que acontece quando usamos espaçamentos excessivos?
