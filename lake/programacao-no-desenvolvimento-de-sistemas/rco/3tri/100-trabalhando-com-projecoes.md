---
titulo: "Trabalhando com Projeções"
tipo: rco-seed
disciplina: programacao-no-desenvolvimento-de-sistemas
sigla_rco: PDS
trimestre: 3
ordem_rco: 100
serie: 3
aula_rco: "Aula 100"
slides: 23
tem_atividade: false
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/3TRI/100-trabalhando-com-projecoes/100-trabalhando-com-projecoes.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/3TRI/100-trabalhando-com-projecoes/AULA 100_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Trabalhando com Projeções

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO NO
- DESENVOLVIMENTO DE
- SISTEMAS
- 3ª SÉRIE
- Trabalhando com Projeções
- Aula 100

_3 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- DESENVOLVIMENTO DE SISTEMAS
- Nesta aula, vamos:
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store
- Aprender a criar projeções no Spring Data para exibir apenas os dados necessários.

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
- Aprendemos a aplicar paginação e ordenação para organizar grandes volumes de dados de forma eficiente. Com isso, as consultas ficaram mais rápidas e os resultados foram apresentados de maneira intuitiva.

_4 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Camila é uma desenvolvedora que precisa criar uma tela de relatórios para a equipe financeira.
- No entanto, os dados retornados estão carregando
- informações desnecessárias, como endereços
- e dados pessoais.
- Camila quer mostrar apenas o nome e a soma das vendas, mas sem reescrever toda a consulta…

_4 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Pergunta
- Como Camila pode usar projeções no Spring Data para otimizar a consulta e exibir apenas os campos necessários?
- Quem sabe responde!

_5 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Camila pode definir uma interface de projeção personalizada que selecione apenas os atributos que ela precisa, como nome e total de vendas.
- Assim, ela evita sobrecarga de dados, melhora a performance e simplifica o código.

_4 imagem(ns) no slide._

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- Projeções
- São técnicas que permitem recuperar apenas parte dos dados de uma entidade no banco de dados, filtrando campos específicos em vez de trazer a entidade completa. Isso é útil para otimizar consultas e melhorar a performance.

_9 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- Criação da Projeção Definida por interfaces ou classes, uma projeção especifica quais campos devem ser retornados de uma consulta.
- Visualização da Projeção A projeção pode ser aplicada diretamente em métodos de repositórios, retornando apenas os atributos selecionados.

_5 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Em aplicações reais, é comum precisar de apenas alguns atributos de uma entidade para exibir em relatórios ou gráficos.
- Projeções ajudam a otimizar essas consultas, reduzindo o consumo de memória e tempo de processamento.

_4 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- Exemplo
- Em uma loja online, para exibir um resumo do produto, pode-se usar uma projeção que mostre apenas o nome, preço e imagem, em vez de carregar toda a descrição e detalhes técnicos.

_5 imagem(ns) no slide._

### Slide 13

- DESENVOLVIMENTO DE SISTEMAS
- Exemplo
- Vamos criar uma interface de projeção para listar apenas os nomes e idades de usuários. Use o Repl.it ou IntelliJ para testar este exemplo.

_4 imagem(ns) no slide._

### Slide 14

- DESENVOLVIMENTO DE SISTEMAS
- Questão de fixação
- Qual é o principal benefício de usar projeções no Spring Data?
- A) Aumentar a complexidade das consultas.
- B) Reduzir a quantidade de dados retornados.
- C) Melhorar a estética do código.
- D) Substituir métodos JPQL.
- Quem sabe responde!

_4 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- Resposta!
- Qual é o principal benefício de usar projeções no Spring Data?
- A) Aumentar a complexidade das consultas.
- B) Reduzir a quantidade de dados retornados.
- C) Melhorar a estética do código.
- D) Substituir métodos JPQL.
- Resposta correta: B)

_3 imagem(ns) no slide._

### Slide 16

- DESENVOLVIMENTO DE SISTEMAS
- Atividade Prática na Plataforma Alura
- Na plataforma Alura vamos acessar o seguinte curso:
- A recomendação é que você continue esse curso extraclasse, pois ele traz um conteúdo essencial para compreender sobre o referido tema.
- Link para o curso: https://cursos.alura.com.br/course/spring-data-jpa

_6 imagem(ns) no slide._

### Slide 17

- DESENVOLVIMENTO DE SISTEMAS
- Criação da projeção
- 9 minutos
- Link para tarefa: https://cursos.alura.com.br/course/spring-data-jpa/task/83430
- A criação de uma projeção envolve definir interfaces ou classes que especificam apenas os campos desejados de uma entidade, permitindo consultas otimizadas e exibindo dados selecionados sem carregar toda a entidade.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- Visualizando a projeção
- 6 minutos
- Link para tarefa: https://cursos.alura.com.br/course/spring-data-jpa/task/83432
- Visualizar uma projeção significa usar a interface definida em métodos de repositórios ou consultas JPQL para retornar apenas os campos selecionados, exibindo dados de forma mais enxuta e eficiente.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje
- Aprendemos como usar projeções no Spring Data para exibir apenas os campos necessários em consultas. Discutimos como isso pode otimizar o desempenho, proteger dados e tornar o desenvolvimento mais eficiente, continuando a construção das técnicas de organização de dados vistas na aula anterior sobre paginação e ordenação.

_4 imagem(ns) no slide._

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

_Fonte: AULA 100_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

ATIVIDADE AULA 100

Questão 1

Qual é a melhor prática ao usar projeções para exibir relatórios financeiros?

A) Incluir todos os campos da entidade.

B) Selecionar apenas os campos necessários.

C) Dividir os campos em várias consultas separadas.

D) Sempre usar consultas nativas.

Resposta:

Resposta correta: B)

Selecionar apenas os campos necessários evita carregamento de informações desnecessárias e protege dados sensíveis.

Questão 2

Quando você deve evitar o uso de projeções?

A) Quando há muitos campos em uma entidade.

B) Quando a consulta é simples e carrega poucos registros.

C) Quando se deseja retornar entidades completas para edição.

D) Quando se usa JPQL.

Resposta:

Resposta correta: C)

Se você precisa das entidades completas para edição ou operações complexas, é melhor não usar projeções para garantir a integridade dos dados.
