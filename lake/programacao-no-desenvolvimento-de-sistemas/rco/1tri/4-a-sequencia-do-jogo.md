---
titulo: "A sequência do jogo"
tipo: rco-seed
disciplina: programacao-no-desenvolvimento-de-sistemas
sigla_rco: PDS
trimestre: 1
ordem_rco: 4
serie: 3
aula_rco: "Aula 04"
slides: 24
tem_atividade: true
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/1TRI/4-a-sequencia-do-jogo/4-a-sequencia-do-jogo.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PDS/1TRI/4-a-sequencia-do-jogo/AULA 04_ATIVIDADE_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PDS/1TRI/4-a-sequencia-do-jogo/AULA 04_SAIBA MAIS_ PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# A sequência do jogo

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO NO
- DESENVOLVIMENTO DE
- SISTEMAS
- 3ª SÉRIE
- A sequência do jogo
- Aula 04

_3 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- DESENVOLVIMENTO DE SISTEMAS
- Na aula de hoje vamos:
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store
- Desenvolver um jogo de adivinhação básico em Python, abordando a geração de números aleatórios e o uso de loops while para processar as tentativas do usuário.

_7 imagem(ns) no slide._

### Slide 4

- DESENVOLVIMENTO DE SISTEMAS
- ATENÇÃO PROFESSOR!
- O Material aqui apresentado, segue a análise do plano de curso contemplando os componentes curriculares e seus objetos de conhecimento, sendo assim, você tem liberdade para customizar o material conforme seu contexto para maior aproveitamento do conteúdo. Em caso de falta ou indisponibilidade de acesso à internet no local de aula, você poderá utilizar os seguintes artigos para criação de material complementar para auxiliar na aula:
- Leitura/Recursos Adicionais:
- "Invent Your Own Computer Games with Python" por Al Sweigart
- Documentação do módulo random em Python: Python Docs – Random
- Ferramenta on line para codificação python:
- https://www.online-python.com/

_5 imagem(ns) no slide._

### Slide 5

- DESENVOLVIMENTO DE SISTEMAS
- Na aula anterior…
- Testamos valores em Python!
- Aprendemos sobre a utilização das estruturas condicionais if, elif e else para tomar decisões baseadas em diferentes condições. Utilizamos operadores de comparação para verificar igualdade, diferença, e outros relacionamentos entre variáveis. Examinamos exemplos práticos para entender melhor como essas estruturas são usadas em situações reais de programação.

_4 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Quais elementos podem ser adicionados para melhorar a experiência do jogador?
- Quem sabe responde!
- Considere um jogo onde o jogador tem que adivinhar um número entre 1 e 10.
- Como garantir que o jogo seja justo e divertido?

_5 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- O jogo deve gerar um número aleatório e dar feedback ao jogador após cada tentativa. Elementos como limitar o número de tentativas ou fornecer dicas podem tornar o jogo mais desafiador e interessante.

_4 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Geração de Números Aleatórios
- A função random.randint(start, end) gera um número inteiro aleatório entre os limites especificados, proporcionando a base para o jogo.
- Utilizamos o módulo random em Python para gerar números aleatórios, crucial em jogos de adivinhação.

_4 imagem(ns) no slide._

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- Estrutura do Loop while
- Em um jogo de adivinhação, ele é usado para permitir múltiplas tentativas até que o jogador acerte o número ou esgote as tentativas.
- O loop while permite repetir um bloco de código enquanto uma condição especificada é verdadeira.

_4 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- Captura de Entradas do Usuário
- A função input() captura as entradas do usuário, essencial em jogos interativos. Ela permite que os jogadores insiram suas adivinhações, que são então processadas pelo programa.

_4 imagem(ns) no slide._

### Slide 11

- Condições e Verificações
- DESENVOLVIMENTO DE SISTEMAS
- Essas estruturas permitem comparar a entrada do usuário com o número gerado aleatoriamente e decidir o fluxo do jogo.
- Usamos estruturas condicionais (if, elif, else) para avaliar as adivinhações dos jogadores.

_4 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- Feedback ao Usuário
- Informações como "muito alto", "muito baixo" ou "correto!" ajudam a orientar e motivar o jogador, além de tornar o jogo mais interativo e divertido.
- Oferecer feedback é essencial para manter o jogador envolvido!
- https://i.gifer.com/7SpJ.gif

_4 imagem(ns) no slide._

### Slide 13

- DESENVOLVIMENTO DE SISTEMAS
- Encerramento do Jogo
- Definimos critérios claros para o fim do jogo, como acertar o número ou esgotar o número de tentativas.
- Isso pode ser controlado por uma condição no loop while ou por uma estrutura condicional dentro do loop.

_4 imagem(ns) no slide._

### Slide 14

- DESENVOLVIMENTO DE SISTEMAS
- Atividade para a fixação do conteúdo estudado
- Responda em seu caderno!
- Qual função do Python é usada para ler a adivinhação do usuário?
- (A) get_input()
- (B) read()
- (C) input()
- (D) fetch()
- https://usagif.com/wp-content/uploads/2020/11/am0ngsusxh-71.gif

_5 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- Atividade para a fixação do conteúdo estudado
- Qual função do Python é usada para ler a adivinhação do usuário?
- (A) get_input()
- (B) read()
- (C) input()
- (D) fetch()
- Resposta correta: C) input()
- https://www.icegif.com/wp-content/uploads/2023/09/icegif-143.gif

_4 imagem(ns) no slide._

> **Notas do apresentador:** Comentário: A função input() é usada para ler entradas do usuário em Python.

### Slide 16

