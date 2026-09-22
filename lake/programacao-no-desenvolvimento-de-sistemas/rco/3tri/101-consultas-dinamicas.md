---
titulo: "Consultas dinâmicas"
tipo: rco-seed
disciplina: programacao-no-desenvolvimento-de-sistemas
sigla_rco: PDS
trimestre: 3
ordem_rco: 101
serie: 3
aula_rco: "Aula 101"
slides: 25
tem_atividade: false
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/3TRI/101-consultas-dinamicas/101-consultas-dinamicas.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/3TRI/101-consultas-dinamicas/AULA 101_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Consultas dinâmicas

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO NO
- DESENVOLVIMENTO DE
- SISTEMAS
- 3ª SÉRIE
- Consultas dinâmicas
- Aula 101

_3 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- DESENVOLVIMENTO DE SISTEMAS
- Nesta aula, vamos:
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store
- Criar consultas dinâmicas usando Specifications no Spring Data JPA.

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
- Aprendemos a usar projeções para exibir apenas os campos necessários em consultas, otimizando a performance e protegendo informações sensíveis.
- Hoje, vamos aprofundar o controle sobre as consultas, criando buscas dinâmicas!

_4 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Rafael é um desenvolvedor que trabalha em um sistema de RH e precisa implementar uma tela de busca para filtrar candidatos.
- No entanto, cada recrutador quer um critério diferente: alguns filtram por experiência, outros por localização ou habilidades. Rafael está com dificuldades para atender a todos com uma única consulta.

_4 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Como Rafael pode usar Specifications no Spring Data JPA para construir consultas dinâmicas que atendam a diferentes filtros sem duplicar código?
- Quem sabe responde!

_5 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Rafael pode usar Specifications para criar critérios de busca modulares, que ele combina conforme os filtros escolhidos pelos recrutadores.
- Assim, ele cria uma consulta dinâmica que se adapta facilmente às preferências de cada um.

_4 imagem(ns) no slide._

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- Consultas dinâmicas com Spring Data JPA permitem filtrar dados com base em condições variáveis, usando Specifications para compor critérios modulares. Isso dá flexibilidade ao desenvolvedor para adaptar consultas conforme os requisitos do sistema.

_4 imagem(ns) no slide._

### Slide 10

- Uma Specification define um critério de busca usando a interface Specification<T>, criando um predicado (condição) que será aplicado na consulta.
- Compondo Specifications:
- É possível combinar várias Specifications com métodos como and(), or(), criando consultas complexas e dinâmicas.
- DESENVOLVIMENTO DE SISTEMAS

_4 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Executando a pesquisa dinâmica
- As Specifications são usadas nos repositórios para buscar dados que atendam a diferentes critérios, conforme os filtros aplicados.

_4 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- Specifications permitem que o sistema se adapte a mudanças nos critérios de pesquisa sem precisar reescrever o código, tornando a manutenção mais simples e as buscas mais precisas.

_4 imagem(ns) no slide._

### Slide 13

- DESENVOLVIMENTO DE SISTEMAS
- Exemplo
- Em uma loja online, Specifications podem ser usadas para permitir que os clientes filtrem produtos por preço, categoria e avaliações, combinando esses critérios conforme a seleção do usuário.

_4 imagem(ns) no slide._

### Slide 14

- DESENVOLVIMENTO DE SISTEMAS
- Exemplo
- Neste exemplo, estamos filtrando usuários com "Silva" no nome e idade superior a 18 anos. Essa estrutura modular permite adicionar mais filtros conforme necessário.

_4 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- Questão de fixação
- Qual é a principal função das Specifications no Spring Data JPA?
- A) Definir consultas nativas de banco de dados.
- B) Modularizar critérios de pesquisa para criar consultas dinâmicas.
- C) Substituir repositórios padrão.
- D) Facilitar a visualização de dados.
- Quem sabe responde!

_4 imagem(ns) no slide._

### Slide 16

- DESENVOLVIMENTO DE SISTEMAS
- Resposta!
- Qual é a principal função das Specifications no Spring Data JPA?
- A) Definir consultas nativas de banco de dados.
- B) Modularizar critérios de pesquisa para criar consultas dinâmicas.
- C) Substituir repositórios padrão.
- D) Facilitar a visualização de dados.
- Resposta correta: B)

_3 imagem(ns) no slide._

### Slide 17

