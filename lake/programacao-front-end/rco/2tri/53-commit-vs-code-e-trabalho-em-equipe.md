---
titulo: "Commit, VS Code e Trabalho em Equipe"
tipo: rco-seed
disciplina: programacao-front-end
sigla_rco: PFE
trimestre: 2
ordem_rco: 53
serie: 2
aula_rco: "Aula 53"
slides: 23
tem_atividade: true
tem_pratica: true
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/2TRI/53-commit-vs-code-e-trabalho-em-equipe/53-commit-vs-code-e-trabalho-em-equipe.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/2TRI/53-commit-vs-code-e-trabalho-em-equipe/AULA 53_ATIVIDADE_PROGRAMAÇÃO FRONT END.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/2TRI/53-commit-vs-code-e-trabalho-em-equipe/AULA 53_PRÁTICA_PROGRAMAÇÃO FRONT END.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Commit, VS Code e Trabalho em Equipe

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- Programação Front-End
- 2ª Série
- Commit, VS Code e Trabalho em Equipe
- Aula 53

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
- Aprender a utilizar os serviços do github em equipe com outras ferramentas, no vaso o VS Code.
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
- Aprendemos como criar uma conta no GitHub e entendemos a diferença dele para o serviço git.

_1 imagem(ns) no slide._

### Slide 7

- Para pensarmos juntos...
- Letícia é uma desenvolvedora júnior que foi contratada recentemente para uma startup de tecnologia. Ela está acostumada a trabalhar sozinha em seus projetos pessoais, utilizando principalmente o VS Code como sua ferramenta principal de desenvolvimento. Na nova empresa, no entanto, ela precisa trabalhar em equipe e se depara com um desafio: todos os projetos da empresa são hospedados no GitHub, uma plataforma que ela tem pouca experiência.

_1 imagem(ns) no slide._

### Slide 8

- Para pensarmos juntos...
- Dúvida da Letícia: "Eu sei como usar o VS Code para escrever e testar meu código, mas não tenho certeza de como posso usá-lo para colaborar com minha equipe no GitHub. O que eu deveria fazer?"
- 3 minutos
- Levante a mão quem sabe responder!!

_3 imagem(ns) no slide._

### Slide 9

- Resposta
- Para colaborar com a equipe no GitHub usando o VS Code, a Letícia pode começar instalando a extensão do GitHub no VS Code. Esta extensão permite que ela acesse repositórios do GitHub diretamente do VS Code, faça alterações, crie commits e faça push dessas alterações de volta para o GitHub sem sair do editor.
- Fonte https://publicdomainvectors.org/pt/vetorial-gratis/Lista-de-verifica%C3%A7%C3%A3o/45330.html

_1 imagem(ns) no slide._

### Slide 10

- Resposta
- Além disso, ela pode gerenciar "pull requests" e revisar o código de seus colegas de equipe diretamente no VS Code. Com essa configuração, Letícia pode colaborar efetivamente com sua equipe no GitHub, mantendo o fluxo de trabalho que ela já está acostumada no VS Code.
- Fonte https://publicdomainvectors.org/pt/vetorial-gratis/Lista-de-verifica%C3%A7%C3%A3o/45330.html

_1 imagem(ns) no slide._

### Slide 11

- Conceituando
- Um "commit" no GitHub é, em essência, uma "fotografia" do seu projeto em um determinado momento. Cada commit contém uma cópia completa do código no momento do commit, bem como uma mensagem de commit que descreve o que foi alterado. Isso permite que você e sua equipe acompanhem as alterações feitas ao longo do tempo, identifiquem quando e onde os erros foram introduzidos e revertam para versões anteriores do projeto se necessário.

_1 imagem(ns) no slide._

### Slide 12

- Conceituando
- O VS Code é um editor de código-fonte popular que vem com uma série de recursos poderosos para desenvolvedores, incluindo suporte integrado para o Git, que é a tecnologia subjacente ao GitHub. Isso significa que você pode realizar a maioria das operações do Git, como fazer commits, diretamente do VS Code.

_1 imagem(ns) no slide._

### Slide 13

- Conceituando
- A grande vantagem de usar o VS Code com o GitHub é a capacidade de gerenciar seu código e colaborar com sua equipe sem sair do seu ambiente de desenvolvimento. Com a extensão do GitHub para o VS Code, você pode clonar repositórios, fazer alterações e commits, criar e gerenciar pull requests, e até mesmo revisar o código de seus colegas de equipe, tudo isso dentro do VS Code.

