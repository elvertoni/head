---
titulo: "Finalizando nossa página HTML Parte I"
tipo: rco-seed
disciplina: programacao-front-end
sigla_rco: PFE
trimestre: 2
ordem_rco: 48
serie: 2
aula_rco: "Aula 48"
slides: 21
tem_atividade: true
tem_pratica: true
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/2TRI/48-finalizando-a-pagina-html-parte-i/48-finalizando-a-pagina-html-parte-i.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/2TRI/48-finalizando-a-pagina-html-parte-i/AULA 48_ATIVIDADE_PROGRAMAÇÃO FRONT END.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/2TRI/48-finalizando-a-pagina-html-parte-i/AULA 48_PRÁTICA_PROGRAMAÇÃO FRONT END.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Finalizando nossa página HTML Parte I

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- Programação Front-End
- 2ª Série
- Finalizando nossa página HTML Parte I
- Aula 48

_1 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- COMPETÊNCIA(S) A SER(EM) DESENVOLVIDA(S) NESTA AULA:
- De acordo com o Plano de Curso de Desenvolvimento de Sistemas:
- HABILIDADE(S) A SER(EM) DESENVOLVIDA(S) NESTA AULA:
- Desenvolver interfaces gráficas para aplicações computacionais.
- Finalizar e validar páginas web.

_1 imagem(ns) no slide._

### Slide 4

- Nesta aula vamos:
- Conclusão da mais uma página em HTML.
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store

_5 imagem(ns) no slide._

### Slide 5 (oculto)

- Este material foi elaborado a partir da análise do plano de curso e reúne os conhecimentos essenciais para o Técnico em Desenvolvimento de Sistemas. As aulas foram organizadas com foco na clareza conceitual, na construção gradual dos conteúdos e na utilização de metodologias ativas que favorecem a compreensão, a participação e o desenvolvimento de habilidades e competências de forma significativa.
- De acordo com a matriz curricular do Curso Técnico em Desenvolvimento de Sistemas, que traz em sua essência componentes estruturados para a realização de aulas práticas, cada unidade curricular deve contemplar, além da abordagem teórica, uma proposta de atividade prática a ser desenvolvida pelo professor. Essa orientação assegura a coerência entre o planejamento didático e o que está estabelecido na matriz, promovendo experiências formativas alinhadas ao perfil profissional previsto.
- O professor tem total autonomia para adaptar o conteúdo conforme o contexto da turma, ajustando exemplos, aprofundamentos e estratégias didáticas para otimizar a aprendizagem e a conexão com a prática profissional.
- Se houver falta de conexão ou indisponibilidade de internet durante a aula, os materiais abaixo podem ser utilizados como apoio para elaborar recursos complementares, garantindo a continuidade da abordagem teórica prevista.
- ATENÇÃO PROFESSOR!
- Projeto aula anterior:
- https://github.com/alura-cursos/aluraplus/archive/refs/heads/aula03.zip
- VS Code:
- https://code.visualstudio.com/

_2 imagem(ns) no slide._

### Slide 6

- Aula anterior
- Dando continuidade ao projeto, realizamos os posicionamentos de elementos para podermos deixar a página funcional.

_1 imagem(ns) no slide._

### Slide 7

- Para pensarmos juntos...
- Juliana é uma desenvolvedora web iniciante que trabalha em um projeto de site para uma pequena empresa. Ela precisa criar uma seção de equipe onde as fotos e informações dos membros da equipe sejam exibidas em uma grade responsiva. Juliana sabia que o Flexbox poderia ser usado para resolver esse problema, mas não sabia como aplicá-lo corretamente.
- https://konia.com.br/wp-content/uploads/2020/02/code-1839406_1920-844x563.jpg

_1 imagem(ns) no slide._

### Slide 8

- Para pensarmos juntos...
- Juliana se pergunta: "Como posso usar o Flexbox para criar uma grade responsiva para a seção de equipe do site?"
- Levante a mão quem sabe responder!

_2 imagem(ns) no slide._

### Slide 9

- Resposta
- Para criar uma grade responsiva usando Flexbox, Juliana pode começar definindo a propriedade CSS display: flex; no container que envolve os itens da equipe. Isso transformará o container em um flex container e permitirá que Juliana controle o layout e o alinhamento dos itens da equipe usando as propriedades flexbox.

