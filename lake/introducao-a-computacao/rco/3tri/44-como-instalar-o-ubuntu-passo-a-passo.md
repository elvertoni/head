---
titulo: "Instalação Ubuntu"
tipo: rco-seed
disciplina: introducao-a-computacao
sigla_rco: IAC
trimestre: 3
ordem_rco: 44
serie: 1
aula_rco: "Aula 44"
slides: 38
tem_atividade: false
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/IAC/3TRI/44-como-instalar-o-ubuntu-passo-a-passo/44-como-instalar-o-ubuntu-passo-a-passo.pptx"
extrator: tools/extrair_rco.py
status: bruto
---

# Instalação Ubuntu

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- INTRODUÇÃO A COMPUTAÇÃO
- 1ª Série
- Instalação Ubuntu
- Aula 44

_1 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- Nesta aula vamos:
- Aprender como fazer a instalação de uma distribuição Linux Ubuntu.

_1 imagem(ns) no slide._

### Slide 4

- Este material foi elaborado com base na análise do plano de curso, abrangendo os conhecimentos essenciais para o curso Técnico em Desenvolvimento de Sistemas. Inclui aulas práticas desenvolvidas de acordo com as metodologias ativas, visando ao desenvolvimento de habilidades e competências de forma dinâmica e significativa. Você tem total liberdade para personalizar o material de acordo com seu contexto, otimizando o aproveitamento deste conteúdo.
- Em caso de falta ou indisponibilidade de acesso à internet no local de aula, você poderá utilizar os seguintes artigos para criação de material complementar para auxiliar na aula:
- ATENÇÃO PROFESSOR!

_1 imagem(ns) no slide._

### Slide 5

- Na aula anterior
- Revimos as principais características dos sistema operacional.

_1 imagem(ns) no slide._

### Slide 6

- INSTALAÇÃO DO LINUX
- Download da Imagem ISO do Linux
- O primeiro passo para a instalação do Ubuntu 18.04 é realizar o download do arquivo de instalação em formato ISO.
- Você pode baixar a imagem ISO do Ubuntu 18.04 LTS aqui.

_1 imagem(ns) no slide._

> **Notas do apresentador:** http://releases.ubuntu.com/18.04/

### Slide 7

- Criando um pen drive bootável de qualquer distribuição Linux no Windows com o Rufus
- Para criar o pen drive bootável, vamos utilizar o Rufus.
- Baixe o programa Rufus, que permite a criação de drives USB inicializáveis de maneira muito fácil, clicando nesse link.
- Insira o pen drive na porta USB do seu notebook ou computador.

_1 imagem(ns) no slide._

### Slide 8

- Criando um pen drive bootável de qualquer distribuição Linux no Windows com o Rufus
- Clique em **Sim**

_4 imagem(ns) no slide._

### Slide 9

- A seguir, aparecerá outra janela, solicitando permissões para que o aplicativo procure atualizações na internet e então clique em **Sim**.
- Clique no botão SELECIONAR, selecione a imagem ISO do Ubuntu 18.04, depois, clique no botão Abrir e no botão INICIAR.
- Quando tudo estiver pronto, clique em FECHAR.

_1 imagem(ns) no slide._

### Slide 10

- Fazendo o boot pelo pen drive
- DESENVOLVIMENTO DE SISTEMAS
- Agora que já tem o pen drive bootável criado, reinicie a máquina clicando no menu Iniciar, que fica no canto inferior esquerdo, clique em Ligar /Desligar e depois, em Reiniciar.

_1 imagem(ns) no slide._

### Slide 11

- Fazendo o boot pelo pen drive
- Pressione várias vezes a tecla F2 até aparecer a tela principal da BIOS (Isso dependerá do fabricante da sua placa-mãe. Cada um escolhe uma tecla, ou uma combinação de teclas, que melhor lhe convém. Geralmente as teclas F1, F2, F10, DEL, ESC e as combinações CTRL + ALT + ESC ou CTRL + ALT + DEL são utilizadas para acessar o BIOS, mas às vezes elas são utilizadas para outras coisas também). Nesse caso a tecla para ter acesso à BIOS do notebook utilizado é um (Dell Inspiron I15 5000 5458) é F2.
- DESENVOLVIMENTO DE SISTEMAS

