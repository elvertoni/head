---
titulo: "Fundamentos do Sistema Operacional"
tipo: rco-seed
disciplina: introducao-a-computacao
sigla_rco: IAC
trimestre: 3
ordem_rco: 46
serie: 1
aula_rco: "Aula 46"
slides: 32
tem_atividade: false
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/IAC/3TRI/46-linux-ubuntu-fundamentos-do-sistema-operacional/46-linux-ubuntu-fundamentos-do-sistema-operacional.pptx"
extrator: tools/extrair_rco.py
status: bruto
---

# Fundamentos do Sistema Operacional

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- INTRODUÇÃO A COMPUTAÇÃO
- 1ª Série
- Linux Ubuntu:
- Fundamentos do Sistema Operacional
- Aula 46

_1 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- Nesta aula vamos:
- Compreender os fundamentos de gerenciamento do sistema operacional Linux Ubuntu.
- Identificar a importância do gerenciamento do sistema operacional Linux Ubuntu.

_1 imagem(ns) no slide._

### Slide 4

- Este material foi elaborado com base na análise do plano de curso, abrangendo os conhecimentos essenciais para o curso Técnico em Desenvolvimento de Sistemas. Inclui aulas práticas desenvolvidas de acordo com as metodologias ativas, visando ao desenvolvimento de habilidades e competências de forma dinâmica e significativa. Você tem total liberdade para personalizar o material de acordo com seu contexto, otimizando o aproveitamento deste conteúdo.
- Em caso de falta ou indisponibilidade de acesso à internet no local de aula, você poderá utilizar os seguintes artigos para criação de material complementar para auxiliar na aula:
- ATENÇÃO PROFESSOR!

_1 imagem(ns) no slide._

### Slide 5

- Aula anterior
- Aprendemos sobre a arquitetura do sistema operacional Ubuntu.

_1 imagem(ns) no slide._

### Slide 6

- Para refletir
- Gerenciar um sistema operacional abarca fazer a configuração do sistema para que o hardware e o software possam ser executados de maneira adequada em computadores pessoais.
- O gerenciamento do sistema operacional Linux Ubuntu pode também ser abordado em diferentes atividades:
- Gerenciar a distribuição e as versões do sistema operacional.
- Gerenciar as atividades de configuração e instalação de dispositivos de hardware e de softwares no computador via sistema operacional.
- Gerenciar arquivos e pastas do usuário através do sistema operacional.

_7 imagem(ns) no slide._

### Slide 7

- Linux Ubuntu x tipos de computadores
- O sistema operacional Linux Ubuntu é um sistema para computadores pessoais?
- Ele é apenas para computadores do tipo PC (Personal Computer)?
- Então o Linux Ubuntu é um sistema operacional que pode ser instalado em todos os tipos de computadores?
- https://t.ctcdn.com.br/flZk8xGrFgPIRdvy_NqbSZOOrDU=/512x288/smart/filters:format(webp)/i624148.jpeg
- Discutam em duplas e socializem as respostas com a turma no final!

_2 imagem(ns) no slide._

### Slide 8

- Resposta
- Fonte: https://asmetro.org.br/portalsn/wp-content/uploads/2023/02/81-1.jpg
- O sistema operacional Linux Ubuntu é um sistema para computadores pessoais?
- Sim, o sistema operacional Linux Ubuntu pode ser instalado para controle e execução das operações em um computador pessoal.

_1 imagem(ns) no slide._

### Slide 9

- Resposta
- Fonte: https://asmetro.org.br/portalsn/wp-content/uploads/2023/02/81-1.jpg
- Ele é apenas para computadores do tipo PC (Personal Computer)?
- Na realidade, o Linux Ubuntu pode ser instalado em computadores pessoais chamados de PC, que conhecemos como desktops ou notebooks, assim como em outros tipos de computadores, como servidores e também em dispositivos móveis.

_3 imagem(ns) no slide._

### Slide 10

- Resposta
- Então o Linux Ubuntu é um sistema operacional que pode ser instalado em todos os tipos de computadores?
- O Linux Ubuntu pode ser instalado na grande maioria de computadores: em supercomputadores, em computadores pessoais, em smartphones e mesmo em dispositivos da internet das coisas (smartwatches, por exemplo). Em nossos estudos iremos considerar os computadores pessoais como dispositivos que operam o sistema operacional Linux Ubuntu.

_1 imagem(ns) no slide._

### Slide 11

