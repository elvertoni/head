---
titulo: "Metodologias de desenvolvimento de software Modelo de processo clássico"
tipo: rco-seed
disciplina: analise-e-metodos-para-sistemas
sigla_rco: AMS
trimestre: 1
ordem_rco: 11
serie: 1
aula_rco: "Aula 11"
slides: 36
tem_atividade: true
tem_pratica: true
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/AMS/1TRI/11-metodologias-de-desenvolvimento-de-software-modelo-de-processo-classico/11-metodologias-de-desenvolvimento-de-software-modelo-de-processo-classico.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/AMS/1TRI/11-metodologias-de-desenvolvimento-de-software-modelo-de-processo-classico/AULA 11_ATIVIDADE_ANÁLISE E MÉTODO PARA SISTEMAS.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/AMS/1TRI/11-metodologias-de-desenvolvimento-de-software-modelo-de-processo-classico/AULA 11_PRÁTICA_ANÁLISE E MÉTODO PARA SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Metodologias de desenvolvimento de software Modelo de processo clássico

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- ANÁLISE E MÉTODO PARA SISTEMAS
- 1ª Série
- Metodologias de desenvolvimento de software Modelo de processo clássico
- Aula 11

_1 imagem(ns) no slide._

### Slide 2

_(sem texto)_

### Slide 3

- ORGANIZAÇÃO CURRICULAR EPT 2026
- A partir de 2026, para atender as mudanças no Ensino Médio (Lei n.º 14.945/2024) as matrizes da Educação Profissional e Tecnológica (EPT), na oferta INTEGRADA, estarão organizadas da seguinte forma:
- Acesse aqui
- Plano de Curso: TÉCNICO EM DESENVOLVIMENTO DE SISTEMAS _INTEGRADO.docx
- Matriz Curricular: OUTUBRO_Matriz_DesenvolvimentoDeSistemas_Integrado_2026_DiurnoNoturno.docx
- 300h
- 1.800h

|  | 1ª série | 2ª série | 3ª série |
| --- | --- | --- | --- |
| Formação Geral Básica | 600 | 600 | 600 |
| Aprofundamento | 100 | 100 | 100 |
| Itinerário da Formação Técnica e Profissional | 300 | 300 | 300 |

- 900h
- 2.100 horas
- 1.200 horas
- O Aprofundamento traz HABILIDADES dos componentes curriculares da FGB, mas também contabiliza na carga horária da EPT, relacionando essas habilidades às HABILIDADES PROFISSIONAIS do Plano de Curso e do Catálogo Nacional de Cursos Técnicos.
- Desta forma, em algumas aulas, você vai encontrar indicativos da integração direta entre as habilidades dos componentes curriculares da FGB/BNCC e das unidades curriculares da EPT.
- SLIDE DO
- PROFESSOR

_2 imagem(ns) no slide._

### Slide 4

