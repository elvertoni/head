---
titulo: "e um modelo de dados"
tipo: rco-seed
disciplina: programacao-no-desenvolvimento-de-sistemas
sigla_rco: PDS
trimestre: 1
ordem_rco: 27
serie: 3
aula_rco: "Aula 27"
slides: 26
tem_atividade: true
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/1TRI/27-duck-typing-e-um-modelo-de-dados/27-duck-typing-e-um-modelo-de-dados.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PDS/1TRI/27-duck-typing-e-um-modelo-de-dados/AULA 27_ATIVIDADE_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# e um modelo de dados

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO NO
- DESENVOLVIMENTO DE
- SISTEMAS
- 3ª SÉRIE
- O Duck Typing
- e um modelo de dados
- Aula 27

_3 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- DESENVOLVIMENTO DE SISTEMAS
- Na aula de hoje, vamos:
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store
- Demonstrar como o conceito de "Duck Typing" se aplica no Python, facilitando a interação entre objetos.

_7 imagem(ns) no slide._

### Slide 4 (oculto)

- DESENVOLVIMENTO DE SISTEMAS
- ATENÇÃO PROFESSOR!
- O Material aqui apresentado, segue a análise do plano de curso contemplando os componentes curriculares e seus objetos de conhecimento, sendo assim, você tem liberdade para customizar o material conforme seu contexto para maior aproveitamento do conteúdo. Em caso de falta ou indisponibilidade de acesso à internet no local de aula, você poderá utilizar os seguintes artigos para criação de material complementar para auxiliar na aula:
- Leitura/Recursos Adicionais:
- Para aprofundamento, recomendo a leitura do Python Enhancement Proposal (PEP) relacionado a duck typing e ABCs. Utilize o IDE online Repl.it para experimentar os exemplos em tempo real sem necessidade de instalação local.

_5 imagem(ns) no slide._

### Slide 5

- DESENVOLVIMENTO DE SISTEMAS
- Na aula anterior…
- Observamos a importância do encapsulamento e como Python suporta este encapsulamento através de convenções, como o uso de sublinhado (_), para denotar métodos privados.

_4 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Marcos, um desenvolvedor júnior, está trabalhando em um projeto que requer integração de várias classes com funcionalidades semelhantes!
- Ele notou que algumas classes não funcionam bem juntas devido à rigidez de tipo…

_5 imagem(ns) no slide._

### Slide 7

- Quem sabe responde!
- DESENVOLVIMENTO DE SISTEMAS
- Como o Duck Typing pode ajudar Marcos a melhorar a interoperabilidade dessas classes?

_6 imagem(ns) no slide._

### Slide 8

- Resposta
- Se os objetos têm métodos compatíveis, eles podem interagir, reduzindo a necessidade de herança rígida e promovendo um código mais flexível e reutilizável.
- DESENVOLVIMENTO DE SISTEMAS
- O Duck Typing permite que Marcos foque mais no comportamento de objetos, do que em sua tipologia exata!

_5 imagem(ns) no slide._

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- Duck Typing
- O conceito de "Duck Typing" no mundo da programação, especialmente em Python, é baseado no ditado:
- "Se parece um pato, nada como um pato e faz quack como um pato, então provavelmente é um pato".

_4 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- Duck Typing
- Ele permite que um objeto seja utilizado em qualquer lugar, desde que suporte os métodos e atributos esperados, promovendo uma flexibilidade significativa no código.
- Em termos de programação, isso significa que o tipo de um objeto é menos importante do que os métodos e propriedades que este possui.

_4 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Este método pode ser usado com qualquer objeto que tenha um método read(), independentemente da classe do objeto.

_4 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- A linguagem Python é altamente flexível, permitindo que os desenvolvedores manipulem essas estruturas de dados (como listas, dicionários, entre outros) de maneira poderosa e intuitiva.
- Por outro lado, o modelo de dados em Python refere-se à estrutura que define como os objetos são construídos e interagem entre si.
- https://static.vecteezy.com/ti/fotos-gratis/p1/10098739-bola-python-sobre-fundo-branco-gratis-foto.jpg

_7 imagem(ns) no slide._

### Slide 13

- DESENVOLVIMENTO DE SISTEMAS
- Todas as classes em Python podem ter atributos e métodos adicionados a elas dinamicamente, o que é um reflexo direto de seu modelo de dados flexível.

_4 imagem(ns) no slide._

### Slide 14

- DESENVOLVIMENTO DE SISTEMAS
- Classes abstratas
- Abstract Base Classes (ABCs) são conceitos importantes em Python, utilizados para definir um conjunto de métodos e propriedades que uma classe deve implementar.
- As ABCs são uma forma de garantir que certos métodos sejam criados nas subclasses, ajudando na construção de uma interface consistente e eficaz em situações de desenvolvimento colaborativo ou em projetos de grande escala.

_4 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- Resumindo…
- O Duck Typing, o modelo de dados flexível de Python e o uso de Classes Abstratas permitem criar softwares flexíveis e robustos.
- A utilização dessas práticas facilita a manutenção, escalabilidade e compreensão do código, elementos essenciais para o desenvolvimento eficiente em ambientes dinâmicos e diversificados de programação.

