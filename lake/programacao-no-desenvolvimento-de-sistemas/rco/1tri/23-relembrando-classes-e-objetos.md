---
titulo: "Relembrando classes e objetos"
tipo: rco-seed
disciplina: programacao-no-desenvolvimento-de-sistemas
sigla_rco: PDS
trimestre: 1
ordem_rco: 23
serie: 3
aula_rco: "Aula 23"
slides: 25
tem_atividade: false
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/1TRI/23-relembrando-classes-e-objetos/23-relembrando-classes-e-objetos.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PDS/1TRI/23-relembrando-classes-e-objetos/AULA 23_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PDS/1TRI/23-relembrando-classes-e-objetos/AULA 23_SAIBA MAIS_ PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Relembrando classes e objetos

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO NO
- DESENVOLVIMENTO DE
- SISTEMAS
- 3ª SÉRIE
- Relembrando classes e objetos
- Aula 23

_3 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- DESENVOLVIMENTO DE SISTEMAS
- Na aula de hoje, vamos:
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store
- Revisar os conceitos fundamentais de classes e objetos, adicionando atributos e métodos e como encapsular comportamento em Python para estruturar melhor nossos programas.

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
- Exploramos métodos privados e estáticos, enfatizando a importância da encapsulação e do uso correto dos métodos da classe para manter a integridade e a organização do código.

_4 imagem(ns) no slide._

### Slide 6

- Para pensarmos juntos!
- Como posso organizar melhor essa classe para reutilizá-la sem repetir o código?
- DESENVOLVIMENTO DE SISTEMAS
- Mas, tem algo que lhe preocupa…
- Marcelo, um desenvolvedor júnior, está desenvolvendo um sistema de gerenciamento de biblioteca e se depara com a necessidade de reutilizar uma classe Livro em diferentes partes do sistema.

_5 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Como Marcelo pode reutilizar a classe Livro mantendo o código organizado e evitando repetições?
- Quem sabe responde!

_6 imagem(ns) no slide._

### Slide 8

- Resposta
- Marcelo precisa utilizar o conceito de encapsulamento para agrupar os dados (atributos) e os métodos relacionados ao Livro em uma única classe.
- Além disso, pode-se adicionar atributos e métodos específicos que sejam necessários em diferentes partes do sistema, garantindo a reutilização e a manutenção facilitada do código.
- DESENVOLVIMENTO DE SISTEMAS

_4 imagem(ns) no slide._

> **Notas do apresentador:** Comentário: Encapsular o comportamento dentro de classes permite que João mantenha o código mais organizado, facilitando a reutilização de código e a manutenção do sistema. Isso mostra a importância de compreender e aplicar os conceitos de orientação a objetos de maneira eficaz.

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- Vamos revisitar os conceitos básicos da programação orientada a objetos (POO), para construir um software de alta qualidade, bem organizado, reutilizável e de fácil manutenção. Esses conceitos fornecem uma base sólida para projetar e implementar sistemas robustos e flexíveis.
- Retomando conceitos
- importantes…

_6 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- A classe é como um blueprint, um modelo para criar objetos e o objeto é uma instância de uma classe, contendo dados (atributos) e comportamentos (métodos) definidos pela classe.
- Por exemplo, podemos ter uma classe Carro com atributos como cor e modelo, e métodos como acelerar() e frear().
- Relembrando
- a aula
- Classes e Objetos

_6 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Adicionar atributos a uma classe é simplesmente
- declarar variáveis dentro da classe.
- Métodos
- são funções definidas dentro da classe que manipulam os atributos da classe ou realizam operações específicas.
- Relembrando
- a aula
- Métodos e Atributos

_6 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- Relembrando
- a aula
- Encapsulamento
- Em Python, por exemplo, usamos métodos getters e setters para acessar ou modificar atributos privados.
- O encapsulamento ajuda na manutenção do código e na segurança dos dados, permitindo que os detalhes internos da implementação de uma classe sejam ocultados e protegidos de acessos externos indevidos.
- Este conceito é um dos pilares da POO e refere-se à restrição do acesso direto aos componentes da classe.

_7 imagem(ns) no slide._

### Slide 13 (oculto)

- DESENVOLVIMENTO DE SISTEMAS
- Exemplos
- Arquivo com exemplo:

_4 imagem(ns) no slide._

### Slide 14

- DESENVOLVIMENTO DE SISTEMAS
- Atividade para a fixação do conteúdo estudado
- Qual método é usado para inicializar um objeto da classe ContaBancaria?
- (A) depositar()
- (B) sacar()
- (C) __init__()
- (D) ContaBancaria()
- Escolhendo alguém para responder essa questão!

