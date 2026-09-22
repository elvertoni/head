---
titulo: "Gerando números aleatórios"
tipo: rco-seed
disciplina: programacao-no-desenvolvimento-de-sistemas
sigla_rco: PDS
trimestre: 1
ordem_rco: 6
serie: 3
aula_rco: "Aula 06"
slides: 26
tem_atividade: true
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PDS/1TRI/6-gerando-numeros-aleatorios/6-gerando-numeros-aleatorios.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PDS/1TRI/6-gerando-numeros-aleatorios/AULA 06_ATIVIDADE_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PDS/1TRI/6-gerando-numeros-aleatorios/AULA 06_SAIBA MAIS_ PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Gerando números aleatórios

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO NO
- DESENVOLVIMENTO DE
- SISTEMAS
- 3ª SÉRIE
- Gerando números aleatórios
- Aula 06

_3 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- DESENVOLVIMENTO DE SISTEMAS
- Na aula de hoje vamos:
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store
- Gerar números aleatórios em Python e como aplicá-los ao nosso jogo de adivinhação. Discutiremos o módulo random e como ele pode ser usado para criar experiências de jogo dinâmicas e imprevisíveis.

_7 imagem(ns) no slide._

### Slide 4

- DESENVOLVIMENTO DE SISTEMAS
- ATENÇÃO PROFESSOR!
- O Material aqui apresentado, segue a análise do plano de curso contemplando os componentes curriculares e seus objetos de conhecimento, sendo assim, você tem liberdade para customizar o material conforme seu contexto para maior aproveitamento do conteúdo. Em caso de falta ou indisponibilidade de acesso à internet no local de aula, você poderá utilizar os seguintes artigos para criação de material complementar para auxiliar na aula:
- Leitura/Recursos Adicionais:
- "Automate the Boring Stuff with Python" por Al Sweigart.
- Documentação do Python sobre o módulo random: Python Docs - Random.
- Ferramenta on line para codificação python:
- https://www.online-python.com/

_5 imagem(ns) no slide._

### Slide 5

- DESENVOLVIMENTO DE SISTEMAS
- Na aula anterior…
- Exploramos diferentes métodos de iteração no contexto do nosso jogo de adivinhação em Python, focando no uso de loops for com range() e variações do loop while para controlar as tentativas do jogador.

_4 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Pense em maneiras de equilibrar o desafio e a jogabilidade justa em um jogo de adivinhação!
- Quem sabe responde!
- Como a aleatoriedade afeta a experiência do jogador?

_5 imagem(ns) no slide._

### Slide 7

- Resposta
- A aleatoriedade torna o jogo mais desafiador e interessante. No entanto, é essencial equilibrar a dificuldade para manter o jogo justo e agradável.
- DESENVOLVIMENTO DE SISTEMAS

_4 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Módulo random
- Este módulo pode criar situações imprevisíveis, aumentando a diversão e o desafio. O random possui várias funções, com randint sendo a mais utilizada para gerar inteiros aleatórios.
- O módulo random do Python oferece funcionalidades para gerar números aleatórios.

_4 imagem(ns) no slide._

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- random.randint() para Jogos
- random.randint(a, b) gera um inteiro aleatório N, onde a <= N <= b. No nosso jogo, essa função cria o elemento surpresa, gerando o número que os jogadores tentarão adivinhar. Isso garante que cada rodada do jogo seja única.

_4 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- Implicações da Aleatoriedade
- A aleatoriedade aumenta
- o fator replay do jogo.
- Ao garantir que cada partida seja diferente, mantém os jogadores engajados e desafiados, pois eles não podem simplesmente memorizar as respostas.

_4 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Aplicação Prática no Jogo
- Implementamos a aleatoriedade no jogo de adivinhação utilizando random.randint(). Isso é feito no início de cada jogo para definir o número alvo, criando uma nova experiência a cada rodada.

_4 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- Considerações sobre Aleatoriedade
- Embora a aleatoriedade adicione excitação, é importante equilibrá-la com regras claras e um design de jogo justo.
- Isso assegura que o jogo permaneça desafiador, mas não frustrante!

