---
titulo: "Redesenhando as classes"
tipo: rco-seed
disciplina: programacao-no-desenvolvimento-de-sistemas
sigla_rco: PDS
trimestre: 3
ordem_rco: 84
serie: 3
aula_rco: "Aula 84"
slides: 29
tem_atividade: false
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/3TRI/84-redesenhando-as-classes/84-redesenhando-as-classes.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PDS/3TRI/84-redesenhando-as-classes/AULA 84_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Redesenhando as classes

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO NO
- DESENVOLVIMENTO DE
- SISTEMAS
- 3ª SÉRIE
- Redesenhando as classes
- Aula 84

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
- Aprender a redesenhar o fluxo de funcionalidades nas classes, ajustando a ordem da inclusão, busca, alteração e exclusão de dados no Windows Forms.

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
- Aprendemos como listar clientes no formulário e exibir seus dados detalhados. Trabalhamos com métodos que buscaram informações no banco de dados e preencheram o formulário de edição. Agora, vamos redesenhar e otimizar esses processos.

_4 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Alice, uma desenvolvedora iniciante, notou que, ao tentar excluir um cliente, uma mensagem de erro inesperada apareceu. Isso dificultou sua operação, pois o cliente não foi excluído corretamente.

_4 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Pergunta
- Como Alice pode ajustar seu código para garantir que a exclusão do cliente seja processada corretamente sem apresentar erros inesperados?
- Quem sabe responde!

_5 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Alice precisa revisar sua lógica de exclusão, certificando-se de que a conexão com o banco de dados está sendo fechada adequadamente e que a condição de exclusão está correta, lidando com erros com mensagens claras.

_4 imagem(ns) no slide._

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- Visão Geral
- Redesenhar classes envolve reorganizar o fluxo de execução do programa, tornando-o mais eficiente e organizado. No Windows Forms, classes são responsáveis por gerenciar ações como inclusão, busca, alteração e exclusão de clientes.

_4 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- Definição e Aplicação
- Reorganizar classes significa melhorar a forma como elas interagem com o banco de dados e como processam informações. Por exemplo, ajustar o método de inclusão para trabalhar melhor com JSON ou redesenhar a busca para evitar erros.

_4 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Importância
- É essencial garantir que o sistema funcione de maneira eficiente e sem erros. Redesenhar classes melhora o desempenho, a legibilidade do código e a experiência do usuário, além de resolver problemas críticos como mensagens de erro.

_4 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- Uso
- Na prática, você reorganiza a lógica de inclusão de clientes, garantindo que todos os dados sejam verificados antes de serem salvos no banco. Ao redesenhar o processo de exclusão, lidamos com a prevenção de erros.

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
- MainForm.cs
- Utilize o visual studio comunity

_5 imagem(ns) no slide._

### Slide 16

- DESENVOLVIMENTO DE SISTEMAS
- MainForm.
- Designer.cs
- Utilize o visual studio comunity

_5 imagem(ns) no slide._

### Slide 17

- DESENVOLVIMENTO DE SISTEMAS
- MainForm.
- Designer.cs
- Utilize o visual studio comunity

_5 imagem(ns) no slide._

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- MainForm.
- Designer.cs
- Utilize o visual studio comunity

_5 imagem(ns) no slide._

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- Program.cs
- Utilize o visual studio comunity

_5 imagem(ns) no slide._

### Slide 20

- DESENVOLVIMENTO DE SISTEMAS
- Questão de fixação
- Qual é a principal vantagem de redesenhar as classes em um projeto C#?
- A) Melhorar a performance do banco de dados
- B) Aumentar a velocidade de compilação
- C) Tornar o código mais organizado e eficiente
- D) Criar um novo banco de dados
- Quem sabe responde!

_4 imagem(ns) no slide._

### Slide 21

- DESENVOLVIMENTO DE SISTEMAS
- Resposta!
- Qual é a principal vantagem de redesenhar as classes em um projeto C#?
- A) Melhorar a performance do banco de dados
- B) Aumentar a velocidade de compilação
- C) Tornar o código mais organizado e eficiente
- D) Criar um novo banco de dados
- Correta : C

_3 imagem(ns) no slide._

### Slide 22

