---
titulo: "Entendendo a Execução de Programas pelo Computador"
tipo: rco-seed
disciplina: introducao-a-computacao
sigla_rco: IAC
trimestre: 2
ordem_rco: 2001
serie: 1
aula_rco: "Aula RETOMADA 2"
slides: 30
tem_atividade: true
tem_pratica: true
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/IAC/2TRI/2001-entendendo-a-execucao-de-programas-pelo-computador/2001-entendendo-a-execucao-de-programas-pelo-computador.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/IAC/2TRI/2001-entendendo-a-execucao-de-programas-pelo-computador/AULA_RETOMADA_2_ATIVIDADE_ INTRODUÇÃO A COMPUTAÇÃO.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/IAC/2TRI/2001-entendendo-a-execucao-de-programas-pelo-computador/AULA RETOMADA_2_PRÁTICA INTRODUÇÃO A COMPUTAÇÃO.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Entendendo a Execução de Programas pelo Computador

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- INTRODUÇÃO A COMPUTAÇÃO
- 1° Série
- Entendendo a Execução de Programas pelo Computador
- Aula RETOMADA 2

_1 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- Nesta aula vamos:
- Rever como o computador executa um programa.
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store

_6 imagem(ns) no slide._

### Slide 4

- Este material foi elaborado com base na análise do plano de curso, abrangendo os conhecimentos essenciais para o curso Técnico em Desenvolvimento de Sistemas. Inclui aulas práticas desenvolvidas de acordo com as metodologias ativas, visando ao desenvolvimento de habilidades e competências de forma dinâmica e significativa. Você tem total liberdade para personalizar o material de acordo com seu contexto, otimizando o aproveitamento deste conteúdo.
- Em caso de falta ou indisponibilidade de acesso à internet no local de aula, você poderá utilizar os seguintes artigos para criação de material complementar para auxiliar na aula:
- Memória RAM:
- https://cursos.alura.com.br/course/arquitetura-computadores-funcionamento-programa/task/86304
- ATENÇÃO PROFESSOR!

_2 imagem(ns) no slide._

### Slide 5

- Para pensarmos juntos...
- Maria acaba de comprar seu primeiro computador e está animada para começar a usar. No entanto, ao começar a instalar programas e salvar arquivos, ela percebe que o espaço no disco rígido do computador está sendo rapidamente consumido. Ela começa a se perguntar sobre o conceito de armazenamento em um computador e como pode gerenciar melhor o espaço disponível.
- 3 minutos
- Conversem e apresentem suas visões!
- https://s2.glbimg.com/BPMQfoP3llbWPgNA0T0rQHSOnRA=/0x0:1920x1080/984x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_08fbf48bc0524877943fe86e43087e7a/internal_photos/bs/2023/d/8/G8GT17SLAPwXtdUxMRkQ/13th-gen-hx-processors-themed-background.jpg

_4 imagem(ns) no slide._

### Slide 6

- Para pensarmos juntos...
- O que é armazenamento em um computador e como posso gerenciar melhor o espaço de armazenamento?
- 3 minutos
- Conversem e apresentem suas visões
- https://static.wixstatic.com/media/721229_92eba4ce963443a0996e31ae7fe1c871~mv2.jpg/v1/fill/w_640,h_304,al_c,q_80,usm_0.66_1.00_0.01,enc_auto/721229_92eba4ce963443a0996e31ae7fe1c871~mv2.jpg

_4 imagem(ns) no slide._

### Slide 7

- Resposta
- O armazenamento em um computador refere-se ao espaço disponível para guardar dados, como programas e arquivos. Existem diferentes tipos de armazenamento, como a memória RAM, que é temporária e usada para dados em uso ativo, e o disco rígido ou SSD, que é um armazenamento de longo prazo para arquivos e programas.
- 3 minutos
- Conversem e apresentem suas visões!
- Fonte https://publicdomainvectors.org/pt/vetorial-gratis/Lista-de-verifica%C3%A7%C3%A3o/45330.html

_4 imagem(ns) no slide._

### Slide 8

