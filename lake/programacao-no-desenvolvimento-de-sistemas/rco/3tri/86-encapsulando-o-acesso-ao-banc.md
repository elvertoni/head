---
titulo: "Encapsulando o acesso ao banco"
tipo: rco-seed
disciplina: programacao-no-desenvolvimento-de-sistemas
sigla_rco: PDS
trimestre: 3
ordem_rco: 86
serie: 3
aula_rco: "Aula 86"
slides: 25
tem_atividade: false
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/3TRI/86-encapsulando-o-acesso-ao-banc/86-encapsulando-o-acesso-ao-banc.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/3TRI/86-encapsulando-o-acesso-ao-banc/AULA 86_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Encapsulando o acesso ao banco

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO NO
- DESENVOLVIMENTO DE
- SISTEMAS
- 3ª SÉRIE
- Encapsulando o acesso ao banco
- Aula 86

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
- Explorar como encapsular o acesso ao banco de dados em um Windows Forms.

_7 imagem(ns) no slide._

### Slide 4

- DESENVOLVIMENTO DE SISTEMAS
- ATENÇÃO PROFESSOR!
- O Material aqui apresentado, segue a análise do plano de curso contemplando os componentes curriculares e seus objetos de conhecimento, sendo assim, você tem liberdade para customizar o material conforme seu contexto para maior aproveitamento do conteúdo. Em caso de falta ou indisponibilidade de acesso à internet no local de aula, você poderá utilizar os seguintes artigos para criação de material complementar para auxiliar na aula:
- Leitura/Recursos Adicionais:
- Visual Studio Community Edition: IDE gratuita para desenvolvimento em .NET.
- .NET Framework: Plataforma de desenvolvimento necessária para criar aplicações Windows Forms.
- VSCode com Extensão C#: Alternativa open-source para desenvolvimento em .NET.

_5 imagem(ns) no slide._

### Slide 5

- DESENVOLVIMENTO DE SISTEMAS
- Na aula anterior…
- Exploramos o uso do LocalDB no Windows Forms. Aprendemos a criar um banco de dados local, construir tabelas, e conectar o Windows Forms para executar operações CRUD no banco de dados.

_4 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Lucas está criando uma aplicação para uma pequena loja que precisa gerenciar seus clientes no banco de dados. Ele percebe que o código de acesso ao banco de dados está espalhado por toda a aplicação, o que torna a manutenção difícil.

_4 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Pergunta
- Como Lucas pode encapsular o acesso ao banco de dados em uma única classe, de modo que qualquer operação de banco seja realizada de forma centralizada e eficiente?
- Quem sabe responde!

_5 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Lucas deve criar uma classe de acesso ao banco de dados que contenha todos os métodos necessários para conectar, executar comandos e retornar resultados. Isso facilita a manutenção, pois qualquer alteração futura será centralizada.

_4 imagem(ns) no slide._

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- Visão Geral
- Encapsular o acesso ao banco de dados significa concentrar a lógica de conexão e manipulação de dados em uma única classe. Isso aumenta a organização, a legibilidade e a manutenibilidade do código, além de facilitar testes e melhorias.

_4 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- Definição e Aplicação
- String de Conexão: É a chave para conectar seu aplicativo ao banco de dados. Ela contém informações como o nome do servidor, banco de dados, autenticação e outras configurações.
- Classe de Acesso ao Banco: Uma classe dedicada a manipular a conexão e as operações do banco de dados.
- Métodos de Comando e Consulta: Funções que encapsulam a lógica de executar comandos SQL, como INSERT, UPDATE, e SELECT.

_3 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Importância
- A centralização do código de banco em uma classe aumenta a coesão do sistema, simplifica a manutenção e a escalabilidade, e reduz a duplicação de código.

_4 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- Uso
- Desenvolvedores frequentemente usam esse conceito em projetos maiores para melhorar a arquitetura de software. A reutilização de métodos de consulta e comando também torna o código mais eficiente.

