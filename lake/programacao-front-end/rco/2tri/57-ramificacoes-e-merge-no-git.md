---
titulo: "Ramificações e Merge no Git"
tipo: rco-seed
disciplina: programacao-front-end
sigla_rco: PFE
trimestre: 2
ordem_rco: 57
serie: 2
aula_rco: "Aula 57"
slides: 23
tem_atividade: true
tem_pratica: true
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/2TRI/57-ramificacoes-e-merge-no-git/57-ramificacoes-e-merge-no-git.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/2TRI/57-ramificacoes-e-merge-no-git/AULA 57_ATIVIDADE_PROGRAMAÇÃO FRONT END.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/2TRI/57-ramificacoes-e-merge-no-git/AULA 57_PRÁTICA_PROGRAMAÇÃO FRONT END.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Ramificações e Merge no Git

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- Programação Front-End
- 2ª Série
- Ramificações e Merge no Git
- Aula 57

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

_2 imagem(ns) no slide._

### Slide 7

- Para pensarmos juntos...
- Alex é um desenvolvedor iniciante que começou recentemente a trabalhar em uma equipe de desenvolvimento de software. Ele está trabalhando em um recurso em um novo branch e finalmente concluiu o seu trabalho. Entusiasmado, ele quer mesclar suas mudanças no branch principal (main), mas está um pouco nervoso pois nunca fez um merge antes.

_2 imagem(ns) no slide._

### Slide 8

- Para pensarmos juntos...
- Alex se pergunta se pode fazer o merge do seu branch diretamente para o branch principal sem nenhuma revisão. Isso é aconselhável?
- Conversem e apresentem suas visões

_2 imagem(ns) no slide._

### Slide 9

- Resposta
- Não, não é aconselhável que Alex faça o merge do seu branch diretamente no branch principal sem nenhuma revisão. Uma boa prática no desenvolvimento de software é fazer uma revisão de código antes de mesclar alterações importantes. Isso pode ser feito por meio de um pull request, por exemplo, que é uma solicitação para mesclar um branch com outro.

_3 imagem(ns) no slide._

### Slide 10

- Resposta
- Ele permite que outros membros da equipe revisem o código e façam comentários antes do merge ser realizado. Isso ajuda a manter a qualidade do código e reduz a chance de erros ou bugs serem introduzidos no branch principal.

_1 imagem(ns) no slide._

### Slide 11

- Conceituando
- No universo do Git, um "branch" é essencialmente uma versão independente do código. Ele permite que você crie uma "ramificação" do seu projeto onde você pode experimentar, desenvolver novas funcionalidades ou corrigir bugs, sem afetar a versão principal (geralmente chamada de "master" ou "main"). Isso é especialmente útil em equipes de desenvolvimento, onde cada desenvolvedor pode trabalhar em seu próprio branch sem interferir no trabalho dos outros.

_1 imagem(ns) no slide._

### Slide 12

- Por outro lado, "merge" é o processo de unir as alterações de um branch de volta ao branch principal ou a qualquer outro branch. Um merge pega o conteúdo de um branch de origem e o integra com o branch de destino. Isso é feito para reunir as mudanças feitas em diferentes branches (por exemplo, para combinar as características que foram desenvolvidas em separado).
- Conceituando

_1 imagem(ns) no slide._

### Slide 13

- Conceituando
- Ambos, branch e merge, são fundamentais para o fluxo de trabalho do Git. Eles permitem que múltiplos desenvolvedores trabalhem em paralelo - cada um em seu próprio branch - e depois juntem suas mudanças de volta para a linha principal do projeto quando estiverem prontos.

_1 imagem(ns) no slide._

### Slide 14

- Conceituando
- Além disso, branches e merges também são fundamentais para manter o controle do histórico de desenvolvimento. Cada merge registra explicitamente onde e quando duas linhas de desenvolvimento se uniram, preservando o contexto histórico de cada mudança.

_2 imagem(ns) no slide._

### Slide 15

- Conceituando
- Por fim, vale ressaltar que saber usar branches e merges corretamente é uma habilidade fundamental para qualquer desenvolvedor que trabalha em um ambiente de controle de versão, pois são ferramentas que permitem que o desenvolvimento de software seja eficiente, seguro e colaborativo.

_3 imagem(ns) no slide._

### Slide 16

- Ainda sobre Git e GitHub, vamos conhecer praticando?
- Na plataforma Alura vamos acessar o seguinte curso:
- Link para o curso: https://cursos.alura.com.br/course/git-github-repositorio-commit-versoes
- Ao longo das atividades, você vai encontrar alguns quizzes e eles não estão ali por acaso! Eles são oportunidades rápidas para testar seu entendimento, reforçar o que aprendeu e identificar pontos que ainda podem melhorar.

_3 imagem(ns) no slide._

