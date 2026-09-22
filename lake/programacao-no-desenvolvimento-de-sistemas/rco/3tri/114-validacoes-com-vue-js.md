---
titulo: "Validações com Vue.js"
tipo: rco-seed
disciplina: programacao-no-desenvolvimento-de-sistemas
sigla_rco: PDS
trimestre: 3
ordem_rco: 114
serie: 3
aula_rco: "Aula 114"
slides: 29
tem_atividade: false
tem_pratica: false
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/3TRI/114-validacoes-com-vue-js/114-validacoes-com-vue-js.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PDS/3TRI/114-validacoes-com-vue-js/AULA 114_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Validações com Vue.js

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- PROGRAMAÇÃO NO
- DESENVOLVIMENTO DE
- SISTEMAS
- 3ª SÉRIE
- Validações com Vue.js
- Aula 114

_3 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- DESENVOLVIMENTO DE SISTEMAS
- Nesta aula, vamos:
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store
- Aprender a aplicar validações com Vue.js, garantindo que os dados dos usuários estejam corretos antes de serem enviados ao servidor.

_7 imagem(ns) no slide._

### Slide 4

- DESENVOLVIMENTO DE SISTEMAS
- ATENÇÃO PROFESSOR!
- O Material aqui apresentado, segue a análise do plano de curso contemplando os componentes curriculares e seus objetos de conhecimento, sendo assim, você tem liberdade para customizar o material conforme seu contexto para maior aproveitamento do conteúdo. Em caso de falta ou indisponibilidade de acesso à internet no local de aula, você poderá utilizar os seguintes artigos para criação de material complementar para auxiliar na aula:
- Leitura/Recursos Adicionais:
- Spring Tool Suite (STS): IDE focada em projetos Spring que facilita a integração de APIs, ideal para configurar AJAX com Spring MVC. Visual Studio Code: Editor de código leve com suporte para JavaScript e Vue.js, tornando o desenvolvimento front-end rápido e acessível. Postman: Ferramenta para testar as APIs e verificar o retorno de dados para AJAX, ajudando a depurar os endpoints com rapidez.

_5 imagem(ns) no slide._

### Slide 5

- DESENVOLVIMENTO DE SISTEMAS
- Na aula anterior…
- Vimos como o AJAX e o Vue.js criam interatividade em uma aplicação web, permitindo a atualização de partes da página sem recarregar. Hoje, usaremos Vue.js para validar dados em tempo real e tornar a aplicação mais confiável e amigável.

_4 imagem(ns) no slide._

### Slide 6

- DESENVOLVIMENTO DE SISTEMAS
- Para pensarmos juntos!
- Carla está criando um formulário de cadastro de produtos para sua loja online, mas quer garantir que todas as informações inseridas estejam corretas, como preço, quantidade e nome.
- Ela também quer exibir uma mensagem de erro caso algum dado esteja incorreto.

_4 imagem(ns) no slide._

### Slide 7

- DESENVOLVIMENTO DE SISTEMAS
- Pergunta
- Como Carla pode configurar validações com Vue.js para garantir que os dados inseridos sejam válidos e ajudar o usuário a corrigir erros com mensagens claras?
- Quem sabe responde!

_5 imagem(ns) no slide._

### Slide 8

- DESENVOLVIMENTO DE SISTEMAS
- Resposta
- Carla pode usar Vue.js para verificar os dados enquanto o usuário digita, aplicando validadores para verificar informações como tipo e limites de valores.
- Além disso, ela pode exibir mensagens de erro personalizadas ao lado dos campos, informando o que está incorreto.

_4 imagem(ns) no slide._

### Slide 9

- DESENVOLVIMENTO DE SISTEMAS
- Validações com Vue.js são usadas para verificar se os dados inseridos pelos usuários são corretos, antes de serem enviados ao servidor.
- Esse processo ajuda a melhorar a confiabilidade dos dados e garante que o usuário forneça informações completas e precisas.

_4 imagem(ns) no slide._

### Slide 10

- DESENVOLVIMENTO DE SISTEMAS
- Definição e Aplicação
- Recuperando valores com JavaScript
- No Vue.js, é possível capturar os valores dos campos do formulário e verificar se estão corretos.
- Criando ofertas
- Com o Vue.js, o usuário pode configurar campos dinâmicos, como ofertas de desconto, que dependem de condições, como valor mínimo de compra.

_4 imagem(ns) no slide._

### Slide 11

