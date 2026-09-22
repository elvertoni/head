---
titulo: "Garantia de Qualidade no Scrum"
tipo: rco-seed
disciplina: analise-e-metodos-para-sistemas
sigla_rco: AMS
trimestre: 2
ordem_rco: 49
serie: 1
aula_rco: "Aula 49"
slides: 23
tem_atividade: true
tem_pratica: true
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/AMS/2TRI/49-garantia-de-qualidade-no-scrum/49-garantia-de-qualidade-no-scrum.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/AMS/2TRI/49-garantia-de-qualidade-no-scrum/AULA 49_ATIVIDADE_ANÁLISE E MÉTODO PARA SISTEMAS.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/AMS/2TRI/49-garantia-de-qualidade-no-scrum/AULA 49_PRÁTICA_ANÁLISE E MÉTODO PARA SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Garantia de Qualidade no Scrum

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- ANÁLISE E MÉTODO PARA SISTEMAS
- 1ª Série
- Garantia de Qualidade no Scrum
- Aula 49

_1 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- COMPETÊNCIA(S) A SER(EM) DESENVOLVIDA(S) NESTA AULA:
- De acordo com o Plano de Curso de Desenvolvimento de Sistemas:
- HABILIDADE(S) A SER(EM) DESENVOLVIDA(S) NESTA AULA:
- Executar alterações e manutenções em aplicações e rotinas de acordo com as definições estabelecidas.
- Realizar testes funcionais de programas de computador e aplicativos.

_1 imagem(ns) no slide._

### Slide 4

- Nesta aula vamos:
- Compreender como a qualidade é trabalhada de forma mais detalhada no Scrum.
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
- Scrum 360:
- https://cursos.alura.com.br/course/scrum-parte-6/task/109162
- Manifesto ágil e liderança nos projetos:
- https://www.alura.com.br/conteudo/scrum-parte-2

_2 imagem(ns) no slide._

### Slide 6

- Aula anterior
- Aprendemos como é feito o gerenciamento de mudanças com o Agile.

_1 imagem(ns) no slide._

### Slide 7

- Para pensarmos juntos...
- José é um desenvolvedor de software que acabou de ser contratado por uma empresa que utiliza a metodologia Ágil em todos os seus projetos. Durante sua primeira semana, José percebeu que sua equipe estava passando por dificuldades para manter a qualidade do software que estavam desenvolvendo. Eles estavam lidando com bugs frequentes e retornos de teste que estavam atrasando o progresso. Ele percebeu que a equipe estava pulando o processo de Desenvolvimento Orientado a Testes (TDD) e a Integração Contínua, e estavam focando apenas no desenvolvimento de novos recursos, o que estava impactando diretamente a qualidade do produto final.

_1 imagem(ns) no slide._

### Slide 8

- Para pensarmos juntos...
- Como José pode convencer sua equipe sobre a importância de incorporar o Desenvolvimento Orientado a Testes (TDD) e a Integração Contínua no seu processo de desenvolvimento, para melhorar a qualidade do software?
- Conversem e apresentem suas visões

_2 imagem(ns) no slide._

### Slide 9

- Resposta
- José pode abordar a situação durante uma retrospectiva de Sprint, que é um evento no Scrum que se destina a refletir e melhorar. Ele pode explicar como o Desenvolvimento Orientado a Testes (TDD) e a Integração Contínua podem ajudar a prevenir bugs e detectar problemas mais cedo no ciclo de desenvolvimento, economizando tempo e esforço a longo prazo. Além disso, José pode mencionar que a qualidade não é algo que pode ser adicionado posteriormente, mas deve ser incorporada ao produto desde o início, conforme as práticas ágeis prescrevem. O objetivo de José é enfatizar que a qualidade é responsabilidade de todos e não apenas de um 'garantidor da qualidade'.

_1 imagem(ns) no slide._

### Slide 10

- Conceituando
- A qualidade é uma parte essencial do desenvolvimento de software e a metodologia Ágil se destaca ao integrar práticas de garantia da qualidade em todas as etapas do processo de desenvolvimento.

_1 imagem(ns) no slide._

### Slide 11

