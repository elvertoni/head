---
titulo: "Máscaras em C#"
tipo: rco-seed
disciplina: programacao-no-desenvolvimento-de-sistemas
sigla_rco: PDS
trimestre: 2
ordem_rco: 61
serie: 3
aula_rco: "Aula 61"
slides: 28
tem_atividade: false
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PDS/2TRI/61-mascaras-em-c/61-mascaras-em-c.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PDS/2TRI/61-mascaras-em-c/AULA 61_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Máscaras em C#

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO NO
- DESENVOLVIMENTO DE
- SISTEMAS
- 3ª SÉRIE
- Máscaras em C#
- Aula 61

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
- Exploraremos as máscaras em C#, aprendendo a aplicá-las em campos de entrada de dados para garantir formatação consistente e validação correta.

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
- Exploramos eventos em C#, incluindo a construção de formulários, escolha do formulário padrão e parâmetros de eventos. Aprendemos como manipular eventos para responder a ações do usuário.

_4 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Ana, uma desenvolvedora júnior, está criando um sistema de cadastro de clientes que exige entradas como CPF e número de telefone. Ela precisa garantir que os dados sejam inseridos no formato correto para evitar erros e facilitar a validação.

_4 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Duas Soluções Possíveis:
- Solução 1: Ana utiliza máscaras de entrada para formatar automaticamente os dados de CPF e telefone.
- Solução 2: Ana decide não usar máscaras e permite que os usuários insiram os dados livremente.
- Quem sabe responde!

_5 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Solução 1 é correta: O uso de máscaras ajuda a padronizar a entrada de dados e reduz a chance de erros de formatação, facilitando a validação.
- Solução 2 é incorreta: Permitir entrada livre sem formatação pode levar a inconsistências nos dados e aumentar a complexidade da validação.

_4 imagem(ns) no slide._

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- Visão Geral
- As máscaras em C# são utilizadas para formatar campos de entrada de dados, garantindo que informações como números de telefone, CPFs e datas sejam inseridas em um formato padrão.

_4 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- Definição e Aplicação
- Máscaras são configurações aplicadas a controles de entrada, como MaskedTextBox, para definir um formato específico para os dados inseridos. Isso ajuda a validar e processar dados de maneira eficiente.

_4 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Importância
- O uso de máscaras é essencial para assegurar a integridade e consistência dos dados inseridos pelos usuários, reduzindo erros e facilitando a validação e o processamento posterior.

_4 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- Uso
- Por exemplo, em sistemas de cadastro, é comum usar máscaras para CPF, CNPJ, números de telefone, etc. Isso garante que todos os usuários insiram os dados no mesmo formato.

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
- O que é uma máscara de entrada em C#?
- A) Uma ferramenta para proteger dados sensíveis.
- B) Um formato pré-definido para entradas de dados.
- C) Uma função para armazenar dados.
- D) Um tipo de banco de dados.
- Quem sabe responde!

_4 imagem(ns) no slide._

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- Questão de fixação
- O que é uma máscara de entrada em C#?
- A) Uma ferramenta para proteger dados sensíveis.
- B) Um formato pré-definido para entradas de dados.
- C) Uma função para armazenar dados.
- D) Um tipo de banco de dados.
- Resposta correta: B)

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
- Máscaras
- 11 minutos
- Link para tarefa: https://cursos.alura.com.br/course/windows-forms-csharp-formularios-componentes-eventos/task/69490
- Máscaras em C# são usadas em campos de entrada para garantir que os dados sejam inseridos em um formato específico, como números de telefone ou CPFs. Elas ajudam a padronizar e validar a entrada de dados.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 22

- DESENVOLVIMENTO DE SISTEMAS
- Manipulando as máscaras
- 17 minutos
- Link para tarefa: https://cursos.alura.com.br/course/windows-forms-csharp-formularios-componentes-eventos/task/69491
- Manipular máscaras em C# envolve ajustar formatos de entrada para campos específicos, como datas ou números de telefone. Isso garante que os dados sejam inseridos corretamente, facilitando a validação e o processamento.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 23

- DESENVOLVIMENTO DE SISTEMAS
- Máscara com validação
- 9 minutos
- Link para tarefa: https://cursos.alura.com.br/course/windows-forms-csharp-formularios-componentes-eventos/task/69492
- Máscaras com validação em C# garantem que os dados inseridos sigam um formato específico, como CPF ou telefone. Combinam formatação com verificações de validade, melhorando a precisão e a integridade dos dados.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 24

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje
- Exploramos o uso de máscaras em C# para garantir a entrada de dados no formato correto, aprendendo a manipular e validar máscaras em campos de texto. Essas técnicas são essenciais para garantir a consistência e integridade dos dados inseridos pelos usuários, facilitando a validação e processamento posterior.

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

_Fonte: AULA 61_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

ATIVIDADE AULA 61

Questão 1

Como a máscara "000.000.000-00" no MaskedTextBox ajuda na entrada de dados?

A) Ela corrige automaticamente os erros de dados.

B) Limita a entrada para o formato de CPF no Brasil.

C) Permite qualquer tipo de entrada de dados.

D) Cria um novo campo de dados.

Resposta correta: B) Limita a entrada para o formato de CPF no Brasil. Essa máscara garante que os CPFs sejam inseridos no formato correto.

Questão 2

Qual componente em C# é geralmente utilizado para aplicar máscaras em campos de texto?

A) TextBox

B) MaskedTextBox

C) Label

D) ComboBox

Resposta correta: B) MaskedTextBox. Esse componente é projetado especificamente para aplicar máscaras de entrada em campos de texto.
