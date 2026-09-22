---
titulo: "Validando a classe"
tipo: rco-seed
disciplina: programacao-no-desenvolvimento-de-sistemas
sigla_rco: PDS
trimestre: 2
ordem_rco: 77
serie: 3
aula_rco: "Aula 77"
slides: 31
tem_atividade: true
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PDS/2TRI/77-validando-a-classe/77-validando-a-classe.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PDS/2TRI/77-validando-a-classe/AULA 77_ATIVIDADE_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Validando a classe

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO NO
- DESENVOLVIMENTO DE
- SISTEMAS
- 3ª SÉRIE
- Validando a classe
- Aula 77

_3 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- DESENVOLVIMENTO DE SISTEMAS
- Nesta aula, vamos:
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store
- Aprender como garantir que os dados inseridos na classe Cliente estejam corretos e como utilizar bibliotecas para facilitar essa validação.

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
- Exploramos a criação da classe Cliente, aprendendo a estruturar propriedades e métodos para representar dados de um cliente em nosso sistema. Também discutimos a importância de uma interface de usuário amigável para o cadastro de clientes, utilizando o Windows Forms.

_4 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Maria, uma desenvolvedora iniciante, está criando um sistema de cadastro de clientes. Ela percebe que algumas informações estão sendo inseridas incorretamente, como e-mails sem "@" ou números de telefone incompletos.

_4 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Pergunta
- Duas Soluções Possíveis:
- Maria pode criar métodos de validação manualmente para cada campo.
- Maria pode utilizar a biblioteca ComponentModel.DataAnnotations para simplificar a validação.
- Quem sabe responde!

_5 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Solução Correta: Utilizar ComponentModel.DataAnnotations permite uma validação padronizada, eficiente e menos propensa a erros.
- Solução Incorreta: Criar métodos manuais pode funcionar, mas aumenta o risco de inconsistências e a quantidade de código a ser mantida.

_4 imagem(ns) no slide._

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- Visão Geral
- A validação de dados é essencial para garantir a integridade e a segurança de um sistema. Sem ela, dados incorretos ou mal formatados podem causar falhas e prejudicar o funcionamento do software.

_4 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- Definição e Aplicação
- Utilizando a biblioteca ComponentModel.DataAnnotations, podemos aplicar regras de validação diretamente nas propriedades de nossas classes, como Cliente. Isso facilita a validação e mantém o código organizado.

_4 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Importância
- A validação é importante para evitar erros que podem comprometer o sistema e para garantir que os dados armazenados sejam sempre corretos e úteis.

_4 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- Uso
- No dia a dia do desenvolvimento, a validação é aplicada sempre que um dado é inserido ou atualizado. Um exemplo comum é a verificação de e-mails e números de telefone, como faremos na nossa classe Cliente.

_4 imagem(ns) no slide._

### Slide 13

- DESENVOLVIMENTO DE SISTEMAS
- Program.cs
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
- MainForm.Designer.cs
- Utilize o visual studio comunity

_5 imagem(ns) no slide._

### Slide 17

- DESENVOLVIMENTO DE SISTEMAS
- MainForm.Designer.cs
- Utilize o visual studio comunity

_5 imagem(ns) no slide._

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- MainForm.Designer.cs
- Utilize o visual studio comunity

_5 imagem(ns) no slide._

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- MainForm.Designer.cs
- Utilize o visual studio comunity

_5 imagem(ns) no slide._

### Slide 20

- DESENVOLVIMENTO DE SISTEMAS
- Cliente.cs
- Utilize o visual studio comunity

_5 imagem(ns) no slide._

### Slide 21

- DESENVOLVIMENTO DE SISTEMAS
- Questão de fixação
- O que é a validação de dados?
- A) Um método para estilizar o código.
- B) Uma forma de garantir que os dados inseridos sejam válidos.
- C) Um processo para remover dados duplicados.
- D) Uma técnica de organização do código.
- Quem sabe responde!

_4 imagem(ns) no slide._

### Slide 22

- DESENVOLVIMENTO DE SISTEMAS
- Resposta!
- O que é a validação de dados?
- A) Um método para estilizar o código.
- B) Uma forma de garantir que os dados inseridos sejam válidos.
- C) Um processo para remover dados duplicados.
- D) Uma técnica de organização do código.
- Resposta correta: B)

_3 imagem(ns) no slide._

### Slide 23

- DESENVOLVIMENTO DE SISTEMAS
- Atividade Prática na Plataforma Alura
- Na plataforma Alura vamos acessar o seguinte curso:
- A recomendação é que você continue esse curso extraclasse, pois ele traz um conteúdo essencial para compreender sobre o referido tema.
- Link para o curso: https://cursos.alura.com.br/course/windows-forms-csharp-barra-ferramentas-classes-json

