---
titulo: "Acessando o banco de dados"
tipo: rco-seed
disciplina: programacao-no-desenvolvimento-de-sistemas
sigla_rco: PDS
trimestre: 3
ordem_rco: 91
serie: 3
aula_rco: "Aula 91"
slides: 23
tem_atividade: false
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/3TRI/91-acessando-o-banco-de-dados/91-acessando-o-banco-de-dados.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/3TRI/91-acessando-o-banco-de-dados/AULA 91_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Acessando o banco de dados

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO NO
- DESENVOLVIMENTO DE
- SISTEMAS
- 3ª SÉRIE
- Acessando o banco de dados
- Aula 91

_3 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- DESENVOLVIMENTO DE SISTEMAS
- Nesta aula, vamos:
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store
- Explorar como conectar o Visual Studio ao SQL Server, configurar corretamente a string de conexão e desenvolver uma classe de acesso ao banco de dados.

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
- Abordamos como realizar operações básicas de CRUD com formulários, garantindo que os dados do usuário fossem manipulados de maneira segura e organizada no SQL Server. Hoje, daremos um passo à frente, explorando o acesso e conexão ao banco de dados.

_4 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Marina está desenvolvendo um sistema de gerenciamento de estoque para a escola. Ela criou as tabelas no SQL Server, mas ao tentar conectar seu formulário no Visual Studio ao banco de dados, percebe que a aplicação não encontra as informações, mostrando mensagens de erro sobre a string de conexão.

_4 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Pergunta
- Por que a aplicação de Marina não consegue acessar o banco de dados e como ajustar isso de maneira eficaz?
- Quem sabe responde!

_5 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- A aplicação de Marina pode não estar conseguindo se conectar devido a uma configuração incorreta da string de conexão no arquivo App.config. A string de conexão deve conter o caminho correto para o banco de dados, juntamente com o nome do servidor e as credenciais de acesso.

_4 imagem(ns) no slide._

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- Acesso ao banco
- O acesso ao banco de dados é uma parte essencial do desenvolvimento de software, permitindo que aplicativos armazenem e recuperem informações de maneira organizada e eficiente.

_4 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- Conexão
- Conectar uma aplicação ao banco de dados envolve criar uma string de conexão, configurar classes de acesso e métodos para executar comandos SQL, garantindo que a comunicação entre o aplicativo e o banco seja fluida.

_4 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Importância
- Sem uma conexão estável, a aplicação não consegue manipular os dados, tornando-se apenas uma interface vazia. Um bom controle do acesso ao banco permite otimizar a performance e a segurança dos dados.

_4 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- Uso
- Imagine um sistema de biblioteca onde você quer adicionar, editar e excluir registros de livros. A classe de acesso ao banco conecta a aplicação e executa esses comandos, garantindo que o sistema reflita as alterações em tempo real.

_4 imagem(ns) no slide._

### Slide 13

- DESENVOLVIMENTO DE SISTEMAS
- Este código demonstra uma maneira simples de abrir e fechar a conexão com o banco de dados, além de executar um comando SQL de inserção.
- Utilize o visual studio comunity

_5 imagem(ns) no slide._

### Slide 14

- DESENVOLVIMENTO DE SISTEMAS
- Questão de fixação
- Qual dos seguintes componentes é essencial para conectar uma aplicação ao banco de dados no Visual Studio?
- A) String de Conexão
- B) Classe Main
- C) Componente DataGridView
- D) Método InitializeComponent
- Quem sabe responde!

_4 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- Resposta!
- Qual dos seguintes componentes é essencial para conectar uma aplicação ao banco de dados no Visual Studio?
- A) String de Conexão
- B) Classe Main
- C) Componente DataGridView
- D) Método InitializeComponent
- Resposta Correta: A)

_3 imagem(ns) no slide._

### Slide 16

- DESENVOLVIMENTO DE SISTEMAS
- Atividade Prática na Plataforma Alura
- Na plataforma Alura vamos acessar o seguinte curso:
- A recomendação é que você continue esse curso extraclasse, pois ele traz um conteúdo essencial para compreender sobre o referido tema.
- Link para o curso: https://cursos.alura.com.br/course/windows-forms-csharp-banco-de-dados-sql-server

