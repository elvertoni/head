---
titulo: "Testando valores"
tipo: rco-seed
disciplina: programacao-no-desenvolvimento-de-sistemas
sigla_rco: PDS
trimestre: 1
ordem_rco: 3
serie: 3
aula_rco: "Aula 03"
slides: 24
tem_atividade: true
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/1TRI/3-testando-valores/3-testando-valores.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PDS/1TRI/3-testando-valores/AULA 03_ATIVIDADE_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/1TRI/3-testando-valores/AULA 03_SAIBA MAIS_ PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Testando valores

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO NO
- DESENVOLVIMENTO DE
- SISTEMAS
- 3ª SÉRIE
- Testando valores
- Aula 03

_3 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- DESENVOLVIMENTO DE SISTEMAS
- Na aula de hoje vamos:
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store
- Testar valores em Python, focando nas estruturas condicionais e operadores de comparação, criando condições para tomar decisões com base em valores de variáveis.

_7 imagem(ns) no slide._

### Slide 4

- DESENVOLVIMENTO DE SISTEMAS
- ATENÇÃO PROFESSOR!
- O Material aqui apresentado, segue a análise do plano de curso contemplando os componentes curriculares e seus objetos de conhecimento, sendo assim, você tem liberdade para customizar o material conforme seu contexto para maior aproveitamento do conteúdo. Em caso de falta ou indisponibilidade de acesso à internet no local de aula, você poderá utilizar os seguintes artigos para criação de material complementar para auxiliar na aula:
- Leitura/Recursos Adicionais:
- "Python Crash Course" por Eric Matthes
- Documentação oficial do Python sobre estruturas condicionais: Python Docs - Control Flow Tools
- Ferramenta on line para codificação python:
- https://www.online-python.com/

_5 imagem(ns) no slide._

### Slide 5

- DESENVOLVIMENTO DE SISTEMAS
- Na aula anterior…
- Coletamos a entrada de dados do usuário em Python utilizando a função input(). Aprendemos a converter as entradas para tipos de dados apropriados como inteiros ou decimais para processamento adicional.
- Discutimos a importância da validação de entrada para garantir que os dados recebidos sejam adequados para uso no programa, evitando assim erros e falhas.

_5 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Como você estruturaria o teste de valores para determinar a categoria apropriada?
- Quem sabe responde!
- Considere um programa que deve categorizar a idade de uma pessoa em criança, adolescente, adulto ou idoso.

_6 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- O programa deve usar a estrutura if-elif-else para comparar a idade com diferentes faixas etárias e atribuir a categoria correspondente.

_9 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Estrutura if
- A estrutura if é o bloco de construção básico para tomada de decisões em Python. Ela permite verificar uma condição e executar um bloco de código se essa condição for verdadeira.
- Por exemplo, if idade < 18: executa um bloco de código para menores de 18 anos.

_4 imagem(ns) no slide._

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- Estrutura elif
- elif, abreviação de 'else if', é usado para verificar múltiplas condições após um if. Quando um if é falso, elif testa outra condição. Por exemplo, após verificar se idade < 18, pode-se usar elif idade < 60: para um novo teste.

_4 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- Estrutura else
- else é uma declaração final em uma cadeia de if-elif que executa um bloco de código se todas as condições anteriores forem falsas.
- É a "rede de segurança" que captura todos os casos não abordados pelo if e elif.

_4 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Operadores de Comparação
- Operadores como ==, !=, <, >, <= e >= são usados para comparar valores. Eles são cruciais nas estruturas de decisão e retornam valores booleanos (True ou False) com base na comparação.

_4 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- Saiba +
- Exemplos práticos englobam desde a verificação da maioridade de um usuário até a comparação de pontuações em um jogo, ou mesmo a tomada de decisões com base em variáveis de ambiente. Esses cenários reais facilitam a compreensão da aplicação das estruturas.
- Clique aqui!

_4 imagem(ns) no slide._

### Slide 13

- DESENVOLVIMENTO DE SISTEMAS
- Boas Práticas
- Incluem escrever condições claras e diretas, evitar cadeias excessivamente longas de elif e garantir que todas as possíveis condições sejam abordadas para evitar erros de lógica. Também é recomendado usar parênteses para tornar as comparações mais claras.

_4 imagem(ns) no slide._

### Slide 14 (oculto)

