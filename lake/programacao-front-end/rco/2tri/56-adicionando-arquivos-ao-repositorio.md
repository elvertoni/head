---
titulo: "Adicionando Arquivos ao Repositório"
tipo: rco-seed
disciplina: programacao-front-end
sigla_rco: PFE
trimestre: 2
ordem_rco: 56
serie: 2
aula_rco: "Aula 56"
slides: 21
tem_atividade: true
tem_pratica: true
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/2TRI/56-adicionando-arquivos-ao-repositorio/56-adicionando-arquivos-ao-repositorio.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/2TRI/56-adicionando-arquivos-ao-repositorio/AULA 56_ATIVIDADE_PROGRAMAÇÃO FRONT END.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/2TRI/56-adicionando-arquivos-ao-repositorio/AULA 56_PRÁTICA_PROGRAMAÇÃO FRONT END.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Adicionando Arquivos ao Repositório

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- Programação Front-End
- 2ª Série
- Adicionando Arquivos ao Repositório
- Aula 56

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
- Aprender a adicionar arquivos para o próximo commit através do Git.
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
- Concluímos os estudos sobre a utilização do Git em modo local sem depender do repositório na nuvem.

_1 imagem(ns) no slide._

### Slide 7

- Para pensarmos juntos...
- Pedro é um desenvolvedor iniciante que acabou de fazer algumas alterações em seu código localmente e agora está pronto para adicioná-las ao seu repositório no GitHub. No entanto, ele percebe que tem muitos arquivos que foram alterados e está preocupado em adicionar acidentalmente alguns arquivos que não queria.

_1 imagem(ns) no slide._

### Slide 8

- Para pensarmos juntos...
- Ele se pergunta: "Como posso garantir que apenas os arquivos que desejo serão adicionados ao repositório?"
- Conversem e apresentem suas visões

_2 imagem(ns) no slide._

### Slide 9

- Resposta
- Pedro pode usar o comando 'git add' seguido do nome do arquivo que deseja adicionar. Dessa forma, ele terá o controle de quais arquivos estão sendo adicionados ao repositório. Se ele quiser adicionar todos os arquivos de uma vez, pode usar o comando 'git add .' . No entanto, é sempre uma boa prática verificar as alterações antes de adicioná-las ao repositório usando 'git status' ou 'git diff'.

_3 imagem(ns) no slide._

### Slide 10

- Conceituando
- O comando "git add" é uma ferramenta essencial no controle de versão do Git. É ele que inicia todo o processo de registrar mudanças em um projeto, permitindo que você selecione quais alterações, feitas no diretório de trabalho, devem ser consideradas para o próximo "commit" (isto é, para o próximo registro oficial das modificações).

_1 imagem(ns) no slide._

### Slide 11

- Ao executar "git add" seguido do nome de um arquivo ou diretório, você está dizendo ao Git para incluir as atualizações daquele local na próxima confirmação. Isso significa que você pode fazer várias alterações, mas escolher adicionar apenas partes específicas dessas alterações. Isso dá um alto grau de controle sobre a granularidade das suas confirmações.
- Conceituando

_1 imagem(ns) no slide._

### Slide 12

- Conceituando
- Uma das grandes vantagens do "git add" é a sua flexibilidade. Você pode usar o comando de várias maneiras para adicionar todo o conteúdo de um diretório, certos tipos de arquivos, ou até mesmo apenas alterações específicas em um arquivo. Esta flexibilidade permite que você organize seu histórico de commits de uma maneira que faça sentido para você e para a equipe do projeto.

_1 imagem(ns) no slide._

### Slide 13

- Conceituando
- Em resumo, o "git add" é uma parte fundamental do fluxo de trabalho do Git que permite aos desenvolvedores escolherem precisamente quais alterações querem commitar, proporcionando um controle refinado sobre o histórico de versões de um projeto.

_1 imagem(ns) no slide._

### Slide 14

