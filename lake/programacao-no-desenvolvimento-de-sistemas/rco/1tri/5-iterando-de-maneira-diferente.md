---
titulo: "Iterando de maneira diferente"
tipo: rco-seed
disciplina: programacao-no-desenvolvimento-de-sistemas
sigla_rco: PDS
trimestre: 1
ordem_rco: 5
serie: 3
aula_rco: "Aula 05"
slides: 25
tem_atividade: true
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PDS/1TRI/5-iterando-de-maneira-diferente/5-iterando-de-maneira-diferente.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PDS/1TRI/5-iterando-de-maneira-diferente/AULA 05_ATIVIDADE_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PDS/1TRI/5-iterando-de-maneira-diferente/AULA 05_SAIBA MAIS_ PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Iterando de maneira diferente

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO NO
- DESENVOLVIMENTO DE
- SISTEMAS
- 3ª SÉRIE
- Iterando de maneira diferente
- Aula 05

_3 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- DESENVOLVIMENTO DE SISTEMAS
- Na aula de hoje vamos:
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store
- Explorar maneiras avançadas de iterar em Python, aplicando-as ao nosso jogo de adivinhação, controlando o número de tentativas e variando a dificuldade.

_7 imagem(ns) no slide._

### Slide 4

- DESENVOLVIMENTO DE SISTEMAS
- ATENÇÃO PROFESSOR!
- O Material aqui apresentado, segue a análise do plano de curso contemplando os componentes curriculares e seus objetos de conhecimento, sendo assim, você tem liberdade para customizar o material conforme seu contexto para maior aproveitamento do conteúdo. Em caso de falta ou indisponibilidade de acesso à internet no local de aula, você poderá utilizar os seguintes artigos para criação de material complementar para auxiliar na aula:
- Leitura/Recursos Adicionais:
- "Python for Data Analysis" por Wes McKinney
- Documentação do Python sobre loops e iterações: Python Docs - Control Flow Tools
- Ferramenta on line para codificação python:
- https://www.online-python.com/

_5 imagem(ns) no slide._

### Slide 5

- DESENVOLVIMENTO DE SISTEMAS
- Na aula anterior…
- Aprendemos a estruturar o jogo usando um loop while para permitir múltiplas tentativas e a lógica condicional if-elif-else para avaliar as respostas do jogador. Discutimos também sobre a importância do feedback ao usuário após cada tentativa, para tornar o jogo mais interativo e envolvente.
- Aprendemos a criar uma sequência de jogo de adivinhação em Python.

_4 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Considere as experiências do usuário!
- Como diferentes métodos de iteração podem afetar a jogabilidade e a dificuldade do nosso jogo de adivinhação?
- Realizem a atividade em duplas e socializem no final!

_5 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Diferentes métodos de iteração podem tornar o jogo mais previsível ou desafiador.
- Por exemplo, um loop com um número fixo de tentativas aumenta a tensão e a excitação.

_4 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Uso do for com range()
- A estrutura for combinada com range() é ideal para loops com um número definido de iterações. No contexto do jogo, for tentativa in range(max_tentativas): permite repetir o bloco de jogo um número específico de vezes, controlando as tentativas do jogador.

_4 imagem(ns) no slide._

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- Variações no Loop while
- Além do for, o loop while pode ser ajustado para adicionar complexidade ao jogo. Por exemplo, usando um contador de tentativas ou uma condição de saída baseada no estado do jogo, como um palpite correto ou o fim das tentativas.

_4 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- Controle de Tentativas
- Controlar o número de tentativas em um jogo de adivinhação adiciona um elemento estratégico. Isso pode ser feito definindo um limite de tentativas e usando um loop for ou while para contar as tentativas do jogador.

_4 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Aplicação Prática
- Adaptar o jogo para diferentes estruturas de loop envolve mudanças no código para incorporar o controle de tentativas.
- Isso inclui ajustar a lógica de verificação do palpite e a condição de término do jogo.
- https://www.codesdope.com/pa-images-bucket/courses/python/w1.gif

_4 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- Estratégias de Iteração
- A escolha entre while e for depende do design do jogo.
- for é preferível para um número fixo de tentativas, enquanto while é melhor para condições de saída mais flexíveis.