_4 imagem(ns) no slide._

### Slide 13

- DESENVOLVIMENTO DE SISTEMAS
- Melhores Práticas
- Ao usar números aleatórios, é importante considerar o impacto na experiência do jogador. Por exemplo, limitar o intervalo de números aleatórios pode ajudar a manter o jogo acessível para iniciantes, enquanto expandi-lo pode aumentar o desafio para jogadores experientes.

_4 imagem(ns) no slide._

### Slide 14 (oculto)

- DESENVOLVIMENTO DE SISTEMAS
- Exemplo atividade para Professor
- Demonstração de código com a implementação de random.randint() no jogo de adivinhação:
- Clique no ícone do
- saiba mais!

_4 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- Atividade para a fixação do conteúdo estudado
- Como gerar um número aleatório entre 1 e 50 em Python?
- (A) random.random(1, 50)
- (B) random.randint(1, 50)
- (C) random.range(1, 50)
- (D) random.number(1, 50)
- Responda em seu caderno!

_5 imagem(ns) no slide._

### Slide 16

- DESENVOLVIMENTO DE SISTEMAS
- Resposta correta
- Como gerar um número aleatório entre 1 e 50 em Python?
- (A) random.random(1, 50)
- (B) random.randint(1, 50)
- (C) random.range(1, 50)
- (D) random.number(1, 50)
- Resposta correta: (B) random.randint(1, 50)

_3 imagem(ns) no slide._

> **Notas do apresentador:** Comentário: random.randint(1, 50) é a função correta para gerar um número inteiro aleatório entre 1 e 50.

### Slide 17

- DESENVOLVIMENTO DE SISTEMAS
- Divida a turma em grupos.
- Cada grupo desenvolverá um jogo de adivinhação em Python, utilizando o módulo random para gerar o número secreto.
- Os grupos utilizarão o ChatGPT para gerar dicas e interações com o jogador durante o jogo.
- Os alunos serão incentivados a explorar a criatividade na elaboração das interações com o ChatGPT.
- Professor:

_4 imagem(ns) no slide._

> **Notas do apresentador:** Proposta de atividade: https://docs.google.com/document/d/1oC4p-W95ml-B3P-Qz2YJIoqjs9MHJo2L/edit?usp=sharing&ouid=118279643127441140656&rtpof=true&sd=true

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- Conclusão
- A geração de números aleatórios desempenha um papel fundamental na criação de jogos, incluindo o nosso jogo de adivinhação. Essa técnica introduz um elemento de incerteza, tornando o jogo mais emocionante e variado.

_4 imagem(ns) no slide._

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- Atividade Prática na Plataforma Alura
- Na plataforma Alura vamos acessar o seguinte curso:
- A recomendação é que você continue esse curso extraclasse, pois ele traz um conteúdo essencial para compreender sobre o referido tema.
- Link para o curso: https://cursos.alura.com.br/course/python-introducao-a-linguagem

_5 imagem(ns) no slide._

### Slide 20

- DESENVOLVIMENTO DE SISTEMAS
- Gerando e arredondando um número aleatório
- 10 minutos
- Link para tarefa: https://cursos.alura.com.br/course/python-introducao-a-linguagem/task/22694
- A lógica principal do nosso jogo já está funcionando, mas ainda há um detalhe, o número secreto não é tão secreto assim, pois ele está fixo! Então vamos alterar isso, para que ele passe a ser um número aleatório, coisa que veremos nesse capítulo.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 21

- DESENVOLVIMENTO DE SISTEMAS
- Definindo um intervalo para a geração de números aleatórios
- 8 minutos
- Link para tarefa: https://cursos.alura.com.br/course/python-introducao-a-linguagem/task/22847
- A ideia de multiplicar o número por 100 parece funcionar, mas podemos lembrar que o número gerado é entre 0.0 e 1.0, que quando multiplicado por 100 fica entre 0 e 100. Só que o nosso jogo não aceita o 0!
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 22

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje:
- Exploramos a geração de números aleatórios em Python e aplicamos isso ao nosso jogo de adivinhação.
- Na próxima aula, adicionaremos níveis de dificuldade e pontuação para enriquecer a experiência do jogo.

