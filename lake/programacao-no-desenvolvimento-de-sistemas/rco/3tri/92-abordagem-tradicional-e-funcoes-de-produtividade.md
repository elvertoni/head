---
titulo: "Abordagem tradicional e funções de produtividade"
tipo: rco-seed
disciplina: programacao-no-desenvolvimento-de-sistemas
sigla_rco: PDS
trimestre: 3
ordem_rco: 92
serie: 3
aula_rco: "Aula 92"
slides: 22
tem_atividade: false
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/3TRI/92-abordagem-tradicional-e-funcoes-de-produtividade/92-abordagem-tradicional-e-funcoes-de-produtividade.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/3TRI/92-abordagem-tradicional-e-funcoes-de-produtividade/AULA 92_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Abordagem tradicional e funções de produtividade

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO NO
- DESENVOLVIMENTO DE
- SISTEMAS
- 3ª SÉRIE
- Abordagem tradicional e funções de produtividade
- Aula 92

_3 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- DESENVOLVIMENTO DE SISTEMAS
- Nesta aula, vamos:
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store
- Explorar as diferenças entre bancos de dados relacionais.

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
- Focamos em como acessar um banco de dados e estruturar uma aplicação que se conecte ao SQL Server, utilizando classes e strings de conexão. Hoje, vamos aprofundar a automação e a produtividade.

_4 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Mariana é uma desenvolvedora iniciante que está construindo uma aplicação para cadastro de produtos. Ela precisa decidir se usa um banco de dados relacional ou não-relacional para armazenar as informações dos produtos e ainda deseja automatizar funções de inclusão e atualização.

_4 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Pergunta
- Duas Soluções Possíveis:
- Banco Relacional: Ideal para dados estruturados com relacionamentos entre diferentes tabelas. Mariana pode usar o SQL Server e desenvolver funções ToInsert e ToUpdate.
- Banco Não-Relacional: Melhor para dados não estruturados e grandes volumes de informações que mudam constantemente. Mariana pode usar o MongoDB e automatizar suas funções diretamente com JSON.
- Quem sabe responde!

_4 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- A solução relacional é a mais indicada quando se trabalha com dados que possuem dependências entre tabelas, como informações de produtos vinculadas a fornecedores e categorias.
- A solução não-relacional é melhor quando não há necessidade de seguir um esquema rígido e o foco é flexibilidade e velocidade de inserção de dados.

_4 imagem(ns) no slide._

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- Integração
- A produtividade em desenvolvimento de software depende de estratégias que facilitem a manipulação de dados e a integração de diferentes fontes. Com a automação e o uso adequado de bancos de dados, é possível criar soluções mais eficientes.

_4 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- Definição e Aplicação
- Bancos Relacionais: Usam tabelas para armazenar dados e são organizados com chaves primárias e estrangeiras.
- Bancos Não-Relacionais: Trabalham com documentos, como o JSON, que são flexíveis e ideais para grandes volumes de dados com menos rigidez.

_4 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Importância
- Escolher entre um banco relacional e não-relacional impacta diretamente a performance e manutenção do sistema. Com funções automatizadas (ToInsert, ToUpdate), é possível reduzir o esforço manual de manipulação de dados.

_4 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- Uso
- ToInsert: Gera automaticamente uma query de inserção com base nos atributos da classe.
- ToUpdate: Cria comandos para atualizar campos específicos do banco.
- DataRow para Classe: Facilita a conversão de um registro de tabela em um objeto de classe, agilizando o trabalho de recuperação de dados.

_4 imagem(ns) no slide._

### Slide 13

- DESENVOLVIMENTO DE SISTEMAS
- Classe Cliente gera comandos SQL para inserir e atualizar dados no banco usando os métodos ToInsert e ToUpdate com base nas propriedades do objeto.
- Utilize o visual studio comunity

_5 imagem(ns) no slide._

### Slide 14

