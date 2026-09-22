---
titulo: "Entendendo como o computador lê o código - Parte I"
tipo: rco-seed
disciplina: introducao-a-computacao
sigla_rco: IAC
trimestre: 2
ordem_rco: 25
serie: 1
aula_rco: "Aula 25"
slides: 26
tem_atividade: true
tem_pratica: true
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/IAC/2TRI/25-entendendo-como-o-computador-le-o-codigo-parte-i/25-entendendo-como-o-computador-le-o-codigo-parte-i.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/IAC/2TRI/25-entendendo-como-o-computador-le-o-codigo-parte-i/AULA 25_INTRODUÇÃO A COMPUTAÇÃO ATIVIDADE.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/IAC/2TRI/25-entendendo-como-o-computador-le-o-codigo-parte-i/AULA 25_PRÁTICA INTRODUÇÃO A COMPUTAÇÃO.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Entendendo como o computador lê o código - Parte I

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- INTRODUÇÃO A COMPUTAÇÃO
- 1ª SÉRIE
- Entendendo como o computador lê o código - Parte I
- Aula 25

_3 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- COMPETÊNCIA(S) A SER(EM) DESENVOLVIDA(S) NESTA AULA:
- De acordo com o Plano de Curso de Desenvolvimento de Sistemas:
- HABILIDADE(S) A SER(EM) DESENVOLVIDA(S) NESTA AULA:
- Desenvolver sistemas computacionais utilizando ambiente de desenvolvimento.
- Compreender os fundamentos da ciência da computação.

_1 imagem(ns) no slide._

### Slide 4

- Este material foi elaborado a partir da análise do plano de curso e reúne os conhecimentos essenciais para o Técnico em Desenvolvimento de Sistemas. As aulas foram organizadas com foco na clareza conceitual, na construção gradual dos conteúdos e na utilização de metodologias ativas que favorecem a compreensão, a participação e o desenvolvimento de habilidades e competências de forma significativa.
- De acordo com a matriz curricular do Curso Técnico em Desenvolvimento de Sistemas, que traz em sua essência componentes estruturados para a realização de aulas práticas, cada unidade curricular deve contemplar, além da abordagem teórica, uma proposta de atividade prática a ser desenvolvida pelo professor. Essa orientação assegura a coerência entre o planejamento didático e o que está estabelecido na matriz, promovendo experiências formativas alinhadas ao perfil profissional previsto.
- O professor tem total autonomia para adaptar o conteúdo conforme o contexto da turma, ajustando exemplos, aprofundamentos e estratégias didáticas para otimizar a aprendizagem e a conexão com a prática profissional.
- Se houver falta de conexão ou indisponibilidade de internet durante a aula, os materiais abaixo podem ser utilizados como apoio para elaborar recursos complementares, garantindo a continuidade da abordagem teórica prevista.
- github.com
- ATENÇÃO PROFESSOR!

_2 imagem(ns) no slide._

### Slide 5

- DESENVOLVIMENTO DE SISTEMAS
- Nesta aula, vamos:
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store
- Entender como o computador lê o seu código - Parte I.

_7 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Este material foi elaborado com base na análise do plano de curso, abrangendo os conhecimentos essenciais para o curso Técnico em Desenvolvimento de Sistemas. Inclui aulas práticas desenvolvidas de acordo com as metodologias ativas, visando ao desenvolvimento de habilidades e competências de forma dinâmica e significativa. Você tem total liberdade para personalizar o material de acordo com seu contexto, otimizando o aproveitamento deste conteúdo.
- Em caso de falta ou indisponibilidade de acesso à internet no local de aula, você poderá utilizar os seguintes artigos para criação de material complementar para auxiliar na aula:
- Para saber mais: https://www.colegiopraxis.com.br/introducao-a-informatica-o-que-voce-precisa-saber/%5B1
- ATENÇÃO PROFESSOR!

_5 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Na aula anterior...
- Concluímos os estudos a respeito de arquitetura de um computador.

_4 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Ana, uma desenvolvedora iniciante, está aprendendo sobre linguagens de programação e como os programas são executados em computadores.
- Ela descobriu que os computadores só entendem a linguagem de máquina, que é um conjunto de instruções binárias específicas para cada tipo de processador.

_4 imagem(ns) no slide._

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- No entanto, Ana ainda não sabe como o código escrito em linguagens de alto nível, como Python ou Java, é convertido em linguagem de máquina para que o computador possa executá-lo.

