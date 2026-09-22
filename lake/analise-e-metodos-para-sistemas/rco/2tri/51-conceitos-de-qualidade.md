---
titulo: "Conceitos de Qualidade"
tipo: rco-seed
disciplina: analise-e-metodos-para-sistemas
sigla_rco: AMS
trimestre: 2
ordem_rco: 51
serie: 1
aula_rco: "Aula 51"
slides: 25
tem_atividade: true
tem_pratica: true
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/AMS/2TRI/51-conceitos-de-qualidade/51-conceitos-de-qualidade.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/AMS/2TRI/51-conceitos-de-qualidade/AULA 51_ATIVIDADE_ANÁLISE E MÉTODO PARA SISTEMAS.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/AMS/2TRI/51-conceitos-de-qualidade/AULA 51_PRÁTICA_ANÁLISE E MÉTODO PARA SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Conceitos de Qualidade

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- ANÁLISE E MÉTODO PARA SISTEMAS
- 1ª Série
- Conceitos de Qualidade
- Aula 51

_1 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- COMPETÊNCIA(S) A SER(EM) DESENVOLVIDA(S) NESTA AULA:
- De acordo com o Plano de Curso de Desenvolvimento de Sistemas:
- HABILIDADE(S) A SER(EM) DESENVOLVIDA(S) NESTA AULA:
- Executar alterações e manutenções em aplicações e rotinas de acordo com as definições estabelecidas.
- Manter registros para análise e refinamento de resultados.

_1 imagem(ns) no slide._

### Slide 4

- Nesta aula vamos:
- Aprender o conceito de qualidade.
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store

_4 imagem(ns) no slide._

### Slide 5

- Este material foi elaborado a partir da análise do plano de curso e reúne os conhecimentos essenciais para o Técnico em Desenvolvimento de Sistemas. As aulas foram organizadas com foco na clareza conceitual, na construção gradual dos conteúdos e na utilização de metodologias ativas que favorecem a compreensão, a participação e o desenvolvimento de habilidades e competências de forma significativa.
- De acordo com a matriz curricular do Curso Técnico em Desenvolvimento de Sistemas, que traz em sua essência componentes estruturados para a realização de aulas práticas, cada unidade curricular deve contemplar, além da abordagem teórica, uma proposta de atividade prática a ser desenvolvida pelo professor. Essa orientação assegura a coerência entre o planejamento didático e o que está estabelecido na matriz, promovendo experiências formativas alinhadas ao perfil profissional previsto.
- O professor tem total autonomia para adaptar o conteúdo conforme o contexto da turma, ajustando exemplos, aprofundamentos e estratégias didáticas para otimizar a aprendizagem e a conexão com a prática profissional.
- Se houver falta de conexão ou indisponibilidade de internet durante a aula, os materiais abaixo podem ser utilizados como apoio para elaborar recursos complementares, garantindo a continuidade da abordagem teórica prevista.
- ATENÇÃO PROFESSOR!
- Scrum e PDCA:
- https://cursos.alura.com.br/course/scrum-parte-6/task/109219

_2 imagem(ns) no slide._

### Slide 6

- Aula anterior
- Aprendemos como a qualidade é gerenciada na ferramenta Scrum.

_1 imagem(ns) no slide._

### Slide 7

- Para pensarmos juntos...
- Paulo é um desenvolvedor júnior em uma startup de software. Ele foi designado para liderar um pequeno projeto para melhorar a funcionalidade do sistema de gestão da empresa. Paulo decidiu aplicar o ciclo PDCA para gerenciar esse projeto.
- Na etapa de Planejamento (Plan), ele definiu que a funcionalidade melhorada deve ser capaz de gerar relatórios personalizados para os usuários. Paulo então começou a Fazer (Do) o trabalho: ele codificou a nova funcionalidade, testou e documentou as mudanças.

_1 imagem(ns) no slide._

### Slide 8

- Para pensarmos juntos...
- Quando ele passou para a etapa de Verificação (Check), percebeu que a funcionalidade não estava gerando os relatórios como esperado. Alguns relatórios saíam incompletos e outros com informações erradas.
- O que Paulo deve fazer na etapa Agir (Act) do ciclo PDCA?
- Quem sabe levanta a mão.

_2 imagem(ns) no slide._

### Slide 9

- Para pensarmos juntos...
- A) Ignorar o problema, já que a funcionalidade está "boa o suficiente".
- B) Começar um novo projeto para corrigir os problemas.
- C) Analisar o problema e ajustar o código para corrigir os erros.
- D) Delegar a resolução do problema para um colega mais experiente.

