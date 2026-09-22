---
titulo: "Trabalhando Localmente com Git – Parte II"
tipo: rco-seed
disciplina: programacao-front-end
sigla_rco: PFE
trimestre: 2
ordem_rco: 55
serie: 2
aula_rco: "Aula 55"
slides: 20
tem_atividade: true
tem_pratica: true
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/2TRI/55-trabalhando-localmente-com-git-parte-ii/55-trabalhando-localmente-com-git-parte-ii.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/2TRI/55-trabalhando-localmente-com-git-parte-ii/AULA 55_ATIVIDADE_PROGRAMAÇÃO FRONT END.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/2TRI/55-trabalhando-localmente-com-git-parte-ii/AULA 55_PRÁTICA_PROGRAMAÇÃO FRONT END.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Trabalhando Localmente com Git – Parte II

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- Programação Front-End
- 2ª Série
- Trabalhando Localmente com Git – Parte II
- Aula 55

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
- Aprender a utilizar o serviço Git de forma local Parte II.
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
- Instalando o Git localmente:
- https://cursos.alura.com.br/course/git-github-repositorio-commit-versoes/task/117550

_2 imagem(ns) no slide._

### Slide 6

- Aula anterior
- Iniciamos os estudos sobre a utilização do Git em modo local sem depender do repositório na nuvem.

_2 imagem(ns) no slide._

### Slide 7

- Para pensarmos juntos...
- Alex é um desenvolvedor júnior que acabou de ingressar em uma nova equipe de desenvolvimento de software. Seu primeiro projeto envolve a adição de uma nova funcionalidade em um código existente. Para entender o histórico de alterações e evitar quebrar algo existente, ele decide usar o comando 'git log' para verificar o histórico de commits no repositório.
- Entretanto, Alex se depara com uma lista enorme de commits. Ele está ciente de que é possível filtrar o histórico de commits, mas não sabe exatamente como fazer isso.

_1 imagem(ns) no slide._

### Slide 8

- Para pensarmos juntos...
- Como Alex pode usar o comando 'git log' para filtrar o histórico de commits de um autor específico?
- Conversem e apresentem suas visões

_2 imagem(ns) no slide._

### Slide 9

- Resposta
- Alex pode usar o comando 'git log --author="nome_do_autor"'. Este comando mostrará apenas os commits feitos pelo autor especificado, tornando muito mais fácil para Alex seguir o histórico de alterações feitas por esse autor específico. Isso permite que ele entenda melhor as mudanças anteriores e contribua de maneira mais eficaz para o projeto.

_1 imagem(ns) no slide._

### Slide 10

- Conceituando
- O comando "clone" do Git é uma operação que cria uma cópia completa de um repositório remoto em seu sistema local. Esse comando é geralmente o primeiro a ser usado ao se interagir com um repositório existente. Ele permite que você tenha seu próprio espaço de trabalho, separado dos demais colaboradores, o que é vital para o trabalho em equipe. A clonagem também permite que você tenha acesso offline aos arquivos e histórico de commits.

_5 imagem(ns) no slide._

### Slide 11

- Conceituando
- Git log é um comando que permite que os usuários visualizem o histórico de commits de um repositório. É útil para ver quem fez o quê e quando. A visualização desse histórico pode ajudar os desenvolvedores a entender as mudanças que ocorreram ao longo do tempo, como correções de bugs, implementação de novas funcionalidades e mudanças estruturais.

_1 imagem(ns) no slide._

### Slide 12

- Conceituando
- A principal vantagem do comando "clone" é que ele permite que você copie rapidamente um projeto e tenha seu próprio espaço para experimentar sem afetar o projeto original. Você pode fazer alterações em seu próprio tempo e enviar (push) as alterações quando estiver pronto.

_1 imagem(ns) no slide._

### Slide 13