_4 imagem(ns) no slide._

### Slide 23

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

### Slide 24

- DESENVOLVIMENTO DE SISTEMAS
- Referências (Imagens)
- Figuras e Imagens:
- https://www.flaticon.com/br
- https://www.istockphoto.com/br
- https://raw.githubusercontent.com/zbtang/React-Native-ViewPager/HEAD/imgs/dotIndicator.gif
- https://storyset.com

_3 imagem(ns) no slide._

### Slide 25

- DESENVOLVIMENTO DE SISTEMAS
- O RCO+Aulas é um projeto da Secretaria de Estado da Educação do Paraná e está em constante revisão. Todos os slides são de uso exclusivo dos professores da Rede Pública de Ensino, com a finalidade específica de aplicação em sala de aula, sendo totalmente vedada a publicização, reutilização, reprodução total ou parcial para quaisquer outros fins.

_4 imagem(ns) no slide._

### Slide 26

- DESENVOLVIMENTO DE SISTEMAS
- Esta publicação tem a cooperação entre a UNESCO e a Secretaria de Estado da Educação e do Esporte do Paraná no âmbito da parceria PRODOC 914BRZ1091, cujo objetivo é trazer soluções inovadoras de gestão da rede pública estadual de educação do Paraná para a melhoria da aprendizagem dos alunos. As indicações de nomes e a apresentação do material ao longo desta publicação não implicam a manifestação de qualquer opinião por parte da UNESCO a respeito da condição jurídica de qualquer país, território, cidade, região ou de suas autoridades, tampouco da delimitação de suas fronteiras ou limites As ideias e opiniões expressas nesta publicação são as dos autores e não refletem obrigatoriamente as da UNESCO nem comprometem a Organização.
- Cooperação Técnica

_4 imagem(ns) no slide._

## Atividade

_Fonte: AULA 06_ATIVIDADE_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

ATIVIDADE AULA 06

Questão 1

Qual função do módulo random é usada para gerar um número inteiro aleatório dentro de um intervalo especificado?

a) random.random()

b) random.choice()

c) random.randint()

d) random.shuffle()

Resposta correta: c) random.randint()

Comentário: random.randint(a, b) gera um número inteiro aleatório N tal que a <= N <= b.

Questão 2

Por que é importante usar números aleatórios em jogos como o de adivinhação?

a) Para aumentar a dificuldade

b) Para garantir a imprevisibilidade

c) Para facilitar a programação

d) Para testar a habilidade do jogador

Resposta correta: b) Para garantir a imprevisibilidade

Comentário: Números aleatórios garantem que cada sessão do jogo seja única e imprevisível, aumentando o desafio e o interesse.

## Outros documentos

_Fonte: AULA 06_SAIBA MAIS_ PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

SAIBA MAIS AULA 06

Exemplo 1: jogo de adivinhação modificado

import random

def jogar_adivinhacao():

print("Bem-vindo ao jogo de adivinhação!")

print("Tente adivinhar o número que estou pensando, entre 1 e 50.")

# Gera um número aleatório entre 1 e 50

numero_secreto = random.randint(1, 50)

max_tentativas = 5

for tentativa in range(1, max_tentativas + 1):

print(f"Tentativa {tentativa} de {max_tentativas}")

palpite = int(input("Digite seu palpite: "))

if palpite < 1 or palpite > 50:

print("Digite um número entre 1 e 50.")

continue

acertou = palpite == numero_secreto

maior = palpite > numero_secreto

menor = palpite < numero_secreto

if acertou:

print(f"Parabéns! Você acertou o número em {tentativa} tentativas.")

break

else:

if maior:

print("Seu palpite foi maior que o número secreto.")

elif menor:

print("Seu palpite foi menor que o número secreto.")

if not acertou:

print(f"Suas tentativas acabaram. O número era {numero_secreto}.")

print("Fim do jogo!")

if __name__ == "__main__":

jogar_adivinhacao()
