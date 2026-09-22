---
titulo: "Criando uma Conta no GitHub – Parte I"
tipo: rco-seed
disciplina: programacao-front-end
sigla_rco: PFE
trimestre: 2
ordem_rco: 51
serie: 2
aula_rco: "Aula 51"
slides: 22
tem_atividade: true
tem_pratica: true
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/2TRI/51-criando-uma-conta-no-github-parte-i/51-criando-uma-conta-no-github-parte-i.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/2TRI/51-criando-uma-conta-no-github-parte-i/AULA 51_ATIVIDADE_PROGRAMAÇÃO FRONT END.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/2TRI/51-criando-uma-conta-no-github-parte-i/AULA 51_PRÁTICA_PROGRAMAÇÃO FRONT END.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Criando uma Conta no GitHub – Parte I

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- Programação Front-End
- 2ª Série
- Criando uma Conta no GitHub – Parte I
- Aula 51

_1 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- COMPETÊNCIA(S) A SER(EM) DESENVOLVIDA(S) NESTA AULA:
- De acordo com o Plano de Curso de Desenvolvimento de Sistemas:
- HABILIDADE(S) A SER(EM) DESENVOLVIDA(S) NESTA AULA:
- Prestar apoio técnico na elaboração da documentação de sistemas.
- Utilizar ferramentas de versionamento para controle de código-fonte.

_1 imagem(ns) no slide._

### Slide 4

- Nesta aula vamos:
- Aprender melhor sobre o git e github, criando uma conta na plataforma parte I.
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store

_4 imagem(ns) no slide._

### Slide 5 (oculto)

- Este material foi elaborado a partir da análise do plano de curso e reúne os conhecimentos essenciais para o Técnico em Desenvolvimento de Sistemas. As aulas foram organizadas com foco na clareza conceitual, na construção gradual dos conteúdos e na utilização de metodologias ativas que favorecem a compreensão, a participação e o desenvolvimento de habilidades e competências de forma significativa.
- De acordo com a matriz curricular do Curso Técnico em Desenvolvimento de Sistemas, que traz em sua essência componentes estruturados para a realização de aulas práticas, cada unidade curricular deve contemplar, além da abordagem teórica, uma proposta de atividade prática a ser desenvolvida pelo professor. Essa orientação assegura a coerência entre o planejamento didático e o que está estabelecido na matriz, promovendo experiências formativas alinhadas ao perfil profissional previsto.
- O professor tem total autonomia para adaptar o conteúdo conforme o contexto da turma, ajustando exemplos, aprofundamentos e estratégias didáticas para otimizar a aprendizagem e a conexão com a prática profissional.
- Se houver falta de conexão ou indisponibilidade de internet durante a aula, os materiais abaixo podem ser utilizados como apoio para elaborar recursos complementares, garantindo a continuidade da abordagem teórica prevista.
- ATENÇÃO PROFESSOR!
- https://cursos.alura.com.br/course/git-github-repositorio-commit-versoes/task/106566
- Site Git:
- https://git-scm.com/
- Site GitHub:
- https://github.com/

_2 imagem(ns) no slide._

### Slide 6

- Aula anterior
- Aprendemos como compartilhar um projeto HTML no github e gitpages.

_1 imagem(ns) no slide._

### Slide 7

- Para pensarmos juntos...
- Imagine que João, um desenvolvedor web iniciante, tenha acabado de começar um novo projeto de criação de um site para uma pequena empresa local. Ele está trabalhando no projeto sozinho, mas sabe que no futuro pode precisar colaborar com outros desenvolvedores. João está ciente da importância de manter o controle das mudanças que faz no código, mas não tem certeza de como proceder.

_1 imagem(ns) no slide._

### Slide 8

- Para pensarmos juntos...
- Qual ferramenta devo usar para versionar e compartilhar meu código de forma eficaz, permitindo a colaboração futura de outros desenvolvedores?
- 3 minutos
- Troque ideias com seus colegas!

_3 imagem(ns) no slide._

### Slide 9

