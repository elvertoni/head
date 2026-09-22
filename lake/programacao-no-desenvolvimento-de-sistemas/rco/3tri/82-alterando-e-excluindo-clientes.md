---
titulo: "Alterando e excluindo clientes"
tipo: rco-seed
disciplina: programacao-no-desenvolvimento-de-sistemas
sigla_rco: PDS
trimestre: 3
ordem_rco: 82
serie: 3
aula_rco: "Aula 82"
slides: 33
tem_atividade: false
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/3TRI/82-alterando-e-excluindo-clientes/82-alterando-e-excluindo-clientes.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/3TRI/82-alterando-e-excluindo-clientes/AULA 82_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Alterando e excluindo clientes

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO NO
- DESENVOLVIMENTO DE
- SISTEMAS
- 3ª SÉRIE
- Alterando e excluindo clientes
- Aula 82

_3 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- DESENVOLVIMENTO DE SISTEMAS
- Nesta aula, vamos:
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store
- Aprender a buscar, alterar e excluir clientes cadastrados em um sistema Windows Forms

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
- Aprendemos a incluir novos clientes em nosso sistema usando Windows Forms e a converter as informações em JSON para facilitar o envio de dados para APIs ou bancos de dados. Agora, vamos nos concentrar em como buscar esses dados, alterá-los e, se necessário, excluí-los, mantendo a consistência da base de dados.

_4 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Laura é uma administradora de um sistema de clientes que precisa atualizar informações incorretas de um cliente e, em alguns casos, excluir dados desatualizados.

_4 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Pergunta
- Soluções Possíveis:
- Laura pode usar um sistema que permite buscar um cliente pelo nome ou ID, carregar os dados no formulário, alterar as informações e salvá-las de volta no banco de dados.
- Ou Laura pode optar por recriar todo o cadastro do cliente ao invés de buscar e alterar os dados, o que pode ser ineficiente.
- Quem sabe responde!

_4 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- A primeira opção é a correta, pois sistemas bem projetados permitem a busca, edição e exclusão de registros de maneira simples, garantindo a integridade dos dados.

_4 imagem(ns) no slide._

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- Visão Geral
- A manipulação de dados existentes, como buscar, alterar e excluir informações, é um passo essencial para manter um sistema atualizado e eficiente. Quando um cliente muda de endereço ou de telefone, por exemplo, o sistema precisa permitir alterações de forma rápida e segura.

_4 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- Definição e Aplicação
- Buscar um Cliente: Permitir que o sistema localize clientes por parâmetros como nome, ID ou CPF.
- Alterar Cliente: Carregar as informações no formulário, permitir alterações e salvar as modificações.
- Excluir Cliente: Remover os dados de forma segura, garantindo que o sistema seja atualizado corretamente.

_4 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Importância
- A exclusão e alteração de dados garante que o sistema esteja sempre com informações atualizadas e precisas. Além disso, permite a limpeza de dados desnecessários, melhorando a performance e organização.

_4 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- Uso
- Na prática, você encontrará essas operações em diversos sistemas, desde CRMs até sistemas bancários. A busca por clientes, edição de dados e exclusão são funcionalidades básicas de qualquer sistema de gestão.

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
- MainForm
- .Designer.cs
- Utilize o visual studio comunity

_5 imagem(ns) no slide._

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- MainForm
- .Designer.cs
- Utilize o visual studio comunity

_5 imagem(ns) no slide._

### Slide 20

- DESENVOLVIMENTO DE SISTEMAS
- Program.cs
- Utilize o visual studio comunity

_5 imagem(ns) no slide._

### Slide 21

- DESENVOLVIMENTO DE SISTEMAS
- Questão de fixação
- O que deve ser considerado ao alterar os dados de um cliente no sistema?
- A) Somente os dados obrigatórios.
- B) Qualquer dado, sem verificação.
- C) Verificar a integridade dos dados antes de salvar.
- D) Atualizar apenas os dados que foram modificados.
- Quem sabe responde!

_4 imagem(ns) no slide._

### Slide 22