- Conceituando
- Por outro lado, o Git log é uma ferramenta valiosa para a revisão do código e o rastreamento de bugs. Permite que você identifique facilmente quando uma alteração específica foi feita, por quem e por quê. Isso ajuda a manter a qualidade do código e facilita a colaboração entre a equipe.

_1 imagem(ns) no slide._

### Slide 14

- Ainda sobre Git e GitHub, vamos conhecer praticando?
- Na plataforma Alura vamos acessar o seguinte curso:
- Link para o curso: https://cursos.alura.com.br/course/git-github-repositorio-commit-versoes
- Ao longo das atividades, você vai encontrar alguns quizzes e eles não estão ali por acaso! Eles são oportunidades rápidas para testar seu entendimento, reforçar o que aprendeu e identificar pontos que ainda podem melhorar.

_3 imagem(ns) no slide._

### Slide 15

- O que vimos até aqui
- 15 minutos
- Resumo do que vimos até aqui na configuração do Git…
- Link para tarefa: https://cursos.alura.com.br/course/git-github-repositorio-commit-versoes/task/106070
- Quando nossos arquivos de configuração estão bem configurados, para o git pull basta fazer git pull, não precisa colocar aquela URL gigante.
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 16

- Vamos praticar?
- Prepare-se, porque nessa atividade, você vai sair do modo aprender e entrar direto no modo praticar.
- A atividade prática vai colocar você diante de um desafio real, que faz relação com o conteúdo aprendido até aqui.

_1 imagem(ns) no slide._

### Slide 17

- O que vimos na aula de hoje:
- Aprendemos a utilizar o Git de forma local no ambiente de desenvolvimento.

_1 imagem(ns) no slide._

### Slide 18

- Pronto para desbloquear sua carreira de TI?
- Está perdido estudando mas não sabe por onde começar? Se a resposta é sim, você está no lugar certo! Descubra as estratégias e ferramentas essenciais para te ajudar a desbloquear seu potencial em TI e buscar sua primeira vaga de emprego no setor!
- Este e-book é um guia completo para quem busca começar pelos melhores caminhos para se tornar um excelente profissional de TI, ensinando a identificar perfis profissionais, aplicar técnicas de estudo eficazes, transformar teoria em prática, e aumentar a visibilidade de seu trabalho no mercado de trabalho. Ideal para novatos e profissionais em transição.
- E o melhor, ele pode ser seu, inteiramente grátis!
- Basta clicar AQUI e realizar o seu cadastro com o seu @escola!

_3 imagem(ns) no slide._

### Slide 19

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

### Slide 20

_(sem texto)_

## Atividade

_Fonte: AULA 55_ATIVIDADE_PROGRAMAÇÃO FRONT END.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação Front-End

2ª SÉRIE

ATIVIDADE AULA 55

Questão 1

O que é o comando "clone" no Git?

a) É o comando usado para criar um novo branch.

b) É o comando usado para ver o histórico de commits.

c) É o comando usado para enviar as alterações para o repositório remoto.

d) É o comando usado para copiar um repositório existente para o seu computador local.

Resposta: A resposta correta é a alternativa (d). O comando "clone" é usado para copiar um repositório existente para o seu computador local, permitindo que você trabalhe no projeto.

Questão 2

Qual o comando utilizado para clonar um repositório do GitHub para o seu computador local?

a) git add

b) git clone https://github.com/username/repository.git

c) git commit -m "Initial commit"

d) git push -u origin master

Resposta: A resposta correta é a alternativa (b). O comando "git clone https://github.com/username/repository.git" é usado para clonar um repositório existente no GitHub para o seu computador local. Lembre-se de substituir "username" pelo nome de usuário do proprietário do repositório e "repository" pelo nome do repositório que você deseja clonar.

## Prática

_Fonte: AULA 55_PRÁTICA_PROGRAMAÇÃO FRONT END.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

PROGRAMAÇÃO FRONT END

2ª SÉRIE

ATIVIDADE PRÁTICA AULA 55

##### 1. Objetivo da Aula Prática

