---
titulo: "Implementando as classes de dado"
tipo: rco-seed
disciplina: programacao-no-desenvolvimento-de-sistemas
sigla_rco: PDS
trimestre: 3
ordem_rco: 93
serie: 3
aula_rco: "Aula 93"
slides: 25
tem_atividade: false
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/3TRI/93-implementando-as-classes-de-dado/93-implementando-as-classes-de-dado.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/3TRI/93-implementando-as-classes-de-dado/AULA 93_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Implementando as classes de dado

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO NO
- DESENVOLVIMENTO DE
- SISTEMAS
- 3ª SÉRIE
- Implementando as classes de dado
- Aula 93

_3 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- DESENVOLVIMENTO DE SISTEMAS
- Nesta aula, vamos:
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store
- Abordar como implementar métodos de inclusão, alteração, exclusão e busca de clientes usando classes de dados no Windows Forms.

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
- Exploramos a abordagem tradicional e funções de produtividade para gerenciamento de dados, discutindo a diferença entre abordagens relacionais e não relacionais, e criando métodos como ToInsert e ToUpdate para simplificar o código SQL nas classes.

_4 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Laura é responsável por gerenciar o cadastro de clientes de uma loja e deseja adicionar um novo recurso para buscar rapidamente os clientes cadastrados e editá-los sem precisar acessar cada registro individualmente.

_4 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Pergunta
- Duas Soluções Possíveis:
- Implementar métodos de busca, alteração e exclusão na classe Cliente para facilitar a manipulação dos dados diretamente no sistema.
- Adicionar cada novo cliente manualmente no banco de dados sem usar métodos específicos, utilizando comandos SQL diretamente.
- Quem sabe responde!

_5 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Solução 1 (Correta): Implementar métodos de busca, alteração e exclusão na classe Cliente para facilitar a manipulação dos dados diretamente no sistema.
- Solução 2 (Falsa): Adicionar cada novo cliente manualmente no banco de dados sem usar métodos específicos, utilizando comandos SQL diretamente.

_4 imagem(ns) no slide._

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- Implementação
- A implementação de classes de dados em um sistema ajuda a centralizar as operações de manipulação de dados, como inclusão, exclusão e atualização, permitindo que o desenvolvedor use métodos específicos para cada funcionalidade.

_4 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- Definição e Aplicação
- Classes de dados são estruturas de código que representam tabelas de um banco de dados e contêm métodos para gerenciar os dados, como inserir um novo registro ou buscar clientes. Essa abordagem melhora a organização e manutenção do código.

_4 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Importância
- A implementação de classes de dados é essencial para construir sistemas mais escaláveis e modularizados, tornando o gerenciamento de informações mais ágil e permitindo a reutilização de métodos de manipulação de dados.

_4 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- Uso
- Em um sistema de cadastro de clientes, por exemplo, métodos de classe como AdicionarCliente, ExcluirCliente, BuscarClientePorId e AtualizarCliente são criados para facilitar a interação com o banco de dados, permitindo operações de CRUD com eficiência.

_4 imagem(ns) no slide._

### Slide 13

- DESENVOLVIMENTO DE SISTEMAS
- Exemplo de código classe que faz a adição cliente, excluir cliente, buscar cliente, atualizar cliente.
- Utilize o visual studio comunity

_5 imagem(ns) no slide._

### Slide 14

- DESENVOLVIMENTO DE SISTEMAS
- Questão de fixação
- Qual é a principal vantagem de encapsular operações de banco de dados em métodos de classe?
- A) Reduzir o tamanho do banco de dados
- B) Facilitar a manutenção e reutilização do código
- C) Aumentar a quantidade de dados armazenados
- D) Permitir apenas a leitura dos dados
- Quem sabe responde!

_4 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- Resposta!
- Qual é a principal vantagem de encapsular operações de banco de dados em métodos de classe?
- A) Reduzir o tamanho do banco de dados
- B) Facilitar a manutenção e reutilização do código
- C) Aumentar a quantidade de dados armazenados
- D) Permitir apenas a leitura dos dados
- Resposta Correta: B

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
- Método de inclusão
- 7 minutos
- Link para tarefa: https://cursos.alura.com.br/course/windows-forms-csharp-banco-de-dados-sql-server/task/76589
- O método de inclusão é responsável por adicionar novos registros a uma tabela no banco de dados. Ele geralmente usa o comando SQL INSERT INTO e recebe valores a serem inseridos nos campos especificados.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- Função de busca de um cliente
- 10 minutos
- Link para tarefa: https://cursos.alura.com.br/course/windows-forms-csharp-banco-de-dados-sql-server/task/76590
- A função de busca de um cliente localiza e retorna os dados de um cliente específico no banco de dados com base em um critério, como ID ou nome, usando o comando SQL SELECT para obter as informações desejadas.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- Método de alteração
- 5 minutos
- Link para tarefa: https://cursos.alura.com.br/course/windows-forms-csharp-banco-de-dados-sql-server/task/76591
- O método de alteração atualiza os dados de um cliente existente no banco de dados utilizando o comando SQL UPDATE. Ele modifica informações específicas, como nome e endereço, com base em um identificador.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 20

- DESENVOLVIMENTO DE SISTEMAS
- Método de exclusão
- 4 minutos
- Link para tarefa: https://cursos.alura.com.br/course/windows-forms-csharp-banco-de-dados-sql-server/task/76592
- O método de exclusão remove um cliente do banco de dados utilizando o comando SQL DELETE. Ele identifica o registro a ser excluído por meio de um ID, apagando permanentemente o dado especificado.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 21

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje
- Implementamos classes de dados para gerenciar clientes em um banco de dados. Exploramos métodos como InserirCliente, AtualizarCliente, ExcluirCliente e BuscarClientePorId, discutindo como encapsular operações de manipulação de dados em métodos específicos. Isso torna a manutenção do sistema mais fácil e eficiente.

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

_Fonte: AULA 93_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

ATIVIDADE AULA 93

Questão 1

Qual dos seguintes métodos é usado para adicionar um novo cliente ao banco de dados?

A) BuscarClientePorId()

B) InserirCliente()

C) AtualizarCliente()

D) ExcluirCliente()

Resposta Correta: B. InserirCliente() é o método que insere um novo cliente no banco de dados.

Questão 2

Como o método ExcluirCliente() é implementado corretamente?

A) SELECT * FROM Clientes

B) DELETE FROM Clientes WHERE Id = {Id}

C) INSERT INTO Clientes VALUES ('Nome')

D) UPDATE Clientes SET Nome = ''

Resposta Correta: B. DELETE FROM Clientes WHERE Id = {Id} é a sintaxe correta para excluir um cliente com base no ID.
