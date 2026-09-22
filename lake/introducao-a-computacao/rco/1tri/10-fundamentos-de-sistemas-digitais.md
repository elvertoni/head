---
titulo: "Fundamentos de Sistemas Digitais"
tipo: rco-seed
disciplina: introducao-a-computacao
sigla_rco: IAC
trimestre: 1
ordem_rco: 10
serie: 1
aula_rco: "Aula 10"
slides: 27
tem_atividade: true
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/IAC/1TRI/10-fundamentos-de-sistemas-digitais/10-fundamentos-de-sistemas-digitais.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/IAC/1TRI/10-fundamentos-de-sistemas-digitais/AULA 10_INTRODUÇÃO A COMPUTAÇÃO ATIVIDADE.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Fundamentos de Sistemas Digitais

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- INTRODUÇÃO A COMPUTAÇÃO
- 1ª SÉRIE
- Fundamentos de Sistemas Digitais
- Aula 10

_3 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- COMPETÊNCIA(S) A SER(EM) DESENVOLVIDA(S) NESTA AULA:
- De acordo com o Plano de Curso de Desenvolvimento de Sistemas:
- HABILIDADE(S) A SER(EM) DESENVOLVIDA(S) NESTA AULA:
- Desenvolver sistemas computacionais utilizando ambiente de desenvolvimento.
- Reconhecer tipos e características (classificação, estrutura e modelos).

_1 imagem(ns) no slide._

### Slide 4

- DESENVOLVIMENTO DE SISTEMAS
- Nesta aula, vamos:
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store
- Compreender a necessidade do uso de sistemas digitais.

_7 imagem(ns) no slide._

### Slide 5

- Este material foi elaborado a partir da análise do plano de curso e reúne os conhecimentos essenciais para o Técnico em Desenvolvimento de Sistemas. As aulas foram organizadas com foco na clareza conceitual, na construção gradual dos conteúdos e na utilização de metodologias ativas que favorecem a compreensão, a participação e o desenvolvimento de habilidades e competências de forma significativa.
- De acordo com a matriz curricular do Curso Técnico em Desenvolvimento de Sistemas, que traz em sua essência componentes estruturados para a realização de aulas práticas, cada unidade curricular deve contemplar, além da abordagem teórica, uma proposta de atividade prática a ser desenvolvida pelo professor. Essa orientação assegura a coerência entre o planejamento didático e o que está estabelecido na matriz, promovendo experiências formativas alinhadas ao perfil profissional previsto.
- O professor tem total autonomia para adaptar o conteúdo conforme o contexto da turma, ajustando exemplos, aprofundamentos e estratégias didáticas para otimizar a aprendizagem e a conexão com a prática profissional.
- Se houver falta de conexão ou indisponibilidade de internet durante a aula, os materiais abaixo podem ser utilizados como apoio para elaborar recursos complementares, garantindo a continuidade da abordagem teórica prevista.
- ATENÇÃO PROFESSOR!
- Para saber mais: FORTUNATO, Daniel Medeiros. Google Drive: Guia Prático para Utilização em Projetos Colaborativos. São Paulo: Novatec, 2019.

_2 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Os sistemas digitais trabalham com valores chamados discretos, valores estes que assumem sempre um mesmo número de pontos entre dois valores.

_4 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Em um termômetro digital, vê-se a medição da temperatura de forma padronizada, ou você está com a temperatura marcando 36,5 ou 36,6, não existe “quase 36,6”, como pode-se verificar em um termômetro analógico.
- Socializem suas respostas
- Quais outros equipamentos utilizam do sistema digital?

_5 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Sistemas Digitais
- OBS: link do vídeo deve ser atualizado caso a apresentação mude de pasta junto com os vídeos.
- https://drive.google.com/file/d/16Kt2AMgYr4JNOl8aaCexOnaGCuFylcss/view?usp=drive_link

_5 imagem(ns) no slide._

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- Escreva no seu caderno a resposta!
- Ainda que o nosso foco seja os sistemas digitais, o sistema analógico foi muito citado. Qual a diferença entre o sistema digital e o analógico?
- Entendemos a diferença, mas onde podemos encontrar a aplicação dos sistemas digitais e analógicos?

_5 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- Escreva no seu caderno a resposta!
- O sistema tem sinais com número finito de valores discretos, se contrapondo a sistemas analógicos, nos quais os sinais têm valores pertencentes a um conjunto infinito.
- Existem nas duas versões: termômetro, relógio, velocímetro e balança.
- Resposta

_5 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Um sistema de refrigeração de uma sala de computadores é formado por dois aparelhos de ar-condicionado.
- Aplicação de
- sistemas digitais
- Nesta sala, existe um termômetro de mercúrio que foi colocado em uma das paredes, o qual pode sofrer baixas elevações, que são de crescentes e decrescentes contínuos. Porém, o sistema de refrigeração monitora digitalmente as elevações de temperatura.