- Esta aula integra conhecimentos da Formação Geral
- Básica, articulando saberes da área de Matemática e suas
- Tecnologias com a área técnica em Desenvolvimento de Sistemas.
- Nesta aula, os estudantes planejam e organizam as etapas do desenvolvimento de um sistema, utilizando tabelas e critérios de comparação (tempo, custo e qualidade) para analisar diferentes modelos de ciclo de vida do software e tomar decisões fundamentadas sobre o método mais adequado a um projeto.
- De acordo com o Currículo para o Ensino Médio do Paraná (Formação Geral Básica, 2022, temos:

| COMPETÊNCIA | HABILIDADES | OBJETIVOS DE APRENDIZAGEM | OBJETOS DO CONHECIMENTO | POSSIBILIDADES DE CONTEÚDOS |
| --- | --- | --- | --- | --- |
| Propor ou participar de ações para investigar problemas relevantes do mundo contemporâneo, utilizando conceitos e procedimentos matemáticos para coletar, organizar, analisar e interpretar dados, de modo a subsidiar a tomada de decisões. | Planejar e executar pesquisa amostral sobre questões relevantes, usando dados coletados diretamente ou em diferentes fontes, e comunicar os resultados por meio de relatório contendo gráficos e interpretação das medidas de tendência central e das medidas de dispersão (amplitude e desvio padrão), utilizando ou não recursos digitais. | Ao final da atividade, espera-se que o estudante seja capaz de: Compreender o papel da pesquisa amostral na resolução de problemas reais Organizar dados quantitativos de forma adequada Calcular medidas de tendência central (média e mediana) Determinar medidas simples de dispersão (amplitude) Representar dados por meio de gráficos | Conteúdos matemáticos mobilizados:  Estatística básica Organização e tratamento de dados Medidas de tendência central (média e mediana) Medidas de dispersão (amplitude) Representação gráfica de dados Interpretação de resultados estatísticos | Conteúdos matemáticos Pesquisa amostral Coleta e análise de dados Estatística descritiva Construção e leitura de gráficos Interpretação quantitativa de resultados Conteúdos contextualizados na EPT Tomada de decisão baseada em dados Priorização de funcionalidades de software Avaliação de necessidades de usuários Uso de dados na engenharia de requisitos Planejamento orientado por evidências |

_1 imagem(ns) no slide._

### Slide 5

- COMPETÊNCIA(S) A SER(EM) DESENVOLVIDA(S) NESTA AULA:
- De acordo com o Plano de Curso de Desenvolvimento de Sistemas:
- HABILIDADE(S) A SER(EM) DESENVOLVIDA(S) NESTA AULA:
- Manter registros para análise e refinamento de resultados.
- MATEMÁTICA (FGB: EM13MAT202) Planejar e executar pesquisa amostral sobre questões relevantes, usando dados coletados diretamente ou em diferentes fontes, e comunicar os resultados por meio de relatório contendo gráficos e interpretação das medidas de tendência central e das medidas de dispersão (amplitude e desvio padrão), utilizando ou não recursos digitais.

_1 imagem(ns) no slide._

### Slide 6

- Nesta aula, vamos:
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store
- Compreender as metodologias de desenvolvimento de software clássico.

_4 imagem(ns) no slide._

### Slide 7

- Este material foi elaborado a partir da análise do plano de curso e reúne os conhecimentos essenciais para o Técnico em Desenvolvimento de Sistemas. As aulas foram organizadas com foco na clareza conceitual, na construção gradual dos conteúdos e na utilização de metodologias ativas que favorecem a compreensão, a participação e o desenvolvimento de habilidades e competências de forma significativa.
- De acordo com a matriz curricular do Curso Técnico em Desenvolvimento de Sistemas, que traz em sua essência componentes estruturados para a realização de aulas práticas, cada unidade curricular deve contemplar, além da abordagem teórica, uma proposta de atividade prática a ser desenvolvida pelo professor. Essa orientação assegura a coerência entre o planejamento didático e o que está estabelecido na matriz, promovendo experiências formativas alinhadas ao perfil profissional previsto.
- O professor tem total autonomia para adaptar o conteúdo conforme o contexto da turma, ajustando exemplos, aprofundamentos e estratégias didáticas para otimizar a aprendizagem e a conexão com a prática profissional.
- Se houver falta de conexão ou indisponibilidade de internet durante a aula, os materiais abaixo podem ser utilizados como apoio para elaborar recursos complementares, garantindo a continuidade da abordagem teórica prevista.
- ATENÇÃO PROFESSOR!
- Dicas para elaborar uma boa entrevista:
- https://cursos.alura.com.br/course/engenharia-requisitos/task/75120
- Documento de requisitos:
- https://cursos.alura.com.br/course/engenharia-requisitos/task/69673

_2 imagem(ns) no slide._

### Slide 8

- Na aula anterior…
- Concluímos o conceito sobre aplicação de levantamento de requisitos e vimos o que um engenheiro de requisitos faz e a demanda inicial.

_1 imagem(ns) no slide._

### Slide 9

- Para pensarmos juntos...
- Quando crianças, em fase de aprendizado, cometemos erros com frequência e o papel dos pais é estar ao lado para fazer as correções, ENSINANDO E ORIENTANDO sobre a forma correta de como tudo funciona, desde o início de nossas vidas. É como se os pais fossem um corretor ortográfico que trabalha o tempo todo.

_1 imagem(ns) no slide._

### Slide 10

- Você se lembra de um erro que cometeu quando criança e seus pais te ajudaram a corrigir?
- Realizem a atividade em duplas e socializem no final!

_2 imagem(ns) no slide._

### Slide 11

- Resposta
- As respostas são pessoais e levarão os estudantes a recordar diferentes momentos de suas vidas. Reserve um tempo para que possam compartilhar e apresentar suas reflexões.

_1 imagem(ns) no slide._

### Slide 12

- Ciclo de desenvolvimento
- O ciclo de vida de desenvolvimento de software é o corretor ortográfico do mundo do desenvolvimento de software, assim como os pais são para as crianças.
- Ele pode sinalizar erros na criação do software antes que eles sejam descobertos em estágios sucessivos e custaria muito mais para consertá-los. Mas é muito mais do que isso: o ciclo de vida de desenvolvimento de software também pode traçar um plano para fazer tudo certo na primeira vez.

_1 imagem(ns) no slide._

### Slide 13

- Ciclo de desenvolvimento
- O processo do ciclo de vida de desenvolvimento de software pode ser clássico, também conhecido como tradicional ou ágil.

_1 imagem(ns) no slide._

### Slide 14

- Compreendendo as metodologias de desenvolvimento de software clássicas
- Vídeo 1:https://drive.google.com/file/d/1bW-AeflczJrNfBAEkWSP-oudQhNjT0wX/view?usp=drive_link

_2 imagem(ns) no slide._

### Slide 15

- Para responder
- As metodologias se comportam de que maneira?

_1 imagem(ns) no slide._

### Slide 16

- Respostas
- As metodologias se comportam de maneira sequencial (fases seguem determinada ordem) e/ou incremental (divisão de escopo) e/ou interativa (retroalimentação de fases) e/ou evolutiva (software é aprimorado).

_1 imagem(ns) no slide._

### Slide 17

- Processo de desenvolvimento de software

_1 imagem(ns) no slide._

### Slide 18

- Metodologias
- Todo projeto desenvolvido de acordo com as metodologias de desenvolvimento clássico de software é realizado mediante algum método de análise de sistemas, projeto e implementação. O número de fases varia de organização para organização.

_1 imagem(ns) no slide._

### Slide 19

- Quais são as principais fases das metodologias de desenvolvimento clássico de software?
- As fases pertencentes às metodologias de desenvolvimento clássico de software contemplam um conjunto sequencial de ações de desenvolvimento que vão desde o diagnóstico do problema até os testes que são necessários para a implementação.

_1 imagem(ns) no slide._

### Slide 20

- Levantamento
- Esta primeira fase é uma visão geral, com as diretrizes do projeto/software.
- Todas as partes interessadas, incluindo clientes, vendedores, especialistas, programadores, analistas de negócios e gerentes de projeto devem se reunir para levantar as informações necessárias sobre o que será construído.
- https://www.criandobits.com.br/wp-content/uploads/2022/01/l-requisitos.jpg

_1 imagem(ns) no slide._

### Slide 21

- Análise
- As partes interessadas devem saber exatamente sobre todo o contexto econômico, técnico, jurídico e de cronograma deste projeto. Nesta fase, são consideradas informações, como a descrição do produto ou serviço, demonstrativos contábeis, detalhes de operação e gerenciamento, pesquisa de marketing e políticas, dados financeiros e obrigações fiscais, requerimentos legais, plano de implementação do projeto, tempo e orçamento.

_1 imagem(ns) no slide._

### Slide 22

- Projeto
- A equipe irá produzir a Especificação do Documento de Projeto com base nos requisitos do usuário e na análise. Essa fase define a arquitetura geral do sistema, descrevendo todas as informações para os desenvolvedores começarem a trabalhar no produto, como recursos, entrada, saída, bancos de dados, formulários, esquemas de codificação, especificações de processamento e tempo esperado para entregar o produto.

_1 imagem(ns) no slide._

### Slide 23

- Codificação
- O desenvolvimento real começa e o produto é construído. Os desenvolvedores devem seguir as diretrizes de codificação definidas por sua organização e ferramentas de programação como compiladores, interpretadores, depuradores.

_1 imagem(ns) no slide._

### Slide 24

- Testes
- A função principal do teste de software é detectar bugs. Os testadores de controle de qualidade (QA) são responsáveis por encontrar e relatar bugs e erros aos desenvolvedores e à equipe de revisão do produto.
- https://fireworkweb.com.br/wp-content/uploads/2021/06/Teste-de-software-1920x1306.png

_1 imagem(ns) no slide._

### Slide 25

- Manutenção
- Envolve correção de bugs, atualização do aplicativo para novas versões do software e aprimoramento, incrementando algumas novas especificações. Após testado e pronto para implantação, o produto é lançado formalmente no mercado apropriado.

_1 imagem(ns) no slide._

### Slide 26

- Fases
- Cada fase serve para orientar e dar flexibilidade para adaptar e executar o projeto de acordo com o objetivo do cliente.
- Por isso, as fases apontam tarefas-chave de cronograma e entrega, para garantir a qualidade do software e o cumprimento do prazo.

_1 imagem(ns) no slide._

### Slide 27

- Fases
- Levantamento
- Análise
- Projeto
- Codificação
- Testes
- Manutenção

_1 imagem(ns) no slide._

### Slide 28

- Vamos para mais um caso?
- Uma empresa de software precisa decidir quais funcionalidades devem ser priorizadas na primeira versão de um sistema.
- Para isso, a equipe realizou uma pesquisa com usuários potenciais, pedindo que avaliassem a importância da funcionalidade “Notificações em tempo real” em uma escala de 0 a 10.
- Pontuações obtidas:
- 8, 7, 9, 6, 8, 10, 7, 8, 9, 6
- 👉 Como a equipe pode analisar esses dados para decidir se essa funcionalidade deve ser priorizada no sistema?
- Responda em seu caderno!

_2 imagem(ns) no slide._

### Slide 29

- Resposta:
- Dados ordenados:
- 6, 6, 7, 7, 8, 8, 8, 9, 9, 10
- Média ≈ 7,8
- Mediana = 8
- Amplitude = 4
- Interpretação:
- A maioria das avaliações está concentrada entre 7 e 9, indicando que os usuários consideram a funcionalidade importante. A variação entre as respostas é moderada, mas não compromete a tendência geral.
- Assim, a funcionalidade pode ser considerada prioritária para o sistema.

_1 imagem(ns) no slide._

### Slide 30

- Para responder no seu caderno!
- Com base na pesquisa realizada, qual alternativa melhor descreve a importância da funcionalidade “Notificações em tempo real” para os usuários?
- A) A funcionalidade tem baixa importância, pois existem valores abaixo de 7.
- B) A maioria dos usuários considera a funcionalidade importante, pois os valores estão concentrados em notas altas.
- C) Não é possível tirar conclusões sem uma nova pesquisa.
- D) A amplitude indica que os usuários discordam totalmente sobre a importância.
- Responda em seu caderno!