- A origem do Linux Ubuntu e suas aplicações?”
- https://drive.google.com/file/d/1IvYkpGqj3ef6Z8KBK683ORDkGf6-pirH/view?usp=drive_link
- OBS: link do vídeo deve ser atualizado caso a apresentação mude de pasta junto com os vídeos

_4 imagem(ns) no slide._

### Slide 12

- Para responder
- 1. Qual foi a origem do Linux Ubuntu?
- 2. E qual é a empresa que é responsável pelo Linux Ubuntu?
- Responda em seu caderno!
- Na aula 44

_3 imagem(ns) no slide._

### Slide 13

- Resposta
- Qual foi a origem do Linux Ubuntu?
- O sistema operacional Linux Ubuntu teve sua origem em 2004 junto a um projeto liderado por Mark Shuttleworth com objetivo de possibilitar um sistema operacional novo com lançamentos frequentes de atualizações, foco em localização e acessibilidade, de fácil uso e interface amigável, com colaboração de comunidades de desenvolvimento e um novo conjunto de ferramentas de software.

_1 imagem(ns) no slide._

### Slide 14

- Resposta
- E qual é a empresa que é responsável pelo Linux Ubuntu?
- Na atualidade a empresa Canonical é uma organização em formato de comunidade que mantém os incentivos e desenvolvimento do sistema Linux Ubuntu.

_3 imagem(ns) no slide._

### Slide 15

- Instalando o Linux Ubuntu
- Ao instalar um sistema operacional Linux Ubuntu é possível ter acesso a um pacote completo de sistemas, pois o sistema é distribuído de forma completa em mídias (como CD, DVD ou arquivos em pendrive) ou mesmo através de downloads de sites que fomentam o modelo Linux baseado no código aberto.

_3 imagem(ns) no slide._

### Slide 16

- Instalando o Linux Ubuntu
- Pacote de dados de instalação para o sistema operacional para um cliente (estação de trabalho).
- Pacote de dados de instalação para o sistema operacional para servidores.
- Pacote de dados para aplicações como suíte de escritório, aplicativos multimídia, navegadores de internet dentre outros.

_3 imagem(ns) no slide._

### Slide 17

- Inicializando o Linux Ubuntu
- O Linux Ubuntu normalmente é iniciado por uma linha de comando, e também possui diversas interfaces gráficas. Importante dizer que o sistema pode ser inicializado em sua interface gráfica de forma automática.
- O Linux Ubuntu então pode ser gerenciado de duas formas: Através de linhas de comandos em uma interface baseada em textos digitados. Através de uma interface gráfica baseada em ícones e janelas.

_1 imagem(ns) no slide._

### Slide 18

- Gerenciamento por linha de comando
- A forma nativa para interface com o sistema Linux é o prompt de comando, ou seja, a inclusão de códigos em formato de comando para interagir com o sistema.
- No prompt de comando são digitados comandos previamente estabelecidos que permitem a instalação do sistema operacional, instalação de pacotes adicionais e o gerenciamento do sistema.
- No gerenciamento normalmente podem ser realizadas:
- Atividades de instalação do sistema.
- Atividades de configuração do sistema.
- Atividades de gerenciamento de arquivos de forma geral.

### Slide 19

- Comandos de gerenciamento
- O gerenciamento do sistema operacional Linux Ubuntu pode fazer uso de comandos para gerenciar serviços do sistema operacional e da rede de computadores, processos (que são programas em execução), arquivos e parâmetros do sistema (data, hora, região, etc).

_1 imagem(ns) no slide._

### Slide 20

- Exemplos de comandos
- Exemplos de comandos para gerenciamento de processos são:
- top – comando para verificar o uso dos processos do sistema.
- ps – lista os processos em execução no sistema.
- pstree – lista os processos em formato de árvore.
- Exemplos de comandos para o gerenciamento de arquivos e diretórios:
- ls – lista arquivos e diretórios do sistema.
- cd – navega entre diretórios.
- cp – copia arquivos e diretórios.
- DESENVOLVIMENTO DE SISTEMAS

_2 imagem(ns) no slide._

### Slide 21

- Gerenciamento por ambiente gráfico
- O Linux oferece a possibilidade de escolher interfaces gráficas diversas, considerando que há pacotes que podem ser copiados e instalados em seu computador (download).
- Exemplos de ambientes gráficos no Linux são: KDE e o GNOME.
- No Linux Ubuntu, o ambiente gráfico também é baseado em janelas e ícones, que dão acesso às atividades e gerenciamento do sistema operacional assim com o aos softwares aplicativos.
- DESENVOLVIMENTO DE SISTEMAS