- Resposta
- Uma solução eficaz para o problema de João seria usar um sistema de controle de versão como o Git. O Git permite que João rastreie as mudanças que faz no seu código ao longo do tempo, facilitando a identificação de quando e onde as alterações foram feitas. Além disso, ao usar um serviço de hospedagem de repositório como o GitHub ou Bitbucket, João pode facilmente compartilhar seu código com outros desenvolvedores, permitindo a colaboração eficaz no projeto.

_1 imagem(ns) no slide._

### Slide 10

- Conceituando
- O compartilhamento e versionamento de código são práticas fundamentais no desenvolvimento de software, incluindo a criação de páginas HTML.
- https://videosdeti.com.br/wp-content/uploads/2018/12/git-githu-cover.png

_1 imagem(ns) no slide._

### Slide 11

- Conceituando
- O compartilhamento de código refere-se à prática de tornar o código de um projeto disponível para outros. Isso permite que múltiplos desenvolvedores trabalhem juntos em um único projeto, promovendo a colaboração e a eficiência. Além disso, o compartilhamento de código permite que outros aprendam com seu trabalho, contribuindo para a comunidade de desenvolvimento como um todo.
- https://lh3.googleusercontent.com/70jaEZnESXQ6SssU5uI4yO62JBz6xq2sNrrz8bW_ap2CuWUaQlbKs3j6NyRJnvcvYwAugkW8WzNJX21dZ2SMd9O_1TTpKZT-FsBkYSPy4rUSpJSo2C-WPTaLc2jQ8ancyj1TetXQ

_1 imagem(ns) no slide._

### Slide 12

- Conceituando
- O versionamento de código, por outro lado, é a prática de acompanhar e controlar as alterações no código-fonte de um projeto. Cada alteração, ou "versão", é registrada com uma mensagem descrevendo o que foi alterado e por que. Isso é incrivelmente útil para rastrear o histórico de um projeto, identificar quando e por que os bugs foram introduzidos, e pode ajudar a resolver conflitos quando várias pessoas estão trabalhando no mesmo projeto.
- https://www.seobility.net/en/wiki/images/7/72/HTML-Sitemap.png

_1 imagem(ns) no slide._

### Slide 13

- Conceituando
- Há várias ferramentas disponíveis para auxiliar no compartilhamento e versionamento de código. Git é o sistema de controle de versão mais popular e é usado para rastrear mudanças no código ao longo do tempo. GitHub, Bitbucket e GitLab são plataformas de hospedagem de código que facilitam o compartilhamento de projetos e a colaboração com outros desenvolvedores.
- https://initialcommit.com/img/initialcommit/git-sim.jpg

_1 imagem(ns) no slide._

### Slide 14

- Conceituando
- Em resumo, o compartilhamento e versionamento de código são práticas essenciais que promovem a colaboração, a aprendizagem e a eficiência no desenvolvimento de software.

_1 imagem(ns) no slide._

### Slide 15

- Ainda sobre Git e GitHub, vamos conhecer praticando?
- Na plataforma Alura vamos acessar o seguinte curso:
- Link para o curso: https://cursos.alura.com.br/course/git-github-repositorio-commit-versoes
- Ao longo das atividades, você vai encontrar alguns quizzes e eles não estão ali por acaso! Eles são oportunidades rápidas para testar seu entendimento, reforçar o que aprendeu e identificar pontos que ainda podem melhorar.

_3 imagem(ns) no slide._

### Slide 16

- Apresentação
- 3 minutos
- Nessa aula vamos iniciar o processo de aprendizado sobre compartilhamento e repositórios.
- Link para tarefa: https://cursos.alura.com.br/course/git-github-repositorio-commit-versoes/task/106062
- Lá no site do GitHub, para você criar sua conta, fazer seu setup, preparar seu repositório, e "commitar". Usar essas palavras: commit, push, pull, tanto via web quanto a partir da linha de comando do seu Linux, do seu Windows, do seu Mac, para fazer isso via comando no terminal.
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 17