- DESENVOLVIMENTO DE SISTEMAS
- Questão de fixação
- Qual é a principal vantagem do uso de ToInsert e ToUpdate em classes de banco de dados?
- A) Melhorar a formatação dos textos no banco
- B) Automatizar a criação de comandos SQL
- C) Evitar redundâncias de código na aplicação
- D) A e B estão corretas
- Quem sabe responde!

_4 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- Resposta!
- Qual é a principal vantagem do uso de ToInsert e ToUpdate em classes de banco de dados?
- A) Melhorar a formatação dos textos no banco
- B) Automatizar a criação de comandos SQL
- C) Evitar redundâncias de código na aplicação
- D) A e B estão corretas
- Resposta correta: B)

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
- Abordagem relacional x Não relacional
- 11 minutos
- Link para tarefa: https://cursos.alura.com.br/course/windows-forms-csharp-banco-de-dados-sql-server/task/76583
- A abordagem relacional organiza dados em tabelas e usa SQL para gerenciá-los. Já a abordagem não relacional (NoSQL) armazena dados de forma flexível, como documentos, ideal para estruturas não rígidas.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje
- Aprendemos a importância de estabelecer corretamente a conexão entre um aplicativo Windows Forms e o SQL Server. Exploramos como criar a string de conexão e utilizar comandos SQL para manipular dados com segurança e eficiência.

_4 imagem(ns) no slide._

### Slide 19

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

### Slide 20

- DESENVOLVIMENTO DE SISTEMAS
- Referências (Imagens)
- Figuras e Imagens:
- https://www.flaticon.com/br
- https://www.istockphoto.com/br
- https://raw.githubusercontent.com/zbtang/React-Native-ViewPager/HEAD/imgs/dotIndicator.gif
- https://storyset.com

_3 imagem(ns) no slide._

### Slide 21

- DESENVOLVIMENTO DE SISTEMAS
- O RCO+Aulas é um projeto da Secretaria de Estado da Educação do Paraná e está em constante revisão. Todos os slides são de uso exclusivo dos professores da Rede Pública de Ensino, com a finalidade específica de aplicação em sala de aula, sendo totalmente vedada a publicização, reutilização, reprodução total ou parcial para quaisquer outros fins.

_4 imagem(ns) no slide._

### Slide 22

- DESENVOLVIMENTO DE SISTEMAS
- Esta publicação tem a cooperação entre a UNESCO e a Secretaria de Estado da Educação e do Esporte do Paraná no âmbito da parceria PRODOC 914BRZ1091, cujo objetivo é trazer soluções inovadoras de gestão da rede pública estadual de educação do Paraná para a melhoria da aprendizagem dos alunos. As indicações de nomes e a apresentação do material ao longo desta publicação não implicam a manifestação de qualquer opinião por parte da UNESCO a respeito da condição jurídica de qualquer país, território, cidade, região ou de suas autoridades, tampouco da delimitação de suas fronteiras ou limites As ideias e opiniões expressas nesta publicação são as dos autores e não refletem obrigatoriamente as da UNESCO nem comprometem a Organização.
- Cooperação Técnica

_4 imagem(ns) no slide._

## Outros documentos

_Fonte: AULA 92_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

ATIVIDADE AULA 92

Questão 1

Qual é a diferença entre bancos de dados relacionais e não-relacionais?

A) Relacionais usam tabelas e não-relacionais usam documentos.

B) Relacionais são mais rápidos.

C) Não-relacionais não possuem estrutura fixa.

D) A e C estão corretas.

Resposta correta: D) A e C estão corretas.

Comentário: Bancos relacionais seguem um esquema rígido, enquanto os não-relacionais têm flexibilidade para armazenar dados sem estrutura fixa.

Questão 2

Quando é mais indicado usar funções como ToInsert e ToUpdate?

A) Para bancos de dados complexos.

B) Para automatizar tarefas repetitivas de manipulação de dados.

C) Para converter dados em arquivos de texto.

D) Para evitar interações manuais com o banco.

Resposta correta: B) Para automatizar tarefas repetitivas de manipulação de dados.

Comentário: Essas funções automatizam a geração de comandos SQL, economizando tempo e evitando erros humanos.
