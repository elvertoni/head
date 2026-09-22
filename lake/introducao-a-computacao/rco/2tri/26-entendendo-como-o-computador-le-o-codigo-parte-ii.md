---
titulo: "Entendendo como o computador lê o código - Parte II"
tipo: rco-seed
disciplina: introducao-a-computacao
sigla_rco: IAC
trimestre: 2
ordem_rco: 26
serie: 1
aula_rco: "Aula 26"
slides: 22
tem_atividade: true
tem_pratica: true
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/IAC/2TRI/26-entendendo-como-o-computador-le-o-codigo-parte-ii/26-entendendo-como-o-computador-le-o-codigo-parte-ii.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/IAC/2TRI/26-entendendo-como-o-computador-le-o-codigo-parte-ii/AULA 26_INTRODUÇÃO A COMPUTAÇÃO ATIVIDADE.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/IAC/2TRI/26-entendendo-como-o-computador-le-o-codigo-parte-ii/AULA 26_PRÁTICA INTRODUÇÃO A COMPUTAÇÃO.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Entendendo como o computador lê o código - Parte II

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- INTRODUÇÃO A COMPUTAÇÃO
- 1ª SÉRIE
- Entendendo como o computador lê o código - Parte II
- Aula 26

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
- Entendendo como o computador lê o código - Parte II

_7 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Na aula anterior...
- Iniciamos os estudos para entender como o computador entende o código que é desenvolvido.

_4 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- João está estudando sobre compiladores e interpretadores e começa a refletir sobre as diferenças entre os dois e como eles se aplicam a diferentes linguagens de programação. Ele se pergunta:
- Se ambos os compiladores e interpretadores convertem código de alto nível para linguagem de máquina, por que escolher um em vez do outro?

_4 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Qual é a principal diferença entre compiladores e interpretadores e por que alguém escolheria um em vez do outro?
- Registre a sua resposta e compartilhe!

_5 imagem(ns) no slide._

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- A principal diferença entre compiladores e interpretadores está no momento em que o código de alto nível é convertido em linguagem de máquina e como isso afeta a execução do programa.
- Compiladores traduzem todo o código-fonte em linguagem de máquina antes da execução, gerando um arquivo executável.

_4 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- Tradutores de código são programas que convertem o código escrito em linguagens de programação de alto nível, como Python, Java e C++, em linguagem de máquina, que é a linguagem compreendida pelos processadores dos computadores.
- Esses tradutores são essenciais porque facilitam a comunicação entre os seres humanos e os computadores, permitindo que os programadores escrevam código de maneira mais compreensível e fácil de entender.

_4 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Existem dois tipos principais de tradutores de código:
- compiladores e interpretadores
- Compiladores são programas que traduzem todo o código-fonte de uma linguagem de alto nível para linguagem de máquina antes da execução, gerando um arquivo executável. Isso permite que o programa seja executado com um desempenho mais rápido, pois a tradução ocorre apenas uma vez e o arquivo executável pode ser usado várias vezes.

_4 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- Interpretadores, por outro lado, traduzem e executam o código-fonte linha por linha durante a execução do programa. Isso facilita a depuração e a modificação do código, pois os erros podem ser identificados e corrigidos mais rapidamente.

_4 imagem(ns) no slide._

### Slide 13

- DESENVOLVIMENTO DE SISTEMAS
- No entanto, a execução do programa pode ser mais lenta, pois a tradução acontece simultaneamente à execução.
- A escolha entre compiladores e interpretadores depende das necessidades do projeto, bem como das características da linguagem de programação utilizada.

_4 imagem(ns) no slide._

### Slide 14

- DESENVOLVIMENTO DE SISTEMAS
- Para responder
- Discutam em duplas e socializem as ideias com a turma no final!
- Por que alguns desenvolvedores escolhem usar interpretadores em vez de compiladores ao trabalhar com linguagens de programação de alto nível?

_5 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Alguns desenvolvedores escolhem usar interpretadores em vez de compiladores porque interpretadores facilitam a depuração e a modificação rápida do código, já que a tradução do código de alto nível para linguagem de máquina ocorre em tempo real, linha por linha, durante a execução do programa.

