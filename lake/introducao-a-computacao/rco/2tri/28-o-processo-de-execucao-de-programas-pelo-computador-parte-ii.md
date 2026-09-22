---
titulo: "Parte II"
tipo: rco-seed
disciplina: introducao-a-computacao
sigla_rco: IAC
trimestre: 2
ordem_rco: 28
serie: 1
aula_rco: "Aula 28"
slides: 26
tem_atividade: true
tem_pratica: true
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/IAC/2TRI/28-o-processo-de-execucao-de-programas-pelo-computador-parte-ii/28-o-processo-de-execucao-de-programas-pelo-computador-parte-ii.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/IAC/2TRI/28-o-processo-de-execucao-de-programas-pelo-computador-parte-ii/AULA 28_INTRODUÇÃO A COMPUTAÇÃO ATIVIDADE.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/IAC/2TRI/28-o-processo-de-execucao-de-programas-pelo-computador-parte-ii/AULA 28_PRÁTICA INTRODUÇÃO A COMPUTAÇÃO.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Parte II

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- INTRODUÇÃO A COMPUTAÇÃO
- 1ª SÉRIE
- O Processo de Execução de Programas pelo Computador
- Parte II
- Aula 28

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
- Aprender sobre o processo de Execução de Programas pelo Computador - Parte II

_7 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Na aula anterior...
- Compreendemos com o computador faz a leitura de códigos e entendemos a diferença entre interpretadores e compiladores.

_4 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Ana é uma estudante do ensino médio que está começando a aprender sobre computadores. Ela sabe que o processador é uma parte vital do computador, muitas vezes referido como o "cérebro" do sistema, mas ela não entende completamente como ele funciona. Ana sabe que o processador executa as instruções do programa, mas ela se pergunta como o processador sabe o que fazer e em que ordem fazer.

_4 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Como o processador de um computador sabe quais instruções executar e em que ordem?
- Conversem e apresentem suas visões

_5 imagem(ns) no slide._

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- O processador executa instruções que são armazenadas na memória do computador como parte de um programa. Cada instrução é uma tarefa específica que o processador deve realizar, como adicionar dois números ou mover dados de um local para outro. O processador sabe em que ordem executar as instruções porque cada programa tem um contador de programa, que mantém a localização da próxima instrução a ser executada.

_4 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- Após a execução de uma instrução, o contador de programa é atualizado para apontar para a próxima instrução. Isso permite que o processador execute as instruções em uma sequência específica, o que é essencial para a execução correta do programa.
- Resposta

_4 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- O processador, também conhecido como Unidade Central de Processamento (CPU), é muitas vezes comparado ao cérebro do computador. É o componente que executa a maioria das instruções dentro do computador, interpretando e realizando as operações básicas que fazem um sistema operar, como operações aritméticas, lógicas, de controle e de entrada/saída.

_4 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- O funcionamento da CPU é baseado em um ciclo de instrução, que consiste em buscar uma instrução memória, decodificá-la para entender o que deve ser feito, executar a operação necessária e, finalmente, armazenar o resultado. Este ciclo é repetido continuamente enquanto o computador está ligado.

_4 imagem(ns) no slide._

### Slide 13

- DESENVOLVIMENTO DE SISTEMAS
- No desenvolvimento de software, o processador desempenha um papel crucial. Os programas de software são, na verdade, uma série de instruções que a CPU precisa executar. A eficiência do processador - incluindo a velocidade do relógio, o número de núcleos (unidades de processamento) e a capacidade de realizar vários processos simultaneamente (multitarefa) - pode ter um grande impacto no quão rápido e eficiente um programa de software pode ser executado.

_4 imagem(ns) no slide._

### Slide 14

- DESENVOLVIMENTO DE SISTEMAS
- Por fim, entender o funcionamento do processador pode ajudar os desenvolvedores a otimizar o software. Por exemplo, se um desenvolvedor sabe que um determinado processador é bom para executar múltiplas tarefas ao mesmo tempo, eles podem projetar seu software para tirar proveito disso. Da mesma forma, um desenvolvedor pode escrever software que executa operações de maneira mais eficiente com base no conhecimento de como a CPU decodifica e executa instruções.

_4 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- Para responder
- Discutam em duplas e socializem as ideias com a turma no final!
- Como a eficiência do processador pode impactar o desempenho de um programa de software?

_5 imagem(ns) no slide._

### Slide 16

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- A eficiência do processador - que inclui fatores como a velocidade do relógio, o número de núcleos e a capacidade de multitarefa - pode ter um impacto significativo no desempenho de um programa de software. Um processador mais eficiente pode executar as instruções do programa mais rapidamente, resultando em um software que funciona de maneira mais suave e rápida.

_4 imagem(ns) no slide._

### Slide 17

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Por outro lado, um processador menos eficiente pode levar a tempos de carregamento mais longos e um desempenho mais lento do software. Além disso, um processador que é capaz de multitarefa eficiente pode permitir que vários processos ou threads de um programa sejam executados simultaneamente, melhorando o desempenho geral do software.

_4 imagem(ns) no slide._

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- Link para o curso: https://cursos.alura.com.br/course/arquitetura-computadores-funcionamento-programa
- Atividade Prática na Plataforma Alura
- Na plataforma Alura vamos acessar o seguinte curso:
- A recomendação é que você continue esse curso extraclasse, pois ele traz um conteúdo essencial para compreender sobre o referido tema.

_5 imagem(ns) no slide._

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- Hora de praticar!
- Divida os participantes em grupos de 3 pessoas, sendo cada grupo uma "CPU". Dentro de cada grupo, atribua funções específicas: uma pessoa será o "Buscador de Instruções", outra será o "Decodificador" e a terceira será o "Executor".
- Espalhe os cartões coloridos (instruções) em uma área do ambiente (memória).
- Ao iniciar o cronômetro, o "Buscador de Instruções" deve ir até a área de memória, pegar um cartão (instrução) e levá-lo para a mesa (processador).