_4 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Ana se questiona: Como o código que escrevo em linguagens de alto nível é traduzido para a linguagem de máquina, de modo que o computador possa executá-lo?
- Troque ideias com seus colegas!

_5 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- O código escrito em linguagens de alto nível é convertido em linguagem de máquina por meio de compiladores ou interpretadores. Ambos são tradutores de código que transformam o código-fonte legível por humanos em instruções binárias compreensíveis pela máquina.

_4 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- Linguagem de máquina é a forma mais básica e primitiva de comunicação entre um computador e seu processador.
- Essa linguagem consiste em instruções binárias, que são sequências de 0s e 1s, compreensíveis apenas pelo processador. Cada instrução corresponde a uma operação específica, como adição, subtração ou movimentação de dados.
- Embora os computadores possam processar rapidamente a linguagem de máquina, ela é difícil de ser entendida e manipulada diretamente pelos seres humanos.

_4 imagem(ns) no slide._

### Slide 13

- DESENVOLVIMENTO DE SISTEMAS
- Em contraste, temos as linguagens de programação de alto nível, como Python, Java e C++, que são projetadas para serem mais compreensíveis e acessíveis para os programadores.
- Essas linguagens permitem que os desenvolvedores escrevam programas utilizando palavras, símbolos e estruturas de controle familiares, facilitando a criação e a manutenção do código.

_4 imagem(ns) no slide._

### Slide 14

- DESENVOLVIMENTO DE SISTEMAS
- Para que um programa escrito em uma linguagem de alto nível seja executado em um computador, é necessário convertê-lo para a linguagem de máquina. Essa conversão é realizada por meio de tradutores de código, como compiladores e interpretadores.

_4 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- Um compilador é um programa que traduz todo o código-fonte de uma linguagem de alto nível para a linguagem de máquina antes da execução. Ele gera um arquivo executável que pode ser rodado no computador.
- O processo de compilação acontece apenas uma vez, e depois, o arquivo gerado pode ser executado várias vezes sem a necessidade de recompilar.

_4 imagem(ns) no slide._

### Slide 16

- DESENVOLVIMENTO DE SISTEMAS
- Já um interpretador traduz e executa o código-fonte linha por linha durante a execução do programa. Isso significa que ele lê cada instrução em uma linguagem de alto nível, a traduz para a linguagem de máquina e a executa imediatamente.
- Esse processo acontece em tempo real, tornando a depuração e a modificação do código mais simples, porém, pode resultar em uma execução mais lenta em comparação com os programas compilados.

_4 imagem(ns) no slide._

### Slide 17

- DESENVOLVIMENTO DE SISTEMAS
- Para responder
- Qual é a principal diferença entre um compilador e um interpretador no processo de tradução de código de alto nível para linguagem de máquina?
- Troque ideias com seus colegas!

_5 imagem(ns) no slide._

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- A principal diferença é que um compilador traduz todo o código-fonte de uma linguagem de alto nível para linguagem de máquina antes da execução, gerando um arquivo executável, enquanto um interpretador traduz e executa o código-fonte linha por linha durante a execução do programa.

_4 imagem(ns) no slide._

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- Link para o curso: https://cursos.alura.com.br/course/arquitetura-computadores-funcionamento-programa
- Atividade Prática na Plataforma Alura
- Na plataforma Alura vamos acessar o seguinte curso:
- A recomendação é que você continue esse curso extraclasse, pois ele traz um conteúdo essencial para compreender sobre o referido tema.

_5 imagem(ns) no slide._

### Slide 20

- DESENVOLVIMENTO DE SISTEMAS
- Hora de praticar!
- Divida os participantes em grupos de 3 a 4 pessoas.
- Distribua cartões ou papéis com instruções simples escritas em linguagem de alto nível (por exemplo, "Some 5 + 3") e em linguagem de máquina (por exemplo, "0101 0011 1000").
- Explique que os cartões representam instruções em duas linguagens diferentes: linguagem de alto nível e linguagem de máquina.
- Desafie cada grupo a "traduzir" as instruções de linguagem de alto nível para linguagem de máquina e vice-versa. Para facilitar, você pode fornecer um "dicionário" simples que relacione operações matemáticas básicas a sequências binárias simplificadas.

_3 imagem(ns) no slide._

### Slide 21