_1 imagem(ns) no slide._

### Slide 10

- Resposta
- A resposta correta é a alternativa C. De acordo com o ciclo PDCA, na etapa de Agir, Paulo deve fazer correções e ajustes com base nas descobertas da fase de Verificação. Isso pode envolver a revisão e correção do código para resolver os problemas encontrados. As outras alternativas não seguem o princípio do ciclo PDCA de melhoria contínua.

_1 imagem(ns) no slide._

### Slide 11

- Conceituando
- O ciclo PDCA (Plan-Do-Check-Act) é uma metodologia amplamente utilizada em gestão de qualidade e é especialmente útil no desenvolvimento de sistemas. A ideia é que a gestão de qualidade seja um processo cíclico, que deve ser constantemente revisado e aprimorado.
- https://uploads-ssl.webflow.com/6399c61683700ed8ab159d36/639fb83838e93f1925021316_Base-imagem-destacada-blog.png

_1 imagem(ns) no slide._

### Slide 12

- Conceituando
- Plan (Planejar): Nesta etapa, é preciso identificar um objetivo ou problema, analisar a situação atual, definir metas e traçar um plano de ação. No desenvolvimento de sistemas, isso pode envolver definir o que o sistema deve fazer, quem são os usuários, quais tecnologias serão usadas, quais prazos e recursos estão disponíveis, entre outros.

_1 imagem(ns) no slide._

### Slide 13

- Conceituando
- A ideia é desenvolver uma versão inicial do sistema para testar se o plano é viável.
- Do (Fazer): Aqui, o plano é colocado em prática. No contexto do desenvolvimento de sistemas, isso envolve atividades como codificação, teste e documentação do software.

_1 imagem(ns) no slide._

### Slide 14

- Conceituando
- Check (Verificar): Nesta fase, é realizada uma análise crítica do que foi feito, para verificar se o resultado está alinhado com o plano original. No desenvolvimento de sistemas, pode envolver testes de software, revisões de código, feedback dos usuários, entre outros. O importante aqui é identificar qualquer desvio em relação ao plano e entender suas causas.

_1 imagem(ns) no slide._

### Slide 15

- Conceituando
- Act (Agir): Esta etapa envolve fazer as correções necessárias e ajustes com base nas descobertas da fase de Verificação. Pode ser necessário refazer parte do trabalho, ajustar o plano original ou até mesmo iniciar um novo ciclo PDCA.
- https://www.neomind.com.br/wp-content/uploads/2020/01/pratica2.png

_1 imagem(ns) no slide._

### Slide 16

- Sobre qualidade, vamos conhecer praticando?
- Na plataforma Alura, vamos acessar o seguinte curso:
- Link para o curso: https://cursos.alura.com.br/course/scrum-parte-6
- Ao longo das atividades, você vai encontrar alguns quizzes e eles não estão ali por acaso! Eles são oportunidades rápidas para testar seu entendimento, reforçar o que aprendeu e identificar pontos que ainda podem melhorar.

_3 imagem(ns) no slide._

### Slide 17

- Ciclo PDCA
- 4 minutos
- O ciclo PDCA (Plan, Do, Check, Act - PDCA) é uma ferramenta no gerenciamento da qualidade e serve para planejar, fazer, verificar e agir.
- Link para tarefa: https://cursos.alura.com.br/course/scrum-parte-6/task/22470
- Planejar a qualidade, portanto, significa pensar em como trabalhar o Backlog do Produto. O Fazer refere-se a como rodar a Sprint. Verificar aponta para a revisão de produto e agir a como elencar pontos de melhoria para evoluir.
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 18

- Scrum de Scrums
- 6 minutos
- O alinhamento entre os times Scrum é geralmente realizado por meio de reuniões de Scrum of Scrums.
- Link para tarefa: https://cursos.alura.com.br/course/scrum-parte-6/task/22471
- Esta é uma reunião diária que acontece na qual um representante (normalmente o Scrum Master ou um membro da equipe designado) de cada equipe compartilha atualizações e informações importantes, incluindo progresso, obstáculos e dependências entre as equipes. Dessa forma, todos os times estão alinhados e cientes do panorama geral do projeto.
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 19

