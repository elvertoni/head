---
titulo: "Execução Simultânea de Programas pelo Computador - Parte I"
tipo: rco-seed
disciplina: introducao-a-computacao
sigla_rco: IAC
trimestre: 2
ordem_rco: 29
serie: 1
aula_rco: "Aula 29"
slides: 26
tem_atividade: true
tem_pratica: true
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/IAC/2TRI/29-execucao-simultanea-de-programas-pelo-computador-parte-i/29-execucao-simultanea-de-programas-pelo-computador-parte-i.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/IAC/2TRI/29-execucao-simultanea-de-programas-pelo-computador-parte-i/AULA 29_PRÁTICA INTRODUÇÃO A COMPUTAÇÃO.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/IAC/2TRI/29-execucao-simultanea-de-programas-pelo-computador-parte-i/AULA 29_INTRODUÇÃO A COMPUTAÇÃO ATIVIDADE.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Execução Simultânea de Programas pelo Computador - Parte I

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- INTRODUÇÃO A COMPUTAÇÃO
- 1ª SÉRIE
- Execução Simultânea de Programas pelo Computador - Parte I
- Aula 29

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
- Entender como o computador executa vários programas ao mesmo tempo Parte I.

_7 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Na aula anterior...
- Compreendemos como o computador executa um programa, sua alocação, entre memórias primárias e secundárias.

_4 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Ana, uma estudante de informática que está começando a se familiarizar com os conceitos de hardware de computadores. Enquanto Ana está aprendendo sobre os processadores, ela se depara com a questão de como o computador é capaz de executar vários programas ao mesmo tempo. Ela entende que um processador de um único núcleo só pode executar um processo de cada vez. No entanto, ela usa vários aplicativos ao mesmo tempo em seu computador, então como isso é possível?

_3 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Se um processador de um único núcleo só pode executar um processo de cada vez, como eu consigo usar vários aplicativos ao mesmo tempo no meu computador?
- Conversem e apresentem suas visões

_5 imagem(ns) no slide._

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- A habilidade do seu computador em executar vários aplicativos simultaneamente é uma combinação de várias técnicas. Primeiro, mesmo em processadores de um único núcleo, o sistema operacional é capaz de alternar rapidamente entre diferentes processos, dando a impressão de que todos estão sendo executados ao mesmo tempo, um processo chamado de multitarefa.

_4 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- A execução de vários programas em um computador é um processo que envolve o gerenciamento eficiente de recursos do sistema, e os processadores modernos desempenham um papel fundamental nesse processo.

_4 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Primeiramente, é importante entender que cada programa que você executa no computador é chamado de "processo". Cada processo tem o seu próprio espaço na memória e utiliza uma parte do tempo do processador para executar suas tarefas. Em um dado momento, pode parecer que vários processos estão sendo executados simultaneamente, mas na verdade, para um processador de um único núcleo, apenas um processo é executado de cada vez.

_4 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- Os processadores modernos, no entanto, são frequentemente multi-core, o que significa que eles têm vários núcleos de processamento independentes. Isso permite que eles executem vários processos verdadeiramente ao mesmo tempo, um em cada núcleo. Além disso, a tecnologia de multithreading permite que cada núcleo alterne rapidamente entre diferentes processos, dando a impressão de paralelismo mesmo em núcleos individuais.

_4 imagem(ns) no slide._

### Slide 13

- DESENVOLVIMENTO DE SISTEMAS
- O sistema operacional do computador gerencia todos esses processos, decidindo quando e por quanto tempo cada processo pode usar o processador. Ele faz isso através de um processo chamado "agendamento", que decide qual processo deve ser executado a seguir. O objetivo do agendamento é garantir que todos os processos tenham uma parcela justa do tempo do processador e que o sistema seja responsivo e eficiente.

_4 imagem(ns) no slide._

### Slide 14

