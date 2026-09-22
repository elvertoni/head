---
titulo: "Igualdade em python"
tipo: rco-seed
disciplina: programacao-no-desenvolvimento-de-sistemas
sigla_rco: PDS
trimestre: 2
ordem_rco: 38
serie: 3
aula_rco: "Aula 38"
slides: 32
tem_atividade: true
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PDS/2TRI/38-igualdade-em-python/38-igualdade-em-python.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PDS/2TRI/38-igualdade-em-python/AULA 38_ATIVIDADE_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PDS/2TRI/38-igualdade-em-python/AULA 38_SAIBA MAIS_ PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Igualdade em python

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO NO
- DESENVOLVIMENTO DE
- SISTEMAS
- 3ª SÉRIE
- Igualdade em python
- Aula 38

_3 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- DESENVOLVIMENTO DE SISTEMAS
- Nesta aula, vamos:
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store
- Entender o conceito de igualdade em Python, focando no método __eq__ e sua importância para comparar objetos.

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
- Na última aula, exploramos polimorfismo e arrays em Python, utilizando listas e Numpy para manipulação de dados.

_4 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Ana está desenvolvendo um sistema para gerenciar uma biblioteca de livros. Ela precisa garantir que dois livros sejam considerados iguais se tiverem o mesmo título e autor, independentemente de outros atributos.

_4 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Duas Soluções Possíveis:
- Comparar objetos da classe Livro diretamente usando ==, sem implementar o método __eq__.
- Implementar o método __eq__ na classe Livro para comparar os atributos titulo e autor.
- Quem sabe responde!

_5 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Solução Correta: Implementar __eq__ permite personalizar a lógica de comparação, garantindo que livros com o mesmo título e autor sejam considerados iguais.
- Solução Falsa: Comparar objetos diretamente sem __eq__ apenas verifica se eles são a mesma instância na memória, o que não garante que livros com o mesmo título e autor sejam considerados iguais.

_4 imagem(ns) no slide._

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- Igualdade em Python
- Igualdade em Python refere-se à capacidade de comparar dois objetos para determinar se são equivalentes em valor. Isso é fundamental para muitas operações, como verificar duplicatas, procurar itens em coleções e garantir a consistência dos dados.

_4 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- Igualdade e o eq
- O método __eq__ é um método especial em Python que permite definir a lógica de comparação de igualdade entre objetos. Quando implementado, __eq__ é chamado ao usar o operador ==. Isso permite comparar objetos com base em seus atributos relevantes.

_4 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Importância da Igualdade
- A definição precisa de igualdade é importante para operações que dependem de comparações, como armazenamento em conjuntos ou dicionários. Implementar __eq__ corretamente garante que objetos sejam comparados de maneira consistente e precisa, evitando erros lógicos no código.

_4 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- Aplicações da Igualdade
- No desenvolvimento de sistemas, igualdade é usada para verificar se itens são duplicados, validar entradas do usuário e gerenciar coleções de objetos. Implementar __eq__ permite personalizar essas verificações para atender às necessidades específicas do sistema.

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

_6 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- Exemplo
- Utilize a plataforma https://www.online-python.com/

_6 imagem(ns) no slide._

### Slide 16

- DESENVOLVIMENTO DE SISTEMAS
- Resultado da compilação
- Utilize a plataforma https://www.online-python.com/

_5 imagem(ns) no slide._

### Slide 17

- DESENVOLVIMENTO DE SISTEMAS
- Mais Exemplos
- Acesse o arquivo Saiba Mais:

_4 imagem(ns) no slide._

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- Atividade para a fixação do conteúdo estudado
- Qual é o propósito do método __eq__ em Python?
- A) Para definir como os objetos são inicializados
- B) Para definir a lógica de comparação de igualdade entre objetos
- C) Para imprimir a representação string de um objeto
- D) Para calcular o hash de um objeto
- Escolhendo alguém para responder essa questão!

_4 imagem(ns) no slide._

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Qual é o propósito do método __eq__ em Python?
- A) Para definir como os objetos são inicializados
- B) Para definir a lógica de comparação de igualdade entre objetos
- C) Para imprimir a representação string de um objeto
- D) Para calcular o hash de um objeto
- Resposta correta: B) Para definir a lógica de comparação de igualdade entre objetos

