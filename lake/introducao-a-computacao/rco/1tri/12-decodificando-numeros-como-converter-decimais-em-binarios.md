---
titulo: "Decodificando Números: Como converter decimais em binários"
tipo: rco-seed
disciplina: introducao-a-computacao
sigla_rco: IAC
trimestre: 1
ordem_rco: 12
serie: 1
aula_rco: "Aula 12"
slides: 20
tem_atividade: true
tem_pratica: true
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/IAC/1TRI/12-decodificando-numeros-como-converter-decimais-em-binarios/12-decodificando-numeros-como-converter-decimais-em-binarios.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/IAC/1TRI/12-decodificando-numeros-como-converter-decimais-em-binarios/AULA 12_INTRODUÇÃO A COMPUTAÇÃO ATIVIDADE.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/IAC/1TRI/12-decodificando-numeros-como-converter-decimais-em-binarios/AULA 12_PRÁTICA INTRODUÇÃO A COMPUTAÇÃO.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Decodificando Números: Como converter decimais em binários

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- INTRODUÇÃO A COMPUTAÇÃO
- 1ª SÉRIE
- Decodificando Números: Como converter decimais em binários
- Aula 12

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

- DESENVOLVIMENTO DE SISTEMAS
- Nesta aula, vamos:
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store
- Conhecer como funciona o cálculo de números binários.

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
- Tudo o que fazemos no computador é convertido para o sistema binário, ou seja, para números que são representados por base 2.
- Isso porque o computador só entende dois estados: ligado (1) e desligado (0), ativo (1) ou inativo (0), e assim por diante...
- Cada letra, cada número, cada comando que executamos é convertido (no final, pois o caminho é longo) em conjuntos de “0” e “1”.
- Para pensarmos juntos!

_4 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Discutam em duplas e socializem as respostas com a turma no final!
- Semelhante a outras linguagem, temos que fazer as conversões, você como aluno aplicado conhece alguma técnica de conversão de um tipo de dado para outro, exemplo, conversão de palavras em outras línguas?

_5 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- De 10 a 2
- OBS: link do vídeo deve ser atualizado caso a apresentação mude de pasta junto com os vídeos.
- https://drive.google.com/file/d/1Ro6O4edXA-faLdYGMuQ423BoyrhPBXeQ/view?usp=drive_link

_5 imagem(ns) no slide._

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- Para responder
- Seguindo as orientações e procedimentos do vídeo, tente transcrever os três primeiros dígitos do seu CPF.

_4 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- Convertendo um número decimal em binário
- Para converter um número decimal em binário, siga os seguintes passos:
- Divida o número decimal por 2.
- Anote o resto da divisão (0 ou 1).
- Divida o resultado inteiro da primeira divisão por 2 novamente.
- Anote o resto da segunda divisão (0 ou 1).
- Continue dividindo e anotando os restos até chegar a 0.
- Escreva os restos em ordem reversa, do último para o primeiro. Essa será a representação em binário do número decimal.
- Por exemplo, vamos converter o número decimal 26 em binário:

_3 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Convertendo um número decimal em binário
- Por exemplo, vamos converter o número decimal 26 em binário:
- 26 ÷ 2 = 13, resto 0
- 13 ÷ 2 = 6, resto 1
- 6 ÷ 2 = 3, resto 0
- 3 ÷ 2 = 1, resto 1
- 1 ÷ 2 = 0, resto 1
- Os restos em ordem reversa são 11010, então a representação em binário de 26 é 11010.

_3 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- Para responder
- A operação de computadores digitais é baseada no armazenamento e processamento de dados binários. Considerando o início em zero, o sistema de numeração binária tem a mesma representação do sistema decimal até o número:
- a) 9.
- b) 15.
- c) 1.
- d) 16.
- Discutam em duplas e socializem as ideias com a turma.

_4 imagem(ns) no slide._

### Slide 13

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- A operação de computadores digitais é baseada no armazenamento e processamento de dados binários. Considerando o início em zero, o sistema de numeração binária tem a mesma representação do sistema decimal até o número:
- a) 9.
- b) 15.
- c) 1.
- d) 16.

_3 imagem(ns) no slide._

### Slide 14

- DESENVOLVIMENTO DE SISTEMAS
- Para responder

| Valor | Decimal | Binário |
| --- | --- | --- |
| Zero |  |  |
| Um |  |  |
| Dois |  |  |

- Anote no seu caderno!

_4 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Anote no seu caderno!

| Valor | Decimal | Binário |
| --- | --- | --- |
| Zero | 0 | 0 |
| Um | 1 | 1 |
| Dois | 2 | 10 |

_4 imagem(ns) no slide._

### Slide 16

- DESENVOLVIMENTO DE SISTEMAS
- O desafio Buscar entender uma problemática aplicando o que foi aprendido na aula de hoje.
- Prontos para criar uma solução?
- Vamos Praticar?

_4 imagem(ns) no slide._

### Slide 17

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje
- Um número binário é uma representação de qualquer outro número, simples ou complexo, com apenas 2 dígitos: 0 e 1.

