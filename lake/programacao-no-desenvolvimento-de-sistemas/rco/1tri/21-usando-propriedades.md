---
titulo: "Usando Propriedades"
tipo: rco-seed
disciplina: programacao-no-desenvolvimento-de-sistemas
sigla_rco: PDS
trimestre: 1
ordem_rco: 21
serie: 3
aula_rco: "Aula 21"
slides: 25
tem_atividade: true
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/1TRI/21-usando-propriedades/21-usando-propriedades.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/1TRI/21-usando-propriedades/AULA 21_ATIVIDADE_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/1TRI/21-usando-propriedades/AULA 21_SAIBA MAIS_ PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Usando Propriedades

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO NO
- DESENVOLVIMENTO DE
- SISTEMAS
- 3ª SÉRIE
- Usando Propriedades
- Aula 21

_3 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- DESENVOLVIMENTO DE SISTEMAS
- Na aula de hoje, vamos:
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store
- Abordar o uso de propriedades, getters e setters em Python, mostrando como encapsular dados e controlar o acesso e modificação de atributos de uma maneira mais segura e organizada.

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
- Trabalhamos o conceito de encapsulamento, destacando a importância de atributos privados e métodos para a manutenção e segurança do código, integrando a coesão como elemento aprimorador da organização das classes.

_4 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Rodrigo é um desenvolvedor iniciante trabalhando em um projeto Python e se depara com a necessidade de controlar o acesso a certos atributos de suas classes.
- Ele pesquisa sobre getters e setters, mas ainda está confuso sobre como e quando usá-los corretamente…
- Ele precisa garantir que certos dados não sejam alterados diretamente, mas não sabe como implementar essa restrição de maneira eficiente.

_5 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Quem sabe responde!
- Qual é a principal vantagem de usar propriedades com getters e setters em Python, em vez de acessar os atributos diretamente?
- Qual?
- Qual?
- Qual?
- Qual?
- Qual?
- Qual?
- Qual?
- Qual?

_5 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Com getters e setters, podemos implementar validações e lógicas específicas antes de atribuir ou retornar valores, garantindo a integridade dos dados e encapsulando a lógica de negócio de forma mais eficaz.
- A principal vantagem é o controle sobre
- o acesso e a modificação dos dados!

_4 imagem(ns) no slide._

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- Isso permite que Rodrigo proteja os atributos de sua classe contra modificações indevidas e garanta que somente valores válidos sejam atribuídos, prevenindo erros e comportamentos inesperados no programa.

_10 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- Na programação orientada a objetos, especialmente em Python, é comum o uso de propriedades, getters e setters para controlar o acesso e a modificação de atributos de uma classe.
- Essa abordagem permite o encapsulamento, um dos pilares da programação orientada a objetos, escondendo os detalhes internos de uma classe e expondo apenas o necessário para o uso externo.

_4 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Propriedades
- Propriedades são usadas para adicionar lógica adicional ao acessar (get) ou modificar (set) um atributo.
- O Python oferece uma maneira elegante de definir propriedades usando o decorador @property para getters e @atributo.setter para setters.

_4 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- Getters
- São métodos usados para obter o valor de um atributo.
- O uso de um getter permite que você adicione lógica adicional durante o acesso ao valor, como validações ou conversões.

_9 imagem(ns) no slide._

### Slide 13

- DESENVOLVIMENTO DE SISTEMAS
- Setters
- São métodos usados para definir o valor de um atributo. Com setters, você pode realizar verificações ou transformações no valor antes de atribuí-lo ao atributo.

_4 imagem(ns) no slide._

### Slide 14 (oculto)

- DESENVOLVIMENTO DE SISTEMAS
- Exemplos
- Arquivos do projeto:

_5 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- Atividade para a fixação do conteúdo estudado
- Qual será o resultado se tentarmos definir o raio de um objeto círculo como um valor negativo?
- (A) O raio será definido como o valor negativo.
- (B) O raio permanecerá inalterado.
- (C) Será gerada uma exceção ValueError.
- (D) O raio será automaticamente convertido para positivo.
- Escolhendo alguém para responder essa questão!

_4 imagem(ns) no slide._

### Slide 16

- DESENVOLVIMENTO DE SISTEMAS
- RESPOSTA
- Qual será o resultado se tentarmos definir o raio de um objeto círculo como um valor negativo?
- (A) O raio será definido como o valor negativo.
- (B) O raio permanecerá inalterado.
- (C) Será gerada uma exceção ValueError.
- (D) O raio será automaticamente convertido para positivo.
- Resposta Correta: (C) Será gerada uma exceção ValueError.