- DESENVOLVIMENTO DE SISTEMAS
- Hora de praticar!
- Estabeleça um tempo limite para a atividade e peça aos grupos que compartilhem suas traduções.
- Ao final da atividade, discuta as dificuldades e facilidades encontradas pelos participantes ao traduzir as instruções e faça a conexão com os conceitos de linguagem de máquina, linguagem de alto nível e tradutores de código, como compiladores e interpretadores.

_3 imagem(ns) no slide._

### Slide 22

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje
- Compreendemos o que é linguagem de máquina e suas particularidades.

_4 imagem(ns) no slide._

### Slide 23

- DESENVOLVIMENTO DE SISTEMAS
- Vamos Praticar?
- Vamos agora colocar em prática o que aprendemos desenvolvendo a atividade sugerida.

_4 imagem(ns) no slide._

### Slide 24

- DESENVOLVIMENTO DE SISTEMAS
- Pronto para desbloquear sua carreira de TI?
- Está perdido estudando mas não sabe por onde começar? Se a resposta é sim, você está no lugar certo! Descubra as estratégias e ferramentas essenciais para te ajudar a desbloquear seu potencial em TI e buscar sua primeira vaga de emprego no setor!
- Este e-book é um guia completo para quem busca começar pelos melhores caminhos para se tornar um excelente profissional de TI, ensinando a identificar perfis profissionais, aplicar técnicas de estudo eficazes, transformar teoria em prática, e aumentar a visibilidade de seu trabalho no mercado de trabalho. Ideal para novatos e profissionais em transição.
- E o melhor, ele pode ser seu, inteiramente grátis!
- Basta clicar AQUI e realizar o seu cadastro com o seu @escola!

_6 imagem(ns) no slide._

### Slide 25

- DESENVOLVIMENTO DE SISTEMAS
- Referências
- Bibliografia
- ALEXANDER, Michael; KUSLEIKA, Richard. A Bíblia do Microsoft Excel 2016. São Paulo: Alta Books,2016.
- CASTRO, Lino Henrique Silva. Ferramentas de Produtividade para Escritório: Utilizando o LibreOffice, o Google Docs e o Microsoft Office. Rio de Janeiro: Alta Books, 2020.
- CORMEN, Thomas H.; LEISERSON, Charles E.; RIVEST, Ronald L.; STEIN, Clifford. Introdução à Ciência da Computação. 3. ed. Rio de Janeiro: Elsevier, 2012.
- FORTUNATO, Daniel Medeiros. Google Drive: Guia Prático para Utilização em Projetos Colaborativos. São Paulo: Novatec, 2019.
- KUROSE, James F.; ROSS, Keith W. Redes de Computadores e a Internet: Uma Abordagem TopDown. 7. ed. São Paulo: Pearson, 2017.
- MARCOTTE, Ethan. Web Design Responsivo: Páginas adaptáveis para todos os dispositivos. São Paulo: Bookman, 2014.
- TANENBAUM, Andrew S.; BOS, Herbert. Sistemas Operacionais Modernos. 4. ed. São Paulo: Pearson, 2015.
- TANENBAUM, Andrew S.; WOODHULL, Albert S. Sistemas Operacionais: Projeto e Implementação. 3 ed. São Paulo: Pearson, 2008.
- TANENBAUM, Andrew S. Redes de Computadores: Das LANs, MANs e WANs às Redes ATM. 4. ed. São Paulo: Pearson, 2003.
- TIDWELL, Jenifer. Design de Interfaces: Fundamentos e Técnicas. 2. ed. São Paulo: Bookman, 2011.
- Figuras e Imagens:
- https://www.flaticon.com/br
- https://www.istockphoto.com/br
- https://raw.githubusercontent.com/zbtang/React-Native-ViewPager/HEAD/imgs/dotIndicator.gif
- https://storyset.com

_2 imagem(ns) no slide._

### Slide 26

- DESENVOLVIMENTO DE SISTEMAS
- O RCO+Aulas é um projeto da Secretaria de Estado da Educação do Paraná e está em constante revisão. Todos os slides são de uso exclusivo dos professores da Rede Pública de Ensino, com a finalidade específica de aplicação em sala de aula, sendo totalmente vedada a publicização, reutilização, reprodução total ou parcial para quaisquer outros fins.

_4 imagem(ns) no slide._

## Atividade

_Fonte: AULA 25_INTRODUÇÃO A COMPUTAÇÃO ATIVIDADE.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

