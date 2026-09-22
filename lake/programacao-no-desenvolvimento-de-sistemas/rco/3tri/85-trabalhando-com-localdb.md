---
titulo: "Trabalhando com LocalDB"
tipo: rco-seed
disciplina: programacao-no-desenvolvimento-de-sistemas
sigla_rco: PDS
trimestre: 3
ordem_rco: 85
serie: 3
aula_rco: "Aula 85"
slides: 25
tem_atividade: false
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/3TRI/85-trabalhando-com-localdb/85-trabalhando-com-localdb.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/3TRI/85-trabalhando-com-localdb/AULA 85_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Trabalhando com LocalDB

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO NO
- DESENVOLVIMENTO DE
- SISTEMAS
- 3ª SÉRIE
- Trabalhando com LocalDB
- Aula 85

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
- Aprenderá como instalar e configurar o LocalDB, criar um banco de dados e suas tabelas, e conectar-se a uma fonte de dados no Windows Forms.

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
- Redesenhamos a estrutura das classes no projeto, otimizando a inclusão, busca, alteração e exclusão de clientes. Também resolvemos problemas relacionados a mensagens de erro e melhoramos a organização da listagem de clientes.

_4 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Lucas está desenvolvendo um sistema de gestão de clientes, mas precisa armazenar os dados localmente. Ele ouviu falar do LocalDB, mas não sabe como iniciar a configuração e conexão.

_4 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Pergunta
- Duas Soluções Possíveis:
- Lucas decide usar arquivos de texto para armazenar os dados dos clientes, achando que seria mais fácil.
- Lucas opta por usar o LocalDB, pois oferece uma solução robusta para armazenar e gerenciar dados de forma segura e eficiente, além de ser fácil de integrar com o Windows Forms.
- Quem sabe responde!

_5 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- A primeira solução não é adequada, pois arquivos de texto não garantem a segurança e consistência dos dados. O LocalDB é mais apropriado, pois oferece um banco de dados real com suporte a transações, segurança e escalabilidade.

_4 imagem(ns) no slide._

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- Visão Geral
- O LocalDB é uma versão compacta do SQL Server, ideal para desenvolvedores que precisam de um banco de dados leve, mas robusto. Ele pode ser usado localmente sem a necessidade de configurar um servidor completo.

_4 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- Definição e Aplicação
- O LocalDB é utilizado para criar e gerenciar bancos de dados locais. Ele é ideal para testes e desenvolvimento de pequenas aplicações que não exigem um servidor de banco de dados externo.

_4 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Importância
- O LocalDB facilita o desenvolvimento, permitindo que os desenvolvedores criem e gerenciem bancos de dados diretamente em seus ambientes locais, sem precisar de infraestrutura complexa. Ele é uma solução prática e eficiente para a persistência de dados.

_4 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- Uso
- Ao desenvolver aplicações como sistemas de cadastro ou controle de estoque, o LocalDB pode ser integrado ao Windows Forms para armazenar e gerenciar dados. Por exemplo, você pode criar um banco de dados para armazenar informações de clientes e produtos.

_4 imagem(ns) no slide._

### Slide 13

- DESENVOLVIMENTO DE SISTEMAS
- Exemplo de conexão com banco de dados
- Utilize o visual studio comunity

_5 imagem(ns) no slide._

### Slide 14

- DESENVOLVIMENTO DE SISTEMAS
- Questão de fixação
- O LocalDB é uma versão compacta de qual sistema de banco de dados?
- A) MySQL
- B) PostgreSQL
- C) SQL Server
- D) Oracle
- Quem sabe responde!

_4 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- Resposta!
- O LocalDB é uma versão compacta de qual sistema de banco de dados?
- A) MySQL
- B) PostgreSQL
- C) SQL Server
- D) Oracle
- Resposta Correta: C) SQL Server

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
- Instalando o LocalDB
- 6 minutos
- Link para tarefa: https://cursos.alura.com.br/course/windows-forms-csharp-introducao-banco-de-dados/task/76484
- O LocalDB é uma versão leve do SQL Server, fácil de instalar e usada para desenvolvimento local. Ele é instalado junto com o Visual Studio ou separadamente através do SQL Server Express, sem configuração complexa.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- Criando o banco
- 5 minutos
- Link para tarefa: https://cursos.alura.com.br/course/windows-forms-csharp-introducao-banco-de-dados/task/76485
- Para criar um banco de dados no LocalDB, você pode usar o SQL Server Management Studio (SSMS) ou o Visual Studio. Basta conectar ao LocalDB, executar o comando SQL CREATE DATABASE, e o banco será criado localmente.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- Criando a tabela do banco
- 7 minutos
- Link para tarefa: https://cursos.alura.com.br/course/windows-forms-csharp-introducao-banco-de-dados/task/76486
- Para criar uma tabela no banco de dados LocalDB, utilize o comando SQL CREATE TABLE. Defina os campos, seus tipos de dados e restrições, como PRIMARY KEY. Isso estrutura onde os dados serão armazenados.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 20

- DESENVOLVIMENTO DE SISTEMAS
- Criando a fonte de dados
- 4 minutos
- Link para tarefa: https://cursos.alura.com.br/course/windows-forms-csharp-introducao-banco-de-dados/task/76487
- Criar uma fonte de dados envolve conectar a aplicação ao banco, definindo a string de conexão e configurando a comunicação entre o Windows Forms e o banco de dados para que os dados sejam manipulados facilmente.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 21

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje
- Aprendemos a instalar e configurar o LocalDB no Visual Studio, criando o banco de dados e sua tabela. Também exploramos como conectar o LocalDB ao Windows Forms e gerenciar os dados de maneira eficaz. Esses conceitos são fundamentais para persistência de dados em projetos locais.

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

_Fonte: AULA 85_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

ATIVIDADE AULA 85

Questão 1

Qual a principal vantagem do LocalDB em comparação com arquivos de texto para armazenamento de dados?

A) Permite armazenar grandes volumes de dados com maior segurança.

B) É mais fácil de usar para iniciantes.

C) Não requer instalação de software.

D) Não precisa de um banco de dados relacional.

Resposta Correta: A) Permite armazenar grandes volumes de dados com maior segurança.

Questão 2

Qual comando é usado para inserir dados em uma tabela no banco de dados LocalDB?

A) UPDATE

B) DELETE

C) INSERT INTO

D) CREATE TABLE

Resposta Correta: C) INSERT INTO

Explicação: O comando INSERT INTO é utilizado para inserir novos registros em uma tabela de banco de dados.
