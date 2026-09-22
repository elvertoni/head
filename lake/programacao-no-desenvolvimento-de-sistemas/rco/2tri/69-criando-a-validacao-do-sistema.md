---
titulo: "Criando a validação do sistema"
tipo: rco-seed
disciplina: programacao-no-desenvolvimento-de-sistemas
sigla_rco: PDS
trimestre: 2
ordem_rco: 69
serie: 3
aula_rco: "Aula 69"
slides: 33
tem_atividade: false
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PDS/2TRI/69-criando-a-validacao-do-sistema/69-criando-a-validacao-do-sistema.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PDS/2TRI/69-criando-a-validacao-do-sistema/AULA 69_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Criando a validação do sistema

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO NO
- DESENVOLVIMENTO DE
- SISTEMAS
- 3ª SÉRIE
- Criando a validação do sistema
- Aula 69

_3 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- DESENVOLVIMENTO DE SISTEMAS
- Nesta aula, vamos:
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store
- Aprender a criar uma tela de login segura e validar a senha de acesso. Vamos explorar como inibir as opções do menu até que o usuário seja autenticado e como fechar abas de forma segura.

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
- Exploramos como utilizar o componente DialogBox para interagir com o usuário através de mensagens e confirmações, ajudando a guiar o fluxo de operação do sistema.

_4 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Ana, uma desenvolvedora júnior, foi designada para implementar a segurança básica em uma aplicação Windows Forms. Ela precisa criar uma tela de login que impeça o acesso a funcionalidades críticas até que o usuário seja autenticado.

_4 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Como Ana pode garantir que o sistema só permita o acesso a usuários autenticados, inibindo as opções do menu e validando a senha de forma eficaz?
- Quem sabe responde!

_5 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Ana deve implementar uma tela de login que valida as credenciais do usuário. Após a autenticação, as opções do menu são habilitadas. A senha deve ser armazenada de forma segura e validada corretamente.

_4 imagem(ns) no slide._

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- Visão Geral
- A validação do sistema é um componente crucial na segurança de qualquer aplicação. Ela garante que apenas usuários autorizados possam acessar as funcionalidades críticas do sistema.

_4 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- Definição e Aplicação
- Validação de sistema envolve a criação de mecanismos para verificar a identidade do usuário antes de conceder acesso a partes sensíveis da aplicação, como menus e funções administrativas.

_4 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Importância
- A segurança de sistemas é fundamental para proteger dados e operações. A validação de usuários impede acessos não autorizados e protege a integridade do sistema.

_4 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- Uso
- Na prática, a validação de sistema é implementada através de telas de login, criptografia de senhas e inibição de funcionalidades até que o usuário seja autenticado.

_4 imagem(ns) no slide._

### Slide 13

- DESENVOLVIMENTO DE SISTEMAS
- Tela do forms (forms1.cs)
- Utilize o Visual Studio Community

_6 imagem(ns) no slide._

### Slide 14

- DESENVOLVIMENTO DE SISTEMAS
- Código do forms (forms1.cs)
- Utilize o Visual Studio Community

_6 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- Código do design do forms (forms1.design.cs)
- Utilize o Visual Studio Community

_6 imagem(ns) no slide._

### Slide 16

- DESENVOLVIMENTO DE SISTEMAS
- Código do design do forms (forms1.design.cs)
- Utilize o Visual Studio Community

_6 imagem(ns) no slide._

### Slide 17

- DESENVOLVIMENTO DE SISTEMAS
- Código do design do forms (forms1.design.cs)
- Utilize o Visual Studio Community

_6 imagem(ns) no slide._

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- Código do design do forms (forms1.design.cs)
- Utilize o Visual Studio Community

_6 imagem(ns) no slide._

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- Código do programa(program.cs)
- Utilize o Visual Studio Community

_6 imagem(ns) no slide._

### Slide 20

- DESENVOLVIMENTO DE SISTEMAS
- Código Main form(MainForm.cs)
- Utilize o Visual Studio Community

_6 imagem(ns) no slide._

### Slide 21

- DESENVOLVIMENTO DE SISTEMAS
- Código Main form(MainForm.Design.cs)
- Utilize o Visual Studio Community

_6 imagem(ns) no slide._

### Slide 22

- DESENVOLVIMENTO DE SISTEMAS
- Código Main form(MainForm.Design.cs)
- Utilize o Visual Studio Community

_6 imagem(ns) no slide._

### Slide 23

- DESENVOLVIMENTO DE SISTEMAS
- Questão de fixação
- Implemente uma função que desabilita todas as opções de menu até que o usuário seja autenticado e, após o login, reabilite-as. Documente o processo e explique como essa prática contribui para a segurança do sistema.
- Quem sabe responde!

_4 imagem(ns) no slide._

### Slide 24

- DESENVOLVIMENTO DE SISTEMAS
- Atividade Prática na Plataforma Alura
- Na plataforma Alura vamos acessar o seguinte curso:
- A recomendação é que você continue esse curso extraclasse, pois ele traz um conteúdo essencial para compreender sobre o referido tema.
- Link para o curso: https://cursos.alura.com.br/course/windows-forms-csharp-menus-formularios-validacao

