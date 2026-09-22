---
titulo: "Execução Simultânea de Programas pelo Computador - Parte II"
tipo: rco-seed
disciplina: introducao-a-computacao
sigla_rco: IAC
trimestre: 2
ordem_rco: 30
serie: 1
aula_rco: "Aula 30"
slides: 20
tem_atividade: true
tem_pratica: true
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/IAC/2TRI/30-execucao-simultanea-de-programas-pelo-computador-parte-ii/30-execucao-simultanea-de-programas-pelo-computador-parte-ii.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/IAC/2TRI/30-execucao-simultanea-de-programas-pelo-computador-parte-ii/AULA 30_INTRODUÇÃO A COMPUTAÇÃO ATIVIDADE.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/IAC/2TRI/30-execucao-simultanea-de-programas-pelo-computador-parte-ii/AULA 30_PRÁTICA INTRODUÇÃO A COMPUTAÇÃO.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Execução Simultânea de Programas pelo Computador - Parte II

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- INTRODUÇÃO A COMPUTAÇÃO
- 1ª SÉRIE
- Execução Simultânea de Programas pelo Computador - Parte II
- Aula 30

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
- Entender como o computador executa vários programas ao mesmo tempo Parte II.

_7 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Na aula anterior...
- Iniciamos o aprendizado sobre como o computador pode executar vários programas ao mesmo tempo, entender o papel do processador nesse processo.

_4 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Mateus, estudante do segundo ano, está editando um vídeo, ouvindo música e navegando na internet, tudo ao mesmo tempo.
- "Por que, às vezes, o vídeo fica travando, mas a música continua tocando normalmente?"
- Realizem a atividade em duplas e socializem no final!

_5 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- O sistema operacional faz o escalonamento dos processos, distribuindo os recursos da CPU entre os programas. A reprodução de música exige poucos recursos e é tratada como uma tarefa leve e contínua. Já o software de edição de vídeo demanda muito mais processamento, podendo gerar lentidão se o uso de CPU estiver próximo do limite ou se não houver núcleos suficientes.

_4 imagem(ns) no slide._

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- Execução Simultânea de Programas pelo Computador se aprofunda no funcionamento interno da multitarefa, como o sistema operacional gerencia threads, processos e distribui tarefas pelos núcleos do processador.

_4 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- Processos: Programas em execução.Threads: Subtarefas dentro dos processos, que podem ser executadas em paralelo.
- Escalonamento: Técnica usada pelo sistema operacional para decidir qual processo será executado a cada instante.
- Núcleos: Unidades físicas no processador capazes de executar tarefas.

_4 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Compreender isso permite:
- Otimizar programas.
- Entender gargalos de desempenho.
- Resolver problemas de travamentos e lentidão.
- Desenvolver aplicações mais eficientes.

_4 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- Quando usamos redes sociais, abrimos músicas, jogamos e navegamos ao mesmo tempo, o sistema distribui essas tarefas entre os núcleos do processador, alternando ou executando paralelamente, dependendo da quantidade de núcleos e da configuração das threads.

_4 imagem(ns) no slide._

### Slide 13

- DESENVOLVIMENTO DE SISTEMAS
- Para responder
- Discutam em duplas e socializem as ideias com a turma no final!
- O que é uma thread?
- Um programa instalado no computador.
- Um sub-processo que realiza uma tarefa dentro de um processo.
- Um hardware do computador.
- Um tipo de memória.

_4 imagem(ns) no slide._

### Slide 14

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- O que é uma thread?
- Um programa instalado no computador.
- Um sub-processo que realiza uma tarefa dentro de um processo.
- Um hardware do computador.
- Um tipo de memória.

_3 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- Link para o curso: https://cursos.alura.com.br/course/arquitetura-computadores-funcionamento-programa
- Atividade Prática na Plataforma Alura
- Na plataforma Alura vamos acessar o seguinte curso:
- A recomendação é que você continue esse curso extraclasse, pois ele traz um conteúdo essencial para compreender sobre o referido tema.

_5 imagem(ns) no slide._

### Slide 16

- DESENVOLVIMENTO DE SISTEMAS
- Vamos Praticar?
- Vamos agora colocar em prática o que aprendemos desenvolvendo a atividade sugerida.

_4 imagem(ns) no slide._

### Slide 17

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje
- Aprendemos como funciona a execução simultânea de programas, entendendo conceitos como processos, threads, núcleos e escalonamento. Esse conhecimento é essencial para criar, analisar e otimizar sistemas e programas, além de compreender como o computador distribui tarefas no dia a dia.

_4 imagem(ns) no slide._

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- Pronto para desbloquear sua carreira de TI?
- Está perdido estudando mas não sabe por onde começar? Se a resposta é sim, você está no lugar certo! Descubra as estratégias e ferramentas essenciais para te ajudar a desbloquear seu potencial em TI e buscar sua primeira vaga de emprego no setor!
- Este e-book é um guia completo para quem busca começar pelos melhores caminhos para se tornar um excelente profissional de TI, ensinando a identificar perfis profissionais, aplicar técnicas de estudo eficazes, transformar teoria em prática, e aumentar a visibilidade de seu trabalho no mercado de trabalho. Ideal para novatos e profissionais em transição.
- E o melhor, ele pode ser seu, inteiramente grátis!
- Basta clicar AQUI e realizar o seu cadastro com o seu @escola!

