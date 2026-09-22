---
titulo: "Métodos de Armazenamento de Dados - Parte I"
tipo: rco-seed
disciplina: introducao-a-computacao
sigla_rco: IAC
trimestre: 2
ordem_rco: 33
serie: 1
aula_rco: "Aula 33"
slides: 21
tem_atividade: true
tem_pratica: true
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/IAC/2TRI/33-metodos-de-armazenamento-de-dados-parte-i/33-metodos-de-armazenamento-de-dados-parte-i.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/IAC/2TRI/33-metodos-de-armazenamento-de-dados-parte-i/AULA 33_INTRODUÇÃO A COMPUTAÇÃO ATIVIDADE.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/IAC/2TRI/33-metodos-de-armazenamento-de-dados-parte-i/AULA 33_PRÁTICA INTRODUÇÃO A COMPUTAÇÃO.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Métodos de Armazenamento de Dados - Parte I

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- INTRODUÇÃO A COMPUTAÇÃO
- 1ª SÉRIE
- Métodos de Armazenamento de Dados - Parte I
- Aula 33

_3 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- DESENVOLVIMENTO DE SISTEMAS
- Nesta aula, vamos:
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store
- Compreender como os dados são armazenados no computador Parte I.

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
- Concluímos os estudos sobre como funciona a memória RAM do computador, e como a memória cache pode impactar no processamento.

_4 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Letícia, uma entusiasta de tecnologia que está aprendendo a programar, depara-se com um conceito novo: o armazenamento de diferentes tipos de dados na memória
- de um computador.
- Ela já entende que os computadores armazenam tudo em forma de bits, mas como eles diferenciam números inteiros, decimais e caracteres ainda é um mistério para ela.

_5 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Então, Letícia pergunta: "Como o computador consegue diferenciar entre um número inteiro, um decimal e um caractere se tudo é armazenado em bits?"
- Quem sabe responde!

_6 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Ótima pergunta, Letícia! Os computadores realmente armazenam tudo como bits, mas eles têm maneiras específicas de interpretar esses bits dependendo do tipo de dados que se espera ler.

_4 imagem(ns) no slide._

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Os números inteiros são armazenados como uma série de bits que representam o valor do número em binário. Já os números decimais são normalmente armazenados usando um formato chamado ponto flutuante, que divide os bits entre uma parte que representa um número inteiro e outra que representa a fração.

_4 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- Os caracteres, por outro lado, são armazenados de acordo com um padrão de codificação, como ASCII ou Unicode. Cada caractere é mapeado para um número específico, que é então armazenado em bits. Assim, quando o computador lê esses bits, ele usa o padrão de codificação para traduzir o número em um caractere.

_4 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Nos computadores, todas as informações, sejam números inteiros, decimais, caracteres ou qualquer outro tipo de dados, são armazenadas em formato binário, que é composto por 0s e 1s.
- Aqui está uma explicação básica de como isso acontece:

_5 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- Números inteiros: são armazenados como binários. Por exemplo, o número 7 é armazenado como 0111 e o número 15 como 1111. Cada número binário é chamado de bit, e um conjunto de 8 bits forma um byte, que é a unidade fundamental de armazenamento.

_4 imagem(ns) no slide._

### Slide 13

- DESENVOLVIMENTO DE SISTEMAS
- Números decimais:
- são um pouco mais complexos!
- Eles são armazenados usando o que é conhecido como ponto flutuante. Basicamente, um número decimal é dividido em duas partes: a parte inteira e a parte fracionária. Cada uma dessas partes é então convertida em binário. O resultado é um número binário que representa o número decimal. É importante notar que nem todos os números decimais podem ser representados com precisão em binário, o que pode levar a erros de arredondamento.

_10 imagem(ns) no slide._

### Slide 14

- DESENVOLVIMENTO DE SISTEMAS
- Caracteres: são armazenados usando padrões de código, como a Tabela ASCII ou Unicode. Cada caractere tem um número único atribuído a ele. Por exemplo, na tabela ASCII, a letra 'A' é representada pelo número 65, que é armazenado em binário.

_4 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- É importante lembrar que, independentemente do tipo de dado, o computador sempre armazena e processa informações em binário. Essa é uma das coisas que torna os computadores tão eficientes.

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
- Vamos Praticar?
- Vamos agora colocar em prática o que aprendemos desenvolvendo a atividade sugerida.

_4 imagem(ns) no slide._

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje
- Como números inteiros, caracteres, listas e números decimais são armazenados na memória;
- O que são os formatos ASCII, Latin1, Unicode e qual sua relação com o UTF-8.