- O ponto central
- 7 minutos
- Vamos iniciar a nossa jornada nos estudos de Git e GitHub?
- Link para tarefa: https://cursos.alura.com.br/course/git-github-repositorio-commit-versoes/task/106063
- Empresas pequenas existem equipes grandes, precisamos de ferramentas que nos ajudam a unificar o que estamos trabalhando. Antes já existiam outras ferramentas, mas Git e GitHub é a principal ferramenta, que todo mundo no universo de tecnologia usa para, de alguma forma, conversar de uma maneira única no sistema.
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 18

- Vamos praticar?
- Prepare-se, porque nessa atividade, você vai sair do modo aprender e entrar direto no modo praticar.
- A atividade prática vai colocar você diante de um desafio real, que faz relação com o conteúdo aprendido até aqui.

_1 imagem(ns) no slide._

### Slide 19

- O que vimos na aula de hoje:
- Conhecemos o serviço git e github.

_2 imagem(ns) no slide._

### Slide 20

- Pronto para desbloquear sua carreira de TI?
- Está perdido estudando mas não sabe por onde começar? Se a resposta é sim, você está no lugar certo! Descubra as estratégias e ferramentas essenciais para te ajudar a desbloquear seu potencial em TI e buscar sua primeira vaga de emprego no setor!
- Este e-book é um guia completo para quem busca começar pelos melhores caminhos para se tornar um excelente profissional de TI, ensinando a identificar perfis profissionais, aplicar técnicas de estudo eficazes, transformar teoria em prática, e aumentar a visibilidade de seu trabalho no mercado de trabalho. Ideal para novatos e profissionais em transição.
- E o melhor, ele pode ser seu, inteiramente grátis!
- Basta clicar AQUI e realizar o seu cadastro com o seu @escola!

_3 imagem(ns) no slide._

### Slide 21

- Referências
- BEAULIEU, Alan. SQL: Guia Prático Para Manipulação de Dados. São Paulo: O'Reilly, 2008.
- CHACON, Scott; STRAUB, Ben. Pro Git. 2ª ed. Berkeley: Apress, 2014.
- DELISLE, Marc. MySQL: Guia do Programador. São Paulo: Novatec, 2010.
- FURGERI, Sérgio. SQL - Curso Prático. São Paulo: Novatec, 2018.
- LOELIGER, Jon; MCCULLOUGH, Matthew. Version Control with Git: Powerful Tools and Techniques for Collaborative Software Development. 2ª ed. Sebastopol: O'Reilly Media, 2012.
- SAMPAIO, Cleuton. Banco de Dados SQL: Aprenda a Construir um Banco de Dados do Zero. São Paulo: Novatec, 2018.
- SANTOS, Rafael. Administração de Banco de Dados: SQL Server 2017. São Paulo: Novatec, 2018.
- SILVERMAN, Richard E. Git Pocket Guide: A Working Introduction. Sebastopol: O'Reilly Media, 2013.
- STANEK, William. SQL Server 2019: Guia Completo do Administrador de Banco de Dados. São Paulo: Novatec, 2019.
- Figuras e Imagens:
- https://www.flaticon.com/br
- https://www.istockphoto.com/br
- https://raw.githubusercontent.com/zbtang/React-Native-ViewPager/HEAD/imgs/dotIndicator.gif
- https://storyset.com

### Slide 22

_(sem texto)_

## Atividade

_Fonte: AULA 51_ATIVIDADE_PROGRAMAÇÃO FRONT END.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação Front-End

2ª SÉRIE

ATIVIDADE AULA 51

Questão 1

O que é versionamento de código?

a) É o processo de tornar o código de um projeto disponível para outros.

b) É uma ferramenta para criar sites.

c) É o processo de acompanhar e controlar as alterações no código-fonte de um projeto.

d) É o nome de uma linguagem de programação.

Resposta: c) O versionamento de código é o processo de acompanhar e controlar as alterações no código-fonte de um projeto. Ele permite que os desenvolvedores rastreiem o histórico do projeto, identifiquem quando e por que os bugs foram introduzidos e resolvam conflitos quando várias pessoas estão trabalhando no mesmo projeto.

Questão 2

Qual das seguintes opções é uma plataforma de hospedagem de código que facilita o compartilhamento de projetos?

