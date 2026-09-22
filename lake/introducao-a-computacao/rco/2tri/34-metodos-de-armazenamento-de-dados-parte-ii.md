---
titulo: "Métodos de Armazenamento de Dados - Parte II"
tipo: rco-seed
disciplina: introducao-a-computacao
sigla_rco: IAC
trimestre: 2
ordem_rco: 34
serie: 1
aula_rco: "Aula 34"
slides: 19
tem_atividade: true
tem_pratica: true
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/IAC/2TRI/34-metodos-de-armazenamento-de-dados-parte-ii/34-metodos-de-armazenamento-de-dados-parte-ii.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/IAC/2TRI/34-metodos-de-armazenamento-de-dados-parte-ii/AULA 34_INTRODUÇÃO A COMPUTAÇÃO ATIVIDADE.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/IAC/2TRI/34-metodos-de-armazenamento-de-dados-parte-ii/AULA 34_PRÁTICA INTRODUÇÃO A COMPUTAÇÃO.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Métodos de Armazenamento de Dados - Parte II

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- INTRODUÇÃO A COMPUTAÇÃO
- 1ª SÉRIE
- Métodos de Armazenamento de Dados - Parte II
- Aula 34

_3 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- DESENVOLVIMENTO DE SISTEMAS
- Nesta aula, vamos:
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store
- Entender como os dados são armazenados no computador Parte II.

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
- Iniciamos os estudos em como os dados são armazenados na memória do computador.

_4 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Leo, é um programador iniciante que está começando a se aprofundar em como as coisas funcionam "por trás das cenas".
- Leo aprendeu sobre arrays e está curioso para saber como eles são armazenados na memória.

_4 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Leo reflete:
- Se um array é como uma fila de caixas no supermercado, então cada caixa na fila deve estar exatamente ao lado da outra, certo?
- Isso significaria que se eu criar um array com cinco elementos, todos os cinco estariam armazenados juntos, em um espaço contíguo na memória.

_4 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Será que isso significa que, se eu precisar adicionar mais um elemento ao array, terei que mover todo o array para um novo local na memória que tenha espaço suficiente para todos os seis elementos?
- Realizem a atividade em duplas e socializem no final!

_5 imagem(ns) no slide._

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- Na verdade, Leo está correto na maioria dos casos. Arrays são geralmente armazenados em blocos contíguos de memória. Por isso, se você precisa adicionar um elemento a um array que já está cheio, normalmente será necessário criar um novo array maior e copiar os elementos antigos para ele. Este é um dos motivos pelos quais, em algumas linguagens de programação, o tamanho dos arrays deve ser conhecido antecipadamente e não pode ser alterado uma vez que o array é criado.

_4 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- Arrays e números de ponto flutuante são fundamentais na computação e são armazenados de maneiras específicas na memória do computador.

_4 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Arrays são uma coleção de elementos do mesmo tipo. Pense neles como uma fila no supermercado - cada "caixa" na fila pode armazenar um item (elemento). Em termos de armazenamento, cada elemento de um array ocupa um espaço contíguo na memória.
- Se você tem um array de 5 inteiros, por exemplo, o computador reserva 5 "caixas" de memória uma ao lado da outra. Quando você precisa acessar um elemento, o computador calcula a posição exata na memória.

_4 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- Números de ponto flutuante, por outro lado, são usados para representar números reais, aqueles com casas decimais. Eles são armazenados na memória em um formato chamado de padrão IEEE 754. Este formato divide o espaço de memória em três partes: sinal, expoente e mantissa (ou fração).
- O sinal indica se o número é positivo ou negativo, o expoente fornece uma ideia da "escala" do número (pense nele como a quantidade de zeros em um número como 1000 ou 0.001), e a mantissa carrega a parte precisa do número.

_6 imagem(ns) no slide._

### Slide 13

- DESENVOLVIMENTO DE SISTEMAS
- Ambos, arrays e números de ponto flutuante, desempenham papéis importantes em muitos aspectos da programação e do processamento de dados, e entender como eles são armazenados na memória pode ajudar a melhorar a eficiência e a eficácia dos seus programas.

_4 imagem(ns) no slide._

### Slide 14

- DESENVOLVIMENTO DE SISTEMAS
- Link para o curso: https://cursos.alura.com.br/course/arquitetura-computadores-funcionamento-programa
- Atividade Prática na Plataforma Alura
- Na plataforma Alura vamos acessar o seguinte curso:
- A recomendação é que você continue esse curso extraclasse, pois ele traz um conteúdo essencial para compreender sobre o referido tema.

_5 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- Vamos Praticar?
- Vamos agora colocar em prática o que aprendemos desenvolvendo a atividade sugerida.

_4 imagem(ns) no slide._

> **Notas do apresentador:** Link da atividade: https://docs.google.com/document/d/14YMgeI0LDKmHVX331os5_VzYiX90Zg-n/edit?usp=drive_link&ouid=112660820765629457253&rtpof=true&sd=true

### Slide 16

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje
- Passagem de parâmetros por valor e por referência;
- Quais são os problemas inerentes aos números de ponto flutuante.