- DESENVOLVIMENTO DE SISTEMAS
- Exemplo atividade para Professor
- # Solicita a idade do usuário
- idade = int(input("Digite sua idade: "))
- # Categoriza a idade
- if idade < 13:
- categoria = "Criança"
- elif idade < 18:
- categoria = "Adolescente"
- elif idade < 60:
- categoria = "Adulto"
- else:
- categoria = "Idoso"
- # Exibe a categoria
- print(f"Você está na categoria: {categoria}.")
- Código Python demonstrando o uso de if-elif-else para categorizar idades.

_3 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- Atividade para a fixação do conteúdo estudado
- Qual estrutura você usaria para testar se um número é positivo, negativo ou zero?
- (A) while
- (B) for
- (C) if-elif-else
- (D) try-except
- Registre a sua resposta e compartilhe!

_5 imagem(ns) no slide._

### Slide 16

- DESENVOLVIMENTO DE SISTEMAS
- Atividade para a fixação do conteúdo estudado
- Qual estrutura você usaria para testar se um número é positivo, negativo ou zero?
- (A) while
- (B) for
- (C) if-elif-else
- (D) try-except
- Resposta correta: (C) if-elif-else

_4 imagem(ns) no slide._

> **Notas do apresentador:** Comentário: A estrutura if-elif-else é ideal para testar se um número é positivo, negativo ou zero, utilizando diferentes condições para cada caso.

### Slide 17

- DESENVOLVIMENTO DE SISTEMAS
- Conclusão
- Testar valores é um componente fundamental da programação em Python, permitindo a execução de diferentes ações com base em condições específicas.

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
- A condição elif
- 8 minutos
- Link para tarefa: https://cursos.alura.com.br/course/python-introducao-a-linguagem/task/22811
- elif, uma abreviação de "else if", é um operador condicional em Python usado após um if. Ele verifica uma nova condição se a anterior for falsa. Utilizado para múltiplas verificações sequenciais, elif evita a execução de códigos adicionais se uma das condições anteriores for verdadeira, tornando o código mais eficiente e legível.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 20

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje:
- Aprendemos sobre o teste de valores usando if-elif-else e operadores de comparação em Python.
- Na próxima aula, aprenderemos a criar laços e fazer iterações.

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

_Fonte: AULA 03_ATIVIDADE_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

ATIVIDADE AULA 03

Questão 1

Qual é a estrutura usada para testar múltiplas condições em Python?

a) for

b) while

c) if-elif-else

d) switch

Resposta correta: c) if-elif-else

Comentário: A estrutura if-elif-else é usada para testar múltiplas condições, onde if é a condição inicial, elif representa as condições subsequentes, e else é a condição final.

Questão 2

Como você verifica a igualdade de duas variáveis em Python?

a) =

b) ==

c) ===

d) !=

Resposta correta: b) ==

Comentário: O operador == é usado para verificar a igualdade entre duas variáveis em Python.

## Outros documentos

_Fonte: AULA 03_SAIBA MAIS_ PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

SAIBA MAIS AULA 03

Exemplo 1: Classificação de Notas

nota = 85

if nota >= 90:

print("A")

elif nota >= 80:

print("B")

elif nota >= 70:

print("C")

elif nota >= 60:

print("D")

else:

print("F")

Exemplo 2: Faixas Etárias

nota = 85

if nota >= 90:

print("A")

elif nota >= 80:

print("B")

elif nota >= 70:

print("C")

elif nota >= 60:

print("D")

else:

print("F")

Exemplo 3: Estações do Ano

mes = "Julho"

if mes in ["Dezembro", "Janeiro", "Fevereiro"]:

print("Verão")

elif mes in ["Março", "Abril", "Maio"]:

print("Outono")

elif mes in ["Junho", "Julho", "Agosto"]:

print("Inverno")

else:

print("Primavera")

Exemplo 4: Categorias de Peso

peso = 75

if peso < 50:

print("Leve")

elif peso < 70:

print("Médio")

elif peso < 90:

print("Pesado")

else:

print("Muito Pesado")

Exemplo 5: Classificação de Filmes

idade = 16

classificacao = "R"

if classificacao == "G":

print("Permitido para todas as idades.")

elif classificacao == "PG" and idade >= 10:

print("Permitido para crianças com mais de 10 anos.")

elif classificacao == "PG-13" and idade >= 13:

print("Permitido para adolescentes com mais de 13 anos.")

elif classificacao == "R" and idade >= 17:

print("Permitido para maiores de 17 anos.")

else:

print("Não permitido.")