a) Google Docs

b) GitHub

c) Facebook

d) Microsoft Word

Resposta: b) GitHub é uma plataforma de hospedagem de código que permite aos desenvolvedores compartilhar seus projetos e colaborar com outros. Além do GitHub, existem outras plataformas de hospedagem de código, como Bitbucket e GitLab, que também facilitam o compartilhamento de projetos e a colaboração.

## Prática

_Fonte: AULA 51_PRÁTICA_PROGRAMAÇÃO FRONT END.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

PROGRAMAÇÃO FRONT END

2ª SÉRIE

ATIVIDADE PRÁTICA AULA 51

##### 1. Objetivo da Aula Prática

Ao final da aula prática, o estudante será capaz de:

- Compreender a importância do versionamento de código.
- Diferenciar Git de GitHub.
- Criar uma conta no GitHub.
- Configurar seu perfil inicial na plataforma.
- Explorar a interface principal do GitHub.
- Identificar como o GitHub é utilizado para colaboração entre desenvolvedores.

###### Produto Final Esperado

O estudante deverá possuir:

- Conta criada no GitHub.
- Perfil configurado.
- Primeiro repositório criado.
- Registro das etapas realizadas durante a atividade.

##### 2. Ferramentas Recomendadas

###### GitHub

Para que serve: hospedagem de projetos e colaboração entre desenvolvedores.

Por que é adequado: é a principal plataforma de compartilhamento de código utilizada no mercado.

Como facilita o aprendizado: permite visualizar projetos reais e construir portfólio profissional.

Site: https://github.com

###### Git

Para que serve: sistema de controle de versões.

Por que é adequado: registra todas as alterações realizadas em um projeto.

Como facilita o aprendizado: ajuda a entender o histórico e evolução do código.

Site: https://git-scm.com

###### VS Code

Para que serve: desenvolvimento e gerenciamento dos arquivos do projeto.

Por que é adequado: possui integração com Git e GitHub.

Como facilita o aprendizado: simplifica o fluxo de desenvolvimento.

Site: https://code.visualstudio.com

###### Navegador Web

Para que serve: acesso ao GitHub.

Por que é adequado: permite criar e administrar repositórios.

Como facilita o aprendizado: possibilita interação direta com a plataforma.

##### 3. Checklist Inicial

Antes de iniciar a prática, o estudante deve possuir:

E-mail válido

Acesso à internet

Navegador atualizado

VS Code instalado

Computador ou notebook disponível

Conta de e-mail acessível para confirmação de cadastro

###### Materiais de Apoio

GitHub:

https://github.com

Git:

https://git-scm.com

Curso Alura:

https://cursos.alura.com.br/course/git-github-repositorio-commit-versoes

##### 4. Passo a Passo do Docente (Aula de até 50 minutos)

###### Preparações Necessárias

- Garantir acesso à internet.
- Verificar se todos possuem e-mail válido.
- Garantir que os alunos consigam acessar o GitHub.

###### Contextualização (5 minutos)

Apresente o cenário:

Empresas de tecnologia trabalham com equipes que desenvolvem software simultaneamente. Para organizar esse trabalho, utilizam sistemas de versionamento.

Pergunta para a turma:

Como várias pessoas conseguem trabalhar no mesmo projeto sem perder versões importantes do código?

###### Conceituando Git e GitHub (10 minutos)

Explique:

###### Git

- Sistema de controle de versões.
- Armazena histórico das alterações.

###### GitHub

- Plataforma que utiliza Git.
- Permite armazenar projetos online.
- Facilita colaboração entre equipes.
Apresente exemplos de empresas que utilizam GitHub.

###### Demonstração da Criação da Conta (10 minutos)

Demonstrar:

- Acesso ao site GitHub.
- Processo de cadastro.
- Confirmação do e-mail.
- Personalização básica do perfil.

###### Exploração da Plataforma (10 minutos)

Mostrar:

- Dashboard.
- Perfil.
- Repositórios.
- Configurações.
- Menu principal.
Explicar a finalidade de cada área.

###### Criação do Primeiro Repositório (10 minutos)

