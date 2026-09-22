---
titulo: "Quando não usar herança"
tipo: rco-seed
disciplina: programacao-no-desenvolvimento-de-sistemas
sigla_rco: PDS
trimestre: 1
ordem_rco: 26
serie: 3
aula_rco: "Aula 26"
slides: 25
tem_atividade: true
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/1TRI/26-quando-nao-usar-heranca/26-quando-nao-usar-heranca.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PDS/1TRI/26-quando-nao-usar-heranca/AULA 26_ATIVIDADE_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PDS/1TRI/26-quando-nao-usar-heranca/AULA 26_SAIBA MAIS_ PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Quando não usar herança

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO NO
- DESENVOLVIMENTO DE
- SISTEMAS
- 3ª SÉRIE
- Quando não usar herança
- Aula 26

_3 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- DESENVOLVIMENTO DE SISTEMAS
- Na aula de hoje, vamos:
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store
- Empregar situações onde a herança pode ser mais prejudicial do que benéfica.

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
- Revisamos conceitos fundamentais de herança e polimorfismo, observando como podem ser aplicados para simplificar e estender funcionalidades de classes base em cenários específicos de desenvolvimento.

_4 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Carlos, um jovem desenvolvedor, começa a usar herança em todos os seus projetos, porém, se depara com uma manutenção difícil e um código confuso.
- Para pensarmos juntos!

_4 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Será que…
- Existem momentos onde a herança NÃO é a melhor escolha?
- Quem sabe responde!

_5 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Sim, Carlos!
- Existem situações onde a herança pode complicar mais do que ajudar, especialmente quando as classes-filhas não representam uma relação estrita de "é um tipo de".
- Em tais casos, composição ou interfaces podem ser mais adequadas, evitando a herança rígida e promovendo maior flexibilidade e desacoplamento no design do software.

_4 imagem(ns) no slide._

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- Finalidade e Utilização
- Herança é um pilar da Programação Orientada a Objetos - POO, que permite a uma classe herdar atributos e métodos de outra classe.
- No entanto, seu uso nem sempre é apropriado!
- Embora a herança possa parecer uma maneira prática de reutilizar código, em alguns casos ela pode levar a uma alta acoplamento e complexidade desnecessária.
- É essencial entender quando e como aplicar herança corretamente para manter o código limpo, manutenível e eficiente.

_4 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- E quando não se deve usar a herança?
- Não se deve usar herança quando as classes não possuem uma relação clara de "é um(a)".
- Se você tem uma classe "Animal" e outra "Automóvel", não faz sentido usar herança entre elas, pois
- UM AUTOMÓVEL NÃO É UM TIPO DE ANIMAL.
- Exemplo!
- A herança deve ser usada apenas quando uma subclasse é verdadeiramente uma especialização da superclasse.

_6 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Criando a playlist e reaproveitando uma list
- Suponha que você esteja construindo uma aplicação para gerenciar playlists de músicas. Em vez de criar uma estrutura de dados complexa do zero, você pode reaproveitar a funcionalidade da lista embutida em Python.
- Uma playlist pode ser representada simplesmente como uma lista de strings (nomes das músicas), aproveitando métodos já existentes para adicionar, remover ou reordenar as músicas.

_4 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- Fugindo da complexidade
- https://s2.glbimg.com/C-mEZ4jxJ7FAz_9CREL0a3UXrBI=/0x0:500x500/500x500/middle/i.s3.glbimg.com/v1/AUTH_59edd422c0c84a879bd37670ae4f538a/internal_photos/bs/2020/H/Z/qcfY6IT9ayAbmO4wavdw/giphy-9-.gif
- Utilizar estruturas e métodos simples quando possível ajuda a evitar a complexidade desnecessária.
- No caso da playlist, ao invés de criar uma classe complexa com herança, usar uma lista diretamente torna o código mais acessível e fácil de entender para outros desenvolvedores, bem como mais fácil de manter.

_4 imagem(ns) no slide._

### Slide 13

- DESENVOLVIMENTO DE SISTEMAS
- Exemplos
- Acesse o arquivo Saiba Mais!

_4 imagem(ns) no slide._

### Slide 14

- DESENVOLVIMENTO DE SISTEMAS
- Atividade para a fixação do conteúdo estudado
- Qual é a principal vantagem de usar listas diretamente para criar uma playlist em Python, em vez de usar uma estrutura de herança?
- (A) Aumenta a complexidade do código
- (B) Facilita a reutilização de código existente
- (C) Torna o código menos flexível
- (D) Requer conhecimento avançado de POO
- Escolhendo alguém para responder essa questão!