- DESENVOLVIMENTO DE SISTEMAS
- Atividade Prática na Plataforma Alura
- Na plataforma Alura vamos acessar o seguinte curso:
- A recomendação é que você continue esse curso extraclasse, pois ele traz um conteúdo essencial para compreender sobre o referido tema.
- Link para o curso: https://cursos.alura.com.br/course/windows-forms-csharp-manipulacao-dados

_6 imagem(ns) no slide._

### Slide 23

- DESENVOLVIMENTO DE SISTEMAS
- Trocando a ordem das classes
- 4 minutos
- Link para tarefa: https://cursos.alura.com.br/course/windows-forms-csharp-manipulacao-dados/task/72494
- Organizar classes por ordem de importância ou dependência ajuda desenvolvedores a navegar mais rapidamente e compreender melhor a lógica do programa, garantindo um fluxo lógico.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 24

- DESENVOLVIMENTO DE SISTEMAS
- Redesenhando a inclusão
- 12 minutos
- Link para tarefa: https://cursos.alura.com.br/course/windows-forms-csharp-manipulacao-dados/task/72495
- Redesenhar a inclusão envolve otimizar o processo de adicionar novos clientes ao sistema. Isso pode incluir ajustar a validação de dados, melhorar a interface de usuário para entradas mais intuitivas.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 25

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje
- Exploramos o redesenho de classes e métodos em um sistema Windows Forms, focando na inclusão, busca, alteração e exclusão de clientes. Aprendemos como melhorar a estrutura do código, garantindo eficiência e clareza no tratamento de erros. Isso fortalece a manutenção e usabilidade do sistema.

_4 imagem(ns) no slide._

### Slide 26

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

### Slide 27

- DESENVOLVIMENTO DE SISTEMAS
- Referências (Imagens)
- Figuras e Imagens:
- https://www.flaticon.com/br
- https://www.istockphoto.com/br
- https://raw.githubusercontent.com/zbtang/React-Native-ViewPager/HEAD/imgs/dotIndicator.gif
- https://storyset.com

_3 imagem(ns) no slide._

### Slide 28

- DESENVOLVIMENTO DE SISTEMAS
- O RCO+Aulas é um projeto da Secretaria de Estado da Educação do Paraná e está em constante revisão. Todos os slides são de uso exclusivo dos professores da Rede Pública de Ensino, com a finalidade específica de aplicação em sala de aula, sendo totalmente vedada a publicização, reutilização, reprodução total ou parcial para quaisquer outros fins.

_4 imagem(ns) no slide._

### Slide 29

- DESENVOLVIMENTO DE SISTEMAS
- Esta publicação tem a cooperação entre a UNESCO e a Secretaria de Estado da Educação e do Esporte do Paraná no âmbito da parceria PRODOC 914BRZ1091, cujo objetivo é trazer soluções inovadoras de gestão da rede pública estadual de educação do Paraná para a melhoria da aprendizagem dos alunos. As indicações de nomes e a apresentação do material ao longo desta publicação não implicam a manifestação de qualquer opinião por parte da UNESCO a respeito da condição jurídica de qualquer país, território, cidade, região ou de suas autoridades, tampouco da delimitação de suas fronteiras ou limites As ideias e opiniões expressas nesta publicação são as dos autores e não refletem obrigatoriamente as da UNESCO nem comprometem a Organização.
- Cooperação Técnica

_4 imagem(ns) no slide._

## Outros documentos

_Fonte: AULA 84_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

ATIVIDADE AULA 84

Questão 1

Qual dos itens abaixo é essencial ao redesenhar um método de inclusão?

A) Fechar a aplicação

B) Verificar os dados antes de salvar

C) Enviar um e-mail de confirmação

D) Excluir os dados do cliente

Correta B

Comentário: Verificar os dados antes de salvar é fundamental para garantir a integridade da inclusão.

Questão 2

Qual é o objetivo de redesenhar a exclusão de clientes?

A) Evitar duplicidades

B) Garantir que os dados sejam removidos corretamente

C) Adicionar mais clientes ao sistema

D) Melhorar a conexão do banco de dados

Correta B

Comentário: O objetivo é assegurar que o processo de exclusão funcione corretamente, removendo o cliente sem erros.
