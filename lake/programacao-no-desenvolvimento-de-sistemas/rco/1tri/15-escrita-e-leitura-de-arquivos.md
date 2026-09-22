---
titulo: "Escrita e leitura de arquivos"
tipo: rco-seed
disciplina: programacao-no-desenvolvimento-de-sistemas
sigla_rco: PDS
trimestre: 1
ordem_rco: 15
serie: 3
aula_rco: "Aula 15"
slides: 27
tem_atividade: true
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/1TRI/15-escrita-e-leitura-de-arquivos/15-escrita-e-leitura-de-arquivos.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PDS/1TRI/15-escrita-e-leitura-de-arquivos/AULA 15_SAIBA MAIS_ PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/1TRI/15-escrita-e-leitura-de-arquivos/AULA 15_ATIVIDADE_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Escrita e leitura de arquivos

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO NO
- DESENVOLVIMENTO DE
- SISTEMAS
- 3ª SÉRIE
- Escrita e leitura de arquivos
- Aula 15

_3 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- DESENVOLVIMENTO DE SISTEMAS
- Na aula de hoje vamos:
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store
- Manipular arquivos em Python, incluindo escrita e leitura, além de escolher uma palavra de um arquivo para aplicações práticas.

_6 imagem(ns) no slide._

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
- Exploramos a implementação do encerramento do jogo, onde com determinada quantidade de erros ele iria encerrar.

_4 imagem(ns) no slide._

### Slide 6

- Para pensarmos juntos!
- João, um jovem programador, está desenvolvendo um jogo de forca em Python para seu portfólio…
- Ele quer aprimorar o jogo, escolhendo palavras aleatoriamente de um arquivo de texto, mas não sabe como ler ou escrever em arquivos com Python.
- Como João pode ler uma lista de palavras de um arquivo e escolher uma aleatoriamente para o jogo?
- DESENVOLVIMENTO DE SISTEMAS

_4 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Como João pode ler palavras de um arquivo e escolher uma aleatoriamente para seu jogo de forca em Python?
- Quem sabe responde!

_5 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Primeiro, ele abre o arquivo em modo de leitura, lê seu conteúdo, divide as palavras em uma lista e, então, usa random.choice() para selecionar uma palavra aleatoriamente. Isso não apenas resolve seu problema, mas também o introduz à manipulação de arquivos, uma habilidade valiosa para qualquer desenvolvedor.
- João pode usar o módulo random junto com as funções open(), read() e split() do Python.

_5 imagem(ns) no slide._

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- Resposta:
- Ao dominar a leitura e escrita de arquivos, João pode expandir significativamente a funcionalidade de seus projetos, armazenando dados externos e configurando jogos de forma mais dinâmica.

_4 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- Introdução
- Essas operações permitem que um programa persista dados entre as execuções, leia informações de configuração, ou até mesmo selecione elementos aleatórios de uma lista pré-definida, como palavras para um jogo da forca.
- No contexto da programação, especialmente ao desenvolver jogos ou aplicativos que necessitam de um conjunto dinâmico de dados, como um jogo da forca, a habilidade de escrever e ler arquivos torna-se fundamental.

_4 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Escrevendo em um Arquivo
- Escrever em um arquivo em Python é realizado usando a função open() com o modo 'w' (write) ou 'a' (append). O modo 'w' cria um novo arquivo ou sobrescreve o existente, enquanto 'a' adiciona ao final do arquivo sem apagar seu conteúdo atual.
- Isso é útil para atualizar logs, resultados de jogos ou listas de palavras.

_4 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- Lendo um Arquivo
- Ler um arquivo envolve abrir o arquivo em modo de leitura ('r') e utilizar métodos como .read(), .readline() ou .readlines() para acessar seu conteúdo.
- Isso permite ao programa obter dados necessários para sua execução, como carregar uma lista de palavras para um jogo.

_4 imagem(ns) no slide._

### Slide 13

