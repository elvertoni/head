---
titulo: "Dispositivos de Entrada e Saída (I/O): Como interagimos com a máquina"
tipo: rco-seed
disciplina: introducao-a-computacao
sigla_rco: IAC
trimestre: 1
ordem_rco: 19
serie: 1
aula_rco: "Aula 19"
slides: 33
tem_atividade: true
tem_pratica: true
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/IAC/1TRI/19-dispositivos-de-entrada-e-saida-i-o-como-interagimos-com-a-maquina/19-dispositivos-de-entrada-e-saida-i-o-como-interagimos-com-a-maquina.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/IAC/1TRI/19-dispositivos-de-entrada-e-saida-i-o-como-interagimos-com-a-maquina/AULA 19_INTRODUÇÃO A COMPUTAÇÃO ATIVIDADE.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/IAC/1TRI/19-dispositivos-de-entrada-e-saida-i-o-como-interagimos-com-a-maquina/AULA 19_PRÁTICA INTRODUÇÃO A COMPUTAÇÃO.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Dispositivos de Entrada e Saída (I/O): Como interagimos com a máquina

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- INTRODUÇÃO A COMPUTAÇÃO
- 1ª SÉRIE
- Dispositivos de Entrada e Saída (I/O): Como interagimos com a máquina
- Aula 19

_3 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- DESENVOLVIMENTO DE SISTEMAS
- Nesta aula, vamos:
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store
- Identificar qual tipo de unidade de armazenamento utilizar em cada caso.

_7 imagem(ns) no slide._

### Slide 4

- DESENVOLVIMENTO DE SISTEMAS
- Este material foi elaborado com base na análise do plano de curso, abrangendo os conhecimentos essenciais para o curso Técnico em Desenvolvimento de Sistemas. Inclui aulas práticas desenvolvidas de acordo com as metodologias ativas, visando ao desenvolvimento de habilidades e competências de forma dinâmica e significativa. Você tem total liberdade para personalizar o material de acordo com seu contexto, otimizando o aproveitamento deste conteúdo.
- Em caso de falta ou indisponibilidade de acesso à internet no local de aula, você poderá utilizar os seguintes artigos para criação de material complementar para auxiliar na aula:
- Para saber mais: FORTUNATO, Daniel Medeiros. Google Drive: Guia Prático para Utilização em Projetos Colaborativos. São Paulo: Novatec, 2019.
- ATENÇÃO PROFESSOR!

_5 imagem(ns) no slide._

### Slide 5

- DESENVOLVIMENTO DE SISTEMAS
- Na aula anterior…
- Compreendemos o funcionamento do hard disk HD em um computador.

_4 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Uma gráfica recebe diariamente muitos arquivos para impressão e encadernação…
- Ela dispõe de um computador com um hard disk (HD) com bastante espaço em disco, para armazenar todos os arquivos que chegam. O gerente da gráfica resolveu fazer cópias de segurança para evitar interrupções ou perda de dados dos clientes

_4 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Dialogue com o colega e socialize as ideias com a turma no final!
- Como ele poderia criar cópias dos arquivos que estão gravados no HD do computador principal? Será que ele precisa comprar outro computador ou outro HD?
- Para pensarmos juntos!

_5 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- O gerente pode usar um pendrive, por exemplo, para armazenar os arquivos.

_4 imagem(ns) no slide._

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- Unidades de Armazenamento
- Mas como tantas informações diferentes podem ser armazenadas e usadas?
- Será que existe algum limite?
- Podemos mesmo armazenar qualquer coisa?
- O armazenamento de dados em formato digital ocorre de diversas formas hoje em dia…

_4 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- Os registros escritos usados pelo ser humano há alguns milhares de anos, desde os rabiscos nas cavernas até os dias de hoje, têm, em sua essência, características comuns: usam símbolos que remetem a algum significado.
- Mas não basta apenas registrar algo em qualquer lugar.
- É preciso, também, saber como ler ou interpretar o que foi registrado.

_4 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Unidades de Armazenamento
- Para a escrita manual, a interpretação vem do letramento, da formação escolar e da prática.
- Mas e os dados digitais? Como são armazenados e interpretados?
- Hoje em dia, a maioria dos celulares gravam vídeos que depois são compartilhados com outras pessoas que podem assistir em TVs, computadores e em outros celulares.

_4 imagem(ns) no slide._

### Slide 12

