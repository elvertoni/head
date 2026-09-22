---
titulo: "Parte I"
tipo: rco-seed
disciplina: introducao-a-computacao
sigla_rco: IAC
trimestre: 2
ordem_rco: 27
serie: 1
aula_rco: "Aula 27"
slides: 22
tem_atividade: true
tem_pratica: true
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/IAC/2TRI/27-o-processo-de-execucao-de-programas-pelo-computador-parte-i/27-o-processo-de-execucao-de-programas-pelo-computador-parte-i.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/IAC/2TRI/27-o-processo-de-execucao-de-programas-pelo-computador-parte-i/AULA 27_PRÁTICA INTRODUÇÃO A COMPUTAÇÃO.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/IAC/2TRI/27-o-processo-de-execucao-de-programas-pelo-computador-parte-i/AULA 27_INTRODUÇÃO A COMPUTAÇÃO ATIVIDADE.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Parte I

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- INTRODUÇÃO A COMPUTAÇÃO
- 1ª SÉRIE
- O Processo de Execução de Programas pelo Computador
- Parte I
- Aula 27

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
- Aprender sobre o processo de Execução de Programas pelo Computador - Parte I

_7 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Na aula anterior...
- Compreendemos com o computador faz a leitura de códigos e entendemos a diferença entre interpretadores e compiladores.

_4 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Maria acaba de comprar seu primeiro computador e está animada para começar a usar. No entanto, ao começar a instalar programas e salvar arquivos, ela percebe que o espaço no disco rígido do computador está sendo rapidamente consumido.
- Ela começa a se perguntar sobre o conceito de armazenamento em um computador e como pode gerenciar melhor o espaço disponível.

_4 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- O que é armazenamento em um computador e como ela poderá gerenciar melhor o espaço de armazenamento?
- Realizem a atividade em duplas e socializem no final!

_5 imagem(ns) no slide._

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- O armazenamento em um computador refere-se ao espaço disponível para guardar dados, como programas e arquivos.
- Existem diferentes tipos de armazenamento, como a memória RAM, que é temporária e usada para dados em uso ativo, e o disco rígido ou SSD, que é um armazenamento de longo prazo para arquivos e programas.

_4 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- O armazenamento de um computador se refere ao local onde os dados são guardados para uso posterior. Isso inclui todos os arquivos, programas, documentos, fotos, músicas, filmes e o sistema operacional. Há diferentes tipos de armazenamento, incluindo a memória de acesso aleatório (RAM), o disco rígido (HDD) ou a unidade de estado sólido (SSD).

_4 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- A RAM é uma forma de armazenamento temporário que permite ao computador acessar rapidamente os dados necessários para as tarefas em execução. Quando você desliga o computador, os dados na RAM são apagados. Por outro lado, o HDD ou SSD são formas de armazenamento de longo prazo. Eles mantêm os dados mesmo quando o computador está desligado.

_4 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- O espaço de armazenamento disponível em um computador tem um grande impacto em sua utilização. Se o disco rígido ou a unidade de estado sólido estiverem quase cheios, o computador pode funcionar mais lentamente, pois terá menos espaço para mover e gerenciar os arquivos.
- Além disso, se a RAM estiver cheia, o computador terá dificuldade em manter muitos programas abertos ao mesmo tempo, o que pode levar a um desempenho mais lento ou travamentos.

_4 imagem(ns) no slide._

### Slide 13

- DESENVOLVIMENTO DE SISTEMAS
- É importante gerenciar o espaço de armazenamento do seu computador, mantendo apenas os arquivos e programas necessários, limpando regularmente os arquivos temporários e considerando soluções de armazenamento externo ou em nuvem se precisar de mais espaço. Ao fazer isso, você pode manter seu computador funcionando de maneira eficiente e evitar problemas de desempenho.

_4 imagem(ns) no slide._

### Slide 14