- DESENVOLVIMENTO DE SISTEMAS
- Escolhendo uma Palavra
- Após ler as palavras de um arquivo, podemos escolher uma aleatoriamente usando o módulo random. Isso permite diversificar a experiência do usuário em jogos, como o da forca, ao não repetir constantemente as mesmas palavras.

_4 imagem(ns) no slide._

### Slide 14

- DESENVOLVIMENTO DE SISTEMAS
- Finalidade e Utilização
- A escrita e leitura de arquivos ampliam significativamente as possibilidades de um programa, permitindo a manipulação de uma grande quantidade de dados de forma eficiente e a criação de experiências de usuário mais ricas e variadas.
- Por exemplo, um jogo da forca que escolhe palavras de um vasto arquivo de texto oferece um desafio novo e interessante a cada rodada.

_4 imagem(ns) no slide._

### Slide 15 (oculto)

- DESENVOLVIMENTO DE SISTEMAS
- Exemplos
- Clique aqui para ter acesso aos arquivos do projeto!

_5 imagem(ns) no slide._

### Slide 16

- DESENVOLVIMENTO DE SISTEMAS
- Atividade para a fixação do conteúdo estudado
- Qual método é usado para ler todas as linhas de um arquivo de texto em Python e armazená-las como uma lista, permitindo a escolha de uma palavra aleatoriamente?
- (A) file.read()
- (B) file.readlines()
- (C) file.readline()
- (D) file.read().splitlines()
- Responda em seu caderno!

_4 imagem(ns) no slide._

### Slide 17

- DESENVOLVIMENTO DE SISTEMAS
- Resposta correta
- Qual método é usado para ler todas as linhas de um arquivo de texto em Python e armazená-las como uma lista, permitindo a escolha de uma palavra aleatoriamente?
- (A) file.read()
- (B) file.readlines()
- (C) file.readline()
- (D) file.read().splitlines()
- Resposta Correta: (D) file.read().splitlines()

_3 imagem(ns) no slide._

> **Notas do apresentador:** Comentário: A opção d é correta porque file.read().splitlines() lê todo o conteúdo do arquivo como uma string única e, em seguida, usa .splitlines() para dividir essa string em uma lista de linhas, removendo os caracteres de nova linha. Isso facilita o processo de escolher uma palavra aleatoriamente da lista sem preocupações adicionais sobre o manuseio de caracteres de nova linha.

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- Conclusão
- A manipulação de arquivos em Python para leitura e escrita amplia a dinâmica de jogos, como o da forca, permitindo a utilização de dados externos para uma experiência renovada a cada partida.

_4 imagem(ns) no slide._

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- Atividade Prática na Plataforma Alura
- Na plataforma Alura vamos acessar o seguinte curso:
- A recomendação é que você continue esse curso extraclasse, pois ele traz um conteúdo essencial para compreender sobre o referido tema.
- Link para o curso: https://cursos.alura.com.br/course/python-3-avancando-na-linguagem

_5 imagem(ns) no slide._

### Slide 20

- DESENVOLVIMENTO DE SISTEMAS
- Escrevendo em um arquivo
- 9 minutos
- Link para tarefa: https://cursos.alura.com.br/course/python-3-avancando-na-linguagem/task/25158
- Para escrever em um arquivo em Python, use open('arquivo.txt', 'w') para abrir (criando se não existir) e write() para adicionar conteúdo. Exemplo: with open('arquivo.txt', 'w') as f: f.write('Hello, world!'). Fecha automaticamente com with.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 21

- DESENVOLVIMENTO DE SISTEMAS
- Lendo um arquivo
- 7 minutos
- Link para tarefa: https://cursos.alura.com.br/course/python-3-avancando-na-linguagem/task/25164
- Para ler um arquivo em Python, utilize open('arquivo.txt', 'r') e o método read() para acessar seu conteúdo. Por exemplo: with open('arquivo.txt', 'r') as f: conteudo = f.read(). Isso lê todo o conteúdo do arquivo para a variável conteudo.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 22