- Primeiro, os armazenamentos nem sempre foram digitais. Há alguns anos eram apenas analógicos.
- Analógicos?
- Sim, essa palavra remete à analogia, ou seja, quando há uma representação de algo por um sistema comparativo ou equivalente. Um exemplo clássico é o disco de vinil, que hoje em dia encontramos como um item vintage.
- Unidades de Armazenamento
- DESENVOLVIMENTO DE SISTEMAS

_4 imagem(ns) no slide._

### Slide 13

- DESENVOLVIMENTO DE SISTEMAS
- No disco de vinil, uma agulha desliza sobre uma espiral, partindo da parte mais externa até a parte mais interna do disco.
- Em uma rotação fixa, ao longo desta espiral, encontram-se muitas oscilações que vibram a agulha exatamente como o som originalmente captado nos estúdios da gravação da música, ou outro material audível. Então, com o uso de um amplificador, o som “esculpido” no vinil renasce nas caixas de som.

_5 imagem(ns) no slide._

### Slide 14

- DESENVOLVIMENTO DE SISTEMAS
- A gravação de dados no estilo analógico reinou durante muitos anos. Além do vinil, também foram usadas fitas magnéticas, tanto para áudio (K7) como para vídeo, por exemplo.

_4 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- E a gravação digital?
- Esse estilo veio naturalmente a partir do momento em que os computadores foram se tornando realidade.
- O estilo analógico representa uma “cópia” em escala de um dado original. O estilo digital equivale a ouvir uma história, registrá-la em outro idioma para depois, outra pessoa recontar a história a partir do registro feito.

_4 imagem(ns) no slide._

### Slide 16

- DESENVOLVIMENTO DE SISTEMAS
- O “idioma” usado para dados digitais é limitado a dois símbolos:
- 0 e 1. Também conhecido como números binários. E é a partir das associações com esses dois números que começamos a registrar tudo no mundo digital.
- Então, poderá haver perda de informação ao se usar o estilo de registro analógico?
- Bem, isso irá depender do grau de exigência para uma cópia e o que se quer copiar.
- Mas, por quê?

_4 imagem(ns) no slide._

### Slide 17

- DESENVOLVIMENTO DE SISTEMAS
- Como os dados são armazenados?
- OBS: link do vídeo deve ser atualizado caso a apresentação mude de pasta junto com os vídeos.
- https://drive.google.com/file/d/1TKY8ldGkwUcGzMQMZEZThlbZi-CZzSqb/view?usp=drive_link

_5 imagem(ns) no slide._

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- Respondendo algumas perguntas…
- CDs e DVDs têm a mesma capacidade de armazenamento, mudando apenas a tecnologia?
- Quem se voluntaria para responder?
- As gravações de dados no passado eram apenas via escrita de texto?
- O primeiro registro fotográfico foi de forma digital? Por quê?

_4 imagem(ns) no slide._

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- Identificar Unidades de Armazenamento
- Pode indicar dois valores, um de cada vez. Equivale aos estados Ligado (1), Desligado (0), Verdadeiro (1) e Falso (0). Ou diretamente aos números 1 e 0.
- O Bit é a menor unidade de medida de armazenamento no sistema digital baseado na numeração binária. É uma abreviação de “dígito binário” ou “binary digit”.

_4 imagem(ns) no slide._

### Slide 20

- DESENVOLVIMENTO DE SISTEMAS
- Identificar Unidades de Armazenamento

_4 imagem(ns) no slide._

### Slide 21

- DESENVOLVIMENTO DE SISTEMAS
- Assim como qualquer unidade de medida,
- o Byte também tem seus múltiplos:
- Pode armazenar um pequeno livro, 700MB é a capacidade de um CD-R.
- 1KB - Kilobyte: 210 = 1024 Bytes.
- Podemos escrever um parágrafo inteiro.
- 1MB - Megabyte: 220 = 1 048 576 Bytes = 1024KB.

_4 imagem(ns) no slide._

### Slide 22

- DESENVOLVIMENTO DE SISTEMAS
- Identificar unidades de armazenamento
- 1GB - Gigabyte: 230 = 1 073 741 824 Bytes = 1024MB.
- Um filme de boa qualidade de cerca de 1h30min pode ser armazenado com 2GB aproximadamente.
- Unidade de armazenamento: HDs, SSDs, cartão de memória, pendrives, DVDs e Blu-Ray.

_4 imagem(ns) no slide._

### Slide 23

- DESENVOLVIMENTO DE SISTEMAS
- Normalmente, é a capacidade padrão dos HDs que são instalados nos computadores atuais. É possível armazenar 10 temporadas em boa qualidade de sua série favorita.
- 1TB - Terabyte: 240 = 1 099 511 627 776 Bytes = 1024GB.

