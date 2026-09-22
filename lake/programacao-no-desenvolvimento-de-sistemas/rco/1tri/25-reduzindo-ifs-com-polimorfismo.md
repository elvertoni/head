---
titulo: "Reduzindo ifs com polimorfismo"
tipo: rco-seed
disciplina: programacao-no-desenvolvimento-de-sistemas
sigla_rco: PDS
trimestre: 1
ordem_rco: 25
serie: 3
aula_rco: "Aula 25"
slides: 26
tem_atividade: true
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/1TRI/25-reduzindo-ifs-com-polimorfismo/25-reduzindo-ifs-com-polimorfismo.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PDS/1TRI/25-reduzindo-ifs-com-polimorfismo/AULA 25_ATIVIDADE_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PDS/1TRI/25-reduzindo-ifs-com-polimorfismo/AULA 25_SAIBA MAIS_ PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Reduzindo ifs com polimorfismo

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO NO
- DESENVOLVIMENTO DE
- SISTEMAS
- 3ª SÉRIE
- Reduzindo ifs com polimorfismo
- Aula 25

_3 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- DESENVOLVIMENTO DE SISTEMAS
- Na aula de hoje, vamos:
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store
- Reconhecer como o polimorfismo pode simplificar o controle de fluxo, substituindo múltiplas condicionais por uma arquitetura mais flexível e escalável.

_7 imagem(ns) no slide._

### Slide 4

- DESENVOLVIMENTO DE SISTEMAS
- ATENÇÃO PROFESSOR!
- O Material aqui apresentado, segue a análise do plano de curso contemplando os componentes curriculares e seus objetos de conhecimento, sendo assim, você tem liberdade para customizar o material conforme seu contexto para maior aproveitamento do conteúdo. Em caso de falta ou indisponibilidade de acesso à internet no local de aula, você poderá utilizar os seguintes artigos para criação de material complementar para auxiliar na aula:
- Leitura/Recursos Adicionais:
- Para praticar os conceitos apresentados, recomendamos o uso do Repl.it, uma IDE online que suporta múltiplas linguagens, incluindo Python, facilitando a experimentação com herança.

_5 imagem(ns) no slide._

### Slide 5

- DESENVOLVIMENTO DE SISTEMAS
- Na aula anterior…
- Trabalhamos o encapsulamento e coesão em Python, detalhando como encapsular comportamento e dados dentro de classes para a manutenção e a clareza do código.

_4 imagem(ns) no slide._

### Slide 6

- https://st5.depositphotos.com/10614052/64464/i/450/depositphotos_644648172-stock-photo-young-bearded-man-laptop-video.jpg
- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Daniel, um jovem programador, enfrenta um código cheio de condicionais if que complicam as atualizações e o entendimento do sistema.
- Ele descobre o polimorfismo como uma solução potencial!

_4 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Como Daniel pode implementar polimorfismo para simplificar seu código?
- Quem sabe responde!
- https://st5.depositphotos.com/10614052/64425/i/150/depositphotos_644257770-stock-photo-young-bearded-man-laptop-sitting.jpg

_5 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Isso elimina a necessidade de condicionais, pois o método correto é chamado de acordo com o tipo de objeto.
- Daniel pode definir métodos em uma classe base e permitir que cada subclasse implemente-os de maneira específica.
- https://st5.depositphotos.com/10614052/64555/i/600/depositphotos_645556118-stock-photo-young-bearded-man-pointing-laptop.jpg

_4 imagem(ns) no slide._

> **Notas do apresentador:** Comentário: Ao usar polimorfismo, João pode manter o código mais organizado e fácil de expandir, evitando condicionais excessivas e tornando o sistema mais modular e flexível.

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- Polimorfismo
- O conceito de polimorfismo é um dos pilares da Programação Orientada a Objetos (OOP), simplificando e expandindo o código, especialmente quando lidamos com uma série de operações condicionais (ifs).
- Polimorfismo, do grego "muitas formas", permite que métodos com o mesmo nome comportem-se de maneira diferente em diferentes classes.
- https://netmidiapropaganda.com.br/wp-content/uploads/2019/03/camelao.gif