- Ainda sobre Git e GitHub, vamos conhecer praticando?
- Na plataforma Alura vamos acessar o seguinte curso:
- Link para o curso: https://cursos.alura.com.br/course/git-github-repositorio-commit-versoes
- Ao longo das atividades, você vai encontrar alguns quizzes e eles não estão ali por acaso! Eles são oportunidades rápidas para testar seu entendimento, reforçar o que aprendeu e identificar pontos que ainda podem melhorar.

_3 imagem(ns) no slide._

### Slide 15

- Git clone e Git log
- 5 minutos
- O "git clone" é um comando Git para copiar um repositório remoto para o local, permitindo trabalhar com os arquivos de maneira independente.
- Link para tarefa: https://cursos.alura.com.br/course/git-github-repositorio-commit-versoes/task/106071
- Já o "git log" permite a visualização do histórico de commits do repositório, mostrando quem fez cada alteração, quando e quais arquivos foram modificados. Ambos são essenciais para o trabalho colaborativo e controle eficiente de versões.
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 16

- Git add
- 6 minutos
- O "git add" é um comando usado no Git para adicionar alterações no diretório de trabalho para a área de preparação, também conhecida como "staging area".
- Link para tarefa: https://cursos.alura.com.br/course/git-github-repositorio-commit-versoes/task/106072
- Ele é o primeiro passo no fluxo de trabalho básico do Git e prepara as alterações para o próximo commit, que é o registro oficial das modificações no repositório.
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 17

- Vamos praticar?
- Prepare-se, porque nessa atividade, você vai sair do modo aprender e entrar direto no modo praticar.
- A atividade prática vai colocar você diante de um desafio real, que faz relação com o conteúdo aprendido até aqui.

_1 imagem(ns) no slide._

### Slide 18

- O que vimos na aula de hoje:
- Aprendemos a utilizar o Git log, Git clone e Git add no ambiente de desenvolvimento.

_1 imagem(ns) no slide._

### Slide 19

- Pronto para desbloquear sua carreira de TI?
- Está perdido estudando mas não sabe por onde começar? Se a resposta é sim, você está no lugar certo! Descubra as estratégias e ferramentas essenciais para te ajudar a desbloquear seu potencial em TI e buscar sua primeira vaga de emprego no setor!
- Este e-book é um guia completo para quem busca começar pelos melhores caminhos para se tornar um excelente profissional de TI, ensinando a identificar perfis profissionais, aplicar técnicas de estudo eficazes, transformar teoria em prática, e aumentar a visibilidade de seu trabalho no mercado de trabalho. Ideal para novatos e profissionais em transição.
- E o melhor, ele pode ser seu, inteiramente grátis!
- Basta clicar AQUI e realizar o seu cadastro com o seu @escola!

_3 imagem(ns) no slide._

### Slide 20

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

### Slide 21

_(sem texto)_

## Atividade

_Fonte: AULA 56_ATIVIDADE_PROGRAMAÇÃO FRONT END.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação Front-End

2ª SÉRIE

ATIVIDADE AULA 56

Questão 1

O que faz o comando 'git add' no Git?

a) Exclui arquivos do repositório.

b) Registra modificações para o próximo commit.

c) Cria uma nova branch.

d) Faz o merge de duas branches.

Comentário: A resposta correta é a opção (b). O comando 'git add' registra modificações para o próximo commit. Ele não exclui arquivos, cria branches ou faz merges, funções que são executadas por outros comandos do Git.

Questão 2

Para que serve o comando 'git clone' no Git?

a) Registra modificações para o próximo commit.

b) Cria uma cópia local de um repositório remoto.

c) Faz o merge de duas branches.

d) Exclui arquivos do repositório.

Comentário: A resposta correta é a opção (b). O comando 'git clone' é usado para criar uma cópia local de um repositório remoto. Ele não registra modificações, faz merges ou exclui arquivos, funções que são executadas por outros comandos do Git.

## Prática

_Fonte: AULA 56_PRÁTICA_PROGRAMAÇÃO FRONT END.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

PROGRAMAÇÃO FRONT END

2ª SÉRIE

ATIVIDADE PRÁTICA AULA 56

##### 1. Objetivo da Aula Prática

