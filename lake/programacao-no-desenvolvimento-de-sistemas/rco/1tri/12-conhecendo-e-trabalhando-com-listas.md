---
titulo: "com listas"
tipo: rco-seed
disciplina: programacao-no-desenvolvimento-de-sistemas
sigla_rco: PDS
trimestre: 1
ordem_rco: 12
serie: 3
aula_rco: "Aula 12"
slides: 25
tem_atividade: true
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/1TRI/12-conhecendo-e-trabalhando-com-listas/12-conhecendo-e-trabalhando-com-listas.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/1TRI/12-conhecendo-e-trabalhando-com-listas/AULA 12_ATIVIDADE_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# com listas

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO NO
- DESENVOLVIMENTO DE
- SISTEMAS
- 3ª SÉRIE
- Conhecendo e trabalhando
- com listas
- Aula 12

_3 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- DESENVOLVIMENTO DE SISTEMAS
- Na aula de hoje vamos:
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store
- Aprender como as listas em Python podem ser usadas para armazenar e manipular dados.

_7 imagem(ns) no slide._

### Slide 4

- DESENVOLVIMENTO DE SISTEMAS
- ATENÇÃO PROFESSOR!
- O Material aqui apresentado, segue a análise do plano de curso contemplando os componentes curriculares e seus objetos de conhecimento, sendo assim, você tem liberdade para customizar o material conforme seu contexto para maior aproveitamento do conteúdo. Em caso de falta ou indisponibilidade de acesso à internet no local de aula, você poderá utilizar os seguintes artigos para criação de material complementar para auxiliar na aula:
- Leitura/Recursos Adicionais:
- Leitura Sugerida: "Python Crash Course" por Eric Matthes, um capítulo dedicado a listas e estruturas de dados.
- IDE Online: PythonAnywhere (pythonanywhere.com) ou Repl.it (replit.com), ambas plataformas suportam Python e são ideais para testar e compartilhar seus códigos.

_5 imagem(ns) no slide._

### Slide 5

- DESENVOLVIMENTO DE SISTEMAS
- Na aula anterior…
- Foi apresentado a manipulação de strings e métodos para encontrar letras dentro de uma palavra, preparando os alunos para entender como armazenar e verificar palpites em um jogo da forca.

_4 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Ela se pergunta: "Como posso usar listas para monitorar quais letras foram corretamente adivinhadas e ainda manter a estrutura da palavra secreta intacta?"
- Isabele, uma desenvolvedora iniciante, está criando seu primeiro jogo da forca em Python!
- Ela entende a lógica básica do jogo, mas está confusa sobre como usar listas para guardar as letras que o jogador já acertou.

_4 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Como Isabele pode organizar as letras acertadas em uma lista de forma que ela possa facilmente verificar o progresso do jogador?
- Registre a sua resposta e compartilhe!

_5 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Quando o jogador acertar uma letra, ela atualizará a lista substituindo o underscore pela letra correta na posição correspondente.
- Isabele pode iniciar uma lista com espaços representados por underscores ("_") para cada letra da palavra secreta.

_4 imagem(ns) no slide._

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Por exemplo, para a palavra "python", a lista inicial seria
- ['_', '_', '_', '_', '_', '_'].
- Se o jogador adivinhar "p", a lista é atualizada para ['p', '_', '_', '_', '_', '_'].
- Este método é eficaz e intuitivo, permitindo que tanto o programador quanto o jogador acompanhem facilmente o progresso do jogo

_4 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- Introdução
- Listas em Python são uma das estruturas de dados
- mais versáteis e utilizadas.
- Isso é especialmente útil em aplicações onde a coleção de itens precisa ser dinâmica, como adicionar, remover ou modificar os itens armazenados.
- Elas permitem armazenar
- uma coleção de itens em
- uma única variável. Listas
- são mutáveis, o que
- significa que seus
- elementos podem ser
- alterados após a lista ser criada.

_4 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Introdução
- Para criar uma lista, utilizamos colchetes [], e para adicionar elementos a ela, podemos usar o método .append().
- Por exemplo, se estamos construindo um jogo da forca, podemos usar uma lista para guardar as letras que o jogador acertou:

_5 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- Exemplo
- Além de adicionar elementos, as listas permitem a remoção com o método .remove(), a ordenação com .sort(), e muitas outras operações. Para acessar um elemento específico, basta referenciar seu índice, lembrando que em Python os índices começam em 0.
- letras_acertadas = []
- letras_acertadas.append('a’)
- letras_acertadas.append('b’)
- print(letras_acertadas) # Saída: ['a', 'b’]

_4 imagem(ns) no slide._

### Slide 13

- DESENVOLVIMENTO DE SISTEMAS
- Fundamentação
- Um aspecto fundamental das listas é a possibilidade de iterar sobre seus elementos.
- Isso pode ser feito através de um loop for, permitindo, por exemplo, verificar se uma letra escolhida pelo jogador está na palavra secreta:

_3 imagem(ns) no slide._

### Slide 14

- DESENVOLVIMENTO DE SISTEMAS
- Fundamentação
- palavra_secreta = "gato“
- tentativa = input("Digite uma letra: ")
- if tentativa in palavra_secreta:
- letras_acertadas.append(tentativa)
- Essa flexibilidade faz das listas uma ferramenta essencial para programadores, especialmente na manipulação de dados e no desenvolvimento de jogos e outras aplicações interativas.

_3 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- Atividade para a fixação do conteúdo estudado
- Quando trabalhando com listas em Python, qual método é usado para adicionar um novo item, como uma letra acertada em um jogo da forca?
- (A) letras_acertadas.insert('a')
- (B) letras_acertadas.append('a')
- (C) letras_acertadas.add('a')
- (D) letras_acertadas.push('a')
- Escolhendo alguém para responder essa questão!

_4 imagem(ns) no slide._

### Slide 16

- DESENVOLVIMENTO DE SISTEMAS
- Resposta correta
- Quando trabalhando com listas em Python, qual método é usado para adicionar um novo item, como uma letra acertada em um jogo da forca?
- (A) letras_acertadas.insert('a')
- (B) letras_acertadas.append('a')
- (C) letras_acertadas.add('a')
- (D) letras_acertadas.push('a’)
- Resposta Correta: (B) letras_acertadas.append('a')

_3 imagem(ns) no slide._

> **Notas do apresentador:** Comentário: A alternativa a é correta porque o método .replace() é usado para substituir partes de uma string por outra. Neste caso, substituir todas as ocorrências de "Python" por "JavaScript" muda efetivamente o texto da string original para refletir a nova linguagem mencionada, demonstrando uma manipulação direta e eficaz do conteúdo da string.

### Slide 17

- DESENVOLVIMENTO DE SISTEMAS
- Conclusão
- As listas em Python são estruturas de dados flexíveis e poderosas, essenciais para coletar e manipular dados dinamicamente em programas e jogos.

_4 imagem(ns) no slide._

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- Atividade Prática na Plataforma Alura
- Na plataforma Alura vamos acessar o seguinte curso:
- A recomendação é que você continue esse curso extraclasse, pois ele traz um conteúdo essencial para compreender sobre o referido tema.
- Link para o curso: https://cursos.alura.com.br/course/python-3-avancando-na-linguagem

_5 imagem(ns) no slide._

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- Estrutura de dados: List
- 11 minutos
- Link para tarefa: https://cursos.alura.com.br/course/python-3-avancando-na-linguagem/task/25131
- A estrutura de dados List em Python permite armazenar uma coleção ordenada e mutável de itens. É versátil para manipulação de dados, suportando operações como adição, remoção e busca de elementos.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 20

- DESENVOLVIMENTO DE SISTEMAS
- Guardando as letras acertadas
- 6 minutos
- Link para tarefa: https://cursos.alura.com.br/course/python-3-avancando-na-linguagem/task/25132
- Para guardar as letras acertadas em um jogo da forca, utilize uma lista em Python. Inicie com uma lista vazia e adicione as letras acertadas pelo jogador usando o método .append(), facilitando o rastreamento do progresso do jogo.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 21

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje:
- Aprendemos como criar, manipular e utilizar listas em Python para armazenar letras acertadas em um jogo da forca, destacando métodos essenciais como .append() e .remove(), fundamentais para o desenvolvimento de jogos interativos.
- Na próxima aula, vamos conhecer e desenvolver operações com tuplas.

_4 imagem(ns) no slide._

### Slide 22

- DESENVOLVIMENTO DE SISTEMAS
- Bibliografia
- PUREWAL, Semmy. Aprendendo a Desenvolver Aplicações Web. Desenvolva rapidamente com as tecnologias JavaScript mais modernas. São Paulo: Novatec, 2014.
- SILVA, L. F.; OLIVEIRA, A. D. de. Desenvolvimento de Software II C#: programação em camadas. [S. l.]: CBL Edição do Autor, 2017. E-book.
- MARTIN, R. C. Arquitetura limpa: o guia do artesão para estrutura e design de software. Rio de Janeiro: Alta Books, 2019. E-book.
- GALOTTI, G. M. A. Qualidade de software. São Paulo: Pearson Education do Brasil, 2016. E-book.
- VAZQUEZ, C. E.; SIMÕES, G. S. Engenharia de requisitos: software orientado ao negócio. São Paulo: Brasport, 2016. E-book.
- Softwares
- Java Netbeans; WebStorm; Sublime Text; Intellij IDEA; Astah Software; Netbeans; Python; Ccharp; Colab; PyCharm; Jupyter Notebook.
- Referências

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

_Fonte: AULA 12_ATIVIDADE_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

ATIVIDADE AULA 12

Questão 1

Como você pode inicializar uma lista vazia em Python para guardar as letras acertadas em um jogo da forca?

a) letras_acertadas = list('a', 'b', 'c')

b) letras_acertadas = []

c) letras_acertadas = list()

d) letras_acertadas = ('a', 'b', 'c')

Resposta Correta: b) letras_acertadas = []

Comentário: A opção b é correta porque a sintaxe [] é usada para inicializar uma lista vazia em Python. Esta forma é direta e eficiente para começar a coletar letras acertadas em um jogo, permitindo adições dinâmicas à medida que o jogador acerta as letras.

Questão 2

Qual método é utilizado para remover um item específico de uma lista em Python?

a) letras_acertadas.delete('a')

b) letras_acertadas.remove('a')

c) letras_acertadas.pop('a')

d) letras_acertadas.discard('a')

Resposta Correta: b) letras_acertadas.remove('a')

Comentário: A opção b é correta porque o método .remove() é usado para remover um item específico de uma lista, identificado pelo seu valor. Este método é especialmente útil em jogos ou aplicações onde você precisa dinamicamente ajustar os conteúdos da lista com base nas ações do usuário.