- DESENVOLVIMENTO DE SISTEMAS
- Para responder
- Discutam em duplas e socializem as ideias com a turma no final!
- Por que é importante gerenciar o espaço de armazenamento em um computador?

_5 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Gerenciar o espaço de armazenamento de um computador é importante por várias razões…
- Em primeiro lugar, um computador com muito pouco espaço de armazenamento disponível pode funcionar mais lentamente, pois tem menos espaço para mover e gerenciar arquivos. Isso pode levar a um desempenho mais lento e até mesmo a travamentos do sistema.

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
- Preparem-se para criar arquivos, decidir o que vai para a memória rápida (RAM), o que deve ser guardado com segurança (Disco Rígido), e o que está só ocupando espaço e precisa ser jogado fora (Lixeira)!
- Hoje, você e sua equipe vão entrar no mundo secreto da tecnologia e se transformar nos gestores de memória de um supercomputador!

_4 imagem(ns) no slide._

> **Notas do apresentador:** Atividade: Entendendo o Armazenamento de Arquivos em um Computador Objetivo: Compreender, de forma prática e lúdica, como o computador organiza e gerencia seus arquivos utilizando a memória RAM, o Disco Rígido e a Lixeira. Materiais necessários: Papéis pequenos (representando arquivos) Canetas ou lápis de cor Caixa grande (Disco Rígido) Mesa pequena (RAM) Cesta (Lixeira) Passo a passo: Formação dos Grupos: Divida os participantes em pequenos grupos. Criação dos Arquivos: Entregue a cada grupo uma pilha de papéis e canetas. Peça que criem diferentes tipos de "arquivos", escrevendo ou desenhando nos papéis. Eles podem representar documentos, imagens, vídeos, etc. Organização dos Arquivos: Após a criação, oriente os grupos a selecionar quais arquivos precisam ser "abertos" ou utilizados no momento. Esses arquivos devem ser colocados sobre a mesa pequena, simbolizando a memória RAM (armazenamento temporário). Os demais arquivos devem ser guardados dentro da caixa grande, que representa o Disco Rígido (armazenamento permanente). Gerenciamento de Espaço: Apresente a cesta como a "Lixeira" do computador. Explique que, quando a RAM ou o Disco Rígido ficam muito cheios, é necessário escolher arquivos menos importantes para serem descartados. Esses papéis devem ser colocados na cesta. Discussão Final: Conduza uma conversa com os participantes sobre o que a dinâmica representou: Como a memória RAM armazena temporariamente arquivos em uso. Como o Disco Rígido guarda arquivos de forma mais duradoura. A importância da organização e do descarte de arquivos desnecessários para manter o bom funcionamento do computador.

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- Vamos Praticar?
- Vamos agora colocar em prática o que aprendemos desenvolvendo a atividade sugerida.

_4 imagem(ns) no slide._

> **Notas do apresentador:** Link da atividade: https://docs.google.com/document/d/1pj4iIv73WpIzcQOHGF3xPiRgiW6Zu4tO/edit?usp=drive_link&ouid=112660820765629457253&rtpof=true&sd=true

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje
- Compreendemos sobre armazenamento de computadores e como ele impacta em sua utilização.

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

_3 imagem(ns) no slide._

### Slide 22

- DESENVOLVIMENTO DE SISTEMAS
- O RCO+Aulas é um projeto da Secretaria de Estado da Educação do Paraná e está em constante revisão. Todos os slides são de uso exclusivo dos professores da Rede Pública de Ensino, com a finalidade específica de aplicação em sala de aula, sendo totalmente vedada a publicização, reutilização, reprodução total ou parcial para quaisquer outros fins.

_4 imagem(ns) no slide._

## Atividade

_Fonte: AULA 27_INTRODUÇÃO A COMPUTAÇÃO ATIVIDADE.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

INTRODUÇÃO A COMPUTAÇÃO

1ª SÉRIE

ATIVIDADE AULA 27

Questão 1

O que acontece quando a RAM de um computador está quase cheia?

a) O computador se desliga automaticamente.