_3 imagem(ns) no slide._

> **Notas do apresentador:** Comentário: O método __eq__ permite personalizar a comparação de igualdade entre objetos, verificando atributos relevantes.

### Slide 20 (oculto)

- DESENVOLVIMENTO DE SISTEMAS
- Vamos Praticar?
- Utilize a plataforma https://www.online-python.com/

_7 imagem(ns) no slide._

> **Notas do apresentador:** Comentário sobre a resposta correta: A imutabilidade das tuplas garante que os dados não sejam alterados acidentalmente, proporcionando segurança.

### Slide 21 (oculto)

- DESENVOLVIMENTO DE SISTEMAS
- Vamos Praticar?
- Utilize a plataforma https://www.online-python.com/

_6 imagem(ns) no slide._

> **Notas do apresentador:** Comentário sobre a resposta correta: A imutabilidade das tuplas garante que os dados não sejam alterados acidentalmente, proporcionando segurança.

### Slide 22 (oculto)

- DESENVOLVIMENTO DE SISTEMAS
- Agora, é com
- 1- Adicionar uma nova pessoa e comparar:
- Adicione uma nova pessoa chamada pessoa4 com o nome "Charlie", idade 28, e email "charlie@example.com".
- Compare pessoa4 com pessoa1 e exiba o resultado.
- 2- Modificar o método eq para incluir o nome e a idade:
- Modifique o método __eq__ para considerar os atributos nome e idade na comparação, além do email.
- Recompare pessoa1 com pessoa3 e pessoa4 e exiba os resultados.

_6 imagem(ns) no slide._

> **Notas do apresentador:** Comentário: O método __eq__ permite personalizar a comparação de igualdade entre objetos, verificando atributos relevantes.

### Slide 23 (oculto)

- DESENVOLVIMENTO DE SISTEMAS
- Esperado
- 1- Adicionar uma nova pessoa e comparar:

_5 imagem(ns) no slide._

> **Notas do apresentador:** Comentário: O método __eq__ permite personalizar a comparação de igualdade entre objetos, verificando atributos relevantes.

### Slide 24 (oculto)

- DESENVOLVIMENTO DE SISTEMAS
- Esperado
- 2- Modificar o método eq para incluir o nome e a idade:

_5 imagem(ns) no slide._

> **Notas do apresentador:** Comentário: O método __eq__ permite personalizar a comparação de igualdade entre objetos, verificando atributos relevantes.

### Slide 25 (oculto)

- DESENVOLVIMENTO DE SISTEMAS
- Esperado
- 2- Modificar o método eq para incluir o nome e a idade:

_5 imagem(ns) no slide._

> **Notas do apresentador:** Comentário: O método __eq__ permite personalizar a comparação de igualdade entre objetos, verificando atributos relevantes.

### Slide 26

- DESENVOLVIMENTO DE SISTEMAS
- Atividade Prática na Plataforma Alura
- Na plataforma Alura vamos acessar o seguinte curso:
- A recomendação é que você continue esse curso extraclasse, pois ele traz um conteúdo essencial para compreender sobre o referido tema.
- Link para o curso: https://cursos.alura.com.br/course/python-collections-listas-e-tuplas

_6 imagem(ns) no slide._

### Slide 27

- DESENVOLVIMENTO DE SISTEMAS
- Itens da aula 4 - Igualdade
- 11 minutos
- Link para tarefa: https://cursos.alura.com.br/course/python-collections-listas-e-tuplas/task/54531
- Igualdade em Python permite comparar se dois objetos têm o mesmo valor. Usando o operador `==`, é possível verificar se os atributos relevantes dos objetos são iguais. A customização dessa comparação é feita através do método especial `__eq__`, garantindo precisão e consistência nas operações que dependem de comparações de objetos.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 28

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje
- Exploramos a importância da igualdade em Python e como o método __eq__ permite personalizar a comparação de objetos. Essa definição precisa de igualdade é essencial para operações em coleções e como implementar __eq__ para garantir comparações consistentes e precisas.

_4 imagem(ns) no slide._

### Slide 29

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

### Slide 30