_6 imagem(ns) no slide._

### Slide 19

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

### Slide 20

- DESENVOLVIMENTO DE SISTEMAS
- O RCO+Aulas é um projeto da Secretaria de Estado da Educação do Paraná e está em constante revisão. Todos os slides são de uso exclusivo dos professores da Rede Pública de Ensino, com a finalidade específica de aplicação em sala de aula, sendo totalmente vedada a publicização, reutilização, reprodução total ou parcial para quaisquer outros fins.

_4 imagem(ns) no slide._

## Atividade

_Fonte: AULA 30_INTRODUÇÃO A COMPUTAÇÃO ATIVIDADE.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

INTRODUÇÃO A COMPUTAÇÃO

1ª SÉRIE

ATIVIDADE AULA 30

Questão 1

Qual dos seguintes NÃO é um exemplo de multitarefa em um computador?

a) Ouvir música enquanto navega na internet.

b) Baixar um arquivo enquanto lê um documento.

c) Executar um programa de verificação de vírus enquanto escreve um e-mail.

d) Ligar o computador.

Resposta: d) Ligar o computador. A alternativa D não é um exemplo de multitarefa porque envolve apenas uma ação - ligar o computador. As outras opções são exemplos de multitarefa, pois envolvem realizar mais de uma tarefa ao mesmo tempo.

Questão 2

O que permite que um computador execute várias tarefas simultaneamente?

a) A memória RAM do computador.

b) A capacidade de multitarefa do sistema operacional.

c) A velocidade do processador.

d) Todas as opções acima.

Resposta: d) Todas as opções acima. A memória RAM, a capacidade de multitarefa do sistema operacional e a velocidade do processador são todos fatores que permitem que um computador execute várias tarefas simultaneamente.

## Prática

_Fonte: AULA 30_PRÁTICA INTRODUÇÃO A COMPUTAÇÃO.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

INTRODUÇÃO A COMPUTAÇÃO

1ª SÉRIE

AULA PRÁTICA 30

Resumo Explicativo:

A execução simultânea de programas, também conhecida como multitarefa, é a capacidade que os sistemas operacionais modernos têm de rodar vários processos ao mesmo tempo. Isso é possível graças a conceitos como processos, threads, escalonamento de CPU e gerenciamento de recursos.

Quando você escuta música, navega na internet e edita um documento ao mesmo tempo, seu computador está alternando rapidamente entre esses processos, dando a impressão de que estão sendo executados simultaneamente. A execução paralela se torna ainda mais poderosa em processadores com múltiplos núcleos, onde diferentes tarefas podem realmente ser executadas ao mesmo tempo, não apenas alternadas.

Entender esse conceito é essencial para quem desenvolve sistemas, já que isso influencia diretamente o desempenho, a otimização de programas e o uso eficiente do hardware.

Estudo de Caso:

Cenário:

Lívia é aluna do segundo ano do curso técnico em desenvolvimento de sistemas. Durante a aula, o professor pediu que ela abrisse um navegador, um editor de texto e um reprodutor de música ao mesmo tempo.

Observando o Gerenciador de Tarefas, Lívia percebeu que cada programa consumia uma quantidade diferente de CPU e memória. Ela ficou curiosa:

“Se o computador só executa uma coisa de cada vez, como tudo isso roda junto?”

O professor explicou que o sistema operacional faz o escalonamento dos processos, ou seja, define qual programa usa a CPU em cada fração de segundo. Além disso, o processador moderno da escola tem quatro núcleos, permitindo que até quatro tarefas sejam realmente executadas ao mesmo tempo.

O desafio da turma era entender como funcionam:

- Processos
- Threads
- Escalonamento
- Núcleos de CPU E criar uma apresentação que explicasse como o computador gerencia a execução simultânea de diversos programas.
Questões

- Liste três conceitos fundamentais relacionados à execução simultânea de programas pelo computador.
- Explique, com suas palavras, como o sistema operacional consegue executar vários programas aparentemente ao mesmo tempo, mesmo que o processador execute uma tarefa por vez em cada núcleo.
- Imagine que seu computador está lento ao rodar vários programas. Cite duas ações que você pode fazer, usando o Gerenciador de Tarefas, para melhorar a performance.
- Analise como os conceitos de processos, threads e núcleos de CPU se relacionam entre si no funcionamento de programas multitarefa.
- Você acha que ter mais núcleos na CPU resolve todos os problemas de lentidão em multitarefa? Justifique considerando limitações de hardware e software.
- Desenvolva um infográfico que mostre como o sistema operacional gerencia três programas abertos simultaneamente, ilustrando o papel do escalonamento, dos processos e dos núcleos da CPU.
