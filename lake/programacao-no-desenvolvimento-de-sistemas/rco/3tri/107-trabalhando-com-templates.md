---
titulo: "Trabalhando com Templates"
tipo: rco-seed
disciplina: programacao-no-desenvolvimento-de-sistemas
sigla_rco: PDS
trimestre: 3
ordem_rco: 107
serie: 3
aula_rco: "Aula 107"
slides: 23
tem_atividade: false
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/3TRI/107-trabalhando-com-templates/107-trabalhando-com-templates.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/3TRI/107-trabalhando-com-templates/AULA 107_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Trabalhando com Templates

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO NO
- DESENVOLVIMENTO DE
- SISTEMAS
- 3ª SÉRIE
- Trabalhando com Templates
- Aula 107

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
- Aprender a trabalhar com templates no Spring MVC para estruturar a aparência da aplicação.

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
- Aprendemos sobre Bean Validation no Spring MVC para garantir que dados do usuário atendam a requisitos específicos antes de serem salvos. Hoje, aplicaremos esse conhecimento, garantindo que nossas páginas tenham layouts consistentes usando templates.

_4 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Rafael está desenvolvendo um site de portfólio e quer que todas as páginas tenham o mesmo cabeçalho com o menu de navegação e o mesmo rodapé.
- Ele não sabe se deve copiar e colar o mesmo código em todas as páginas ou se existe uma maneira mais eficiente de organizar essas seções repetidas.

_4 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Pergunta
- Qual é a melhor abordagem para Rafael reutilizar o cabeçalho e o rodapé nas páginas sem precisar repetir o código em cada uma delas?
- Quem sabe responde!

_5 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Rafael pode usar um template base no Thymeleaf e incluir o cabeçalho e o rodapé como fragmentos.
- Ele só precisa definir essas seções uma vez e incluí-las em cada página, garantindo consistência e facilidade de manutenção.

_4 imagem(ns) no slide._

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- Trabalhar com templates em Spring MVC significa criar layouts reutilizáveis para páginas, padronizando elementos visuais, como cabeçalhos e rodapés, e garantindo uma aparência coesa em toda a aplicação.

_4 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- Finalizando o topo
- Um template facilita a padronização desse elemento em várias páginas…
- O cabeçalho (topo) é a parte superior da página que geralmente contém o menu de navegação e o logotipo.
- Um template base define a estrutura da página, incluindo fragmentos (como header e footer) que podem ser reutilizados, evitando duplicação de código.

_5 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Importância
- Templates aumentam a eficiência, pois permitem a reutilização de elementos visuais em várias páginas, mantendo um layout uniforme e simplificando a manutenção. Eles são fundamentais para aplicações que precisam de uma interface consistente e bem organizada.

_4 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- Em um blog, todas as páginas de postagem têm o mesmo
- cabeçalho e rodapé.
- Criando um template base com esses elementos, o desenvolvedor evita duplicação e mantém um design uniforme.

_4 imagem(ns) no slide._

### Slide 13

- DESENVOLVIMENTO DE SISTEMAS
- Exemplo
- Como criar um template base e incluir o cabeçalho e o rodapé

_4 imagem(ns) no slide._

### Slide 14

- DESENVOLVIMENTO DE SISTEMAS
- Questão de fixação
- Qual é a principal vantagem de usar templates no Thymeleaf com Spring MVC?
- A) Tornar a aplicação mais lenta.
- B) Evitar repetição de código em várias páginas.
- C) Dificultar a manutenção de cabeçalhos e rodapés.
- D) Incompatibilidade com Bean Validation.
- Quem sabe responde!

_4 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- Resposta!
- Qual é a principal vantagem de usar templates no Thymeleaf com Spring MVC?
- A) Tornar a aplicação mais lenta.
- B) Evitar repetição de código em várias páginas.
- C) Dificultar a manutenção de cabeçalhos e rodapés.
- D) Incompatibilidade com Bean Validation.
- Resposta correta: B)

_3 imagem(ns) no slide._

### Slide 16

- DESENVOLVIMENTO DE SISTEMAS
- Atividade Prática na Plataforma Alura
- Na plataforma Alura vamos acessar o seguinte curso:
- A recomendação é que você continue esse curso extraclasse, pois ele traz um conteúdo essencial para compreender sobre o referido tema.
- Link para o curso: https://cursos.alura.com.br/course/spring-mvc-thymeleaf-bootstrap

_6 imagem(ns) no slide._

### Slide 17

- DESENVOLVIMENTO DE SISTEMAS
- Criando o template
- 9 minutos
- Link para tarefa: https://cursos.alura.com.br/course/spring-mvc-thymeleaf-bootstrap/task/80880
- Criar um template no Spring MVC envolve definir uma estrutura base, como cabeçalho, rodapé e layout principal. Com Thymeleaf, o template pode ser reutilizado em várias páginas, garantindo consistência visual.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- O que vimos na aula de hoje
- Vimos como usar templates com Spring MVC para criar layouts reutilizáveis e padronizados, organizando elementos como cabeçalho e rodapé para melhorar a consistência da interface. Esta estrutura facilita a manutenção e atualização da aplicação, aplicando o que vimos em validação de dados com Bean Validation à organização visual e de layout.

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

_Fonte: AULA 107_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

ATIVIDADE AULA 107

Questão 1

Como você incluiria um fragmento de cabeçalho em uma página com Thymeleaf?

A) th:text="header"

B) th:replace="header"

C) th:include="fragments/header :: header"

D) th:copy="header"

Resposta:

Resposta correta: C)

O th:include é usado para adicionar um fragmento em uma página, como o cabeçalho, garantindo que ele seja reutilizável.

Questão 2

Qual é o benefício de usar fragmentos no Thymeleaf?

A) Reduzir a quantidade de dados no banco de dados.

B) Facilitar a adição de conteúdo dinâmico em páginas.

C) Substituir funções de controle de navegação.

D) Carregar imagens mais rapidamente.

Resposta:

Resposta correta: B)

Fragmentos permitem incluir partes de HTML, como cabeçalhos e rodapés, em várias páginas, facilitando a padronização e atualização do conteúdo
