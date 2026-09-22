---
titulo: "encerramento do jogo"
tipo: rco-seed
disciplina: programacao-no-desenvolvimento-de-sistemas
sigla_rco: PDS
trimestre: 1
ordem_rco: 14
serie: 3
aula_rco: "Aula 14"
slides: 24
tem_atividade: true
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/1TRI/14-implementando-o-encerramento-do-jogo/14-implementando-o-encerramento-do-jogo.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/1TRI/14-implementando-o-encerramento-do-jogo/AULA 14_ATIVIDADE_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/1TRI/14-implementando-o-encerramento-do-jogo/AULA 14_SAIBA MAIS_ PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# encerramento do jogo

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO NO
- DESENVOLVIMENTO DE
- SISTEMAS
- 3ª SÉRIE
- Implementando o
- encerramento do jogo
- Aula 14

_3 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- DESENVOLVIMENTO DE SISTEMAS
- Na aula de hoje vamos:
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store
- Abordar estratégias para implementar o encerramento do jogo após um número definido de tentativas erradas.

_7 imagem(ns) no slide._

### Slide 4

- DESENVOLVIMENTO DE SISTEMAS
- ATENÇÃO PROFESSOR!
- O Material aqui apresentado, segue a análise do plano de curso contemplando os componentes curriculares e seus objetos de conhecimento, sendo assim, você tem liberdade para customizar o material conforme seu contexto para maior aproveitamento do conteúdo. Em caso de falta ou indisponibilidade de acesso à internet no local de aula, você poderá utilizar os seguintes artigos para criação de material complementar para auxiliar na aula:
- Leitura/Recursos Adicionais:
- Leitura Sugerida: "Python Crash Course" por Eric Matthes, um capítulo dedicado a listas e estruturas de dados.
- IDE Online: Repl.it (https://repl.it) ou o Python Tutor (http://pythontutor.com), que permitem a execução de código Python online sem necessidade de instalação local.

_5 imagem(ns) no slide._

### Slide 5

- DESENVOLVIMENTO DE SISTEMAS
- Na aula anterior…
- Conhecemos o que são tuplas e a utilização em conjunto com listas.

_4 imagem(ns) no slide._

### Slide 6

- Para pensarmos juntos!
- Ele tem um
- desafio!
- DESENVOLVIMENTO DE SISTEMAS
- Imagine que Marcelo, um desenvolvedor iniciante, está criando seu primeiro jogo da forca em Python.
- https://media1.tenor.com/m/lFBYhj2pAGUAAAAC/pensando-pensativo.gif
- "Como usar listas para gerenciar as tentativas e decidir o momento certo para encerrar o jogo?"

_5 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Como Marcelo pode implementar o controle de tentativas erradas usando listas em Python?
- Registre a sua resposta e compartilhe!

_5 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Marcelo pode criar uma lista para armazenar cada tentativa errada do usuário!
- A cada erro, ele adiciona a tentativa à lista. Utilizando o tamanho
- dessa lista (len(lista_de_erros)),
- ele pode verificar se o
- número de tentativas
- erradas atingiu o
- limite estipulado para o jogo.
- Se sim, o jogo é encerrado com uma mensagem indicativa. Isso permite um controle eficaz e oferece ao jogador uma visão clara de quantas tentativas restam, melhorando a interação com o jogo.

_4 imagem(ns) no slide._

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- Implementando o
- Encerramento do Jogo
- No contexto do jogo da forca, isso geralmente ocorre quando o jogador adivinha corretamente a palavra ou excede o número permitido de tentativas erradas. A finalidade é garantir que o jogo tenha um ciclo de vida claro e proporcione uma experiência de início, meio e fim ao usuário.
- A implementação do encerramento do jogo envolve definir condições sob as quais o jogo deve terminar.

_4 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- Estipulando Tentativas de Erros
- Esse limite ajuda a aumentar a tensão e o desafio do jogo, incentivando o jogador a pensar cuidadosamente sobre cada palpite. Gerenciar as tentativas de erros também permite ao desenvolvedor ajustar a dificuldade do jogo.
- É o limite máximo de erros que o jogador pode cometer antes de o jogo terminar.

_4 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Compreensão de Lista
- No desenvolvimento de jogos, pode ser usada para gerar listas que armazenam, por exemplo, as letras já tentadas pelo jogador ou as letras que compõem a palavra secreta.
- A compreensão de listas é um recurso poderoso em Python que permite criar listas de maneira concisa e eficiente.

_4 imagem(ns) no slide._

### Slide 12 (oculto)

- DESENVOLVIMENTO DE SISTEMAS
- Exemplo Prático
- Clique aqui para acessar o projeto

_5 imagem(ns) no slide._

### Slide 13

- DESENVOLVIMENTO DE SISTEMAS
- Implementação
- Esses conceitos não só melhoram a lógica do jogo mas também proporcionam uma melhor experiência ao usuário, equilibrando desafio e jogabilidade.
- O encerramento do jogo, o controle das tentativas de erros e o uso de compreensão de listas são fundamentais para criar jogos desafiadores e envolventes em Python.

_4 imagem(ns) no slide._

### Slide 14

- DESENVOLVIMENTO DE SISTEMAS
- Atividade para a fixação do conteúdo estudado
- Qual comando em Python verifica se o número de tentativas erradas excede um limite estabelecido, encerrando o jogo?
- (A) if erros > 3: print("Game Over")
- (B) if len(erros) == 3: print("Game Over")
- (C) if len(erros) >= 3: print("Game Over")
- (D) if erros.count() > 3: print("Game Over")
- Quem sabe responde!

_4 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- Resposta certa
- Qual comando em Python verifica se o número de tentativas erradas excede um limite estabelecido, encerrando o jogo?
- (A) if erros > 3: print("Game Over")
- (B) if len(erros) == 3: print("Game Over")
- (C) if len(erros) >= 3: print("Game Over")
- (D) if erros.count() > 3: print("Game Over")
- Resposta Correta: (C) if len(erros) >= 3: print("Game Over")

_3 imagem(ns) no slide._

> **Notas do apresentador:** Comentário: A opção c é correta porque utiliza corretamente a função len() para obter o número de itens na lista erros e verifica se esse número é maior ou igual ao limite de erros permitidos antes de encerrar o jogo com uma mensagem "Game Over". Isso ilustra como controlar as tentativas erradas e decidir o momento de encerrar o jogo de maneira eficaz.

### Slide 16

- DESENVOLVIMENTO DE SISTEMAS
- Conclusão
- Implementar o encerramento do jogo e controlar as tentativas erradas com listas promove uma jogabilidade estruturada, melhorando a experiência do usuário ao fornecer desafios claros e limites definidos.

_4 imagem(ns) no slide._

### Slide 17

- DESENVOLVIMENTO DE SISTEMAS
- Atividade Prática na Plataforma Alura
- Na plataforma Alura vamos acessar o seguinte curso:
- A recomendação é que você continue esse curso extraclasse, pois ele traz um conteúdo essencial para compreender sobre o referido tema.
- Link para o curso: https://cursos.alura.com.br/course/python-3-avancando-na-linguagem

_5 imagem(ns) no slide._

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- Estipulando tentativas de erros
- 11 minutos
- Link para tarefa: https://cursos.alura.com.br/course/python-3-avancando-na-linguagem/task/25156
- Estipular tentativas de erros em jogos como o da forca permite definir um limite de erros permitidos, aumentando o desafio. Utiliza-se uma lista para armazenar e contar essas tentativas, encerrando o jogo quando o limite é atingido.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- Estipulando tentativas de erros
- 6 minutos
- Link para tarefa: https://cursos.alura.com.br/course/python-3-avancando-na-linguagem/task/25157
- A compreensão de lista em Python é uma forma concisa de criar listas. Ela permite gerar novas listas aplicando uma expressão a cada item de uma sequência existente, tudo em uma única linha de código, tornando o programa mais legível e eficiente.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 20

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje:
- Trabalhamos as técnicas do encerramento do jogo e estipular tentativas de erros usando listas, além de introduzir a compreensão de lista, essenciais para criar jogos interativos em Python.
- Na próxima aula, manipular arquivos em Python, incluindo escrita e leitura!

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

_Fonte: AULA 14_ATIVIDADE_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

ATIVIDADE AULA 14

Questão 1

Qual função em Python é usada para adicionar uma tentativa errada à lista de erros em um jogo?

a) erros.add('x')