- Conceituando
- O armazenamento de um computador se refere ao local onde os dados são guardados para uso posterior. Isso inclui todos os arquivos, programas, documentos, fotos, músicas, filmes e o sistema operacional. Há diferentes tipos de armazenamento, incluindo a memória de acesso aleatório (RAM), o disco rígido (HDD) ou a unidade de estado sólido (SSD).
- https://wiki.inf.ufpr.br/computacao/lib/exe/fetch.php?w=400&tok=f88954&media=a:jornada-do-desenvolvedor-arquitetura-de-computadores-gustavo-kennedy-renkel.jpeg

_2 imagem(ns) no slide._

### Slide 9

- Conceituando
- A RAM é uma forma de armazenamento temporário que permite ao computador acessar rapidamente os dados necessários para as tarefas em execução. Quando você desliga o computador, os dados na RAM são apagados. Por outro lado, o HDD ou SSD são formas de armazenamento de longo prazo. Eles mantêm os dados mesmo quando o computador está desligado.
- https://alexide.github.io/conteudo/img/img1.png

_2 imagem(ns) no slide._

### Slide 10

- Conceituando
- O espaço de armazenamento disponível em um computador tem um grande impacto em sua utilização. Se o disco rígido ou a unidade de estado sólido estiverem quase cheios, o computador pode funcionar mais lentamente, pois terá menos espaço para mover e gerenciar os arquivos. Além disso, se a RAM estiver cheia, o computador terá dificuldade em manter muitos programas abertos ao mesmo tempo, o que pode levar a um desempenho mais lento ou travamentos.
- https://tm.ibxk.com.br/2021/12/22/22114306286189.jpg?ims=1200x675

_2 imagem(ns) no slide._

### Slide 11

- Conceituando
- É importante gerenciar o espaço de armazenamento do seu computador, mantendo apenas os arquivos e programas necessários, limpando regularmente os arquivos temporários e considerando soluções de armazenamento externo ou em nuvem se precisar de mais espaço. Ao fazer isso, você pode manter seu computador funcionando de maneira eficiente e evitar problemas de desempenho.
- https://tecnologia.culturamix.com/blog/wp-content/uploads/2012/09/Hardware-6.png

_2 imagem(ns) no slide._

### Slide 12

- Conceituando
- O processador, também conhecido como Unidade Central de Processamento (CPU), é muitas vezes comparado ao cérebro do computador. É o componente que executa a maioria das instruções dentro do computador, interpretando e realizando as operações básicas que fazem um sistema operar, como operações aritméticas, lógicas, de controle e de entrada/saída.

_2 imagem(ns) no slide._

### Slide 13

- Conceituando
- O funcionamento da CPU é baseado em um ciclo de instrução, que consiste em buscar uma instrução de memória, decodificá-la para entender o que deve ser feito, executar a operação necessária e, finalmente, armazenar o resultado. Este ciclo é repetido continuamente enquanto o computador está ligado.

_2 imagem(ns) no slide._

### Slide 14

- Conceituando
- No desenvolvimento de software, o processador desempenha um papel crucial. Os programas de software são, na verdade, uma série de instruções que a CPU precisa executar. A eficiência do processador - incluindo a velocidade do relógio, o número de núcleos (unidades de processamento) e a capacidade de realizar vários processos simultaneamente (multitarefa) - pode ter um grande impacto no quão rápido e eficiente um programa de software pode ser executado.
- https://tecnologia.culturamix.com/blog/wp-content/uploads/2012/09/Hardware-6.png

_2 imagem(ns) no slide._

### Slide 15

- Conceituando
- Por fim, entender o funcionamento do processador pode ajudar os desenvolvedores a otimizar o software. Por exemplo, se um desenvolvedor sabe que um determinado processador é bom para executar múltiplas tarefas ao mesmo tempo, eles podem projetar seu software para tirar proveito disso. Da mesma forma, um desenvolvedor pode escrever software que executa operações de maneira mais eficiente com base no conhecimento de como a CPU decodifica e executa instruções.
- https://wiki.inf.ufpr.br/computacao/lib/exe/fetch.php?w=400&tok=f88954&media=a:jornada-do-desenvolvedor-arquitetura-de-computadores-gustavo-kennedy-renkel.jpeg

_2 imagem(ns) no slide._

### Slide 16

- Para Responder
- Por que é importante gerenciar o espaço de armazenamento em um computador?
- 5 minutos
- Discutam em duplas e socializem as ideias com a turma no final!
- Fonte: https://st3.depositphotos.com/13324256/19463/i/1600/depositphotos_194633760-free-stock-photo-pink-toned-picture-computer-keyboard.jpg