- DESENVOLVIMENTO DE SISTEMAS
- Aplicando validadores
- Validadores são funções que verificam dados específicos, como números, formatos de e-mail, limites de texto etc.
- Apresentando mensagens de erro
- Vue.js permite exibir mensagens de erro personalizadas, informando ao usuário qual campo precisa de atenção e por quê.

_4 imagem(ns) no slide._

### Slide 12

- DESENVOLVIMENTO DE SISTEMAS
- As validações evitam que dados incorretos ou incompletos sejam enviados, o que poupa tempo ao usuário e evita erros no servidor.
- Elas melhoram a usabilidade e dão mais confiança ao usuário ao ver que o sistema fornece feedback claro.

_4 imagem(ns) no slide._

### Slide 13

- DESENVOLVIMENTO DE SISTEMAS
- Em um sistema de reservas, o Vue.js pode validar se uma data é futura e se o campo de e-mail está no formato correto, permitindo que o usuário corrija qualquer erro antes de enviar a solicitação.

_4 imagem(ns) no slide._

### Slide 14

- DESENVOLVIMENTO DE SISTEMAS
- Exemplo
- Exemplo de validação simples com Vue.js, verificando se um campo de nome está preenchido e exibindo uma mensagem de erro se estiver vazio

_4 imagem(ns) no slide._

### Slide 15

- DESENVOLVIMENTO DE SISTEMAS
- Exemplo
- Aqui, o campo "Nome" é validado para garantir que não esteja vazio. Se o usuário tentar enviar o formulário sem preencher o nome, uma mensagem de erro será exibida.

_4 imagem(ns) no slide._

### Slide 16

- DESENVOLVIMENTO DE SISTEMAS
- Questão de fixação
- Qual é a função principal das validações em uma aplicação com Vue.js?
- A) Recarregar a página a cada nova entrada.
- B) Garantir que os dados inseridos estejam corretos antes do envio.
- C) Substituir formulários HTML.
- D) Alterar o design da página.
- Quem sabe responde!

_4 imagem(ns) no slide._

### Slide 17

- DESENVOLVIMENTO DE SISTEMAS
- Resposta!
- Qual é a função principal das validações em uma aplicação com Vue.js?
- A) Recarregar a página a cada nova entrada.
- B) Garantir que os dados inseridos estejam corretos antes do envio.
- C) Substituir formulários HTML.
- D) Alterar o design da página.
- Resposta correta: B)

_3 imagem(ns) no slide._

### Slide 18

- DESENVOLVIMENTO DE SISTEMAS
- Atividade Prática na Plataforma Alura
- Na plataforma Alura vamos acessar o seguinte curso:
- A recomendação é que você continue esse curso extraclasse, pois ele traz um conteúdo essencial para compreender sobre o referido tema.
- Link para o curso: https://cursos.alura.com.br/course/spring-mvc-security-rest-vuejs-ajax

_6 imagem(ns) no slide._

### Slide 19

- DESENVOLVIMENTO DE SISTEMAS
- Recuperando valores com JavaScript
- 10 minutos
- Link para tarefa: https://cursos.alura.com.br/course/spring-mvc-security-rest-vuejs-ajax/task/81147
- Recuperar valores com JavaScript permite capturar dados inseridos em campos de formulários de forma dinâmica. Com Vue.js, o v-model facilita essa tarefa, sincronizando os valores diretamente com variáveis, o que agiliza a validação e manipulação de dados.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 20

- DESENVOLVIMENTO DE SISTEMAS
- Aplicando validadores
- 7 minutos
- Link para tarefa: https://cursos.alura.com.br/course/spring-mvc-security-rest-vuejs-ajax/task/81149
- Aplicar validadores em Vue.js garante que os dados atendam a certos critérios antes de serem enviados. Eles verificam se os campos estão preenchidos corretamente, como e-mail ou números, evitando erros e melhorando a qualidade dos dados.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 21

- DESENVOLVIMENTO DE SISTEMAS
- Apresentando mensagens de erro
- 14 minutos
- Link para tarefa: https://cursos.alura.com.br/course/spring-mvc-security-rest-vuejs-ajax/task/81150
- Apresentar mensagens de erro em Vue.js orienta o usuário a corrigir dados incorretos em tempo real. Com v-if, mensagens personalizadas aparecem ao detectar erros, melhorando a experiência e prevenindo falhas no envio de informações.
- Atividade no portal Alura

_7 imagem(ns) no slide._

