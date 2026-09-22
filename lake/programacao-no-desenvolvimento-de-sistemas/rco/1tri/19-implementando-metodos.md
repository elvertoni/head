---
titulo: "Implementando Métodos"
tipo: rco-seed
disciplina: programacao-no-desenvolvimento-de-sistemas
sigla_rco: PDS
trimestre: 1
ordem_rco: 19
serie: 3
aula_rco: "Aula 19"
slides: 27
tem_atividade: true
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/1TRI/19-implementando-metodos/19-implementando-metodos.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PDS/1TRI/19-implementando-metodos/AULA 19_ATIVIDADE_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/1TRI/19-implementando-metodos/AULA 19_SAIBA MAIS_ PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Implementando Métodos

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO NO
- DESENVOLVIMENTO DE
- SISTEMAS
- 3ª SÉRIE
- Implementando Métodos
- Aula 19

_3 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- DESENVOLVIMENTO DE SISTEMAS
- Na aula de hoje vamos:
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store
- Implementar e utilizar métodos em classes Python, além de entender o papel do valor None e como o coletor de lixo otimiza a gestão de memória.

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
- Relacionamos as classes, objetos e construtores em Python, focando na criação de instâncias e na inicialização de atributos.

_4 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- João, um desenvolvedor júnior, está criando uma aplicação em Python e se depara com a necessidade de adicionar funcionalidades específicas aos seus objetos.
- Ele sabe que precisa implementar métodos, mas não tem certeza de como proceder ou de como o coletor de lixo do Python gerencia a memória.

_5 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- "Como posso adicionar comportamentos aos meus objetos e garantir uma boa gestão de memória?"
- Quem sabe responde!
- João pergunta…

_10 imagem(ns) no slide._

### Slide 8

- Resposta
- Métodos são funções que pertencem a uma classe e operam com seus atributos.
- DESENVOLVIMENTO DE SISTEMAS
- João pode definir métodos dentro de suas classes para adicionar comportamentos aos objetos.
- O Python possui um coletor de lixo que automaticamente libera a memória alocada para objetos que não são mais necessários, usando contagem de referência e detecção de ciclos para identificar e coletar objetos não alcançáveis.

_4 imagem(ns) no slide._

> **Notas do apresentador:** Comentário: Implementar métodos permite que João adicione funcionalidades específicas aos seus objetos, tornando seu código mais organizado e modular. Quanto à gestão de memória, ele não precisa se preocupar excessivamente com a liberação de memória para objetos inutilizados, pois o coletor de lixo do Python cuida desse processo, permitindo que ele foque mais na lógica da aplicação.

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- Introdução
- Na programação orientada a objetos em Python, os métodos são funções definidas dentro de uma classe que descrevem os comportamentos dos objetos criados a partir dessa classe.
- Eles são essenciais para interagir com os atributos dos objetos, permitindo não apenas recuperar ou modificar os dados, mas também executar qualquer operação relevante ao contexto do objeto.

_4 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- Implementação de Métodos
- A implementação de métodos segue a sintaxe básica de definição de funções em Python, com a diferença de que o primeiro parâmetro de um método é sempre 'self', que é uma referência ao objeto que chama o método.
- Essa característica permite que o método acesse e manipule os atributos e outros métodos do objeto.

_4 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Exemplo
- Considerando uma classe 'ContaBancaria', um método 'depositar' pode aumentar o saldo da conta, enquanto um método 'sacar' diminuiria esse saldo.
- Ambos os métodos trabalham modificando o atributo 'saldo' do objeto 'ContaBancaria' que os invocou.
- O código está no próximo slide

_6 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- class ContaBancaria:
- def __init__(self, saldo=0):
- self.saldo = saldo
- def depositar(self, valor):
- self.saldo += valor
- def sacar(self, valor):
- if self.saldo >= valor:
- self.saldo -= valor
- else:
- print("Saldo insuficiente")