_4 imagem(ns) no slide._

### Slide 16

- DESENVOLVIMENTO DE SISTEMAS
- Link para o curso: https://cursos.alura.com.br/course/arquitetura-computadores-funcionamento-programa
- Atividade Prática na Plataforma Alura
- Na plataforma Alura vamos acessar o seguinte curso:
- A recomendação é que você continue esse curso extraclasse, pois ele traz um conteúdo essencial para compreender sobre o referido tema.

_5 imagem(ns) no slide._

### Slide 17

- DESENVOLVIMENTO DE SISTEMAS
- Hora de praticar!
- Já imaginou como o computador entende os comandos que a gente escreve?
- Que tal entrar no mundo da programação de um jeito totalmente diferente e divertido?

_4 imagem(ns) no slide._

> **Notas do apresentador:** Dinâmica: Entendendo o Processo de Compilação Divida os participantes em grupos de 3 a 4 integrantes. Entregue a cada grupo dois tipos de cartões: Cartões com instruções escritas em linguagem de alto nível (semelhante a comandos de programação); Cartões com instruções equivalentes em linguagem de máquina (representando comandos que um computador entende). Dentro de cada grupo, atribuam os seguintes papéis: Programador: será responsável por montar um código simples utilizando os cartões em linguagem de alto nível. Compilador humano: deverá converter o código criado pelo programador para linguagem de máquina, utilizando os cartões de referência. Computador humano: executará as instruções em linguagem de máquina, realizando uma tarefa prática (como uma operação matemática simples, por exemplo: somar dois números). Após a execução da tarefa, cada grupo deverá discutir: Como a dinâmica ilustra o processo de compilação; Quais as vantagens e desvantagens de se utilizar compiladores em comparação com interpretadores; Em quais situações cada tipo de tradutor pode ser mais apropriado. Objetivo da atividade: Esta dinâmica visa demonstrar, de forma prática e colaborativa, como funciona o processo de tradução de um programa escrito em linguagem de alto nível para linguagem de máquina. Ao simular os papéis envolvidos, os participantes compreendem melhor o funcionamento de compiladores e refletem sobre as diferentes abordagens de tradução de código na programação.

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- Vamos Praticar?
- Vamos agora colocar em prática o que aprendemos desenvolvendo a atividade sugerida.

_4 imagem(ns) no slide._

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje
- Compreendemos o que é compiladores e interpretadores e suas particularidades.

_4 imagem(ns) no slide._

### Slide 20

- DESENVOLVIMENTO DE SISTEMAS
- Pronto para desbloquear sua carreira de TI?
- Está perdido estudando mas não sabe por onde começar? Se a resposta é sim, você está no lugar certo! Descubra as estratégias e ferramentas essenciais para te ajudar a desbloquear seu potencial em TI e buscar sua primeira vaga de emprego no setor!
- Este e-book é um guia completo para quem busca começar pelos melhores caminhos para se tornar um excelente profissional de TI, ensinando a identificar perfis profissionais, aplicar técnicas de estudo eficazes, transformar teoria em prática, e aumentar a visibilidade de seu trabalho no mercado de trabalho. Ideal para novatos e profissionais em transição.
- E o melhor, ele pode ser seu, inteiramente grátis!
- Basta clicar AQUI e realizar o seu cadastro com o seu @escola!

_6 imagem(ns) no slide._

### Slide 21

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

### Slide 22

- DESENVOLVIMENTO DE SISTEMAS
- O RCO+Aulas é um projeto da Secretaria de Estado da Educação do Paraná e está em constante revisão. Todos os slides são de uso exclusivo dos professores da Rede Pública de Ensino, com a finalidade específica de aplicação em sala de aula, sendo totalmente vedada a publicização, reutilização, reprodução total ou parcial para quaisquer outros fins.

_4 imagem(ns) no slide._

## Atividade

_Fonte: AULA 26_INTRODUÇÃO A COMPUTAÇÃO ATIVIDADE.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

INTRODUÇÃO A COMPUTAÇÃO

1ª SÉRIE

ATIVIDADE AULA 26

Questão 1

O que é um compilador?