Ao final da aula prática, o estudante será capaz de:

- Clonar um repositório remoto utilizando Git.
- Explorar o histórico de commits utilizando o comando git log.
- Filtrar commits por autor.
- Interpretar informações presentes no histórico do projeto.
- Identificar alterações realizadas por diferentes colaboradores.
- Compreender a importância do rastreamento de alterações em projetos de software.

###### Produto Final Esperado

O estudante deverá:

- Clonar um repositório GitHub.
- Consultar o histórico de commits.
- Filtrar commits de um autor específico.
- Registrar evidências dos comandos executados.
- Elaborar um breve relatório sobre o histórico analisado.

##### 2. Ferramentas Recomendadas

###### Git

Para que serve: controle de versão distribuído.

Por que é adequado: permite rastrear alterações e analisar o histórico do projeto.

Como facilita o aprendizado: possibilita compreender a evolução de um software ao longo do tempo.

Site: https://git-scm.com

###### GitHub

Para que serve: armazenamento dos repositórios remotos.

Por que é adequado: disponibiliza projetos para clonagem e colaboração.

Como facilita o aprendizado: permite visualizar projetos reais utilizados pela comunidade.

Site: https://github.com

###### Visual Studio Code (VS Code)

Para que serve: edição e navegação nos arquivos do projeto.

Por que é adequado: possui integração nativa com Git.

Como facilita o aprendizado: permite visualizar alterações e histórico de forma prática.

Site: https://code.visualstudio.com

###### Git Bash ou Terminal

Para que serve: execução dos comandos Git.

Por que é adequado: oferece acesso completo às funcionalidades da ferramenta.

Como facilita o aprendizado: aproxima o estudante do ambiente profissional.

##### 3. Checklist Inicial

Antes de iniciar a prática, o estudante deve possuir:

Git instalado

VS Code instalado

Conta GitHub ativa

Conexão com internet

Git Bash ou Terminal disponível

Repositório GitHub para análise

###### Materiais de Apoio

GitHub:

https://github.com

Git:

https://git-scm.com

Curso Alura:

https://cursos.alura.com.br/course/git-github-repositorio-commit-versoes

##### 4. Passo a Passo do Docente (Aula de até 50 minutos)

###### Preparações Necessárias

- Verificar instalação do Git.
- Confirmar acesso ao GitHub.
- Disponibilizar um repositório para análise.
- Testar o terminal dos computadores.

###### Contextualização (5 minutos)

Apresente o cenário:

Alex entrou em uma equipe de desenvolvimento e precisa entender rapidamente o histórico de alterações de um projeto.

Pergunta:

Como descobrir quem fez determinada alteração em um sistema?

###### Revisão dos Conceitos (10 minutos)

Revisar:

- Git local.
- Clone.
- Commit.
- Histórico.
- Controle de versão distribuído.
Explicar a importância do histórico para manutenção de sistemas.

###### Demonstração do Clone (10 minutos)

Demonstrar:

- Acesso ao GitHub.
- Cópia da URL do repositório.
- Clonagem local.
- Abertura no VS Code.
Explicar a diferença entre repositório local e remoto.

###### Demonstração do Git Log (10 minutos)

Demonstrar:

- Visualização do histórico.
- Informações exibidas:
- autor;
- data;
- mensagem do commit.
Mostrar exemplos de filtros por autor.

###### Prática Guiada (10 minutos)

Orientar os alunos a:

- clonar um projeto;
- analisar commits;
- localizar commits específicos;
- aplicar filtro por autor.

###### Encerramento (5 minutos)

Verificar:

- clone realizado;
- histórico consultado;
- filtro executado corretamente.

###### Pontos de Atenção

- Verificar se o clone foi concluído.
- Conferir escrita correta do nome do autor.
- Explicar que o histórico não deve ser alterado indevidamente.
- Estimular leitura das mensagens de commit.

##### 5. Atividade Prática — Descrição Geral

