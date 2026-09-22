---
titulo: "Windows 10 - Entendendo sua Arquitetura"
tipo: rco-seed
disciplina: introducao-a-computacao
sigla_rco: IAC
trimestre: 2
ordem_rco: 39
serie: 1
aula_rco: "Aula 39"
slides: 27
tem_atividade: true
tem_pratica: true
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/IAC/2TRI/39-windows-10-entendendo-sua-arquitetura/39-windows-10-entendendo-sua-arquitetura.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/IAC/2TRI/39-windows-10-entendendo-sua-arquitetura/AULA 39_INTRODUÇÃO A COMPUTAÇÃO ATIVIDADE.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/IAC/2TRI/39-windows-10-entendendo-sua-arquitetura/AULA 39_PRÁTICA INTRODUÇÃO A COMPUTAÇÃO.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Windows 10 - Entendendo sua Arquitetura

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- INTRODUÇÃO A COMPUTAÇÃO
- 1ª SÉRIE
- Windows 10 - Entendendo sua Arquitetura
- Aula 39

_3 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- DESENVOLVIMENTO DE SISTEMAS
- Nesta aula, vamos:
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store
- Compreender a arquitetura básica do sistema operacional Windows 10.

_7 imagem(ns) no slide._

### Slide 4

- DESENVOLVIMENTO DE SISTEMAS
- Este material foi elaborado com base na análise do plano de curso, abrangendo os conhecimentos essenciais para o curso Técnico em Desenvolvimento de Sistemas. Inclui aulas práticas desenvolvidas de acordo com as metodologias ativas, visando ao desenvolvimento de habilidades e competências de forma dinâmica e significativa. Você tem total liberdade para personalizar o material de acordo com seu contexto, otimizando o aproveitamento deste conteúdo.
- Em caso de falta ou indisponibilidade de acesso à internet no local de aula, você poderá utilizar os seguintes artigos para criação de material complementar para auxiliar na aula:
- Para saber mais: Lei de Moore:
- https://cursos.alura.com.br/course/arquitetura-computadores-funcionamento-programa/task/86311
- ATENÇÃO PROFESSOR!

_5 imagem(ns) no slide._

### Slide 5

- DESENVOLVIMENTO DE SISTEMAS
- Na aula anterior...
- Aprendemos as principais características de um sistema operacional.

_4 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Para nos comunicarmos com as pessoas usamos uma certa linguagem…
- Quando usamos um computador ele precisa “entender” o que queremos fazer, ou seja, é preciso uma linguagem específica para que ele nos entenda. Essa linguagem é chamada de Sistema Operacional.
- Considerando os dias atuais, há uma diversidade relativamente grande de sistemas operacionais que podem ser utilizados junto a dispositivos computacionais.

_3 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Há sistemas operacionais específicos para:
- ● Supercomputadores
- ● Servidores de rede de computadores
- ● Computadores pessoais
- ● Smartphones
- ● Dispositivos de Internet das Coisas

_4 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Quais são os sistemas operacionais mais utilizados para computadores pessoais, considerando os desktops e notebooks?
- Realizem a atividade em duplas e socializem no final!
- Há outros sistemas operacionais diferentes do Microsoft Windows para equipar os desktops e notebooks?
- E para controlar os smartphones, quais são os sistemas operacionais utilizados?

_6 imagem(ns) no slide._

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Windows 10 e 11 para os desktops e notebooks.
- Há versões diversificadas do Linux, um sistema operacional que nos anos 2020 pode ser considerado muito avançado e com interface bastante atrativa, mesmo para usuários leigos em ciência da computação.
- Os mais conhecidos são o Android
- da Google e o iOS da Apple.

_4 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- Considere que você irá instalar um jogo no seu computador, mas ele ficou muito lento e pesado. Ao conferir o tipo de sistema, descobriu que é 32 bits. Um dos requisitos do jogo é que o tipo de sistema seja de 64 bits. A solução seria atualizar o sistema operacional para o Windows 10 que possui o tipo de sistema de 64 bits.

