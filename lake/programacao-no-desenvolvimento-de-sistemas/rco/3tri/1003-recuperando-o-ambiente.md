---
titulo: "Recuperando o ambiente"
tipo: rco-seed
disciplina: programacao-no-desenvolvimento-de-sistemas
sigla_rco: PDS
trimestre: 3
ordem_rco: 1003
serie: 3
aula_rco: "Aula Nivelamento 2"
slides: 27
tem_atividade: false
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/3TRI/1003-recuperando-o-ambiente/1003-recuperando-o-ambiente.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/3TRI/1003-recuperando-o-ambiente/AULA NIV2_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Recuperando o ambiente

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO NO
- DESENVOLVIMENTO DE
- SISTEMAS
- 3ª SÉRIE
- Recuperando o ambiente
- Aula Nivelamento 2

_3 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- DESENVOLVIMENTO DE SISTEMAS
- Nesta aula, vamos:
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store
- Aprender como configurar e conectar um projeto Windows Forms a um banco de dados.

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
- Trabalhamos com JSON e classes, entendendo como manipular dados de arquivos JSON e como isso pode ser aplicado no projeto de classes em C#. Hoje, avançaremos para a persistência desses dados em um banco de dados, tornando o sistema mais robusto.

_4 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Mariana está desenvolvendo um sistema de cadastro de clientes. Ela percebe que, a cada vez que fecha a aplicação, as informações dos clientes são perdidas, e ela precisa inseri-las novamente ao reiniciar. Para resolver o problema, Mariana decide utilizar um banco de dados, mas não sabe por onde começar.

_4 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Pergunta
- Como Mariana pode configurar o seu sistema para que os dados inseridos pelos usuários sejam salvos permanentemente no banco de dados?
- Quem sabe responde!

_5 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Mariana deve aprender a conectar o formulário da aplicação ao banco de dados e implementar métodos para salvar, atualizar e recuperar dados do banco, garantindo persistência das informações.

_4 imagem(ns) no slide._

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- Visão Geral
- Persistência de dados refere-se à capacidade de um sistema de manter informações, mesmo após ser desligado. Em aplicações Windows Forms, isso é feito com a integração de um banco de dados.

_4 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- Definição e Aplicação
- Persistir dados significa salvá-los permanentemente no banco de dados. Isso envolve conectar a aplicação ao banco de dados, enviar comandos SQL e lidar com o retorno desses comandos.

_4 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Importância
- Sem persistência de dados, os usuários teriam que reinserir as informações a cada uso da aplicação. Armazenar os dados em um banco de dados torna o sistema muito mais funcional e confiável.

_4 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- Uso
- Na prática, os sistemas precisam armazenar informações importantes como cadastro de clientes, produtos, pedidos e outras informações de negócio. Utilizando a persistência de dados, as informações são mantidas para uso futuro.

_4 imagem(ns) no slide._

### Slide 13

- DESENVOLVIMENTO DE SISTEMAS
- MainForm.cs
- Utilize o visual studio comunity

_5 imagem(ns) no slide._

### Slide 14

- DESENVOLVIMENTO DE SISTEMAS
- MainForm.cs
- Utilize o visual studio comunity

_5 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- MainForm
- .Designer.cs
- Utilize o visual studio comunity

_5 imagem(ns) no slide._

### Slide 16

- DESENVOLVIMENTO DE SISTEMAS
- MainForm
- .Designer.cs
- Utilize o visual studio comunity

_5 imagem(ns) no slide._

### Slide 17

- DESENVOLVIMENTO DE SISTEMAS
- MainForm
- .Designer.cs
- Utilize o visual studio comunity

_5 imagem(ns) no slide._

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- Program.cs
- Utilize o visual studio comunity

_5 imagem(ns) no slide._

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- Questão de fixação
- Qual é a função principal de um banco de dados em um sistema Windows Forms?
- A) Garantir que os dados sejam exibidos em tempo real
- B) Armazenar e organizar dados de forma persistente
- C) Melhorar a interface gráfica
- D) Limitar a quantidade de dados exibidos
- Quem sabe responde!

_4 imagem(ns) no slide._

### Slide 20