_3 imagem(ns) no slide._

### Slide 12

- Fazendo o boot pelo pen drive
- Nesse caso a tecla para ter acesso à BIOS do notebook utilizado (Dell Inspiron I15 5000 5458) é um (Dell Inspiron I15 5000 5458) é F2.

_3 imagem(ns) no slide._

### Slide 13

- Fazendo o boot pelo pen drive
- Na tela da BIOS, selecione a opção Boot Sequence.

_2 imagem(ns) no slide._

### Slide 14

- Fazendo o boot pelo pen drive
- Na próxima tela que aparece, deixe marcado a opção Legacy e coloque em primeiro lugar a opção USB Storage Device.

_2 imagem(ns) no slide._

### Slide 15

- Fazendo o boot pelo pen drive
- Clique em Apply para aplicar as alterações.

_2 imagem(ns) no slide._

### Slide 16

- Fazendo o boot pelo pen drive
- Para concluir, clique em Exit.

_2 imagem(ns) no slide._

### Slide 17

- Fazendo o boot pelo pen drive
- Depois que o sistema é inicializado usando o pen drive bootável, você pode ver a tela a seguir apresentada com opções incluindo Teste o Ubuntu e Instalar o Ubuntu, como mostra a imagem abaixo.

_1 imagem(ns) no slide._

### Slide 18

- Fazendo o boot pelo pen drive
- Clique em Instalar o Ubuntu para continuar com o processo de instalação.
- OBS: Cuidado! Você aqui irá apagar todos os dados e sistemas já instalados, faça isso em um computador que não seja utilizado posteriormente.

_1 imagem(ns) no slide._

### Slide 19

- Fazendo o boot pelo pen drive
- Escolha o seu layout do teclado favorito e clique em Continuar (No meu caso vou escolher Português Brasil).

_1 imagem(ns) no slide._

### Slide 20

- Fazendo o boot pelo pen drive
- Na próxima tela, você verá as opções abaixo, incluindo:
- Tipo de instalação: Instalação normal ou instalação mínima. Se você deseja uma instalação mínima, selecione a segunda opção, caso contrário, vá para a instalação normal. No meu caso, estou fazendo a instalação normal.

_1 imagem(ns) no slide._

### Slide 21

- Fazendo o boot pelo pen drive
- Baixar atualizações durante a instalação do Ubuntu (selecione esta opção se o seu sistema tiver conectividade com a Internet durante a instalação).
- Instalar software de terceiros para hardware gráfico e Wi-Fi, MP3 e formatos de mídia adicionais Selecione esta opção se o seu sistema tiver conectividade à Internet). E clique em Continuar para proceder com a instalação.

_1 imagem(ns) no slide._

### Slide 22

- Fazendo o boot pelo pen drive
- Em seguida, o instalador apresenta as seguintes opções de instalação, incluindo:
- Apague o disco e instale o Ubuntu
- Criptografar a nova instalação do Ubuntu por segurança
- Utilize o LVM com a nova instalação do Ubuntu
- Algo mais
- DESENVOLVIMENTO DE SISTEMAS

_2 imagem(ns) no slide._

### Slide 23

- Fazendo o boot pelo pen drive
- Apagar disco e instalar o Ubuntu - Escolha esta opção se o seu sistema tiver apenas o Ubuntu e apagar qualquer outra coisa que não seja um problema. Isso garante que uma nova cópia do Ubuntu 18.04 LTS seja instalada no seu sistema.
- Criptografar a nova instalação do Ubuntu para segurança - Escolha essa opção se você estiver procurando por segurança estendida para seus discos, pois eles serão completamente criptografados. Se você é iniciante, é melhor não se preocupar com essa opção.
- DESENVOLVIMENTO DE SISTEMAS

_3 imagem(ns) no slide._

### Slide 24