_4 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Ao falar em sistemas operacionais, é muito comum já direcionarmos o pensamento para a palavra Windows!
- O Windows é um sistema operacional criado em 1983 e possui diversas versões que foram modificadas e atualizadas ao longo do tempo, trazendo cada vez mais facilidades aos usuários. Atualmente, a versão mais utilizada é a 10.
- Este é um sistema utilizado em computadores pessoais do tipo desktop e notebook, assim como, possui versões para outros dispositivos, como os smartphones.

_4 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- Considerando que o Microsoft Windows 10 é um sistema operacional para computadores do tipo IBM PC, tecnicamente utiliza um tipo de arquitetura de hardware chamada de CISC (Complex Instructions Set Computer), utilizada em computadores com plataformas do tipo x86 (computadores pessoais) dentre outras como X64, ARM e ARM64.
- x86 é uma arquitetura com processamento de 32 bits, e, X64 refere-se a 64bits, mas que suporta aplicações mais antigas de 32 bits.
- Resumindo: 32 bits e 64 bits indicam a arquitetura do sistema operacional.

_4 imagem(ns) no slide._

### Slide 13

- DESENVOLVIMENTO DE SISTEMAS
- Qual sistema operacional que normalmente é utilizado em computadores pessoais que você conhece?
- O Windows 10 é um sistema operacional para que tipo de computador?
- Para Responder

_5 imagem(ns) no slide._

### Slide 14

- DESENVOLVIMENTO DE SISTEMAS
- Windows que é um sistema operacional para computadores pessoais (desktops e notebooks) muito utilizado na atualidade.
- o Windows 10 é um sistema operacional para ser utilizado em computadores do tipo IBM PC, originário da IBM que ficou conhecido como computador pessoal.
- Resposta

_4 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- Quando instalamos um programa no computador que tem o Windows 10 como sistema operacional, muitas vezes é preciso escolher entre duas siglas: 32 bits e 64 bits.
- Você sabe o que significa?

_4 imagem(ns) no slide._

### Slide 16

- DESENVOLVIMENTO DE SISTEMAS
- Arquitetura de 32 ou 64 bits
- Link: https://drive.google.com/file/d/1DZfK8L3jJGAF67m1s5ylO9MgmQlduq9x/view?usp=drive_link
- OBS: link do vídeo deve ser atualizado caso a apresentação mude de pasta junto com os vídeos

_5 imagem(ns) no slide._

### Slide 17

- DESENVOLVIMENTO DE SISTEMAS
- Para Responder
- Falando sobre arquitetura de processamento…
- Qual permite maior performance no Windows 10?
- Responda em seu caderno!

_5 imagem(ns) no slide._

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- O Windows 10 suporta dois tipos de arquitetura de processamento de dados: 32 bits, e 64 bits, sendo que há maior aproveitamento de memória e maior performance com a utilização de processamento em 64 bits.

_4 imagem(ns) no slide._

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- Antes de falarmos sobre arquitetura do sistema operacional, precisamos compreender dois tipos de arquitetura de processadores.
- ● Arquitetura RISC (Reduced Instructions Set Computer)
- ● Arquitetura CISC (Complex Instructions Set Computer)

_4 imagem(ns) no slide._

### Slide 20

- DESENVOLVIMENTO DE SISTEMAS
- Esta arquitetura previa que um processador teria um conjunto reduzido de instruções para executar o processamento de dados.
- Arquitetura utilizada por processadores do tipo SPARC e ARM e outros disponíveis em dispositivos como IPod, IPhone, videogames.
- Arquitetura RISC
- (Reduced Instructions Set Computer)

_4 imagem(ns) no slide._

### Slide 21

