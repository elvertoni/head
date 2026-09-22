---
titulo: "Ordenação customizada"
tipo: rco-seed
disciplina: programacao-no-desenvolvimento-de-sistemas
sigla_rco: PDS
trimestre: 2
ordem_rco: 41
serie: 3
aula_rco: "Aula 41"
slides: 29
tem_atividade: true
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PDS/2TRI/41-ordenacao-customizada/41-ordenacao-customizada.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PDS/2TRI/41-ordenacao-customizada/AULA 41_ATIVIDADE_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PDS/2TRI/41-ordenacao-customizada/AULA 41_SAIBA MAIS_ PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Ordenação customizada

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO NO
- DESENVOLVIMENTO DE
- SISTEMAS
- 3ª SÉRIE
- Ordenação customizada
- Aula 41

_3 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- DESENVOLVIMENTO DE SISTEMAS
- Nesta aula, vamos:
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store
- Aprender como ordenar objetos que não possuem uma ordem natural em Java.

_7 imagem(ns) no slide._

### Slide 4

- DESENVOLVIMENTO DE SISTEMAS
- ATENÇÃO PROFESSOR!
- O Material aqui apresentado, segue a análise do plano de curso contemplando os componentes curriculares e seus objetos de conhecimento, sendo assim, você tem liberdade para customizar o material conforme seu contexto para maior aproveitamento do conteúdo. Em caso de falta ou indisponibilidade de acesso à internet no local de aula, você poderá utilizar os seguintes artigos para criação de material complementar para auxiliar na aula:
- Leitura/Recursos Adicionais:
- Online Python: Um IDE online gratuito que permite escrever, executar e compartilhar código Python diretamente no navegador, ideal para testes rápidos e colaborações.
- Google Colab: Um ambiente de Jupyter Notebook que roda no navegador, gratuito e ótimo para projetos que envolvem bibliotecas como Numpy.

_5 imagem(ns) no slide._

### Slide 5

- DESENVOLVIMENTO DE SISTEMAS
- Na aula anterior…
- Discutimos a ordem natural dos objetos, como strings e números, que implementam a interface Comparable. Vimos como usar o método compareTo para ordenar esses objetos de forma natural, com base em suas propriedades intrínsecas.

_4 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Lucas está desenvolvendo um sistema de gerenciamento de biblioteca. Ele precisa ordenar uma lista de livros não apenas por título, mas também por ano de publicação e autor. No entanto, a classe Livro que ele criou não implementa a interface Comparable.

_4 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Como Lucas pode implementar a interface Comparable na classe Livro para definir uma ordem natural e criar um Comparator para uma ordenação customizada?
- Quem sabe responde!

_5 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Lucas pode implementar a interface Comparable na classe Livro e sobrescrever o método compareTo para definir a ordem natural dos livros, como por título. Ele também pode criar classes que implementam a interface Comparator para ordenar os livros por ano de publicação e autor.

_4 imagem(ns) no slide._

> **Notas do apresentador:** Com essa abordagem, Lucas pode facilmente ordenar os livros de várias maneiras, dependendo das necessidades do usuário. Isso melhora a flexibilidade e a funcionalidade do sistema de gerenciamento de biblioteca.

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- Ordenação Customizada de Objetos
- Em python, nem todos os objetos têm uma ordem natural definida. Para ordenar esses objetos, podemos implementar a interface Comparable ou usar a interface Comparator.

_4 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- Definição e Aplicação
- A interface Comparable permite definir uma ordem natural para objetos ao implementar o método compareTo. A interface Comparator permite criar múltiplos critérios de ordenação ao implementar o método compare.

_4 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Importância
- Ordenação é essencial em muitas aplicações para organizar dados de forma lógica e acessível. Ordenação customizada permite maior controle e flexibilidade na forma como os dados são apresentados.

_4 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- Uso Prático
- Ordenação customizada é usada em sistemas como catálogos de produtos, bibliotecas digitais, e bancos de dados, onde diferentes critérios de ordenação são necessários para atender a várias necessidades do usuário.

_4 imagem(ns) no slide._

### Slide 13

