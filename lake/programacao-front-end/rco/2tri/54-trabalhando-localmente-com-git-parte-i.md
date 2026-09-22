---
titulo: "Trabalhando localmente Parte I"
tipo: rco-seed
disciplina: programacao-front-end
sigla_rco: PFE
trimestre: 2
ordem_rco: 54
serie: 2
aula_rco: "Aula 54"
slides: 22
tem_atividade: true
tem_pratica: true
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/PFE/2TRI/54-trabalhando-localmente-com-git-parte-i/54-trabalhando-localmente-com-git-parte-i.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/2TRI/54-trabalhando-localmente-com-git-parte-i/AULA 54_ATIVIDADE_PROGRAMAÇÃO FRONT END.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/2TRI/54-trabalhando-localmente-com-git-parte-i/AULA 54_PRÁTICA_PROGRAMAÇÃO FRONT END.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Trabalhando localmente Parte I

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- Programação Front-End
- 2ª Série
- Trabalhando localmente Parte I
- Aula 54

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
- Aprender a utilizar o serviço Git de forma local.
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
- Aprendemos como utilizar o VS Code em conjunto com o GitHub.

_1 imagem(ns) no slide._

### Slide 7

- Para pensarmos juntos...
- João é um desenvolvedor iniciante que está começando a trabalhar em seu primeiro grande projeto. Ele ouviu falar sobre o Git e entende que é uma ferramenta poderosa para controle de versão, mas ele só teve experiência usando-o em um contexto online até agora. João tem um longo voo pela frente e planeja usar esse tempo para trabalhar em seu projeto, mas está preocupado que não será capaz de usar o Git durante o voo, já que não terá acesso à internet.

_1 imagem(ns) no slide._

### Slide 8

- Para pensarmos juntos...
- João pode continuar usando o Git para controle de versão em seu projeto durante o voo, mesmo sem acesso à internet?
- Conversem e apresentem suas visões

_2 imagem(ns) no slide._

### Slide 9

- Resposta
- Sim, João pode continuar usando o Git para controle de versão em seu projeto durante o voo, mesmo sem acesso à internet. Isso porque o Git é uma ferramenta de controle de versão distribuída, o que significa que ele pode ser usado localmente no computador de João, sem a necessidade de uma conexão com a internet ou um servidor central.

_1 imagem(ns) no slide._

### Slide 10

- Resposta
- João pode fazer commits, criar e mudar entre branches, e fazer várias outras tarefas do Git localmente. As únicas tarefas que exigem uma conexão com a internet são o push e o pull, que são usados para sincronizar o repositório local de João com um repositório remoto.

_19 imagem(ns) no slide._

### Slide 11

- Conceituando
- O Git é uma ferramenta de controle de versão distribuída, o que significa que pode ser usada localmente em seu computador, sem a necessidade de uma conexão com a internet ou um servidor central. A principal função do Git é permitir o rastreamento e gerenciamento de alterações em arquivos, especialmente útil no contexto de desenvolvimento de software.
- https://videosdeti.com.br/wp-content/uploads/2018/12/git-githu-cover.png

_3 imagem(ns) no slide._

### Slide 12

- Conceituando
- Além disso, o Git local é muito rápido, já que todas as operações são executadas localmente, sem a necessidade de se comunicar com um servidor remoto.
- https://lh3.googleusercontent.com/70jaEZnESXQ6SssU5uI4yO62JBz6xq2sNrrz8bW_ap2CuWUaQlbKs3j6NyRJnvcvYwAugkW8WzNJX21dZ2SMd9O_1TTpKZT-FsBkYSPy4rUSpJSo2C-WPTaLc2jQ8ancyj1TetXQ
- O uso local do Git é especialmente útil por várias razões. Primeiro, ele oferece a capacidade de trabalhar offline. Como todas as operações (exceto o push e o pull) são locais, você pode continuar trabalhando mesmo quando não está conectado à internet.

_1 imagem(ns) no slide._

### Slide 13

