---
titulo: "Introdução à Estruturas e Registros em C"
tipo: rco-seed
disciplina: programacao-no-desenvolvimento-de-sistemas
sigla_rco: PDS
trimestre: 2
ordem_rco: 50
serie: 3
aula_rco: "Aula 50"
slides: 25
tem_atividade: true
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PDS/2TRI/50-introducao-a-estruturas-e-registros-em-c/50-introducao-a-estruturas-e-registros-em-c.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PDS/2TRI/50-introducao-a-estruturas-e-registros-em-c/AULA 50_ATIVIDADE_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Introdução à Estruturas e Registros em C

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO NO
- DESENVOLVIMENTO DE
- SISTEMAS
- 3ª SÉRIE
- Introdução à Estruturas e Registros em C
- Aula 50

_3 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- DESENVOLVIMENTO DE SISTEMAS
- Nesta aula, vamos:
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store
- Exploraremos como as estruturas e registros em C nos permitem organizar e manipular dados de forma eficiente. Vamos aprender a definir estruturas, declarar variáveis de estrutura e acessar seus membros.

_7 imagem(ns) no slide._

### Slide 4

- DESENVOLVIMENTO DE SISTEMAS
- ATENÇÃO PROFESSOR!
- O Material aqui apresentado, segue a análise do plano de curso contemplando os componentes curriculares e seus objetos de conhecimento, sendo assim, você tem liberdade para customizar o material conforme seu contexto para maior aproveitamento do conteúdo. Em caso de falta ou indisponibilidade de acesso à internet no local de aula, você poderá utilizar os seguintes artigos para criação de material complementar para auxiliar na aula:
- Leitura/Recursos Adicionais:
- Dev-C++: Um IDE gratuito e leve para programação em C e C++, ótimo para iniciantes.
- OnlineGDB: Um compilador e depurador online para C, fácil de usar e permite compartilhar código.

_5 imagem(ns) no slide._

### Slide 5

- DESENVOLVIMENTO DE SISTEMAS
- Na aula anterior…
- Revisamos a aplicação prática e revisão de código em C, focando na importância da legibilidade e organização do código para facilitar a manutenção e colaboração.

_4 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Maria está desenvolvendo um programa para gerenciar informações de alunos, incluindo nome, idade e notas. Ela está aprendendo sobre estruturas e registros em C para organizar esses dados de forma eficiente.

_4 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Como Maria pode definir e usar uma estrutura para armazenar as informações dos alunos de maneira organizada?
- Quem sabe responde!

_5 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Maria pode definir uma estrutura chamada Aluno que inclui membros como nome, idade e notas. Usando essa estrutura, ela pode criar variáveis de tipo Aluno e acessar os membros usando o operador ponto (.).

_4 imagem(ns) no slide._

> **Notas do apresentador:** Entender e usar estruturas permitirá que Maria organize dados complexos de forma simples e eficiente, facilitando operações como cálculos de média e armazenamento de informações.

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- Estruturas de dados em C
- Estruturas em C são coleções de variáveis de tipos diferentes agrupadas sob um único nome. Elas permitem organizar dados relacionados, como informações de um aluno, em um formato coeso.

_4 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- Definição e Aplicação
- Uma estrutura é definida usando a palavra-chave struct, seguida pela definição dos membros. Por exemplo:

_4 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Importância
- Estruturas são essenciais para organizar dados complexos em programas C, tornando o código mais legível e eficiente. Elas são a base para registros e tipos de dados mais complexos usados em sistemas maiores.

_4 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- Uso
- Na prática, estruturas são usadas para agrupar dados relacionados. Por exemplo, um sistema de gerenciamento de alunos pode usar uma estrutura para armazenar informações pessoais e acadêmicas dos alunos.

_4 imagem(ns) no slide._

### Slide 13

- DESENVOLVIMENTO DE SISTEMAS
- Exemplo
- Utilize a plataforma https://www.onlinegdb.com/

_5 imagem(ns) no slide._