b) append.erros('x')

c) erros.append('x')

d) add.erros('x')

Resposta Correta: c) erros.append('x')

Comentário: A opção c é a correta porque o método .append() é utilizado em listas para adicionar um item ao final da lista. Este método é fundamental para jogos que precisam registrar cada tentativa errada do jogador, atualizando a lista de erros.

Questão 2

Como você pode verificar se o número de tentativas erradas atingiu o limite para encerrar o jogo?

a) if erros == limite: print("Game Over")

b) if count(erros) >= limite: print("Game Over")

c) if len(erros) > limite: print("Game Over")

d) if len(erros) >= limite: print("Game Over")

Resposta Correta: d) if len(erros) >= limite: print("Game Over")

Comentário: A alternativa d é correta porque utiliza len(erros) para obter a quantidade de erros e compara esse número com o limite estipulado. Se o número de erros for maior ou igual ao limite, o jogo é encerrado, demonstrando uma maneira eficaz de controlar as tentativas e determinar o fim do jogo.

## Outros documentos

_Fonte: AULA 14_SAIBA MAIS_ PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

SAIBA MAIS AULA 14

Exemplo 1:.

palavra_secreta = "python"

tentativas_erradas = []

max_erros = 5

# Loop do jogo

while len(tentativas_erradas) < max_erros:

letra = input("Digite uma letra: ")

if letra not in palavra_secreta:

tentativas_erradas.append(letra)

print(f"Erros: {len(tentativas_erradas)} de {max_erros}")

if len(tentativas_erradas) == max_erros:

print("Você perdeu!")

break

Este exemplo mostra como as tentativas erradas são armazenadas em uma lista e como o jogo é encerrado quando o número de erros atinge o limite máximo.