- DESENVOLVIMENTO DE SISTEMAS
- Esta arquitetura previa que um processador teria um conjunto complexo de instruções para executar o processamento de dados.
- Arquitetura utilizada por processadores do tipo Intel X86 e seus sucessores como Pentium e AMD que equipam os computadores pessoais da atualidade.
- Arquitetura CISC
- (Complex Instructions Set Computer)

_4 imagem(ns) no slide._

### Slide 22

- DESENVOLVIMENTO DE SISTEMAS
- Computadores pessoais são originários da década de 1970 e tiveram uma grande evolução durante os anos 1980, quando dispositivos foram projetados para ser utilizados por usuários leigos, junto a um computador desenvolvido com uma plataforma chamada de x86, que vem evoluindo nos últimos 50 anos.
- De forma geral, a arquitetura dos computadores pessoais é baseada em uma arquitetura de processamento CISC, e que é utilizada em microprocessadores da grande maioria dos computadores do tipo pessoal na atualidade.

_4 imagem(ns) no slide._

### Slide 23 (oculto)

- DESENVOLVIMENTO DE SISTEMAS
- Vamos Praticar?
- Vamos agora colocar em prática o que aprendemos desenvolvendo a atividade sugerida.

_4 imagem(ns) no slide._

### Slide 24

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje
- Aprendemos que o Microsoft Windows 10 pode ser instalado em versões de 32 bits e de 64 bits.

_4 imagem(ns) no slide._

### Slide 25

- DESENVOLVIMENTO DE SISTEMAS
- Pronto para desbloquear sua carreira de TI?
- Está perdido estudando mas não sabe por onde começar? Se a resposta é sim, você está no lugar certo! Descubra as estratégias e ferramentas essenciais para te ajudar a desbloquear seu potencial em TI e buscar sua primeira vaga de emprego no setor!
- Este e-book é um guia completo para quem busca começar pelos melhores caminhos para se tornar um excelente profissional de TI, ensinando a identificar perfis profissionais, aplicar técnicas de estudo eficazes, transformar teoria em prática, e aumentar a visibilidade de seu trabalho no mercado de trabalho. Ideal para novatos e profissionais em transição.
- E o melhor, ele pode ser seu, inteiramente grátis!
- Basta clicar AQUI e realizar o seu cadastro com o seu @escola!

_6 imagem(ns) no slide._

### Slide 26

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

### Slide 27

- DESENVOLVIMENTO DE SISTEMAS
- O RCO+Aulas é um projeto da Secretaria de Estado da Educação do Paraná e está em constante revisão. Todos os slides são de uso exclusivo dos professores da Rede Pública de Ensino, com a finalidade específica de aplicação em sala de aula, sendo totalmente vedada a publicização, reutilização, reprodução total ou parcial para quaisquer outros fins.

_4 imagem(ns) no slide._

## Atividade

_Fonte: AULA 39_INTRODUÇÃO A COMPUTAÇÃO ATIVIDADE.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

INTRODUÇÃO A COMPUTAÇÃO

1ª SÉRIE

ATIVIDADE AULA 39

Questão 1

Os sistemas operacionais são softwares de base, com o objetivo de controlar o hardware e que necessitam ser programados com as tecnologias compatíveis às arquiteturas de processamento de dados dos processadores dos computadores. Sendo assim, considera-se que a correta arquitetura utilizada em computadores pessoais é denominada

a) CISC (Complex Instructions Set Computer).

b) RISC (Reduced Instructions Set Computer).

c) DISC (Distributed Instructions Set Computer).

d) GISC (Graphic Instructions Set Computer).

Resposta comentada: CISC (Complex Instructions Set Computer), é a arquitetura que previa que um processador teria um conjunto complexo de instruções para executar o processamento de dados. Utilizada por processadores do tipo Intel X86 e seus sucessores como Pentium e AMD. Arquitetura RISC (Reduced Instructions Set Computer), é a arquitetura previa que um processador teria um conjunto reduzido de instruções para executar o processamento de dados, a utilizada por processadores do tipo SPARC e ARM e outros disponíveis em dispositivos como IPod, IPhone, videogames. Os termos DISC e GIST não existem nas definições de arquiteturas.

