---
titulo: "Eventos em C#"
tipo: rco-seed
disciplina: programacao-no-desenvolvimento-de-sistemas
sigla_rco: PDS
trimestre: 2
ordem_rco: 60
serie: 3
aula_rco: "Aula 60"
slides: 28
tem_atividade: false
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PDS/2TRI/60-eventos-em-c/60-eventos-em-c.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PDS/2TRI/60-eventos-em-c/AULA 60_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Eventos em C#

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO NO
- DESENVOLVIMENTO DE
- SISTEMAS
- 3ª SÉRIE
- Eventos em C#
- Aula 60

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
- Aprender como criar e configurar eventos em C#.

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
- Conhecemos padrões, botões e caixas de texto no Windows Forms. Aprendemos como criar e configurar labels, botões e text boxes, além de entender a importância dos eventos para a interação do usuário com a interface.

_4 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- João, um estudante de programação, está desenvolvendo uma aplicação Windows Forms para gerenciar uma pequena biblioteca. Ele precisa adicionar eventos para interagir com os usuários, como botões para adicionar, remover e atualizar livros.

_4 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Como João pode implementar eventos nos botões para adicionar, remover e atualizar livros de forma eficiente e intuitiva?
- Quem sabe responde!

_5 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- João deve utilizar eventos como Click nos botões. Ele pode criar métodos que serão executados quando os botões forem clicados, manipulando os dados da biblioteca conforme necessário.

_4 imagem(ns) no slide._

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- Visão Geral
- Eventos em C# são mecanismos que permitem que ações sejam disparadas em resposta a interações do usuário ou outras atividades. Eles são essenciais para criar aplicações interativas.

_4 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- Definição e Aplicação
- Um evento é uma notificação enviada por um objeto quando uma ação ocorre. Em C#, eventos são geralmente associados a controles de interface do usuário, como botões e caixas de texto.

_4 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Importância
- Eventos são fundamentais para desenvolver aplicações interativas e responsivas. Eles permitem que o software reaja às ações do usuário, proporcionando uma melhor experiência.

_4 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- Uso
- Eventos são usados para capturar cliques de botões, mudanças em campos de texto, seleções em listas, entre outros. Isso permite que os desenvolvedores criem interfaces dinâmicas e interativas.

_4 imagem(ns) no slide._

### Slide 13

- DESENVOLVIMENTO DE SISTEMAS
- Tela do forms (forms.cs)
- Utilize o Visual Studio Community

_6 imagem(ns) no slide._

### Slide 14

- DESENVOLVIMENTO DE SISTEMAS
- Código do forms (forms.cs)
- Utilize o Visual Studio Community

_6 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- Código do design do forms (forms.design.cs)
- Utilize o Visual Studio Community

_6 imagem(ns) no slide._

### Slide 16

- DESENVOLVIMENTO DE SISTEMAS
- Código do design do forms (forms.design.cs)
- Utilize o Visual Studio Community

_6 imagem(ns) no slide._

### Slide 17

- DESENVOLVIMENTO DE SISTEMAS
- Código do programa(program.cs)
- Utilize o Visual Studio Community

_6 imagem(ns) no slide._

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- Questão de fixação
- Qual é a função de um evento em C#?
- A) Armazenar dados
- B) Reagir a ações do usuário
- C) Gerar relatórios
- D) Compilar o código
- Quem sabe responde!

_4 imagem(ns) no slide._

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- Questão de fixação
- Qual é a função de um evento em C#?
- A) Armazenar dados
- B) Reagir a ações do usuário
- C) Gerar relatórios
- D) Compilar o código
- Resposta: B) Reagir a ações do usuário

_3 imagem(ns) no slide._

### Slide 20

- DESENVOLVIMENTO DE SISTEMAS
- Atividade Prática na Plataforma Alura
- Na plataforma Alura vamos acessar o seguinte curso:
- A recomendação é que você continue esse curso extraclasse, pois ele traz um conteúdo essencial para compreender sobre o referido tema.
- Link para o curso: https://cursos.alura.com.br/course/windows-forms-csharp-formularios-componentes-eventos

_6 imagem(ns) no slide._

### Slide 21

- DESENVOLVIMENTO DE SISTEMAS
- Construindo um novo formulário
- 21 minutos
- Link para tarefa: https://cursos.alura.com.br/course/windows-forms-csharp-formularios-componentes-eventos/task/69485
- Para construir um novo formulário no Visual Studio, crie um novo arquivo de formulário no projeto. Use o designer para arrastar e soltar controles, e codifique a lógica no arquivo .cs correspondente.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 22

- DESENVOLVIMENTO DE SISTEMAS
- Escolhendo o formulário padrão
- 5 minutos
- Link para tarefa: https://cursos.alura.com.br/course/windows-forms-csharp-formularios-componentes-eventos/task/69486
- Para escolher o formulário padrão em um projeto C#, abra o arquivo `Program.cs` e ajuste o método `Application.Run(new NomeFormulario());` para apontar para o formulário desejado, que será exibido ao iniciar o aplicativo.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 23

- DESENVOLVIMENTO DE SISTEMAS
- Parâmetros de um evento
- 15 minutos
- Link para tarefa: https://cursos.alura.com.br/course/windows-forms-csharp-formularios-componentes-eventos/task/69487
- Os parâmetros de um evento em C# geralmente incluem `sender`, que indica o objeto que disparou o evento, e `EventArgs`, que fornece dados adicionais do evento. Eles ajudam a manipular o comportamento do evento.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 24

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje
- Aprendemos sobre eventos em C#, como construir e configurar um novo formulário, escolher o formulário padrão e entender os parâmetros de um evento. Isso nos preparou para criar aplicações interativas e dinâmicas.

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

_Fonte: AULA 60_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

ATIVIDADE AULA 60

Questão 1

O que acontece quando o método Application.Exit() é chamado em um evento de clique de botão?

A) Fecha apenas o formulário atual, mas mantém o aplicativo em execução.

B) Fecha o formulário atual e inicia um novo formulário.

C) Encerra toda a aplicação e fecha todos os formulários.

D) Minimiza o formulário atual.

Resposta Correta: C

Comentário: O método Application.Exit() encerra toda a aplicação, fechando todos os formulários que estão abertos e finalizando o processo do aplicativo.

Questão 2

Qual é o papel do EventArgs no método que manipula eventos, como no exemplo BtnShowMessage_Click?

A) Especifica o tipo de evento a ser tratado.

B) Contém dados de evento que podem ser usados pelos manipuladores de eventos.

C) Define a aparência dos componentes de interface do usuário.

D) Altera as propriedades dos controles no formulário.

Resposta Correta: B

Comentário: EventArgs é uma classe base para classes que contêm dados de eventos. Ele é usado em métodos de manipulador de eventos para passar informações sobre o evento que ocorreu, embora, no caso de eventos padrão como cliques de botão, EventArgs geralmente não contenha informações adicionais específicas.