_6 imagem(ns) no slide._

### Slide 17

- DESENVOLVIMENTO DE SISTEMAS
- Criando a conexão do SQL Server no Visual Studio
- 7 minutos
- Link para tarefa: https://cursos.alura.com.br/course/windows-forms-csharp-banco-de-dados-sql-server/task/76578
- Criar a conexão do SQL Server no Visual Studio envolve configurar a string de conexão no App.config, definir o servidor e o banco de dados a ser acessado, e testar a conexão para garantir a comunicação correta.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- Criando a classe de acesso à base de dados
- 9 minutos
- Link para tarefa: https://cursos.alura.com.br/course/windows-forms-csharp-banco-de-dados-sql-server/task/76579
- Criar a classe de acesso à base de dados centraliza operações como inclusão, consulta, atualização e exclusão. Ela utiliza comandos SQL e a string de conexão para interagir com o banco, facilitando a manutenção.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje
- Aprendemos a importância de estabelecer corretamente a conexão entre um aplicativo Windows Forms e o SQL Server. Exploramos como criar a string de conexão e utilizar comandos SQL para manipular dados com segurança e eficiência.

_4 imagem(ns) no slide._

### Slide 20

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

### Slide 21

- DESENVOLVIMENTO DE SISTEMAS
- Referências (Imagens)
- Figuras e Imagens:
- https://www.flaticon.com/br
- https://www.istockphoto.com/br
- https://raw.githubusercontent.com/zbtang/React-Native-ViewPager/HEAD/imgs/dotIndicator.gif
- https://storyset.com

_3 imagem(ns) no slide._

### Slide 22

- DESENVOLVIMENTO DE SISTEMAS
- O RCO+Aulas é um projeto da Secretaria de Estado da Educação do Paraná e está em constante revisão. Todos os slides são de uso exclusivo dos professores da Rede Pública de Ensino, com a finalidade específica de aplicação em sala de aula, sendo totalmente vedada a publicização, reutilização, reprodução total ou parcial para quaisquer outros fins.

_4 imagem(ns) no slide._

### Slide 23

- DESENVOLVIMENTO DE SISTEMAS
- Esta publicação tem a cooperação entre a UNESCO e a Secretaria de Estado da Educação e do Esporte do Paraná no âmbito da parceria PRODOC 914BRZ1091, cujo objetivo é trazer soluções inovadoras de gestão da rede pública estadual de educação do Paraná para a melhoria da aprendizagem dos alunos. As indicações de nomes e a apresentação do material ao longo desta publicação não implicam a manifestação de qualquer opinião por parte da UNESCO a respeito da condição jurídica de qualquer país, território, cidade, região ou de suas autoridades, tampouco da delimitação de suas fronteiras ou limites As ideias e opiniões expressas nesta publicação são as dos autores e não refletem obrigatoriamente as da UNESCO nem comprometem a Organização.
- Cooperação Técnica

_4 imagem(ns) no slide._

## Outros documentos

_Fonte: AULA 91_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

ATIVIDADE AULA 91

Questão 1

Qual é o método utilizado para abrir uma conexão com o banco de dados no C#?

A) SqlConnection.Open()

B) SqlDataReader.Read()

C) SqlCommand.ExecuteReader()

D) SqlDataAdapter.Fill()

Resposta Correta: A)

Explicação: SqlConnection.Open() é o método usado para estabelecer a conexão com o banco de dados especificado na string de conexão.

Questão 2

Por que é importante fechar a conexão com o banco de dados após realizar operações?

A) Para evitar consumo excessivo de memória.

B) Para apagar dados automaticamente.

C) Para garantir que o banco de dados seja excluído.

D) Para evitar atualizações.

Resposta Correta: A)

Explicação: Manter a conexão aberta desnecessariamente pode consumir recursos e causar problemas de desempenho no sistema.