_4 imagem(ns) no slide._

### Slide 24

- DESENVOLVIMENTO DE SISTEMAS
- A partir daqui, as comparações já ganham proporções muito elevadas…
- 1PB - Petabyte: 250 = 1 125 899 906 842 624 Bytes = 1024TB.
- Equivale à capacidade de todos os HDs dos computadores de uma escola mediana.
- 1EB - Exabyte: 260 = 1 048 576 TB, mais de 1 milhão de Terabytes.

_4 imagem(ns) no slide._

### Slide 25

- DESENVOLVIMENTO DE SISTEMAS
- 1ZB - Zettabyte: 270 = 1 073 741 824 TB, mais de 1 bilhão de Terabytes.
- 1YB - Yottabyte: 280 = 1 099 511 627 776 TB, mais de 1 trilhão de Terabytes.
- 1BB - Brontobyte: 290 = 1 125 899 906 842 624 TB, mais de 1 quatrilhão de Terabytes.
- 1GEB - Geopbyte: 2100 = 1 152 921 504 606 846 976 TB, mais de 1 quintilhão de Terabytes.

_4 imagem(ns) no slide._

### Slide 26

- DESENVOLVIMENTO DE SISTEMAS
- Atualmente, com o advento da computação em nuvem, conhecida como cloud computing, muitas empresas têm optado por ela para armazenar seus dados.

_4 imagem(ns) no slide._

### Slide 27

- DESENVOLVIMENTO DE SISTEMAS
- Procurem fazer sempre uma cópia extra de segurança (backup, em inglês) de qualquer dado que julgue importante, afinal, imprevistos podem ocorrer, e a recuperação de dados nem sempre é possível.
- Algo que devemos levar em conta quando fizermos algum armazenamento é a disponibilidade futura dos dados gravados.

_4 imagem(ns) no slide._

### Slide 28

- DESENVOLVIMENTO DE SISTEMAS
- TAREFA PARA CASA!
- Faça uma pesquisa para saber qual o maior volume de armazenamento em pen drives atualmente.

_4 imagem(ns) no slide._

### Slide 29

- DESENVOLVIMENTO DE SISTEMAS
- Vamos Praticar?
- Já imaginou como seria usar um computador sem enxergar a tela?
- Ou sem poder ouvir os sons que ele emite?
- Será que um teclado e um monitor são suficientes para garantir acessibilidade? Como você faria diferente?
- A tecnologia tem o poder de transformar vidas, mas para isso, precisa ser acessível para TODOS!

_5 imagem(ns) no slide._

### Slide 30

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje
- Os dados podem ser armazenados em mídias diferentes e como podem ser acessados.

_4 imagem(ns) no slide._

### Slide 31

- DESENVOLVIMENTO DE SISTEMAS
- Pronto para desbloquear sua carreira de TI?
- Está perdido estudando mas não sabe por onde começar? Se a resposta é sim, você está no lugar certo! Descubra as estratégias e ferramentas essenciais para te ajudar a desbloquear seu potencial em TI e buscar sua primeira vaga de emprego no setor!
- Este e-book é um guia completo para quem busca começar pelos melhores caminhos para se tornar um excelente profissional de TI, ensinando a identificar perfis profissionais, aplicar técnicas de estudo eficazes, transformar teoria em prática, e aumentar a visibilidade de seu trabalho no mercado de trabalho. Ideal para novatos e profissionais em transição.
- E o melhor, ele pode ser seu, inteiramente grátis!
- Basta clicar AQUI e realizar o seu cadastro com o seu @escola!

_6 imagem(ns) no slide._

### Slide 32

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

### Slide 33

- DESENVOLVIMENTO DE SISTEMAS
- O RCO+Aulas é um projeto da Secretaria de Estado da Educação do Paraná e está em constante revisão. Todos os slides são de uso exclusivo dos professores da Rede Pública de Ensino, com a finalidade específica de aplicação em sala de aula, sendo totalmente vedada a publicização, reutilização, reprodução total ou parcial para quaisquer outros fins.

_3 imagem(ns) no slide._

## Atividade

_Fonte: AULA 19_INTRODUÇÃO A COMPUTAÇÃO ATIVIDADE.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

INTRODUÇÃO A COMPUTAÇÃO

1ª SÉRIE

ATIVIDADE AULA 19

Questão 1