_3 imagem(ns) no slide._

### Slide 31

- Veja se você acertou…
- Alternativa correta: B
- Os dados mostram concentração de notas altas, com média próxima de 8 e mediana igual a 8, indicando que a maioria dos usuários considera a funcionalidade importante.
- Embora existam algumas avaliações menores, elas não alteram a tendência geral observada na pesquisa.

_2 imagem(ns) no slide._

### Slide 32

- Vamos praticar?
- Prepare-se, porque nessa atividade, você vai sair do modo aprender e entrar direto no modo praticar.
- A atividade prática vai colocar você diante de um desafio real: sensação de ver seu próprio código aparecer online! Acessível, documentado e pronto para o mundo!

_1 imagem(ns) no slide._

### Slide 33

- O que vimos na aula de hoje:
- Aprendemos que os projetos desenvolvidos com as metodologias de desenvolvimento clássico de software são executados mediante algum método de análise de sistemas, projeto e implementação.
- Aprendemos que as fases compreendem: levantamento, análise, projeto, codificação, testes e manutenção.

_1 imagem(ns) no slide._

### Slide 34

- Pronto para desbloquear sua carreira de TI?
- Está perdido estudando mas não sabe por onde começar? Se a resposta é sim, você está no lugar certo! Descubra as estratégias e ferramentas essenciais para te ajudar a desbloquear seu potencial em TI e buscar sua primeira vaga de emprego no setor!
- Este e-book é um guia completo para quem busca começar pelos melhores caminhos para se tornar um excelente profissional de TI, ensinando a identificar perfis profissionais, aplicar técnicas de estudo eficazes, transformar teoria em prática, e aumentar a visibilidade de seu trabalho no mercado de trabalho. Ideal para novatos e profissionais em transição.
- E o melhor, ele pode ser seu, inteiramente grátis!
- Basta clicar AQUI e realizar o seu cadastro com o seu @escola!

