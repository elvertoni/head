---
titulo: "Lidando com a entrada do usuário"
tipo: rco-seed
disciplina: programacao-no-desenvolvimento-de-sistemas
sigla_rco: PDS
trimestre: 1
ordem_rco: 2
serie: 3
aula_rco: "Aula 02"
slides: 24
tem_atividade: true
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/1TRI/2-lidando-com-a-entrada-do-usuario/2-lidando-com-a-entrada-do-usuario.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/1TRI/2-lidando-com-a-entrada-do-usuario/AULA 02_ATIVIDADE_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/1TRI/2-lidando-com-a-entrada-do-usuario/AULA 02_SAIBA MAIS_ PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Lidando com a entrada do usuário

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO NO
- DESENVOLVIMENTO DE
- SISTEMAS
- 3ª SÉRIE
- Lidando com a entrada do usuário
- Aula 02

_3 imagem(ns) no slide._

### Slide 2

- DESENVOLVIMENTO DE SISTEMAS
- Na aula de hoje vamos:
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store
- Manipular entradas do usuário em Python, abordando a função input() e conversão de tipos.

_7 imagem(ns) no slide._

### Slide 3

- DESENVOLVIMENTO DE SISTEMAS
- ATENÇÃO PROFESSOR!
- O Material aqui apresentado, segue a análise do plano de curso contemplando os componentes curriculares e seus objetos de conhecimento, sendo assim, você tem liberdade para customizar o material conforme seu contexto para maior aproveitamento do conteúdo. Em caso de falta ou indisponibilidade de acesso à internet no local de aula, você poderá utilizar os seguintes artigos para criação de material complementar para auxiliar na aula:
- Leitura/Recursos Adicionais:
- Documentação oficial do Python: Python.org
- Tutorial de instalação do Python: Real Python - Installing Python
- Ferramenta on line para codificação python:
- https://www.online-python.com/

_5 imagem(ns) no slide._

### Slide 4

- DESENVOLVIMENTO DE SISTEMAS
- Na aula anterior…
- Na aula anterior, focamos na instalação do Python 3, abordando como baixar e instalar a linguagem em diferentes sistemas operacionais. Discutimos a importância de adicionar o Python ao PATH do sistema para facilitar sua execução e verificamos a instalação correta através do comando python --version no terminal ou prompt de comando. Também introduzimos o interpretador interativo Python (IDLE) e os conceitos básicos sobre a gestão de pacotes usando pip.

_4 imagem(ns) no slide._

### Slide 5

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Imagine que Alice, uma programadora iniciante, precisa criar um programa que solicite o nome e a idade do usuário e os exiba na tela.
- Quem sabe responde!
- Como ela deve utilizar a função input() para capturar essas informações?

_6 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Alice deve usar a função input() para capturar o nome e a idade.
- Para a idade, ela deve converter a entrada para um número inteiro usando int(input()).

_4 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Utilização da Função input()
- A função input() é essencial em Python para interação com o usuário. Ela pausa o programa e espera pela entrada do usuário, retornando-a como uma string. É frequentemente utilizada para coletar dados em aplicações interativas.

_4 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Tipos de Dados em Entradas
- Ao usar input(), todas as entradas são consideradas strings.
- É importante converter essas entradas para o tipo de dado apropriado, como int ou float, para operações matemáticas ou lógicas, utilizando funções de conversão de tipo.

_4 imagem(ns) no slide._

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- Tratamento de Entradas
- O tratamento de entradas é fundamental para evitar erros. Isso inclui verificar a validade dos dados inseridos, tratando exceções através de estruturas como try-except e garantindo que a entrada atenda aos critérios do programa.

_4 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- Exemplos Práticos
- Exemplos práticos incluem solicitar ao usuário informações como nome, idade ou preferências e usar esses dados em cálculos ou decisões lógicas. São demonstrações simples que ilustram a captura e utilização de dados do usuário.

_4 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Aplicações da Entrada de Usuário
- A entrada do usuário é usada em uma variedade de aplicações, como formulários, pesquisas, jogos interativos e interfaces de usuário.
- Compreender como coletar e usar essas entradas é necessário para desenvolver programas interativos eficientes!
- https://franciscochaves.com.br/assets/img/blog/2017/07/logo-python-entrada-dados.png

_4 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- Boas Práticas
- Incluem a clara instrução ao usuário sobre o tipo de entrada esperado, validação de dados para garantir integridade e segurança, e tratamento de erros para evitar falhas no programa devido a entradas inesperadas ou inválidas.
- https://posit.co/wp-content/uploads/2023/02/python-academy-blog-hero.jpeg

_4 imagem(ns) no slide._

### Slide 13 (oculto)

- DESENVOLVIMENTO DE SISTEMAS
- Exemplo atividade para Professor
- Professor, crie um código Python simples solicitando o nome e a idade do usuário e exibindo estas informações.
- # Solicita o nome do usuário
- nome = input("Digite seu nome: ")
- # Solicita a idade do usuário
- idade = input("Digite sua idade: ")
- # Exibe as informações coletadas
- print("Olá {nome}, você tem {idade} anos.")
- https://cdn.iconscout.com/icon/free/png-256/free-python-3629591-3032289.png?f=webp

_4 imagem(ns) no slide._

### Slide 14

- DESENVOLVIMENTO DE SISTEMAS
- Atividade para a fixação do conteúdo estudado
- Para garantir que a entrada do usuário seja um número inteiro, qual abordagem é correta?
- (A) input(int)
- (B) int(input())
- (C) input().toInt()
- (D) int.parse(input())
- Responda em seu caderno!