_2 imagem(ns) no slide._

### Slide 22

- Ambiente Gráfico
- O ambiente gráfico é formado por um conjunto de itens:
- Área de Trabalho (Desktop) – há uma grande tela com um local para que suas aplicações sejam abertas e utilizadas da forma desejada.
- Podemos considerar a Área de Trabalho como o ambiente em que o usuário trabalha.
- Barra de Menus (Painel) – com as funções comuns utilizadas no Ubuntu e acesso aos recursos de sistema e informações como hora, botão de ligar e desligar, controle de som e de teclado, etc.
- Barra de Tarefas – fica na parte inferior da área de trabalho (normalmente) que exibe os programas abertos para utilização.
- DESENVOLVIMENTO DE SISTEMAS

_2 imagem(ns) no slide._

### Slide 23

- Ambiente Gráfico
- Lançador (Laucnher) – permite o acesso a aplicações, dispositivos e abriga o Painel Inicial como primeiro ambiente que leva o usuário a acessar outros recursos. Mantém os ícones de programas usados com frequência no sistema operacional e assemelha-se a uma barra de tarefas. Permite acesso à Lixeira, Pasta Pessoal, alternador de espaços de trabalho e dispositivos de armazenamento (HD / SSD, CD e DVD) e Configurações.
- Ainda há outros itens como: Indicadores, Notificações do Sistema e Lixeira.
- DESENVOLVIMENTO DE SISTEMAS

_2 imagem(ns) no slide._

### Slide 24

- Ambiente Gráfico
- Configurações – dá acesso a um ambiente que permite as configurações do sistema operacional assim como de periféricos e softwares aplicativos no sistema.
- Painel Inicial (Dashboard) – permite acesso e gerenciamento de arquivos e acessórios, normalmente está disponível na área de trabalho e é semelhante ao Menu Iniciar do Windows.
- Também permite o usuário gerenciar documentos, fotos, músicas, vídeos, aplicativos e acessórios do Linux Ubuntu, oferece.
- Aqui temos um ambiente rico e completo que auxiliar o usuário a fazer o real gerenciamento do sistema operacional.
- DESENVOLVIMENTO DE SISTEMAS

_2 imagem(ns) no slide._

### Slide 25

- Ambiente Gráfico
- O Dashboard permite gerenciar:
- Terminal.
- Visualizador de documentos.
- Gerenciamento de arquivos compactados.
- Detalhes.
- Área de trabalho.
- Editor de texto.
- E diversos outros recursos para gerenciar seu computador.

_1 imagem(ns) no slide._

### Slide 26

- Vamos Praticar?
- Vamos agora colocar em prática o que aprendemos desenvolvendo a atividade sugerida.

_4 imagem(ns) no slide._

### Slide 27

- https://www.zenarmor.com/docs/linux-tutorials/what-is-linux
- DESENVOLVIMENTO DE SISTEMAS

_6 imagem(ns) no slide._

### Slide 28

- O que vimos na aula de hoje:
- Aprendemos que o Linux Ubuntu é um sistema operacional de código aberto (open source).
- Aprendemos que ele tem objetivo de oportunizar uso de softwares em formato de código aberto.
- DESENVOLVIMENTO DE SISTEMAS
- DESENVOLVIMENTO DE SISTEMAS

_6 imagem(ns) no slide._

### Slide 29

- Acesse o
- QR code e
- realize a sua
- inscrição!

_5 imagem(ns) no slide._

### Slide 30

- Pronto para desbloquear sua carreira de TI?
- Está perdido estudando mas não sabe por onde começar? Se a resposta é sim, você está no lugar certo! Descubra as estratégias e ferramentas essenciais para te ajudar a desbloquear seu potencial em TI e buscar sua primeira vaga de emprego no setor!
- Este e-book é um guia completo para quem busca começar pelos melhores caminhos para se tornar um excelente profissional de TI, ensinando a identificar perfis profissionais, aplicar técnicas de estudo eficazes, transformar teoria em prática, e aumentar a visibilidade de seu trabalho no mercado de trabalho. Ideal para novatos e profissionais em transição.
- E o melhor, ele pode ser seu, inteiramente grátis!
- Basta clicar AQUI e realizar o seu cadastro com o seu @escola!

_3 imagem(ns) no slide._

### Slide 31

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

### Slide 32

_(sem texto)_