- DESENVOLVIMENTO DE SISTEMAS
- Para responder
- Discutam em duplas e socializem as ideias com a turma no final!
- O que é a tecnologia de multithreading em processadores modernos e como ela contribui para a execução de vários programas em um computador?

_5 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- A tecnologia de multithreading é uma técnica em que um núcleo de um processador pode executar várias "threads" (subtarefas de um processo) de maneira alternada e extremamente rápida, dando a impressão de que essas threads estão sendo executadas simultaneamente. Isso é possível graças a recursos como a divisão do tempo de execução e a alternância rápida entre threads.

_3 imagem(ns) no slide._

### Slide 16

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Essa tecnologia contribui para a execução eficiente de vários programas, pois permite que cada núcleo do processador seja utilizado de maneira mais eficaz, melhorando a utilização dos recursos do sistema e a resposta do computador.

_4 imagem(ns) no slide._

### Slide 17

- DESENVOLVIMENTO DE SISTEMAS
- Link para o curso: https://cursos.alura.com.br/course/arquitetura-computadores-funcionamento-programa
- Atividade Prática na Plataforma Alura
- Na plataforma Alura vamos acessar o seguinte curso:
- A recomendação é que você continue esse curso extraclasse, pois ele traz um conteúdo essencial para compreender sobre o referido tema.

_5 imagem(ns) no slide._

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- Hora de praticar!
- enquanto os outros serão os "Programas". Se possível, divida os "Programas" em grupos menores para representar os diferentes núcleos de um processador multi-core.
- Cada "Programa" terá uma tarefa ou atividade específica para realizar, como resolver um quebra-cabeça, fazer um desenho, escrever um texto, etc.

_4 imagem(ns) no slide._

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- Hora de praticar!
- O "Processador" terá que gerenciar todos os "Programas", decidindo quando e por quanto tempo cada um pode trabalhar em sua tarefa. O "Processador" pode mudar de "Programa" a qualquer momento, fazendo com que um "Programa" pare de trabalhar em sua tarefa e outro comece.

_4 imagem(ns) no slide._

### Slide 20

- DESENVOLVIMENTO DE SISTEMAS
- Hora de praticar!
- Para adicionar a ideia de multithreading, cada "Programa" pode ter várias tarefas diferentes que precisam ser realizadas, e o "Processador" pode alternar não apenas entre "Programas", mas também entre as diferentes tarefas de um único "Programa".
- A dinâmica continua até que todas as tarefas sejam concluídas. O objetivo é fazer com que os participantes experimentem como um processador gerencia a execução de vários programas e tarefas ao mesmo tempo.

_4 imagem(ns) no slide._

### Slide 21

- DESENVOLVIMENTO DE SISTEMAS
- Hora de praticar!
- Esta dinâmica pode dar uma ideia visual e prática de como um computador gerencia a execução de vários programas, mesmo com um único processador.

_4 imagem(ns) no slide._

### Slide 22

- DESENVOLVIMENTO DE SISTEMAS
- Vamos Praticar?
- Vamos agora colocar em prática o que aprendemos desenvolvendo a atividade sugerida.

_4 imagem(ns) no slide._

### Slide 23

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje
- Aprendemos com o computador pode executar vários programas ao mesmo tempo.

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

_3 imagem(ns) no slide._

### Slide 26

- DESENVOLVIMENTO DE SISTEMAS
- O RCO+Aulas é um projeto da Secretaria de Estado da Educação do Paraná e está em constante revisão. Todos os slides são de uso exclusivo dos professores da Rede Pública de Ensino, com a finalidade específica de aplicação em sala de aula, sendo totalmente vedada a publicização, reutilização, reprodução total ou parcial para quaisquer outros fins.

_4 imagem(ns) no slide._

## Atividade

_Fonte: AULA 29_INTRODUÇÃO A COMPUTAÇÃO ATIVIDADE.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

INTRODUÇÃO A COMPUTAÇÃO

1ª SÉRIE

ATIVIDADE AULA 29

Questão 1