_4 imagem(ns) no slide._

### Slide 17

- Resposta
- Gerenciar o espaço de armazenamento de um computador é importante por várias razões. Em primeiro lugar, um computador com muito pouco espaço de armazenamento disponível pode funcionar mais lentamente, pois tem menos espaço para mover e gerenciar arquivos. Isso pode levar a um desempenho mais lento e até mesmo a travamentos do sistema.
- 5 minutos
- Fonte: https://st3.depositphotos.com/13324256/19463/i/1600/depositphotos_194633760-free-stock-photo-pink-toned-picture-computer-keyboard.jpg

_3 imagem(ns) no slide._

### Slide 18

- Ainda sobre Arquitetura de computadores, vamos conhecer praticando?
- Na plataforma Alura vamos acessar o seguinte curso:
- Link para o curso: https://cursos.alura.com.br/course/arquitetura-computadores-funcionamento-programa
- Para melhor entendimento do conteúdo é recomendado que se responda aos quiz que estiverem entre as atividades propostas

_2 imagem(ns) no slide._

### Slide 19

- Sobre Arquitetura de computadores, vamos conhecer praticando?
- A recomendação é que você continue esse curso extra-classe, pois ele traz um conteúdo introdutório essencial para compreender sobre o referido tema no desenvolvimento de software.
- Na tela seguinte siga as tarefas que estiverem em sequência igual ao próximo exemplo.

_2 imagem(ns) no slide._

### Slide 20

- Sobre Arquitetura de computadores, vamos conhecer praticando?
- Os próximos itens serão para guiar nas principais atividades que são necessárias para o entendimento da aula de hoje, embora existam mais atividades na plataforma, em sala iremos desenvolver as essenciais, fique a vontade para praticar em casa.

_1 imagem(ns) no slide._

### Slide 21

- Armazenando código
- 7 minutos
- Os arquivos ficam guardados em algum lugar do computador e provavelmente em algum sistema de pasta.
- Link para tarefa: https://cursos.alura.com.br/course/arquitetura-computadores-funcionamento-programa/task/86301
- Mas como que fisicamente armazena no sistema de pastas, como que fisicamente guarda esses arquivos?
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 22

- Memória RAM
- 8 minutos
- Temos nosso programa que está armazenado e é mandado para a memória RAM para ser executado.
- Link para tarefa: https://cursos.alura.com.br/course/arquitetura-computadores-funcionamento-programa/task/86302
- É na memória RAM que guarda os dados computador está lendo, modificando constantemente naquele momento.
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 23

- Funcionamento do processador
- 10 minutos
- O processador tem um papel crucial na execução de suas aplicações.
- Link para tarefa: https://cursos.alura.com.br/course/arquitetura-computadores-funcionamento-programa/task/86305
- Com base no seu desenvolvimento, ele irá consumir recursos de processamento, nesse caso a arquitetura tem impacto crucial.
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 24

- Executando código
- 10 minutos
- O processador irá executar as instruções, e o seu software faz parte dessas instruções.
- Link para tarefa: https://cursos.alura.com.br/course/arquitetura-computadores-funcionamento-programa/task/86306
- Precisamos executar as instruções de uma forma bem-organizada, dessa maneira todas as instruções do computador são executadas na mesma sequência de passos, sempre na mesma sequência cíclica para executar as instruções.
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 25

- Memória na prática
- 10 minutos
- Memória primária e secundária também impacta no desempenho.
- Link para tarefa: https://cursos.alura.com.br/course/arquitetura-computadores-funcionamento-programa/task/86308
- A memória secundária, como o disco rígido ou SSD, é crucial no desenvolvimento de software pois armazena o código-fonte e os arquivos de dados usados. Além disso, é onde os programas e bibliotecas necessários para o desenvolvimento são instalados, e onde os aplicativos compilados são armazenados para execução.
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 26

- Vamos Praticar?
- Agora é com você! vamos praticar? Praticar é uma forma de poder fixar o conteúdo e melhorar o aprendizado.

_1 imagem(ns) no slide._

### Slide 27