- DESENVOLVIMENTO DE SISTEMAS
- Escolhendo uma palavra
- 8 minutos
- Link para tarefa: https://cursos.alura.com.br/course/python-3-avancando-na-linguagem/task/25166
- Para escolher uma palavra aleatória de um arquivo em Python, primeiramente leia o arquivo e divida as palavras em uma lista usando splitlines(). Em seguida, utilize random.choice(lista) para selecionar uma palavra. Exemplo: palavra = random.choice(open('palavras.txt').read().splitlines()).
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 23

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje:
- Aprendemos a escrever e ler arquivos em Python, abordando métodos para adicionar, acessar conteúdo e selecionar palavras aleatoriamente para o jogo desenvolvido.
- Na próxima aula, estudaremos as técnicas de aprimoramento, legibilidade e manutenção do código.

_4 imagem(ns) no slide._

### Slide 24

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

### Slide 25

- DESENVOLVIMENTO DE SISTEMAS
- Referências (Imagens)
- Figuras e Imagens:
- https://www.flaticon.com/br
- https://www.istockphoto.com/br
- https://raw.githubusercontent.com/zbtang/React-Native-ViewPager/HEAD/imgs/dotIndicator.gif
- https://storyset.com

_3 imagem(ns) no slide._

### Slide 26

- DESENVOLVIMENTO DE SISTEMAS
- O RCO+Aulas é um projeto da Secretaria de Estado da Educação do Paraná e está em constante revisão. Todos os slides são de uso exclusivo dos professores da Rede Pública de Ensino, com a finalidade específica de aplicação em sala de aula, sendo totalmente vedada a publicização, reutilização, reprodução total ou parcial para quaisquer outros fins.

_4 imagem(ns) no slide._

### Slide 27

- DESENVOLVIMENTO DE SISTEMAS
- Esta publicação tem a cooperação entre a UNESCO e a Secretaria de Estado da Educação e do Esporte do Paraná no âmbito da parceria PRODOC 914BRZ1091, cujo objetivo é trazer soluções inovadoras de gestão da rede pública estadual de educação do Paraná para a melhoria da aprendizagem dos alunos. As indicações de nomes e a apresentação do material ao longo desta publicação não implicam a manifestação de qualquer opinião por parte da UNESCO a respeito da condição jurídica de qualquer país, território, cidade, região ou de suas autoridades, tampouco da delimitação de suas fronteiras ou limites As ideias e opiniões expressas nesta publicação são as dos autores e não refletem obrigatoriamente as da UNESCO nem comprometem a Organização.
- Cooperação Técnica

_4 imagem(ns) no slide._

## Atividade

_Fonte: AULA 15_ATIVIDADE_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

ATIVIDADE AULA 15

Questão 1

Quando você quer adicionar mais conteúdo a um arquivo sem apagar o que já existe, qual modo de abertura você deve usar?

a) 'r+'

b) 'w'

c) 'a'

d) 'wb'

Resposta Correta: c) 'a'

Comentário: A opção c é a correta porque o modo 'a' (append) permite adicionar conteúdo ao final de um arquivo existente sem apagar o conteúdo já presente. Isso é especialmente útil para atualizações incrementais de arquivos, como adicionar novas palavras a uma lista no jogo da forca.

Questão 2

Qual função em Python permite escolher um item aleatório de uma lista?

a) random.range(list)

b) random.select(list)

c) random.choice(list)

d) list.pick()

Resposta Correta: c) random.choice(list)

Comentário: A alternativa c é a correta porque random.choice(list) é uma função do módulo random que seleciona um item aleatório de uma lista, perfeita para escolher uma palavra aleatoriamente de uma lista lida de um arquivo.

## Outros documentos

_Fonte: AULA 15_SAIBA MAIS_ PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

SAIBA MAIS AULA 15

Exemplo de Escrita:

with open('palavras.txt', 'w') as arquivo:

arquivo.write("Python\nJava\nC++\n")

Exemplo de Leitura:

with open('palavras.txt', 'r') as arquivo:

palavras = arquivo.readlines()

Exemplo de Escolha de Palavra:

import random

palavra_secreta = random.choice(palavras).strip()