O armazenamento de dados nem sempre foi feito de forma digital. Desde muito tempo, o ser humano vem fazendo registros de praticamente tudo que julga importante. É um estilo analógico de armazenamento de dados:

a) Transformação de uma informação qualquer em números binários.

b) Representação em escala de uma informação em áudio ou visual.

c) Gravação de fotos em um HD.

d) Ouvir uma história e reescrever em um idioma de caracteres reduzidos.

Resposta comentada: Os dados analógicos são capturas contínuas do que está acontecendo no momento. Representam uma cópia em escala menor de alguma informação observável. Transformar uma informação em números binários é um processo digital, assim como gravar fotos em um hard disk. Reescrever uma história com caracteres reduzidos pode trazer perda de dados importantes e não caracteriza um processo analógico.

Questão 2

Gravar dados é uma tarefa muito comum hoje em dia. E o smartphone é um dos meios mais usados pelas pessoas. São fotos, vídeos e até ligações. O processo digital de armazenamento de dados neste dispositivo:

a) Trata da criação de uma versão das informações colhidas em uma escala menor.

b) Trata da produção de arquivos de tamanhos diferentes.

c) Trata da criação de arquivos em uma versão entendida apenas por smartphones.

d) Trata da conversão de informações como áudio e vídeo para um formato diferente, entendido apenas pelo computador.

Resposta comentada: Como o celular é um minicomputador, os dados precisam estar no formato digital para que sejam armazenados e processados. Criar uma versão em uma escala menor é um processo analógico, assim como a produção de discos de vinil e uma pintura de um quadro.

## Prática

_Fonte: AULA 19_PRÁTICA INTRODUÇÃO A COMPUTAÇÃO.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

INTRODUÇÃO A COMPUTAÇÃO

1ª SÉRIE

AULA PRÁTICA 19

Resumo Explicativo:

Os dispositivos de entrada e saída (I/O) são os responsáveis pela comunicação entre o usuário e o computador. Eles permitem que dados sejam enviados ao sistema (entrada) e que o sistema apresente respostas ao usuário (saída).

Dispositivos de entrada incluem:

- Teclado
- Mouse
- Microfone
- Scanner
- Câmera
Dispositivos de saída incluem:

- Monitor
- Impressora
- Caixas de som
- Projetor
Alguns dispositivos, como telas sensíveis ao toque, funcionam como entrada e saída simultaneamente. No desenvolvimento de sistemas, entender os dispositivos I/O é fundamental para projetar interfaces eficientes, acessíveis e adequadas às necessidades do usuário final.

Estudo de Caso:

Cenário: Um grupo de estudantes do curso técnico de informática foi convidado para desenvolver uma solução acessível para alunos com deficiência visual em uma escola pública. A proposta envolve criar uma interface de leitura digital simples que permita o acesso a conteúdos educacionais.

Durante o planejamento, o grupo identificou os seguintes pontos:

- Dispositivos tradicionais como mouse e monitor não são adequados para usuários com deficiência visual.
- É necessário integrar dispositivos de entrada por voz e saída por áudio, como microfones e sintetizadores de voz.
- O sistema precisa ser simples, funcional e compatível com os recursos disponíveis na escola.
Agora, o grupo precisa decidir:

- Quais dispositivos de entrada e saída utilizar no projeto?
- Como integrar esses dispositivos ao sistema desenvolvido?
- Como garantir que a interface seja acessível e intuitiva mesmo sem o uso da visão?
A escolha correta dos dispositivos I/O será decisiva para o sucesso do projeto e para garantir inclusão digital na escola.

Questões:

- Liste cinco exemplos de dispositivos de entrada e cinco de saída e indique a função básica de cada um.
- Explique, com suas palavras, a importância dos dispositivos de entrada e saída na interação entre usuário e computador.
- Suponha que você está desenvolvendo um sistema para deficientes auditivos. Quais dispositivos de saída você usaria e por quê?
- Analise as diferenças entre um dispositivo que é apenas de entrada, um que é apenas de saída e um que é híbrido. Dê um exemplo para cada tipo e explique suas funções no contexto do desenvolvimento de sistemas.
- Avalie a escolha de uma escola que fornece apenas teclado e monitor para alunos com deficiência visual. Essa decisão atende às necessidades de acessibilidade? Justifique sua resposta com base na função dos dispositivos de I/O.
- Projete uma solução interativa que utilize pelo menos um dispositivo de entrada e um de saída alternativos para atender usuários com limitações físicas (ex: controle por voz e feedback por áudio). Descreva como o sistema funcionaria e quais tecnologias seriam usadas.
