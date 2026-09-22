---
titulo: "Linux Ubuntu: Explorando a Arquitetura"
tipo: rco-seed
disciplina: introducao-a-computacao
sigla_rco: IAC
trimestre: 3
ordem_rco: 45
serie: 1
aula_rco: "Aula 45"
slides: 30
tem_atividade: false
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/IAC/3TRI/45-linux-ubuntu-explorando-a-arquitetura/45-linux-ubuntu-explorando-a-arquitetura.pptx"
extrator: tools/extrair_rco.py
status: bruto
---

# Linux Ubuntu: Explorando a Arquitetura

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- INTRODUÇÃO A COMPUTAÇÃO
- 1ª Série
- Linux Ubuntu: Explorando a Arquitetura
- Aula 45

_1 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- Este material foi elaborado com base na análise do plano de curso, abrangendo os conhecimentos essenciais para o curso Técnico em Desenvolvimento de Sistemas. Inclui aulas práticas desenvolvidas de acordo com as metodologias ativas, visando ao desenvolvimento de habilidades e competências de forma dinâmica e significativa. Você tem total liberdade para personalizar o material de acordo com seu contexto, otimizando o aproveitamento deste conteúdo.
- Em caso de falta ou indisponibilidade de acesso à internet no local de aula, você poderá utilizar os seguintes artigos para criação de material complementar para auxiliar na aula:
- GitHub: Plataforma para hospedagem e colaboração em projetos de software livre.
- F-Droid: Repositório de aplicativos Android de código aberto.
- LibreOffice: Pacote de escritório gratuito e open source, ótimo exemplo de software livre usado em casa e em empresas.
- ATENÇÃO PROFESSOR!

_2 imagem(ns) no slide._

### Slide 4

- Nesta aula vamos:
- Conhecer a arquitetura básica do sistema operacional Linux Ubuntu com os demais sistemas operacionais.
- Identificar as vantagens e desvantagens de tal arquitetura.
- DESENVOLVIMENTO DE SISTEMAS

_5 imagem(ns) no slide._

### Slide 5

- Aula anterior
- Compreendemos o processo de instalação do sistema operacional Ubuntu, identificando as etapas e configurações necessárias para seu correto funcionamento.

_1 imagem(ns) no slide._

### Slide 6

- Você sabia que…
- Os sistemas operacionais foram criados, primeiramente, para controle e organização de recursos dos computadores de grande e médio porte, e eram exclusivos para esses computadores.
- Em seguida, com o desenvolvimento de computadores pessoais na década de 1970, sistemas operacionais específicos para estes computadores passaram a ser desenvolvidos.

_1 imagem(ns) no slide._

### Slide 7

- Além do Microsoft Windows, vocês conhecem mais algum outro sistema operacional?
- E o Linux é um sistema operacional ou são vários sistemas operacionais?
- Então o Linux tem diferentes distribuições?
- Realizem a atividade em duplas e socializem no final!

_2 imagem(ns) no slide._

### Slide 8

- Diversos sistemas operacionais foram e são utilizados em supercomputadores, computadores de grande porte, computadores pessoais e dispositivos móveis na atualidade. Alguns deles são: UNIX, System 7, FreeBSD, Android, iOS, Mac OS X e o Linux.

_1 imagem(ns) no slide._

### Slide 9

- Linux é um sistema operacional de código aberto, que permite que pessoas possam ter acesso ao seu código fonte, alterar via programação parte do sistema e redistribuir com características próprias.

_1 imagem(ns) no slide._

### Slide 10

- Diferentes sistemas Linux são chamados de distribuições. Sendo que o Ubuntu é uma delas, e também possui outras versões e novas distribuições, pois o código é aberto e permite que programadores reprogramem o sistema operacional.
- Professor(a), a partir das respostas, reforce que o Linux é um sistema operacional de código aberto (open source), que permite reprogramação do código fonte e desenvolvimento de novos sistemas operacionais.
- O Ubuntu é uma distribuição do Linux muito utilizada e que também possui outras distribuições.

_1 imagem(ns) no slide._

### Slide 11

- O que é um software open source?
- https://drive.google.com/file/d/1K2ekD-7hy4-OUW9eyqF8ASp2kAZlnfqX/view?usp=drive_link
- OBS: link do vídeo deve ser atualizado caso a apresentação mude de pasta junto com os vídeos

_2 imagem(ns) no slide._

### Slide 12

- Para responder
- O que é um software open source?
- Um software de código aberto pode ser reprogramado?
- O Ubuntu é um sistema operacional ou uma distribuição?
- Responda em seu caderno!

_2 imagem(ns) no slide._

### Slide 13

- Resposta
- 1. O que é um software open source?
- O termo open source refere-se a um tipo de software que tem seu código aberto, ou seja, um software que pode ser livremente adquirido por um programador e reeditado por ele, a fim de ser convertido em um sistema executável, como um sistema operacional, que controla um computador.

