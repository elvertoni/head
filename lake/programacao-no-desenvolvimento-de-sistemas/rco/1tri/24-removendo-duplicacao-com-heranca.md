---
titulo: "Removendo duplicação com herança"
tipo: rco-seed
disciplina: programacao-no-desenvolvimento-de-sistemas
sigla_rco: PDS
trimestre: 1
ordem_rco: 24
serie: 3
aula_rco: "Aula 24"
slides: 23
tem_atividade: true
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/1TRI/24-removendo-duplicacao-com-heranca/24-removendo-duplicacao-com-heranca.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PDS/1TRI/24-removendo-duplicacao-com-heranca/AULA 24_ATIVIDADE_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PDS/1TRI/24-removendo-duplicacao-com-heranca/AULA 24_SAIBA MAIS_ PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Removendo duplicação com herança

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO NO
- DESENVOLVIMENTO DE
- SISTEMAS
- 3ª SÉRIE
- Removendo duplicação com herança
- Aula 24

_3 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- DESENVOLVIMENTO DE SISTEMAS
- Na aula de hoje, vamos:
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store
- Implementar o conceito de herança na eliminação de duplicações de código, promovendo a sua reutilização de maneira eficaz.

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
- Relembramos alguns conceitos (classes - objetos - atributos - métodos - encapsulamento), fundamentais para criar classes bem definidas e responsáveis por suas próprias funcionalidades e dados.

_4 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Felipe, um desenvolvedor junior, se depara com várias classes em seu projeto que compartilham muitos métodos e atributos semelhantes, resultando em um código extenso e difícil de manter…
- https://img.freepik.com/premium-photo/thoughtful-professional-man-portrait-studio-professional-man-glasses_474717-101263.jpg?size=626&ext=jpg&ga=GA1.1.1700460183.1712793600&semt=ais

_4 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- "Como posso simplificar meu código evitando repetições?"
- Quem sabe responde!
- Ele se pergunta…

_5 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Felipe pode utilizar o conceito de herança, permitindo que classes compartilhem métodos e atributos comuns através de uma classe-pai, reduzindo a duplicação e facilitando a manutenção.

_4 imagem(ns) no slide._

> **Notas do apresentador:** Comentário: A herança é uma poderosa ferramenta da programação orientada a objetos que ajuda a reduzir a complexidade do código, promove a reutilização e facilita a manutenção. Ao identificar os elementos comuns entre classes, João pode criar uma classe base da qual outras classes derivam, herdando suas propriedades e métodos. Isso não apenas economiza tempo mas também minimiza erros, tornando o código mais limpo e organizado.

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- Herança
- É um dos pilares fundamentais da Programação Orientada a Objetos (POO) e serve como uma ferramenta poderosa para promover a reutilização de código, reduzindo a duplicação e facilitando a manutenção de projetos de software.

_4 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- A ideia por trás da herança é permitir que novas classes adquiram propriedades e métodos de classes existentes, chamadas de classes-pais ou superclasses.
- Isso significa que uma classe filha pode estender a funcionalidade de uma classe-pai sem precisar reescrever o código já existente.

_5 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Finalidade
- A finalidade da herança é promover um maior nível de abstração e reutilização no desenvolvimento de software.
- Ao herdar de uma classe pai, a classe filha automaticamente incorpora todos os métodos e atributos da classe pai, permitindo que o desenvolvedor se concentre em implementar novas funcionalidades específicas para a classe filha.
- Isso traz uma economiza de tempo e ajuda a manter o
- código mais limpo, organizado e fácil de entender!

_4 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- Um exemplo clássico de herança é uma
- hierarquia de classes de veículos.
- Podemos então criar classes derivadas, como Carro e Moto, que herdam essas propriedades e métodos da classe Veiculo, mas também introduzem suas peculiaridades, como o atributo numeroDePortas no caso do Carro, ou cilindradas para a Moto.
- Imagine uma classe base chamada Veiculo, que possui atributos como marca, modelo e ano, além de métodos como ligar() e desligar().

_5 imagem(ns) no slide._

### Slide 13

- DESENVOLVIMENTO DE SISTEMAS
- Exemplos
- Acesse o Saiba Mais

_4 imagem(ns) no slide._

### Slide 14

- DESENVOLVIMENTO DE SISTEMAS
- Atividade para a fixação do conteúdo estudado
- Qual das seguintes afirmações melhor descreve a herança em Python?
- (A) Permite criar novas classes sem herdar de nenhuma classe existente.
- (B) É um mecanismo de reutilizar código criando uma nova classe a partir de uma existente.
- (C) Usada apenas para modificar métodos existentes em outras classes.
- (D) Permite que uma classe herde múltiplos métodos estáticos de outras classes.
- Escolhendo alguém para responder essa questão!

_4 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- RESPOSTA
- Qual das seguintes afirmações melhor descreve a herança em Python?
- (A) Permite criar novas classes sem herdar de nenhuma classe existente.
- (B) É um mecanismo de reutilizar código criando uma nova classe a partir de uma existente.
- (C) Usada apenas para modificar métodos existentes em outras classes.
- (D) Permite que uma classe herde múltiplos métodos estáticos de outras classes.
- Resposta correta:
- (B) É um mecanismo de reutilizar código criando uma nova classe a partir de uma existente.

_3 imagem(ns) no slide._

> **Notas do apresentador:** Comentário: A herança é fundamental em Python para a reutilização de código, permitindo que novas classes adotem atributos e comportamentos de classes existentes, estendendo ou modificando suas funcionalidades de maneira eficiente.