a) Um programa que traduz código escrito em linguagem natural para linguagem de máquina.

b) Um programa que traduz código escrito em linguagem de máquina para linguagem de alto nível.

c) Um programa que traduz código escrito em linguagem de alto nível para linguagem de máquina.

d) Um programa que interpreta e executa código em tempo real.

Resposta correta: c) Um programa que traduz código escrito em linguagem de alto nível para linguagem de máquina.

Comentário: Um compilador é um programa que traduz todo o código-fonte escrito em uma linguagem de programação de alto nível, como Python, Java ou C++, para a linguagem de máquina, que é compreensível pelo processador do computador. A tradução ocorre antes da execução do programa e gera um arquivo executável que pode ser rodado no computador.

Questão 2

Qual das seguintes afirmações é verdadeira sobre os compiladores?

a) Os compiladores não geram arquivos executáveis.

b) Os compiladores traduzem o código-fonte linha por linha durante a execução do programa.

c) Os compiladores são usados apenas para linguagens de programação obsoletas.

d) Os compiladores convertem o código de alto nível em linguagem de máquina apenas uma vez, gerando um arquivo executável.

Resposta correta: d) Os compiladores convertem o código de alto nível em linguagem de máquina apenas uma vez, gerando um arquivo executável.

Comentário: Compiladores traduzem todo o código-fonte de uma linguagem de programação de alto nível para a linguagem de máquina antes da execução, gerando um arquivo executável. Esse processo de compilação ocorre apenas uma vez, e depois, o arquivo gerado pode ser executado várias vezes sem a necessidade de recompilar. Isso difere dos interpretadores, que traduzem e executam o código-fonte linha por linha durante a execução do programa.

## Prática

_Fonte: AULA 26_PRÁTICA INTRODUÇÃO A COMPUTAÇÃO.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

INTRODUÇÃO A COMPUTAÇÃO

1ª SÉRIE

AULA PRÁTICA 26

Resumo Explicativo:

Na segunda parte do estudo sobre como o computador lê o código, aprofundamos a análise do processo de execução de programas, abordando tópicos como linguagem de máquina, código intermediário, bytecode, e a função das máquinas virtuais. Compreender essas etapas permite ao aluno visualizar o que acontece entre o código que escrevemos e a ação final no computador, o que é essencial para resolver problemas de desempenho, compatibilidade e depuração em desenvolvimento de sistemas.

Estudo de Caso:

Cenário:

Durante a criação de um sistema simples de cadastro em Java, a aluna Gabriela percebeu que o programa funcionava em seu computador com Windows, mas também executava normalmente em um notebook com Linux, sem precisar de alterações. Curiosa, ela perguntou ao professor:

“Se o sistema operacional é diferente, como o programa funciona do mesmo jeito?”

O professor então explicou o conceito de bytecode e Java Virtual Machine (JVM): o código Java é compilado para um formato intermediário que não depende do sistema operacional, pois a JVM interpreta o bytecode em qualquer plataforma compatível.

Gabriela e seu grupo passaram a explorar como máquinas virtuais, interpretação em tempo de execução e compilação just-in-time (JIT) tornam essa portabilidade possível. Eles também compararam com linguagens que não usam máquinas virtuais, como C, que precisam ser recompiladas para cada sistema.

Questões:

- Liste três conceitos fundamentais envolvidos na execução de programas com máquinas virtuais (como JVM).
- Explique, com suas palavras, o que é o bytecode e como ele permite a execução de programas em diferentes sistemas operacionais.
- Você escreveu um programa em Java. Descreva o que acontece desde o momento em que você compila o código até ele ser executado em um computador com outro sistema operacional.
- Compare os processos de execução de um programa Java e um programa C. Quais são as principais diferenças e como elas impactam na portabilidade?
- Você acha que o uso de máquinas virtuais torna o sistema mais eficiente ou mais lento? Justifique sua resposta com base em desempenho e compatibilidade.
- Desenvolva uma apresentação em grupo (com diagramas ou fluxogramas) explicando como o Java transforma o código-fonte em uma ação executada na máquina, destacando o papel da JVM, bytecode e do compilador.
