---
titulo: "CRUD com formulário"
tipo: rco-seed
disciplina: programacao-no-desenvolvimento-de-sistemas
sigla_rco: PDS
trimestre: 3
ordem_rco: 89
serie: 3
aula_rco: "Aula 89"
slides: 23
tem_atividade: false
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/3TRI/89-crud-com-formulario/89-crud-com-formulario.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/3TRI/89-crud-com-formulario/AULA 89_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# CRUD com formulário

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO NO
- DESENVOLVIMENTO DE
- SISTEMAS
- 3ª SÉRIE
- CRUD com formulário
- Aula 89

_3 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- DESENVOLVIMENTO DE SISTEMAS
- Nesta aula, vamos:
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store
- Aprender a criar um CRUD completo em Windows Forms, utilizando comandos SQL para manipular dados.

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
- Aprendemos os comandos SQL mais importantes, como SELECT, INSERT, UPDATE e DELETE. Agora, vamos aplicar esses comandos diretamente em um sistema CRUD com Windows Forms, onde será possível gerenciar dados diretamente de um formulário interativo.

_4 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Mariana precisa criar um sistema de cadastro de clientes, onde possa incluir, editar e excluir clientes da base de dados de sua empresa. Ela já conseguiu criar o formulário, mas não sabe como integrar o banco de dados.

_4 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Pergunta
- Duas Soluções Possíveis:
- Mariana pode usar SQL diretamente no código, criando comandos para manipular os dados do cliente com o botão de salvar e exibir informações em campos de texto.
- Mariana tenta salvar os dados manualmente sem uma conexão com o banco de dados, criando apenas arquivos locais no seu computador para armazenar informações.
- Quem sabe responde!

_4 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- A solução correta é a melhor escolha, pois usar SQL em um sistema de banco de dados permite que os dados sejam armazenados de maneira segura e eficiente, e que possam ser acessados ou modificados posteriormente.

_4 imagem(ns) no slide._

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- CRUD é um acrônimo para Create, Read, Update, Delete — operações fundamentais em qualquer sistema de banco de dados. Em um Windows Forms, essas operações são feitas através de botões e campos de texto que interagem com o banco de dados por meio de comandos SQL.

_4 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- CRUD é importante para manipular dados no dia a dia, seja para inserir um novo registro, ler dados existentes, atualizar informações ou deletar registros antigos. Cada operação CRUD é essencial para manter uma base de dados organizada e atualizada.

_4 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Manipular dados com eficiência garante a consistência e integridade da informação. Um sistema CRUD bem implementado evita erros, permite mudanças rápidas e ajuda a empresa a manter seus registros organizados.

_4 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- Em um formulário Windows Forms, os comandos SQL são executados diretamente em botões, como “Salvar”, “Atualizar”, “Excluir”. O usuário pode inserir ou alterar informações e ver os dados refletidos no banco de dados em tempo real.

_4 imagem(ns) no slide._

### Slide 13

- DESENVOLVIMENTO DE SISTEMAS
- Neste exemplo, temos um método para inserir dados em uma base de dados.
- Utilize o visual studio comunity

_5 imagem(ns) no slide._

### Slide 14

- DESENVOLVIMENTO DE SISTEMAS
- Questão de fixação
- O que significa CRUD?
- A) Codificar, Rodar, Usar, Desligar
- B) Criar, Ler, Atualizar, Deletar
- C) Copiar, Recortar, Usar, Deletar
- D) Colar, Renomear, Usar, Desligar
- Quem sabe responde!

_4 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- Resposta!
- O que significa CRUD?
- A) Codificar, Rodar, Usar, Desligar
- B) Criar, Ler, Atualizar, Deletar
- C) Copiar, Recortar, Usar, Deletar
- D) Colar, Renomear, Usar, Desligar
- Resposta Correta: B. CRUD representa as principais operações de um banco de dados.

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
- Modificando a classe Cliente
- 7 minutos
- Link para tarefa: https://cursos.alura.com.br/course/windows-forms-csharp-introducao-banco-de-dados/task/76501
- Modificar a classe Cliente envolve ajustar suas propriedades ou métodos para atender às novas necessidades do sistema, como incluir validações adicionais, novos campos ou otimizar o código para melhor desempenho.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- Modificando o código fonte do formulário
- 9 minutos
- Link para tarefa: https://cursos.alura.com.br/course/windows-forms-csharp-introducao-banco-de-dados/task/76502
- Modificar o código-fonte do formulário envolve ajustar eventos, adicionar novos controles ou atualizar lógicas de interface. Essas mudanças melhoram a interação do usuário e a funcionalidade geral do sistema.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje
- Como construir um CRUD completo usando Windows Forms e SQL. Exploramos como criar, ler, atualizar e deletar dados de uma base de dados, aplicando esses conceitos diretamente em formulários interativos. Isso fornece uma base sólida para o desenvolvimento de sistemas com interfaces amigáveis e eficientes.

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

_Fonte: AULA 89_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

ATIVIDADE AULA 89

Questão 1

Qual comando SQL é utilizado para buscar todos os clientes de uma tabela?

A) SELECT * FROM Clientes

B) INSERT INTO Clientes

C) DELETE FROM Clientes

D) UPDATE Clientes SET

Resposta Correta: A. O comando SELECT * FROM Clientes é utilizado para buscar todos os clientes presentes na tabela.

Questão 2

Qual comando SQL é utilizado para alterar o nome de um cliente no banco de dados?

A) SELECT Nome FROM Clientes

B) INSERT INTO Nome

C) UPDATE Clientes SET Nome

D) DELETE Nome FROM Clientes

Resposta Correta: C. O comando UPDATE Clientes SET Nome é utilizado para alterar o nome de um cliente no banco de dados.