_4 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- Finalidade e Utilização
- O polimorfismo é usado para tornar sistemas mais modulares, fáceis de entender e expandir, permitindo que programadores utilizem a mesma interface para diferentes tipos de dados subjacentes.
- Se o objeto for de uma classe Dog, ele pode retornar "bark", e se for de uma classe Cat, ele pode retornar "meow".
- Por exemplo, você pode ter uma função que chama o método .speak() em um objeto.
- https://www.petz.com.br/blog//wp-content/uploads/2019/09/cachorros-e-gatos.jpg

_5 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Finalidade e Utilização
- A função .speak() não precisa saber que tipo de animal é, ela apenas sabe que pode chamar esse método.
- Isso reduz a necessidade de verificar o tipo do objeto ou implementar condicionais complexas para determinar o comportamento.
- https://vetquality.com.br/wp-content/uploads/sites/2/2024/02/cao-e-gato-filhotes.jpg

_4 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- Reduzindo ifs com Polimorfismo
- Isso elimina a necessidade de múltiplas verificações if e torna o código mais fácil de gerenciar.
- Na prática, isso significa que ao invés de um bloco de condicionais que executam diferentes blocos de código dependendo do tipo de objeto, métodos sobrecarregados são chamados com base na classe do objeto.

_4 imagem(ns) no slide._

### Slide 13

- DESENVOLVIMENTO DE SISTEMAS
- Além de manipular comportamentos, o polimorfismo também pode ser utilizado para personalizar a representação textual de objetos, isto é, como os objetos são apresentados quando convertidos em strings. Isso é geralmente alcançado sobrescrevendo o método especial __str__ em Python.
- Representação Textual de Objetos

_4 imagem(ns) no slide._

### Slide 14 (oculto)

- DESENVOLVIMENTO DE SISTEMAS
- Exemplos
- Acesse o arquivo Saiba Mais!

_4 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- Atividade para a fixação do conteúdo estudado
- Qual das seguintes afirmações melhor descreve o polimorfismo?
- (A) Permite que diferentes classes tenham métodos com o mesmo nome mas implementações diferentes.
- (B) Restringe os métodos que podem ser chamados baseados no tipo de dados.
- (C) Requer que todos os métodos sejam estáticos e privados.
- (D) Impede a reutilização de código entre classes relacionadas.
- Escolhendo alguém para responder essa questão!

_4 imagem(ns) no slide._

### Slide 16

- DESENVOLVIMENTO DE SISTEMAS
- Atividade para a fixação do conteúdo estudado
- Qual das seguintes afirmações melhor descreve o polimorfismo?
- (A) Permite que diferentes classes tenham métodos com o mesmo nome mas implementações diferentes.
- (B) Restringe os métodos que podem ser chamados baseados no tipo de dados.
- (C) Requer que todos os métodos sejam estáticos e privados.
- (D) Impede a reutilização de código entre classes relacionadas.
- Resposta correta:
- (A) Permite que diferentes classes tenham métodos com o mesmo nome mas implementações diferentes.

_3 imagem(ns) no slide._

> **Notas do apresentador:** Comentário sobre a resposta: A resposta correta é a alternativa (a). O polimorfismo é uma característica fundamental da programação orientada a objetos que permite que objetos de diferentes classes derivadas sejam tratados como objetos de uma classe base, com cada tipo respondendo de maneira diferente ao mesmo método ou mensagem, facilitando a reutilização e a expansão do código.

### Slide 17

- DESENVOLVIMENTO DE SISTEMAS
- Conclusão
- O polimorfismo e representações textuais são essenciais para eficiência e clareza no código, permitindo flexibilidade no tratamento de diferentes tipos de objetos e uma interação mais intuitiva com o usuário.