_4 imagem(ns) no slide._

### Slide 17

- DESENVOLVIMENTO DE SISTEMAS
- Pronto para desbloquear sua carreira de TI?
- Está perdido estudando mas não sabe por onde começar? Se a resposta é sim, você está no lugar certo! Descubra as estratégias e ferramentas essenciais para te ajudar a desbloquear seu potencial em TI e buscar sua primeira vaga de emprego no setor!
- Este e-book é um guia completo para quem busca começar pelos melhores caminhos para se tornar um excelente profissional de TI, ensinando a identificar perfis profissionais, aplicar técnicas de estudo eficazes, transformar teoria em prática, e aumentar a visibilidade de seu trabalho no mercado de trabalho. Ideal para novatos e profissionais em transição.
- E o melhor, ele pode ser seu, inteiramente grátis!
- Basta clicar AQUI e realizar o seu cadastro com o seu @escola!

_6 imagem(ns) no slide._

### Slide 18

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

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- O RCO+Aulas é um projeto da Secretaria de Estado da Educação do Paraná e está em constante revisão. Todos os slides são de uso exclusivo dos professores da Rede Pública de Ensino, com a finalidade específica de aplicação em sala de aula, sendo totalmente vedada a publicização, reutilização, reprodução total ou parcial para quaisquer outros fins.

_4 imagem(ns) no slide._

## Atividade

_Fonte: AULA 34_INTRODUÇÃO A COMPUTAÇÃO ATIVIDADE.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

INTRODUÇÃO A COMPUTAÇÃO

1ª SÉRIE

ATIVIDADE AULA 34

Questão 1

Em programação, o que é um array?

a) Uma coleção de valores que estão armazenados em posições separadas na memória.

b) Uma coleção de valores que estão armazenados em posições contíguas na memória.

c) Um tipo de dado que armazena um único valor.

d) Um tipo de dado que não pode ser armazenado na memória.

Resposta correta: b) Um array é uma coleção de valores que são armazenados em posições contíguas na memória. Isso permite um acesso rápido e eficiente aos seus elementos.

Questão 2

O que acontece quando você quer adicionar um elemento a um array que já está cheio?

a) O sistema automaticamente cria espaço adicional no final do array existente.

b) Você deve criar um novo array maior e copiar os elementos antigos para ele.

c) Nada, você pode adicionar elementos a um array indefinidamente sem se preocupar com o espaço na memória.

d) O computador automaticamente apaga o último elemento do array para criar espaço para o novo elemento.

Resposta correta: b) Se um array já está cheio e você quer adicionar um novo elemento a ele, geralmente será necessário criar um novo array que seja maior e copiar os elementos antigos para ele. Isso ocorre porque arrays são armazenados em blocos contíguos de memória, e se o bloco atual não tem mais espaço, você precisará de um bloco maior.

## Prática

_Fonte: AULA 34_PRÁTICA INTRODUÇÃO A COMPUTAÇÃO.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

INTRODUÇÃO A COMPUTAÇÃO

1ª SÉRIE

AULA PRÁTICA 34

Resumo Explicativo:

Na segunda parte do estudo sobre métodos de armazenamento, o foco está nas técnicas lógicas de organização dos dados, como bancos de dados, armazenamento em nuvem e tecnologias de redundância e backup. A forma como os dados são estruturados, acessados e protegidos influencia diretamente na eficiência e segurança de sistemas computacionais, sendo um conhecimento essencial no desenvolvimento de software.

Estudo de Caso:

Cenário:

O professor Alex está organizando uma feira de tecnologia na escola e desafia os alunos a propor soluções para armazenar com segurança os dados dos visitantes, expositores e avaliações coletadas durante o evento. Duas equipes apresentam ideias:

- A Equipe A propõe usar um banco de dados relacional simples em um servidor local.
- A Equipe B sugere usar o Google Sheets conectado a uma planilha na nuvem com backups automáticos.
Durante os testes, a Equipe A enfrenta dificuldades para montar o servidor e garantir disponibilidade, enquanto a Equipe B consegue coletar e compartilhar os dados rapidamente, mas enfrenta limitações na estrutura e segurança dos dados sensíveis.

O professor então promove um debate sobre como combinar diferentes métodos de armazenamento de forma eficiente, levando em conta escalabilidade, custo, confiabilidade e segurança da informação.

Questões

- Liste três formas de armazenamento de dados além dos dispositivos físicos tradicionais.
- Explique com suas palavras o que é armazenamento em nuvem e como ele se diferencia do armazenamento local.
- Se você tivesse que armazenar dados de alunos com notas, nomes e turmas, qual ferramenta ou método usaria e por quê?
- Compare as vantagens e desvantagens entre usar um banco de dados relacional local e uma planilha em nuvem para armazenamento de dados escolares.
- Na sua opinião, é viável para uma escola pública usar apenas soluções em nuvem para armazenar seus dados administrativos? Justifique com base em segurança, acessibilidade e custo.
- Desenvolva uma proposta de estrutura de armazenamento de dados para um sistema escolar simples, combinando pelo menos dois métodos (ex: banco de dados + backup em nuvem).