_4 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Qual é a principal vantagem de usar listas diretamente para criar uma playlist em Python, em vez de usar uma estrutura de herança?
- (A) Aumenta a complexidade do código
- (B) Facilita a reutilização de código existente
- (C) Torna o código menos flexível
- (D) Requer conhecimento avançado de POO
- Resposta Correta: (B) Facilita a reutilização de código existente

_3 imagem(ns) no slide._

> **Notas do apresentador:** Comentário sobre a resposta: Utilizar listas diretamente para gerenciar playlists tira proveito dos métodos embutidos de Python, simplificando o desenvolvimento e manutenção do código ao reutilizar funcionalidades já testadas e otimizadas, em vez de criar novas estruturas complexas onde não são necessárias.

### Slide 16

- DESENVOLVIMENTO DE SISTEMAS
- Conclusão
- A herança deve ser evitada em situações onde estruturas simples e já existentes como listas podem ser utilizadas eficientemente, promovendo simplicidade e reduzindo a chance de erros e complicações desnecessárias.

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
- Criando a playlist
- 11 minutos
- Link para tarefa: https://cursos.alura.com.br/course/python-3-avancando-orientacao-objetos/task/41786
- Criar uma playlist em Python pode ser simplesmente gerenciado com uma lista, que permite adicionar, remover ou manipular faixas de maneira eficiente sem a necessidade de estruturas complexas como classes.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- Reaproveitando um list
- 9 minutos
- Link para tarefa: https://cursos.alura.com.br/course/python-3-avancando-orientacao-objetos/task/41787
- Reaproveitar um list em Python envolve utilizar métodos pré-existentes para efetuar operações como inserção, exclusão e iteração, maximizando eficiência e reduzindo a necessidade de código redundante ou complexo.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 20

- DESENVOLVIMENTO DE SISTEMAS
- Fugindo da complexidade
- 9 minutos
- Link para tarefa: https://cursos.alura.com.br/course/python-3-avancando-orientacao-objetos/task/41788
- "Fugindo da complexidade" refere-se a simplificar soluções de software, evitando sobrecomplicar o código com estruturas desnecessárias. Prioriza-se manter a clareza e a manutenibilidade, facilitando o entendimento e a manutenção futura.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 21

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje:
- Compreendemos quando devemos evitar a herança em Python, optando por estruturas mais simples como listas para tarefas como criar e gerenciar playlists, visando simplificar o código e aumentar sua mantenabilidade.

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

_Fonte: AULA 26_ATIVIDADE_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

ATIVIDADE AULA 26

Questão 1

Por que evitar a herança quando é possível usar uma lista em Python para gerenciar coleções simples como playlists?

a) Porque a herança sempre acelera o acesso aos dados

b) Para evitar a reescrita de métodos existentes

c) Para reduzir a complexidade e aumentar a flexibilidade

d) Porque isso torna o código menos seguro

Resposta Correta: c) Para reduzir a complexidade e aumentar a flexibilidade

Comentário: A herança pode introduzir complexidade desnecessária quando simples estruturas de dados como listas já fornecem a funcionalidade necessária, permitindo um código mais flexível e fácil de manter.

Questão 2

Qual é uma razão válida para reutilizar listas ao invés de criar novas classes em Python para tarefas simples?

a) Classes fornecem automaticamente melhores performances

b) Listas não permitem encapsulamento de dados

c) Reutilizar listas aproveita métodos e propriedades existentes eficientemente

d) Herança é menos suportada em Python

Resposta Correta: c) Reutilizar listas aproveita métodos e propriedades existentes eficientemente

Comentário: Reaproveitar listas permite usar a funcionalidade pronta da linguagem Python, minimizando o esforço de desenvolvimento e mantendo o código limpo e simples.

## Outros documentos

_Fonte: AULA 26_SAIBA MAIS_ PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

SAIBA MAIS AULA 23

Exemplo prático:

# Simples implementação de uma playlist usando lista

playlist = ["song1.mp3", "song2.mp3", "song3.mp3"]

# Adicionar uma música

playlist.append("song4.mp3")

# Remover uma música

playlist.remove("song2.mp3")

# Exibir a playlist

print(playlist)