Ao final da aula prática, o estudante será capaz de:

- Compreender a função da área de preparação (Staging Area) do Git.
- Utilizar o comando git add para selecionar arquivos específicos.
- Utilizar o comando git add . para adicionar múltiplos arquivos.
- Verificar alterações utilizando git status.
- Analisar o histórico de commits utilizando git log.
- Preparar corretamente alterações antes de realizar um commit.

###### Produto Final Esperado

O estudante deverá:

- Clonar um repositório.
- Realizar alterações em arquivos.
- Adicionar arquivos específicos utilizando git add.
- Verificar o status do projeto.
- Registrar evidências do processo realizado.

##### 2. Ferramentas Recomendadas

###### Git

Para que serve: sistema de controle de versão distribuído.

Por que é adequado: permite gerenciar alterações de forma segura e organizada.

Como facilita o aprendizado: possibilita acompanhar cada etapa do fluxo de versionamento.

Site: https://git-scm.com

###### GitHub

Para que serve: armazenamento e compartilhamento de repositórios.

Por que é adequado: permite trabalhar com projetos reais.

Como facilita o aprendizado: conecta o ambiente local ao ambiente remoto.

Site: https://github.com

###### Visual Studio Code (VS Code)

Para que serve: edição dos arquivos do projeto.

Por que é adequado: possui integração nativa com Git.

Como facilita o aprendizado: permite visualizar alterações facilmente.

Site: https://code.visualstudio.com

###### Git Bash ou Terminal

Para que serve: execução dos comandos Git.

Por que é adequado: fornece acesso completo às funcionalidades da ferramenta.

Como facilita o aprendizado: aproxima o aluno do ambiente profissional de desenvolvimento.

##### 3. Checklist Inicial

Antes de iniciar a prática, o estudante deve possuir:

Git instalado

VS Code instalado

Conta GitHub ativa

Conexão com internet

Git Bash ou Terminal disponível

Repositório GitHub para clonagem

Projeto de exemplo disponível

###### Materiais de Apoio

Git:

https://git-scm.com

GitHub:

https://github.com

Curso Alura:

https://cursos.alura.com.br/course/git-github-repositorio-commit-versoes

##### 4. Passo a Passo do Docente (Aula de até 50 minutos)

###### Preparações Necessárias

- Verificar instalação do Git.
- Garantir acesso ao GitHub.
- Disponibilizar um repositório para testes.
- Validar funcionamento do terminal.

###### Contextualização (5 minutos)

Apresente o cenário:

Pedro realizou diversas alterações em seu projeto e agora precisa decidir exatamente quais arquivos serão enviados para o próximo commit.

Pergunta para a turma:

Como evitar adicionar arquivos incorretos ao histórico do projeto?

###### Revisão Conceitual (10 minutos)

Revisar:

- Repositório local.
- Clone.
- Histórico de commits.
- Área de preparação (Staging Area).
Explicar o fluxo:

- Arquivo Alterado
- ↓
- git add
- ↓
- Staging Area
- ↓
- Commit

###### Demonstração do Git Status (5 minutos)

Mostrar:

- Como visualizar arquivos modificados.
- Como identificar arquivos preparados e não preparados.
Explicar a importância da conferência antes do commit.

###### Demonstração do Git Add (10 minutos)

Demonstrar:

- Adição de um único arquivo.
- Adição de vários arquivos.
- Adição de todo o projeto.
Explicar quando utilizar cada abordagem.

###### Prática Guiada (15 minutos)

Os alunos deverão:

- Clonar o projeto.
- Alterar arquivos.
- Verificar status.
- Adicionar arquivos específicos.
- Conferir novamente o status.

###### Encerramento (5 minutos)

Validar:

- Arquivos preparados corretamente.
- Compreensão do fluxo de versionamento.
- Uso adequado do Git Add.

###### Pontos de Atenção

- Não adicionar arquivos desnecessários.
- Sempre verificar o status antes do commit.
- Diferenciar arquivos modificados e arquivos preparados.
- Conferir a estrutura do repositório.

##### 5. Atividade Prática — Descrição Geral