_4 imagem(ns) no slide._

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- DESENVOLVIMENTO DE SISTEMAS
- Atividade Prática na Plataforma Alura
- Na plataforma Alura vamos acessar o seguinte curso:
- A recomendação é que você continue esse curso extraclasse, pois ele traz um conteúdo essencial para compreender sobre o referido tema.
- Link para o curso: https://cursos.alura.com.br/course/python-3-avancando-orientacao-objetos

_8 imagem(ns) no slide._

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- Polimorfismo
- 11 minutos
- Link para tarefa: https://cursos.alura.com.br/course/python-3-avancando-orientacao-objetos/task/41783
- Polimorfismo é um princípio da programação orientada a objetos que permite que métodos com o mesmo nome atuem de forma diferente em diferentes classes. Isso aumenta a flexibilidade e a reutilização de código, permitindo diferentes comportamentos para uma interface comum.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 20

- DESENVOLVIMENTO DE SISTEMAS
- Reduzindo ifs
- 11 minutos
- Link para tarefa: https://cursos.alura.com.br/course/python-3-avancando-orientacao-objetos/task/41784
- Reduzir o uso excessivo de instruções "if" por meio de polimorfismo melhora a clareza e a manutenção do código. Em vez de múltiplas verificações condicionais, a lógica específica de cada tipo de objeto é encapsulada em suas próprias classes, facilitando as atualizações e a leitura do código.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 21

- DESENVOLVIMENTO DE SISTEMAS
- Representação textual de objetos
- 7 minutos
- Link para tarefa: https://cursos.alura.com.br/course/python-3-avancando-orientacao-objetos/task/41785
- A representação textual de objetos em programação, geralmente implementada através de métodos como `__str__` ou `__repr__` em Python, permite visualizar informações de objetos de forma legível, facilitando o debug e a logística de dados.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 22

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje:
- Reconhecemos como o polimorfismo ajuda a reduzir o uso de estruturas condicionais (ifs) e como a representação textual via __str__ facilita a visualização e o debug de objetos, essencial para uma programação mais limpa e compreensível.

_3 imagem(ns) no slide._

### Slide 23

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

_Fonte: AULA 25_ATIVIDADE_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

ATIVIDADE AULA 25

Questão 1

O que o polimorfismo permite em programação orientada a objetos?

a) A criação de métodos que não podem ser reescritos.

b) A aplicação de funções matemáticas em todos os objetos.

c) Classes derivadas a terem métodos que reagem diferentemente ao mesmo chamado de método da classe base.

d) Todos os objetos devem ter os mesmos métodos e propriedades.

Resposta correta: c) Classes derivadas a terem métodos que reagem diferentemente ao mesmo chamado de método da classe base.

Comentário: O polimorfismo é uma técnica que permite que métodos com o mesmo nome comportem-se de forma diferente para cada classe derivada, aumentando a flexibilidade e a possibilidade de reutilização de código.

Questão 2

Qual é o principal benefício de utilizar a representação textual de objetos em Python através do método __str__?

a) Forçar todos os objetos a converterem para string antes de serem processados.

b) Permitir uma representação legível e personalizada de objetos quando impressos.

c) Garantir que todos os erros sejam mostrados como strings.

d) Converter automaticamente todos os atributos de objeto em strings privadas.

Resposta correta: b) Permitir uma representação legível e personalizada de objetos quando impressos.

Comentário: O método __str__ é usado para definir uma representação legível do objeto que é conveniente para o usuário final, especialmente quando os objetos precisam ser impressos ou convertidos em strings de forma clara.

## Outros documentos

_Fonte: AULA 25_SAIBA MAIS_ PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

SAIBA MAIS AULA 23

Exemplo prático:

class Animal:

def speak(self):

raise NotImplementedError("Subclasses must implement this!")

class Dog(Animal):

def speak(self):

return "bark"

class Cat(Animal):

def speak(self):

return "meow"

# Uso de polimorfismo

def make_animal_speak(animal):

print(animal.speak())

# Criando instâncias

dog = Dog()

cat = Cat()

# Chamando a função

make_animal_speak(dog)

make_animal_speak(cat)