_4 imagem(ns) no slide._

### Slide 13

- DESENVOLVIMENTO DE SISTEMAS
- Dicas de Otimização
- Elaborar loops eficientes e facilmente compreensíveis requer a prevenção de loops infinitos, a adoção de nomes descritivos para variáveis e a implementação de uma lógica de saída adequada para encerrar o jogo de maneira clara e compreensível.

_4 imagem(ns) no slide._

### Slide 14 (oculto)

- DESENVOLVIMENTO DE SISTEMAS
- Exemplo atividade para Professor
- Para acessar o código adaptado do jogo de adivinhação, onde utilizamos um loop for com range() para limitar as tentativas do jogador, clique no Link do Saiba Mais!
- JOGO DE ADIVINHAÇÃO

_4 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- Atividade para a fixação do conteúdo estudado
- Qual estrutura de loop é ideal para adicionar um número fixo de tentativas em um jogo?
- (A) while
- (B) for
- (C) do-while
- (D) repeat
- Quem sabe responde!

_4 imagem(ns) no slide._

### Slide 16

- DESENVOLVIMENTO DE SISTEMAS
- Resposta correta
- Qual estrutura de loop é ideal para adicionar um número fixo de tentativas em um jogo?
- (A) while
- (B) for
- (C) do-while
- (D) Repeat
- Resposta correta: (B) for

_3 imagem(ns) no slide._

> **Notas do apresentador:** Comentário: for com range() é ideal para definir um número fixo de tentativas, proporcionando controle preciso sobre as iterações.

### Slide 17

- DESENVOLVIMENTO DE SISTEMAS
- Conclusão
- A capacidade de iterar de maneiras diferentes é uma habilidade valiosa em Python, especialmente em aplicações como jogos, onde o controle de fluxo é extremamente necessário.

_4 imagem(ns) no slide._

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- Atividade Prática na Plataforma Alura
- Na plataforma Alura vamos acessar o seguinte curso:
- A recomendação é que você continue esse curso extraclasse, pois ele traz um conteúdo essencial para compreender sobre o referido tema.
- Link para o curso: https://cursos.alura.com.br/course/python-introducao-a-linguagem

_5 imagem(ns) no slide._

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- O laço com for
- 9 minutos
- Link para tarefa: https://cursos.alura.com.br/course/python-introducao-a-linguagem/task/24567
- O laço for em Python é usado para iterar sobre uma sequência (como uma lista, tupla ou string) ou um intervalo de números gerados por range(). Sua estrutura, for variável in sequência: bloco_de_código, executa o bloco de código para cada elemento na sequência. É ideal para situações onde o número de iterações é conhecido ou definido.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 20

- DESENVOLVIMENTO DE SISTEMAS
- Encerrando a interação e o loop
- 9 minutos
- Link para tarefa: https://cursos.alura.com.br/course/python-introducao-a-linguagem/task/24569
- Para encerrar uma interação e sair de um loop em Python, usa-se a instrução break. Ela interrompe imediatamente o ciclo mais interno (seja for ou while) em que está inserida, independentemente da condição do loop. É útil para terminar loops antecipadamente quando uma condição específica é atendida.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 21

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje:
- Aprendemos como realizar iterações avançadas em Python, aplicadas ao nosso jogo de adivinhação, com ênfase no controle de tentativas e variação da dificuldade.
- Na próxima aula, exploraremos a geração de números aleatórios e suas aplicações.

_4 imagem(ns) no slide._

### Slide 22

- DESENVOLVIMENTO DE SISTEMAS
- Bibliografia
- PUREWAL, Semmy. Aprendendo a Desenvolver Aplicações Web. Desenvolva rapidamente com as tecnologias JavaScript mais modernas. São Paulo: Novatec, 2014.
- SILVA, L. F.; OLIVEIRA, A. D. de. Desenvolvimento de Software II C#: programação em camadas. [S. l.]: CBL Edição do Autor, 2017. E-book.
- MARTIN, R. C. Arquitetura limpa: o guia do artesão para estrutura e design de software. Rio de Janeiro: Alta Books, 2019. E-book.
- GALOTTI, G. M. A. Qualidade de software. São Paulo: Pearson Education do Brasil, 2016. E-book.
- VAZQUEZ, C. E.; SIMÕES, G. S. Engenharia de requisitos: software orientado ao negócio. São Paulo: Brasport, 2016. E-book.
- Softwares
- Java Netbeans; WebStorm; Sublime Text; Intellij IDEA; Astah Software; Netbeans; Python; Ccharp; Colab; PyCharm; Jupyter Notebook.
- Referências