_4 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- Certa vez, os funcionários perceberam que a temperatura local não saía dos 15°C no sistema digital, mas ao olharem no termômetro de mercúrio, perceberam que a temperatura passava dos 15°C, mas não ultrapassou 15,5°C.
- Por que isso acontecia?

_4 imagem(ns) no slide._

### Slide 13

- DESENVOLVIMENTO DE SISTEMAS
- O problema é que o sistema digital deveria emitir um alarme nos 15,5°C, pois esta pouca diferença de calor começaria a comprometer as máquinas locais.
- Precisaram, então, ajustar o sistema digital, mudando o seu arredondamento de valores.
- Este é um dos “poréns” do uso dos sistemas digitais: a conversão do valor analógico para o digital chegará sempre muito próxima.

_8 imagem(ns) no slide._

### Slide 14

- DESENVOLVIMENTO DE SISTEMAS
- A primeira informação que é necessário ter em mente é que um computador NÃO consegue entender letras, apenas números, e para ser mais específico, apenas os números 0 e 1. E então vocês podem perguntar: “E a quantidade fenomenal de palavras que digitamos?”. Bom, estas palavras são “traduzidas” para a linguagem que o computador entende. Quando digitamos uma letra, na verdade estamos passando um número para o computador, e mais um número que será convertido para um outro sistema numérico, o famoso sistema binário.
- Tabela ASCII

_4 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- A história da tabela ASCII
- OBS: link do vídeo deve ser atualizado caso a apresentação mude de pasta junto com os vídeos.
- https://drive.google.com/file/d/1xLdtWTn6XjKoEGOEpnAk_TDu5GtPizrd/view?usp=drive_link

_5 imagem(ns) no slide._

### Slide 16

- DESENVOLVIMENTO DE SISTEMAS
- Escreva no seu caderno a resposta!
- No vídeo foi apresentada uma justificativa muito convincente quanto à importância da criação da Tabela ASCII. Qual é essa justificativa?
- Pode-se concluir que uma Tabela ASCII é...?
- Atividade

_6 imagem(ns) no slide._

### Slide 17

- DESENVOLVIMENTO DE SISTEMAS
- Na informática, o uso de padrões é muito útil e se faz necessário. Antes cada computador utilizava uma regra diferente para representar estes caracteres, o que poderia fazer com que a produção de um material em um computador não funcionasse em outro.
- Uma tabela ASCII é um sistema de representação de letras, algarismos e sinais de pontuação e de controle, por meio de um sinal codificado em forma de código binário.
- Resposta

_3 imagem(ns) no slide._

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- Tabela ASCII
- Como visto no vídeo, o código ASCII foi proposto por Robert W. Bemer como uma solução para unificar a representação de caracteres alfanuméricos em computadores.
- É verdade que antes de 1960 cada computador utilizava uma regra diferente para representar estes caracteres e é possível imaginar o caos que era, confeccionar um trabalho em um computador e ficar na expectativa que funcione ao menos parcialmente em outro computador.

_3 imagem(ns) no slide._

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- Tabela ASCII
- O computador precisa processar e converter tudo para bytes, pois é isso que ele entende. Porém, ocorria que estas conversões não tinham um padrão.

_4 imagem(ns) no slide._

### Slide 20

- DESENVOLVIMENTO DE SISTEMAS
- Tabela ASCII
- Alguns dos caracteres não podem ser impressos (de código 0 a 31), pois eram na verdade comandos para computadores antigos.
- Foi aí que entrou a tabela ASCII (sigla para Código Padrão Americano para o Intercâmbio de Informação), o que rendeu uma grande vantagem, afinal já não se teria tantos casos de incompatibilidade de informações entre os computadores.

_3 imagem(ns) no slide._

### Slide 21

- DESENVOLVIMENTO DE SISTEMAS
- Tabela ASCII
- Como o computador só entende zeros e uns, quando se digita algo (qualquer coisa mesmo), estas informações são convertidas.
- Ocorre que nós também não conseguimos entender os zeros e uns de retorno do computador e por isso esta informação também é convertida. Por exemplo, por trás deste material que você está lendo existem um monte de zero e uns convertidos para caracteres que possam ser legíveis pelo homem.

_6 imagem(ns) no slide._

### Slide 22

- DESENVOLVIMENTO DE SISTEMAS
- Tabela ASCII
- Perceba que cada caractere está vinculado a um código binário e é assim que o computador enxerga cada um deles, um conjunto de zeros e uns. Quando se digita, por exemplo, “Oi!”, o computador está realizando uma conversão de cada caractere para então processar esta informação.
- O nosso “Oi!” para o computador é 01001111 01101001 00100001.

_3 imagem(ns) no slide._

### Slide 23

- DESENVOLVIMENTO DE SISTEMAS
- Vamos praticar alguns conceitos?
- O que é um
- sistema?
- O que significa o
- termo "digital"?
- O que é
- sistema
- analógico?
- O que é
- sinal
- digital?
- Grupo 1
- Grupo 2
- Grupo 3
- Grupo 4