### Slide 17

- Branch
- 6 minutos
- Durante todo o desenvolvimento deste curso, sempre utilizamos o main, que é o nosso projeto principal.
- Link para tarefa: https://cursos.alura.com.br/course/git-github-repositorio-commit-versoes/task/106073
- O que acontece, geralmente, quando vamos trabalhar em um cenário que tem mais de uma pessoa trabalhando no projeto é que existe o código principal, o main, antigamente era chamado de master e existem outras ramificações.
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 18

- Merge
- 6 minutos
- Estamos trabalhando com duas branches, a branch principal (main) e a branch de desenvolvimento.
- Link para tarefa: https://cursos.alura.com.br/course/git-github-repositorio-commit-versoes/task/106074
- Agora, precisamos pegar tudo que está em desenvolvimento e enviar para a main. Esse "enviar para a main" tem um nome técnico no mundo Git: merge. Nós vamos "mergear" esses dois.
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 19

- Vamos praticar?
- Prepare-se, porque nessa atividade, você vai sair do modo aprender e entrar direto no modo praticar.
- A atividade prática vai colocar você diante de um desafio real, que faz relação com o conteúdo aprendido até aqui.

_1 imagem(ns) no slide._

### Slide 20

- O que vimos na aula de hoje:
- Aprendemos o que é o Branch e o Merge dentro do Git em ambiente de desenvolvimento.

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

_Fonte: AULA 57_ATIVIDADE_PROGRAMAÇÃO FRONT END.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação Front-End

2ª SÉRIE

ATIVIDADE AULA 57

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

_Fonte: AULA 57_PRÁTICA_PROGRAMAÇÃO FRONT END.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

PROGRAMAÇÃO FRONT END

2ª SÉRIE

ATIVIDADE PRÁTICA AULA 57

##### 1. Objetivo da Aula Prática

Ao final da aula prática, o estudante será capaz de:

- Compreender o conceito de Branch (ramificação) no Git.
- Criar branches para desenvolvimento de novas funcionalidades.
- Trabalhar em uma branch independente sem afetar a branch principal.
- Realizar merges entre branches.
- Entender a importância das revisões antes da integração de código.
- Simular um fluxo básico de trabalho colaborativo.

###### Produto Final Esperado

O estudante deverá:

- Criar uma nova branch.
- Realizar alterações em um projeto.
- Registrar commits na branch criada.
- Executar o merge com a branch principal.
- Documentar o processo realizado.

##### 2. Ferramentas Recomendadas

###### Git

Para que serve: controle de versão distribuído.

Por que é adequado: permite criar linhas independentes de desenvolvimento.

Como facilita o aprendizado: possibilita simular fluxos profissionais utilizados por equipes de software.

Site: https://git-scm.com

###### GitHub

Para que serve: hospedagem de repositórios e colaboração.

Por que é adequado: permite visualizar branches e histórico de alterações.

Como facilita o aprendizado: aproxima os alunos do ambiente utilizado no mercado.

Site: https://github.com

###### Visual Studio Code (VS Code)

Para que serve: desenvolvimento e edição do projeto.

Por que é adequado: possui integração nativa com Git.

Como facilita o aprendizado: permite acompanhar visualmente as mudanças realizadas em cada branch.

Site: https://code.visualstudio.com

###### Git Bash ou Terminal

Para que serve: execução dos comandos Git.

Por que é adequado: fornece acesso completo aos recursos de versionamento.

Como facilita o aprendizado: permite compreender o funcionamento interno do Git.

##### 3. Checklist Inicial

Antes de iniciar a prática, o estudante deve possuir:

Git instalado

VS Code instalado

Conta GitHub ativa

Repositório local configurado

Projeto disponível para testes

Conexão com internet

Git Bash ou Terminal funcionando

###### Materiais de Apoio

Git:

https://git-scm.com

GitHub:

https://github.com

Curso Alura:

https://cursos.alura.com.br/course/git-github-repositorio-commit-versoes

##### 4. Passo a Passo do Docente (Aula de até 50 minutos)

###### Preparações Necessárias

- Confirmar que todos possuem um repositório local.
- Verificar instalação do Git.
- Garantir acesso ao VS Code e ao terminal.
- Disponibilizar um projeto simples para testes.

###### Contextualização (5 minutos)

Apresente o cenário:

Uma equipe precisa desenvolver uma nova funcionalidade sem comprometer a versão estável do sistema.

Pergunta para a turma:

Como desenvolver algo novo sem correr o risco de quebrar o código principal?

###### Conceituando Branches (10 minutos)

Explique:

- O que é uma branch.
- Branch principal (main).
- Branch de desenvolvimento.
- Trabalho paralelo em equipes.
Apresente um diagrama simples:

- Main
- ├── Feature Login
- ├── Feature Cadastro
- └── Correção de Bug