_1 imagem(ns) no slide._

### Slide 14

- Conceituando
- Em resumo, a combinação do VS Code e do GitHub oferece uma solução poderosa e conveniente para o desenvolvimento e a colaboração em projetos de software. Permite que você gerencie seu código de forma eficaz, rastreie alterações e colabore com sua equipe de forma eficiente, tudo dentro de um único ambiente de desenvolvimento.

_1 imagem(ns) no slide._

### Slide 15

- Ainda sobre Git e GitHub, vamos conhecer praticando?
- Na plataforma Alura vamos acessar o seguinte curso:
- Link para o curso: https://cursos.alura.com.br/course/git-github-repositorio-commit-versoes
- Ao longo das atividades, você vai encontrar alguns quizzes e eles não estão ali por acaso! Eles são oportunidades rápidas para testar seu entendimento, reforçar o que aprendeu e identificar pontos que ainda podem melhorar.

_3 imagem(ns) no slide._

### Slide 16

- Commit
- 4 minutos
- O "commit" é uma operação fundamental no Git, e por extensão, no GitHub.
- Link para tarefa: https://cursos.alura.com.br/course/git-github-repositorio-commit-versoes/task/106065
- Quando você faz um commit, você está efetivamente salvando o estado atual do seu projeto, incluindo todas as alterações que você fez aos arquivos desde o último commit. Cada commit é acompanhado por uma mensagem de commit, que é uma descrição das alterações que foram feitas
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 17

- VSCode no GitHub
- 9 minutos
- O VS Code, quando usado com o GitHub, fornece um ambiente de desenvolvimento unificado para escrita, teste e versionamento de código.
- Link para tarefa: https://cursos.alura.com.br/course/git-github-repositorio-commit-versoes/task/106066
- Ele permite que os desenvolvedores realizem tarefas do Git, como commits, push e pull, diretamente na interface do editor. Além disso, com o suporte integrado para GitHub, os desenvolvedores podem colaborar em tempo real, revisar pull requests e resolver conflitos de merge diretamente no VS Code.
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 18

- Adicionando um colaborador
- 5 minutos
- Agora vamos aprender a colaborar juntos em um projeto. Trabalhar em projetos que outro criou devido a terem acesso ao mesmo repositório.
- Link para tarefa: https://cursos.alura.com.br/course/git-github-repositorio-commit-versoes/task/106067
- O acesso compartilhado no GitHub permite a colaboração em tempo real, com vários desenvolvedores podendo trabalhar em diferentes partes de um projeto simultaneamente. Isso facilita a revisão de código e a troca de feedback entre os membros da equipe.
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 19

- Vamos praticar?
- Prepare-se, porque nessa atividade, você vai sair do modo aprender e entrar direto no modo praticar.
- A atividade prática vai colocar você diante de um desafio real, que faz relação com o conteúdo aprendido até aqui.

_1 imagem(ns) no slide._

### Slide 20

- O que vimos na aula de hoje:
- Aprendemos a fazer um commit e como utilizar o VS Code com o github.

_1 imagem(ns) no slide._

### Slide 21

- Pronto para desbloquear sua carreira de TI?
- Está perdido estudando mas não sabe por onde começar? Se a resposta é sim, você está no lugar certo! Descubra as estratégias e ferramentas essenciais para te ajudar a desbloquear seu potencial em TI e buscar sua primeira vaga de emprego no setor!
- Este e-book é um guia completo para quem busca começar pelos melhores caminhos para se tornar um excelente profissional de TI, ensinando a identificar perfis profissionais, aplicar técnicas de estudo eficazes, transformar teoria em prática, e aumentar a visibilidade de seu trabalho no mercado de trabalho. Ideal para novatos e profissionais em transição.
- E o melhor, ele pode ser seu, inteiramente grátis!
- Basta clicar AQUI e realizar o seu cadastro com o seu @escola!

_3 imagem(ns) no slide._

### Slide 22

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

### Slide 23

_(sem texto)_

## Atividade

_Fonte: AULA 53_ATIVIDADE_PROGRAMAÇÃO FRONT END.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação Front-End

2ª SÉRIE

ATIVIDADE AULA 53

Questão 1

O que é um commit no contexto do GitHub?

A) Um comando para clonar um repositório.

B) Uma descrição detalhada de um repositório.

C) Uma maneira de baixar arquivos de um repositório.

D) Um ponto na história do seu repositório que captura o estado dos arquivos naquele momento.