- Conceituando
- Além disso, o Git local permite que você faça experimentos seguros. Você pode criar novos branches (ramificações) para experimentar novas ideias ou recursos e, em seguida, mesclá-los de volta ao branch principal quando estiverem prontos. Se algo der errado, você pode facilmente voltar ao estado anterior do seu projeto usando o histórico de commit.

_1 imagem(ns) no slide._

### Slide 14

- Conceituando
- Por último, o Git local incentiva o comprometimento frequente do código. Como você não precisa estar online para fazer um commit, é mais provável que você faça commits menores e mais frequentes, o que é considerado uma boa prática em desenvolvimento de software. Esses commits frequentes criam um histórico detalhado do progresso do seu projeto, facilitando a identificação de quando e onde os erros foram introduzidos.

_5 imagem(ns) no slide._

### Slide 15

- Ainda sobre Git e GitHub, vamos conhecer praticando?
- Na plataforma Alura vamos acessar o seguinte curso:
- Link para o curso: https://cursos.alura.com.br/course/git-github-repositorio-commit-versoes
- Ao longo das atividades, você vai encontrar alguns quizzes e eles não estão ali por acaso! Eles são oportunidades rápidas para testar seu entendimento, reforçar o que aprendeu e identificar pontos que ainda podem melhorar.

_3 imagem(ns) no slide._

### Slide 16

- Git clone e log
- 7 minutos
- Até agora, estávamos usando o site do GitHub! Cadê o Git?
- Link para tarefa: https://cursos.alura.com.br/course/git-github-repositorio-commit-versoes/task/106068
- Quando usamos o GitHub estamos sempre usando o Git. Por que essa diferença? Por que essas palavras? GitHub é uma empresa, que inclusive foi comprada pela Microsoft. Mas ela foi criada justamente para facilitar o uso do Git.
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 17

- Git status, commit e push
- 14 minutos
- Nós fizemos muitas das edições lá no site do GitHub, já percebemos vendo o log no Git.
- Link para tarefa: https://cursos.alura.com.br/course/git-github-repositorio-commit-versoes/task/106069
- A grande sacada que o Linus Torvalds teve quando criou o Git, foi que esse repositório não é centralizado, ele está tanto no GitHub quanto agora, depois que você fez o comando git clone, ele está na sua máquina. É um sistema de controle de versão distribuído.
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 18

- Vamos praticar?
- Prepare-se, porque nessa atividade, você vai sair do modo aprender e entrar direto no modo praticar.
- A atividade prática vai colocar você diante de um desafio real, que faz relação com o conteúdo aprendido até aqui.

_1 imagem(ns) no slide._

### Slide 19

- O que vimos na aula de hoje:
- Aprendemos a utilizar o Git de forma local no ambiente de desenvolvimento.

_1 imagem(ns) no slide._

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

_Fonte: AULA 54_ATIVIDADE_PROGRAMAÇÃO FRONT END.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação Front-End

2ª SÉRIE

ATIVIDADE AULA 54

Questão 1

Qual das seguintes ações você pode realizar localmente com o Git, mesmo sem uma conexão com a internet?

A) Clonar um repositório do GitHub.

B) Fazer push de suas alterações para um repositório remoto.

C) Fazer um commit de suas alterações.

D) Fazer um pull das últimas alterações de um repositório remoto.

Resposta correta:

C) Fazer um commit de suas alterações.

Isso é algo que você pode fazer localmente com o Git, mesmo sem uma conexão com a internet. As outras opções envolvem interações com um repositório remoto, que exigiriam uma conexão com a internet.

Questão 2

Qual das seguintes afirmações é verdadeira sobre o Git?

A) O Git pode ser usado para rastrear alterações localmente, mesmo sem uma conexão com a internet.

B) O Git só pode ser usado com repositórios remotos.

C) O Git requer uma conexão com a internet para funcionar.

D) O Git não permite que você reverta para versões anteriores de seu código sem uma conexão com a internet.

Resposta correta:

A) O Git pode ser usado para rastrear alterações localmente, mesmo sem uma conexão com a internet.