### Slide 14

- DESENVOLVIMENTO DE SISTEMAS
- Resultado da compilação
- Utilize a plataforma https://www.onlinegdb.com/

_5 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- Atividade para a fixação do conteúdo estudado
- Qual é a sintaxe correta para definir uma estrutura chamada Livro com membros titulo, autor e ano?
- A) struct Livro { char titulo[100]; char autor[50]; int ano; };
- B) struct Livro ( char titulo[100]; char autor[50]; int ano; );
- C) struct Livro { string titulo; string autor; int ano; };
- D) struct Livro { char titulo; char autor; int ano; };
- Escolhendo alguém para responder essa questão!

_4 imagem(ns) no slide._

### Slide 16

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Qual é a sintaxe correta para definir uma estrutura chamada Livro com membros titulo, autor e ano?
- A) struct Livro { char titulo[100]; char autor[50]; int ano; };
- B) struct Livro ( char titulo[100]; char autor[50]; int ano; );
- C) struct Livro { string titulo; string autor; int ano; };
- D) struct Livro { char titulo; char autor; int ano; };
- Comentários: A opção A usa a sintaxe correta para definir uma estrutura em C.

_3 imagem(ns) no slide._

### Slide 17

- DESENVOLVIMENTO DE SISTEMAS
- Vamos Praticar?
- Utilize a plataforma https://www.onlinegdb.com/

_6 imagem(ns) no slide._

> **Notas do apresentador:** Comentário sobre a resposta correta: A imutabilidade das tuplas garante que os dados não sejam alterados acidentalmente, proporcionando segurança.

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- Vamos Praticar?
- Utilize a plataforma https://www.onlinegdb.com/

_6 imagem(ns) no slide._

> **Notas do apresentador:** Comentário sobre a resposta correta: A imutabilidade das tuplas garante que os dados não sejam alterados acidentalmente, proporcionando segurança.

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- Vamos Praticar?
- Utilize a plataforma https://www.onlinegdb.com/
- Adicionar mais um campo à estrutura
- Peça aos alunos para adicionar mais um campo matricula à estrutura Aluno e atualizar o código para coletar e exibir este novo campo.

_6 imagem(ns) no slide._

> **Notas do apresentador:** Comentário sobre a resposta correta: A imutabilidade das tuplas garante que os dados não sejam alterados acidentalmente, proporcionando segurança.

### Slide 20

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Utilize a plataforma https://www.onlinegdb.com/

_6 imagem(ns) no slide._

> **Notas do apresentador:** Comentário sobre a resposta correta: A imutabilidade das tuplas garante que os dados não sejam alterados acidentalmente, proporcionando segurança.

### Slide 21

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje
- Exploramos a definição e uso de estruturas e registros em C, aprendendo a organizar dados complexos de forma eficiente. Discutimos a importância das estruturas, como aplicá-las em programas práticos e fornecemos exemplos de código para ilustrar seu uso.

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

_5 imagem(ns) no slide._

## Atividade

_Fonte: AULA 50_ATIVIDADE_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

ATIVIDADE AULA 50

Questão 1

Qual das seguintes alternativas é verdadeira sobre o acesso aos membros de uma estrutura?

A) O operador -> é usado para acessar membros de uma estrutura diretamente.

B) O operador . é usado para acessar membros de uma estrutura diretamente.

C) O operador & é usado para acessar membros de uma estrutura diretamente.

D) O operador * é usado para acessar membros de uma estrutura diretamente.

Resposta Correta: B

Comentário: O operador ponto (.) é usado para acessar diretamente os membros de uma estrutura em C.

Questão 2

Qual é a finalidade principal de usar estruturas em C?

A) Armazenar variáveis globais.

B) Organizar dados de diferentes tipos sob um único nome.

C) Facilitar a criação de loops.

D) Reduzir o tempo de compilação.

Resposta Correta: B

Comentário: Estruturas permitem organizar dados de diferentes tipos sob um único nome, facilitando a manipulação de dados complexos.