Resposta Correta: D) Um ponto na história do seu repositório que captura o estado dos arquivos naquele momento. Um commit no GitHub é como um ponto de salvamento no seu projeto, permitindo que você retorne a esse ponto a qualquer momento.

Questão 2

Qual comando Git é usado para criar um novo commit?

A) git add

B) git commit

C) git push

D) git pull

Resposta Correta: B) git commit. O comando 'git commit' é usado para criar um novo commit. No entanto, antes de poder fazer isso, geralmente você usa o comando 'git add' para adicionar quaisquer novas ou alterações de arquivos ao seu próximo commit.

## Prática

_Fonte: AULA 53_PRÁTICA_PROGRAMAÇÃO FRONT END.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

PROGRAMAÇÃO FRONT END

2ª SÉRIE

ATIVIDADE PRÁTICA AULA 53

##### 1. Objetivo da Aula Prática

Ao final da aula prática, o estudante será capaz de:

- Compreender o conceito de commit no Git.
- Realizar commits utilizando a interface do VS Code.
- Conectar o VS Code a um repositório GitHub.
- Compartilhar um repositório com outro usuário.
- Trabalhar colaborativamente em um projeto utilizando GitHub.
- Registrar alterações de forma organizada através de mensagens de commit.

###### Produto Final Esperado

O estudante deverá:

- Realizar pelo menos 2 commits em um projeto.
- Compartilhar o repositório com um colega.
- Receber ou conceder acesso de colaborador.
- Registrar as alterações realizadas no histórico do projeto.

##### 2. Ferramentas Recomendadas

###### GitHub

Para que serve: hospedagem de repositórios e colaboração em equipe.

Por que é adequado: é a principal plataforma de versionamento utilizada no mercado.

Como facilita o aprendizado: permite visualizar histórico de alterações e colaboração entre usuários.

Site: https://github.com

###### Visual Studio Code (VS Code)

Para que serve: desenvolvimento e gerenciamento de código.

Por que é adequado: possui integração nativa com Git e GitHub.

Como facilita o aprendizado: permite realizar commits sem sair do ambiente de desenvolvimento.

Site: https://code.visualstudio.com

###### Git

Para que serve: controle de versões do projeto.

Por que é adequado: registra e organiza alterações realizadas no código.

Como facilita o aprendizado: permite acompanhar a evolução do projeto.

Site: https://git-scm.com

##### 3. Checklist Inicial

Antes de iniciar a prática, o estudante deve possuir:

Conta GitHub criada

VS Code instalado

Git instalado

Repositório criado no GitHub

Conexão com internet

Projeto HTML ou projeto simples disponível

Acesso ao e-mail cadastrado

###### Materiais de Apoio

GitHub:

https://github.com

Git:

https://git-scm.com

Curso Alura:

https://cursos.alura.com.br/course/git-github-repositorio-commit-versoes

##### 4. Passo a Passo do Docente (Aula de até 50 minutos)

###### Preparações Necessárias

- Verificar acesso ao GitHub.
- Confirmar instalação do Git.
- Confirmar instalação do VS Code.
- Garantir que todos possuam um repositório criado.

###### Contextualização (5 minutos)

Apresente o cenário:

Uma equipe de desenvolvimento precisa trabalhar simultaneamente em um mesmo projeto sem sobrescrever o trabalho dos colegas.

Pergunta para a turma:

Como podemos registrar alterações e acompanhar quem modificou cada parte do projeto?

###### Revisão dos Conceitos (10 minutos)

Explicar:

- Git
- GitHub
- Repositório
- Commit
- Histórico de versões
Apresentar exemplos simples de histórico de alterações.

###### Demonstração do Commit no VS Code (10 minutos)

Mostrar:

- Alteração de um arquivo.
- Área de controle de versão.
- Inserção de mensagem de commit.
- Salvamento da alteração.
Explicar boas práticas para mensagens de commit.

Exemplos:

- Adiciona página inicial
- Corrige alinhamento do menu
- Atualiza informações do rodapé

###### Demonstração da Colaboração (10 minutos)

Mostrar:

- Configuração de colaborador.
- Compartilhamento do repositório.
- Convite para outro usuário.
Explicar a importância do trabalho colaborativo.

###### Prática Guiada (10 minutos)

Os alunos deverão:

- Alterar um arquivo.
- Criar um commit.
- Compartilhar o repositório.
- Aceitar convite de colaboração.