Isso é verdade porque o Git é uma ferramenta de controle de versão distribuída, o que significa que ele pode ser usado localmente sem a necessidade de uma conexão com a internet ou um servidor central. As outras opções são falsas.

## Prática

_Fonte: AULA 54_PRÁTICA_PROGRAMAÇÃO FRONT END.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

PROGRAMAÇÃO FRONT END

2ª SÉRIE

ATIVIDADE PRÁTICA AULA 54

##### 1. Objetivo da Aula Prática

Ao final da aula prática, o estudante será capaz de:

- Compreender o funcionamento do Git local.
- Clonar um repositório remoto para sua máquina.
- Identificar alterações em arquivos utilizando o Git.
- Realizar commits localmente.
- Consultar o histórico de alterações de um projeto.
- Sincronizar alterações entre ambiente local e GitHub.

###### Produto Final Esperado

O estudante deverá:

- Clonar um repositório GitHub.
- Realizar alterações em arquivos locais.
- Registrar pelo menos 2 commits.
- Consultar o histórico utilizando o comando log.
- Enviar as alterações para o GitHub.

##### 2. Ferramentas Recomendadas

###### Git

Para que serve: controle de versão distribuído.

Por que é adequado: permite trabalhar mesmo sem conexão com internet.

Como facilita o aprendizado: possibilita registrar alterações localmente e compreender o funcionamento do versionamento.

Site: https://git-scm.com

###### GitHub

Para que serve: hospedagem dos repositórios.

Por que é adequado: permite sincronizar e compartilhar projetos.

Como facilita o aprendizado: possibilita visualizar o histórico e acompanhar as alterações.

Site: https://github.com

###### Visual Studio Code (VS Code)

Para que serve: edição dos arquivos do projeto.

Por que é adequado: possui integração nativa com Git.

Como facilita o aprendizado: permite executar operações de versionamento sem sair do ambiente de desenvolvimento.

Site: https://code.visualstudio.com

###### Terminal Git Bash

Para que serve: execução dos comandos Git.

Por que é adequado: fornece acesso completo às funcionalidades do Git.

Como facilita o aprendizado: permite compreender o funcionamento dos comandos utilizados no mercado.

##### 3. Checklist Inicial

Antes de iniciar a prática, o estudante deve possuir:

Git instalado

VS Code instalado

Conta GitHub criada

Repositório GitHub criado

Conexão com internet

Acesso ao Git Bash ou Terminal

Projeto disponível no GitHub

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
- Verificar acesso ao GitHub.
- Garantir que todos possuam um repositório.
- Testar acesso ao terminal.

###### Contextualização (5 minutos)

Apresente o cenário:

João está em uma viagem sem internet e precisa continuar desenvolvendo seu projeto.

Pergunta:

É possível utilizar Git sem conexão com a internet?

Conduzir a discussão antes da explicação.

###### Conceituando Git Local (10 minutos)

Explicar:

- Controle de versão distribuído.
- Repositório local.
- Diferença entre Git e GitHub.
- Operações que funcionam offline:
- commit
- branch
- log
- status
Explicar que apenas push e pull dependem de conexão.

###### Demonstração do Clone (10 minutos)

Demonstrar:

- Copiar URL do repositório.
- Executar clone.
- Abrir projeto no VS Code.
Explicar o conceito de cópia local do projeto.

###### Demonstração dos Comandos Básicos (10 minutos)

Demonstrar:

- status
- commit
- log
- push
Mostrar o fluxo completo de alteração.

###### Prática Guiada (10 minutos)

Os alunos deverão:

- Clonar repositório.
- Alterar arquivos.
- Criar commits.
- Visualizar histórico.
- Enviar alterações.

###### Encerramento (5 minutos)

Verificar:

- Repositório clonado.
- Histórico de commits.
- Alterações sincronizadas.

###### Pontos de Atenção

- Não apagar arquivos do projeto.
- Verificar mensagens de commit.
- Confirmar que o clone foi realizado corretamente.
- Conferir se o push foi concluído.