- DESENVOLVIMENTO DE SISTEMAS
- Exemplo
- Utilize a plataforma https://www.online-python.com/

_5 imagem(ns) no slide._

### Slide 14

- DESENVOLVIMENTO DE SISTEMAS
- Exemplo
- Utilize a plataforma https://www.online-python.com/

_5 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- Mais Exemplos
- Acesse o arquivo Saiba Mais:

_4 imagem(ns) no slide._

### Slide 16

- DESENVOLVIMENTO DE SISTEMAS
- Atividade para a fixação do conteúdo estudado
- Qual método é usado para definir a ordem natural dos objetos de uma classe que implementa a interface Comparable?
- A) compare
- B) compareTo
- C) compareWith
- D) sortWith
- Escolhendo alguém para responder essa questão!

_4 imagem(ns) no slide._

### Slide 17

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Qual método é usado para definir a ordem natural dos objetos de uma classe que implementa a interface Comparable?
- A) compare
- B) compareTo
- C) compareWith
- D) sortWith
- Resposta Correta: B) compareTo

_3 imagem(ns) no slide._

> **Notas do apresentador:** Comentário: O método compareTo é implementado para definir a ordem natural dos objetos de uma classe.

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- Vamos Praticar?
- Utilize a plataforma https://www.online-python.com/

_6 imagem(ns) no slide._

> **Notas do apresentador:** Comentário sobre a resposta correta: A imutabilidade das tuplas garante que os dados não sejam alterados acidentalmente, proporcionando segurança.

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- Vamos Praticar?
- Utilize a plataforma https://www.online-python.com/

_6 imagem(ns) no slide._

> **Notas do apresentador:** Comentário sobre a resposta correta: A imutabilidade das tuplas garante que os dados não sejam alterados acidentalmente, proporcionando segurança.

### Slide 20

- DESENVOLVIMENTO DE SISTEMAS
- Agora, é com
- 1- Modifique o código para ordenar a lista produtos pelo preço em ordem decrescente e imprima o resultado.
- 2- Modifique o código para ordenar a lista produtos pelo comprimento do nome dos produtos e imprima o resultado.

_6 imagem(ns) no slide._

> **Notas do apresentador:** Comentário: O método __eq__ permite personalizar a comparação de igualdade entre objetos, verificando atributos relevantes.

### Slide 21

- DESENVOLVIMENTO DE SISTEMAS
- Esperado
- 1- Modifique o código para ordenar a lista produtos pelo preço em ordem decrescente e imprima o resultado.

_5 imagem(ns) no slide._

> **Notas do apresentador:** Comentário: O método __eq__ permite personalizar a comparação de igualdade entre objetos, verificando atributos relevantes.

### Slide 22

- DESENVOLVIMENTO DE SISTEMAS
- Esperado
- 2- Modifique o código para ordenar a lista produtos pelo comprimento do nome dos produtos e imprima o resultado.

_5 imagem(ns) no slide._

> **Notas do apresentador:** Comentário: O método __eq__ permite personalizar a comparação de igualdade entre objetos, verificando atributos relevantes.

### Slide 23

- DESENVOLVIMENTO DE SISTEMAS
- Atividade Prática na Plataforma Alura
- Na plataforma Alura vamos acessar o seguinte curso:
- A recomendação é que você continue esse curso extraclasse, pois ele traz um conteúdo essencial para compreender sobre o referido tema.
- Link para o curso: https://cursos.alura.com.br/course/python-collections-listas-e-tuplas

_6 imagem(ns) no slide._

### Slide 24

- DESENVOLVIMENTO DE SISTEMAS
- Itens da aula 7 – Ordem Customizada
- 17 minutos
- Link para tarefa: https://cursos.alura.com.br/course/python-collections-listas-e-tuplas/task/54534
- A ordenação customizada em Python utiliza a função `sorted()` com o parâmetro `key` para definir critérios específicos de ordenação. Lambdas são frequentemente usadas para acessar valores dentro de coleções complexas.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 25

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje
- Nesta aula, exploramos a ordenação customizada de objetos em python. Demonstramos esses conceitos com exemplos práticos, permitindo uma compreensão profunda e aplicável no desenvolvimento de sistemas.