- Revisão e Validação
- 5 minutos
- No Scrum, a revisão e validação ocorrem durante a Sprint Review, uma cerimônia ao final de cada Sprint.
- Link para tarefa: https://cursos.alura.com.br/course/scrum-parte-6/task/22472
- A equipe apresenta o trabalho concluído durante a Sprint ao Product Owner e aos stakeholders. Eles revisam, fornecem feedback e validam se o trabalho atende aos critérios de aceitação definidos. Esta reunião ajuda a garantir que o produto esteja se desenvolvendo conforme necessário e esperado.
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 20

- Retrospectiva
- 5 minutos
- A retrospectiva do Scrum é uma cerimônia que ocorre ao final de cada Sprint, após a Revisão da Sprint e antes do próximo Planejamento da Sprint.
- Link para tarefa: https://cursos.alura.com.br/course/scrum-parte-6/task/22473
- Nesta reunião, a equipe Scrum reflete sobre o que funcionou bem e o que pode ser melhorado para a próxima Sprint. É uma oportunidade para aprendizado contínuo, melhoria de processos e para reforçar a auto-organização da equipe.
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 21

- Vamos praticar?
- Prepare-se, porque nessa atividade, você vai sair do modo aprender e entrar direto no modo praticar.
- A atividade prática vai colocar você diante de um desafio real: sensação de ver seu próprio código aparecer online! Acessível, documentado e pronto para o mundo!

_1 imagem(ns) no slide._

### Slide 22

- O que vimos na aula de hoje:
- Aprendemos sobre o ciclo PDCA e a relação com o Scrum.

_1 imagem(ns) no slide._

### Slide 23

- Pronto para desbloquear sua carreira de TI?
- Está perdido estudando mas não sabe por onde começar? Se a resposta é sim, você está no lugar certo! Descubra as estratégias e ferramentas essenciais para te ajudar a desbloquear seu potencial em TI e buscar sua primeira vaga de emprego no setor!
- Este e-book é um guia completo para quem busca começar pelos melhores caminhos para se tornar um excelente profissional de TI, ensinando a identificar perfis profissionais, aplicar técnicas de estudo eficazes, transformar teoria em prática, e aumentar a visibilidade de seu trabalho no mercado de trabalho. Ideal para novatos e profissionais em transição.
- E o melhor, ele pode ser seu, inteiramente grátis!
- Basta clicar AQUI e realizar o seu cadastro com o seu @escola!

_3 imagem(ns) no slide._

### Slide 24

- Referências
- AFFONSO DE OLIVEIRA, Maurício. Análise e Projeto de Sistemas de Informação Orientados para a Internet. São Paulo: Érica, 2007.
- BEZERRA, Eduardo. Engenharia de Requisitos: Software Orientado ao Negócio. São Paulo: Novatec, 2010.
- BOOCH, Grady; RUMBAUGH, James; JACOBSON, Ivar. UML - Guia do Usuário. 2ª ed. Rio de Janeiro: Campus, 2005.
- GANE, Chris; SARSON, Trish. Análise Estruturada de Sistemas. Rio de Janeiro: LTC, 1995.
- MAGNO DA SILVA NOVAES, Carlos; SAMPAIO DO PRADO LEITE, Júlio César. Análise e Projeto de Sistemas de Informação com UML e Unified Process. São Paulo: Elsevier, 2003.
- PRESSMAN, Roger S.; MAXIM, Bruce R. Engenharia de Software: Uma Abordagem Profissional. 7ª ed. Porto Alegre: AMGH, 2016.
- PRESSMAN, Roger S. Engenharia de Software: Conceitos e Práticas. São Paulo: McGraw-Hill, 2011.
- RITTER, Tiago. Gerenciamento de Projetos: Como definir e controlar o escopo do projeto. São Paulo: Casa do Código, 2017.
- SOARES, Raphael. Metodologia de Desenvolvimento de Software: Um Guia Prático para Iniciantes. São Paulo: Novatec, 2014.
- SOUSA, André S. C.; GUISSI, Viviane Cristina. Modelagem de Processos de Negócio. São Paulo: Érica, 2012.
- Figuras e Imagens:
- https://www.flaticon.com/br
- https://www.istockphoto.com/br
- https://raw.githubusercontent.com/zbtang/React-Native-ViewPager/HEAD/imgs/dotIndicator.gif
- https://storyset.com

### Slide 25

_(sem texto)_

## Atividade

_Fonte: AULA 51_ATIVIDADE_ANÁLISE E MÉTODO PARA SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

ANÁLISE E MÉTODO PARA SISTEMAS

1ª SÉRIE

ATIVIDADE AULA 51

Questão 1

No ciclo PDCA, o que significa a etapa "Plan"?

