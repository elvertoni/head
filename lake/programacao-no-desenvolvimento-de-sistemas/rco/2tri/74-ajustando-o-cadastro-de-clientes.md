---
titulo: "Ajustando o cadastro de clientes"
tipo: rco-seed
disciplina: programacao-no-desenvolvimento-de-sistemas
sigla_rco: PDS
trimestre: 2
ordem_rco: 74
serie: 3
aula_rco: "Aula 74"
slides: 28
tem_atividade: false
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PDS/2TRI/74-ajustando-o-cadastro-de-clientes/74-ajustando-o-cadastro-de-clientes.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PDS/2TRI/74-ajustando-o-cadastro-de-clientes/AULA 74_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Ajustando o cadastro de clientes

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO NO
- DESENVOLVIMENTO DE
- SISTEMAS
- 3ª SÉRIE
- Ajustando o cadastro de clientes
- Aula 74

_3 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- DESENVOLVIMENTO DE SISTEMAS
- Nesta aula, vamos:
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store
- Aprimorar o cadastro de clientes, organizando melhor as informações.

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
- Iniciamos o cadastro de clientes criando uma interface simples com campos básicos como Nome, Endereço, Telefone e Email. Hoje, vamos expandir e organizar essa interface, tornando-a mais funcional e eficiente.

_4 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Maria está criando um formulário de cadastro de clientes, mas percebe que os dados estão desorganizados e os campos são preenchidos em uma ordem confusa. Ela precisa melhorar a usabilidade do formulário.

_4 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Pergunta
- Como Maria pode organizar o formulário para melhorar a experiência do usuário e garantir que os dados sejam inseridos de maneira lógica e fluida?
- Quem sabe responde!

_5 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Maria deve utilizar o TabIndex para definir a ordem de navegação entre os campos, agrupar informações relacionadas usando GroupBox, e adicionar opções como CheckBox e RadioButtons para facilitar a escolha de opções específicas.

_4 imagem(ns) no slide._

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- Visão Geral
- O ajuste e organização dos elementos de um formulário são essenciais para criar interfaces de usuário intuitivas e funcionais. Agrupar informações, definir a ordem de navegação e utilizar elementos interativos como CheckBox, RadioButtons e ComboBox são práticas fundamentais nesse processo.

_4 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- Definição e Aplicação
- TabIndex: Permite definir a ordem em que os controles do formulário são acessados ao pressionar a tecla Tab.
- CheckBox e RadioButtons: São usados para apresentar ao usuário opções que podem ser marcadas ou desmarcadas (CheckBox) ou para permitir a escolha de uma única opção dentro de um grupo (RadioButtons).
- ComboBox: Oferece uma lista suspensa de opções, permitindo que o usuário escolha uma entre várias.

_3 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Importância
- Organizar o formulário e utilizar esses controles melhora a usabilidade, torna o sistema mais eficiente e reduz a probabilidade de erros na inserção de dados.

_4 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- Uso
- Em sistemas de cadastro, como o de clientes, essas práticas ajudam a criar interfaces onde os dados são inseridos de forma estruturada e lógica, garantindo que as informações sejam coletadas corretamente e de maneira eficiente.

_4 imagem(ns) no slide._

### Slide 13

- DESENVOLVIMENTO DE SISTEMAS
- Código do forms (FormCadastro.cs)
- Utilize o visual studio comunity

_6 imagem(ns) no slide._

### Slide 14

- DESENVOLVIMENTO DE SISTEMAS
- Código do design do forms (FormCadastro.design.cs)
- Utilize o visual studio comunity

_6 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- Código do design do forms (FormCadastro.design.cs)
- Utilize o visual studio comunity

_6 imagem(ns) no slide._

### Slide 16

- DESENVOLVIMENTO DE SISTEMAS
- Código do design do forms (FormCadastro.design.cs)
- Utilize o visual studio comunity

_6 imagem(ns) no slide._

### Slide 17

- DESENVOLVIMENTO DE SISTEMAS
- Código do design do forms (FormCadastro.design.cs)
- Utilize o visual studio comunity

_6 imagem(ns) no slide._

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- Código do programa(program.cs)
- Utilize o visual studio comunity

_6 imagem(ns) no slide._

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- Questão de fixação
- O que é o TabIndex e por que ele é importante?
- A) Um controle de interface que mostra uma lista de itens.
- B) Um índice que define a ordem de navegação dos controles.
- C) Um botão que inicia uma ação específica.
- D) Um componente que exibe mensagens de erro.
- Quem sabe responde!

_4 imagem(ns) no slide._

