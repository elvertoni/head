---
titulo: "Classes e Objetos em python"
tipo: rco-seed
disciplina: programacao-no-desenvolvimento-de-sistemas
sigla_rco: PDS
trimestre: 1
ordem_rco: 18
serie: 3
aula_rco: "Aula 18"
slides: 25
tem_atividade: true
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/1TRI/18-classes-e-objetos-em-python/18-classes-e-objetos-em-python.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PDS/1TRI/18-classes-e-objetos-em-python/AULA 18_SAIBA MAIS_ PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/1TRI/18-classes-e-objetos-em-python/AULA 18_ATIVIDADE_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Classes e Objetos em python

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO NO
- DESENVOLVIMENTO DE
- SISTEMAS
- 3ª SÉRIE
- Classes e Objetos em python
- Aula 18

_3 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- DESENVOLVIMENTO DE SISTEMAS
- Na aula de hoje, vamos:
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store
- Explorar o conceito fundamental de classes e objetos em Python, incluindo a criação de construtores para inicializar nossos objetos.

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
- Abordamos o problema do paradigma procedural e suas particularidades frente à programação orientada a objetos.

_4 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Mateus se pergunta…
- "Como posso organizar meu código de forma mais eficiente e lógica?"
- Ao iniciar um novo projeto de sistema bancário, ele se depara com a necessidade de organizar melhor seu código para facilitar a manutenção e expansão futura.
- Mateus é um desenvolvedor iniciante que sempre programou seguindo o paradigma procedural.

_9 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Como a programação orientada a objetos pode ajudar Carlos a organizar melhor seu projeto de sistema bancário?
- (A) Permitindo que ele escreva menos código.
- (B) Organizando o código em funções independentes.
- (C) Agrupando dados e comportamentos em classes e objetos.
- (D) Fazendo o código rodar mais rápido.
- Quem sabe responde!

_4 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Resposta Correta
- (C) Agrupando dados e comportamentos em classes e objetos.

_5 imagem(ns) no slide._

> **Notas do apresentador:** Comentário sobre a resposta: A programação orientada a objetos permite a Carlos organizar seu projeto de sistema bancário de forma mais lógica e eficiente, agrupando dados (como saldo, número da conta) e comportamentos (como depósito, saque) relacionados em classes. Cada conta bancária pode ser representada como um objeto, uma instância da classe, facilitando a manutenção e a expansão do código.

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- Introdução
- Classes e objetos são conceitos centrais neste paradigma, oferecendo uma maneira de encapsular dados e comportamentos relacionados.
- No mundo da programação Python, a Programação Orientada a Objetos (POO) é um paradigma fundamental que permite aos desenvolvedores estruturar seus programas de forma eficiente e intuitiva.

_4 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- Classe
- Uma classe pode ser entendida como um blueprint ou um template para criar objetos. Ela define um conjunto de atributos (dados) e métodos (comportamentos) que serão compartilhados por todos os objetos criados a partir dela.
- Imagine uma classe como a planta de uma casa, especificando os quartos, banheiros, cozinha, e assim por diante, mas sem construir a casa real…

_4 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Objeto
- Um objeto é uma instância de uma classe. Se a classe é a planta, o objeto seria uma casa construída a partir dessa planta. Cada objeto tem seu próprio conjunto de valores para os atributos definidos pela classe, permitindo que você tenha múltiplos objetos com características próprias, mas compartilhando a mesma estrutura e comportamentos.

_4 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- Construtor
- O construtor é um método especial dentro de uma classe, tipicamente chamado de __init__ em Python.
- Ele é executado automaticamente sempre que um novo objeto da classe é criado, permitindo a inicialização dos atributos do objeto com valores específicos.
- Por exemplo, ao criar um objeto que representa uma conta bancária, o construtor pode ser usado para inicializar o número da conta, o titular e o saldo inicial.

_4 imagem(ns) no slide._

### Slide 13 (oculto)

- DESENVOLVIMENTO DE SISTEMAS
- Exemplos

_4 imagem(ns) no slide._

### Slide 14

- DESENVOLVIMENTO DE SISTEMAS
- Atividade para a fixação do conteúdo estudado
- Qual é a finalidade do método __init__ em uma classe Python?
- (A) Imprimir informações do objeto
- (B) Destruir um objeto
- (C) Inicializar atributos do objeto
- (D) Realizar cálculos matemáticos
- Escolhendo alguém para responder essa questão!

_4 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- Resposta correta
- Qual é a finalidade do método __init__ em uma classe Python?
- (A) Imprimir informações do objeto
- (B) Destruir um objeto
- (C) Inicializar atributos do objeto
- (D) Realizar cálculos matemáticos
- Resposta correta: (C) Inicializar atributos do objeto