A) Executar a tarefa.

B) Verificar os resultados.

C) Planejar a tarefa.

D) Ajustar as ações.

Comentário:

A resposta correta é a alternativa C. "Plan", no inglês, significa planejar. Esta é a fase do ciclo PDCA em que se define o problema a ser resolvido, identificam-se os objetivos e planeja-se como atingir esses objetivos.

Questão 2

Como o ciclo PDCA se aplica ao desenvolvimento de software?

A) O ciclo PDCA não tem aplicação no desenvolvimento de software.

B) O ciclo PDCA é aplicado uma única vez durante a criação do software.

C) O ciclo PDCA é aplicado apenas na fase de manutenção do software.

D) O ciclo PDCA é aplicado continuamente ao longo do ciclo de vida do software.

Comentário:

A resposta correta é a alternativa D. O ciclo PDCA é uma ferramenta de gestão de qualidade que pode ser aplicada continuamente ao longo do ciclo de vida do software, desde o planejamento até a manutenção, para promover a melhoria contínua.

## Prática

_Fonte: AULA 51_PRÁTICA_ANÁLISE E MÉTODO PARA SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

ANÁLISE E MÉTODO PARA SISTEMAS

1ª SÉRIE

ATIVIDADE PRÁTICA AULA 51

#### 1. Objetivo da Aula Prática

Ao final desta aula prática, o estudante deverá:

- Compreender o funcionamento do ciclo PDCA (Plan, Do, Check, Act).
- Relacionar os conceitos de qualidade com o desenvolvimento de sistemas.
- Desenvolver a habilidade de identificar problemas, propor melhorias e aplicar ações corretivas.
- Ser capaz de utilizar o ciclo PDCA para analisar e melhorar um processo simples de desenvolvimento de software.
- Entender como o PDCA se relaciona com práticas do Scrum, como Sprint Review e Retrospectiva.

#### 2. Ferramentas Recomendadas

###### Post-its ou Cartões de Papel

Para que serve: Registrar problemas, ações, verificações e melhorias.

Por que é adequada ao tema: Facilita a visualização das etapas do ciclo PDCA.

Como facilita o aprendizado: Permite organizar informações de forma simples e colaborativa.

###### Quadro Branco ou Cartolina

Para que serve: Montar visualmente o ciclo PDCA.

Por que é adequada ao tema: Ajuda a representar cada etapa do processo de melhoria contínua.

Como facilita o aprendizado: Torna o processo visível para toda a equipe.

###### Google Docs ou Planilhas Google

Para que serve: Documentar as etapas do PDCA.

Por que é adequada ao tema: Permite registrar decisões e melhorias identificadas.

Como facilita o aprendizado: Ajuda na organização e análise das informações.

###### Trello (Opcional)

Para que serve: Organizar tarefas e melhorias identificadas.

Por que é adequada ao tema: Simula a organização de atividades em ambientes ágeis.

Como facilita o aprendizado: Permite visualizar o acompanhamento das ações corretivas.

#### 3. Checklist Inicial

Antes de iniciar a prática, os estudantes devem possuir:

- Papel ou post-its
- Canetas ou marcadores
- Cartolina ou quadro branco
- Computador ou celular (opcional)
- Acesso ao conteúdo da aula
- Equipes organizadas entre 3 e 5 integrantes
- Espaço para discussão em grupo

#### 4. Passo a Passo do Docente (Aula de até 50 minutos)

##### Como conduzir a aula

- Retome o conteúdo da aula anterior sobre gerenciamento da qualidade em projetos Scrum.
- Apresente o conceito de melhoria contínua.
- Explique cada etapa do ciclo PDCA:
- Plan (Planejar)
- Do (Executar)
- Check (Verificar)
- Act (Agir)
- Relacione o PDCA com as cerimônias do Scrum:
- Planejamento da Sprint
- Execução da Sprint
- Sprint Review
- Retrospectiva
- Apresente o cenário da atividade prática.
- Organize os grupos.
- Explique a dinâmica.

##### Preparações necessárias

- Organizar os grupos.
- Separar materiais para a atividade.
- Preparar o cenário do desafio.
- Disponibilizar quadro ou cartolina.

##### Alertas e pontos de atenção

- Os alunos podem focar apenas na solução.
- Reforce a importância da etapa de verificação.
- Incentive justificativas para cada decisão tomada.
- Estimule a participação de todos os integrantes.

##### Dinâmica sugerida

Análise do Problema → Planejamento → Simulação da Solução → Verificação → Ação Corretiva

