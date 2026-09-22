---
titulo: "Criando uma Conta no GitHub – Parte II"
tipo: rco-seed
disciplina: programacao-front-end
sigla_rco: PFE
trimestre: 2
ordem_rco: 52
serie: 2
aula_rco: "Aula 52"
slides: 20
tem_atividade: true
tem_pratica: true
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/2TRI/52-criando-uma-conta-no-github-parte-ii/52-criando-uma-conta-no-github-parte-ii.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/2TRI/52-criando-uma-conta-no-github-parte-ii/AULA 52_ATIVIDADE_PROGRAMAÇÃO FRONT END.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-001/AULAS_RCO/PFE/2TRI/52-criando-uma-conta-no-github-parte-ii/AULA 52_PRÁTICA_PROGRAMAÇÃO FRONT END.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Criando uma Conta no GitHub – Parte II

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- Programação Front-End
- 2ª Série
- Criando uma Conta no GitHub – Parte II
- Aula 52

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
- Aprender melhor sobre o git e github, criando uma conta na plataforma parte II.
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
- Iniciamos o processo de aprofundamento sobre as ferramentas Git e GitHub.

_1 imagem(ns) no slide._

### Slide 7

- Para pensarmos juntos...
- João é um desenvolvedor web iniciante e está trabalhando em seu primeiro projeto de website. Ele tem feito progressos significativos, mas agora ele precisa colaborar com sua amiga Ana, que é uma designer gráfica, para aprimorar a interface do usuário. João ouviu falar sobre o GitHub como uma plataforma para compartilhar código e colaborar, mas ele não tem certeza de como começar.

_1 imagem(ns) no slide._

### Slide 8

- Para pensarmos juntos...
- Qual é o primeiro passo que João deve tomar para compartilhar seu código com Ana através do GitHub?
- Troque ideias com seus colegas!

_2 imagem(ns) no slide._

### Slide 9

- Resposta
- O primeiro passo que João deve tomar é criar um repositório no GitHub. Em seguida, ele pode fazer o "push" do seu código local para este repositório remoto. Depois disso, João pode compartilhar o link do repositório com Ana, permitindo que ela acesse o código, faça alterações e "commit" essas alterações de volta para o repositório. Desta forma, ambos podem trabalhar juntos no mesmo código, mantendo um histórico de todas as alterações feitas.
- Fonte https://publicdomainvectors.org/pt/vetorial-gratis/Lista-de-verifica%C3%A7%C3%A3o/45330.html

_1 imagem(ns) no slide._

### Slide 10

- Conceituando
- O GitHub é uma plataforma de hospedagem de código-fonte que utiliza o sistema de controle de versão Git. Ele é um serviço essencial para muitos desenvolvedores, pois permite a colaboração e o compartilhamento de código de uma maneira organizada e eficiente.

_1 imagem(ns) no slide._

### Slide 11

- Conceituando
- O compartilhamento de código no GitHub é realizado através da criação de "repositórios". Um repositório é essencialmente um diretório de arquivos e pastas de um projeto, juntamente com o histórico de todas as alterações feitas nesses arquivos. Isso permite que os desenvolvedores rastreiem e revertam alterações quando necessário.

_1 imagem(ns) no slide._

### Slide 12

- Conceituando
- A principal vantagem do GitHub é a colaboração. Vários desenvolvedores podem trabalhar no mesmo projeto simultaneamente sem se atrapalharem. Eles podem fazer suas próprias alterações em uma "branch" separada e, em seguida, "merge" dessas alterações de volta ao projeto principal quando estiverem prontas. Isso facilita o desenvolvimento em equipe e reduz o risco de conflitos de código.

_1 imagem(ns) no slide._

### Slide 13

- Conceituando
- Além disso, o GitHub também é uma excelente ferramenta para o compartilhamento de código aberto. Projetos de código aberto são aqueles em que o código-fonte é disponibilizado publicamente para que qualquer pessoa possa visualizar, usar, modificar e distribuir. Isso promove a colaboração em grande escala e o avanço rápido da tecnologia.

_1 imagem(ns) no slide._

### Slide 14

- Ainda sobre Git e GitHub, vamos conhecer praticando?
- Na plataforma Alura vamos acessar o seguinte curso:
- Link para o curso: https://cursos.alura.com.br/course/git-github-repositorio-commit-versoes
- Ao longo das atividades, você vai encontrar alguns quizzes e eles não estão ali por acaso! Eles são oportunidades rápidas para testar seu entendimento, reforçar o que aprendeu e identificar pontos que ainda podem melhorar.

_3 imagem(ns) no slide._

### Slide 15

- Conta no GitHub
- 14 minutos
- Como criar a conta no GitHub.
- Link para tarefa: https://cursos.alura.com.br/course/git-github-repositorio-commit-versoes/task/106064
- Link de acesso a página: https://github.com/ a conta é gratuita, basta fazer o preenchimento do cadastro.
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 16