O estudante deverá simular a manutenção de um projeto já existente.

Durante a atividade ele precisará:

- Clonar um repositório.
- Modificar arquivos.
- Utilizar o Git para identificar alterações.
- Adicionar apenas os arquivos desejados para o próximo commit.

###### Problema Real Simulado

Um desenvolvedor precisa preparar cuidadosamente as alterações antes de registrá-las oficialmente no histórico do projeto.

###### Habilidade Desenvolvida

Gerenciamento de alterações utilizando a área de preparação do Git.

##### 6. Metodologia Ativa Utilizada

###### Aprendizagem Baseada em Problemas (PBL)

O estudante resolve um cenário comum do desenvolvimento profissional.

###### Aprendizagem por Experimentação

Executa comandos reais do Git.

###### Ensino por Descoberta

Observa o comportamento dos arquivos durante o fluxo de versionamento.

###### Elementos de Lemov

- Modelagem
- Prática Guiada
- Verificação de Compreensão
- Feedback Imediato
- Revisão

##### 7. Passo a Passo da Atividade Prática (para os alunos)

###### Etapa 1 – Clonar o Repositório

- Acesse um repositório disponibilizado pelo professor.
- Copie a URL do projeto.
- Abra o Git Bash.
- Clone o repositório.
- Abra o projeto no VS Code.

###### Etapa 2 – Modificar Arquivos

- Escolha dois arquivos do projeto.
- Realize alterações simples:
- adicionar texto;
- alterar título;
- modificar comentários.
- Salve os arquivos.

###### Etapa 3 – Verificar Alterações

- Abra o terminal.
- Consulte o status do projeto.
- Observe quais arquivos foram modificados.

###### Etapa 4 – Adicionar Arquivos

- Adicione apenas um dos arquivos alterados.
- Consulte novamente o status.
- Verifique quais arquivos estão preparados.

###### Etapa 5 – Adicionar Todos os Arquivos

- Utilize a opção para adicionar todas as alterações.
- Consulte novamente o status.

###### Etapa 6 – Registrar Evidências

- Capture prints:
- do status inicial;
- após adicionar um arquivo;
- após adicionar todos os arquivos.

##### 8. Exemplo ou Demonstração

###### Fluxo do Git Add

- Arquivo Modificado
- ↓
- git status
- ↓
- git add
- ↓
- Staging Area
- ↓
- Pronto para Commit

###### Fluxo Completo

- Clone
- ↓
- Alteração
- ↓
- Status
- ↓
- Git Add
- ↓
- Status
- ↓
- Commit

###### Conceitos Aplicados

| Conceito | Aplicação |
| --- | --- |
| Git Clone | Copiar repositório |
| Git Status | Verificar alterações |
| Git Add | Preparar arquivos |
| Staging Area | Área de preparação |
| Commit | Registro oficial |

##### 9. Resultado Esperado

O estudante deverá apresentar:

- Repositório clonado.
- Arquivos modificados.
- Arquivos preparados utilizando Git Add.
- Evidências das etapas realizadas.

###### Critérios de Verificação

O professor deverá verificar:

Clone realizado corretamente

Alterações identificadas

Uso adequado do Git Status

Uso correto do Git Add

Compreensão da área de preparação

##### 10. Formato de Entrega da Atividade

###### O que deve ser enviado

- Print do clone realizado.
- Print do Git Status antes do Git Add.
- Print do Git Status após o Git Add.
- Breve descrição das alterações realizadas.

###### Nomeação Sugerida

- Aula56_NomeSobrenome
Exemplo:

- Aula56_CarlosSilva

###### Onde Entregar

- Google Classroom
- Google Drive
- AVA da instituição

###### Prazo Sugerido

Ao final da aula.

##### 11. Encerramento e Reflexão

Promova uma discussão com a turma:

###### Perguntas para reflexão

- Qual a função da área de preparação do Git?
- Por que o Git Add é uma etapa importante antes do commit?
- Quando é melhor adicionar apenas alguns arquivos em vez de todos?
- Como o Git ajuda a manter o histórico organizado?