_3 imagem(ns) no slide._

> **Notas do apresentador:** Comentário: O método __init__ é chamado automaticamente ao criar um novo objeto de uma classe, servindo para definir e inicializar os atributos do objeto, conforme especificado pelos valores passados na sua criação.

### Slide 16

- DESENVOLVIMENTO DE SISTEMAS
- Conclusão
- Classes e objetos são fundamentais em Python, permitindo modelar o mundo real de forma mais intuitiva. Com eles, organizamos dados e comportamentos de maneira estruturada.

_5 imagem(ns) no slide._

### Slide 17

- DESENVOLVIMENTO DE SISTEMAS
- Atividade Prática na Plataforma Alura
- Na plataforma Alura vamos acessar o seguinte curso:
- A recomendação é que você continue esse curso extraclasse, pois ele traz um conteúdo essencial para compreender sobre o referido tema.
- Link para o curso: https://cursos.alura.com.br/course/python-entendendo-orientacao-objetos

_5 imagem(ns) no slide._

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- Classe e Objeto
- 11 minutos
- Link para tarefa: https://cursos.alura.com.br/course/python-entendendo-orientacao-objetos/task/128378
- Classe é um modelo ou blueprint para criar objetos, definindo atributos e métodos. Objeto é uma instância de uma classe, com estados e comportamentos específicos. Usamos classes para organizar e estruturar o código em Python.
- Atividade no portal Alura

_8 imagem(ns) no slide._

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- Construtor
- 11 minutos
- Link para tarefa: https://cursos.alura.com.br/course/python-entendendo-orientacao-objetos/task/128379
- O construtor em Python, definido pelo método __init__(), inicializa novas instâncias de uma classe. Ele configura o estado inicial do objeto, atribuindo valores aos atributos do objeto quando ele é criado.
- Atividade no portal Alura

_8 imagem(ns) no slide._

### Slide 20

- DESENVOLVIMENTO DE SISTEMAS
- Acessando atributos
- 6 minutos
- Link para tarefa: https://cursos.alura.com.br/course/python-entendendo-orientacao-objetos/task/128380
- Acessar atributos em Python é feito usando o operador ponto (.). Após a criação de uma instância, você pode acessar ou modificar seus atributos diretamente: objeto.atributo. Isso permite a leitura e a escrita em atributos específicos do objeto.
- Atividade no portal Alura

_8 imagem(ns) no slide._

### Slide 21

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje:
- Compreendemos como a refatoração e a organização do código em funções podem melhorar significativamente a qualidade do software, facilitando tanto a compreensão quanto a manutenção do código por diferentes desenvolvedores.

_4 imagem(ns) no slide._

### Slide 22

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

_Fonte: AULA 18_ATIVIDADE_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

ATIVIDADE AULA 18

Questão 1

Qual método é utilizado para criar objetos em Python?

a) __start__()

b) __create__()

c) __init__()

d) __new__()

Resposta correta: c) __init__()

Comentário sobre a resposta correta: O método __init__() é o construtor em Python, usado para inicializar os atributos do objeto assim que ele é criado. Este método é chamado automaticamente ao criar uma instância de uma classe.

Questão 2

O que é um objeto em Python?

a) Uma função especial para processamento de dados.

b) Uma variável que armazena valores numéricos exclusivamente.

c) Uma estrutura de dados que armazena apenas strings.

d) Uma instância de uma classe que contém dados e métodos.

Resposta correta: d) Uma instância de uma classe que contém dados e métodos.

Comentário sobre a resposta correta: Um objeto é uma instância de uma classe, encapsulando dados (atributos) e comportamentos (métodos) específicos. Em Python, tudo é objeto, incluindo inteiros, listas, funções e mais.

## Outros documentos

_Fonte: AULA 18_SAIBA MAIS_ PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

SAIBA MAIS AULA 18

Neste exemplo, a classe ContaBancaria define uma estrutura para objetos que representam contas bancárias, incluindo um método para depositar dinheiro. O construtor inicializa cada nova conta com um número, titular e saldo, enquanto o método depositar permite aumentar o saldo da conta.

Exemplo prático:

class ContaBancaria:

def __init__(self, numero, titular, saldo=0):

self.numero = numero

self.titular = titular

self.saldo = saldo

def depositar(self, valor):

self.saldo += valor

# Criando um objeto da classe ContaBancaria

conta_do_joao = ContaBancaria("1234-5", "João", 1000)

# Usando um método do objeto

conta_do_joao.depositar(500)