_1 imagem(ns) no slide._

### Slide 10

- Resposta
- Depois de criar o flex container, ela pode usar a propriedade flex-wrap: wrap; para permitir que os itens da equipe se ajustem automaticamente às linhas seguintes quando não houver espaço suficiente na linha atual. Além disso, Juliana pode usar a propriedade flex nos itens da equipe para controlar o tamanho e a proporção deles em relação aos outros itens. Com essas configurações, a grade responsiva será criada, e os itens da equipe serão ajustados automaticamente para se adaptar a diferentes tamanhos de tela.

_1 imagem(ns) no slide._

### Slide 11

- Conceituando
- O Flexbox, também conhecido como Flexible Box Layout, é um modelo de layout CSS que facilita a criação de layouts responsivos e dinâmicos para páginas HTML. Ele oferece maior flexibilidade e controle sobre o posicionamento e dimensionamento de elementos dentro de um container, permitindo que os elementos se ajustem automaticamente ao espaço disponível. Flexbox é especialmente útil para criar layouts complexos que precisam se adaptar a diferentes tamanhos de tela e dispositivos.
- https://cdn.pixabay.com/photo/2014/07/08/09/58/html5-386614_1280.jpg

_1 imagem(ns) no slide._

### Slide 12

- Conceituando
- Para começar a usar o Flexbox, primeiro você precisa definir um container como um flex container, aplicando a propriedade CSS display: flex;. Ao fazer isso, todos os elementos filhos diretos desse container se tornam itens flexíveis e podem ser posicionados e dimensionados usando as propriedades do Flexbox. Algumas propriedades importantes do Flexbox incluem justify-content, align-items e flex-direction, que controlam o alinhamento e a direção dos itens flexíveis dentro do container.
- https://slideplayer.com.br/slide/3284708/11/images/5/Exemplo+Form+GET+%3Chtml%3E.jpg

_1 imagem(ns) no slide._

### Slide 13

- Conceituando
- Um dos principais benefícios do Flexbox é a capacidade de criar layouts responsivos sem a necessidade de usar técnicas complicadas, como floats ou posicionamento absoluto. Com o Flexbox, você pode criar layouts que se ajustam automaticamente ao tamanho da tela, garantindo que seu site seja adaptável e fácil de usar em uma variedade de dispositivos e tamanhos de tela.
- https://www.seobility.net/en/wiki/images/7/72/HTML-Sitemap.png

_1 imagem(ns) no slide._

### Slide 14

- Conceituando
- Em resumo, o Flexbox é uma poderosa ferramenta CSS que facilita a criação de layouts responsivos e adaptáveis para páginas HTML. Ao usar um flex container e aplicar as propriedades apropriadas do Flexbox, você pode criar layouts complexos e flexíveis que se adaptam automaticamente aos diferentes tamanhos de tela e dispositivos, melhorando a experiência do usuário e facilitando a manutenção do código.
- https://www.seobility.net/en/wiki/images/c/ca/HTML-Special-Characters.png

_1 imagem(ns) no slide._

### Slide 15

- Ainda sobre o HTML e CSS, vamos conhecer praticando?
- Na plataforma Alura vamos acessar o seguinte curso:
- Link para o curso: https://cursos.alura.com.br/course/html-css-praticando-html-css
- Ao longo das atividades, você vai encontrar alguns quizzes e eles não estão ali por acaso! Eles são oportunidades rápidas para testar seu entendimento, reforçar o que aprendeu e identificar pontos que ainda podem melhorar.

_3 imagem(ns) no slide._

### Slide 16

- Flexbox
- 16 minutos
- O que falta fazermos em nossa página? O que vamos fazer nessa aula?
- Link para tarefa: https://cursos.alura.com.br/course/html-css-praticando-html-css/task/103168
- Criar os layouts flexíveis para dispositivos diferentes, com o flexbox temos uma utilidade em criar layouts complexos que precisam se adaptar.
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 17

- Vamos praticar?
- Prepare-se, porque nessa atividade, você vai sair do modo aprender e entrar direto no modo praticar.
- A atividade prática vai colocar você diante de um desafio real, que faz relação com o conteúdo aprendido até aqui.

_1 imagem(ns) no slide._

### Slide 18