_4 imagem(ns) no slide._

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- Pronto para desbloquear sua carreira de TI?
- Está perdido estudando mas não sabe por onde começar? Se a resposta é sim, você está no lugar certo! Descubra as estratégias e ferramentas essenciais para te ajudar a desbloquear seu potencial em TI e buscar sua primeira vaga de emprego no setor!
- Este e-book é um guia completo para quem busca começar pelos melhores caminhos para se tornar um excelente profissional de TI, ensinando a identificar perfis profissionais, aplicar técnicas de estudo eficazes, transformar teoria em prática, e aumentar a visibilidade de seu trabalho no mercado de trabalho. Ideal para novatos e profissionais em transição.
- E o melhor, ele pode ser seu, inteiramente grátis!
- Basta clicar AQUI e realizar o seu cadastro com o seu @escola!

_6 imagem(ns) no slide._

### Slide 20

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

### Slide 21

- DESENVOLVIMENTO DE SISTEMAS
- O RCO+Aulas é um projeto da Secretaria de Estado da Educação do Paraná e está em constante revisão. Todos os slides são de uso exclusivo dos professores da Rede Pública de Ensino, com a finalidade específica de aplicação em sala de aula, sendo totalmente vedada a publicização, reutilização, reprodução total ou parcial para quaisquer outros fins.

_4 imagem(ns) no slide._

## Atividade

_Fonte: AULA 33_INTRODUÇÃO A COMPUTAÇÃO ATIVIDADE.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

INTRODUÇÃO A COMPUTAÇÃO

1ª SÉRIE

ATIVIDADE AULA 33

Questão 1

Como os números inteiros são geralmente armazenados na memória do computador?

A) Como caracteres no formato Unicode.

B) Como uma série de bits que representam o valor do número em binário.

C) Como imagens.

D) Usando o formato de ponto flutuante.

Comentário: A resposta correta é B. Os números inteiros são armazenados como uma série de bits que representam o valor do número em binário.

Questão 2

Como um caractere é normalmente armazenado na memória de um computador?

A) Usando um formato de ponto flutuante.

B) Mapeando cada caractere para um número específico que é armazenado como bits.

C) Como uma imagem.

D) Como um número inteiro sem qualquer codificação.

Comentário: A resposta correta é B. Cada caractere é mapeado para um número específico, que é então armazenado como bits. Quando o computador lê esses bits, ele usa um padrão de codificação (como ASCII ou Unicode) para traduzir o número de volta em um caractere.

## Prática

_Fonte: AULA 33_PRÁTICA INTRODUÇÃO A COMPUTAÇÃO.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

INTRODUÇÃO A COMPUTAÇÃO

1ª SÉRIE

AULA PRÁTICA 33

Resumo Explicativo:

Os métodos de armazenamento de dados referem-se às formas como as informações são guardadas em dispositivos físicos e lógicos. Na Parte I, o foco está nos dispositivos mais comuns – como HDDs, SSDs, pendrives e cartões de memória – e nos conceitos fundamentais como arquivos, blocos, setores, e o papel do sistema de arquivos. Entender como os dados são armazenados é essencial para otimizar o acesso, garantir segurança e planejar soluções de software eficientes.

Estudo de Caso:

Cenário:

Laura está ajudando sua escola a organizar os arquivos digitais da biblioteca. No processo, ela percebe que alguns computadores ainda usam HDs antigos, enquanto outros já possuem SSDs. Ela também encontra arquivos duplicados, corrompidos ou mal nomeados. O professor propõe que ela analise como diferentes tipos de armazenamento impactam na organização, velocidade e integridade dos dados.

Laura pesquisa e descobre que:

- O HDD (disco rígido) usa discos magnéticos rotativos e é mais lento.
- O SSD (unidade de estado sólido) não possui partes móveis e tem leitura/escrita muito mais rápidas.
- Um sistema de arquivos (como FAT32, NTFS ou ext4) define como os dados são gravados e localizados.
- Blocos e setores são unidades físicas e lógicas de armazenamento.
- A organização e o nome dos arquivos impactam diretamente a acessibilidade e integridade dos dados.
Diante disso, Laura propõe uma reorganização dos arquivos e a substituição gradual dos HDs por SSDs nos computadores mais usados, começando pelos setores administrativos.

Questões

- Liste três tipos de dispositivos de armazenamento de dados e defina o que é um sistema de arquivos.
- Explique com suas palavras a diferença entre HDD e SSD. Como essa diferença afeta o desempenho dos computadores?
- Se sua escola precisa arquivar rapidamente grandes volumes de vídeo para um evento, qual tipo de armazenamento seria mais eficiente e por quê?
- Compare os sistemas de arquivos FAT32 e NTFS em termos de limitações de tamanho e segurança. Quais características diferenciam um do outro?
- Você concorda com a proposta de Laura de substituir os HDs por SSDs nos computadores da escola? Justifique sua resposta considerando custo, desempenho e durabilidade.
- Crie um plano de organização para os arquivos da biblioteca escolar, incluindo nomeação padronizada, backups periódicos e recomendações sobre qual tipo de armazenamento utilizar em cada setor.
