---
titulo: "Trabalhando com Bean Validation"
tipo: rco-seed
disciplina: programacao-no-desenvolvimento-de-sistemas
sigla_rco: PDS
trimestre: 3
ordem_rco: 106
serie: 3
aula_rco: "Aula 106"
slides: 23
tem_atividade: false
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/3TRI/106-trabalhando-com-bean-validation/106-trabalhando-com-bean-validation.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/3TRI/106-trabalhando-com-bean-validation/AULA 106_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Trabalhando com Bean Validation

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO NO
- DESENVOLVIMENTO DE
- SISTEMAS
- 3ª SÉRIE
- Trabalhando com Bean Validation
- Aula 106

_3 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- DESENVOLVIMENTO DE SISTEMAS
- Nesta aula, vamos:
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store
- Aprender a validar dados de formulários em Java usando Bean Validation.

_7 imagem(ns) no slide._

### Slide 4

- DESENVOLVIMENTO DE SISTEMAS
- ATENÇÃO PROFESSOR!
- O Material aqui apresentado, segue a análise do plano de curso contemplando os componentes curriculares e seus objetos de conhecimento, sendo assim, você tem liberdade para customizar o material conforme seu contexto para maior aproveitamento do conteúdo. Em caso de falta ou indisponibilidade de acesso à internet no local de aula, você poderá utilizar os seguintes artigos para criação de material complementar para auxiliar na aula:
- Leitura/Recursos Adicionais:
- Spring Initializr (start.spring.io): Uma ferramenta online que permite criar projetos Spring Boot rapidamente. Você pode selecionar dependências como Spring Data JPA e H2 Database para começar.

_5 imagem(ns) no slide._

### Slide 5

- DESENVOLVIMENTO DE SISTEMAS
- Na aula anterior…
- Trabalhamos com formulários em Spring MVC, aprendendo a capturar e salvar pedidos dos usuários. Agora, vamos focar na validação dessas informações para garantir que os dados sejam inseridos corretamente antes do processamento.

_4 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Ana está desenvolvendo um sistema de pedidos, mas ao testar, percebe que dados incorretos foram salvos no banco.
- Ela precisa garantir que os campos estejam corretamente preenchidos.
- Como Ana pode garantir que os campos obrigatórios sejam validados e mensagens de erro adequadas sejam exibidas ao usuário?
- Quem sabe responde!

_5 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Resposta…
- Ana pode usar Bean Validation para aplicar restrições nos campos e mostrar mensagens de erro quando os dados estiverem inválidos.

_4 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Bean Validation
- É uma especificação em Java para garantir a integridade dos dados em aplicações. Ele permite adicionar anotações nos modelos para definir regras de validação.

_4 imagem(ns) no slide._

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- Definição e Aplicação
- O Bean Validation ajuda a evitar a inserção de dados incorretos ou incompletos. Ele pode ser aplicado diretamente nas classes de modelo, utilizando anotações como @NotNull, @Size, e @Email.

_5 imagem(ns) no slide._

### Slide 10

- Importância
- A validação de dados garante que o sistema
- receba apenas informações válidas, prevenindo
- erros e melhorando a confiabilidade da aplicação.
- DESENVOLVIMENTO DE SISTEMAS

_5 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Uso
- Em um formulário de pedido, podemos garantir que o nome do cliente não seja vazio, o valor seja numérico, e o email seja formatado corretamente.

_4 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- Exemplo
- Validação de Dados com Bean Validation: Garantindo Qualidade nos Pedidos

_4 imagem(ns) no slide._

### Slide 13

- DESENVOLVIMENTO DE SISTEMAS
- Questão de fixação
- Qual anotação valida se um campo não está vazio em Java?
- A) @Size
- B) @Email
- C) @NotNull
- D) @Pattern
- Quem sabe responde!

_4 imagem(ns) no slide._

### Slide 14

- DESENVOLVIMENTO DE SISTEMAS
- Resposta!
- Qual anotação valida se um campo não está vazio em Java?
- A) @Size
- B) @Email
- C) @NotNull
- D) @Pattern
- Resposta Correta: C) @NotNull

_3 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- Atividade Prática na Plataforma Alura
- Na plataforma Alura vamos acessar o seguinte curso:
- A recomendação é que você continue esse curso extraclasse, pois ele traz um conteúdo essencial para compreender sobre o referido tema.
- Link para o curso: https://cursos.alura.com.br/course/spring-mvc-thymeleaf-bootstrap