_4 imagem(ns) no slide._

### Slide 16

- DESENVOLVIMENTO DE SISTEMAS
- Atividade para a fixação do conteúdo estudado
- Qual das seguintes afirmações melhor descreve o conceito de Duck Typing em Python?
- (A) Requer que todos os objetos herdem de uma classe base comum.
- (B) Permite a execução de qualquer método, desde que exista na classe.
- (C) Permite a utilização de um objeto em qualquer lugar, contanto que este suporte os métodos e atributos esperados.
- (D) Força que métodos específicos sejam escritos com assinaturas exatas.
- Troque ideias com seus colegas!

_4 imagem(ns) no slide._

### Slide 17

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Qual das seguintes afirmações melhor descreve o conceito de Duck Typing em Python?
- (A) Requer que todos os objetos herdem de uma classe base comum.
- (B) Permite a execução de qualquer método, desde que exista na classe.
- (C) Permite a utilização de um objeto em qualquer lugar, contanto que este suporte os métodos e atributos esperados.
- (D) Força que métodos específicos sejam escritos com assinaturas exatas.
- Resposta Correta: (C) Permite a utilização de um objeto em qualquer lugar, contanto que este suporte os métodos e atributos esperados.

_3 imagem(ns) no slide._

> **Notas do apresentador:** Comentário sobre a resposta: A alternativa (c) capta essencialmente o princípio do Duck Typing. No Python, não importa qual classe o objeto pertence; o que importa são as funcionalidades (métodos e atributos) que o objeto suporta. Isso permite flexibilidade e polimorfismo sem a necessidade de uma hierarquia de herança rígida.

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- Conclusão
- O Python emprega Duck Typing e Classes Abstratas para oferecer flexibilidade e garantir padrões em design de software, facilitando a criação de sistemas robustos e de fácil manutenção.

_4 imagem(ns) no slide._

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- Atividade Prática na Plataforma Alura
- Na plataforma Alura vamos acessar o seguinte curso:
- A recomendação é que você continue esse curso extraclasse, pois ele traz um conteúdo essencial para compreender sobre o referido tema.
- Link para o curso: https://cursos.alura.com.br/course/python-3-avancando-orientacao-objetos

_6 imagem(ns) no slide._

### Slide 20

- DESENVOLVIMENTO DE SISTEMAS
- Modelo de dados Python
- 11 minutos
- Link para tarefa: https://cursos.alura.com.br/course/python-3-avancando-orientacao-objetos/task/41790
- O modelo de dados Python permite a definição estruturada de dados com classes, facilitando a organização e manipulação de complexas estruturas de dados através de métodos, atributos e herança, promovendo reusabilidade e clareza no código.
- Atividade no portal Alura

_8 imagem(ns) no slide._

### Slide 21

- DESENVOLVIMENTO DE SISTEMAS
- Classes abstratas ou ABCs
- 10 minutos
- Link para tarefa: https://cursos.alura.com.br/course/python-3-avancando-orientacao-objetos/task/41791
- Classes abstratas em Python, conhecidas como Abstract Base Classes (ABCs), são usadas para definir métodos que devem ser criados em subclasses, garantindo uma estrutura comum e prevenindo a instanciação direta, essencial para o design de software robusto.
- Atividade no portal Alura

_8 imagem(ns) no slide._

### Slide 22

- O que vimos na aula de hoje
- Aplicamos os conceitos avançados Duck Typing e Classes Abstratas, compreendendo os seus impactos na reutilização e manutenção do código em Python, proporcionando uma base sólida para um desenvolvimento eficiente.
- DESENVOLVIMENTO DE SISTEMAS

_4 imagem(ns) no slide._

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

_Fonte: AULA 27_ATIVIDADE_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

ATIVIDADE AULA 27

Questão 1

Qual é o principal benefício do uso de Classes Abstratas em Python (ABCs)?

a) Forçar a criação de métodos não relacionados.

b) Permitir a criação de classes que não podem ser instanciadas.

c) Impedir a herança de qualquer classe.

d) Aumentar a eficiência do código.

Resposta Correta: b) Permitir a criação de classes que não podem ser instanciadas.

Comentário sobre a resposta:

Classes Abstratas ou Abstract Base Classes (ABCs) são usadas para criar uma classe base com métodos que devem ser implementados por subclasses, garantindo assim uma interface consistente. Elas não podem ser instanciadas diretamente, o que ajuda a evitar erros de design e implementação.

Questão 2

O que o conceito de Duck Typing facilita em Python?

a) A verificação de tipos em tempo de compilação.

b) A escrita de código mais seguro e previsível.

c) O uso de objetos baseado em seus métodos atuais, não no tipo.

d) A restrição na maneira como objetos de diferentes classes interagem.

Resposta Correta: c) O uso de objetos baseado em seus métodos atuais, não no tipo.

Comentário sobre a resposta:

Duck Typing em Python permite que o desenvolvedor se preocupe menos com o tipo do objeto e mais com a funcionalidade que ele oferece, o que pode simplificar o design e melhorar a reutilização do código.