##### 5. Atividade Prática — Descrição Geral

O estudante deverá trabalhar com um repositório Git localmente, simulando uma situação real de desenvolvimento sem depender constantemente do GitHub.

A atividade consiste em:

- Clonar um projeto.
- Realizar alterações locais.
- Registrar commits.
- Consultar histórico.
- Sincronizar alterações.

###### Problema Real Simulado

Desenvolvimento de software durante um período sem acesso à internet.

###### Habilidade Desenvolvida

Versionamento local de código utilizando Git.

##### 6. Metodologia Ativa Utilizada

###### Aprendizagem Baseada em Projeto (PBL)

Os alunos trabalham sobre um projeto real.

###### Aprendizagem por Experimentação

Executam comandos reais do Git.

###### Ensino por Descoberta

Observam o comportamento do repositório local.

###### Elementos de Lemov

- Modelagem
- Prática Guiada
- Verificação de Compreensão
- Feedback Imediato
- Revisão

##### 7. Passo a Passo da Atividade Prática (para os alunos)

###### Etapa 1 – Clonar o Repositório

- Acesse seu repositório GitHub.
- Copie a URL do projeto.
- Abra o Git Bash.
- Execute o comando de clone.
- Abra a pasta criada no VS Code.

###### Etapa 2 – Alterar Arquivos

- Abra um arquivo do projeto.
- Adicione:
- novo texto;
- nova seção;
- ou melhoria visual.
- Salve o arquivo.

###### Etapa 3 – Verificar Alterações

- Abra o terminal.
- Consulte o status do projeto.
- Observe os arquivos modificados.

###### Etapa 4 – Criar Commit

- Adicione as alterações ao controle de versão.
- Crie uma mensagem de commit.
- Realize o commit.
Exemplo:

- Atualiza conteúdo da página inicial

###### Etapa 5 – Consultar Histórico

- Visualize o histórico de commits.
- Identifique o commit recém-criado.

###### Etapa 6 – Sincronizar

- Envie as alterações ao GitHub.
- Atualize o repositório no navegador.
- Confirme o envio.

##### 8. Exemplo ou Demonstração

###### Fluxo do Git Local

- Repositório GitHub
- ↓
- Clone
- ↓
- Repositório Local
- ↓
- Alteração
- ↓
- Commit
- ↓
- Push
- ↓
- GitHub Atualizado

###### Comandos Trabalhados

| Comando | Função |
| --- | --- |
| git clone | Clonar repositório |
| git status | Verificar alterações |
| git commit | Registrar alterações |
| git log | Visualizar histórico |
| git push | Enviar alterações |

###### Exemplo de Histórico

- Commit 1 → Projeto inicial
- Commit 2 → Atualização do menu
- Commit 3 → Inclusão de nova seção

##### 9. Resultado Esperado

O estudante deverá apresentar:

- Repositório clonado localmente.
- Arquivo modificado.
- Pelo menos dois commits realizados.
- Histórico consultado.
- Alterações enviadas ao GitHub.

###### Critérios de Verificação

O professor deverá verificar:

Clone realizado corretamente

Alterações registradas

Histórico atualizado

Commit com descrição adequada

Push realizado com sucesso

##### 10. Formato de Entrega da Atividade

###### O que deve ser enviado

- Print do terminal mostrando o histórico.
- Print do repositório atualizado.
- Link do repositório GitHub.

###### Nomeação Sugerida

- Aula54_NomeSobrenome
Exemplo:

- Aula54_JoaoSilva

###### Onde Entregar

- Google Classroom
- Google Drive
- AVA da instituição

###### Prazo Sugerido

Ao final da aula.

##### 11. Encerramento e Reflexão

Promova uma discussão com a turma:

###### Perguntas para reflexão

- Por que o Git consegue funcionar sem internet?
- Qual a vantagem de possuir um repositório local?
- Como o histórico de commits ajuda no desenvolvimento?
- Em quais situações trabalhar offline pode ser importante?