###### Encerramento (5 minutos)

Validar:

- Commits realizados.
- Histórico atualizado.
- Colaboradores adicionados.

###### Pontos de Atenção

- Utilizar mensagens de commit claras.
- Não compartilhar senhas.
- Conferir se o commit foi realmente realizado.
- Verificar se o colaborador recebeu o convite.

##### 5. Atividade Prática — Descrição Geral

O estudante deverá simular um ambiente de desenvolvimento colaborativo.

A atividade consiste em:

- Criar alterações em um projeto.
- Registrar essas alterações através de commits.
- Compartilhar o repositório com um colega.
- Trabalhar em conjunto no mesmo projeto.

###### Problema Real Simulado

Desenvolvimento colaborativo de um sistema web por uma equipe de programadores.

###### Habilidade Desenvolvida

Versionamento de código e colaboração em equipe utilizando GitHub e VS Code.

##### 6. Metodologia Ativa Utilizada

###### Aprendizagem Baseada em Projeto (PBL)

Os estudantes trabalham sobre um projeto real.

###### Aprendizagem Colaborativa

Os alunos interagem entre si através de um repositório compartilhado.

###### Aprendizagem por Experimentação

Executam commits e acompanham o histórico do projeto.

###### Elementos de Lemov

- Modelagem
- Prática Guiada
- Verificação de Compreensão
- Feedback Imediato
- Revisão

##### 7. Passo a Passo da Atividade Prática (para os alunos)

###### Etapa 1 – Abrir o Projeto

- Abra seu projeto no VS Code.
- Verifique se ele está conectado ao GitHub.

###### Etapa 2 – Fazer Alterações

- Escolha um arquivo do projeto.
- Adicione:
- um texto;
- uma imagem;
- uma nova seção; ou
- uma melhoria visual.

###### Etapa 3 – Realizar Commit

- Abra a aba Controle de Código-Fonte.
- Visualize os arquivos alterados.
- Escreva uma mensagem de commit.
- Clique em Commit.

###### Etapa 4 – Compartilhar Repositório

- Acesse o GitHub.
- Abra o repositório.
- Acesse Settings → Collaborators.
- Adicione um colega da turma.

###### Etapa 5 – Validar Colaboração

- O colega deverá aceitar o convite.
- Ambos devem visualizar o repositório compartilhado.

###### Etapa 6 – Registrar Evidências

- Capture um print:
- do commit realizado;
- do histórico de commits;
- do colaborador adicionado.

##### 8. Exemplo ou Demonstração

###### Fluxo de Trabalho

- Editar Arquivo
- ↓
- Salvar Alteração
- ↓
- Commit
- ↓
- GitHub
- ↓
- Histórico Atualizado

###### Exemplo de Mensagem de Commit

- Adiciona seção de contato na página inicial

###### Estrutura de Colaboração

- Aluno A
- ↓
- Repositório GitHub
- ↑
- Aluno B

###### Conceitos Aplicados

| Conceito | Aplicação |
| --- | --- |
| Commit | Registro de alterações |
| Git | Controle de versões |
| GitHub | Compartilhamento de código |
| Colaborador | Trabalho em equipe |
| VS Code | Ambiente de desenvolvimento |

##### 9. Resultado Esperado

O estudante deverá apresentar:

- Repositório funcionando.
- Pelo menos 2 commits realizados.
- Histórico atualizado.
- Colaborador adicionado ao projeto.
- Prints comprovando as etapas.

###### Critérios de Verificação

O professor deverá verificar:

Commit realizado corretamente

Mensagem de commit adequada

Histórico atualizado

Colaborador adicionado

Participação na atividade colaborativa

##### 10. Formato de Entrega da Atividade

###### O que deve ser enviado

- Print do histórico de commits.
- Print do colaborador adicionado.
- Link do repositório GitHub.

###### Nomeação Sugerida

- Aula53_NomeSobrenome
Exemplo:

- Aula53_MariaOliveira

###### Onde Entregar

- Google Classroom
- Google Drive
- AVA da instituição

###### Prazo Sugerido

Ao final da aula.

##### 11. Encerramento e Reflexão

Promova uma conversa com a turma:

###### Perguntas para reflexão

- Por que o commit é considerado uma "fotografia" do projeto?
- Como o histórico de commits ajuda uma equipe?
- Quais vantagens existem em utilizar GitHub integrado ao VS Code?
- Como o trabalho colaborativo pode acelerar o desenvolvimento de software?