_3 imagem(ns) no slide._

### Slide 35

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

### Slide 36

_(sem texto)_

## Atividade

_Fonte: AULA 11_ATIVIDADE_ANÁLISE E MÉTODO PARA SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

ANÁLISE E MÉTODO PARA SISTEMAS

1ª SÉRIE

ATIVIDADE AULA 11

Questão 1

Muitas empresas de desenvolvimento de sistemas buscam frequentemente se atualizar e se aperfeiçoar para atender melhor a um mercado de constantes mudanças e exigências. Frente a essa realidade, podemos afirmar que as corporações buscam:

a) Desenvolver cada vez mais sistemas de baixa qualidade.

b) Poucos Clientes para não gerar despesas

c) excelentes ferramentas de trabalho e desenvolver produtos de qualidade.

d) Desenvolvedores inexperientes considerando baixo investimento.

Resposta comentada

As corporações estão sempre em busca de atualizar suas metodologias de desenvolvimento, para se adequar às constantes mudanças e exigências do mercado, buscando atingir cada vez mais qualidade. Sendo assim, é importante considerar que as corporações buscam sistemas de qualidade, cada vez mais clientes e desenvolvedores com experiência em desenvolvimento.

Questão 2

As metodologias de desenvolvimento de software são muito importantes e são usadas principalmente para vários projetos de desenvolvimento de software. Além disso, todas essas metodologias populares de desenvolvimento de software funcionam bem em certos projetos, dependendo da natureza dele. Elas se comportam de maneira sequencial e/ou incremental e/ou iterativa e/ou evolutiva. O que contempla características do comportamento sequencial?

