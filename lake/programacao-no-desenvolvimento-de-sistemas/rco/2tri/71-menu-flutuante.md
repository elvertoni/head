---
titulo: "Menu flutuante"
tipo: rco-seed
disciplina: programacao-no-desenvolvimento-de-sistemas
sigla_rco: PDS
trimestre: 2
ordem_rco: 71
serie: 3
aula_rco: "Aula 71"
slides: 26
tem_atividade: false
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PDS/2TRI/71-menu-flutuante/71-menu-flutuante.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PDS/2TRI/71-menu-flutuante/AULA 71_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Menu flutuante

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO NO
- DESENVOLVIMENTO DE
- SISTEMAS
- 3ª SÉRIE
- Menu flutuante
- Aula 71

_3 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- DESENVOLVIMENTO DE SISTEMAS
- Nesta aula, vamos:
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store
- Criar e interagir com menus flutuantes no Windows Forms, capturando eventos do mouse para acionar ações específicas

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
- Aprendemos como interagir com eventos do mouse em um formulário Windows Forms, capturando propriedades e alterando o comportamento do cursor em tempo real.

_4 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Maria está desenvolvendo uma aplicação de gerenciamento de arquivos e deseja adicionar um menu flutuante que aparece quando o usuário clica com o botão direito do mouse em um item da lista. Esse menu deve permitir que o usuário execute ações como renomear, excluir ou visualizar detalhes do arquivo.

_4 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Como Maria pode implementar um menu flutuante que apareça na posição exata onde o usuário clica com o mouse, e que execute as ações desejadas?
- Quem sabe responde!

_5 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Maria deve usar o evento MouseClick para capturar a posição do clique e utilizar um ContextMenuStrip para criar o menu flutuante. Ela pode então associar as ações do menu aos itens clicados, utilizando a posição do mouse para exibir o menu no local correto.

_4 imagem(ns) no slide._

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- Visão Geral
- Menus flutuantes (ou contextuais) são elementos que aparecem em resposta a cliques do mouse, geralmente com o botão direito. Eles oferecem opções baseadas no contexto da interface, como ações específicas para o item selecionado.

_4 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- Definição e Aplicação
- Um menu flutuante em Windows Forms é criado utilizando o componente ContextMenuStrip. Ele é utilizado para fornecer opções adicionais ao usuário em resposta a um clique do mouse em um determinado controle ou área do formulário.

_4 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Importância
- Menus flutuantes melhoram a interatividade e usabilidade da aplicação, permitindo que os usuários acessem rapidamente funções específicas sem navegar pelos menus principais.

_4 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- Uso
- Em aplicações como gerenciadores de arquivos, editores de texto, e navegadores, menus flutuantes são comuns para ações como copiar, colar, renomear, e excluir itens.

_4 imagem(ns) no slide._

### Slide 13

- DESENVOLVIMENTO DE SISTEMAS
- Tela do forms (MainForm.cs)
- Depois de compilado, clique com o botão direito sobre a área desse form
- Utilize o Visual Studio Community

_6 imagem(ns) no slide._

### Slide 14

- DESENVOLVIMENTO DE SISTEMAS
- Código do forms (MainForm.cs)
- Utilize o Visual Studio Community

_6 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- Código do design do forms (MainForm.design.cs)
- Utilize o Visual Studio Community

_6 imagem(ns) no slide._

### Slide 16

- DESENVOLVIMENTO DE SISTEMAS
- Código do programa(program.cs)
- Utilize o Visual Studio Community

_6 imagem(ns) no slide._

### Slide 17

- DESENVOLVIMENTO DE SISTEMAS
- Questão de fixação
- Qual dos seguintes eventos é utilizado para capturar um clique do mouse em um formulário?
- A) MouseClick
- B) KeyPress
- C) Load
- D) Close
- Quem sabe responde!

_4 imagem(ns) no slide._

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Qual dos seguintes eventos é utilizado para capturar um clique do mouse em um formulário?
- A) MouseClick
- B) KeyPress
- C) Load
- D) Close
- Resposta correta: A. O evento MouseClick é utilizado para capturar um clique do mouse em um formulário.