- Vamos praticar?
- Prepare-se, porque nessa atividade, você vai sair do modo aprender e entrar direto no modo praticar.
- A atividade prática vai colocar você diante de um desafio real, que faz relação com o conteúdo aprendido até aqui.

_1 imagem(ns) no slide._

### Slide 17

- O que vimos na aula de hoje:
- Aprendemos a criar uma conta no GitHub.

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

_Fonte: AULA 52_ATIVIDADE_PROGRAMAÇÃO FRONT END.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

Programação Front-End

2ª SÉRIE

ATIVIDADE AULA 52

Questão 1

Qual é a principal finalidade do GitHub?

a) Hospedagem de sites

b) Armazenamento de fotos

c) Hospedagem de código-fonte e facilitação da colaboração entre desenvolvedores

d) Compartilhamento de vídeos

Resposta correta: c) Hospedagem de código-fonte e facilitação da colaboração entre desenvolvedores

O GitHub é uma plataforma que hospeda código-fonte e facilita a colaboração entre desenvolvedores. Ele permite que os desenvolvedores rastreiem e gerenciem alterações no código, e também colaborar com outros desenvolvedores em projetos.

Questão 2

Como os desenvolvedores podem colaborar em um projeto no GitHub?

a) Eles precisam estar no mesmo local físico

b) Eles podem trabalhar em diferentes "branches" e fazer "merge" das alterações

c) Eles precisam enviar o código por e-mail uns aos outros

d) Eles só podem visualizar o código, mas não podem fazer alterações

Resposta correta: b) Eles podem trabalhar em diferentes "branches" e fazer "merge" das alterações

No GitHub, os desenvolvedores podem criar suas próprias "branches" de um projeto e trabalhar nelas independentemente. Quando as alterações estão prontas, eles podem fazer "merge" dessas alterações de volta ao projeto principal. Isso permite que vários desenvolvedores trabalhem no mesmo projeto simultaneamente sem se atrapalharem.

## Prática

_Fonte: AULA 52_PRÁTICA_PROGRAMAÇÃO FRONT END.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

PROGRAMAÇÃO FRONT END

2ª SÉRIE

ATIVIDADE PRÁTICA AULA 52

##### 1. Objetivo da Aula Prática

Ao final da aula prática, o estudante será capaz de:

- Criar e configurar corretamente uma conta no GitHub.
- Compreender o conceito de repositório.
- Criar seu primeiro repositório público.
- Compartilhar um repositório com colegas.
- Identificar como o GitHub apoia o trabalho colaborativo.
- Reconhecer a importância do versionamento no desenvolvimento de software.

###### Produto Final Esperado

O estudante deverá possuir:

- Conta GitHub ativa e configurada.
- Perfil personalizado.
- Primeiro repositório criado.
- Link do perfil e do repositório compartilhados com o professor.

##### 2. Ferramentas Recomendadas

###### GitHub

Para que serve: hospedagem de código-fonte e colaboração entre desenvolvedores.

Por que é adequado: é a plataforma mais utilizada para compartilhamento de projetos de software.

Como facilita o aprendizado: permite armazenar projetos, criar portfólio e trabalhar em equipe.

Site: https://github.com

###### Navegador Web

Para que serve: acesso à plataforma GitHub.

Por que é adequado: permite realizar todo o processo de cadastro e gerenciamento.

Como facilita o aprendizado: oferece uma interface simples para iniciantes.

###### VS Code

Para que serve: desenvolvimento de projetos e integração futura com Git.

Por que é adequado: amplamente utilizado no mercado.

Como facilita o aprendizado: prepara o estudante para as próximas etapas do versionamento.

Site: https://code.visualstudio.com

##### 3. Checklist Inicial

Antes de iniciar a prática, o estudante deve possuir:

Conta de e-mail válida

Navegador atualizado

Conexão com internet

VS Code instalado

Acesso ao site GitHub

Bloco de notas ou documento para registrar informações

###### Materiais de Apoio

GitHub:

https://github.com

Curso Alura:

https://cursos.alura.com.br/course/git-github-repositorio-commit-versoes

##### 4. Passo a Passo do Docente (Aula de até 50 minutos)

###### Preparações Necessárias

- Verificar acesso à internet.
- Garantir que todos os alunos possuam e-mail válido.
- Testar previamente o acesso ao GitHub.

###### Contextualização (5 minutos)

Apresente o cenário:

João precisa compartilhar seu projeto com Ana para que ambos possam trabalhar juntos.

Pergunte:

Como dois desenvolvedores conseguem trabalhar no mesmo projeto sem trocar arquivos por e-mail?

###### Revisão Conceitual (10 minutos)

Explique:

- O que é Git.
- O que é GitHub.
- O que é um repositório.
- O que significa colaboração em software.
Apresente exemplos de projetos colaborativos conhecidos.