a) Fases seguem determinada ordem.

b) Fases não segue ordem nenhuma.

c) Fases seguem ordem mista, ora sequencial, ora interativa.

d) Fases que segue um modelo entregue por partes.

Resposta comentada

As atividades são realizadas em sequência, não existem retornos entre as atividades e toda a documentação é produzida após o término do projeto. O modelo entregue por partes é encontrado na fase incremental.

## Prática

_Fonte: AULA 11_PRÁTICA_ANÁLISE E MÉTODO PARA SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

ANÁLISE E MÉTODO PARA SISTEMAS

1ª SÉRIE

ATIVIDADE PRÁTICA AULA 11

##### 1. Objetivo da Aula Prática

Ao final desta aula prática, o estudante deverá:

- Aprender como funciona o ciclo de vida clássico de desenvolvimento de software.
- Desenvolver a habilidade prática de identificar e aplicar as fases sequenciais do processo clássico.
- Ser capaz de produzir um modelo organizado das fases de desenvolvimento de um sistema, desde o levantamento até a manutenção.

##### 2. Ferramentas Recomendadas

Caderno ou Folha A4

- Para que serve: Planejamento inicial e organização das fases do processo.
- Por que é adequada ao tema: O material enfatiza compreensão conceitual e estrutura sequencial.
- Como facilita o aprendizado: Permite esboçar fluxos e organizar ideias antes da formalização.
Google Docs (https://docs.google.com)

- Para que serve: Registro estruturado das fases do desenvolvimento.
- Por que é adequada ao tema: Facilita a documentação clara e sequencial do processo.
- Como facilita o aprendizado: Permite edição e revisão rápida.
Google Slides (https://slides.google.com)

- Para que serve: Representação visual do ciclo de desenvolvimento.
- Por que é adequada ao tema: O processo clássico é mais fácil de compreender visualmente.
- Como facilita o aprendizado: Ajuda a visualizar as etapas e suas relações.
(Ferramentas gratuitas, online ou de uso livre.)

##### 3. Checklist Inicial

Antes de iniciar a prática, o estudante deve ter:

- Caderno ou folhas para anotações
- Caneta ou lápis
- Computador ou notebook
- Conexão com a internet
- Acesso ao material da aula (PDF ou slides)
- Ambiente: sala de aula ou laboratório de informática

##### 4. Passo a Passo do Docente (Aula de até 50 minutos)

###### Como conduzir a aula

- Retome brevemente as aulas anteriores sobre requisitos.
- Apresente o conceito de ciclo de vida de desenvolvimento de software como um “corretor de erros antecipado”.
- Explique que os modelos clássicos seguem fases bem definidas e sequenciais.
- Destaque as principais fases apresentadas no material:
- Levantamento
- Análise
- Projeto
- Codificação
- Testes
- Manutenção
- Apresente a atividade prática.

###### Preparações necessárias

- Garantir que os alunos compreendam cada fase antes da prática
- Preparar um exemplo simples de sistema (ex.: aplicativo escolar)
- Disponibilizar quadro ou projetor para síntese coletiva

###### Alertas e pontos de atenção

- Alunos podem confundir ordem das fases
- Reforce que no modelo clássico as etapas são sequenciais
- Oriente para não misturar fases técnicas com fases de negócio

###### Dinâmica sugerida

- Revisão conceitual → prática guiada → apresentação → feedback

###### Gerenciamento de tempo (50 minutos)

- Contextualização e explicação: 15 minutos
- Orientação da atividade: 5 minutos
- Execução da prática: 20 minutos
- Socialização e fechamento: 10 minutos

##### 5. Atividade Prática — Descrição Geral

O estudante deverá aplicar o modelo de processo clássico a um sistema fictício, organizando todas as fases do ciclo de desenvolvimento.

Sugestão de cenário: desenvolvimento de um sistema simples (ex.: sistema de biblioteca escolar, agenda digital ou controle de tarefas).

A atividade simula a estrutura real de um projeto tradicional de software, permitindo compreender como cada fase contribui para a qualidade final.

A habilidade desenvolvida será a capacidade de planejar o desenvolvimento de software de forma estruturada e sequencial.

##### 6. Metodologia Ativa Utilizada

- Aprendizagem baseada em problemas (PBL)
- Ensino por descoberta
- Aprendizagem colaborativa
Elementos de Lemov aplicados:

- Objetivo claro
- Participação ativa
- Produção visível
- Estruturação do pensamento

##### 7. Passo a Passo da Atividade Prática (para os alunos)

- Leia o cenário apresentado pelo professor.
- Defina qual sistema será desenvolvido.
- Descreva a fase de levantamento, identificando informações necessárias.
- Descreva a fase de análise, considerando contexto e viabilidade.
- Planeje a fase de projeto, definindo arquitetura e funcionamento.
- Descreva a fase de codificação, indicando desenvolvimento do sistema.
- Defina a fase de testes, considerando verificação de erros.
- Descreva a fase de manutenção, prevendo atualizações e melhorias.
- Organize todas as fases na ordem correta.

##### 8. Exemplo ou Demonstração

Exemplo simplificado — Sistema de Biblioteca Escolar

- Levantamento: identificar necessidades de alunos e professores
- Análise: verificar viabilidade técnica e financeira
- Projeto: definir telas, banco de dados e funcionalidades
- Codificação: desenvolvimento do sistema
- Testes: verificar erros e falhas
- Manutenção: correções e melhorias após implantação

##### 9. Resultado Esperado

O estudante deverá apresentar:

- Descrição clara de cada fase do ciclo clássico
- Ordem correta das etapas
- Coerência entre as fases e o sistema escolhido
O professor poderá verificar o aprendizado observando:

- Compreensão do processo sequencial
- Clareza das descrições
- Aplicação correta dos conceitos

##### 10. Formato de Entrega da Atividade

- Formato: Registro no caderno, folha ou arquivo digital
- Nome do arquivo (se digital): Processo_Classico_NomeAluno
- Local de entrega: Avaliação em sala ou envio via Google Classroom/Drive
- Prazo sugerido: Durante a aula

##### 11. Encerramento e Reflexão

Finalize a aula conduzindo uma reflexão orientada:

- Por que seguir fases estruturadas ajuda no sucesso do projeto?
- O que pode acontecer se uma etapa for ignorada?
- Em quais situações o modelo clássico pode ser mais adequado?