- DESENVOLVIMENTO DE SISTEMAS
- Atividade Prática na Plataforma Alura
- Na plataforma Alura vamos acessar o seguinte curso:
- A recomendação é que você continue esse curso extraclasse, pois ele traz um conteúdo essencial para compreender sobre o referido tema.
- Link para o curso: https://cursos.alura.com.br/course/spring-data-jpa

_6 imagem(ns) no slide._

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- Estrutura da Specification
- 14 minutos
- Link para tarefa: https://cursos.alura.com.br/course/spring-data-jpa/task/83433
- A estrutura de uma Specification define critérios de pesquisa usando a interface Specification<T>, criando predicados que filtram dados de forma dinâmica, compondo consultas personalizáveis no Spring Data JPA.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- Compondo Specifications
- 11 minutos
- Link para tarefa: https://cursos.alura.com.br/course/spring-data-jpa/task/83434
- Compor Specifications envolve combinar múltiplos critérios usando métodos como and(), or(), e where(). Isso permite criar consultas dinâmicas e flexíveis, adaptáveis a diferentes filtros no Spring Data JPA.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 20

- DESENVOLVIMENTO DE SISTEMAS
- Executando a pesquisa dinâmica
- 5 minutos
- Link para tarefa: https://cursos.alura.com.br/course/spring-data-jpa/task/83458
- Para executar uma pesquisa dinâmica, use Specification nos métodos de repositórios (findAll(Specification)), aplicando filtros personalizados e combinados conforme as necessidades de busca do usuário.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 21

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje
- Aprendemos a criar consultas dinâmicas usando Specifications no Spring Data JPA, entendendo como compor e combinar critérios para adaptar buscas conforme a necessidade.
- Isso nos dá controle total sobre os resultados, facilitando a criação de consultas complexas e modulares.

_4 imagem(ns) no slide._

### Slide 22

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

### Slide 23

- DESENVOLVIMENTO DE SISTEMAS
- Referências (Imagens)
- Figuras e Imagens:
- https://www.flaticon.com/br
- https://www.istockphoto.com/br
- https://raw.githubusercontent.com/zbtang/React-Native-ViewPager/HEAD/imgs/dotIndicator.gif
- https://storyset.com

_3 imagem(ns) no slide._

### Slide 24

- DESENVOLVIMENTO DE SISTEMAS
- O RCO+Aulas é um projeto da Secretaria de Estado da Educação do Paraná e está em constante revisão. Todos os slides são de uso exclusivo dos professores da Rede Pública de Ensino, com a finalidade específica de aplicação em sala de aula, sendo totalmente vedada a publicização, reutilização, reprodução total ou parcial para quaisquer outros fins.

_4 imagem(ns) no slide._

### Slide 25

- DESENVOLVIMENTO DE SISTEMAS
- Esta publicação tem a cooperação entre a UNESCO e a Secretaria de Estado da Educação e do Esporte do Paraná no âmbito da parceria PRODOC 914BRZ1091, cujo objetivo é trazer soluções inovadoras de gestão da rede pública estadual de educação do Paraná para a melhoria da aprendizagem dos alunos. As indicações de nomes e a apresentação do material ao longo desta publicação não implicam a manifestação de qualquer opinião por parte da UNESCO a respeito da condição jurídica de qualquer país, território, cidade, região ou de suas autoridades, tampouco da delimitação de suas fronteiras ou limites As ideias e opiniões expressas nesta publicação são as dos autores e não refletem obrigatoriamente as da UNESCO nem comprometem a Organização.
- Cooperação Técnica

_4 imagem(ns) no slide._

## Outros documentos

_Fonte: AULA 101_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

ATIVIDADE AULA 101

Questão 1

Qual é a melhor prática ao criar Specifications para diferentes filtros?

A) Reescrever a consulta para cada novo filtro.

B) Criar métodos modulares e reutilizáveis.

C) Usar apenas consultas JPQL.

D) Declarar todos os filtros em uma única classe.

Resposta:

Resposta correta: B)

Criar métodos modulares permite combinar Specifications facilmente, evitando duplicação de código e facilitando a manutenção.

Questão 2

Quando você deve evitar o uso de Specifications no Spring Data JPA?

A) Quando a consulta é muito simples.

B) Quando há muitos filtros.

C) Quando a consulta usa Native Queries.

D) Quando se quer modificar diretamente a entidade.

Resposta:

Resposta correta: A)

Para consultas simples, Specifications podem adicionar complexidade desnecessária. Nesses casos, é melhor usar métodos padrão do repositório.