###### Demonstração da Criação da Conta (10 minutos)

Demonstrar:

- Cadastro no GitHub.
- Escolha do nome de usuário.
- Confirmação do e-mail.
- Configuração básica do perfil.

###### Demonstração da Criação do Repositório (10 minutos)

Mostrar:

- Botão New Repository.
- Nomeação do projeto.
- Repositório público.
- Criação do repositório.
Explicar:

- finalidade dos repositórios;
- armazenamento de projetos.

###### Compartilhamento do Repositório (10 minutos)

Demonstrar:

- Como copiar o link do repositório.
- Como compartilhar com colegas.
- Como acessar repositórios públicos.

###### Fechamento (5 minutos)

Verificar:

- Contas criadas.
- Repositórios criados.
- Links funcionando.

###### Pontos de Atenção

- Escolher um nome de usuário profissional.
- Utilizar um e-mail válido.
- Guardar login e senha com segurança.
- Evitar nomes inadequados para repositórios.

##### 5. Atividade Prática — Descrição Geral

O estudante deverá criar sua conta GitHub e estruturar seu ambiente inicial de trabalho.

Durante a atividade ele deverá:

- Criar sua conta.
- Configurar seu perfil.
- Criar um repositório.
- Compartilhar o link do repositório com um colega.

###### Problema Real Simulado

Preparação de ambiente para colaboração em projetos de desenvolvimento de software.

###### Habilidade Desenvolvida

Utilização de ferramentas de versionamento e compartilhamento de código.

##### 6. Metodologia Ativa Utilizada

###### Aprendizagem Baseada em Projeto (PBL)

O estudante constrói seu próprio ambiente profissional.

###### Aprendizagem por Experimentação

Explora os recursos da plataforma GitHub.

###### Ensino por Descoberta

Investiga funcionalidades disponíveis no ambiente.

###### Elementos de Lemov

- Modelagem
- Prática Guiada
- Verificação de Compreensão
- Feedback Imediato
- Revisão

##### 7. Passo a Passo da Atividade Prática (para os alunos)

###### Etapa 1 – Criar Conta

- Acesse o site do GitHub.
- Clique em Sign Up.
- Informe:
- e-mail;
- senha;
- nome de usuário.
- Conclua o cadastro.
- Confirme o e-mail recebido.

###### Etapa 2 – Configurar Perfil

- Adicione:
- foto (opcional);
- nome completo;
- biografia simples.
Exemplo:

Estudante do Curso Técnico em Desenvolvimento de Sistemas.

###### Etapa 3 – Criar Repositório

- Clique em New Repository.
- Defina o nome:
- meu-primeiro-projeto
- Escolha a opção Public.
- Crie o repositório.

###### Etapa 4 – Compartilhar

- Copie o link do repositório.
- Compartilhe com um colega.
- Acesse o repositório de um colega.

###### Etapa 5 – Registro

- Faça um print:
- do perfil;
- do repositório.
- Salve os arquivos para entrega.

##### 8. Exemplo ou Demonstração

###### Estrutura Esperada

| Item | Exemplo |
| --- | --- |
| Usuário | joaosilva |
| Bio | Estudante de Desenvolvimento de Sistemas |
| Repositório | meu-primeiro-projeto |

###### Estrutura do Ambiente

- GitHub
- │
- ├── Perfil
- │
- ├── Repositório
- │
- └── Link Compartilhado

###### Fluxo de Compartilhamento

- Aluno
- ↓
- GitHub
- ↓
- Repositório
- ↓
- Compartilhamento
- ↓
- Colaboração

##### 9. Resultado Esperado

O estudante deverá apresentar:

- Conta GitHub criada.
- Perfil configurado.
- Repositório criado.
- Link compartilhado.
- Prints de comprovação.

###### Critérios de Verificação

O professor deverá verificar:

Conta criada corretamente

Perfil configurado

Repositório criado

Compartilhamento realizado

Compreensão dos conceitos apresentados

##### 10. Formato de Entrega da Atividade

###### O que deve ser enviado

- Print do perfil GitHub.
- Print do repositório criado.
- Link do perfil.
- Link do repositório.

###### Nomeação Sugerida

- Aula52_NomeSobrenome
Exemplo:

- Aula52_JoaoSilva

###### Onde Entregar

- Google Classroom
- Google Drive
- AVA da instituição

###### Prazo Sugerido

Ao final da aula.

##### 11. Encerramento e Reflexão

Promova uma conversa final com a turma:

###### Perguntas para reflexão

- Por que o GitHub é tão utilizado pelas empresas?
- Como o compartilhamento de código facilita o trabalho em equipe?
- Quais vantagens um desenvolvedor possui ao manter projetos publicados?
- Como o versionamento ajuda a evitar perda de trabalho?