Questão 2

Ao instalar um programa no seu computador, apareceu duas opções de arquitetura de processamento de dados. Considerando o Microsoft Windows 10, qual a arquitetura de processamento de dados que oferece maior performance para computadores pessoais?

a) Arquitetura de 8 bits.

b) Arquitetura de 16 bits.

c) Arquitetura de 32 bits.

d) Arquitetura de 64 bits.

Resposta comentada: Sistemas operacionais que operam em 32 bits estão limitados a suportar o uso de memória RAM (Random Access Memory), a famosa memória que utilizamos para guardar e executar os programas quando o computador está em funcionamento, no volume de 4 GB, sendo que não há espaço para um maior volume de programas serem trabalhados pelo sistema operacional. Já os processadores que operam em 64 bits, mais recentes, podem processar programas utilizando toda a memória RAM do computador, sem limites. Temos então uma arquitetura que consegue executar de forma mais eficiente um maior volume de programas, o que deixa o nosso computador com maior capacidade de processamento e então, mais veloz. Sistemas operacionais com arquitetura de 8 e 16 bits estão em desuso.

## Prática

_Fonte: AULA 39_PRÁTICA INTRODUÇÃO A COMPUTAÇÃO.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

INTRODUÇÃO A COMPUTAÇÃO

1ª SÉRIE

AULA PRÁTICA 39

Resumo Explicativo:

O Windows 10 é um dos sistemas operacionais mais utilizados no mundo, e sua arquitetura foi projetada para oferecer desempenho, segurança e compatibilidade com uma ampla variedade de dispositivos. Ela é composta por camadas e componentes que trabalham juntos, como o Kernel, os drivers, os serviços do sistema, a interface gráfica, e as APIs que permitem que softwares se comuniquem com o hardware. Compreender essa arquitetura é fundamental para desenvolvedores que desejam criar aplicativos compatíveis e otimizados.

Estudo de Caso:

Cenário:

Daniel, aluno do terceiro ano do curso técnico em desenvolvimento de sistemas, começou a criar um software que precisa se comunicar com dispositivos USB e acessar arquivos do sistema. Durante o desenvolvimento, ele percebeu que o Windows 10 oferece APIs e serviços específicos que controlam permissões e interações com o hardware.

Ao pesquisar mais, Daniel descobriu que:

- O Kernel é o núcleo que gerencia recursos e controla os processos.
- Os drivers permitem que o sistema operacional converse com o hardware.
- Os serviços do sistema executam tarefas em segundo plano.
- A interface gráfica (explorer.exe) é separada do Kernel e pode ser reiniciada sem reiniciar o sistema inteiro.
Com essas informações, ele entendeu que seu software precisa usar permissões corretas e interagir com as APIs do Windows para funcionar de forma segura e estável.

O desafio do projeto foi criar um diagrama mostrando como seu aplicativo interage com cada camada da arquitetura do Windows 10, desde o clique do usuário até a comunicação com o dispositivo USB.

Questões

- Liste quatro componentes principais da arquitetura do Windows 10.
- Explique com suas palavras qual é a função do Kernel no Windows 10 e por que ele é considerado o núcleo do sistema.
- Imagine que você quer criar um programa que exibe informações da CPU em tempo real. Quais partes da arquitetura do Windows 10 você precisará acessar ou usar?
- Analise como os drivers e os serviços do sistema trabalham juntos para garantir que os dispositivos de hardware funcionem corretamente no Windows 10.
- Você acha que separar a interface gráfica (explorer.exe) do Kernel é uma boa decisão de arquitetura? Justifique sua resposta considerando segurança e estabilidade.
- Desenvolva um fluxograma que mostre os passos que acontecem no Windows 10 quando um usuário conecta um pendrive, incluindo quais componentes da arquitetura são envolvidos em cada etapa.