- DESENVOLVIMENTO DE SISTEMAS
- Resposta!
- Qual é a função principal de um banco de dados em um sistema Windows Forms?
- A) Garantir que os dados sejam exibidos em tempo real
- B) Armazenar e organizar dados de forma persistente
- C) Melhorar a interface gráfica
- D) Limitar a quantidade de dados exibidos
- Correta: B) Armazenar e organizar dados de forma persistente

_3 imagem(ns) no slide._

### Slide 21

- DESENVOLVIMENTO DE SISTEMAS
- Atividade Prática na Plataforma Alura
- Na plataforma Alura vamos acessar o seguinte curso:
- A recomendação é que você continue esse curso extraclasse, pois ele traz um conteúdo essencial para compreender sobre o referido tema.
- Link para o curso: https://cursos.alura.com.br/course/windows-forms-csharp-introducao-banco-de-dados

_6 imagem(ns) no slide._

### Slide 22

- DESENVOLVIMENTO DE SISTEMAS
- Entendendo um banco de dados
- 6 minutos
- Link para tarefa: https://cursos.alura.com.br/course/windows-forms-csharp-introducao-banco-de-dados/task/76483
- Um banco de dados é uma coleção organizada de dados que permite o armazenamento, gerenciamento e recuperação eficiente de informações. Ele é essencial para aplicações que precisam persistir dados de forma estruturada.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 23

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje
- Aprendemos a importância da persistência de dados e como integrá-la ao nosso sistema Windows Forms, além de aplicarmos esse conhecimento para conectar, salvar e recuperar informações de um banco de dados. Com isso, nossos sistemas se tornam mais robustos e confiáveis.

_4 imagem(ns) no slide._

### Slide 24

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

### Slide 25

- DESENVOLVIMENTO DE SISTEMAS
- Referências (Imagens)
- Figuras e Imagens:
- https://www.flaticon.com/br
- https://www.istockphoto.com/br
- https://raw.githubusercontent.com/zbtang/React-Native-ViewPager/HEAD/imgs/dotIndicator.gif
- https://storyset.com

_3 imagem(ns) no slide._

### Slide 26

- DESENVOLVIMENTO DE SISTEMAS
- O RCO+Aulas é um projeto da Secretaria de Estado da Educação do Paraná e está em constante revisão. Todos os slides são de uso exclusivo dos professores da Rede Pública de Ensino, com a finalidade específica de aplicação em sala de aula, sendo totalmente vedada a publicização, reutilização, reprodução total ou parcial para quaisquer outros fins.

_4 imagem(ns) no slide._

### Slide 27

- DESENVOLVIMENTO DE SISTEMAS
- Esta publicação tem a cooperação entre a UNESCO e a Secretaria de Estado da Educação e do Esporte do Paraná no âmbito da parceria PRODOC 914BRZ1091, cujo objetivo é trazer soluções inovadoras de gestão da rede pública estadual de educação do Paraná para a melhoria da aprendizagem dos alunos. As indicações de nomes e a apresentação do material ao longo desta publicação não implicam a manifestação de qualquer opinião por parte da UNESCO a respeito da condição jurídica de qualquer país, território, cidade, região ou de suas autoridades, tampouco da delimitação de suas fronteiras ou limites As ideias e opiniões expressas nesta publicação são as dos autores e não refletem obrigatoriamente as da UNESCO nem comprometem a Organização.
- Cooperação Técnica

_5 imagem(ns) no slide._

## Outros documentos

_Fonte: AULA NIV2_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

ATIVIDADE AULA NIV2

Questão 1

Qual comando SQL é utilizado para inserir novos dados em uma tabela do banco de dados?

A) SELECT

B) UPDATE

C) DELETE

D) INSERT

Resposta correta:

D) INSERT

O comando INSERT é utilizado para adicionar novos registros a uma tabela no banco de dados.

Questão 2

Para abrir uma conexão com o banco de dados no C#, qual classe do namespace System.Data.SqlClient é utilizada?

A) SqlReader

B) SqlCommand

C) SqlConnection

D) SqlAdapter

Resposta correta:

C) SqlConnection

A classe SqlConnection é responsável por estabelecer a conexão entre a aplicação e o banco de dados.
