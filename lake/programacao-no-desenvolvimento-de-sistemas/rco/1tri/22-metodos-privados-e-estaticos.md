---
titulo: "Métodos privados e estáticos"
tipo: rco-seed
disciplina: programacao-no-desenvolvimento-de-sistemas
sigla_rco: PDS
trimestre: 1
ordem_rco: 22
serie: 3
aula_rco: "Aula 22"
slides: 24
tem_atividade: true
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/1TRI/22-metodos-privados-e-estaticos/22-metodos-privados-e-estaticos.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PDS/1TRI/22-metodos-privados-e-estaticos/AULA 22_ATIVIDADE_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PDS/1TRI/22-metodos-privados-e-estaticos/AULA 22_SAIBA MAIS_ PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Métodos privados e estáticos

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO NO
- DESENVOLVIMENTO DE
- SISTEMAS
- 3ª SÉRIE
- Métodos privados e estáticos
- Aula 22

_3 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- DESENVOLVIMENTO DE SISTEMAS
- Na aula de hoje, vamos:
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store
- Reconhecer a importância dos métodos privados e estáticos na programação orientada a objetos em Python, destacando suas aplicações e benefícios.

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
- Utilizamos conceitos de encapsulamento, atributos privados, e coesão, fundamentais para a construção de softwares robustos e bem estruturados.

_4 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Ele precisa criar métodos que possam ser usados sem a necessidade de instanciar objetos.
- "Como posso implementar métodos privados e estáticos em Python para atender a essas necessidades?"
- João é um desenvolvedor iniciante que se depara com a necessidade de restringir o acesso a certos métodos de uma classe em seu projeto de software, garantindo que somente a própria classe possa chamá-los.
- Ele se pergunta:

_5 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Respondendo a pergunta!
- Quem sabe responde!
- Por que usar métodos privados em Python?
- (A) Para melhorar a performance do código.
- (B) Para permitir acesso irrestrito aos métodos.
- (C) Para restringir o acesso aos métodos fora da classe.
- (D) Para tornar todos os métodos acessíveis globalmente.

_5 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- (C) Para restringir o acesso aos métodos fora da classe.

_4 imagem(ns) no slide._

> **Notas do apresentador:** Comentário sobre a resposta: Métodos privados em Python são utilizados para limitar o acesso a determinadas funcionalidades da classe, garantindo que somente a própria classe possa utilizá-los. Isso ajuda a manter a integridade dos dados e a lógica interna da classe, prevenindo usos indevidos ou alterações não autorizadas por partes do código externas à classe.

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- Na programação orientada a objetos em Python, os métodos são essenciais na definição de comportamentos das classes e, por extensão, dos objetos criados a partir dessas classes.
- Métodos estáticos
- Dentro deste contexto, existem diferentes tipos de métodos que servem a propósitos específicos:
- Métodos privados
- Métodos da classe

_4 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- O objetivo de um método privado é encapsular a lógica interna da classe, escondendo-a de outras classes ou do restante do código. Isto é útil quando queremos que certas operações sejam restritas ao uso interno da classe, prevenindo assim seu acesso ou alteração indevida. Em Python, métodos privados são usualmente indicados por um prefixo de sublinhado duplo (__) no início do nome.
- São aqueles que só podem ser acessados dentro da própria classe onde foram definidos.
- Métodos Privados

_4 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Métodos da Classe
- São métodos que não pertencem a uma instância específica da, mas a uma classe em si.
- Eles são marcados com o decorador @classmethod e devem receber como primeiro parâmetro uma referência à classe, convencionalmente nomeada cls.
- Esses métodos podem acessar e modificar o estado da classe, mas não o estado de instâncias individuais.

_5 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- Métodos Estáticos
- São similares aos métodos da classe, mas não recebem uma referência explícita nem à instância (self) nem à classe (cls).
- Eles funcionam de maneira similar a funções regulares definidas fora da classe, mas são colocados dentro da classe por conveniência ou organização lógica.
- Eles são definidos com o decorador @staticmethod e são úteis para realizar operações que, embora relacionadas à classe, não interagem diretamente com seus atributos ou outros métodos.

_4 imagem(ns) no slide._

### Slide 13 (oculto)

- DESENVOLVIMENTO DE SISTEMAS
- Exemplos
- Arquivos do projeto:

_4 imagem(ns) no slide._

> **Notas do apresentador:** Arquivo: https://github.com/alura-cursos/Curso-Python-3-Introdu-o-a-Orienta-o-a-objetos/archive/capitulo5.zip

### Slide 14

- DESENVOLVIMENTO DE SISTEMAS
- Atividade para a fixação do conteúdo estudado
- Qual a finalidade do método metodo_classe na classe Exemplo?
- (A) Modificar o valor de um atributo de instância
- (B) Acessar um atributo privado da instância
- (C) Realizar uma operação que depende do estado da classe
- (D) Somar um valor arbitrário ao atributo valor
- Escolhendo alguém para responder essa questão!

