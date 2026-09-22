---
titulo: "Arquivos em C e Revisão Geral do Projeto"
tipo: rco-seed
disciplina: programacao-no-desenvolvimento-de-sistemas
sigla_rco: PDS
trimestre: 2
ordem_rco: 53
serie: 3
aula_rco: "Aula 53"
slides: 25
tem_atividade: false
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PDS/2TRI/53-arquivos-em-c-e-revisao-geral-do-projeto/53-arquivos-em-c-e-revisao-geral-do-projeto.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PDS/2TRI/53-arquivos-em-c-e-revisao-geral-do-projeto/AULA 53_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Arquivos em C e Revisão Geral do Projeto

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO NO
- DESENVOLVIMENTO DE
- SISTEMAS
- 3ª SÉRIE
- Arquivos em C e Revisão Geral do Projeto
- Aula 53

_3 imagem(ns) no slide._

### Slide 2

_(sem texto)_

_1 imagem(ns) no slide._

### Slide 3

- DESENVOLVIMENTO DE SISTEMAS
- Nesta aula, vamos:
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store
- Armazenar e recuperar
- arquivos em C de forma eficiente.

_7 imagem(ns) no slide._

### Slide 4

- DESENVOLVIMENTO DE SISTEMAS
- ATENÇÃO PROFESSOR!
- O Material aqui apresentado, segue a análise do plano de curso contemplando os componentes curriculares e seus objetos de conhecimento, sendo assim, você tem liberdade para customizar o material conforme seu contexto para maior aproveitamento do conteúdo. Em caso de falta ou indisponibilidade de acesso à internet no local de aula, você poderá utilizar os seguintes artigos para criação de material complementar para auxiliar na aula:
- Leitura/Recursos Adicionais:
- Dev-C++: Um IDE gratuito e leve para programação em C e C++, ótimo para iniciantes.
- Online GDB: Um compilador e depurador online para C, fácil de usar e permite compartilhar código.

_5 imagem(ns) no slide._

### Slide 5

- DESENVOLVIMENTO DE SISTEMAS
- Na aula anterior…
- Abordamos as estruturas e registros em C, aprendendo a organizar e manipular dados complexos. Utilizamos exemplos práticos para ilustrar como essas estruturas podem ser aplicadas para resolver problemas do mundo real.

_4 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- João está desenvolvendo um sistema de biblioteca que precisa armazenar informações sobre livros, incluindo título, autor e ano de publicação.
- Ele quer que esses dados sejam persistentes, ou seja, que permaneçam disponíveis mesmo após o programa ser fechado.

_4 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Como João pode utilizar arquivos em C para armazenar e recuperar as informações dos livros de forma eficiente?
- Quem sabe responde!

_6 imagem(ns) no slide._

### Slide 8

- Resposta
- João pode usar funções de manipulação de arquivos em C, como fopen, fprintf, fscanf, fclose, para criar, escrever e ler dados de arquivos.
- Ele pode armazenar cada livro em uma linha do arquivo, com os campos separados por vírgulas ou espaços.
- DESENVOLVIMENTO DE SISTEMAS

_4 imagem(ns) no slide._

> **Notas do apresentador:** Usar arquivos permite que os dados dos livros sejam preservados entre as execuções do programa, facilitando a gestão e recuperação das informações sem perda de dados.

### Slide 9

- Visão Geral
- Arquivos em C permitem armazenar dados em formato persistente, facilitando a leitura e escrita de informações.
- DESENVOLVIMENTO DE SISTEMAS
- Isso é essencial para a criação de aplicativos que precisam manter dados entre execuções!

_4 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- Definição e Aplicação
- Arquivos são utilizados para guardar informações que precisam ser acessadas posteriormente. Em C, funções como fopen, fclose, fprintf, e fscanf são usadas para manipular arquivos.

_4 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Importância
- Manipular arquivos é essencial para criar programas que necessitam de persistência de dados, como sistemas de gestão, bancos de dados simples, e aplicativos que exigem configuração armazenada.

_4 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- Uso
- Por exemplo, um programa de biblioteca pode usar arquivos para salvar informações sobre livros, permitindo que o sistema recupere esses dados na próxima execução.

_4 imagem(ns) no slide._

### Slide 13

- DESENVOLVIMENTO DE SISTEMAS
- Exemplo
- Utilize a plataforma https://www.onlinegdb.com/
- Aqui está um exemplo de programa que armazena informações de livros em um arquivo:

_5 imagem(ns) no slide._

### Slide 14

- DESENVOLVIMENTO DE SISTEMAS
- Resultado da compilação
- Utilize a plataforma https://www.onlinegdb.com/

_5 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- Atividade para a fixação do conteúdo estudado
- Qual das opções não é uma função usada para manipulação de arquivos em C?
- (A) fopen
- (B) fprintf
- (C) fclose
- (D) fprint
- Escolhendo alguém para responder essa questão!

_4 imagem(ns) no slide._

### Slide 16

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Qual das opções não é uma função usada para manipulação de arquivos em C?
- (A) fopen
- (B) fprintf
- (C) fclose
- (D) Fprint
- Resposta Correta: (D) fprint - Não existe uma função fprint em C. As funções corretas são fopen, fprintf, e fclose.

_3 imagem(ns) no slide._

### Slide 17

- DESENVOLVIMENTO DE SISTEMAS
- Vamos Praticar?
- Utilize a plataforma https://www.onlinegdb.com/

_6 imagem(ns) no slide._

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- Vamos Praticar?
- Utilize a plataforma https://www.onlinegdb.com/

_6 imagem(ns) no slide._

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- Vamos Praticar?
- Utilize a plataforma https://www.onlinegdb.com/
- Modifique o código para contar o número de livros armazenados no arquivo e exibir esse número após a leitura dos livros.

_6 imagem(ns) no slide._

### Slide 20

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Utilize a plataforma https://www.onlinegdb.com/

_6 imagem(ns) no slide._

### Slide 21

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje
- Exploramos como usar arquivos em C para armazenar e recuperar dados, além de revisar o projeto para consolidar o conhecimento. Entender a manipulação de arquivos é essencial para criar programas que necessitam de persistência de dados, como sistemas de gerenciamento e bancos de dados simples.

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

## Outros documentos

_Fonte: AULA 53_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

ATIVIDADE AULA 53

Questão 1

Qual das seguintes funções é usada para ler dados de um arquivo em C?

A) fopen

B) fclose

C) fprintf

D) fscanf

Resposta Correta: D) fscanf - fscanf é usada para ler dados de um arquivo.

Questão 2

O que significa o modo "a" ao abrir um arquivo com fopen em C?

A) Abrir para leitura

B) Abrir para escrita, apagando o conteúdo existente

C) Abrir para escrita, adicionando ao final do arquivo

D) Abrir para leitura e escrita

Resposta Correta: C) Abrir para escrita, adicionando ao final do arquivo - O modo "a" adiciona dados ao final do arquivo sem apagar o conteúdo existente.