_4 imagem(ns) no slide._

### Slide 13

- DESENVOLVIMENTO DE SISTEMAS
- O valor 'None' em Python é usado para representar a ausência de valor.
- Em contextos de métodos e gestão de memória, 'None' pode ser usado para desvincular referências a objetos, facilitando o trabalho do coletor de lixo.
- É frequentemente utilizado como valor padrão para parâmetros que podem não receber um argumento ou para indicar que uma variável ou objeto está "vazio".

_4 imagem(ns) no slide._

### Slide 14

- DESENVOLVIMENTO DE SISTEMAS
- O coletor de lixo em Python é uma funcionalidade que permite a recuperação automática de memória.
- Ele detecta objetos que não são mais acessíveis ou necessários no programa e libera a memória por eles ocupada.
- Isso é particularmente útil em uma linguagem de alto nível como Python, onde o gerenciamento de memória é abstraído do desenvolvedor.

_4 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- O coletor trabalha principalmente através da contagem de referências, eliminando objetos que não têm mais referências apontando para eles, além de detectar e resolver referências cíclicas que não seriam coletadas apenas pela contagem de referências.

_5 imagem(ns) no slide._

### Slide 16 (oculto)

- DESENVOLVIMENTO DE SISTEMAS
- Exemplos
- Acesse os arquivos do projeto!

_4 imagem(ns) no slide._

> **Notas do apresentador:** Acesse os arquivos do projeto! https://github.com/alura-cursos/Curso-Python-3-Introdu-o-a-Orienta-o-a-objetos/archive/capitulo2.zip

### Slide 17

- DESENVOLVIMENTO DE SISTEMAS
- Atividade para a fixação do conteúdo estudado
- Qual método especial em Python é utilizado para inicializar um objeto?
- (A) __start__()
- (B) __init__()
- (C) __begin__()
- (D) __create__()
- Escolhendo alguém para responder essa questão!

_4 imagem(ns) no slide._

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- Atividade para a fixação do conteúdo estudado
- Qual método especial em Python é utilizado para inicializar um objeto?
- (A) __start__()
- (B) __init__()
- (C) __begin__()
- (D) __create__()
- Resposta correta: (B) __init__()

_3 imagem(ns) no slide._

> **Notas do apresentador:** O método __init__() é chamado automaticamente ao criar um objeto. Ele é usado para inicializar os atributos do objeto, estabelecendo o estado inicial. No exemplo da lâmpada, __init__ define se a lâmpada começa ligada ou desligada.

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- Conclusão
- A implementação e uso de métodos em classes Python, juntamente com a compreensão de conceitos como None e a atuação do coletor de lixo, são fundamentais para a gestão eficaz de memória e a criação de códigos limpos e eficientes.

_4 imagem(ns) no slide._

### Slide 20

- DESENVOLVIMENTO DE SISTEMAS
- Atividade Prática na Plataforma Alura
- Na plataforma Alura vamos acessar o seguinte curso:
- A recomendação é que você continue esse curso extraclasse, pois ele traz um conteúdo essencial para compreender sobre o referido tema.
- Link para o curso: https://cursos.alura.com.br/course/python-entendendo-orientacao-objetos

_5 imagem(ns) no slide._

### Slide 21

- DESENVOLVIMENTO DE SISTEMAS
- Usando métodos
- 14 minutos
- Link para tarefa: https://cursos.alura.com.br/course/python-entendendo-orientacao-objetos/task/128381
- Métodos são funções definidas dentro de uma classe e são usados para manipular os dados dos objetos dessa classe. Para usar um método, você primeiro precisa criar uma instância da classe (um objeto) e então chamar o método usando a notação de ponto, por exemplo: objeto.metodo().
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 22

