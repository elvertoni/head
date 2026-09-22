---
titulo: "Desenvolvendo um User Control"
tipo: rco-seed
disciplina: programacao-no-desenvolvimento-de-sistemas
sigla_rco: PDS
trimestre: 2
ordem_rco: 67
serie: 3
aula_rco: "Aula 67"
slides: 22
tem_atividade: false
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PDS/2TRI/67-desenvolvendo-um-user-control/67-desenvolvendo-um-user-control.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PDS/2TRI/67-desenvolvendo-um-user-control/AULA 67_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Desenvolvendo um User Control

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO NO
- DESENVOLVIMENTO DE
- SISTEMAS
- 3ª SÉRIE
- Desenvolvendo um User Control
- Aula 67

_3 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- DESENVOLVIMENTO DE SISTEMAS
- Nesta aula, vamos:
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store
- Criar um User Control
- no Windows Forms.

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
- Aprendemos sobre formulários MDI (Multiple Document Interface), como organizá-los e fixar o tamanho das janelas. Exploramos como criar uma interface mais organizada e gerenciável para aplicativos com múltiplos documentos.

_4 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Joana, uma estudante do ensino médio, está
- criando uma aplicação de biblioteca.
- Ela precisa de um controle personalizado que possa ser reutilizado em várias partes do aplicativo.
- Ela também deseja adicionar abas com imagens para facilitar a navegação.
- Como Joana
- poderá fazer isso?

_5 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- O que ela deverá fazer?
- Criar um User Control personalizado e utilizar um TabControl para adicionar abas com imagens.
- Adicionar todos os controles diretamente em um único formulário sem usar User Controls ou abas.
- Quem sabe responde!

_7 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Resposta correta…
- Utilizar User Controls e TabControl ajuda a manter o código organizado e facilita a reutilização de componentes.
- Adicionar todos os controles em um único formulário sem organização torna o código confuso e difícil de manter!

_5 imagem(ns) no slide._

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- Visão Geral
- User Controls no Windows Forms permitem criar componentes personalizados que podem ser reutilizados em diferentes partes da aplicação.
- O uso de TabPages em um TabControl permite organizar a interface de forma clara e acessível.

_5 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- Definição e Aplicação
- User Control
- Componente personalizado que encapsula a funcionalidade específica.
- TabPage
- Abas usadas dentro de um TabControl para organizar a interface.
- Imagens em TabPage
- Adicionar ícones ou imagens às abas para melhorar a experiência do usuário.

_4 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Importância
- Criar User Controls e usar TabPages organiza melhor o código, melhora a reutilização de componentes e cria uma interface de usuário mais amigável e fácil de navegar.

_4 imagem(ns) no slide._

### Slide 12

- Uso
- User Control
- Pode ser usado para criar um componente de entrada de dados reutilizável.
- DESENVOLVIMENTO DE SISTEMAS
- TabPage
- Utilizado para dividir diferentes seções de um aplicativo, como Home, Settings, e Profile.
- Imagens em TabPage Melhoram a navegação visual e tornam o aplicativo mais atraente.

_3 imagem(ns) no slide._

### Slide 13

- DESENVOLVIMENTO DE SISTEMAS
- Questão de fixação
- Qual a função do User Control no Windows Forms?
- (A) Adicionar interatividade ao formulário.
- (B) Criar componentes personalizados reutilizáveis.
- (C) Gerenciar dados do usuário.
- (D) Melhorar a performance do aplicativo.
- Quem sabe responde!

_4 imagem(ns) no slide._

### Slide 14

- DESENVOLVIMENTO DE SISTEMAS
- Questão de fixação
- Qual a função do User Control no Windows Forms?
- (A) Adicionar interatividade ao formulário.
- (B) Criar componentes personalizados reutilizáveis.
- (C) Gerenciar dados do usuário.
- (D) Melhorar a performance do aplicativo.
- Resposta Correta: (B)Criar componentes personalizados reutilizáveis.

_3 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- Atividade Prática na Plataforma Alura
- Na plataforma Alura vamos acessar o seguinte curso:
- A recomendação é que você continue esse curso extraclasse, pois ele traz um conteúdo essencial para compreender sobre o referido tema.
- Link para o curso: https://cursos.alura.com.br/course/windows-forms-csharp-menus-formularios-validacao

_6 imagem(ns) no slide._

### Slide 16

- DESENVOLVIMENTO DE SISTEMAS
- Controle de Usuário de Windows Forms
- 17 minutos
- Link para tarefa: https://cursos.alura.com.br/course/windows-forms-csharp-menus-formularios-validacao/task/70746
- O Controle de Usuário de Windows Forms permite criar componentes personalizados e reutilizáveis, encapsulando funcionalidades específicas. Facilita a manutenção e organização do código, melhorando a eficiência do desenvolvimento.
- Atividade no Portal Alura!

_7 imagem(ns) no slide._

### Slide 17

- DESENVOLVIMENTO DE SISTEMAS
- Adicionando uma TabPage
- 9 minutos
- Link para tarefa: https://cursos.alura.com.br/course/windows-forms-csharp-menus-formularios-validacao/task/70747
- Adicionar uma TabPage em um Windows Forms permite organizar o conteúdo em abas, facilitando a navegação e o acesso a diferentes seções de uma aplicação. É útil para melhorar a interface e a experiência do usuário.
- Atividade no Portal Alura!

_7 imagem(ns) no slide._

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje
- Exploramos a criação de User Controls no Windows Forms e a adição de TabPages com imagens. Aprendemos como esses componentes podem melhorar a organização e a reutilização de código, além de tornar a interface do usuário mais intuitiva e atrativa.

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

_5 imagem(ns) no slide._

## Outros documentos

_Fonte: AULA 67_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

ATIVIDADE AULA 67

Questão 1

Para que serve a propriedade MdiParent em um formulário?

A. Definir o título do formulário.

B. Especificar o formulário pai em uma interface MDI.

C. Determinar a posição do formulário na tela.

D. Ajustar o tamanho do formulário.

Comentário: A propriedade MdiParent especifica o formulário pai em uma interface MDI, permitindo que o formulário seja exibido dentro do contêiner MDI.

Questão 2

Qual é a vantagem de usar um TabControl em um aplicativo Windows Forms?

A. Melhorar a segurança do aplicativo.

B. Organizar melhor a interface do usuário.

C. Aumentar a velocidade do aplicativo.

D. Reduzir o uso de memória.

Comentário: Usar um TabControl ajuda a organizar melhor a interface do usuário, tornando-a mais intuitiva e fácil de navegar.