_6 imagem(ns) no slide._

### Slide 24

- DESENVOLVIMENTO DE SISTEMAS
- DLL ComponentModel.DataAnnotations
- 7 minutos
- Link para tarefa: https://cursos.alura.com.br/course/windows-forms-csharp-barra-ferramentas-classes-json/task/71287
- A DLL System.ComponentModel.DataAnnotations em C# fornece atributos de validação, como [Required], [EmailAddress] e [Phone], que ajudam a garantir que os dados de entrada estejam corretos e formatados adequadamente antes de serem processados.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 25

- DESENVOLVIMENTO DE SISTEMAS
- Método de validação
- 6 minutos
- Link para tarefa: https://cursos.alura.com.br/course/windows-forms-csharp-barra-ferramentas-classes-json/task/71288
- Um método de validação em C# aplica regras para verificar se os dados de um objeto estão corretos, usando atributos como [Required] e [EmailAddress]. Ele ajuda a garantir que o objeto esteja pronto para uso ou armazenamento, retornando erros caso as validações falhem. É fundamental para a integridade dos dados em aplicações.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 26

- DESENVOLVIMENTO DE SISTEMAS
- Instanciando a classe Cliente
- 11 minutos
- Link para tarefa: https://cursos.alura.com.br/course/windows-forms-csharp-barra-ferramentas-classes-json/task/71289
- Instanciar a classe Cliente em C# significa criar um novo objeto dessa classe, permitindo o armazenamento e a manipulação dos dados do cliente. Isso é feito com Cliente cliente = new Cliente();, onde cliente é o objeto que poderá acessar e modificar os atributos definidos na classe, como Nome, Endereço, Telefone, e Email.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 27

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje
- Aprendemos a validar os dados de nossa classe Cliente utilizando a biblioteca ComponentModel.DataAnnotations. Exploramos a importância da validação para manter a integridade dos dados e como aplicar essas técnicas de forma prática em nossos projetos.

_4 imagem(ns) no slide._

### Slide 28

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

### Slide 29

- DESENVOLVIMENTO DE SISTEMAS
- Referências (Imagens)
- Figuras e Imagens:
- https://www.flaticon.com/br
- https://www.istockphoto.com/br
- https://raw.githubusercontent.com/zbtang/React-Native-ViewPager/HEAD/imgs/dotIndicator.gif
- https://storyset.com

_3 imagem(ns) no slide._

### Slide 30

- DESENVOLVIMENTO DE SISTEMAS
- O RCO+Aulas é um projeto da Secretaria de Estado da Educação do Paraná e está em constante revisão. Todos os slides são de uso exclusivo dos professores da Rede Pública de Ensino, com a finalidade específica de aplicação em sala de aula, sendo totalmente vedada a publicização, reutilização, reprodução total ou parcial para quaisquer outros fins.

_4 imagem(ns) no slide._

### Slide 31

- DESENVOLVIMENTO DE SISTEMAS
- Esta publicação tem a cooperação entre a UNESCO e a Secretaria de Estado da Educação e do Esporte do Paraná no âmbito da parceria PRODOC 914BRZ1091, cujo objetivo é trazer soluções inovadoras de gestão da rede pública estadual de educação do Paraná para a melhoria da aprendizagem dos alunos. As indicações de nomes e a apresentação do material ao longo desta publicação não implicam a manifestação de qualquer opinião por parte da UNESCO a respeito da condição jurídica de qualquer país, território, cidade, região ou de suas autoridades, tampouco da delimitação de suas fronteiras ou limites As ideias e opiniões expressas nesta publicação são as dos autores e não refletem obrigatoriamente as da UNESCO nem comprometem a Organização.
- Cooperação Técnica

_5 imagem(ns) no slide._

## Atividade

_Fonte: AULA 77_ATIVIDADE_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

ATIVIDADE AULA 77

Questão 1

Qual dos atributos a seguir é usado para validar e-mails?

A) [Phone]

B) [Required]

C) [EmailAddress]

D) [StringLength]

Resposta correta: C. O atributo [EmailAddress] é usado para validar e-mails.

Questão 2

Qual a função do atributo [Required]?

A) Validar números de telefone.

B) Garantir que uma propriedade não seja nula.

C) Definir o tamanho máximo de uma string.

D) Validar endereços de e-mail.

Resposta correta: B. O atributo [Required] garante que uma propriedade não seja nula.