_4 imagem(ns) no slide._

### Slide 20

- DESENVOLVIMENTO DE SISTEMAS
- Hora de praticar!
- O "Decodificador" deve então olhar para a cor do cartão e dizer ao "Executor" qual ação realizar (por exemplo, vermelho pode ser "pular", azul pode ser "bater palmas", etc.).
- O "Executor" realiza a ação e, em seguida, o "Buscador de Instruções" pode buscar a próxima instrução. Este ciclo se repete durante um tempo determinado.

_4 imagem(ns) no slide._

### Slide 21

- DESENVOLVIMENTO DE SISTEMAS
- Hora de praticar!
- Depois de completar a atividade, discuta como a dinâmica representa o funcionamento de um processador de computador. Ressalte a importância de cada componente (Buscador, Decodificador e Executor) e como a velocidade e eficiência de cada um pode afetar o desempenho geral do sistema. Este é um bom momento para discutir conceitos como velocidade de clock, paralelismo e multitarefa.

_4 imagem(ns) no slide._

### Slide 22

- DESENVOLVIMENTO DE SISTEMAS
- Vamos Praticar?
- Vamos agora colocar em prática o que aprendemos desenvolvendo a atividade sugerida.

_4 imagem(ns) no slide._

### Slide 23

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje
- Compreendemos sobre o funcionamento do processador e como ele impacta no desenvolvimento de aplicações.

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

_Fonte: AULA 28_INTRODUÇÃO A COMPUTAÇÃO ATIVIDADE.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

INTRODUÇÃO A COMPUTAÇÃO

1ª SÉRIE

ATIVIDADE AULA 27

Questão 1

O que a velocidade do clock de um processador determina?

a) A quantidade de armazenamento no disco rígido

b) A quantidade de memória RAM que o processador pode usar

c) A quantidade de energia que o processador consome

d) O número de instruções que o processador pode executar por segundo

Resposta correta: d) O número de instruções que o processador pode executar por segundo. A velocidade do clock de um processador determina quantas instruções ele pode executar em um segundo. Portanto, um processador com uma velocidade de clock mais alta pode executar mais instruções por segundo do que um com uma velocidade de clock mais baixa.

Questão 2

O que significa dizer que um processador é "dual-core"?

a) O processador tem dois componentes principais: a Unidade de Controle e a Unidade Aritmética e Lógica.

b) O processador pode executar duas instruções simultaneamente.

c) O processador pode armazenar o dobro da quantidade de dados que um processador de um único núcleo.

d) O processador consome o dobro de energia que um processador de um único núcleo.

Resposta correta: b) O processador pode executar duas instruções simultaneamente. Um processador "dual-core" tem dois núcleos de processamento independentes, o que significa que ele pode executar duas instruções ao mesmo tempo, aumentando o desempenho geral.

## Prática

_Fonte: AULA 28_PRÁTICA INTRODUÇÃO A COMPUTAÇÃO.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

INTRODUÇÃO A COMPUTAÇÃO

1ª SÉRIE

AULA PRÁTICA 28

Resumo Explicativo:

Na segunda parte do estudo sobre o processo de execução de programas, aprofundamos a compreensão de como a arquitetura interna do processador, a gestão de memória, e o papel dos registradores, cache e barramentos impactam a execução de programas. Também abordamos a diferença entre a execução sequencial e a execução paralela, além de conceitos como pipeline, que permite que múltiplas instruções sejam processadas simultaneamente, aumentando o desempenho dos sistemas.

Compreender esses conceitos é fundamental para qualquer desenvolvedor, pois influencia diretamente na otimização de software, na eficiência dos algoritmos e no entendimento dos limites físicos do hardware.

Estudo de Caso:

Cenário:

Carlos, aluno de desenvolvimento de sistemas, percebeu que dois programas executando a mesma tarefa (processamento de imagens) tinham tempos de execução muito diferentes em computadores aparentemente semelhantes.

Ao investigar, descobriu que:

- O primeiro computador tinha uma CPU com mais núcleos e suporte a execução paralela.
- O segundo tinha uma arquitetura mais antiga, com menor cache e sem pipeline eficiente.
Carlos passou a entender que não basta analisar apenas a quantidade de memória ou o clock da CPU, mas também como o processador gerencia as instruções, como usa cache, registradores e se utiliza técnicas de paralelismo para acelerar as tarefas.

O professor então propôs um desafio:

- Que Carlos e seus colegas criassem um mapa visual do caminho que uma instrução percorre dentro do processador, desde a busca na memória até a execução, destacando o papel dos barramentos, cache, registradores e pipeline.
Questões

- Liste três componentes internos fundamentais no processo de execução de um programa dentro da CPU.
- Explique, com suas palavras, como o pipeline melhora o desempenho da execução de programas.
- Se um programa demora muito para ser executado e você percebe que ele realiza muitas leituras e escritas na memória, qual solução prática você poderia propor para melhorar o desempenho?
- Analise como os registradores, a memória cache e os barramentos trabalham juntos durante a execução de uma instrução. Quais são as relações de dependência entre eles?
- Você acha que sempre adicionar mais núcleos ao processador garante que o programa execute mais rápido? Justifique sua resposta considerando limitações de software e hardware.
- Crie um fluxograma ou um infográfico que represente o caminho completo de uma instrução, desde que é buscada na memória até sua execução, destacando os componentes envolvidos e suas funções (cache, registradores, barramentos, unidade de controle, etc).