- O que vimos na aula de hoje:
- Aprendemos o flexbox em páginas HTML e CSS.

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

_Fonte: AULA 48_ATIVIDADE_PROGRAMAÇÃO FRONT END.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação Front-End

2ª SÉRIE

ATIVIDADE AULA 48

Questão 1

Qual propriedade CSS deve ser aplicada a um container para transformá-lo em um flex container?

a) position: flex;

b) display: flex;

c) flex-direction: row;

d) flex-wrap: wrap;

Resposta correta: b) display: flex;

Ao aplicar a propriedade display: flex; a um container, ele se transforma em um flex container, e seus filhos diretos se tornam itens flexíveis. Isso permite usar as propriedades do Flexbox para controlar o posicionamento e o dimensionamento desses itens.

Questão 2

Qual propriedade do Flexbox é usada para controlar a direção em que os itens flexíveis são dispostos dentro do container?

a) justify-content;

b) align-items;

c) flex-wrap;

d) flex-direction;

Resposta correta: d) flex-direction;

A propriedade flex-direction controla a direção em que os itens flexíveis são organizados dentro do container. Os valores comuns para essa propriedade são row (horizontal) e column (vertical), permitindo que os itens sejam dispostos em uma única linha ou coluna, respectivamente.

## Prática

_Fonte: AULA 48_PRÁTICA_PROGRAMAÇÃO FRONT END.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

PROGRAMAÇÃO FRONT END

2ª SÉRIE

ATIVIDADE PRÁTICA AULA 48

##### 1. Objetivo da Aula Prática

Ao final da aula prática, o estudante será capaz de:

- Compreender o funcionamento básico do Flexbox.
- Organizar elementos utilizando layouts flexíveis.
- Criar seções responsivas que se adaptam a diferentes tamanhos de tela.
- Utilizar propriedades como:
- display: flex
- justify-content
- align-items
- flex-wrap
- Melhorar a organização visual do projeto desenvolvido nas aulas anteriores.

###### Produto Final Esperado

Uma nova seção da página desenvolvida utilizando Flexbox para organizar imagens, textos e botões de forma responsiva e visualmente agradável.

##### 2. Ferramentas Recomendadas

###### VS Code

Para que serve: desenvolvimento e edição do HTML e CSS.

Por que é adequado: permite visualizar e organizar facilmente a estrutura do projeto.

Como facilita o aprendizado: oferece recursos de destaque de sintaxe e visualização rápida das alterações.

###### Navegador Web

Para que serve: testar e visualizar a página.

Por que é adequado: permite verificar o comportamento do layout.

Como facilita o aprendizado: possibilita observar como o Flexbox organiza os elementos.

###### DevTools do Navegador

Para que serve: inspecionar elementos HTML e regras CSS.

Por que é adequado: permite visualizar containers e itens flexíveis.

Como facilita o aprendizado: ajuda a compreender o posicionamento dos elementos.

##### 3. Checklist Inicial

Antes de iniciar a prática, o estudante deve possuir:

Projeto desenvolvido nas aulas anteriores

Arquivos:

- index.html
- style.css
Estrutura HTML funcional

Imagens do projeto disponíveis

Navegador atualizado

VS Code instalado

Conexão com internet

###### Material de Apoio

Curso Alura:

https://cursos.alura.com.br/course/html-css-praticando-html-css

##### 4. Passo a Passo do Docente (Aula de até 50 minutos)

###### Preparações Necessárias

- Verificar se todos possuem o projeto aberto.
- Garantir que CSS e imagens estejam funcionando.
- Revisar rapidamente:
- classes CSS
- sections
- margin
- padding

###### Contextualização (5 minutos)

Apresentar o problema:

Muitos sites precisam organizar imagens e textos lado a lado, mas sem quebrar o layout em diferentes tamanhos de tela.

Perguntar:

Como podemos organizar vários elementos sem precisar calcular posições manualmente?

###### Introdução ao Flexbox (10 minutos)

Explicar:

- O que é um Flex Container.
- O que são Flex Items.
- Benefícios do Flexbox:
- alinhamento simples
- responsividade
- organização visual
Demonstrar visualmente.

###### Demonstração Prática (10 minutos)

Criar uma seção contendo:

- imagem
- título
- descrição
- botão
Aplicar:

- display:flex
- justify-content
- align-items
Mostrar os resultados em tempo real.

###### Prática Guiada (15 minutos)

Orientar os alunos a:

- criar nova seção;
- inserir conteúdo;
- aplicar Flexbox;
- ajustar alinhamentos.

###### Revisão e Validação (10 minutos)

Verificar:

- alinhamento correto;
- distribuição dos elementos;
- organização visual;
- responsividade básica.

###### Pontos de Atenção

- Não aplicar Flexbox em elementos errados.
- Manter estrutura organizada.
- Verificar fechamento correto das tags HTML.
- Evitar excesso de espaçamentos.

##### 5. Atividade Prática — Descrição Geral

O estudante deverá criar uma nova seção para a landing page utilizando Flexbox.

Essa seção deverá conter:

- uma imagem;
- um título;
- um texto descritivo;
- um botão.
Todos os elementos deverão ser organizados utilizando Flexbox.

###### Problema Real Simulado

Desenvolvimento de uma seção promocional para uma plataforma de streaming.

###### Habilidade Desenvolvida

Construção de layouts modernos e responsivos utilizando CSS Flexbox.

##### 6. Metodologia Ativa Utilizada

###### Aprendizagem Baseada em Projeto (PBL)

Os alunos continuam evoluindo um projeto real.

###### Experimentação Prática

Testam diferentes propriedades do Flexbox.

###### Ensino por Descoberta

Observam como cada propriedade altera o layout.

###### Elementos de Lemov

- Modelagem
- Prática Guiada
- Verificação de Compreensão
- Feedback Imediato
- Revisão Contínua

##### 7. Passo a Passo da Atividade Prática (para os alunos)

###### Etapa 1 – Criar a nova seção

- Abra o arquivo index.html.
- Crie uma nova <section>.
- Adicione:
- imagem;
- título;
- texto;
- botão.

###### Etapa 2 – Criar container Flex

- Adicione uma classe ao container principal.
- No CSS, aplique:
- display flex

###### Etapa 3 – Organizar elementos

- Ajuste o alinhamento horizontal.
- Ajuste o alinhamento vertical.
- Organize os espaçamentos.

###### Etapa 4 – Responsividade básica

- Permita quebra de linha usando Flexbox.
- Teste em diferentes larguras de tela.

###### Etapa 5 – Finalização

- Salve os arquivos.
- Atualize o navegador.
- Revise o resultado visual.

##### 8. Exemplo ou Demonstração

###### Estrutura HTML

- <section class="secao-flex">
- <img src="img/plataforma.png" alt="Plataforma">
- <div>
- <h2>Assista onde quiser</h2>
- <p>Acesse seus conteúdos favoritos em diversos dispositivos.</p>
- <button>Saiba Mais</button>
- </div>
- </section>

###### Estrutura CSS

- .secao-flex {
- display: flex;
- justify-content: space-between;
- align-items: center;
- flex-wrap: wrap;
- }

###### Conceitos Aplicados

| Propriedade | Função |
| --- | --- |
| display:flex | ativa Flexbox |
| justify-content | alinhamento horizontal |
| align-items | alinhamento vertical |
| flex-wrap | quebra de linha automática |

##### 9. Resultado Esperado

O estudante deverá entregar:

- Nova seção criada.
- Flexbox funcionando corretamente.
- Elementos alinhados.
- Layout organizado.
- Código HTML e CSS organizado.

###### Critérios de Verificação

O professor deverá verificar:

Uso correto do Flexbox

Estrutura HTML organizada

Alinhamento visual adequado

Reutilização de estilos

Funcionamento da página

##### 10. Formato de Entrega da Atividade

###### Arquivos

- index.html
- style.css
- imagens utilizadas

###### Nome da Pasta

- Aula48_NomeSobrenome
Exemplo:

- Aula48_JoaoSilva

###### Local de Entrega

- Google Classroom
- Google Drive
- AVA da instituição

###### Prazo

Entrega ao final da aula.

##### 11. Encerramento e Reflexão

Promova uma conversa final com a turma:

###### Perguntas para reflexão

- Qual a principal vantagem do Flexbox?
- Como o Flexbox facilita a criação de layouts responsivos?
- Em quais situações você utilizaria Grid em vez de Flexbox?
- Como a organização visual influencia a experiência do usuário?