_3 imagem(ns) no slide._

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- Atividade Prática na Plataforma Alura
- Na plataforma Alura vamos acessar o seguinte curso:
- A recomendação é que você continue esse curso extraclasse, pois ele traz um conteúdo essencial para compreender sobre o referido tema.
- Link para o curso: https://cursos.alura.com.br/course/windows-forms-csharp-eventos-mouse-componentes

_6 imagem(ns) no slide._

### Slide 20

- DESENVOLVIMENTO DE SISTEMAS
- Capturando o mouse no formulário
- 8 minutos
- Link para tarefa: https://cursos.alura.com.br/course/windows-forms-csharp-eventos-mouse-componentes/task/71001
- Capturar o mouse em um formulário permite detectar cliques e movimentos do mouse, oferecendo a capacidade de interagir diretamente com a interface do usuário. Esse recurso é essencial para criar menus flutuantes e outros comportamentos dinâmicos baseados na posição do cursor, melhorando a interatividade e a experiência do usuário em aplicações Windows Forms.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 21

- DESENVOLVIMENTO DE SISTEMAS
- Capturando a posição do clique
- 5 minutos
- Link para tarefa: https://cursos.alura.com.br/course/windows-forms-csharp-eventos-mouse-componentes/task/71002
- Capturar a posição do clique em um formulário Windows Forms é crucial para identificar onde o usuário interagiu na interface. Isso permite desencadear ações específicas com base na coordenada exata do clique, como exibir menus contextuais ou mover elementos, melhorando a interatividade e a precisão da aplicação.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 22

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje
- Aprendemos a criar menus flutuantes no Windows Forms, capturando eventos do mouse para exibir e interagir com esses menus de forma contextual. Esta habilidade permite melhorar a usabilidade e a interatividade das aplicações, oferecendo aos usuários uma interface mais rica e intuitiva.

_4 imagem(ns) no slide._

### Slide 23

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

### Slide 24

- DESENVOLVIMENTO DE SISTEMAS
- Referências (Imagens)
- Figuras e Imagens:
- https://www.flaticon.com/br
- https://www.istockphoto.com/br
- https://raw.githubusercontent.com/zbtang/React-Native-ViewPager/HEAD/imgs/dotIndicator.gif
- https://storyset.com

_3 imagem(ns) no slide._

### Slide 25

- DESENVOLVIMENTO DE SISTEMAS
- O RCO+Aulas é um projeto da Secretaria de Estado da Educação do Paraná e está em constante revisão. Todos os slides são de uso exclusivo dos professores da Rede Pública de Ensino, com a finalidade específica de aplicação em sala de aula, sendo totalmente vedada a publicização, reutilização, reprodução total ou parcial para quaisquer outros fins.

_4 imagem(ns) no slide._

### Slide 26

- DESENVOLVIMENTO DE SISTEMAS
- Esta publicação tem a cooperação entre a UNESCO e a Secretaria de Estado da Educação e do Esporte do Paraná no âmbito da parceria PRODOC 914BRZ1091, cujo objetivo é trazer soluções inovadoras de gestão da rede pública estadual de educação do Paraná para a melhoria da aprendizagem dos alunos. As indicações de nomes e a apresentação do material ao longo desta publicação não implicam a manifestação de qualquer opinião por parte da UNESCO a respeito da condição jurídica de qualquer país, território, cidade, região ou de suas autoridades, tampouco da delimitação de suas fronteiras ou limites As ideias e opiniões expressas nesta publicação são as dos autores e não refletem obrigatoriamente as da UNESCO nem comprometem a Organização.
- Cooperação Técnica

_5 imagem(ns) no slide._

## Outros documentos

_Fonte: AULA 71_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

ATIVIDADE AULA 71

Questão 1

Como você pode associar uma ação específica a um item de menu flutuante?

A) Utilizando o evento Click do item de menu.

B) Alterando a propriedade Text do formulário.

C) Alterando a cor de fundo do formulário.

D) Utilizando o evento KeyPress do formulário.

Resposta correta: A. A ação é associada ao item de menu utilizando o evento Click.

Questão 2

Qual a importância de capturar a posição do clique ao exibir um menu flutuante?

A) Para abrir o menu na posição central do formulário.

B) Para exibir o menu na posição onde o mouse foi clicado.

C) Para impedir que o menu seja exibido.

D) Para redimensionar o formulário.

Resposta correta: B. Capturar a posição do clique é importante para exibir o menu na posição correta em relação ao clique do mouse.