- DESENVOLVIMENTO DE SISTEMAS
- Conclusão
- Desenvolver um jogo de adivinhação é uma excelente maneira de praticar lógica de programação, estruturas de repetição e interação com o usuário em Python. Um exemplo do jogo em python está no arquivo saiba mais.

_5 imagem(ns) no slide._

### Slide 17

- DESENVOLVIMENTO DE SISTEMAS
- Atividade Prática na Plataforma Alura
- Na plataforma Alura vamos acessar o seguinte curso:
- A recomendação é que você continue esse curso extraclasse, pois ele traz um conteúdo essencial para compreender sobre o referido tema.
- Link para o curso: https://cursos.alura.com.br/course/python-introducao-a-linguagem

_5 imagem(ns) no slide._

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- O laço com while
- 11 minutos
- Link para tarefa: https://cursos.alura.com.br/course/python-introducao-a-linguagem/task/24543
- O laço while em Python repete um bloco de código enquanto uma condição especificada é verdadeira. É ideal para situações onde o número de iterações não é conhecido antecipadamente. A estrutura básica é while condição: bloco_de_código, executando o bloco de código até que a condição se torne falsa.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- Formatação de strings
- 4 minutos
- Link para tarefa: https://cursos.alura.com.br/course/python-introducao-a-linguagem/task/24546
- A formatação de strings em Python pode ser feita de várias maneiras. As mais comuns incluem o uso do método format(), como em "{} {}".format(var1, var2), e f-strings, introduzidas no Python 3.6, como em f"{var1} {var2}". Ambos os métodos permitem a inserção de variáveis e expressões dentro de strings, facilitando a criação de mensagens dinâmicas e formatadas.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 20

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje:
- Na próxima aula, aprofundaremos os nossos estudos sobre iterações e manipulação de dados!
- Aprendemos a criar um jogo de adivinhação em Python, desde a geração de números aleatórios até o feedback interativo com o usuário.

_4 imagem(ns) no slide._

### Slide 21

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

### Slide 22

- DESENVOLVIMENTO DE SISTEMAS
- Referências (Imagens)
- Figuras e Imagens:
- https://www.flaticon.com/br
- https://www.istockphoto.com/br
- https://raw.githubusercontent.com/zbtang/React-Native-ViewPager/HEAD/imgs/dotIndicator.gif
- https://storyset.com

_3 imagem(ns) no slide._

### Slide 23

- DESENVOLVIMENTO DE SISTEMAS
- O RCO+Aulas é um projeto da Secretaria de Estado da Educação do Paraná e está em constante revisão. Todos os slides são de uso exclusivo dos professores da Rede Pública de Ensino, com a finalidade específica de aplicação em sala de aula, sendo totalmente vedada a publicização, reutilização, reprodução total ou parcial para quaisquer outros fins.

_4 imagem(ns) no slide._

### Slide 24

- DESENVOLVIMENTO DE SISTEMAS
- Esta publicação tem a cooperação entre a UNESCO e a Secretaria de Estado da Educação e do Esporte do Paraná no âmbito da parceria PRODOC 914BRZ1091, cujo objetivo é trazer soluções inovadoras de gestão da rede pública estadual de educação do Paraná para a melhoria da aprendizagem dos alunos. As indicações de nomes e a apresentação do material ao longo desta publicação não implicam a manifestação de qualquer opinião por parte da UNESCO a respeito da condição jurídica de qualquer país, território, cidade, região ou de suas autoridades, tampouco da delimitação de suas fronteiras ou limites As ideias e opiniões expressas nesta publicação são as dos autores e não refletem obrigatoriamente as da UNESCO nem comprometem a Organização.
- Cooperação Técnica

_4 imagem(ns) no slide._

## Atividade

_Fonte: AULA 04_ATIVIDADE_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

ATIVIDADE AULA 04

Questão 1

Qual estrutura de repetição é mais adequada para um jogo de adivinhação onde o número de tentativas é desconhecido?

a) for

b) while

c) do-while

d) foreach

Resposta correta: b) while

Comentário: while é ideal para loops com um número indeterminado de iterações, como em um jogo de adivinhação onde o jogador continua tentando até acertar.

Questão 2

Como gerar um número aleatório entre 1 e 10 em Python?

a) random.randint(1, 10)

b) random.range(1, 10)

c) random.number(1, 10)

d) random(1, 10)

Resposta correta: a) random.randint(1, 10)

Comentário: A função random.randint(1, 10) do módulo random gera um número inteiro aleatório entre 1 e 10.

## Outros documentos

_Fonte: AULA 04_SAIBA MAIS_ PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

SAIBA MAIS AULA 04

Exemplo 1: jogo de adivinhação

import random

# Gera um número aleatório entre 1 e 10

numero_secreto = random.randint(1, 10)

tentativas = 0

max_tentativas = 5

print("Bem-vindo ao jogo de adivinhação!")

print("Tente adivinhar o número que estou pensando, entre 1 e 10.")

# Loop do jogo

while tentativas < max_tentativas:

# Captura a entrada do usuário

palpite = int(input("Digite seu palpite: "))

# Incrementa o número de tentativas

tentativas += 1

# Verifica o palpite do jogador

if palpite == numero_secreto:

print(f"Parabéns! Você acertou o número em {tentativas} tentativas.")

break

elif palpite < numero_secreto:

print("Quase lá! Tente um número maior.")

else:

print("Quase lá! Tente um número menor.")

# Informa ao jogador quantas tentativas restam

if tentativas < max_tentativas:

print(f"Você tem {max_tentativas - tentativas} tentativas restantes.")

else:

print("Infelizmente, você não acertou. O número era", numero_secreto)

print("Fim do jogo!")