b) O computador não será capaz de salvar novos arquivos.

c) O computador pode funcionar mais lentamente e ter dificuldade em manter muitos programas abertos ao mesmo tempo.

d) O computador começará a deletar arquivos aleatórios para liberar espaço.

Resposta correta: c) Quando a RAM de um computador está quase cheia, o computador pode funcionar mais lentamente e ter dificuldade em manter muitos programas abertos ao mesmo tempo. A RAM é usada para armazenamento temporário de dados que estão em uso ativo. Se a RAM estiver cheia, o computador terá que trabalhar mais para gerenciar esses dados, o que pode levar a um desempenho mais lento.

Questão 2

Qual das seguintes ações NÃO ajudaria a gerenciar melhor o espaço de armazenamento em um computador?

a) Desinstalar programas que não são mais necessários.

b) Limpar regularmente os arquivos temporários.

c) Salvar todos os arquivos e programas no disco rígido do computador.

d) Considerar o uso de serviços de armazenamento em nuvem.

Resposta correta: c) Salvar todos os arquivos e programas no disco rígido do computador. Embora possa parecer uma boa ideia manter todos os seus arquivos e programas em um só lugar para fácil acesso, fazer isso pode levar a um desempenho mais lento do computador se o disco rígido estiver quase cheio. É importante gerenciar o espaço de armazenamento, mantendo apenas os arquivos e programas necessários no disco rígido e considerando outras soluções de armazenamento, como armazenamento em nuvem ou externo, se precisar de mais espaço.

## Prática

_Fonte: AULA 27_PRÁTICA INTRODUÇÃO A COMPUTAÇÃO.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

INTRODUÇÃO A COMPUTAÇÃO

1ª SÉRIE

AULA PRÁTICA 27

Resumo Explicativo:

O processo de execução de programas pelo computador é uma sequência de etapas que transforma o código fonte escrito por programadores em ações executadas pela máquina. Esse processo envolve a tradução do código (por compiladores ou interpretadores), a alocação na memória RAM, o carregamento de instruções pela CPU, e a realização das operações necessárias. Compreender essas etapas ajuda o estudante a entender como funciona “por dentro” o sistema que ele está desenvolvendo, permitindo otimizações e diagnósticos mais eficazes.

Estudo de Caso:

Cenário:

Durante uma aula prática, o professor propôs aos alunos a criação de um programa que soma dois números digitados pelo usuário. A aluna Júlia escreveu o código em C e compilou sem erros. Mas ficou com uma dúvida:

“Como o computador entende o que escrevi e executa isso tão rápido?”

O professor decidiu aproveitar o momento para explicar passo a passo o que ocorre quando um programa é executado:

- O código-fonte é convertido em linguagem de máquina por um compilador.
- O sistema operacional aloca espaço na memória RAM para o programa.
- A CPU lê as instruções, uma a uma, a partir do registrador de instrução.
- A execução ocorre através de ciclos de busca, decodificação e execução.
Júlia e sua turma foram desafiados a criar uma linha do tempo visual com as etapas do processo de execução, destacando o papel da CPU, da RAM, do sistema operacional e dos arquivos executáveis.

Questões:

- Quais são as três etapas principais do ciclo de execução da CPU durante a execução de um programa?
- Explique com suas palavras como o sistema operacional colabora com a CPU no processo de execução de um programa.
- Suponha que você escreveu um programa que imprime "Olá, mundo!" em C. Quais etapas ocorrem desde o momento da escrita até o momento da exibição da frase na tela?
- Analise as funções do compilador, da RAM e da CPU no processo de execução. Como elas se relacionam entre si para que o programa funcione?
- Na sua opinião, é mais vantajoso programar em uma linguagem compilada ou interpretada quando o objetivo é velocidade de execução? Justifique sua resposta.
- Desenvolva um infográfico ou vídeo curto explicativo que mostre visualmente as etapas que ocorrem desde o código-fonte até a execução final no computador.
