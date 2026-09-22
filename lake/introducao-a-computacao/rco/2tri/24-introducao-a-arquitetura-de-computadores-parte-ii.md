---
titulo: "Introdução à Arquitetura de Computadores - Parte II"
tipo: rco-seed
disciplina: introducao-a-computacao
sigla_rco: IAC
trimestre: 2
ordem_rco: 24
serie: 1
aula_rco: "Aula 24"
slides: 26
tem_atividade: true
tem_pratica: true
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/IAC/2TRI/24-introducao-a-arquitetura-de-computadores-parte-ii/24-introducao-a-arquitetura-de-computadores-parte-ii.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/IAC/2TRI/24-introducao-a-arquitetura-de-computadores-parte-ii/AULA 24_INTRODUÇÃO A COMPUTAÇÃO ATIVIDADE.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/IAC/2TRI/24-introducao-a-arquitetura-de-computadores-parte-ii/AULA 24_PRÁTICA INTRODUÇÃO A COMPUTAÇÃO.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Introdução à Arquitetura de Computadores - Parte II

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- INTRODUÇÃO A COMPUTAÇÃO
- 1ª SÉRIE
- Introdução à Arquitetura de Computadores - Parte II
- Aula 24

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
- Compreender dos fundamentos básicos da arquitetura de computadores.

_7 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Na aula anterior...
- Tivemos inicio a introdução de arquitetura de computadores e como eles se comportam.

_4 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Sabendo que o termo “arquitetura” remete ao estudo e modelagem da estrutura de um ambiente físico, podemos rapidamente entender que “arquitetura de computadores” refere-se ao estudo da estrutura de computadores.

_4 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Porém, não é só a estrutura física de um computador que deve ser observada, mas também a estrutura lógica, o que nos remete ao hardware e ao software, comparando com o mundo não digital, podemos pensar em construções civis e construções artísticas que podem muito bem sem misturar.

_4 imagem(ns) no slide._

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Por que é importante compreender a arquitetura de computadores, incluindo tanto a estrutura física quanto a lógica?
- Discutam em duplas e socializem as respostas com a turma no final!

_5 imagem(ns) no slide._

### Slide 10

- Compreender a arquitetura de computadores é importante porque auxilia profissionais da área de TI a projetar e otimizar sistemas computacionais eficientes, robustos e adaptáveis às necessidades dos usuários.
- DESENVOLVIMENTO DE SISTEMAS

_4 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Arquitetura de computadores: o básico
- OBS: link do vídeo deve ser atualizado caso a apresentação mude de pasta junto com os vídeos.
- https://drive.google.com/file/d/1fYBKw0Pp8KncK5vxzxvlNqTG7hqs6nys/view?usp=drive_link

_5 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- Para responder
- Como é a relação entre os componentes?
- O termo “controlador” foi citado e será muito mencionado. Qual foi a definição apresentada?
- Discutam em duplas e socializem as ideias com a turma no final!

_5 imagem(ns) no slide._

### Slide 13

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- 1. São representados por meio de sistemas hierárquicos, o que se mostra ideal para o estudo de conjuntos complexos e que atuam em diferentes níveis.
- 2. É um chip ou um conjunto de chips que controla fisicamente o dispositivo; ele recebe comandos do sistema operacional (software), por exemplo, para ler dados dos dispositivos e para enviá-los.

_6 imagem(ns) no slide._

### Slide 14

- DESENVOLVIMENTO DE SISTEMAS
- O processador é o “cérebro” do computador, e é em função deste que toda a estrutura trabalha. Um computador pode possuir um microprocessador simples, mas também pode ser uma supermáquina com inúmeros processadores.

_5 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- Componente básicos de um computador
- Até este momento, os componentes do computador foram estudados de forma isolada, mas a partir de agora, todos os elementos irão se encaixar.
- Ao estudarmos qualquer assunto complexo e/ou com grande riqueza de detalhes, a estratégia mais natural para facilitar o processo de aprendizado é subdividir o tema principal em partes menores, e então, preocupar-se somente com uma porção por vez.

_4 imagem(ns) no slide._

### Slide 16

- DESENVOLVIMENTO DE SISTEMAS

_4 imagem(ns) no slide._

### Slide 17

- DESENVOLVIMENTO DE SISTEMAS
- Sendo os principais componentes do computador, o processador, a memória e o dispositivo de E/S, sua comunicação, ou seja, a transmissão de dados é realizada por uma estrutura de interconexão entre estes e todos os outros componentes, que chamamos de barramento.
- Este barramento são conexões elétricas que transportam as informações entre os dispositivos de hardware.

_4 imagem(ns) no slide._

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- De forma técnica, quando observamos os termos propostos pela arquitetura de computadores, um barramento é um conjunto de linhas de comunicação (condutor elétrico ou fibra ótica) que permite a interligação entre dispositivos de um sistema de computação (CPU; Memória Principal; HD e outros periféricos), ou entre vários sistemas de computação.

_4 imagem(ns) no slide._

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- Para aumentar o desempenho do sistema, os barramentos são organizados de forma hierárquica, isolando o tráfego de dados entre CPU e memória do tráfego proveniente de operações de E/S. A CPU (Central Process Unit ou Unidade Central de Processamento) é composta pelos elementos a seguir.