### Slide 20

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- O que é o TabIndex e por que ele é importante?
- A) Um controle de interface que mostra uma lista de itens.
- B) Um índice que define a ordem de navegação dos controles.
- C) Um botão que inicia uma ação específica.
- D) Um componente que exibe mensagens de erro.
- Resposta: B) Um índice que define a ordem de navegação dos controles.

_3 imagem(ns) no slide._

### Slide 21

- DESENVOLVIMENTO DE SISTEMAS
- Atividade Prática na Plataforma Alura
- Na plataforma Alura vamos acessar o seguinte curso:
- A recomendação é que você continue esse curso extraclasse, pois ele traz um conteúdo essencial para compreender sobre o referido tema.
- Link para o curso: https://cursos.alura.com.br/course/windows-forms-csharp-eventos-mouse-componentes

_6 imagem(ns) no slide._

### Slide 22

- DESENVOLVIMENTO DE SISTEMAS
- Ajustando o projeto
- 24 minutos
- Link para tarefa: https://cursos.alura.com.br/course/windows-forms-csharp-eventos-mouse-componentes/task/71020
- Ajustar o projeto envolve organizar os arquivos, separar o código de interface da lógica, e garantir que os componentes estejam corretamente configurados. Isso facilita a manutenção e melhora a clareza e eficiência do desenvolvimento.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 23

- DESENVOLVIMENTO DE SISTEMAS
- TabIndex
- 11 minutos
- Link para tarefa: https://cursos.alura.com.br/course/windows-forms-csharp-eventos-mouse-componentes/task/71016
- O TabIndex define a ordem em que os controles de um formulário são selecionados quando o usuário pressiona a tecla Tab. Configurar corretamente o TabIndex melhora a navegabilidade e a usabilidade do aplicativo.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 24

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje
- Aprimoramos o formulário de cadastro de clientes, organizando os campos, definindo a ordem de navegação, e adicionando opções interativas como CheckBox, RadioButtons e ComboBox para melhorar a usabilidade e a eficiência do sistema.

_4 imagem(ns) no slide._

### Slide 25

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

### Slide 26

- DESENVOLVIMENTO DE SISTEMAS
- Referências (Imagens)
- Figuras e Imagens:
- https://www.flaticon.com/br
- https://www.istockphoto.com/br
- https://raw.githubusercontent.com/zbtang/React-Native-ViewPager/HEAD/imgs/dotIndicator.gif
- https://storyset.com

_3 imagem(ns) no slide._

### Slide 27

- DESENVOLVIMENTO DE SISTEMAS
- O RCO+Aulas é um projeto da Secretaria de Estado da Educação do Paraná e está em constante revisão. Todos os slides são de uso exclusivo dos professores da Rede Pública de Ensino, com a finalidade específica de aplicação em sala de aula, sendo totalmente vedada a publicização, reutilização, reprodução total ou parcial para quaisquer outros fins.

_4 imagem(ns) no slide._

### Slide 28

- DESENVOLVIMENTO DE SISTEMAS
- Esta publicação tem a cooperação entre a UNESCO e a Secretaria de Estado da Educação e do Esporte do Paraná no âmbito da parceria PRODOC 914BRZ1091, cujo objetivo é trazer soluções inovadoras de gestão da rede pública estadual de educação do Paraná para a melhoria da aprendizagem dos alunos. As indicações de nomes e a apresentação do material ao longo desta publicação não implicam a manifestação de qualquer opinião por parte da UNESCO a respeito da condição jurídica de qualquer país, território, cidade, região ou de suas autoridades, tampouco da delimitação de suas fronteiras ou limites As ideias e opiniões expressas nesta publicação são as dos autores e não refletem obrigatoriamente as da UNESCO nem comprometem a Organização.
- Cooperação Técnica

_5 imagem(ns) no slide._

## Outros documentos

_Fonte: AULA 74_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

ATIVIDADE AULA 74

Questão 1

Qual das opções abaixo representa a função de um ComboBox?

A) Mostrar uma lista fixa de itens.

B) Exibir um menu flutuante.

C) Permitir ao usuário selecionar uma opção de uma lista suspensa.

D) Ordenar os elementos na tela.

Resposta: C) Permitir ao usuário selecionar uma opção de uma lista suspensa.

Questão 2

Como o CheckBox pode melhorar a interface de um formulário?

A) Permitindo a seleção de múltiplas opções de maneira clara e intuitiva.

B) Limitando as escolhas do usuário a uma única opção.

C) Ordenando automaticamente os campos do formulário.

D) Exibindo uma mensagem de confirmação.

Resposta: A) Permitindo a seleção de múltiplas opções de maneira clara e intuitiva.