_4 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Qual método é usado para inicializar um objeto da classe ContaBancaria?
- (A) depositar()
- (B) sacar()
- (C) __init__()
- (D) ContaBancaria()
- Resposta Correta: (C) __init__()

_3 imagem(ns) no slide._

> **Notas do apresentador:** Comentário sobre a resposta correta: O método __init__() é o construtor da classe ContaBancaria, utilizado para inicializar os objetos desta classe com atributos iniciais como titular e saldo. Ele estabelece o estado inicial do objeto quando este é criado.

### Slide 16

- DESENVOLVIMENTO DE SISTEMAS
- Conclusão
- Ao compreendermos o conceito de classes e objetos, conseguimos construir a base para a programação orientada a objetos. Adicionando atributos e métodos a essas classes, criamos estruturas que representam entidades e suas funcionalidades no sistema.
- Além disso, a discussão sobre a importância do encapsulamento reforça a necessidade de proteger os dados e comportamentos dos objetos, garantindo segurança e integridade do sistema.

_4 imagem(ns) no slide._

### Slide 17

- DESENVOLVIMENTO DE SISTEMAS
- Atividade Prática na Plataforma Alura
- Na plataforma Alura vamos acessar o seguinte curso:
- A recomendação é que você continue esse curso extraclasse, pois ele traz um conteúdo essencial para compreender sobre o referido tema.
- Link para o curso: https://cursos.alura.com.br/course/python-3-avancando-orientacao-objetos

_5 imagem(ns) no slide._

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- Relembrando classes e objetos
- 12 minutos
- Link para tarefa: https://cursos.alura.com.br/course/python-3-avancando-orientacao-objetos/task/41777
- Revisitar classes e objetos é essencial para aprimorar a compreensão da Programação Orientada a Objeto (POO). Classes definem estruturas para objetos, que são instâncias contendo atributos e métodos específicos, facilitando a organização e modularização do código.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- Adicionando atributos e métodos
- 9 minutos
- Link para tarefa: https://cursos.alura.com.br/course/python-3-avancando-orientacao-objetos/task/41778
- Adicionar atributos e métodos a classes em POO é crucial para definir características e ações de objetos. Atributos representam dados, enquanto métodos são funções internas que manipulam esses dados ou interagem com outros objetos, aumentando a versatilidade e a reusabilidade do código.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 20

- DESENVOLVIMENTO DE SISTEMAS
- Encapsulando comportamento
- 8 minutos
- Link para tarefa: https://cursos.alura.com.br/course/python-3-avancando-orientacao-objetos/task/41779
- Encapsular comportamento em POO permite ocultar detalhes internos da classe, expondo apenas métodos necessários para a interação. Isso fortalece a modularidade e a segurança, facilitando a manutenção e a evolução do código sem impactar os usuários da classe.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 21

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje:
- Retomamos alguns conceitos importantes no contexto da programação, que contribuem para a qualidade, escalabilidade e manutenção do código.

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

## Outros documentos

_Fonte: AULA 23_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

ATIVIDADE AULA 23

Questão 1

Qual é o propósito do encapsulamento em programação orientada a objetos?

a) Aumentar a complexidade do código

b) Permitir o acesso direto a todos os atributos

c) Proteger o estado interno de um objeto

d) Facilitar a alteração de código por terceiros

Resposta Correta: c) Proteger o estado interno de um objeto

Comentário sobre a resposta correta: O encapsulamento ajuda a proteger os dados dentro de um objeto, permitindo que somente métodos específicos dentro da mesma classe possam acessar ou modificar esses dados, mantendo a integridade e a segurança do objeto.

Questão 2

Como um método pode ser definido em uma classe Python para adicionar um atributo a um objeto?

a) Utilizando uma função externa

b) Definindo um método dentro da classe que atribui um valor a um atributo

c) Atribuindo valores diretamente aos atributos fora da classe

d) Utilizando comandos especiais do Python fora da classe

Resposta Correta: b) Definindo um método dentro da classe que atribui um valor a um atributo

Comentário sobre a resposta correta: Métodos dentro de classes são usados para definir comportamentos dos objetos, incluindo a inicialização e modificação de seus atributos. Isso permite uma organização lógica e um controle mais seguro dos dados do objeto.

## Outros documentos

_Fonte: AULA 23_SAIBA MAIS_ PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

SAIBA MAIS AULA 23

Exemplo prático:

class Carro:

def __init__(self, cor, modelo):

self.cor = cor

self.modelo = modelo

def acelerar(self):

print("Acelerando...")

def frear(self):

print("Freando...")