_3 imagem(ns) no slide._

> **Notas do apresentador:** 📢 Atividade: "Desvendando os Sistemas – Analógico vs. Digital" 👨‍💻 Objetivo: Compreender e aplicar os conceitos de sistema, digital, analógico e sinal digital por meio de uma atividade interativa e colaborativa. 🔹 Instruções para os Grupos: 1️⃣ Dividam-se em grupos de 4 a 5 participantes. 2️⃣ Cada grupo deverá pesquisar e debater os seguintes conceitos: O que é um sistema? Exemplos no cotidiano. O que significa o termo "digital"? Comparação com o analógico. O que é um sistema analógico? Exemplos práticos. O que é um sinal digital? Características e exemplos. 3️⃣ Após a discussão, cada grupo deverá produzir uma apresentação criativa para compartilhar o que aprenderam com a turma. A apresentação pode ser feita de forma livre, usando um dos formatos abaixo: 📜 Mapa mental ou esquema ilustrado. 🎭 Encenação rápida representando sistemas analógicos e digitais. 🎤 Explicação em formato de podcast (curto e objetivo). 🎥 Vídeo curto demonstrando exemplos reais. 4️⃣ Cada grupo terá até 5 minutos para apresentar seu trabalho para a turma. 5️⃣ Após todas as apresentações, o professor conduzirá uma discussão final, conectando os conceitos abordados aos sistemas digitais aplicados na tecnologia e no dia a dia.

### Slide 24

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje
- Uma tabela ASCII é um sistema de representação de letras, algarismos e sinais de pontuação e de controle, por meio de um sinal codificado em forma de código binário.
- Os computadores operam executando cálculos, representando números e imagens no sistema de numeração binário.

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

_Fonte: AULA 10_INTRODUÇÃO A COMPUTAÇÃO ATIVIDADE.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

INTRODUÇÃO A COMPUTAÇÃO

1ª SÉRIE

ATIVIDADE AULA 10

Questão 1

A representação digital tem certas vantagens sobre a representação analógica em aplicações eletrônicas. Para citar uma, dados digitais podem ser processados e transmitidos de forma mais eficiente e confiável que dados analógicos. Além disso, dados digitais possuem uma grande vantagem quando é necessário armazenamento (memorização). Por exemplo, a música quando convertida para o formato digital pode ser armazenada de forma mais compacta e reproduzida com maior precisão e pureza que quando está no formato analógico. O ruído (flutuações indesejadas na tensão) quase não afeta os dados digitais tanto quanto afeta os sinais analógicos (FLOYD, 2007). A partir desse contexto, é possível afirmar que uma das vantagens dos sistemas digitais é:

a) Praticamente não são afetados pelas distorções, interferências e ruídos.

b) Têm o poder de definir uma quantidade infinita de informações.

c) A densidade do sinal digital é muito mais elevada do que a do sinal analógico.

d) Os sinais digitais têm um fácil processamento.

Resposta comentada: A alternativa a) está correta, pois está é uma das vantagens mais importantes do sistema digital, porém é preciso ficar atento a algumas distorções no que diz respeito ao valor recebido e ao valor processado. A alternativa b) está incorreta, pois o sistema digital trabalha com valores discretos, ou seja, padrões definidos de valores. A alternativa c) está incorreta, pois, trata-se de um caso contrário, porque na verdade a densidade do sinal analógico é maior do que a digital. A alternativa d) está incorreta, pois os sinais digitais não possuem um fácil processamento, sempre será preciso um sistema informatizado para o fazer.

Questão 2

Uma determinada gravadora de música realiza a primeira gravação das músicas cantadas em seu estúdio em fitas magnéticas, pois deseja manter a melhor qualidade do som, qualidade esta idêntica àquela propagada no estúdio. É correto dizer que o sistema utilizado neste caso é o:

a) Sistema digital, pois certamente o processo apresentado foi muito fácil de projetar.

b) Sistema analógico, pois o ambiente proposto proporcionaria ruídos, que causam distorções.

c) Sistema analógico, pois a informação foi armazenada sem perdas no processamento.

d) Sistema digital, pois era preciso uma quantidade infinita de valores para gravação da música.

Resposta comentada: A alternativa a) está incorreta, pois um estúdio de gravação é um local planejado e projetado para a gravação de som, o que justifica um sistema digital não condizer com a situação proposta. A alternativa b) está incorreta, pois, mesmo tendo sido utilizado um sistema analógico para a gravação das músicas, um ambiente no qual ocorrem muitos ruídos certamente proporcionaria a interferência das informações. A alternativa c) está correta, pois a informação foi armazenada sem perdas quando em seu processamento, situação que ocorre quando realizamos o sistema digital. A alternativa d) está incorreta, pois o sistema digital trabalha com números discretos e não com uma quantidade infinita e sem padrão.