_3 imagem(ns) no slide._

> **Notas do apresentador:** Comentário sobre a resposta: Ao tentar definir o raio com um valor negativo, o setter raio é chamado, e a condição dentro deste método levanta uma exceção ValueError, impedindo que o valor negativo seja atribuído ao raio. Isso demonstra a utilidade dos setters para validar dados antes de modificá-los, mantendo a integridade dos atributos da classe.

### Slide 17

- DESENVOLVIMENTO DE SISTEMAS
- Conclusão
- Usar propriedades com getters e setters em Python facilita o controle e a validação de acesso aos dados, garantindo a encapsulação e a segurança dos atributos da classe.

_4 imagem(ns) no slide._

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- Atividade Prática na Plataforma Alura
- Na plataforma Alura vamos acessar o seguinte curso:
- A recomendação é que você continue esse curso extraclasse, pois ele traz um conteúdo essencial para compreender sobre o referido tema.
- Link para o curso: https://cursos.alura.com.br/course/python-entendendo-orientacao-objetos

_5 imagem(ns) no slide._

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- Getters e Setters
- 10 minutos
- Link para tarefa: https://cursos.alura.com.br/course/python-entendendo-orientacao-objetos/task/128387
- Getters e setters são métodos que permitem acessar e modificar atributos privados de uma classe de maneira controlada. Getters retornam o valor do atributo, enquanto setters permitem alterá-lo, podendo incluir validações para garantir a integridade dos dados.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 20

- DESENVOLVIMENTO DE SISTEMAS
- Propriedades
- 16 minutos
- Link para tarefa: https://cursos.alura.com.br/course/python-entendendo-orientacao-objetos/task/128388
- Propriedades em Python oferecem uma forma elegante de acessar e modificar atributos de uma classe, combinando getters e setters. Utilizam-se decoradores para criar propriedades, facilitando a leitura e manutenção do código ao encapsular lógicas de acesso e validação dos atributos.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 21

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje
- Exploramos como getters, setters e as propriedades permitem um controle mais refinado sobre o acesso e a modificação de atributos em Python, garantindo práticas seguras de programação orientada a objetos.

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

_Fonte: AULA 21_ATIVIDADE_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

ATIVIDADE AULA 21

Questão 1

Qual é a principal vantagem de usar getters e setters em uma classe Python?

a) Aumentar a velocidade do código.

b) Permitir acesso direto aos atributos.

c) Facilitar a cópia de objetos.

d) Controlar o acesso e a validação dos dados.

Resposta Correta: d) Controlar o acesso e a validação dos dados.

Comentário:

Getters e Setters são usados para controlar o acesso aos atributos de uma classe. Eles permitem validar dados antes de modificá-los e podem fornecer uma interface segura para a manipulação de atributos privados.

Questão 2

O que acontece se você tentar acessar diretamente um atributo privado fora da sua classe em Python?

a) O atributo é deletado automaticamente.

b) Uma exceção é levantada.

c) O valor do atributo é retornado sem problemas.

d) O atributo é convertido para público automaticamente.

Resposta Correta: b) Uma exceção é levantada.

Comentário:

Acessar diretamente um atributo privado (indicado por um sublinhado duplo __ no início do nome) fora da sua classe em Python normalmente resulta em um erro, pois o nome do atributo é alterado internamente para incluir o nome da classe, um mecanismo conhecido como name mangling.

## Outros documentos

_Fonte: AULA 21_SAIBA MAIS_ PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

SAIBA MAIS AULA 21

Exemplo prático:

class Pessoa:

def __init__(self, nome):

self._nome = nome # Atributo privado

@property

def nome(self):

return self._nome

@nome.setter

def nome(self, valor):

if isinstance(valor, str) and len(valor) > 0:

self._nome = valor

else:

raise ValueError("Nome deve ser uma string não vazia")

pessoa = Pessoa("João")

print(pessoa.nome) # Acessa usando o getter

pessoa.nome = "Ana" # Modifica usando o setter

print(pessoa.nome) # Novamente acessa usando o getter

Neste exemplo, a classe Pessoa tem um atributo _nome, que é privado (indicado pelo underscore _). Usamos um getter para retornar o valor do nome e um setter para validar o novo valor antes de modificá-lo. Isso garante que apenas nomes válidos sejam atribuídos ao _nome, encapsulando a lógica de validação dentro da classe.
