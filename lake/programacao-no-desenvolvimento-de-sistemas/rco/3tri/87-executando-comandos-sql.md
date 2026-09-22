---
titulo: "Executando comandos SQL"
tipo: rco-seed
disciplina: programacao-no-desenvolvimento-de-sistemas
sigla_rco: PDS
trimestre: 3
ordem_rco: 87
serie: 3
aula_rco: "Aula 87"
slides: 25
tem_atividade: false
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/3TRI/87-executando-comandos-sql/87-executando-comandos-sql.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/3TRI/87-executando-comandos-sql/AULA 87_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Executando comandos SQL

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO NO
- DESENVOLVIMENTO DE
- SISTEMAS
- 3ª SÉRIE
- Executando comandos SQL
- Aula 87

_3 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- DESENVOLVIMENTO DE SISTEMAS
- Nesta aula, vamos:
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store
- Aprender a criar e executar comandos SQL diretamente no Windows Forms.

_7 imagem(ns) no slide._

### Slide 4

- DESENVOLVIMENTO DE SISTEMAS
- ATENÇÃO PROFESSOR!
- O Material aqui apresentado, segue a análise do plano de curso contemplando os componentes curriculares e seus objetos de conhecimento, sendo assim, você tem liberdade para customizar o material conforme seu contexto para maior aproveitamento do conteúdo. Em caso de falta ou indisponibilidade de acesso à internet no local de aula, você poderá utilizar os seguintes artigos para criação de material complementar para auxiliar na aula:
- Leitura/Recursos Adicionais:
- Visual Studio Community (IDE gratuita para desenvolvimento em C#)
- Funcionalidades: Criação e desenvolvimento de Windows Forms com suporte para SQL Server.
- SQL Server Express (Banco de dados gratuito)
- Funcionalidades: Suporte para criar e testar bancos de dados locais.

_5 imagem(ns) no slide._

### Slide 5

- DESENVOLVIMENTO DE SISTEMAS
- Na aula anterior…
- Abordamos como encapsular o acesso ao banco de dados, criando métodos que facilitam a manipulação de dados. Aprendemos sobre a string de conexão, como executá-la e como capturar respostas do banco.

_4 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Mariana está desenvolvendo um sistema para uma pequena empresa. Ela precisa cadastrar novos clientes e salvar seus dados no banco de dados LocalDB. Durante a execução, ela enfrenta dificuldades em definir e executar os comandos SQL corretamente.

_4 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Pergunta
- Como Mariana pode usar comandos SQL no Windows Forms para incluir os dados de novos clientes?
- Quem sabe responde!

_5 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Mariana pode criar a classe FicharioDB, onde encapsulará a lógica de inclusão de dados. Dentro dessa classe, ela pode definir um comando SQL INSERT INTO para armazenar os dados dos clientes em uma tabela no banco de dados. Esse comando é executado por meio do SqlCommand e ExecuteNonQuery().

_4 imagem(ns) no slide._

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- Executar comandos SQL diretamente em uma aplicação Windows Forms é uma habilidade fundamental para quem está desenvolvendo sistemas que precisam manipular bancos de dados. Esses comandos permitem inserir, atualizar e excluir informações.

_4 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- Comandos SQL (Structured Query Language) são instruções usadas para manipular dados em um banco de dados. No contexto de Windows Forms, esses comandos são enviados para o banco através de classes como SqlCommand. O comando INSERT INTO, por exemplo, permite incluir novos dados no banco.

_4 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Entender e aplicar comandos SQL no Windows Forms permite que o desenvolvedor integre a interface gráfica com o banco de dados, possibilitando o armazenamento e a recuperação de dados de clientes ou outros tipos de informações.

_4 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- Um sistema de cadastro de clientes pode utilizar SQL para armazenar informações como nome, endereço e telefone de forma permanente no banco de dados. Comandos SQL são usados para enviar essas informações da interface gráfica (formulário) para o banco.

_4 imagem(ns) no slide._

### Slide 13

- DESENVOLVIMENTO DE SISTEMAS
- Neste exemplo, a classe FicharioDB contém o método IncluirCliente, que executa um comando SQL de inclusão no banco de dados.
- Utilize o visual studio comunity

_5 imagem(ns) no slide._

### Slide 14

- DESENVOLVIMENTO DE SISTEMAS
- Questão de fixação
- Pergunta: Qual comando SQL é usado para inserir dados em uma tabela?
- A) SELECT
- B) DELETE
- C) INSERT INTO
- D) UPDATE
- Quem sabe responde!

_4 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- Resposta!
- Pergunta: Qual comando SQL é usado para inserir dados em uma tabela?
- A) SELECT
- B) DELETE
- C) INSERT INTO
- D) UPDATE
- Resposta Correta: C) INSERT INTO

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
- Criando a classe FicharioDB
- 12 minutos
- Link para tarefa: https://cursos.alura.com.br/course/windows-forms-csharp-introducao-banco-de-dados/task/76493
- A classe FicharioDB encapsula a lógica de interação com o banco de dados, centralizando operações como inserção, exclusão e atualização de dados. Ela simplifica o acesso ao banco, organizando melhor o código.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- Definição da linguagem SQL
- 13 minutos
- Link para tarefa: https://cursos.alura.com.br/course/windows-forms-csharp-introducao-banco-de-dados/task/76494
- A linguagem SQL (Structured Query Language) é usada para gerenciar e manipular bancos de dados relacionais. Ela permite realizar operações como inserção, atualização, exclusão e consulta de dados de forma eficiente.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- Comandos SQL
- 11 minutos
- Link para tarefa: https://cursos.alura.com.br/course/windows-forms-csharp-introducao-banco-de-dados/task/76495
- Comandos SQL são instruções utilizadas para manipular dados em um banco. Incluem "SELECT" para consultas, "INSERT" para inserção, "UPDATE" para atualização, e "DELETE" para exclusão de registros.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 20

- DESENVOLVIMENTO DE SISTEMAS
- Comandos de inclusão na classe
- 9 minutos
- Link para tarefa: https://cursos.alura.com.br/course/windows-forms-csharp-introducao-banco-de-dados/task/76496
- Os comandos de inclusão na classe permitem inserir novos registros no banco de dados. Utilizam o SQL "INSERT INTO" dentro de métodos, passando valores para colunas específicas e salvando as informações corretamente.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 21

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje
- Você aprendeu a executar comandos SQL em um Windows Forms utilizando a classe FicharioDB. Exploramos como comandos SQL funcionam, focamos na inclusão de clientes no banco de dados e vimos exemplos práticos de código. Agora você pode executar consultas e manipular dados diretamente de sua aplicação!

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

_Fonte: AULA 87_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

ATIVIDADE AULA 87

Questão 1

O que a função ExecuteNonQuery() faz no código?

A) Executa uma consulta SQL que retorna dados

B) Executa um comando SQL sem retornar dados

C) Exclui dados do banco de dados

D) Atualiza os dados sem usar parâmetros

Resposta Correta: B) Executa um comando SQL sem retornar dados.

Explicação: O método ExecuteNonQuery() é usado para comandos que não retornam dados, como INSERT, UPDATE, e DELETE.

Questão 2

Qual comando SQL é usado para modificar dados existentes em uma tabela?

A) INSERT INTO

B) UPDATE

C) DELETE

D) SELECT

Resposta Correta: B) UPDATE

Explicação: O comando UPDATE é usado para modificar registros existentes em uma tabela no banco de dados.