_4 imagem(ns) no slide._

### Slide 20

- DESENVOLVIMENTO DE SISTEMAS
- A CPU contém internamente uma memória de alta velocidade, que permite o armazenamento de valores intermediários ou informações de comando.
- Essa memória é composta por “registros”, e cada registro tem uma função própria.

_4 imagem(ns) no slide._

### Slide 21

- DESENVOLVIMENTO DE SISTEMAS

_4 imagem(ns) no slide._

### Slide 22

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje
- Conhecemos as funções básicas de um computador são: o processamento de dados, o armazenamento de dados, a transferência de dados e o controle.

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

_Fonte: AULA 24_INTRODUÇÃO A COMPUTAÇÃO ATIVIDADE.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

INTRODUÇÃO A COMPUTAÇÃO

1ª SÉRIE

ATIVIDADE AULA 24

Questão 1

A estrutura da arquitetura de um computador é formada, basicamente, por registradores, nos quais são armazenados os dados e as instruções correntes:

- Unidade central de processamento.
- Memória RAM.
- Hard disk.
- Unidade Lógica e Aritmética.
Resposta comentada: A resposta correta é a alternativa A, pois a unidade central de processamento (CPU) é uma estrutura formada, basicamente, por registradores. A memória RAM é um tipo de tecnologia que permite o acesso aos arquivos armazenados no computador, enquanto o hard disk, popularmente chamado de HD (derivação de HDD do inglês hard disk drive) é a "memória de massa" ou "memória secundária" do computador. Por fim, a unidade lógica e aritmética (ULA), em inglês Arithmetic Logic Unit (ALU), é um circuito digital que realiza operações de adição e booleana AND.

Questão 2

A análise de um sistema de computação permite uma compreensão mais clara da estrutura de funcionamento de um computador, identificando claramente os seguintes pontos: o comportamento de cada componente, por meio dos dados e sinais de controle que são trocados com os demais componentes e a interconexão entre eles. Sobre o computador e seus periféricos, é correto afirmar que:

- O teclado é um periférico que permite comunicação bidirecional.
- A CPU é o único dispositivo com acesso direto à memória. Todos os periféricos dependem da CPU para leitura e escrita na RAM.
- Um monitor touchscreen é um periférico apenas de saída.
- O Universal Serial Bus é o novo barramento interno para comunicação CPU – Memória RAM.
Resposta comentada: A resposta correta é a alternativa B, pois o processador é o único dispositivo com acesso direto à memória. Todos os periféricos dependem do processador para leitura e escrita na RAM. A alternativa A está incorreta, pois o teclado é um dispositivo apenas de entrada. A alternativa C está incorreta, pois um monitor touchscreen é um periférico de entrada e saída. A alternativa D está incorreta, pois o Universal Seral Bus (USB) é um padrão de indústria que estabelece especificações para cabos e conectores, promovendo a fácil conexão de vários periféricos.

## Prática

_Fonte: AULA 24_PRÁTICA INTRODUÇÃO A COMPUTAÇÃO.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

INTRODUÇÃO A COMPUTAÇÃO

1ª SÉRIE

AULA PRÁTICA 24

Resumo Explicativo:

A arquitetura de computadores define como os componentes internos de um sistema computacional trabalham em conjunto para processar dados e executar tarefas. Na Parte II deste tema, aprofundamos o entendimento sobre elementos como barramentos, ciclos de instrução, memória cache, registradores e a comunicação entre CPU e memória. Compreender esses conceitos é fundamental para o desenvolvimento de sistemas eficientes, otimizando desempenho e compatibilidade entre hardware e software.

Estudo de Caso:

Cenário:

A equipe de alunos da turma de Desenvolvimento de Sistemas do 2º ano do ensino médio técnico foi convidada a participar de uma maratona escolar de tecnologia. O desafio: criar uma simulação educacional que mostre, em tempo real, o caminho percorrido por uma instrução dentro de um computador — desde seu carregamento na memória até sua execução pela CPU.

Durante a preparação, os alunos se depararam com dificuldades:

- Entender como os dados se movem entre os registradores, cache, RAM e CPU.
- Explicar a função dos barramentos (de dados, de endereço e de controle).
- Representar de forma visual os estágios do ciclo de instrução: busca, decodificação, execução e escrita.
A equipe percebeu que, para completar a tarefa, era necessário compreender de forma clara e prática a arquitetura interna do computador e como ela influencia o desempenho do sistema.

Questões:

- Liste os três tipos principais de barramentos utilizados na arquitetura de computadores e a função básica de cada um.
- Explique, com suas próprias palavras, o que ocorre durante o ciclo de instrução em um processador.
- Suponha que um programa está acessando dados constantemente da RAM em vez da cache. Qual impacto isso pode ter no desempenho? Proponha uma solução simples para esse problema.
- Analise como os registradores, a memória cache e a RAM interagem durante a execução de uma instrução. Qual o papel de cada um nesse fluxo?
- Você acredita que o aumento do tamanho da memória cache sempre melhora o desempenho do sistema? Justifique sua resposta com base na arquitetura de computadores.
- Crie um fluxograma ou roteiro visual que simule as etapas do ciclo de instrução, incluindo a movimentação dos dados entre os componentes envolvidos (registradores, cache, RAM, unidade de controle, etc).