_4 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- Atividade para a fixação do conteúdo estudado
- Para garantir que a entrada do usuário seja um número inteiro, qual abordagem é correta?
- (A) input(int)
- (B) int(input())
- (C) input().toInt()
- (D) int.parse(input())
- Resposta correta: (B) int(input())

_4 imagem(ns) no slide._

> **Notas do apresentador:** Comentário: A abordagem correta para garantir que a entrada seja um número inteiro é usar int(input()).

### Slide 16

- DESENVOLVIMENTO DE SISTEMAS
- Conclusão
- Entender como lidar com entradas do usuário é fundamental para a interação em muitos programas Python. Esta aula fornece uma base sólida para essa habilidade essencial.

_4 imagem(ns) no slide._

### Slide 17

- DESENVOLVIMENTO DE SISTEMAS
- Atividade Prática na Plataforma Alura
- Na plataforma Alura vamos acessar o seguinte curso:
- A recomendação é que você continue esse curso extraclasse, pois ele traz um conteúdo essencial para compreender sobre o referido tema.
- Link para o curso: https://cursos.alura.com.br/course/python-introducao-a-linguagem

_5 imagem(ns) no slide._

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- Instalando e conhecendo o PyCharm
- 10 minutos
- Link para tarefa: https://cursos.alura.com.br/course/python-introducao-a-linguagem/task/22764
- Há várias opções de editores de texto no mercado, entre elas o Atom e o Sublime Text. Apesar de esses editores nos ajudarem a escrever o código, eles não são focados no Python, e sim em dar suporte a várias linguagens. Então, vamos utilizar uma ferramenta (IDE, do inglês Integrated Development Environment) só focada para o Python, assim como existe o Eclipse para o Java.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- Comparando variáveis
- 17 minutos
- Link para tarefa: https://cursos.alura.com.br/course/python-introducao-a-linguagem/task/22779
- Em Python, para comparar variáveis, utilizam-se operadores como == (igualdade), != (diferença), > (maior que), < (menor que), >= (maior ou igual) e <= (menor ou igual). As comparações resultam em valores booleanos True ou False. Por exemplo: a == b verifica se a é igual a b.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 20

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje
- Na próxima aula, testaremos e validaremos essas entradas para garantir a robustez dos programas!
- Aprendemos a capturar e tratar entradas do usuário em Python.

_4 imagem(ns) no slide._

### Slide 21

- DESENVOLVIMENTO DE SISTEMAS
- Referências
- Bibliografia
- PUREWAL, Semmy. Aprendendo a Desenvolver Aplicações Web. Desenvolva rapidamente com as tecnologias JavaScript mais modernas. São Paulo: Novatec, 2014.
- SILVA, L. F.; OLIVEIRA, A. D. de. Desenvolvimento de Software II C#: programação em camadas. [S. l.]: CBL Edição do Autor, 2017. E-book.
- MARTIN, R. C. Arquitetura limpa: o guia do artesão para estrutura e design de software. Rio de Janeiro: Alta Books, 2019. E-book.
- GALOTTI, G. M. A. Qualidade de software. São Paulo: Pearson Education do Brasil, 2016. E-book.
- VAZQUEZ, C. E.; SIMÕES, G. S. Engenharia de requisitos: software orientado ao negócio. São Paulo: Brasport, 2016. E-book.
- Softwares
- Java Netbeans; WebStorm; Sublime Text; Intellij IDEA; Astah Software; Netbeans; Python; Ccharp; Colab; PyCharm; Jupyter Notebook.

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

_Fonte: AULA 02_ATIVIDADE_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

ATIVIDADE AULA 02

Questão 1

Qual função é utilizada em Python para receber entrada do usuário?

a) input()

b) get()

c) read()

d) receive()

Resposta correta: a) input()

Comentário: A função input() é usada em Python para capturar a entrada do usuário como uma string.

Questão 2

Como converter a entrada do usuário em um tipo inteiro em Python?

a) int(input())

b) input(int)

c) input().toInt()

d) parse(input())

Resposta correta: a) int(input())

Comentário: Para converter a entrada do usuário em um número inteiro, utilizamos a função int() em conjunto com input().

## Outros documentos

_Fonte: AULA 02_SAIBA MAIS_ PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

SAIBA MAIS AULA 02

# Solicita nome e idade do usuário

nome = input("Digite seu nome: ")

idade = input("Digite sua idade: ")

# Converte a idade para um inteiro

idade = int(idade)

print(f"Olá {nome}, você tem {idade} anos.")

try:

numero = int(input("Digite um número: "))

print(f"O número digitado foi {numero}.")

except ValueError:

print("Erro: Por favor, digite um número válido.")

while True:

entrada = input("Digite 'sim' ou 'não': ")

if entrada.lower() in ('sim', 'não'):

break

print("Entrada inválida. Tente novamente.")

print(f"Você digitou '{entrada}'.")

# Solicita dois números e realiza uma soma

try:

num1 = float(input("Digite o primeiro número: "))

num2 = float(input("Digite o segundo número: "))

soma = num1 + num2

print(f"A soma de {num1} e {num2} é {soma}.")

except ValueError:

print("Erro: Por favor, digite valores numéricos.")

nome = input("Digite seu nome: ")

cidade = input("Digite sua cidade: ")

print(f"Olá, {nome}! Como está o tempo em {cidade} hoje?")