_4 imagem(ns) no slide._

### Slide 26

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

### Slide 27

- DESENVOLVIMENTO DE SISTEMAS
- Referências (Imagens)
- Figuras e Imagens:
- https://www.flaticon.com/br
- https://www.istockphoto.com/br
- https://raw.githubusercontent.com/zbtang/React-Native-ViewPager/HEAD/imgs/dotIndicator.gif
- https://storyset.com

_3 imagem(ns) no slide._

### Slide 28

- DESENVOLVIMENTO DE SISTEMAS
- O RCO+Aulas é um projeto da Secretaria de Estado da Educação do Paraná e está em constante revisão. Todos os slides são de uso exclusivo dos professores da Rede Pública de Ensino, com a finalidade específica de aplicação em sala de aula, sendo totalmente vedada a publicização, reutilização, reprodução total ou parcial para quaisquer outros fins.

_4 imagem(ns) no slide._

### Slide 29

- DESENVOLVIMENTO DE SISTEMAS
- Esta publicação tem a cooperação entre a UNESCO e a Secretaria de Estado da Educação e do Esporte do Paraná no âmbito da parceria PRODOC 914BRZ1091, cujo objetivo é trazer soluções inovadoras de gestão da rede pública estadual de educação do Paraná para a melhoria da aprendizagem dos alunos. As indicações de nomes e a apresentação do material ao longo desta publicação não implicam a manifestação de qualquer opinião por parte da UNESCO a respeito da condição jurídica de qualquer país, território, cidade, região ou de suas autoridades, tampouco da delimitação de suas fronteiras ou limites As ideias e opiniões expressas nesta publicação são as dos autores e não refletem obrigatoriamente as da UNESCO nem comprometem a Organização.
- Cooperação Técnica

_5 imagem(ns) no slide._

## Atividade

_Fonte: AULA 41_ATIVIDADE_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

ATIVIDADE AULA 41

Questão 1

Para que serve a interface Comparator em Java?

A) Para definir a estrutura de uma classe.

B) Para criar múltiplos critérios de ordenação.

C) Para comparar dois números.

D) Para converter objetos em strings.

Resposta Correta: B) Para criar múltiplos critérios de ordenação.

Comentário: A interface Comparator permite a criação de diferentes critérios de ordenação para objetos.

Questão 2

Como você poderia modificar o código para ordenar os livros primeiro por ano de publicação e, em caso de empate, por título?

A) Usar dois Comparator diferentes sequencialmente.

B) Usar um Comparator composto que combine os dois critérios.

C) Implementar a interface Comparable duas vezes.

D) Usar uma lista de comparadores.

Resposta Correta: B) Usar um Comparator composto que combine os dois critérios.

Comentário: O Comparator composto permite combinar múltiplos critérios de ordenação para resolver empates.

## Outros documentos

_Fonte: AULA 41_SAIBA MAIS_ PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

SAIBA MAIS AULA 41

Resumo Explicativo:

A ordenação customizada em Python permite que desenvolvedores definam critérios específicos para ordenar coleções de dados. Utilizando a função sorted() e o método sort() com o parâmetro key, é possível ordenar listas de acordo com regras personalizadas, como ordenar dicionários por valores específicos ou ordenar listas de strings pelo comprimento. Esse recurso é essencial para criar sistemas flexíveis e eficientes que podem manipular dados complexos de maneira lógica e estruturada.

Estudo de Caso:

Imagine que você é um desenvolvedor criando um sistema de gerenciamento de inventário para uma loja online. O sistema precisa organizar produtos não apenas pelo preço, mas também pelo nome e pela quantidade em estoque. Além disso, é necessário criar relatórios que mostrem os produtos mais caros e os produtos com nomes mais curtos.

Exemplo de código:

# Lista de dicionários representando produtos

produtos = [

{"nome": "Teclado", "preco": 45.50, "quantidade": 12},

{"nome": "Mouse", "preco": 20.75, "quantidade": 50},

{"nome": "Monitor", "preco": 150.00, "quantidade": 8},

{"nome": "CPU", "preco": 500.00, "quantidade": 5},

{"nome": "Cabo HDMI", "preco": 15.00, "quantidade": 30}

]