_3 imagem(ns) no slide._

### Slide 23

- DESENVOLVIMENTO DE SISTEMAS
- Referências (Imagens)
- Figuras e Imagens:
- https://www.flaticon.com/br
- https://www.istockphoto.com/br
- https://raw.githubusercontent.com/zbtang/React-Native-ViewPager/HEAD/imgs/dotIndicator.gif
- https://storyset.com

_3 imagem(ns) no slide._

### Slide 24

- DESENVOLVIMENTO DE SISTEMAS
- O RCO+Aulas é um projeto da Secretaria de Estado da Educação do Paraná e está em constante revisão. Todos os slides são de uso exclusivo dos professores da Rede Pública de Ensino, com a finalidade específica de aplicação em sala de aula, sendo totalmente vedada a publicização, reutilização, reprodução total ou parcial para quaisquer outros fins.

_4 imagem(ns) no slide._

### Slide 25

- DESENVOLVIMENTO DE SISTEMAS
- Esta publicação tem a cooperação entre a UNESCO e a Secretaria de Estado da Educação e do Esporte do Paraná no âmbito da parceria PRODOC 914BRZ1091, cujo objetivo é trazer soluções inovadoras de gestão da rede pública estadual de educação do Paraná para a melhoria da aprendizagem dos alunos. As indicações de nomes e a apresentação do material ao longo desta publicação não implicam a manifestação de qualquer opinião por parte da UNESCO a respeito da condição jurídica de qualquer país, território, cidade, região ou de suas autoridades, tampouco da delimitação de suas fronteiras ou limites As ideias e opiniões expressas nesta publicação são as dos autores e não refletem obrigatoriamente as da UNESCO nem comprometem a Organização.
- Cooperação Técnica

_4 imagem(ns) no slide._

## Atividade

_Fonte: AULA 05_ATIVIDADE_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

ATIVIDADE AULA 05

Questão 1

Qual método em Python permite iterar sobre uma sequência de números com passos específicos?

a) while

b) for

c) iterate()

d) range()

Resposta correta: d) range()

Comentário: range() é usado em loops for para gerar sequências numéricas, permitindo definir início, fim e passos da iteração.

Questão 2

Como você modificaria o loop do jogo de adivinhação para limitar o número de tentativas?

a) Usar while com contador

b) Usar for com range()

c) Alterar a condição do while

d) Todas as opções acima são válidas

Resposta correta: d) Todas as opções acima são válidas

Comentário: Tanto a utilização de um contador em um loop while, quanto o uso de for com range(), são maneiras eficazes de limitar as tentativas no jogo.

## Outros documentos

_Fonte: AULA 05_SAIBA MAIS_ PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

SAIBA MAIS AULA 05

Exemplo 1: jogo de adivinhação

import random

# Gera um número aleatório entre 1 e 10

numero_secreto = random.randint(1, 10)

max_tentativas = 5

print("Bem-vindo ao jogo de adivinhação!")

print("Tente adivinhar o número que estou pensando, entre 1 e 10. Você tem 5 tentativas.")

# Loop do jogo com um número fixo de tentativas

for tentativa in range(max_tentativas):

# Captura a entrada do usuário

palpite = int(input(f"Tentativa {tentativa + 1}/{max_tentativas}. Digite seu palpite: "))

# Verifica o palpite do jogador

if palpite == numero_secreto:

print(f"Parabéns! Você acertou o número em {tentativa + 1} tentativas.")

break

elif palpite < numero_secreto:

print("Quase lá! Tente um número maior.")

else:

print("Quase lá! Tente um número menor.")

# Checa se esta é a última tentativa

if tentativa == max_tentativas - 1:

print(f"Suas tentativas acabaram. O número era {numero_secreto}.")

print("Fim do jogo!")