O estudante deverá atuar como membro de uma equipe que recebeu um projeto já existente e precisa compreender seu histórico de desenvolvimento.

A atividade consiste em:

- Clonar o repositório.
- Investigar o histórico.
- Filtrar commits por autor.
- Identificar alterações relevantes.
- Produzir um resumo da análise.

###### Problema Real Simulado

Análise de histórico de desenvolvimento de um sistema antes da implementação de novas funcionalidades.

###### Habilidade Desenvolvida

Leitura, interpretação e rastreamento de alterações em projetos versionados.

##### 6. Metodologia Ativa Utilizada

###### Aprendizagem Baseada em Problemas (PBL)

O estudante investiga um histórico real de projeto.

###### Aprendizagem por Descoberta

Explora comandos para localizar informações específicas.

###### Experimentação Prática

Executa operações reais do Git.

###### Elementos de Lemov

- Modelagem
- Prática Guiada
- Verificação de Compreensão
- Feedback Imediato
- Revisão

##### 7. Passo a Passo da Atividade Prática (para os alunos)

###### Etapa 1 – Clonar o Projeto

- Acesse um repositório GitHub indicado pelo professor.
- Copie a URL do projeto.
- Abra o Git Bash.
- Clone o repositório para sua máquina.
- Abra o projeto no VS Code.

###### Etapa 2 – Analisar o Histórico

- Acesse o terminal.
- Visualize o histórico completo de commits.
- Observe:
- autores;
- datas;
- descrições.

###### Etapa 3 – Filtrar por Autor

- Escolha um autor presente no histórico.
- Execute o filtro por autor.
- Analise apenas os commits desse colaborador.

###### Etapa 4 – Registrar Informações

- Identifique:
- quantidade de commits;
- tipo de alterações realizadas;
- frequência de participação.
- Registre suas observações.

###### Etapa 5 – Evidências

- Capture prints:
- do clone realizado;
- do histórico;
- do filtro por autor.

##### 8. Exemplo ou Demonstração

###### Fluxo da Atividade

- GitHub
- ↓
- Clone
- ↓
- Repositório Local
- ↓
- Git Log
- ↓
- Filtro por Autor
- ↓
- Análise do Histórico

###### Exemplo de Informações Encontradas

| Item | Exemplo |
| --- | --- |
| Autor | João Silva |
| Data | 10/03/2025 |
| Commit | Correção do menu principal |

###### Conceitos Aplicados

| Conceito | Aplicação |
| --- | --- |
| Clone | Copiar projeto remoto |
| Log | Visualizar histórico |
| Commit | Registro de alteração |
| Autor | Responsável pela modificação |
| Git Local | Trabalho offline |

##### 9. Resultado Esperado

O estudante deverá apresentar:

- Repositório clonado.
- Histórico consultado.
- Filtro por autor aplicado.
- Relatório simples contendo observações sobre os commits encontrados.

###### Critérios de Verificação

O professor deverá verificar:

Clone realizado corretamente

Histórico consultado

Filtro por autor utilizado

Interpretação adequada das informações

Participação na análise proposta

##### 10. Formato de Entrega da Atividade

###### O que deve ser enviado

- Print do repositório clonado.
- Print do histórico de commits.
- Print do filtro por autor.
- Relatório contendo as observações realizadas.

###### Nomeação Sugerida

- Aula55_NomeSobrenome
Exemplo:

- Aula55_AnaSouza

###### Onde Entregar

- Google Classroom
- Google Drive
- AVA da instituição

###### Prazo Sugerido

Ao final da aula.

##### 11. Encerramento e Reflexão

Promova uma discussão final:

###### Perguntas para reflexão

- Como o histórico de commits ajuda na manutenção de sistemas?
- Por que é importante escrever boas mensagens de commit?
- Como o filtro por autor pode ajudar uma equipe?
- O que aconteceria se não existisse um histórico das alterações realizadas?