_4 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Qual a finalidade do método metodo_classe na classe Exemplo?
- (A) Modificar o valor de um atributo de instância
- (B) Acessar um atributo privado da instância
- (C) Realizar uma operação que depende do estado da classe
- (D) Somar um valor arbitrário ao atributo valor
- Resposta correta:
- (C) Realizar uma operação que depende do estado da classe

_3 imagem(ns) no slide._

> **Notas do apresentador:** O método metodo_classe é um exemplo de um método da classe, que opera com base no estado da classe (cls.valor) e não no estado de uma instância específica. Este método é útil para operações que são relevantes para a classe como um todo, como manipular ou acessar atributos estáticos.

### Slide 16

- DESENVOLVIMENTO DE SISTEMAS
- Conclusão
- Métodos privados e estáticos são essenciais para o encapsulamento e coesão do código, garantindo que operações internas sejam protegidas e que funções utilitárias estejam organizadas dentro da classe.
- https://hermes.dio.me/articles/cover/7b3b628e-7cf4-45e8-ab16-34e9c4a92d57.jpg

_4 imagem(ns) no slide._

### Slide 17

- DESENVOLVIMENTO DE SISTEMAS
- DESENVOLVIMENTO DE SISTEMAS
- Atividade Prática na Plataforma Alura
- Na plataforma Alura vamos acessar o seguinte curso:
- A recomendação é que você continue esse curso extraclasse, pois ele traz um conteúdo essencial para compreender sobre o referido tema.
- Link para o curso: https://cursos.alura.com.br/course/python-entendendo-orientacao-objetos

_8 imagem(ns) no slide._

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- Métodos privados
- 12 minutos
- Link para tarefa: https://cursos.alura.com.br/course/python-entendendo-orientacao-objetos/task/128389
- Métodos privados em Python são definidos com um duplo sublinhado (__) no início do nome. Eles são usados para encapsular a lógica interna da classe, protegendo-a de acessos externos indevidos e mantendo a integridade dos dados.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- Métodos da classe
- 9 minutos
- Link para tarefa: https://cursos.alura.com.br/course/python-entendendo-orientacao-objetos/task/128390
- Métodos de classe em Python são definidos com o decorador @classmethod e recebem a classe como primeiro argumento, nomeado por convenção como cls. São úteis para operações que pertencem à classe, não a uma instância específica, facilitando ações globais sobre a classe.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 20

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje:
- Reconhecemos a importância e aplicação de métodos privados e estáticos em Python.
- Aprendemos como eles contribuem para o encapsulamento de lógica interna e organização de funções que não dependem do estado da instância ou classe.
- https://hermes.dio.me/assets/articles/6a2e695a-6374-4be8-875f-479c252ef16a.png

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

_Fonte: AULA 22_ATIVIDADE_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

ATIVIDADE AULA 22

Questão 1

Qual método é utilizado para acessar dados que não devem ser expostos fora da classe?

a) Método público

b) Método estático

c) Método da classe

d) Método privado

Resposta correta: d)

Métodos privados, indicados por um sublinhado duplo antes do nome (__nomeMetodo), são usados para encapsular a lógica interna da classe, não sendo acessíveis fora dela. Eles protegem os dados e operações internas da classe de acessos externos não autorizados.

Questão 2

Para que serve um método estático em uma classe Python?

a) Para alterar atributos de instância

b) Para acessar e modificar atributos da classe

c) Para realizar operações que não dependem do estado da instância ou da classe

d) Para inicializar um novo objeto da classe

Resposta correta: c)

Métodos estáticos, definidos com o decorador @staticmethod, são utilizados para executar operações que não dependem do estado da instância (self) ou da classe (cls). Eles são como funções normais, mas pertencem ao namespace da classe.

## Outros documentos

_Fonte: AULA 22_SAIBA MAIS_ PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

SAIBA MAIS AULA 22

Exemplo prático:

class Calculadora:

@staticmethod

def somar(a, b):

return a + b

@classmethod

def criar_do_valor(cls, valor):

return cls(valor, valor) # Supondo que a classe tenha um construtor que aceite dois valores

def __init__(self, valor_a, valor_b):

self.a = valor_a

self.b = valor_b

def __metodo_privado(self):

# Método privado, apenas para uso interno

print("Este é um método privado.")

def operacao_interna(self):

self.__metodo_privado() # Chamada do método privado dentro da classe

Este exemplo ilustra a utilização de métodos estáticos, métodos da classe e métodos privados dentro de uma classe Calculadora. Cada um desses métodos serve a um propósito específico, demonstrando a flexibilidade e a organização que a programação orientada a objetos proporciona ao desenvolvimento de software em Python.