_6 imagem(ns) no slide._

### Slide 25

- DESENVOLVIMENTO DE SISTEMAS
- Tela de login
- 12 minutos
- Link para tarefa: https://cursos.alura.com.br/course/windows-forms-csharp-menus-formularios-validacao/task/70757
- A tela de login é a interface inicial de um sistema, onde os usuários inserem suas credenciais (usuário e senha) para acessar funcionalidades restritas. É essencial para a segurança, validando quem pode usar o sistema.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 26

- DESENVOLVIMENTO DE SISTEMAS
- Inibindo as opções do menu
- 9 minutos
- Link para tarefa: https://cursos.alura.com.br/course/windows-forms-csharp-menus-formularios-validacao/task/70758
- "Inibir as opções do menu" significa desativar temporariamente certas funcionalidades em um sistema. Isso pode ser útil para restringir o acesso a recursos até que determinadas condições sejam atendidas, como a autenticação do usuário.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 27

- DESENVOLVIMENTO DE SISTEMAS
- Validando a senha
- 11 minutos
- Link para tarefa: https://cursos.alura.com.br/course/windows-forms-csharp-menus-formularios-validacao/task/70759
- Validar a senha é verificar se ela atende critérios de segurança, como tamanho mínimo, caracteres especiais, e combinações de letras e números. Isso garante que a senha seja forte e protege o acesso ao sistema.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 28

- DESENVOLVIMENTO DE SISTEMAS
- Fechando as abas
- 17 minutos
- Link para tarefa: https://cursos.alura.com.br/course/windows-forms-csharp-menus-formularios-validacao/task/70760
- Fechar abas em uma aplicação envolve encerrar sessões ou tarefas específicas do usuário, liberando recursos e garantindo que os dados sejam salvos ou descartados de forma adequada antes de finalizar a aba.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 29

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje
- Aprendemos a criar uma tela de login e a implementar a validação de senha para garantir a segurança do sistema. Também exploramos como inibir menus e reabilitá-los após a autenticação do usuário. Essas práticas são essenciais para proteger dados e funcionalidades sensíveis em aplicações de software.

_4 imagem(ns) no slide._

### Slide 30

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

### Slide 31

- DESENVOLVIMENTO DE SISTEMAS
- Referências (Imagens)
- Figuras e Imagens:
- https://www.flaticon.com/br
- https://www.istockphoto.com/br
- https://raw.githubusercontent.com/zbtang/React-Native-ViewPager/HEAD/imgs/dotIndicator.gif
- https://storyset.com

_3 imagem(ns) no slide._

### Slide 32

- DESENVOLVIMENTO DE SISTEMAS
- O RCO+Aulas é um projeto da Secretaria de Estado da Educação do Paraná e está em constante revisão. Todos os slides são de uso exclusivo dos professores da Rede Pública de Ensino, com a finalidade específica de aplicação em sala de aula, sendo totalmente vedada a publicização, reutilização, reprodução total ou parcial para quaisquer outros fins.

_4 imagem(ns) no slide._

### Slide 33

- DESENVOLVIMENTO DE SISTEMAS
- Esta publicação tem a cooperação entre a UNESCO e a Secretaria de Estado da Educação e do Esporte do Paraná no âmbito da parceria PRODOC 914BRZ1091, cujo objetivo é trazer soluções inovadoras de gestão da rede pública estadual de educação do Paraná para a melhoria da aprendizagem dos alunos. As indicações de nomes e a apresentação do material ao longo desta publicação não implicam a manifestação de qualquer opinião por parte da UNESCO a respeito da condição jurídica de qualquer país, território, cidade, região ou de suas autoridades, tampouco da delimitação de suas fronteiras ou limites As ideias e opiniões expressas nesta publicação são as dos autores e não refletem obrigatoriamente as da UNESCO nem comprometem a Organização.
- Cooperação Técnica

_5 imagem(ns) no slide._

## Outros documentos

_Fonte: AULA 69_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

ATIVIDADE AULA 69

Questão 1

Qual é o objetivo de inibir as opções do menu antes da autenticação do usuário?

A) Facilitar a navegação do usuário

B) Melhorar a interface gráfica

C) Proteger as funcionalidades do sistema de acessos não autorizados

D) Otimizar a performance do sistema

Comentário: A resposta correta é C). Inibir as opções do menu antes da autenticação garante que somente usuários autorizados possam acessar as funcionalidades do sistema.

Questão 2

Por que é importante validar a senha do usuário de forma segura?

A) Para melhorar a experiência do usuário

B) Para evitar acessos não autorizados e proteger os dados do sistema

C) Para aumentar a velocidade do sistema

D) Para reduzir o uso de memória

Comentário: A resposta correta é B). A validação segura da senha é fundamental para proteger o sistema contra acessos não autorizados e manter a integridade dos dados.
