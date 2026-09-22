---
titulo: "Jogando com Bits: De binários à decimais"
tipo: rco-seed
disciplina: introducao-a-computacao
sigla_rco: IAC
trimestre: 1
ordem_rco: 13
serie: 1
aula_rco: "Aula 13"
slides: 17
tem_atividade: true
tem_pratica: true
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/IAC/1TRI/13-jogando-com-bits-de-binarios-a-decimais/13-jogando-com-bits-de-binarios-a-decimais.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/IAC/1TRI/13-jogando-com-bits-de-binarios-a-decimais/AULA 13_INTRODUÇÃO A COMPUTAÇÃO ATIVIDADE.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/IAC/1TRI/13-jogando-com-bits-de-binarios-a-decimais/AULA 13_PRÁTICA INTRODUÇÃO A COMPUTAÇÃO.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Jogando com Bits: De binários à decimais

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- INTRODUÇÃO A COMPUTAÇÃO
- 1ª SÉRIE
- Jogando com Bits: De binários à decimais
- Aula 13

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

- DESENVOLVIMENTO DE SISTEMAS
- Nesta aula, vamos:
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store
- Compreender como funciona o cálculo de números binários.

_7 imagem(ns) no slide._

### Slide 5

- Este material foi elaborado a partir da análise do plano de curso e reúne os conhecimentos essenciais para o Técnico em Desenvolvimento de Sistemas. As aulas foram organizadas com foco na clareza conceitual, na construção gradual dos conteúdos e na utilização de metodologias ativas que favorecem a compreensão, a participação e o desenvolvimento de habilidades e competências de forma significativa.
- De acordo com a matriz curricular do Curso Técnico em Desenvolvimento de Sistemas, que traz em sua essência componentes estruturados para a realização de aulas práticas, cada unidade curricular deve contemplar, além da abordagem teórica, uma proposta de atividade prática a ser desenvolvida pelo professor. Essa orientação assegura a coerência entre o planejamento didático e o que está estabelecido na matriz, promovendo experiências formativas alinhadas ao perfil profissional previsto.
- O professor tem total autonomia para adaptar o conteúdo conforme o contexto da turma, ajustando exemplos, aprofundamentos e estratégias didáticas para otimizar a aprendizagem e a conexão com a prática profissional.
- Se houver falta de conexão ou indisponibilidade de internet durante a aula, os materiais abaixo podem ser utilizados como apoio para elaborar recursos complementares, garantindo a continuidade da abordagem teórica prevista.
- ATENÇÃO PROFESSOR!
- Para saber mais: FORTUNATO, Daniel Medeiros. Google Drive: Guia Prático para Utilização em Projetos Colaborativos. São Paulo: Novatec, 2019.

_2 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Vocês já tentaram ver um filme em outro idioma sem legenda? Conseguiram entender algo? Como foi essa experiência?
- Discutam em duplas e socializem as respostas com a turma no final!

_5 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Entendendo o computador!
- OBS: link do vídeo deve ser atualizado caso a apresentação mude de pasta junto com os vídeos.
- https://drive.google.com/file/d/1dBWoY8c0q2wMD7Oxv8b5sup0_fGp3bE0/view?usp=drive_link

_5 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Para responder
- 1- Qual sistema de numeração utilizamos no nosso dia a dia?
- 2- O que se pode concluir sobre os sistemas de numeração?
- Discutam em duplas e socializem as ideias com a turma no final!

_5 imagem(ns) no slide._

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- 1 - O sistema que utilizamos no nosso dia a dia é o sistema decimal.
- 2 - Os sistemas de numeração fazem parte da fundamentação da Ciência e Engenharia da Computação.

_4 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- Conversão de número binário para decimal
- Conversão do número 1 0 1 0 0 1 para decimal:
- Primeiro, deve-se inverter a posição dos números: 1 0 1 0 0 1 => 1 0 0 1 0 1
- Após, multiplicam-se estes valores por 2 elevado à potência do número da posição de cada dígito, iniciando por 0:

_3 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Conversão de número binário para decimal
- 1 x 20 => 1 x 1 = 1
- 0 x 2¹ => 0 x 2 = 0
- 0 x 2² => 0 x 4 = 0
- 1 x 2³ => 1 x 8 = 8
- 0 x 24 => 0 x 16 = 0
- 1 x 25 => 1 x 32 = 32
- Por fim, somam-se os resultados das multiplicações: 1 + 8 + 32 = 41