- DESENVOLVIMENTO DE SISTEMAS
- Referências (Imagens)
- Figuras e Imagens:
- https://www.flaticon.com/br
- https://www.istockphoto.com/br
- https://raw.githubusercontent.com/zbtang/React-Native-ViewPager/HEAD/imgs/dotIndicator.gif
- https://storyset.com

_3 imagem(ns) no slide._

### Slide 31

- DESENVOLVIMENTO DE SISTEMAS
- O RCO+Aulas é um projeto da Secretaria de Estado da Educação do Paraná e está em constante revisão. Todos os slides são de uso exclusivo dos professores da Rede Pública de Ensino, com a finalidade específica de aplicação em sala de aula, sendo totalmente vedada a publicização, reutilização, reprodução total ou parcial para quaisquer outros fins.

_4 imagem(ns) no slide._

### Slide 32

- DESENVOLVIMENTO DE SISTEMAS
- Esta publicação tem a cooperação entre a UNESCO e a Secretaria de Estado da Educação e do Esporte do Paraná no âmbito da parceria PRODOC 914BRZ1091, cujo objetivo é trazer soluções inovadoras de gestão da rede pública estadual de educação do Paraná para a melhoria da aprendizagem dos alunos. As indicações de nomes e a apresentação do material ao longo desta publicação não implicam a manifestação de qualquer opinião por parte da UNESCO a respeito da condição jurídica de qualquer país, território, cidade, região ou de suas autoridades, tampouco da delimitação de suas fronteiras ou limites As ideias e opiniões expressas nesta publicação são as dos autores e não refletem obrigatoriamente as da UNESCO nem comprometem a Organização.
- Cooperação Técnica

_5 imagem(ns) no slide._

## Atividade

_Fonte: AULA 38_ATIVIDADE_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

ATIVIDADE AULA 38

Questão 1

O que acontece se o método __eq__ não for implementado em uma classe e dois objetos dessa classe forem comparados usando ==?

A) Uma exceção será levantada

B) Python usará a comparação de identidade padrão

C) Python usará a comparação de tipos

D) Os objetos serão considerados sempre iguais

Resposta correta: B) Python usará a comparação de identidade padrão

Comentário: Sem __eq__, Python compara se os objetos são a mesma instância na memória.

Questão 2

Qual método especial é comumente implementado junto com __eq__ para garantir a consistência em coleções como conjuntos e dicionários?

A) __init__

B) __str__

C) __hash__

D) __repr__

Resposta correta: C) __hash__

Comentário: __hash__ deve ser implementado junto com __eq__ para garantir que objetos iguais tenham o mesmo hash, permitindo a correta operação em conjuntos e dicionários.

## Outros documentos

_Fonte: AULA 38_SAIBA MAIS_ PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

SAIBA MAIS AULA 38

Resumo Explicativo:

Igualdade em Python é um conceito fundamental que permite comparar dois objetos para determinar se eles têm o mesmo valor. Isso é realizado através do operador ==, que internamente chama o método especial __eq__. Implementar __eq__ permite personalizar a lógica de comparação, garantindo que objetos sejam considerados iguais com base em critérios específicos, como atributos relevantes. Esse conceito é crucial em muitas operações, como verificar duplicatas, pesquisar itens em coleções e validar dados.

Estudo de Caso:

Imagine uma biblioteca que está desenvolvendo um sistema para gerenciar seus livros. O sistema precisa garantir que dois livros sejam considerados iguais se tiverem o mesmo título e autor, independentemente de outros atributos, como o ano de publicação ou a edição. Para isso, o desenvolvedor deve implementar o método __eq__ na classe Livro. Isso permitirá que o sistema trate livros duplicados de forma correta, simplificando operações como adicionar livros a coleções e verificar se um livro já está no acervo.

Exemplo de código:

class Livro:

def __init__(self, titulo, autor, ano):

self.titulo = titulo

self.autor = autor

self.ano = ano

def __eq__(self, outro):

if isinstance(outro, Livro):

return self.titulo == outro.titulo and self.autor == outro.autor

return False

def __hash__(self):

return hash((self.titulo, self.autor))

def __repr__(self):

return f"Livro(titulo='{self.titulo}', autor='{self.autor}', ano={self.ano})"