_1 imagem(ns) no slide._

### Slide 14

- Resposta
- 2. Um software de código aberto pode ser reprogramado?
- Exatamente isso. Um software do tipo open source pode ser reprogramado e o programador do sistema pode gerar uma nova versão ou, corretamente dizendo, um novo software, que no contexto de sistemas operacionais Linux são chamados de distribuição.

_1 imagem(ns) no slide._

### Slide 15

- Resposta
- 3. O Ubuntu é um sistema operacional ou uma distribuição?
- O Ubuntu é uma distribuição de um sistema operacional que utiliza o código aberto (open source) Linux.

_1 imagem(ns) no slide._

### Slide 16

- Open source é um modelo de desenvolvimento e distribuição de software, em que o código fonte (linhas de programação) é aberto, e pode ser revisado e reprogramado livremente por qualquer pessoa.

_1 imagem(ns) no slide._

### Slide 17

- Linux
- Com um projeto voltado para a criação de um sistema operacional que fosse de livre utilização e reprogramação, o projeto Linux surgiu com o apoio de diversos programadores.
- O resultado foi a criação de um novo sistema operacional, que podia ser copiado e reprogramado livremente.

_1 imagem(ns) no slide._

### Slide 18

- A origem do Linux
- O sistema operacional Linux é originário de um movimento de desenvolvimento de software de forma colaborativa liderado pelo finlandês Linus Torvalds.
- Em 1991, haviam diversos sistemas operacionais para computadores pessoais, como o UNIX, o MS-DOS, o Windows, o OS/2 da IBM, Amiga OS, MacOS da Apple, dentre outros.

_1 imagem(ns) no slide._

### Slide 19

- Linux Ubuntu
- É um sistema operacional baseado no código fonte do Linux, criado em 2004, com versões para servidores e para desktop (estações de trabalho).
- Oferece um instalador personalizado, ambiente de aplicativos para servidor e estações de trabalho.
- DESENVOLVIMENTO DE SISTEMAS

_2 imagem(ns) no slide._

### Slide 20

- Linux Ubuntu
- Arquitetura do Linux Ubuntu
- O sistema operacional Linux Ubuntu é formado por um núcleo do sistema chamado de Kernel, uma biblioteca de funções padrão, um Shell e aplicações.
- O núcleo do sistema possibilita:
- detecção de hardware;
- gerenciamento de entrada e saída de dados;
- gerenciamento do sistema de arquivos;
- gerenciamento de memória;
- controle de processos (programas em execução).

### Slide 21

- Linux Ubuntu
- A biblioteca de funções: permite acesso a recursos de hardware por meio de programas em execução.
- Shell: faz a leitura dos comandos do usuário ou programas acessados por ícones na interface gráfica e executa programas.
- Aplicações: são os programas oferecidos junto com o sistema operacional, como: editor de texto, planilha, browser de internet, calculadora.
- DESENVOLVIMENTO DE SISTEMAS

_4 imagem(ns) no slide._

### Slide 22

- Distribuições que fazem uso do Linux Ubuntu
- Assim como o Ubuntu é uma distribuição Linux, há também distribuições do sistema Ubuntu.
- Algumas distribuições são:
- Ubuntu Gnome.
- Ubuntu Mate.
- Kubuntu.
- Xbuntu.
- Ubuntu Studio.
- Ubuntu Mobile and Embedded Edition.
- DESENVOLVIMENTO DE SISTEMAS

_2 imagem(ns) no slide._

### Slide 23

- Vantagens no uso do sistema Linux Ubuntu
- Podem ser consideradas vantagens na utilização do Linux:
- gratuito;
- open source;
- atualizações rápidas;
- requisitos de hardware simples;
- personalizável;
- instalado em servidores e em estações de trabalho.
- DESENVOLVIMENTO DE SISTEMAS

_2 imagem(ns) no slide._

### Slide 24

- Desvantagens no uso do sistema Linux Ubuntu
- Podem ser consideradas desvantagens em utilizar um sistema Linux:
- dependência de linhas de comando para operação do sistema;
- incompatibilidade com alguns aplicativos;
- não há uma empresa responsável pelo código e sua manutenção;
- dependência de profissionais especializados;
- menor volume de programas aplicativos e jogos;
- performance.
- DESENVOLVIMENTO DE SISTEMAS

_2 imagem(ns) no slide._

### Slide 25

- Vamos Praticar?
- Vamos colocar em prática o que aprendemos desenvolvendo a atividade sugerida.

_1 imagem(ns) no slide._

### Slide 26

- https://rikerlinux.com.br/historia-do-linux/

_4 imagem(ns) no slide._

### Slide 27

- O que vimos na aula de hoje:
- Aprendemos que o Linux Ubuntu é um sistema operacional baseado em Linux..
- Aprendemos que o Linux Ubuntu pode ser instalado em servidores de rede e em desktops (estações de trabalho)..

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
- Bibliografia:
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