### Slide 22

- O que vimos na aula de hoje
- Exploramos como aplicar validações com Vue.js para garantir a integridade dos dados antes do envio. Aprendemos a recuperar valores, criar ofertas dinâmicas, aplicar validadores e exibir mensagens de erro claras para o usuário. Essas práticas não só melhoram a experiência do usuário, mas também asseguram que a aplicação receba dados precisos e completos, facilitando o gerenciamento e a segurança dos dados.
- DESENVOLVIMENTO DE SISTEMAS

_4 imagem(ns) no slide._

### Slide 23

_(sem texto)_

_1 imagem(ns) no slide._

### Slide 24

_(sem texto)_

_1 imagem(ns) no slide._

### Slide 25

- DESENVOLVIMENTO DE SISTEMAS
- Pronto para desbloquear sua carreira de TI?
- Está perdido estudando mas não sabe por onde começar? Se a resposta é sim, você está no lugar certo! Descubra as estratégias e ferramentas essenciais para te ajudar a desbloquear seu potencial em TI e buscar sua primeira vaga de emprego no setor!
- Este e-book é um guia completo para quem busca começar pelos melhores caminhos para se tornar um excelente profissional de TI, ensinando a identificar perfis profissionais, aplicar técnicas de estudo eficazes, transformar teoria em prática, e aumentar a visibilidade de seu trabalho no mercado de trabalho. Ideal para novatos e profissionais em transição.
- E o melhor, ele pode ser seu, inteiramente grátis!
- Basta clicar AQUI e realizar o seu cadastro com o seu @escola!

_5 imagem(ns) no slide._

### Slide 26

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

### Slide 27

- DESENVOLVIMENTO DE SISTEMAS
- Referências (Imagens)
- Figuras e Imagens:
- https://www.flaticon.com/br
- https://www.istockphoto.com/br
- https://raw.githubusercontent.com/zbtang/React-Native-ViewPager/HEAD/imgs/dotIndicator.gif
- https://storyset.com

_3 imagem(ns) no slide._

### Slide 28

- DESENVOLVIMENTO DE SISTEMAS
- O RCO+Aulas é um projeto da Secretaria de Estado da Educação do Paraná e está em constante revisão. Todos os slides são de uso exclusivo dos professores da Rede Pública de Ensino, com a finalidade específica de aplicação em sala de aula, sendo totalmente vedada a publicização, reutilização, reprodução total ou parcial para quaisquer outros fins.

_4 imagem(ns) no slide._

### Slide 29

- DESENVOLVIMENTO DE SISTEMAS
- Esta publicação tem a cooperação entre a UNESCO e a Secretaria de Estado da Educação e do Esporte do Paraná no âmbito da parceria PRODOC 914BRZ1091, cujo objetivo é trazer soluções inovadoras de gestão da rede pública estadual de educação do Paraná para a melhoria da aprendizagem dos alunos. As indicações de nomes e a apresentação do material ao longo desta publicação não implicam a manifestação de qualquer opinião por parte da UNESCO a respeito da condição jurídica de qualquer país, território, cidade, região ou de suas autoridades, tampouco da delimitação de suas fronteiras ou limites As ideias e opiniões expressas nesta publicação são as dos autores e não refletem obrigatoriamente as da UNESCO nem comprometem a Organização.
- Cooperação Técnica

_5 imagem(ns) no slide._

## Outros documentos

_Fonte: AULA 114_PROGRAMAÇÃO NO DESENVOLVIMENTO DE SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação No Desenvolvimento de Sistemas

3ª SÉRIE

ATIVIDADE AULA 114

Questão 1

Qual é a principal vantagem de validar dados com Vue.js?

A) Reduz o uso de CSS.

B) Atualiza o banco de dados automaticamente.

C) Oferece feedback imediato ao usuário, evitando erros no servidor.

D) Exclui a necessidade de formulários.

Resposta:

Resposta correta: C)

A validação com Vue.js oferece feedback em tempo real, melhorando a precisão dos dados e a experiência do usuário.

Questão 2

Como você pode recuperar valores de campos em um formulário usando Vue.js?

A) Usando funções backend diretamente.

B) Com variáveis reativas v-model ligadas aos campos do formulário.

C) Com alertas no navegador.

D) Recarregando a página.

Resposta:

Resposta correta: B)

O v-model em Vue.js sincroniza automaticamente os valores dos campos, permitindo que os dados sejam recuperados e verificados em tempo real.
