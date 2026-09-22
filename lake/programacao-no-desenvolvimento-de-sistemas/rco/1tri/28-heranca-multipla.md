---
titulo: "Herança múltipla"
tipo: rco-seed
disciplina: programacao-no-desenvolvimento-de-sistemas
sigla_rco: PDS
trimestre: 1
ordem_rco: 28
serie: 3
aula_rco: "Aula 28"
slides: 25
tem_atividade: true
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PDS/1TRI/28-heranca-multipla/28-heranca-multipla.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PDS/1TRI/28-heranca-multipla/AULA 28_ATIVIDADE_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PDS/1TRI/28-heranca-multipla/AULA 28_SAIBA MAIS_ PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Herança múltipla

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO NO
- DESENVOLVIMENTO DE
- SISTEMAS
- 3ª SÉRIE
- Herança múltipla
- Aula 28

_3 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- DESENVOLVIMENTO DE SISTEMAS
- Na aula de hoje, vamos:
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store
- Investigar a complexidade e os benefícios da herança múltipla em Python.

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
- Demonstramos como o uso de Classes Abstratas em Python pode criar uma base sólida para nossos objetos, introduzindo a necessidade de métodos abstratos para garantir a implementação nas subclasses.

_4 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Fernando, um desenvolvedor iniciante, está tentando aplicar herança múltipla em um projeto de sistema escolar para gerenciar tanto os atributos de 'Pessoa' quanto os de 'Funcionário' em uma nova classe 'Professor'...

_4 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Como posso combinar estas duas classes sem conflito e aproveitar ao máximo as funcionalidades de ambas?
- Quem sabe responde!

_5 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Fernando deve utilizar a herança múltipla com cautela, garantindo que não haja métodos com o mesmo nome nas classes base, a menos que seja intencional.
- Ele pode definir claramente os métodos __init__ em sua nova classe para inicializar corretamente os atributos de ambas as classes bases.
- Usar Mixins pode ajudá-lo a agregar funcionalidades específicas sem complicar a hierarquia de herança.

_4 imagem(ns) no slide._

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- É um recurso de Programação Orientada a Objetos que permite que uma classe derive características e comportamentos de mais de uma Super-classe Este conceito é particularmente útil em linguagens como Python, onde a flexibilidade e reutilização de código são incentivadas.
- Herança múltipla

_4 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- Finalidade
- A principal finalidade da herança múltipla é permitir que os desenvolvedores criem novas classes que combinem e estendam o comportamento de múltiplas classes existentes.
- Isso evita a duplicação de código e promove uma maior modularidade no design de software.

_4 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Complexidade
- A herança múltipla pode introduzir complexidades, especialmente quando as classes-mães têm métodos com os mesmos nomes ou quando as cadeias de herança se tornam muito extensas.
- Para resolver essas questões, Python usa um método chamado C3 Linearization para definir claramente a ordem na qual os métodos são resolvidos se houver ambiguidade.

_5 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- Mixins
- São um tipo específico da herança múltipla, onde as classes são usadas para fornecer métodos que podem ser adicionados a outras classes através de herança.
- Mixins são geralmente pequenos e focados em uma funcionalidade específica, facilitando a reutilização de código sem forçar uma relação de pai e filho completa.

_4 imagem(ns) no slide._

### Slide 13 (oculto)

- DESENVOLVIMENTO DE SISTEMAS
- Exemplos
- Acesse o arquivo
- SAIBA MAIS!

_4 imagem(ns) no slide._

### Slide 14

- DESENVOLVIMENTO DE SISTEMAS
- Atividade para a fixação do conteúdo estudado
- Qual é o principal benefício da utilização de mixins em Python?
- (A) Permitir a execução de múltiplos programas simultaneamente.
- (B) Reduzir a necessidade de duplicação de código.
- (C) Incentivar o uso de herança múltipla para todos os objetos.
- (D) Aumentar a complexidade do código.
- Escolhendo alguém para responder essa questão!

_4 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Qual é o principal benefício da utilização de mixins em Python?
- (A) Permitir a execução de múltiplos programas simultaneamente.
- (B) Reduzir a necessidade de duplicação de código.
- (C) Incentivar o uso de herança múltipla para todos os objetos.
- (D) Aumentar a complexidade do código.
- Resposta correta: (B) Reduzir a necessidade de duplicação de código.

