---
titulo: "Inclusão de clientes"
tipo: rco-seed
disciplina: programacao-no-desenvolvimento-de-sistemas
sigla_rco: PDS
trimestre: 3
ordem_rco: 81
serie: 3
aula_rco: "Aula 81"
slides: 28
tem_atividade: false
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/3TRI/81-inclusao-de-clientes/81-inclusao-de-clientes.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/3TRI/81-inclusao-de-clientes/AULA 81_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Inclusão de clientes

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO NO
- DESENVOLVIMENTO DE
- SISTEMAS
- 3ª SÉRIE
- Inclusão de clientes
- Aula 81

_3 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- DESENVOLVIMENTO DE SISTEMAS
- Nesta aula, vamos:
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store
- Aprender a transformar a classe de cliente em formato JSON.

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
- Focamos na manutenção dos dados de clientes, entendendo como recuperar, limpar e salvar as informações de forma eficiente. Também vimos como validar os dados antes de salvá-los no banco de dados.

_4 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Ana precisa incluir novos clientes em seu sistema. No entanto, o sistema atual não utiliza JSON para enviar os dados ao servidor. Ela quer saber como pode converter as informações de um cliente para JSON e garantir que a inclusão seja feita corretamente.

_4 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Pergunta
- Como Ana pode transformar os dados de um cliente em JSON e incluir esses dados no sistema de forma eficiente?
- Quem sabe responde!

_5 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Ana pode utilizar a biblioteca Newtonsoft.Json para serializar a classe Cliente em JSON. Depois, ela pode implementar um método de inclusão que utiliza essa conversão para inserir os dados no banco de dados ou enviá-los para uma API.

_4 imagem(ns) no slide._

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- Visão Geral
- JSON (JavaScript Object Notation) é um formato leve de troca de dados amplamente usado em aplicações web e APIs. Serializar uma classe em JSON permite transformar objetos em texto estruturado, ideal para persistência e comunicação entre sistemas.

_4 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- Definição e Aplicação
- JSON e classes: Serializar uma classe significa transformar suas propriedades em um formato legível e estruturado (JSON).
- Método de inclusão: É o procedimento no qual os dados do cliente são capturados, transformados e incluídos no sistema ou banco de dados.

_4 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Importância
- Com a crescente integração entre diferentes sistemas, saber como transformar classes em JSON e utilizá-las para incluir dados é essencial para garantir flexibilidade e eficiência no desenvolvimento de software.

_4 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- Uso
- Ao implementar funcionalidades de inclusão, um desenvolvedor pode transformar dados de formulários em JSON para envio a APIs, permitindo o uso eficiente e padronizado de dados.

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
- Cliente.cs
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
- Qual é o principal benefício de serializar uma classe em JSON?
- A) Facilitar a comunicação entre sistemas
- B) Compactar dados
- C) Reduzir o tamanho do código
- D) Aumentar a velocidade de execução
- Quem sabe responde!

_4 imagem(ns) no slide._

### Slide 21

- DESENVOLVIMENTO DE SISTEMAS
- Resposta!
- Qual é o principal benefício de serializar uma classe em JSON?
- A) Facilitar a comunicação entre sistemas
- B) Compactar dados
- C) Reduzir o tamanho do código
- D) Aumentar a velocidade de execução
- Resposta correta: A) Facilitar a comunicação entre sistemas

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
- Transformando classe em JSON
- 12 minutos
- Link para tarefa: https://cursos.alura.com.br/course/windows-forms-csharp-manipulacao-dados/task/72478
- Transformar uma classe em JSON permite converter os dados de um objeto para um formato legível e intercambiável. No C#, isso é feito usando bibliotecas como o Newtonsoft.Json, facilitando o armazenamento e transmissão.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 24

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje
- Hoje aprendemos como transformar classes em JSON, criar métodos de inclusão e salvar clientes no sistema. Exploramos a importância de utilizar o JSON para facilitar a comunicação entre sistemas e como aplicá-lo no desenvolvimento de software.

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

_4 imagem(ns) no slide._

## Outros documentos

_Fonte: AULA 81_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

ATIVIDADE AULA 81

Questão 1

Qual biblioteca é usada para converter uma classe em JSON no .NET?

A) System.Text.Json

B) Json.NET

C) XMLSerializer

D) EntityFramework

Resposta correta: B) Json.NET

Explicação: Json.NET (Newtonsoft.Json) é uma biblioteca popular para manipulação de JSON no .NET.

Questão 2

Para qual tipo de sistema o formato JSON é mais útil?

A) Sistemas isolados

B) Sistemas de troca de arquivos locais

C) Sistemas que utilizam comunicação entre serviços

D) Sistemas desktop sem conexão de rede

Resposta correta: C) Sistemas que utilizam comunicação entre serviços

Explicação: JSON é amplamente utilizado em sistemas distribuídos que dependem da comunicação entre diferentes plataformas e serviços.