- DESENVOLVIMENTO DE SISTEMAS
- Resposta!
- O que deve ser considerado ao alterar os dados de um cliente no sistema?
- A) Somente os dados obrigatórios.
- B) Qualquer dado, sem verificação.
- C) Verificar a integridade dos dados antes de salvar.
- D) Atualizar apenas os dados que foram modificados.
- Resposta Correta: C

_3 imagem(ns) no slide._

### Slide 23

- DESENVOLVIMENTO DE SISTEMAS
- Atividade Prática na Plataforma Alura
- Na plataforma Alura vamos acessar o seguinte curso:
- A recomendação é que você continue esse curso extraclasse, pois ele traz um conteúdo essencial para compreender sobre o referido tema.
- Link para o curso: https://cursos.alura.com.br/course/windows-forms-csharp-manipulacao-dados

_6 imagem(ns) no slide._

### Slide 24

- DESENVOLVIMENTO DE SISTEMAS
- Transformando classe em JSON
- 12 minutos
- Link para tarefa: https://cursos.alura.com.br/course/windows-forms-csharp-manipulacao-dados/task/72483
- Buscar um cliente em um sistema envolve localizar seus dados no banco de dados ou outra fonte, geralmente através de um ID, nome ou CPF. Isso permite que as informações sejam carregadas para visualização ou edição.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 25

- DESENVOLVIMENTO DE SISTEMAS
- Escrevendo no formulário
- 17 minutos
- Link para tarefa: https://cursos.alura.com.br/course/windows-forms-csharp-manipulacao-dados/task/72484
- Escrever no formulário significa preencher os campos da interface com os dados de um cliente, como nome, endereço e telefone. Isso facilita a visualização e edição, permitindo que os usuários modifiquem as informações.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 26

- DESENVOLVIMENTO DE SISTEMAS
- Apagando o cliente
- 8 minutos
- Link para tarefa: https://cursos.alura.com.br/course/windows-forms-csharp-manipulacao-dados/task/72485
- Apagar um cliente envolve a remoção de seus dados do sistema ou banco de dados. Isso pode ser feito confirmando a exclusão com o usuário e garantindo que os dados sejam removidos de forma segura e permanente.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 27

- DESENVOLVIMENTO DE SISTEMAS
- Melhorando o processo de exclusão
- 11 minutos
- Link para tarefa: https://cursos.alura.com.br/course/windows-forms-csharp-manipulacao-dados/task/72486
- Melhorar o processo de exclusão envolve adicionar confirmações, realizar backups e garantir que a remoção seja definitiva. Isso evita exclusões acidentais e permite uma recuperação caso ocorra algum erro.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 28

- DESENVOLVIMENTO DE SISTEMAS
- Alterando o cliente
- 9 minutos
- Link para tarefa: https://cursos.alura.com.br/course/windows-forms-csharp-manipulacao-dados/task/72487
- Alterar o cliente envolve buscar os dados existentes, permitir modificações no formulário e atualizar o banco de dados com as novas informações. Esse processo garante que as mudanças sejam salvas corretamente.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 29

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje
- Aprendemos a buscar, alterar e excluir clientes no sistema de cadastro. Essas operações são essenciais para a manutenção de um sistema eficiente e atualizado. O próximo passo é aprofundar-se na validação de dados e na otimização da performance do sistema com essas operações.

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

_4 imagem(ns) no slide._

## Outros documentos

_Fonte: AULA 82_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

ATIVIDADE AULA 82

Questão 1

Por que é importante permitir a alteração de dados no formulário de clientes?

A) Para manter as informações atualizadas e relevantes.

B) Para excluir dados antigos de forma rápida.

C) Para criar novos registros com facilidade.

D) Para aumentar a segurança do sistema.

Resposta Correta: A

Explicação: Manter as informações atualizadas garante que as decisões baseadas nesses dados sejam precisas.

Questão 2

Qual é o impacto de não permitir a exclusão de dados no sistema?

A) Maior volume de dados desatualizados.

B) Redução no uso de recursos do sistema.

C) Melhora na segurança do sistema.

D) Dificuldade em alterar registros futuros.

Resposta Correta: A

Explicação: Sem a exclusão de dados obsoletos, o sistema pode se tornar sobrecarregado e ineficiente, armazenando informações desnecessárias.