_3 imagem(ns) no slide._

> **Notas do apresentador:** Comentário: Mixins são úteis em Python para adicionar funcionalidades específicas a classes sem necessidade de criar uma cadeia de herança complexa. Eles permitem a reutilização de código de maneira modular e flexível, o que pode simplificar significativamente o design do software e manter o código mais organizado e fácil de manter.

### Slide 16

- DESENVOLVIMENTO DE SISTEMAS
- Concluindo
- A herança múltipla, quando usada corretamente, juntamente com Mixins, permite uma abordagem flexível e potente para a extensão de classes em Python, facilitando o reutilização do código, mantendo a modularidade.

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
- Mais de uma classe mãe
- 7 minutos
- Link para tarefa: https://cursos.alura.com.br/course/python-3-avancando-orientacao-objetos/task/41780
- Herança múltipla permite que uma classe em Python herde comportamentos e atributos de mais de uma Super-classe. Isso proporciona maior flexibilidade, mas requer cuidado para evitar conflitos e ambiguidades nos métodos herdados.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- Resolução de métodos
- 9 minutos
- Link para tarefa: https://cursos.alura.com.br/course/python-3-avancando-orientacao-objetos/task/41781
- A resolução de métodos em contextos de herança múltipla é gerida pelo algoritmo C3 Linearization em Python. Ele define uma ordem específica de busca para métodos, garantindo que cada classe pai seja considerada uma única vez de forma consistente.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 20

- DESENVOLVIMENTO DE SISTEMAS
- Mixins
- 7 minutos
- Link para tarefa: https://cursos.alura.com.br/course/python-3-avancando-orientacao-objetos/task/41782
- Mixins são classes que fornecem métodos para serem reutilizados por outras classes, sem a necessidade de herança tradicional. Eles permitem a composição de comportamentos e propriedades em múltiplas classes, aumentando a modularidade e flexibilidade do código.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 21

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje:
- Investigamos como a herança múltipla funciona em Python e como resolvemos problemas de resolução de métodos usando a ordem de classes na herança.
- Demonstramos como o uso de Mixins pode adicionar funcionalidades sem complicar a hierarquia de classes.

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

_Fonte: AULA 28_ATIVIDADE_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

ATIVIDADE AULA 28

Questão 1

Em Python, como é chamado o conflito que pode surgir com a herança múltipla quando dois métodos têm o mesmo nome?

a) Método duplicado

b) Problema de resolução de métodos

c) Conflito de nomeação

d) Diamond problem

Resposta correta: d) Diamond problem

Comentário:

O "Diamond problem" ocorre quando uma classe herda de duas classes que possuem o mesmo método. Isso pode causar ambiguidade sobre qual método deve ser executado, algo que Python resolve usando a ordem em que as classes são listadas na declaração de herança.

Questão 2

Qual é o principal uso dos Mixins em Python?

a) Substituir completamente a herança tradicional

b) Prover um conjunto de métodos que pode ser usado por diversas classes

c) Encapsular todos os atributos em métodos privados

d) Gerar exceções específicas para métodos conflitantes

Resposta correta: b) Prover um conjunto de métodos que pode ser usado por diversas classes

Comentário:

Mixins são usados para fornecer métodos reutilizáveis que podem ser incluídos em outras classes sem recorrer à herança tradicional, facilitando a manutenção do código e aumentando a modularidade.

## Outros documentos

_Fonte: AULA 28_SAIBA MAIS_ PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

SAIBA MAIS AULA 23

Exemplo prático:

class Document:

def show(self):

return "Showing document base"

class PrintableMixin:

def print(self):

return "Print document"

class EditableMixin:

def edit(self):

return "Edit document"

class PdfDocument(Document, PrintableMixin, EditableMixin):

pass

pdf = PdfDocument()

print(pdf.show()) # Usa método de Document

print(pdf.print()) # Usa método de PrintableMixin

print(pdf.edit()) # Usa método de EditableMixin

Neste exemplo, PdfDocument é capaz de herdar funcionalidades de uma classe base Document e dois mixins: PrintableMixin e EditableMixin. Cada mixin adiciona um comportamento específico, o que é uma maneira eficiente de compor classes com funcionalidades customizadas sem criar uma cadeia de herança complexa.