- Conceituando
- No contexto da metodologia Ágil, o gerenciamento da qualidade não é uma atividade separada que ocorre ao final do ciclo de desenvolvimento, mas sim uma consideração contínua que permeia todo o processo. Isto é, a qualidade é 'incorporada' ao produto desde o início, em vez de ser 'inspecionada' no final.
- https://www.neomind.com.br/wp-content/uploads/2020/01/pratica2.png

_1 imagem(ns) no slide._

### Slide 12

- Conceituando
- Uma maneira pela qual a qualidade é assegurada é por meio de práticas como o Desenvolvimento Orientado por Testes (Test-Driven Development, TDD) e a Integração Contínua. No TDD, os testes são escritos antes do código, o que ajuda a esclarecer os requisitos e orientar o design.
- A Integração Contínua, por outro lado, envolve a verificação regular do código em um repositório comum, permitindo que problemas sejam detectados e corrigidos rapidamente.

_1 imagem(ns) no slide._

### Slide 13

- Conceituando
- As equipes ágeis também se esforçam para manter a qualidade por meio de inspeções regulares e adaptações. Isso é evidenciado nas revisões de Sprint e nas retrospectivas, onde a equipe analisa o trabalho concluído e discute maneiras de melhorar.

_1 imagem(ns) no slide._

### Slide 14

- Resumo
- Finalmente, o gerenciamento de qualidade ágil é colaborativo. A responsabilidade pela qualidade é de todos na equipe, não apenas de um 'garantidor da qualidade'. Isso encoraja a comunicação, a aprendizagem e a melhoria contínua, fundamentais para a manutenção da alta qualidade em um ambiente ágil.

_1 imagem(ns) no slide._

### Slide 15

- Sobre qualidade, vamos conhecer praticando?
- Na plataforma Alura, vamos acessar o seguinte curso:
- Link para o curso: https://cursos.alura.com.br/course/scrum-parte-6
- Ao longo das atividades, você vai encontrar alguns quizzes e eles não estão ali por acaso! Eles são oportunidades rápidas para testar seu entendimento, reforçar o que aprendeu e identificar pontos que ainda podem melhorar.

_3 imagem(ns) no slide._

### Slide 16

- Apresentação
- 5 minutos
- Neste aula vamos conversar um pouco mais sobre o Gerenciamento da Qualidade.
- Link para tarefa: https://cursos.alura.com.br/course/scrum-parte-6/task/22465
- Vamos nos aprofundar mais em alguns dos conceitos que já vimos em aulas passadas.
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 17

- Qualidade no Scrum
- 6 minutos
- Nesta aula abordaremos qualidade no Scrum.
- Link para tarefa: https://cursos.alura.com.br/course/scrum-parte-6/task/22467
- Que é a capacidade do Scrum de atender certos requisitos e das entregas atenderem também os critérios de aceitação.
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 18

- Qualidade no Scrum
- 4 minutos
- O Backlog Priorizado contém os requisitos individuais que definem o escopo do projeto e fornece uma lista de prioridades a serem entregues.
- Link para tarefa: https://cursos.alura.com.br/course/scrum-parte-6/task/22468
- Essa lista deve conter itens, como histórias de usuário, e que eles estejam diretamente ligados aos Critérios de Aceitação.
- Atividade no portal Alura

_4 imagem(ns) no slide._

### Slide 19

- Vamos praticar?
- Prepare-se, porque nessa atividade, você vai sair do modo aprender e entrar direto no modo praticar.
- A atividade prática vai colocar você diante de um desafio real: sensação de ver seu próprio código aparecer online! Acessível, documentado e pronto para o mundo!

_1 imagem(ns) no slide._

### Slide 20

- O que vimos na aula de hoje:
- Aprendemos o gerenciamento de qualidade no processo de metodologia ágil.

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

### Slide 23

_(sem texto)_

## Atividade

_Fonte: AULA 49_ATIVIDADE_ANÁLISE E MÉTODO PARA SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

ANÁLISE E MÉTODO PARA SISTEMAS

1ª SÉRIE

ATIVIDADE AULA 49

Questão 1

No gerenciamento de qualidade em modelos ágeis, qual dos seguintes é uma técnica popular para a verificação da qualidade do código em cada estágio de desenvolvimento?

A. Teste de desempenho

B. Teste de unidade

C. Teste de carga

D. Teste de segurança

Resposta: B. Teste de unidade