### Slide 16

- DESENVOLVIMENTO DE SISTEMAS
- Conclusão
- A herança é uma técnica poderosa na POO que ajuda a reduzir a duplicação de código, facilitando a manutenção e promovendo uma estrutura de código mais limpa e organizada.

_4 imagem(ns) no slide._

### Slide 17

- DESENVOLVIMENTO DE SISTEMAS
- DESENVOLVIMENTO DE SISTEMAS
- Atividade Prática na Plataforma Alura
- Na plataforma Alura vamos acessar o seguinte curso:
- A recomendação é que você continue esse curso extraclasse, pois ele traz um conteúdo essencial para compreender sobre o referido tema.
- Link para o curso: https://cursos.alura.com.br/course/python-3-avancando-orientacao-objetos

_8 imagem(ns) no slide._

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- Explicando a herança
- 8 minutos
- Link para tarefa: https://cursos.alura.com.br/course/python-3-avancando-orientacao-objetos/task/41795
- A herança é um pilar da programação orientada a objetos, permitindo que uma classe herde atributos e métodos de outra, facilitando a reutilização de código e a criação de relações hierárquicas entre classes, otimizando assim o desenvolvimento de sistemas mais complexos e mantendo a coesão.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje:
- Exploramos como a herança permite compartilhar código comum entre classes, reduzindo a duplicação e facilitando a manutenção do código em projetos de software.
- https://media.licdn.com/dms/image/D4D12AQFe5Ie0x29PdQ/article-cover_image-shrink_720_1280/0/1702765551324?e=2147483647&v=beta&t=sPYE-m6e0L1EEuvlGR2Ey1PUci_zFwICrSYmRnfaY9M

_4 imagem(ns) no slide._

### Slide 20

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

### Slide 21

- DESENVOLVIMENTO DE SISTEMAS
- Referências (Imagens)
- Figuras e Imagens:
- https://www.flaticon.com/br
- https://www.istockphoto.com/br
- https://raw.githubusercontent.com/zbtang/React-Native-ViewPager/HEAD/imgs/dotIndicator.gif
- https://storyset.com

_3 imagem(ns) no slide._

### Slide 22

- DESENVOLVIMENTO DE SISTEMAS
- O RCO+Aulas é um projeto da Secretaria de Estado da Educação do Paraná e está em constante revisão. Todos os slides são de uso exclusivo dos professores da Rede Pública de Ensino, com a finalidade específica de aplicação em sala de aula, sendo totalmente vedada a publicização, reutilização, reprodução total ou parcial para quaisquer outros fins.

_4 imagem(ns) no slide._

### Slide 23

- DESENVOLVIMENTO DE SISTEMAS
- Esta publicação tem a cooperação entre a UNESCO e a Secretaria de Estado da Educação e do Esporte do Paraná no âmbito da parceria PRODOC 914BRZ1091, cujo objetivo é trazer soluções inovadoras de gestão da rede pública estadual de educação do Paraná para a melhoria da aprendizagem dos alunos. As indicações de nomes e a apresentação do material ao longo desta publicação não implicam a manifestação de qualquer opinião por parte da UNESCO a respeito da condição jurídica de qualquer país, território, cidade, região ou de suas autoridades, tampouco da delimitação de suas fronteiras ou limites As ideias e opiniões expressas nesta publicação são as dos autores e não refletem obrigatoriamente as da UNESCO nem comprometem a Organização.
- Cooperação Técnica

_4 imagem(ns) no slide._

## Atividade

_Fonte: AULA 24_ATIVIDADE_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

ATIVIDADE AULA 24

Questão 1

O que é herança na programação orientada a objetos?

a) Uma função que calcula a média de valores

b) Um loop que executa até que uma condição seja verdadeira

c) Uma forma de uma classe herdar propriedades e métodos de outra classe (Correta)

d) Uma maneira de criar interfaces gráficas no Python

Comentário: Herança permite que uma classe derive propriedades e métodos de outra, promovendo reutilização de código e organização.

Questão 2

Qual é o propósito principal da herança?

a) Reduzir a duplicação de código e facilitar a manutenção (Correta)

b) Aumentar a complexidade do código

c) Limitar o uso de métodos entre classes

d) Criar mais variáveis globais

Comentário: A herança visa reduzir a duplicação de código ao permitir que classes compartilhem atributos e métodos, facilitando a manutenção do sistema.

## Outros documentos

_Fonte: AULA 24_SAIBA MAIS_ PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

SAIBA MAIS AULA 23

Exemplo prático:

class Veiculo:

def __init__(self, marca, modelo, ano):

self.marca = marca

self.modelo = modelo

self.ano = ano

def ligar(self):

print("Veículo ligado")

def desligar(self):

print("Veículo desligado")

class Carro(Veiculo):

def __init__(self, marca, modelo, ano, numeroDePortas):

super().__init__(marca, modelo, ano)

self.numeroDePortas = numeroDePortas

class Moto(Veiculo):

def __init__(self, marca, modelo, ano, cilindradas):

super().__init__(marca, modelo, ano)

self.cilindradas = cilindradas

A utilização da herança facilita a expansão e a manutenção do código, pois mudanças feitas na classe pai automaticamente se refletem nas classes filhas, a menos que sejam explicitamente sobrescritas. Isso garante consistência e reduz a probabilidade de erros.
