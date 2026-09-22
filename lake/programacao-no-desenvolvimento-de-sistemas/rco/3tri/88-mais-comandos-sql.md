---
titulo: "Mais comandos SQL"
tipo: rco-seed
disciplina: programacao-no-desenvolvimento-de-sistemas
sigla_rco: PDS
trimestre: 3
ordem_rco: 88
serie: 3
aula_rco: "Aula 88"
slides: 25
tem_atividade: false
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/3TRI/88-mais-comandos-sql/88-mais-comandos-sql.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/3TRI/88-mais-comandos-sql/AULA 88_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Mais comandos SQL

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO NO
- DESENVOLVIMENTO DE
- SISTEMAS
- 3ª SÉRIE
- Mais comandos SQL
- Aula 88

_3 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- DESENVOLVIMENTO DE SISTEMAS
- Nesta aula, vamos:
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store
- Aprender como usar comandos SQL para buscar, alterar e excluir registros de um banco de dados.

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
- Aprendemos a executar comandos SQL no Windows Forms, incluindo como inserir dados no banco de dados e encapsular o acesso ao banco usando classes. Hoje, vamos expandir esse conhecimento com comandos para buscar, alterar e excluir clientes.

_4 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Ana, uma desenvolvedora iniciante, precisa implementar um sistema de busca e exclusão de clientes no seu sistema de cadastro, mas está incerta sobre como construir as consultas SQL corretas.

_4 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Pergunta
- Como Ana deve construir seus comandos SQL para buscar e excluir clientes de forma eficiente e segura?
- Quem sabe responde!

_5 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Ana deve utilizar os comandos SQL SELECT para buscar clientes e DELETE para excluí-los, garantindo que o comando DELETE seja acompanhado de uma confirmação e de uma condição de filtro para não apagar dados por engano.

_4 imagem(ns) no slide._

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- Comandos SQL de busca, alteração e exclusão são fundamentais em qualquer sistema que manipula dados. Essas operações garantem a integridade e atualização das informações no banco de dados.

_4 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- Definição e Aplicação
- Comandos de Busca (SELECT): Usados para buscar informações de uma tabela com base em condições.
- Comandos de Alteração (UPDATE): Permitem modificar dados existentes.
- Comandos de Exclusão (DELETE): Removem registros com base em critérios específicos.

_4 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Esses comandos são a base da manipulação de dados em qualquer aplicação. Sem eles, não seria possível atualizar, remover ou recuperar informações essenciais de um banco de dados.

_4 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- Em sistemas de cadastro de clientes, como um aplicativo de gestão de vendas, é comum os usuários buscarem informações de um cliente, atualizarem seu endereço ou telefone e, eventualmente, excluírem o cadastro de um cliente antigo.

_4 imagem(ns) no slide._

### Slide 13

- DESENVOLVIMENTO DE SISTEMAS
- Neste exemplo, temos um método para busca e outro para excluir um cliente pelo ID na query
- Utilize o visual studio comunity

_5 imagem(ns) no slide._

### Slide 14

- DESENVOLVIMENTO DE SISTEMAS
- Questão de fixação
- Qual comando SQL é usado para buscar todos os registros de uma tabela?
- A) INSERT
- B) SELECT
- C) UPDATE
- D) DELETE
- Quem sabe responde!

_4 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- Resposta!
- Qual comando SQL é usado para buscar todos os registros de uma tabela?
- A) INSERT
- B) SELECT
- C) UPDATE
- D) DELETE
- Resposta Correta: B) SELECT

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
- Comandos de busca de um cliente
- 10 minutos
- Link para tarefa: https://cursos.alura.com.br/course/windows-forms-csharp-introducao-banco-de-dados/task/76497
- Os comandos de busca de um cliente, geralmente utilizando o SQL SELECT, são fundamentais para recuperar informações específicas de um cliente em um banco de dados, com base em critérios como o ID ou nome.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- Buscar todos os clientes
- 8 minutos
- Link para tarefa: https://cursos.alura.com.br/course/windows-forms-csharp-introducao-banco-de-dados/task/76498
- O comando SQL para buscar todos os clientes (SELECT * FROM Clientes) permite recuperar todas as informações armazenadas na tabela de clientes. Isso é útil para listar ou visualizar todos os registros existentes.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- Apagando um cliente
- 5 minutos
- Link para tarefa: https://cursos.alura.com.br/course/windows-forms-csharp-introducao-banco-de-dados/task/76499
- O comando SQL para apagar um cliente (DELETE FROM Clientes WHERE Id = @Id) remove o registro correspondente do banco de dados. Esse comando é usado com cautela, pois a exclusão é permanente e irreversível.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 20

- DESENVOLVIMENTO DE SISTEMAS
- Alteração do cliente
- 5 minutos
- Link para tarefa: https://cursos.alura.com.br/course/windows-forms-csharp-introducao-banco-de-dados/task/76500
- A alteração de um cliente no banco de dados é feita com o comando SQL UPDATE, que atualiza os campos especificados. Exemplo: UPDATE Clientes SET Nome = @Nome WHERE Id = @Id. Isso permite modificar dados específicos de um cliente sem afetar o restante das informações.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 21

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje
- Aprendemos como usar comandos SQL para buscar, alterar e excluir registros de um banco de dados dentro de um aplicativo Windows Forms. Essas operações são essenciais para manter um sistema de gerenciamento de dados atualizado e funcional.

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

_Fonte: AULA 88_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

ATIVIDADE AULA 88

Questão 1

Qual comando SQL deve ser usado para alterar o nome de um cliente em um banco de dados?

A) SELECT

B) UPDATE

C) INSERT

D) DELETE

Resposta Correta: B) UPDATE

Explicação: O comando UPDATE é utilizado para modificar registros em uma tabela existente.

Questão 2

Qual é a vantagem de adicionar parâmetros em um comando SQL ao buscar dados?

A) Evita a repetição de dados

B) Melhora a performance do sistema

C) Previne injeção de SQL e garante a segurança dos dados

D) Diminui o tamanho do banco de dados

Resposta Correta: C) Previne injeção de SQL e garante a segurança dos dados

Explicação: Usar parâmetros ajuda a evitar injeção de SQL, tornando a aplicação mais segura ao lidar com dados fornecidos por usuários.