- DESENVOLVIMENTO DE SISTEMAS
- None e Coletor de lixo
- 8 minutos
- Link para tarefa: https://cursos.alura.com.br/course/python-entendendo-orientacao-objetos/task/128383
- None é usado em Python para representar a ausência de valor. Funciona como um marcador de lugar para variáveis que não foram atribuídas a um valor específico. O coletor de lixo de Python gerencia automaticamente a memória, liberando espaço ao detectar objetos sem referências, prevenindo vazamentos de memória.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 23

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje:
- Exploramos como implementar e utilizar métodos em classes Python, entendemos o valor None para representar a ausência de valor e discutimos o papel do coletor de lixo na gestão automática de memória.

_4 imagem(ns) no slide._

### Slide 24

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

### Slide 25

- DESENVOLVIMENTO DE SISTEMAS
- Referências (Imagens)
- Figuras e Imagens:
- https://www.flaticon.com/br
- https://www.istockphoto.com/br
- https://raw.githubusercontent.com/zbtang/React-Native-ViewPager/HEAD/imgs/dotIndicator.gif
- https://storyset.com

_3 imagem(ns) no slide._

### Slide 26

- DESENVOLVIMENTO DE SISTEMAS
- O RCO+Aulas é um projeto da Secretaria de Estado da Educação do Paraná e está em constante revisão. Todos os slides são de uso exclusivo dos professores da Rede Pública de Ensino, com a finalidade específica de aplicação em sala de aula, sendo totalmente vedada a publicização, reutilização, reprodução total ou parcial para quaisquer outros fins.

_4 imagem(ns) no slide._

### Slide 27

- DESENVOLVIMENTO DE SISTEMAS
- Esta publicação tem a cooperação entre a UNESCO e a Secretaria de Estado da Educação e do Esporte do Paraná no âmbito da parceria PRODOC 914BRZ1091, cujo objetivo é trazer soluções inovadoras de gestão da rede pública estadual de educação do Paraná para a melhoria da aprendizagem dos alunos. As indicações de nomes e a apresentação do material ao longo desta publicação não implicam a manifestação de qualquer opinião por parte da UNESCO a respeito da condição jurídica de qualquer país, território, cidade, região ou de suas autoridades, tampouco da delimitação de suas fronteiras ou limites As ideias e opiniões expressas nesta publicação são as dos autores e não refletem obrigatoriamente as da UNESCO nem comprometem a Organização.
- Cooperação Técnica

_4 imagem(ns) no slide._

## Atividade

_Fonte: AULA 19_ATIVIDADE_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

ATIVIDADE AULA 19

Questão 1

Qual das seguintes opções é verdadeira sobre o uso do método None em Python?

a) É usado para definir constantes.

b) Representa um valor numérico zero.

c) É utilizado para indicar a ausência de valor.

d) Define uma nova classe.

Resposta correta: c) É utilizado para indicar a ausência de valor.

Comentário sobre a resposta correta: None é um valor especial em Python que representa a ausência de valor ou a nulidade. Ele é frequentemente usado para inicializar variáveis ou indicar que uma variável ou retorno de método não tem nenhum valor útil associado.

Questão 2

Como o Python realiza a gestão de memória para objetos não mais necessários?

a) Usando uma função especial de limpeza manual.

b) Através do método __del__.

c) Utilizando um contador de referências.

d) Com o coletor de lixo automático.

Resposta correta: d) Com o coletor de lixo automático.

Comentário sobre a resposta correta: Python possui um coletor de lixo automático que gerencia a liberação de memória para objetos que não têm mais referências apontando para eles, ajudando a prevenir vazamentos de memória.

## Outros documentos

_Fonte: AULA 19_SAIBA MAIS_ PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

SAIBA MAIS AULA 19

Exemplo prático:

class ContaBancaria:

def __init__(self, saldo=0):

self.saldo = saldo

def depositar(self, valor):

self.saldo += valor

def sacar(self, valor):

if self.saldo >= valor:

self.saldo -= valor

else:

print("Saldo insuficiente")