Demonstrar:

- Criação de um repositório vazio.
- Definição do nome.
- Escolha entre público e privado.

###### Encerramento (5 minutos)

Validar:

- Conta criada.
- Perfil configurado.
- Repositório criado.

###### Pontos de Atenção

- Conferir a confirmação do e-mail.
- Evitar esquecer usuário e senha.
- Anotar login em local seguro.
- Não compartilhar credenciais.

##### 5. Atividade Prática — Descrição Geral

O estudante deverá criar sua conta GitHub e configurar seu ambiente inicial para utilização da plataforma.

A atividade inclui:

- Cadastro na plataforma.
- Configuração do perfil.
- Criação do primeiro repositório.
- Registro das etapas realizadas.

###### Problema Real Simulado

Preparação de ambiente para trabalho em equipe em projetos de desenvolvimento de software.

###### Habilidade Desenvolvida

Utilização de plataformas de versionamento e colaboração.

##### 6. Metodologia Ativa Utilizada

###### Aprendizagem Baseada em Projeto (PBL)

Os alunos iniciam a construção do próprio ambiente profissional.

###### Aprendizagem por Experimentação

Exploram uma ferramenta utilizada amplamente pelo mercado.

###### Ensino por Descoberta

Navegam pela plataforma identificando recursos disponíveis.

###### Elementos de Lemov

- Modelagem
- Prática Guiada
- Verificação de Compreensão
- Feedback Imediato
- Revisão

##### 7. Passo a Passo da Atividade Prática (para os alunos)

###### Etapa 1 – Criar Conta

- Acesse https://github.com
- Clique em Sign Up.
- Informe:
- e-mail;
- senha;
- nome de usuário.
- Conclua o cadastro.
- Confirme o e-mail enviado pela plataforma.

###### Etapa 2 – Configurar Perfil

- Adicione:
- foto de perfil (opcional);
- nome;
- biografia simples.
Exemplo:

Estudante de Desenvolvimento de Sistemas.

###### Etapa 3 – Criar Primeiro Repositório

- Clique em New Repository.
- Defina o nome:
- meu-primeiro-repositorio
- Escolha repositório público.
- Clique em Create Repository.

###### Etapa 4 – Explorar a Plataforma

- Acesse seu perfil.
- Visualize o repositório criado.
- Explore:
- Repositories;
- Projects;
- Settings.

###### Etapa 5 – Registro

- Faça um print:
- do perfil;
- do repositório criado.
- Salve as imagens para entrega.

##### 8. Exemplo ou Demonstração

###### Estrutura do Perfil

| Item | Exemplo |
| --- | --- |
| Nome de usuário | joaosilva |
| Nome exibido | João Silva |
| Bio | Estudante de Desenvolvimento de Sistemas |

###### Exemplo de Repositório

- meu-primeiro-repositorio

###### Estrutura Esperada

- GitHub
- │
- ├── Perfil
- │
- └── Repositório
- └── meu-primeiro-repositorio

##### 9. Resultado Esperado

O estudante deverá apresentar:

- Conta GitHub criada.
- Perfil configurado.
- Primeiro repositório criado.
- Prints de comprovação.

###### Critérios de Verificação

O professor deverá verificar:

Conta criada com sucesso

Perfil acessível

Repositório criado

Organização das informações

Compreensão dos conceitos apresentados

##### 10. Formato de Entrega da Atividade

###### O que deve ser enviado

- Print do perfil GitHub.
- Print do repositório criado.

###### Nomeação Sugerida

- Aula51_NomeSobrenome
Exemplo:

- Aula51_MariaSilva

###### Local de Entrega

- Google Classroom
- Google Drive
- AVA da instituição

###### Prazo Sugerido

Ao final da aula.

##### 11. Encerramento e Reflexão

Promova uma discussão final:

###### Perguntas para reflexão

- Por que o GitHub é tão utilizado pelas empresas?
- Qual a diferença entre Git e GitHub?
- Como o versionamento ajuda no desenvolvimento de software?
- De que forma um perfil GitHub pode contribuir para sua carreira?