##### Gerenciamento de Tempo

| Etapa | Tempo |
| --- | --- |
| Revisão dos conceitos | 10 min |
| Explicação da atividade | 5 min |
| Planejamento (Plan) | 10 min |
| Execução e Verificação (Do + Check) | 15 min |
| Ação Corretiva (Act) | 5 min |
| Reflexão final | 5 min |

Total: 50 minutos

#### 5. Atividade Prática — Descrição Geral

Os estudantes deverão atuar como uma equipe responsável por melhorar um sistema de gerenciamento escolar.

O sistema apresenta problemas simulados que afetam sua qualidade.

Cada grupo deverá utilizar o ciclo PDCA para:

- Identificar o problema.
- Planejar uma solução.
- Executar a proposta.
- Verificar os resultados.
- Definir ações corretivas e melhorias.
A atividade simula situações reais encontradas em projetos de desenvolvimento de software e qualidade de processos.

#### 6. Metodologia Ativa Utilizada

###### Aprendizagem Baseada em Problemas (PBL)

Os alunos resolvem um problema real utilizando uma metodologia de qualidade.

###### Aprendizagem Colaborativa

As decisões são tomadas coletivamente.

###### Simulação Profissional

A atividade reproduz situações encontradas em equipes de desenvolvimento.

###### Elementos de Lemov Aplicados

- Objetivo Claro
- Produção Visível
- Participação Ativa
- Discussão Estruturada
- Feedback Imediato

#### 7. Passo a Passo da Atividade Prática (para os alunos)

##### Cenário

Uma escola utiliza um sistema para registrar notas dos alunos.

Foram identificados os seguintes problemas:

- Algumas notas não estão sendo salvas corretamente.
- O sistema demora para carregar relatórios.
- Usuários relatam dificuldades para localizar informações.

##### Etapa 1 – PLAN (Planejar)

- Formem grupos de 3 a 5 integrantes.
- Analisem os problemas apresentados.
- Escolham o problema mais crítico.
- Definam possíveis causas.
- Elaborem um plano de ação para resolver o problema.

##### Etapa 2 – DO (Executar)

- Descrevam quais ações seriam realizadas para solucionar o problema.
Exemplo:

- Revisar regras de cadastro.
- Melhorar consultas do sistema.
- Reorganizar menus.

##### Etapa 3 – CHECK (Verificar)

- Avaliem se a solução proposta realmente resolve o problema.
- Registrem possíveis falhas ainda existentes.

##### Etapa 4 – ACT (Agir)

- Definam melhorias adicionais.
- Registrem ações corretivas para evitar que o problema aconteça novamente.

##### Etapa 5 – Apresentação

- Apresentem para a turma:
- Problema escolhido
- Plano criado
- Resultado esperado
- Melhorias propostas

#### 8. Exemplo ou Demonstração

##### Problema

Relatórios apresentam informações incompletas.

###### PLAN

Identificar quais dados não estão sendo carregados corretamente.

###### DO

Revisar a lógica de geração dos relatórios.

###### CHECK

Verificar se todos os dados aparecem corretamente após a correção.

###### ACT

Criar testes periódicos para validar os relatórios antes das próximas entregas.

#### 9. Resultado Esperado

O estudante deverá apresentar:

- Problema analisado.
- Aplicação completa das quatro etapas do PDCA.
- Plano de ação documentado.
- Propostas de melhoria contínua.
O professor poderá verificar o aprendizado observando:

- Compreensão das etapas do PDCA.
- Capacidade de análise.
- Coerência das soluções propostas.
- Participação dos integrantes.

#### 10. Formato de Entrega da Atividade

###### O que deve ser entregue

Documento, cartolina ou apresentação contendo:

- Problema identificado
- Etapa Plan
- Etapa Do
- Etapa Check
- Etapa Act
- Melhorias propostas

###### Nome do arquivo

- PDCA_Qualidade_Aula51_NomeGrupo

###### Local de entrega

- Sala de aula
- Ambiente virtual utilizado pelo professor

###### Prazo sugerido

Ao final da aula.

#### 11. Encerramento e Reflexão

Conduza a reflexão utilizando as perguntas:

- Qual etapa do PDCA foi mais difícil de executar?
- Por que a fase de verificação é tão importante?
- O que pode acontecer quando uma equipe ignora os resultados encontrados?
- Como o PDCA contribui para a melhoria contínua?
- Qual a relação entre PDCA e as cerimônias do Scrum?