- O que vimos na aula de hoje:
- Compreendemos sobre armazenamento de computadores e como ele impacta em sua utilização.
- Compreendemos sobre o funcionamento do processador e como ele impacta no desenvolvimento de aplicações.

_1 imagem(ns) no slide._

### Slide 28

- Pronto para desbloquear sua carreira de TI?
- Está perdido estudando mas não sabe por onde começar? Se a resposta é sim, você está no lugar certo! Descubra as estratégias e ferramentas essenciais para te ajudar a desbloquear seu potencial em TI e buscar sua primeira vaga de emprego no setor!
- Este e-book é um guia completo para quem busca começar pelos melhores caminhos para se tornar um excelente profissional de TI, ensinando a identificar perfis profissionais, aplicar técnicas de estudo eficazes, transformar teoria em prática, e aumentar a visibilidade de seu trabalho no mercado de trabalho. Ideal para novatos e profissionais em transição.
- E o melhor, ele pode ser seu, inteiramente grátis!
- Basta clicar AQUI e realizar o seu cadastro com o seu @escola!

_3 imagem(ns) no slide._

### Slide 29

- Referências:
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

### Slide 30

_(sem texto)_

## Atividade

_Fonte: AULA_RETOMADA_2_ATIVIDADE_ INTRODUÇÃO A COMPUTAÇÃO.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

INTRODUÇÃO A COMPUTAÇÃO

1ª SÉRIE

ATIVIDADE AULA RETOMADA 2

Questão 1

Qual das seguintes opções melhor descreve a sequência de passos que um computador realiza para executar um programa?

a) Leitura -> Armazenamento -> Execução

b) Armazenamento -> Leitura -> Execução

c) Execução -> Leitura -> Armazenamento

d) Leitura -> Execução -> Armazenamento

Resposta Correta: a) Leitura -> Armazenamento -> Execução. O computador lê o programa do dispositivo de armazenamento, o carrega na memória e então o executa.

Questão 2

Qual componente de um computador é responsável pela execução das instruções de um programa?

a) Memória RAM

b) Disco rígido

c) Unidade central de processamento (CPU)

d) Placa de vídeo

Resposta Correta: c) Unidade central de processamento (CPU). A CPU é o cérebro do computador, onde as instruções de um programa são executadas.

## Prática

_Fonte: AULA RETOMADA_2_PRÁTICA INTRODUÇÃO A COMPUTAÇÃO.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

INTRODUÇÃO A COMPUTAÇÃO

1ª SÉRIE

AULA PRÁTICA RETOMADA 2

Resumo Explicativo:

Quando um programa é executado no computador, ele passa por várias etapas desde o armazenamento no disco até a execução pelo processador. Esse processo envolve a leitura do código pela CPU, a alocação de memória pela RAM e a coordenação com o sistema operacional para gerenciar recursos. Entender esse fluxo é fundamental para futuros desenvolvedores, pois permite otimizar o desempenho, identificar gargalos e compreender como o software se comunica com o hardware.

Estudo de Caso:

Cenário:

Bianca é estudante do ensino médio técnico e decidiu criar um jogo simples em Python. Após escrever o código no editor, ela executa o programa e observa o funcionamento: o personagem responde aos comandos, sons são reproduzidos e os pontos são atualizados na tela. No entanto, ela notou que, em alguns momentos, o jogo ficava lento.

Ao conversar com seu professor, Bianca descobre que o código-fonte é interpretado pelo Python, que o sistema operacional gerencia os processos em execução e que, se outros programas estiverem abertos, podem competir pelos mesmos recursos — especialmente memória RAM e CPU. Assim, ela aprende como o sistema operacional e o hardware trabalham juntos para executar seu jogo.

Questões:

- Quais são os principais componentes envolvidos na execução de um programa no computador?
- Explique com suas palavras como um código é transformado em ações visíveis na tela do computador.
- Dado um código simples em Python, identifique em qual etapa pode ocorrer lentidão caso o computador esteja com pouca memória disponível.
- Analise a relação entre o sistema operacional e o processador durante a execução de um programa. Quais funções cada um desempenha?
- Avalie se manter muitos programas abertos ao mesmo tempo pode impactar a execução de um novo programa. Justifique sua resposta com base no funcionamento da execução.
- Desenvolva um infográfico que represente as etapas da execução de um programa, desde o clique no botão “executar” até a resposta na tela.