# Criando instâncias da classe Livro

livro1 = Livro("1984", "George Orwell", 1949)

livro2 = Livro("1984", "George Orwell", 1950)

livro3 = Livro("Brave New World", "Aldous Huxley", 1932)

# Comparando os livros usando o método __eq__

print("livro1 é igual a livro2?", livro1 == livro2) # Deve retornar True

print("livro1 é igual a livro3?", livro1 == livro3) # Deve retornar False

# Adicionando os livros a um conjunto

conjunto_livros = {livro1, livro2, livro3}

print("Conjunto de livros:", conjunto_livros) # Deve conter livro1 e livro3, pois livro1 e livro2 são iguais

Questões:

1- Liste os principais métodos especiais usados para definir igualdade em Python.

Resposta esperada: Os principais métodos especiais são __eq__ para definir igualdade e __hash__ para permitir que objetos sejam usados em conjuntos e dicionários.

2-Explique com suas próprias palavras como o método __eq__ funciona e por que ele é importante.

Resposta esperada: O método __eq__ é usado para comparar dois objetos e determinar se eles são iguais com base em atributos específicos. Ele é importante porque permite personalizar a lógica de comparação, garantindo que objetos sejam comparados corretamente.

3- Implemente uma classe Pessoa onde duas pessoas são consideradas iguais se tiverem o mesmo nome e idade. Adicione duas instâncias dessa classe a um conjunto e exiba o resultado.

*Resposta esperada:*

class Pessoa:

def __init__(self, nome, idade):

self.nome = nome

self.idade = idade

def __eq__(self, outro):

if isinstance(outro, Pessoa):

return self.nome == outro.nome and self.idade == outro.idade

return False

def __hash__(self):

return hash((self.nome, self.idade))

def __repr__(self):

return f"Pessoa(nome='{self.nome}', idade={self.idade})"

pessoa1 = Pessoa("Alice", 30)

pessoa2 = Pessoa("Alice", 30)

pessoa3 = Pessoa("Bob", 25)

conjunto_pessoas = {pessoa1, pessoa2, pessoa3}

print(conjunto_pessoas) # Deve conter pessoa1 (ou pessoa2) e pessoa3, pois pessoa1 e pessoa2 são iguais

4- Identifique as partes do código de exemplo que permitem a comparação e uso de objetos Livro em conjuntos e explique como elas funcionam.

Resposta esperada: O método __eq__ compara os atributos titulo e autor para determinar se dois objetos Livro são iguais. O método __hash__ calcula um valor de hash baseado nesses atributos, permitindo que os objetos sejam usados em conjuntos. O método __repr__ fornece uma representação legível dos objetos para facilitar a depuração.

5- Faça uma crítica sobre a implementação da igualdade na classe Livro. Existe algum ponto que poderia ser melhorado ou outro atributo que deveria ser considerado na comparação?

Resposta esperada: A implementação atual compara apenas titulo e autor, o que pode ser adequado na maioria dos casos. No entanto, se a edição ou ano de publicação for relevante para a igualdade, esses atributos também poderiam ser incluídos na comparação.

6- Desenvolva um projeto onde você implemente uma classe Produto para um sistema de estoque, garantindo que dois produtos sejam considerados iguais se tiverem o mesmo código de barras. Adicione vários produtos a um conjunto e verifique a correta identificação de duplicatas.

*Resposta esperada:*

class Produto:

def __init__(self, nome, codigo_barras, preco):

self.nome = nome

self.codigo_barras = codigo_barras

self.preco = preco

def __eq__(self, outro):

if isinstance(outro, Produto):

return self.codigo_barras == outro.codigo_barras

return False

def __hash__(self):

return hash(self.codigo_barras)

def __repr__(self):

return f"Produto(nome='{self.nome}', codigo_barras='{self.codigo_barras}', preco={self.preco})"

produto1 = Produto("Produto A", "123456789", 19.99)

produto2 = Produto("Produto B", "123456789", 29.99)

produto3 = Produto("Produto C", "987654321", 39.99)

conjunto_produtos = {produto1, produto2, produto3}

print(conjunto_produtos) # Deve conter produto1 (ou produto2) e produto3, pois produto1 e produto2 têm o mesmo código de barras