- Fazendo o boot pelo pen drive
- Utilize o LVM com a nova instalação do Ubuntu - Escolha esta opção se desejar utilizar sistemas de arquivos baseados em LVM.
- Opção avançada - Escolha essa opção se você for um usuário avançado e quiser criar manualmente suas próprias partições e quiser instalar o Ubuntu junto com o sistema operacional existente (pode ser Windows ou outra distribuição do Linux).
- DESENVOLVIMENTO DE SISTEMAS

_3 imagem(ns) no slide._

### Slide 25

- Fazendo o boot pelo pen drive
- Para particionar o HD, selecione Opção avançada, e clique em Continuar.

_2 imagem(ns) no slide._

### Slide 26

- Fazendo o boot pelo pen drive
- Você pode ver o tamanho do disco disponível para o Ubuntu na próxima janela.
- Agora, para criar suas próprias partições, clique em Nova Tabela de Partições.

_2 imagem(ns) no slide._

### Slide 27

- Fazendo o boot pelo pen drive
- Vai aparecer uma mensagem, clique em Continuar.
- Selecione o espaço livre e clique no símbolo "+" para criar uma nova partição.
- Em Editar partição, defina o Tamanho que você desejar para a instalação do Ubuntu, selecione Usar como: Sistema de arquivos ext4, Formatar partição e Ponto de montagem: /

_2 imagem(ns) no slide._

### Slide 28

- Fazendo o boot pelo pen drive
- Depois, clique em OK.
- Crie uma pequena partição de 4GB como o Swap área.

_2 imagem(ns) no slide._

### Slide 29

- Fazendo o boot pelo pen drive
- Escolha seu fuso horário favorito e sua localidade, depois clique em Continuar.

_2 imagem(ns) no slide._

### Slide 30

- Fazendo o boot pelo pen drive
- Na próxima tela que aparece, crie seu usuário e sua senha.

_2 imagem(ns) no slide._

### Slide 31

- Fazendo o boot
- pelo pen drive
- A instalação do Ubuntu 18.04 LTS começa agora e leva cerca de 5 a 10 minutos, dependendo da velocidade do seu computador.

_2 imagem(ns) no slide._

### Slide 32

- Fazendo o boot pelo pen drive
- Quando a instalação estiver concluída, remova o pen drive da maquina e clique em Reiniciar agora para reiniciar o sistema.

_2 imagem(ns) no slide._

### Slide 33

- Fazendo o boot pelo pen drive
- Depois que o sistema for reiniciado após a instalação, você verá a tela de login, digite o nome de usuário e a senha que você definiu durante a instalação.

_2 imagem(ns) no slide._

### Slide 34

- Vamos Praticar?
- Vamos colocar em prática o que aprendemos desenvolvendo a atividade sugerida.

_1 imagem(ns) no slide._

### Slide 35

- O que vimos na aula de hoje:
- Aprendemos como realizar uma instalação de uma distribuição Linux Ubuntu passo a passo.
- Aprendemos que para realizar esse procedimento todos os dados do computador serão apagados, portanto tome cuidado, faça backup antes.
- DESENVOLVIMENTO DE SISTEMAS

_2 imagem(ns) no slide._

### Slide 36

- Pronto para desbloquear sua carreira de TI?
- Está perdido estudando mas não sabe por onde começar? Se a resposta é sim, você está no lugar certo! Descubra as estratégias e ferramentas essenciais para te ajudar a desbloquear seu potencial em TI e buscar sua primeira vaga de emprego no setor!
- Este e-book é um guia completo para quem busca começar pelos melhores caminhos para se tornar um excelente profissional de TI, ensinando a identificar perfis profissionais, aplicar técnicas de estudo eficazes, transformar teoria em prática, e aumentar a visibilidade de seu trabalho no mercado de trabalho. Ideal para novatos e profissionais em transição.
- E o melhor, ele pode ser seu, inteiramente grátis!
- Basta clicar AQUI e realizar o seu cadastro com o seu @escola!

_3 imagem(ns) no slide._

### Slide 37

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

### Slide 38

_(sem texto)_