Comentário: No gerenciamento de qualidade ágil, os testes de unidade são realizados regularmente para garantir que cada componente do software funcione corretamente. Esses testes são realizados em cada estágio de desenvolvimento, ajudando as equipes a identificar e corrigir problemas mais cedo no processo.

Questão 2

Qual dos seguintes não é uma prática associada ao gerenciamento de qualidade em modelos ágeis?

A. Desenvolvimento Orientado a Testes (TDD)

B. Integração Contínua

C. Code Reviews

D. Codificação sem testes

Resposta: D. Codificação sem testes

Comentário: Em modelos ágeis, a qualidade é uma preocupação constante e é integrada ao processo de desenvolvimento. A codificação sem testes vai contra esse princípio, pois negligencia a verificação da qualidade do código. Práticas como TDD, Integração Contínua e Code Reviews são comuns em ambientes ágeis e visam manter a qualidade do software.

## Prática

_Fonte: AULA 49_PRÁTICA_ANÁLISE E MÉTODO PARA SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

ANÁLISE E MÉTODO PARA SISTEMAS

1ª SÉRIE

ATIVIDADE PRÁTICA AULA 49

#### 1. Objetivo da Aula Prática

Ao final desta aula prática, o estudante deverá:

- Compreender como a qualidade é incorporada ao processo Scrum.
- Desenvolver a habilidade de analisar funcionalidades utilizando critérios de aceitação.
- Entender a importância do Desenvolvimento Orientado por Testes (TDD) e da Integração Contínua.
- Ser capaz de identificar falhas de qualidade em histórias de usuário e propor melhorias.
- Aplicar conceitos de qualidade colaborativa em um ambiente ágil.

#### 2. Ferramentas Recomendadas

###### Post-its ou Cartões de Papel

Para que serve: Registrar histórias de usuário, critérios de aceitação e possíveis falhas.

Por que é adequada ao tema: Permite organizar requisitos e analisar qualidade de forma visual.

Como facilita o aprendizado: Ajuda os estudantes a compreenderem a relação entre requisitos e qualidade.

###### Quadro Branco ou Cartolina

Para que serve: Organizar histórias de usuário e critérios de aceitação.

Por que é adequada ao tema: Facilita a visualização coletiva das análises.

Como facilita o aprendizado: Estimula a discussão colaborativa sobre qualidade.

###### Google Docs

Para que serve: Documentar critérios de aceitação e resultados das análises.

Por que é adequada ao tema: Permite registrar evidências da atividade.

Como facilita o aprendizado: Ajuda a estruturar o pensamento crítico dos estudantes.

###### Trello (Opcional)

Para que serve: Simular um backlog priorizado.

Por que é adequada ao tema: Permite relacionar histórias de usuário aos critérios de aceitação.

Como facilita o aprendizado: Aproxima os estudantes das ferramentas utilizadas no mercado.

#### 3. Checklist Inicial

Antes de iniciar a prática, os estudantes devem possuir:

- Papel ou post-its
- Canetas ou marcadores
- Quadro ou cartolina
- Computador ou celular (opcional)
- Acesso ao conteúdo da aula
- Equipes organizadas entre 3 e 5 integrantes
- Espaço para discussão em grupo

#### 4. Passo a Passo do Docente (Aula de até 50 minutos)

##### Como conduzir a aula

- Retome o tema da aula anterior sobre gerenciamento de mudanças.
- Apresente os conceitos de qualidade no Scrum.
- Explique a importância da qualidade contínua.
- Apresente os conceitos de:
- Critérios de Aceitação
- Desenvolvimento Orientado por Testes (TDD)
- Integração Contínua
- Revisão de Sprint
- Retrospectiva
- Explique que a qualidade é responsabilidade de toda a equipe.
- Apresente a atividade prática.

##### Preparações necessárias

- Separar materiais para os grupos.
- Preparar exemplos de histórias de usuário.
- Organizar os grupos.
- Disponibilizar quadro ou cartolina.

##### Alertas e pontos de atenção

- Os alunos podem confundir teste com qualidade.
- Reforce que qualidade começa nos requisitos.
- Incentive a análise dos critérios de aceitação.
- Estimule a participação de todos os integrantes.

##### Dinâmica sugerida

Análise de Requisitos → Criação dos Critérios de Aceitação → Revisão → Correção → Apresentação

##### Gerenciamento de Tempo