O que é multithreading em um processador?

a) É uma técnica que permite que um único processador execute várias tarefas ao mesmo tempo.

b) É uma técnica que permite que um único programa seja dividido em várias partes menores.

c) É um tipo de processador que só pode executar uma tarefa de cada vez.

d) É uma técnica que permite que um único processador execute apenas um tipo de tarefa.

Resposta correta: a) Multithreading é uma técnica que permite que um único processador execute várias tarefas ao mesmo tempo.

Questão 2

Como o multithreading beneficia a execução de programas em um computador?

a) Permite que um programa seja executado mais rapidamente, dividindo-o em várias partes que podem ser executadas simultaneamente.

b) Permite que vários programas sejam executados simultaneamente, cada um em seu próprio núcleo.

c) Permite que um único programa utilize todos os núcleos de um processador ao mesmo tempo.

d) Todos os itens acima.

Resposta correta: d) Todos os itens acima. O multithreading pode permitir que um programa seja dividido e suas partes sejam executadas simultaneamente, permitir a execução simultânea de vários programas, e permitir que um único programa utilize todos os núcleos de um processador ao mesmo tempo.

## Prática

_Fonte: AULA 29_PRÁTICA INTRODUÇÃO A COMPUTAÇÃO.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

INTRODUÇÃO A COMPUTAÇÃO

1ª SÉRIE

AULA PRÁTICA 29

Resumo Explicativo:

A execução simultânea de programas, também chamada de multitarefa, é um conceito fundamental na arquitetura de sistemas operacionais modernos. O processador, mesmo com poucos núcleos, dá a impressão de executar vários programas ao mesmo tempo, alternando rapidamente entre eles através de uma técnica chamada escalonamento de processos.

Quando há mais de um núcleo ou suporte a multithreading, o computador realmente executa múltiplas instruções em paralelo. Compreender como a CPU gerencia essa execução é essencial para desenvolver softwares eficientes, capazes de utilizar os recursos do hardware de forma otimizada.

Estudo de Caso:

Cenário:

Durante uma aula, o professor propôs aos alunos uma reflexão prática: observar o gerenciador de tarefas do sistema operacional.

Mariana percebeu que, mesmo assistindo a uma aula online, ouvindo música no Spotify, navegando no Google Chrome e editando um texto no Word, todos os programas pareciam funcionar ao mesmo tempo.

Curiosa, ela perguntou:

“Se o computador tem apenas 4 núcleos, como ele faz tantas coisas ao mesmo tempo?”

O professor explicou que o sistema operacional gerencia essa execução por meio do escalonador de processos, que divide o tempo da CPU entre os programas ativos. Ele também mostrou que programas podem ser divididos em threads, unidades menores que também podem ser executadas paralelamente, dependendo da capacidade da CPU.

O desafio proposto foi:

- Que os alunos explicassem como o sistema operacional gerencia a execução de vários programas e como o hardware (núcleos e threads) influencia nesse processo.
Questões

- Liste dois conceitos fundamentais relacionados à execução simultânea de programas pelo computador.
- Explique, com suas palavras, como o sistema operacional consegue fazer com que vários programas pareçam funcionar ao mesmo tempo, mesmo quando o processador tem poucos núcleos.
- Você percebe que seu computador fica mais lento quando abre muitos programas. O que isso tem a ver com o uso da CPU e a execução simultânea? Descreva uma solução prática para melhorar o desempenho.
- Analise como os conceitos de núcleos, threads e escalonamento de processos trabalham juntos para garantir a execução simultânea de tarefas. Como eles se relacionam?
- Você acha que, para um usuário comum, é mais vantajoso investir em um processador com mais núcleos ou mais threads? Justifique sua resposta considerando desempenho e custo.
- Desenvolva um infográfico ou uma apresentação que explique como funciona a execução simultânea de programas, destacando o papel dos núcleos, threads e do sistema operacional no gerenciamento dos processos.