_6 imagem(ns) no slide._

### Slide 16

- DESENVOLVIMENTO DE SISTEMAS
- Validação do pedido
- 12 minutos
- Link para tarefa: https://cursos.alura.com.br/course/spring-mvc-thymeleaf-bootstrap/task/80877
- A validação do pedido garante que os dados inseridos pelo usuário, como nome, quantidade e email, estejam corretos antes de serem processados. Usando Bean Validation, podemos definir regras e evitar erros.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 17

- DESENVOLVIMENTO DE SISTEMAS
- Mensagens de erro
- 11 minutos
- Link para tarefa: https://cursos.alura.com.br/course/spring-mvc-thymeleaf-bootstrap/task/80878
- As mensagens de erro são fundamentais para orientar o usuário quando há falhas na validação de dados. Elas informam de forma clara e específica quais campos precisam ser corrigidos, melhorando a experiência.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje
- Aprendemos como usar Bean Validation para garantir a qualidade dos dados inseridos nos formulários, focando em validar pedidos e exibir mensagens de erro quando necessário. A validação de dados melhora a segurança e a confiabilidade da aplicação.

_4 imagem(ns) no slide._

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- Pronto para desbloquear sua carreira em TI?
- Está perdido estudando mas não sabe por onde começar? Se a resposta é sim, você está no lugar certo! Descubra as estratégias e ferramentas essenciais para te ajudar a desbloquear seu potencial em TI e buscar sua primeira vaga de emprego no setor!
- Este e-book é um guia completo para quem busca começar pelos melhores caminhos para se tornar um excelente profissional de TI, ensinando a identificar perfis profissionais, aplicar técnicas de estudo eficazes, transformar teoria em prática, e aumentar a visibilidade de seu trabalho no mercado de trabalho. Ideal para novatos e profissionais em transição.
- E o melhor, ele pode ser seu, inteiramente grátis!

_7 imagem(ns) no slide._

### Slide 20

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

### Slide 21

- DESENVOLVIMENTO DE SISTEMAS
- Referências (Imagens)
- Figuras e Imagens:
- https://www.flaticon.com/br
- https://www.istockphoto.com/br
- https://raw.githubusercontent.com/zbtang/React-Native-ViewPager/HEAD/imgs/dotIndicator.gif
- https://storyset.com

_3 imagem(ns) no slide._

### Slide 22

- DESENVOLVIMENTO DE SISTEMAS
- O RCO+Aulas é um projeto da Secretaria de Estado da Educação do Paraná e está em constante revisão. Todos os slides são de uso exclusivo dos professores da Rede Pública de Ensino, com a finalidade específica de aplicação em sala de aula, sendo totalmente vedada a publicização, reutilização, reprodução total ou parcial para quaisquer outros fins.

_4 imagem(ns) no slide._

### Slide 23

- DESENVOLVIMENTO DE SISTEMAS
- Esta publicação tem a cooperação entre a UNESCO e a Secretaria de Estado da Educação e do Esporte do Paraná no âmbito da parceria PRODOC 914BRZ1091, cujo objetivo é trazer soluções inovadoras de gestão da rede pública estadual de educação do Paraná para a melhoria da aprendizagem dos alunos. As indicações de nomes e a apresentação do material ao longo desta publicação não implicam a manifestação de qualquer opinião por parte da UNESCO a respeito da condição jurídica de qualquer país, território, cidade, região ou de suas autoridades, tampouco da delimitação de suas fronteiras ou limites As ideias e opiniões expressas nesta publicação são as dos autores e não refletem obrigatoriamente as da UNESCO nem comprometem a Organização.
- Cooperação Técnica

_4 imagem(ns) no slide._

## Outros documentos

_Fonte: AULA 106_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

ATIVIDADE AULA 106

Questão 1

Como você pode garantir que o campo "quantidade" de um pedido seja um número maior que zero?

A) @NotNull

B) @Min(1)

C) @Max(0)

D) @Size

Resposta Correta: B) @Min(1)

Comentário: A anotação @Min(1) define o valor mínimo para o campo.

Questão 2

Qual anotação é usada para garantir que um campo "nome" tenha no mínimo 2 caracteres?

A) @Min(2)

B) @Size(min=2)

C) @Length(min=2)

D) @Pattern(min=2)

Resposta Correta: B) @Size(min=2)

Comentário: A anotação @Size(min=2) garante que o tamanho mínimo da string seja 2 caracteres.