| Etapa | Tempo |
| --- | --- |
| Revisão dos conceitos | 10 min |
| Explicação da atividade | 5 min |
| Análise das histórias | 10 min |
| Criação dos critérios | 15 min |
| Apresentações | 5 min |
| Reflexão final | 5 min |

Total: 50 minutos

#### 5. Atividade Prática — Descrição Geral

Os estudantes deverão atuar como uma equipe Scrum responsável por garantir a qualidade de um sistema.

Cada grupo receberá histórias de usuário simples e deverá:

- Identificar possíveis problemas de qualidade.
- Criar critérios de aceitação.
- Simular testes para verificar se a funcionalidade atende aos requisitos.
- Propor melhorias para aumentar a qualidade do produto.
A atividade simula situações reais enfrentadas por equipes Scrum durante o desenvolvimento de software.

A habilidade desenvolvida será a capacidade de analisar requisitos e garantir a qualidade desde o início do desenvolvimento.

#### 6. Metodologia Ativa Utilizada

###### Aprendizagem Baseada em Problemas (PBL)

Os estudantes resolvem problemas relacionados à qualidade do software.

###### Simulação Profissional

A atividade reproduz práticas comuns em equipes Scrum.

###### Aprendizagem Colaborativa

As decisões são construídas coletivamente.

###### Elementos de Lemov Aplicados

- Objetivo Claro
- Produção Visível
- Participação Ativa
- Discussão Estruturada
- Feedback Imediato

#### 7. Passo a Passo da Atividade Prática (para os alunos)

###### Cenário

Uma equipe está desenvolvendo um aplicativo de controle de tarefas escolares.

###### Etapa 1 – Análise das Histórias

- Formem grupos de 3 a 5 integrantes.
- Analisem as histórias de usuário fornecidas pelo professor.
Exemplo:

Como estudante, quero cadastrar tarefas escolares para que eu possa organizar meus estudos.

###### Etapa 2 – Definição dos Critérios de Aceitação

- Criem pelo menos 3 critérios de aceitação para cada história.
Exemplo:

- O sistema deve permitir cadastrar uma tarefa.
- O sistema deve permitir definir uma data.
- O sistema deve salvar a tarefa corretamente.

###### Etapa 3 – Simulação dos Testes

- Imaginem que a funcionalidade foi desenvolvida.
- Verifiquem se todos os critérios foram atendidos.
- Identifiquem possíveis falhas.

###### Etapa 4 – Proposta de Melhoria

- Registrem melhorias necessárias para aumentar a qualidade da funcionalidade.

###### Etapa 5 – Apresentação

- Apresentem os critérios de aceitação criados.
- Expliquem quais problemas foram encontrados.
- Mostrem as melhorias propostas.

#### 8. Exemplo ou Demonstração

##### História de Usuário

Como aluno, quero cadastrar tarefas escolares para organizar meus estudos.

###### Critérios de Aceitação

| Nº | Critério |
| --- | --- |
| 1 | Permitir cadastrar tarefa |
| 2 | Permitir informar data |
| 3 | Salvar os dados corretamente |

###### Possível Problema

O sistema não salva a data da tarefa.

###### Melhoria Proposta

Adicionar validação e teste automático para o campo de data.

#### 9. Resultado Esperado

O estudante deverá apresentar:

- Histórias analisadas.
- Critérios de aceitação definidos.
- Problemas identificados.
- Sugestões de melhoria.
O professor poderá verificar o aprendizado observando:

- Qualidade dos critérios criados.
- Capacidade de identificar falhas.
- Participação da equipe.
- Clareza das justificativas.

#### 10. Formato de Entrega da Atividade

###### O que deve ser entregue

- Cartolina, quadro ou documento digital contendo:
- História de usuário
- Critérios de aceitação
- Problemas encontrados
- Melhorias propostas

###### Nome do arquivo

- QualidadeScrum_Aula49_NomeGrupo

###### Local de entrega

- Sala de aula
- Plataforma utilizada pelo professor

###### Prazo sugerido

Ao final da aula.

#### 11. Encerramento e Reflexão

Conduza uma discussão utilizando as perguntas:

- É possível garantir qualidade apenas no final do projeto?
- Qual a importância dos critérios de aceitação?
- Como o TDD ajuda a reduzir erros?
- Por que a qualidade é responsabilidade de toda a equipe?
- O que acontece quando funcionalidades são entregues sem testes adequados?