_3 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- Conversão de número binário para decimal
- Escreva um número de base dois, em um papel. Não se preocupe com o número que será anotado. Ele poderá ser aleatório, contanto que contenha de 5 a 10 dígitos. Depois, coloque seu nome.
- Coloque o papel na urna. Depois de misturados os papéis, pegue um papel e converta o número para o sistema decimal. Após, coloque seu nome na folha.
- Repita este processo, mas agora verifique se o colega fez a conversão correta. Depois, coloque seu nome e entregue ao colega para realizar a correção da conversão.

_6 imagem(ns) no slide._

### Slide 13

- DESENVOLVIMENTO DE SISTEMAS
- O desafio:
- Buscar entender uma problemática aplicando o que foi aprendido na aula de hoje.
- Prontos para criar uma solução?
- Vamos Praticar?

_4 imagem(ns) no slide._

### Slide 14

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje
- Para converter um número binário para decimal, é preciso multiplicar cada dígito pela potência de 2 relativa à posição por ele ocupada e somar os resultados.
- Um sistema de números é uma maneira sistemática de representar números com caracteres simbólicos, e usa um valor-base para agrupar convenientemente números em formato compacto.

_4 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- Pronto para desbloquear sua carreira de TI?
- Está perdido estudando mas não sabe por onde começar? Se a resposta é sim, você está no lugar certo! Descubra as estratégias e ferramentas essenciais para te ajudar a desbloquear seu potencial em TI e buscar sua primeira vaga de emprego no setor!
- Este e-book é um guia completo para quem busca começar pelos melhores caminhos para se tornar um excelente profissional de TI, ensinando a identificar perfis profissionais, aplicar técnicas de estudo eficazes, transformar teoria em prática, e aumentar a visibilidade de seu trabalho no mercado de trabalho. Ideal para novatos e profissionais em transição.
- E o melhor, ele pode ser seu, inteiramente grátis!
- Basta clicar AQUI e realizar o seu cadastro com o seu @escola!

_6 imagem(ns) no slide._

### Slide 16

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

_3 imagem(ns) no slide._

### Slide 17

- DESENVOLVIMENTO DE SISTEMAS
- O RCO+Aulas é um projeto da Secretaria de Estado da Educação do Paraná e está em constante revisão. Todos os slides são de uso exclusivo dos professores da Rede Pública de Ensino, com a finalidade específica de aplicação em sala de aula, sendo totalmente vedada a publicização, reutilização, reprodução total ou parcial para quaisquer outros fins.

_4 imagem(ns) no slide._

## Atividade

_Fonte: AULA 13_INTRODUÇÃO A COMPUTAÇÃO ATIVIDADE.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

INTRODUÇÃO A COMPUTAÇÃO

1ª SÉRIE

ATIVIDADE AULA 13

Questão 1

Um administrador de sistemas, ao analisar o conteúdo de um arquivo binário, percebeu que o primeiro byte desse arquivo é um número igual a 10, que corresponde, em decimal, ao valor:

a) 1.

b) 7.

c) 3.

d) 2.

Resposta comentada: Para a solução dessa questão, é necessário realizar a conversão do número no sistema numérico de base 2 para base 10:

Primeiro, deve-se inverter a posição dos números: 1 0 => 0 1

Após, multiplica-se estes valores por 2 elevado à potência do número da posição de cada dígito, iniciando por 0:

0 x 20 => 1 x 0 = 0

1 x 2¹ => 1 x 2 = 2

O resultado da conversão demonstra que o valor em representação por meio do sistema numérico decimal é 2. Assim, a alternativa correta é a d).

O valor no sistema binário dos números apresentados nas alternativas (incorretas a, b e c) são, respectivamente: 1, 1 1 1 e 1 1.

Questão 2

O sistema binário representa a base para o funcionamento dos computadores. Assim, um hodômetro binário (instrumento que indica distâncias percorridas por pedestres ou por veículos), mostra no display o número 1 0 1 0 0 1 1 0. A representação desse número em decimal e o próximo número binário mostrado no display serão, respectivamente:

a) 166, 1 0 1 0 0 1 1 1.

b) 31, 1 1 0 0 1 0.

c) 202, 1 1 0 0 1 0 0 1.

d) 180, 1 0 0 1 1 0 0.

Resposta comentada: Primeiro, deve-se inverter a posição dos números: 1 0 1 0 0 1 1 0 => 0 1 1 0 0 1 0 1.

Após, multiplicam-se estes valores por 2 elevado à potência do número da posição de cada dígito, iniciando por 0:

0 x 20 => 0 x 1 = 0

1 x 2¹ => 1 x 2 = 2

1 x 2² => 1 x 4 = 4

0 x 2³ => 0 x 8 = 0

0 x 24 => 0 x 16 = 0

1 x 25 => 1 x 32 = 32

0 x 26 => 0 x 64 = 0

1 x 27 => 1 x 128 = 128

Por fim, soma-se os resultados das multiplicações: 2 + 4 + 32 + 128 = 166.

Para descobrir qual o próximo número (167) representado no sistema binário, basta somar mais 1 ao número apresentado no enunciado: 1 0 1 0 0 1 1 0 + 1 = 1 0 1 0 0 1 1 1. Assim, a alternativa correta é a letra a).

As conversões dos números representados no sistema decimal para sistema binário e vice-versa nas alternativas (incorretas b, c e d) são, respectivamente: 1 1 1 1 1, 50; 1 1 0 0 1 0 1 0, 201; 1 0 1 1 0 1 0 0, 76.

## Prática

_Fonte: AULA 13_PRÁTICA INTRODUÇÃO A COMPUTAÇÃO.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

INTRODUÇÃO A COMPUTAÇÃO

1ª SÉRIE

AULA PRÁTICA 13

Resumo Explicativo:

Os computadores utilizam o sistema binário, que é composto apenas pelos dígitos 0 e 1, para armazenar e processar informações. No entanto, nós, humanos, utilizamos o sistema decimal no dia a dia. Para que possamos entender e manipular os dados computacionais, é essencial saber converter números binários para decimais.

A conversão de binário para decimal ocorre multiplicando cada bit pelo valor de sua posição na base 2 e somando os resultados. Esse processo é fundamental para diversas áreas da tecnologia da informação, como redes de computadores, programação e desenvolvimento de sistemas embarcados.

Estudo de Caso:

Cenário: Uma empresa de desenvolvimento de jogos digitais chamada BitPlay está criando um novo jogo educativo chamado "Jogando com Bits". O jogo tem como objetivo ensinar conceitos básicos de computação, como conversão de números binários para decimais, de maneira interativa para estudantes do ensino médio.

Os desenvolvedores do jogo enfrentam um desafio: muitos estudantes acham difícil entender a lógica da conversão entre sistemas numéricos e se confundem ao realizar os cálculos. Para resolver esse problema, a equipe precisa projetar uma mecânica de jogo intuitiva, onde os jogadores convertam números binários em decimais para avançar de fase e desbloquear novos desafios.

A equipe de design do jogo precisa definir:

- Como tornar a conversão binária para decimal divertida e desafiadora?
- Quais mecanismos podem ser usados para reforçar o aprendizado de forma prática?
- Como garantir que os jogadores compreendam o conceito sem precisar de explicações teóricas extensas?
O objetivo do jogo é ajudar os alunos a desenvolverem fluência na conversão de números binários para decimais de forma lúdica e envolvente.

Questões

- Liste os passos para converter um número binário para decimal manualmente.
- Explique, com suas palavras, por que os computadores utilizam o sistema binário e como a conversão para decimal é aplicada no desenvolvimento de sistemas.
- Converta o número binário 10110 para decimal e explique o processo passo a passo.
- Analise como a posição de cada bit em um número binário influencia seu valor decimal correspondente. O que acontece se um bit de maior ordem for alterado?
- Avalie a eficácia de ensinar conversão binária para decimal através de um jogo educativo em comparação com um método tradicional, como explicações em sala de aula. Quais são as vantagens e desafios de cada abordagem?
- Proponha um conceito para uma nova fase do jogo "Jogando com Bits" que torne a conversão binária para decimal mais envolvente. Descreva a mecânica e os desafios da fase.