# Ordenar os produtos pelo preço de forma crescente

produtos_ordenados_preco = sorted(produtos, key=lambda x: x['preco'])

print("Produtos ordenados pelo preço (crescente):")

for produto in produtos_ordenados_preco:

print(f"{produto['nome']}: ${produto['preco']}")

# Ordenar os produtos pelo nome em ordem alfabética

produtos_ordenados_nome = sorted(produtos, key=lambda x: x['nome'])

print("\nProdutos ordenados pelo nome (alfabética):")

for produto in produtos_ordenados_nome:

print(f"{produto['nome']}: ${produto['preco']}")

# Ordenar os produtos pela quantidade em estoque de forma decrescente

produtos_ordenados_quantidade = sorted(produtos, key=lambda x: x['quantidade'], reverse=True)

print("\nProdutos ordenados pela quantidade (decrescente):")

for produto in produtos_ordenados_quantidade:

print(f"{produto['nome']}: {produto['quantidade']} unidades")

Questões:

1- Liste dois métodos usados para ordenar listas em Python de forma personalizada.

Resposta esperada: Os métodos são sort() e sorted().

2- Explique como o parâmetro key é usado na função sorted() para realizar uma ordenação customizada.

Resposta esperada: O parâmetro key em sorted() permite especificar uma função que extrai um valor de cada item da lista, usado para determinar a ordem. Isso permite ordenar com base em qualquer aspecto dos itens da lista.

3- Dado a lista de produtos acima, modifique o código para ordenar os produtos pelo comprimento do nome e imprima o resultado.

*Resposta esperada:*

# Ordenar os produtos pelo comprimento do nome

produtos_ordenados_comprimento_nome = sorted(produtos, key=lambda x: len(x['nome']))

print("\nProdutos ordenados pelo comprimento do nome:")

for produto in produtos_ordenados_comprimento_nome:

print(f"{produto['nome']}: ${produto['preco']}")

4- Identifique as partes do código de exemplo que usam sorted() e explique como cada uma contribui para a ordenação dos dados.

Resposta esperada: sorted(produtos, key=lambda x: x['preco']) ordena produtos por preço crescente; sorted(produtos, key=lambda x: x['nome']) ordena por nome; sorted(produtos, key=lambda x: x['quantidade'], reverse=True) ordena por quantidade em estoque de forma decrescente.

5- Avalie a eficácia de usar funções lambda para a ordenação customizada de dados em Python. Justifique sua resposta com base nos exemplos fornecidos.

Resposta esperada: As funções lambda são eficazes para ordenação customizada porque permitem definir de forma concisa e clara os critérios de ordenação, tornando o código mais flexível e fácil de entender.

6- Desenvolva um código que ordene uma lista de estudantes por nota média e, em seguida, por nome em ordem alfabética. Utilize sorted() com lambdas para implementar a solução.

*Resposta esperada:*

# Lista de dicionários representando estudantes

estudantes = [

{"nome": "Carlos", "nota_media": 85.5},

{"nome": "Ana", "nota_media": 92.0},

{"nome": "Pedro", "nota_media": 78.0},

{"nome": "Beatriz", "nota_media": 88.5},

{"nome": "Mariana", "nota_media": 95.0}

]

# Ordenar os estudantes pela nota média de forma decrescente

estudantes_ordenados_nota = sorted(estudantes, key=lambda x: x['nota_media'], reverse=True)

print("Estudantes ordenados pela nota média (decrescente):")

for estudante in estudantes_ordenados_nota:

print(f"{estudante['nome']}: {estudante['nota_media']}")

# Ordenar os estudantes pelo nome em ordem alfabética

estudantes_ordenados_nome = sorted(estudantes, key=lambda x: x['nome'])

print("\nEstudantes ordenados pelo nome (alfabética):")

for estudante in estudantes_ordenados_nome:

print(f"{estudante['nome']}: {estudante['nota_media']}")