_4 imagem(ns) no slide._

### Slide 13

- DESENVOLVIMENTO DE SISTEMAS
- Classe para
- Encapsular a
- Conexão com o
- Banco de dados
- Utilize o visual studio comunity

_5 imagem(ns) no slide._

### Slide 14

- DESENVOLVIMENTO DE SISTEMAS
- Questão de fixação
- Qual o principal benefício de encapsular o acesso ao banco de dados?
- A) Aumentar a performance
- B) Facilitar a manutenção
- C) Reduzir a complexidade do código
- D) Melhorar a segurança do banco de dados
- Quem sabe responde!

_4 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- Resposta!
- Qual o principal benefício de encapsular o acesso ao banco de dados?
- A) Aumentar a performance
- B) Facilitar a manutenção
- C) Reduzir a complexidade do código
- D) Melhorar a segurança do banco de dados
- Resposta correta: B

_3 imagem(ns) no slide._

### Slide 16

- DESENVOLVIMENTO DE SISTEMAS
- Atividade Prática na Plataforma Alura
- Na plataforma Alura vamos acessar o seguinte curso:
- A recomendação é que você continue esse curso extraclasse, pois ele traz um conteúdo essencial para compreender sobre o referido tema.
- Link para o curso: https://cursos.alura.com.br/course/windows-forms-csharp-introducao-banco-de-dados

_6 imagem(ns) no slide._

### Slide 17

- DESENVOLVIMENTO DE SISTEMAS
- Entendendo a string de conexão
- 14 minutos
- Link para tarefa: https://cursos.alura.com.br/course/windows-forms-csharp-introducao-banco-de-dados/task/76488
- A string de conexão é uma cadeia de caracteres que contém as informações necessárias para conectar um aplicativo a um banco de dados, como servidor, banco de dados, autenticação e outras configurações essenciais.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- Classe de acesso ao banco de dados
- 8 minutos
- Link para tarefa: https://cursos.alura.com.br/course/windows-forms-csharp-introducao-banco-de-dados/task/76489
- A classe de acesso ao banco de dados encapsula a lógica para conectar, executar comandos e consultas. Ela centraliza operações como inserir, atualizar e excluir dados, facilitando a manutenção e reutilização do código.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- Obtendo a string de conexão
- 5 minutos
- Link para tarefa: https://cursos.alura.com.br/course/windows-forms-csharp-introducao-banco-de-dados/task/76490
- A string de conexão é obtida geralmente de um arquivo de configuração, como app.config, para facilitar a gestão do acesso ao banco de dados. Ela contém informações como servidor, nome do banco, autenticação e outras configurações necessárias para estabelecer a conexão.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 20

- DESENVOLVIMENTO DE SISTEMAS
- Método para executar um comando
- 8 minutos
- Link para tarefa: https://cursos.alura.com.br/course/windows-forms-csharp-introducao-banco-de-dados/task/76491
- O método para executar um comando em C# utiliza a classe SqlCommand para enviar instruções SQL ao banco de dados. Ele pode ser usado para inserções, atualizações e exclusões, executando o método ExecuteNonQuery().
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 21

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje
- Cobrimos a importância do encapsulamento no acesso ao banco de dados, aprendemos como configurar a string de conexão e desenvolver métodos eficientes para executar comandos e consultas.

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

## Outros documentos

_Fonte: AULA 86_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

ATIVIDADE AULA 86

Questão 1

Como um método de consulta pode ser otimizado?

A) Utilizando transações

B) Usando consultas SQL inline

C) Reutilizando conexões abertas

D) Separando a lógica de negócio e de consulta

Resposta correta: D

Questão 2

Por que é importante obter a string de conexão de forma dinâmica?

A) Para aumentar a segurança

B) Para facilitar a troca de ambientes

C) Para reduzir o tempo de execução

D) Para automatizar a conexão

Resposta correta: B