INTRODUÇÃO A COMPUTAÇÃO

1ª SÉRIE

ATIVIDADE AULA 25

Questão 1

O que é a linguagem de máquina?

a) Uma linguagem de programação de alto nível, como Python ou Java.

b) Um conjunto de instruções binárias específicas para cada tipo de processador.

c) Uma linguagem natural, como inglês ou espanhol, usada para escrever programas de computador.

d) Um sistema de notação matemática usado para descrever algoritmos.

Resposta correta: b) Um conjunto de instruções binárias específicas para cada tipo de processador.

Comentário: A linguagem de máquina é um conjunto de instruções binárias (sequências de 0s e 1s) compreensíveis apenas pelo processador de um computador. Cada instrução corresponde a uma operação específica, como adição, subtração ou movimentação de dados. A linguagem de máquina é a forma mais básica e primitiva de comunicação entre um computador e seu processador.

Questão 2

Por que os programadores geralmente não escrevem diretamente em linguagem de máquina?

a) Porque a linguagem de máquina é fácil de entender e não oferece desafios.

b) Porque a linguagem de máquina é composta apenas por zeros.

c) Porque a linguagem de máquina é difícil de entender e manipular diretamente pelos seres humanos.

d) Porque a linguagem de máquina é obsoleta e não é mais usada.

Resposta correta: c) Porque a linguagem de máquina é difícil de entender e manipular diretamente pelos seres humanos.

Comentário: A linguagem de máquina, composta por instruções binárias, é difícil de ser entendida e manipulada diretamente pelos seres humanos. Por isso, os programadores geralmente escrevem código em linguagens de programação de alto nível, como Python, Java e C++, que são mais compreensíveis e acessíveis. Essas linguagens de alto nível são convertidas em linguagem de máquina por meio de tradutores de código, como compiladores e interpretadores, permitindo que os computadores executem os programas.

## Prática

_Fonte: AULA 25_PRÁTICA INTRODUÇÃO A COMPUTAÇÃO.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

INTRODUÇÃO A COMPUTAÇÃO

1ª SÉRIE

AULA PRÁTICA 25

Resumo Explicativo:

Quando programamos, usamos linguagens de alto nível como JavaScript, Python ou C, mas o computador só entende linguagem de máquina — formada por sequências binárias (0 e 1). Para "compreender" o que escrevemos, o código precisa passar por um processo de interpretação ou compilação, sendo transformado em instruções que o processador pode executar. Esta etapa envolve conceitos como compiladores, interpretadores, linguagens de programação, código fonte e código de máquina. Entender esse fluxo é essencial para quem deseja desenvolver sistemas eficientes e compatíveis com o hardware.

Estudo de Caso:

Cenário:

Na aula de Introdução ao Desenvolvimento de Sistemas, a professora propõe que os alunos descubram o que acontece “por trás dos bastidores” quando clicamos em Executar em um código no Visual Studio Code.

Lucas, um aluno curioso, escreveu um programa simples em Python para exibir uma mensagem de boas-vindas. Ele ficou intrigado:

“Como o computador consegue transformar essa frase que escrevi em algo que aparece na tela?”

A professora então explicou que existe um interpretador, que lê o código linha por linha e o transforma em comandos que a máquina entende. E que, em outras linguagens, como C++, o código precisa ser compilado, ou seja, convertido todo de uma vez antes de ser executado.

O desafio lançado à turma foi:

- Descobrir a diferença entre linguagens compiladas e interpretadas.
- Rastrear o caminho do código fonte até o momento em que o computador executa a ação.
- Criar uma explicação visual ou uma simulação que represente esse processo.
Questões:

- Quais são os dois principais tipos de tradução de código usados pelo computador para entender linguagens de programação?
- Explique a diferença entre um interpretador e um compilador, usando exemplos de linguagens conhecidas.
- Imagine que você escreveu um programa em Python e clicou em “Executar”. Descreva, em etapas, o que o interpretador faz para mostrar o resultado na tela.
- Analise o processo de leitura de código em linguagens compiladas e interpretadas. Quais etapas são iguais e quais são diferentes entre os dois métodos?
- Você acha que é melhor aprender uma linguagem interpretada ou compilada primeiro? Justifique sua escolha com base em desempenho e aprendizado.
- Crie um infográfico ou fluxograma que ilustre o processo de leitura de código pelo computador, desde o código fonte até a execução, destacando os papéis do compilador ou interpretador.
