---
titulo: "Encapsulamento em python"
tipo: rco-seed
disciplina: programacao-no-desenvolvimento-de-sistemas
sigla_rco: PDS
trimestre: 1
ordem_rco: 20
serie: 3
aula_rco: "Aula 20"
slides: 26
tem_atividade: true
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/1TRI/20-encapsulamento-em-python/20-encapsulamento-em-python.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/1TRI/20-encapsulamento-em-python/AULA 20_ATIVIDADE_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Encapsulamento em python

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO NO
- DESENVOLVIMENTO DE
- SISTEMAS
- 3ª SÉRIE
- Encapsulamento em python
- Aula 20

_3 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- DESENVOLVIMENTO DE SISTEMAS
- Na aula de hoje, vamos:
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store
- Reconhecer como o encapsulamento protege os dados dentro de uma classe, utilizando atributos privados para controle.

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
- Listamos métodos em Python, definindo comportamentos dentro de classes e a importância do coletor de lixo e do valor None.

_4 imagem(ns) no slide._

### Slide 6

- Para pensarmos juntos!
- Pedro, um desenvolvedor iniciante, enfrenta o desafio de proteger os dados de suas classes de acesso e modificação externos.
- DESENVOLVIMENTO DE SISTEMAS
- Ele se pergunta:
- "Como posso garantir que somente métodos internos da classe manipulem certos atributos?"

_4 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Qual é a melhor prática que Pedro pode adotar para proteger os dados de sua classe de acessos indevidos?
- Quem sabe responde!

_6 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Prefixando-os com dois sublinhados __, e criando métodos públicos para acessá-los e modificá-los de forma controlada.
- Pedro deve utilizar o encapsulamento, definindo atributos como privados!

_4 imagem(ns) no slide._

> **Notas do apresentador:** Comentário: Ao tornar atributos privados e oferecer métodos para sua manipulação, Pedro não apenas protege os dados de sua classe, mas também garante que qualquer interação com esses dados siga as regras que ele definiu, mantendo a integridade e a consistência do estado do objeto.

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- Encapsulamento
- Essa técnica protege os dados contra acessos ou modificações indevidas e contribui para a modularidade e manutenção do código, pois o funcionamento interno de uma classe fica oculto para o restante do programa.
- É um dos pilares fundamentais da Programação Orientada a Objetos (POO), que visa restringir o acesso direto aos dados de um objeto e permitir sua manipulação apenas através de métodos específicos.

_4 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- Atributos privados
- Os atributos privados em Python são definidos prefixando o nome com dois sublinhados (ex: __atributo).
- Isso sinaliza ao Python que esses atributos não devem ser acessados diretamente de fora da classe, mas sim através de métodos públicos (getters e setters), que são interfaces para consulta e alteração desses dados.
- Vale ressaltar que, diferentemente de outras linguagens, o Python não impõe restrições de acesso fortes; trata-se mais de uma convenção.

_5 imagem(ns) no slide._

### Slide 11

- Coesão
- O encapsulamento ajuda na coesão, que é a medida de quão relacionadas e focadas estão as responsabilidades de uma classe.
- Uma classe coesa tem um propósito bem definido, onde seus métodos e atributos estão diretamente relacionados a esse propósito, facilitando assim a compreensão, a manutenção e a expansão do código.
- DESENVOLVIMENTO DE SISTEMAS

_4 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- class ContaBancaria:
- def __init__(self, saldo_inicial):
- self.__saldo = saldo_inicial
- def depositar(self, valor):
- if valor > 0:
- self.__saldo += valor
- return True
- return False

_5 imagem(ns) no slide._

### Slide 13

- DESENVOLVIMENTO DE SISTEMAS
- def sacar(self, valor):
- if 0 < valor <= self.__saldo:
- self.__saldo -= valor
- return True
- return False
- def consultar_saldo(self):
- return self.__saldo

_4 imagem(ns) no slide._

> **Notas do apresentador:** No exemplo acima, o saldo da conta bancária é um atributo privado (__saldo), garantindo que ele só possa ser modificado pelos métodos depositar e sacar, e consultado pelo método consultar_saldo. Isso ilustra o encapsulamento, protegendo o saldo contra manipulações diretas e errôneas, e mantém a classe coesa ao redor da gestão do saldo.

### Slide 14 (oculto)

- DESENVOLVIMENTO DE SISTEMAS
- Exemplos
- Arquivos do projeto:

_4 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- Atividade para a fixação do conteúdo estudado
- Qual das seguintes opções melhor descreve o motivo para usar atributos privados em uma classe em Python?
- (A) Para aumentar a velocidade do programa.
- (B) Para permitir acesso irrestrito aos atributos.
- (C) Para proteger os atributos de modificações externas não autorizadas.
- (D) Para utilizar menos memória.
- Escolhendo alguém para responder essa questão!

_4 imagem(ns) no slide._

### Slide 16

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Qual das seguintes opções melhor descreve o motivo para usar atributos privados em uma classe em Python?
- (A) Para aumentar a velocidade do programa.
- (B) Para permitir acesso irrestrito aos atributos.
- (C) Para proteger os atributos de modificações externas não autorizadas.
- (D) Para utilizar menos memória.
- Resposta Correta:
- (C) Para proteger os atributos de modificações externas não autorizadas.

_3 imagem(ns) no slide._

> **Notas do apresentador:** Comentário sobre a resposta: Atributos privados são usados para encapsular os dados dentro de uma classe, protegendo-os contra acessos e modificações diretas de fora da classe. Isso ajuda a manter a integridade dos dados e facilita a manutenção do código.

### Slide 17

- DESENVOLVIMENTO DE SISTEMAS
- Conclusão
- Encapsulamento em Python é essencial para a segurança dos dados, permitindo que classes gerenciem seus próprios dados e exponham apenas métodos necessários externamente, aumentando a coesão e a manutenção do código.

_5 imagem(ns) no slide._

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- Atividade Prática na Plataforma Alura
- Na plataforma Alura vamos acessar o seguinte curso:
- A recomendação é que você continue esse curso extraclasse, pois ele traz um conteúdo essencial para compreender sobre o referido tema.
- Link para o curso: https://cursos.alura.com.br/course/python-entendendo-orientacao-objetos

_5 imagem(ns) no slide._

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- Atributos privados
- 10 minutos
- Link para tarefa: https://cursos.alura.com.br/course/python-entendendo-orientacao-objetos/task/128384
- Para garantir encapsulamento em Python, os atributos privados são definidos com dois sublinhados iniciais (__), como __atributo_privado. Isso impede o acesso direto de fora da classe, promovendo a segurança e a integridade dos dados internos.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 20

- DESENVOLVIMENTO DE SISTEMAS
- Encapsulamento
- 12 minutos
- Link para tarefa: https://cursos.alura.com.br/course/python-entendendo-orientacao-objetos/task/128385
- A encapsulação é um dos pilares da programação orientada a objetos, permitindo que detalhes de implementação de uma classe sejam ocultados, expondo apenas o necessário para o uso externo.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 21

- DESENVOLVIMENTO DE SISTEMAS
- Coesão
- 5 minutos
- Link para tarefa: https://cursos.alura.com.br/course/python-entendendo-orientacao-objetos/task/128386
- A coesão refere-se ao princípio de design de software que assegura que uma classe seja responsável por uma única funcionalidade ou conceito, aumentando a modularidade e a facilidade de manutenção do código.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 22

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje:
- Exploramos o encapsulamento, atributos privados, e a importância da coesão em Python.
- Aprendemos como proteger dados dentro de classes, utilizando atributos privados e expondo funcionalidades através de métodos públicos.

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

_Fonte: AULA 20_ATIVIDADE_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

ATIVIDADE AULA 20

Questão 1

Qual a principal razão para utilizar encapsulamento em Python?

a) Tornar o código mais rápido.

b) Permitir que todos os atributos sejam públicos.

c) Proteger a parte interna da classe, escondendo seus detalhes de implementação.

d) Facilitar o acesso direto aos dados por outras classes.

Resposta Correta: c) Proteger a parte interna da classe, escondendo seus detalhes de implementação.

Comentário: Encapsulamento é uma técnica fundamental na programação orientada a objetos que ajuda a esconder os detalhes internos de como uma classe funciona, permitindo expor apenas o necessário para o uso externo, mantendo a integridade e segurança dos dados internos.

Questão 2

Como são declarados os atributos privados em uma classe Python para garantir o encapsulamento?

a) Utilizando o prefixo __ antes do nome do atributo.

b) Declarando os atributos fora dos métodos.

c) Usando a palavra-chave "private" antes do nome do atributo.

d) Nomeando os atributos com letras maiúsculas.

Resposta Correta: a) Utilizando o prefixo __ antes do nome do atributo.

Comentário: Em Python, atributos privados são declarados com um duplo sublinhado (__) antes do nome do atributo. Isso os torna inacessíveis fora da classe, exceto por métodos internos da classe, fortalecendo o encapsulamento.