###### Conceituando Merge (10 minutos)

Explique:

- O que é merge.
- Quando realizar merge.
- Boas práticas antes da integração.
- Importância da revisão de código.
Apresente o conceito de Pull Request de forma introdutória.

###### Demonstração Prática (10 minutos)

Demonstrar:

- Criação de branch.
- Alteração de arquivos.
- Commit na branch.
- Retorno para a main.
- Merge da branch.
Mostrar visualmente o histórico.

###### Prática Guiada (10 minutos)

Orientar os alunos a:

- Criar branch própria.
- Modificar projeto.
- Registrar commit.
- Realizar merge.

###### Encerramento (5 minutos)

Validar:

- Branch criada.
- Commit registrado.
- Merge realizado com sucesso.

###### Pontos de Atenção

- Confirmar qual branch está ativa antes de alterar arquivos.
- Não realizar merge sem testar alterações.
- Utilizar nomes claros para branches.
- Registrar commits descritivos.

##### 5. Atividade Prática — Descrição Geral

O estudante deverá simular o trabalho de uma equipe de desenvolvimento.

Cada aluno criará uma nova funcionalidade em uma branch separada e, após concluir o desenvolvimento, integrará essa funcionalidade à branch principal através do merge.

###### Problema Real Simulado

Desenvolvimento de uma nova funcionalidade sem comprometer a estabilidade do sistema principal.

###### Habilidade Desenvolvida

Gerenciamento de versões utilizando branches e integração de código por meio de merge.

##### 6. Metodologia Ativa Utilizada

###### Aprendizagem Baseada em Projeto (PBL)

Os alunos trabalham em um projeto versionado semelhante ao ambiente profissional.

###### Aprendizagem por Experimentação

Executam comandos reais de branch e merge.

###### Aprendizagem Colaborativa

Simulam o fluxo utilizado por equipes de desenvolvimento.

###### Elementos de Lemov

- Modelagem
- Prática Guiada
- Verificação de Compreensão
- Feedback Imediato
- Revisão

##### 7. Passo a Passo da Atividade Prática (para os alunos)

###### Etapa 1 – Preparação

- Abra o projeto no VS Code.
- Verifique a branch atual.
- Atualize o repositório local, se necessário.

###### Etapa 2 – Criar Branch

- Crie uma nova branch chamada:
- feature-seunome
Exemplo:

- feature-maria
- Acesse a nova branch.

###### Etapa 3 – Desenvolver Alteração

- Escolha um arquivo do projeto.
- Realize uma melhoria:
- adicionar seção;
- alterar texto;
- adicionar imagem;
- melhorar layout.
- Salve as alterações.

###### Etapa 4 – Registrar Commit

- Adicione os arquivos modificados.
- Crie um commit descritivo.
Exemplo:

- Adiciona seção de contato

###### Etapa 5 – Realizar Merge

- Retorne para a branch principal.
- Execute o merge da branch criada.
- Verifique se a alteração foi integrada.

###### Etapa 6 – Evidências

- Capture prints:
- da branch criada;
- do commit realizado;
- do merge concluído.

##### 8. Exemplo ou Demonstração

###### Fluxo de Branches

- Main
- │
- ├── feature-login
- │
- ├── feature-cadastro
- │
- └── feature-relatorios

###### Fluxo de Merge

- feature-login
- │
- ▼
- Merge
- │
- ▼
- Main

###### Fluxo Completo

- Criar Branch
- ↓
- Modificar Arquivos
- ↓
- Commit
- ↓
- Merge
- ↓
- Projeto Atualizado

##### 9. Resultado Esperado

O estudante deverá apresentar:

- Branch criada corretamente.
- Alteração desenvolvida.
- Commit registrado.
- Merge concluído.
- Projeto funcionando após integração.

###### Critérios de Verificação

O professor deverá verificar:

Criação correta da branch

Alteração realizada na branch

Commit registrado

Merge executado corretamente

Funcionamento do projeto após integração

##### 10. Formato de Entrega da Atividade

###### O que deve ser enviado

- Print da criação da branch.
- Print do histórico de commits.
- Print do merge realizado.
- Link do repositório GitHub.

###### Nomeação Sugerida

- Aula57_NomeSobrenome
Exemplo:

- Aula57_AnaSouza

###### Onde Entregar

- Google Classroom
- Google Drive
- AVA da instituição

###### Prazo Sugerido

Ao final da aula.

##### 11. Encerramento e Reflexão

Promova uma discussão com a turma:

###### Perguntas para reflexão

- Por que as branches são importantes em projetos colaborativos?
- Qual o risco de trabalhar diretamente na branch principal?
- Como o merge ajuda na organização do desenvolvimento?
- Por que a revisão de código é recomendada antes de integrar alterações?