_4 imagem(ns) no slide._

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- Pronto para desbloquear sua carreira de TI?
- Está perdido estudando mas não sabe por onde começar? Se a resposta é sim, você está no lugar certo! Descubra as estratégias e ferramentas essenciais para te ajudar a desbloquear seu potencial em TI e buscar sua primeira vaga de emprego no setor!
- Este e-book é um guia completo para quem busca começar pelos melhores caminhos para se tornar um excelente profissional de TI, ensinando a identificar perfis profissionais, aplicar técnicas de estudo eficazes, transformar teoria em prática, e aumentar a visibilidade de seu trabalho no mercado de trabalho. Ideal para novatos e profissionais em transição.
- E o melhor, ele pode ser seu, inteiramente grátis!
- Basta clicar AQUI e realizar o seu cadastro com o seu @escola!

_6 imagem(ns) no slide._

### Slide 19

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

### Slide 20

- DESENVOLVIMENTO DE SISTEMAS
- O RCO+Aulas é um projeto da Secretaria de Estado da Educação do Paraná e está em constante revisão. Todos os slides são de uso exclusivo dos professores da Rede Pública de Ensino, com a finalidade específica de aplicação em sala de aula, sendo totalmente vedada a publicização, reutilização, reprodução total ou parcial para quaisquer outros fins.

_4 imagem(ns) no slide._

## Atividade

_Fonte: AULA 12_INTRODUÇÃO A COMPUTAÇÃO ATIVIDADE.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

INTRODUÇÃO A COMPUTAÇÃO

1ª SÉRIE

ATIVIDADE AULA 12

Questão 1

Os computadores utilizam um sistema de numeração em que todas as quantidades se representam com base em dois números, ou seja, zero e um. O sistema de numeração mencionado é o:

a) Decimal.

b) Hexadecimal.

c) Binário.

d) Octal.

Resposta comentada: A alternativa A está incorreta, pois o computador, não entende os números decimais que compreendemos. A alternativa B e D estão incorretas, pois o sistema de numeração hexadecimal e octal são sistemas de meio campo, que os desenvolvedores utilizam para não precisar digitar longos números representados no sistema binário. A alternativa C está correta, pois este é o nome dado ao sistema que utiliza dois símbolos para ser representado (zero e um).

Questão 2

Um computador processa os dados por meio de pequenos conjuntos dados, mais especificamente em conjuntos de 8 bits, cada bit pode receber um valor: 0 ou 1. Suponhamos que em um desses conjuntos processados pelo computador conste o que seria no sistema decimal o valor 11. Qual seria a representação em sistema binário deste valor?

a) 1 0 1.

b) 1 1 1.

c) 1 0 1 1.

d) 1 1 0 1.

Resposta comentada: Para transformarmos um número do sistema decimal para o binário, é preciso dividi-lo em 2 por várias vezes. Veja:

11 : 2 = 5; resto 1

5 : 2 = 2; resto 1

2 : 2 = 1; resto 0

Unificando o último resto com o último resultado e, da sequência e os demais restos do penúltimo ao primeiro resto: alternativa correta C) 1 0 1 1.

A título de curiosidade, os números em sistema decimal dos valores em sistema binário apresentado nas alternativas A, B e D, são respectivamente 5, 7 e 13.

## Prática

_Fonte: AULA 12_PRÁTICA INTRODUÇÃO A COMPUTAÇÃO.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

INTRODUÇÃO A COMPUTAÇÃO

1ª SÉRIE

AULA PRÁTICA 12

Resumo Explicativo:

O sistema de numeração binário é a base da computação moderna, pois os computadores utilizam apenas dois dígitos (0 e 1) para processar e armazenar informações. Enquanto os humanos utilizam comumente o sistema decimal (com dez dígitos de 0 a 9), os computadores representam números e operações por meio de combinações de bits. Converter números decimais em binários é uma habilidade fundamental para qualquer estudante de tecnologia, pois permite entender como os dados são manipulados internamente pelos sistemas computacionais. Esse conhecimento é essencial no desenvolvimento de sistemas, na programação de baixo nível e na otimização de algoritmos.

Estudo de Caso:

Cenário: Uma empresa de segurança digital está desenvolvendo um novo protocolo de criptografia baseado na conversão de números decimais em binários. Para garantir um funcionamento eficiente, a equipe precisa converter rapidamente números inteiros para a base binária antes de aplicá-los em algoritmos de segurança.

No entanto, um dos estagiários da empresa está com dificuldades para entender como funciona o processo de conversão de decimal para binário. Ele precisa compreender que a conversão ocorre através de divisões sucessivas por 2, armazenando os restos das divisões na ordem inversa.

Desafio:

- Como ensinar esse conceito de forma clara e eficiente para novos integrantes da equipe?
- Como garantir que os números sejam convertidos corretamente e sem erros manuais?
- Como automatizar esse processo para evitar desperdício de tempo?
A equipe de segurança precisa desenvolver uma solução que torne a conversão rápida, confiável e acessível para todos os desenvolvedores da empresa.

Questões:

- Liste os passos necessários para converter um número decimal em binário manualmente.
- Explique, com suas palavras, por que os computadores utilizam o sistema binário ao invés do sistema decimal.
- Converta manualmente o número decimal 25 para binário e justifique cada etapa da conversão.
- Analise a relação entre os bits de um número binário e seu valor decimal correspondente. Como a posição de cada bit afeta o valor do número?
- Avalie a eficiência de diferentes métodos para converter números decimais em binários. Você considera que a conversão manual é mais eficiente do que a conversão programada? Justifique sua resposta.
- Desenvolva um pequeno algoritmo em Python que converta qualquer número decimal para binário. Explique como seu código funciona e quais são suas vantagens em relação ao processo manual.
