---
titulo: "Ciclo de vida de software"
tipo: rco-seed
disciplina: analise-e-metodos-para-sistemas
sigla_rco: AMS
trimestre: 1
ordem_rco: 3
serie: 1
aula_rco: "Aula 03"
slides: 26
tem_atividade: true
tem_pratica: true
fontes:
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/AMS/1TRI/3-ciclo-de-vida-de-software/3-ciclo-de-vida-de-software.pptx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/AMS/1TRI/3-ciclo-de-vida-de-software/AULA 03_PRÁTICA_ANÁLISE E MÉTODO PARA SISTEMAS.docx"
  - "lake/AULAS_RCO-20260922T223029Z-1-002/AULAS_RCO/AMS/1TRI/3-ciclo-de-vida-de-software/AULA 3_ATIVIDADE_ANÁLISE E MÉTODO PARA SISTEMAS.docx"
extrator: tools/extrair_rco.py
status: bruto
---

# Ciclo de vida de software

> Conteúdo BRUTO extraído do RCO (SEED-PR) por `tools/extrair_rco.py`. Insumo para curadoria pela skill prof-toni; não editar à mão, reextrair.

## Slides

### Slide 1 — Curso Técnico Profissional DESENVOLVIMENTO DE SISTEMAS

- ANÁLISE E MÉTODO PARA SISTEMAS
- 1ª Série
- Ciclo de vida de software
- Aula 03

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
| Propor ou participar de ações para investigar desafios do mundo contemporâneo e tomar decisões éticas e socialmente responsáveis, com base na análise de problemas sociais, como os voltados a situações de saúde, sustentabilidade, das implicações da tecnologia no mundo do trabalho, entre outros, mobilizando e articulando conceitos, procedimentos e linguagens próprios da Matemática. | (EM13MAT203) Planejar e executar ações envolvendo a criação e a utilização de aplicativos, jogos (digitais ou não), planilhas para o controle de orçamento familiar, simuladores de cálculos de juros compostos, dentre outros, para aplicar conceitos matemáticos e tomar decisões. | Utilizar diversas estratégias para o cálculo de porcentagens nas situações do dia a dia. Analisar e avaliar situações comerciais em que são empregados descontos ou acréscimos para tomada de decisões financeiras. Compreender, aplicar e calcular juros simples e juros compostos nas situações de cálculo em situações de empréstimos, financiamentos, investimentos e multas progressivas. | Matemática Financeira. | Porcentagem. Aumentos e Descontos. Lucro e Prejuízo. |

_1 imagem(ns) no slide._

### Slide 5

- COMPETÊNCIA(S) A SER(EM) DESENVOLVIDA(S) NESTA AULA:
- De acordo com o Plano de Curso de Desenvolvimento de Sistemas:
- HABILIDADE(S) A SER(EM) DESENVOLVIDA(S) NESTA AULA:
- Dimensionar requisitos e funcionalidades do sistema.
- LINGUAGENS (FGB: EM13LGG104) Utilizar as diferentes linguagens, levando em conta seus funcionamentos, para a compreensão e produção de textos e discursos em diversos campos de atuação social.

_1 imagem(ns) no slide._

### Slide 6

- Nesta aula, vamos:
- Para um melhor aproveitamento de conteúdo você pode baixar o aplicativo da Alura para seu celular e acompanhar os materiais, clique nos respectivos links:
- Google Play
- App Store
- Entender o ciclo de vida do software.

_5 imagem(ns) no slide._

### Slide 7

- Este material foi elaborado a partir da análise do plano de curso e reúne os conhecimentos essenciais para o Técnico em Desenvolvimento de Sistemas. As aulas foram organizadas com foco na clareza conceitual, na construção gradual dos conteúdos e na utilização de metodologias ativas que favorecem a compreensão, a participação e o desenvolvimento de habilidades e competências de forma significativa.
- De acordo com a matriz curricular do Curso Técnico em Desenvolvimento de Sistemas, que traz em sua essência componentes estruturados para a realização de aulas práticas, cada unidade curricular deve contemplar, além da abordagem teórica, uma proposta de atividade prática a ser desenvolvida pelo professor. Essa orientação assegura a coerência entre o planejamento didático e o que está estabelecido na matriz, promovendo experiências formativas alinhadas ao perfil profissional previsto.
- O professor tem total autonomia para adaptar o conteúdo conforme o contexto da turma, ajustando exemplos, aprofundamentos e estratégias didáticas para otimizar a aprendizagem e a conexão com a prática profissional.
- Se houver falta de conexão ou indisponibilidade de internet durante a aula, os materiais abaixo podem ser utilizados como apoio para elaborar recursos complementares, garantindo a continuidade da abordagem teórica prevista.
- ATENÇÃO PROFESSOR!

_1 imagem(ns) no slide._

### Slide 8

- Na aula anterior…
- Conhecemos e compreendemos os processos de Engenharia de Software

_1 imagem(ns) no slide._

### Slide 9

- Para pensarmos juntos...
- Quando nos referimos a um plano estruturado que orienta o desenvolvimento, a manutenção e a substituição de um software específico, estamos falando de uma metodologia.
- Mas afinal, de qual metodologia se trata?
- Você saberia identificar?
- Realizem a atividade em duplas e socializem no final!

_2 imagem(ns) no slide._

### Slide 10

- Você consegue identificar qual método poderia ser utilizado para o desenvolvimento de um software?

_1 imagem(ns) no slide._

### Slide 11

- Ciclo de vida de desenvolvimento de software
- Ciclo de vida do software é o termo utilizado para definir o conjunto de etapas que ocorrem entre a concepção de um sistema e o instante em que ele é descontinuado pelo desenvolvedor. Ele ajuda a orientar a equipe de desenvolvedores, assim como o direcionamento de recursos.
- Desse modo, os times podem sempre focar no que for mais importante, evitando problemas e garantindo o máximo de satisfação do usuário

_1 imagem(ns) no slide._

### Slide 12

- Gestão do ciclo de vida
- A gestão do ciclo de vida do sistema é importante por permitir ao negócio ter um planejamento inteligente e capaz de identificar quando é a melhor hora de executar cada tarefa que envolve a criação e a manutenção de um sistema.
- Ou seja, torna o processo de gestão do aplicativo mais robusto e organizado. Assim, o time pode ter maior controle sobre a aplicação e evitar cenários de risco.

_1 imagem(ns) no slide._

### Slide 13

- Ciclo de vida de desenvolvimento de software
- Link:https://drive.google.com/file/d/1FhUXtZ4H4rWLRGEafdF0htnZQtjctXmt/view?usp=share_link
- OBS: link do vídeo deve ser atualizado caso a apresentação mude de pasta junto com os vídeos

_3 imagem(ns) no slide._

> **Notas do apresentador:** Link do vídeo: https://drive.google.com/file/d/1FhUXtZ4H4rWLRGEafdF0htnZQtjctXmt/view?usp=share_link

### Slide 14

- Modelos de ciclo de vida de software
- Conforme o mercado de desenvolvimento de sistemas evoluiu, diferentes modelos de ciclo de desenvolvimento foram criados. Cada um busca atender a diferentes necessidades, o que exige do gestor um cuidado maior na hora de escolher o seu.
- Confira, a seguir, os principais modos de manter uma aplicação funcional!

_2 imagem(ns) no slide._

### Slide 15

- Modelos de ciclo de vida de software
- Cascata
- Incremental
- Modelo Evolutivo
- Modelo V
- Prototipagem
- Modelo Espiral
- Modelo de ciclo de vida
- associado ao RUP

_1 imagem(ns) no slide._

### Slide 16

- Modelos de ciclos de vida de software
- Link: https://drive.google.com/file/d/1WhKkJppwYyd_DMwtpPhX4M06AmYGtAMu/view?usp=share_link
- OBS: link do vídeo deve ser atualizado caso a apresentação mude de pasta junto com os vídeos

_3 imagem(ns) no slide._

### Slide 17

- Vamos para mais um caso?
- Khyonara é a proprietária de uma empresa de desenvolvimento de software. Ela deseja produzir um site de compras com a mais alta qualidade, menor custo e menor tempo possível, usando um fluxo de fases bem estruturado.
- Vocês sabem como funciona o Ciclo de Vida
- do Desenvolvimento de Software?
- Represente esse processo por meio de um esquema
- no caderno, respondendo a essa questão.
- Responda em seu caderno!

_4 imagem(ns) no slide._

### Slide 18

- Resposta:
- Reduzindo o custo de desenvolvimento de software e, ao mesmo tempo, melhorando a qualidade e encurtando o tempo de produção.
- MELHORAR A QUALIDADE , ENCURTANDO O TEMPO DE PRODUÇÃO
- REDUÇÃO DE CUSTO

_1 imagem(ns) no slide._

### Slide 19

- Para responder no seu caderno!
- O Ciclo de Vida de Desenvolvimento de Software tem como objetivo produzir um software de alta qualidade, capaz de atender ou superar as expectativas do cliente, alcançando a conclusão dentro do prazo e das estimativas de custo. Qual alternativa abaixo não é verdadeira quando tratamos de Ciclo de Vida?
- (A) É também chamado Processo de Desenvolvimento de Software.
- (B) É uma estrutura que define tarefas executadas em cada etapa do processo de desenvolvimento de software.
- (C) Não é um processo seguido por um projeto de software dentro de uma organização de software.
- (D) SDLC é a sigla de Software Development Life Cycle.
- Responda em seu caderno!

_3 imagem(ns) no slide._

### Slide 20

- Veja se você acertou…
- O Ciclo de Vida de Desenvolvimento de Software tem como objetivo produzir um software de alta qualidade, capaz de atender ou superar as expectativas do cliente, alcançando a conclusão dentro do prazo e das estimativas de custo. Qual alternativa abaixo não é verdadeira quando tratamos de Ciclo de Vida?
- (A) É também chamado Processo de Desenvolvimento de Software.
- (B) É uma estrutura que define tarefas executadas em cada etapa do processo de desenvolvimento de software.
- (C) Não é um processo seguido por um projeto de software dentro de uma organização de software.
- (D) SDLC é a sigla de Software Development Life Cycle.

_2 imagem(ns) no slide._

### Slide 21

- Explicação:
- A ISO/IEC 12207 é um padrão internacional que estabelece os processos do ciclo de vida do software.
- Seu objetivo é definir, de forma sistematizada, as atividades e tarefas necessárias para o desenvolvimento, a manutenção e a evolução de sistemas de software.

_1 imagem(ns) no slide._

### Slide 22

- Vamos praticar?
- Prepare-se, porque nessa atividade, você vai sair do modo aprender e entrar direto no modo praticar.
- A atividade prática vai colocar você diante de um desafio real: sensação de ver seu próprio código aparecer online! Acessível, documentado e pronto para o mundo!

_1 imagem(ns) no slide._

### Slide 23

- O que vimos na aula de hoje:
- Aprendemos sobre o ciclo de vida do desenvolvimento de software, além de entender que o ciclo faz uso de modelos para facilitar a organização das etapas e processos.

_1 imagem(ns) no slide._

### Slide 24

- Pronto para desbloquear sua carreira de TI?
- Está perdido estudando mas não sabe por onde começar? Se a resposta é sim, você está no lugar certo! Descubra as estratégias e ferramentas essenciais para te ajudar a desbloquear seu potencial em TI e buscar sua primeira vaga de emprego no setor!
- Este e-book é um guia completo para quem busca começar pelos melhores caminhos para se tornar um excelente profissional de TI, ensinando a identificar perfis profissionais, aplicar técnicas de estudo eficazes, transformar teoria em prática, e aumentar a visibilidade de seu trabalho no mercado de trabalho. Ideal para novatos e profissionais em transição.
- E o melhor, ele pode ser seu, inteiramente grátis!
- Basta clicar AQUI e realizar o seu cadastro com o seu @escola!

_3 imagem(ns) no slide._

### Slide 25

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

### Slide 26

_(sem texto)_

## Atividade

_Fonte: AULA 3_ATIVIDADE_ANÁLISE E MÉTODO PARA SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

ANÁLISE E MÉTODO PARA SISTEMAS

1ª SÉRIE

ATIVIDADE AULA 03

Questão 1

O ciclo de vida define uma metodologia para aprimorar a qualidade do software e o processo de desenvolvimento. A seguir, assinale a alternativa que contém a definição de um dos estágios típicos do Ciclo de Vida de desenvolvimento de sistemas:

a) Não documentar claramente os requisitos do produto.

b) A análise de requisitos é o estágio mais importante e fundamental no Ciclo de Vida de desenvolvimento de sistemas.

c) Fornece uma estrutura padronizada que define atividades e produtos.

d) Facilita o rastreamento e controle do projeto.

Resposta comentada: O planejamento dos requisitos de garantia de qualidade e a identificação dos riscos associados ao projeto também são feitos na fase de planejamento.

Questão 2

O conceito inicial e a criação do Ciclo de Vida de Desenvolvimento de Software tratavam apenas das atividades de segurança como uma tarefa separada e única, realizada como parte da fase de teste. As deficiências dessa abordagem foram: o número inevitavelmente alto de vulnerabilidades e os bugs descobertos tarde demais no processo, ou em certos casos, nem mesmo descobertos.

Sobre as vantagens de implementar o Ciclo de Vida de Desenvolvimento de Software, a seguir, assinale a alternativa incorreta:

a) Ajuda no planejamento, estimativa e programação do projeto.

b) Aumenta a visibilidade em todos os aspectos do ciclo de vida para todas as partes interessadas envolvidas no processo de desenvolvimento.

c) Aumenta a velocidade de desenvolvimento.

d) Aumenta os riscos do projeto.

Resposta comentada: O Ciclo de Vida do Desenvolvimento de Software oferece às organizações uma abordagem sistemática, ou seja, um passo a passo para desenvolver softwares de sucesso, a partir da reunião dos requisitos iniciais de um novo produto, diminuindo assim os riscos do projeto.

## Prática

_Fonte: AULA 03_PRÁTICA_ANÁLISE E MÉTODO PARA SISTEMAS.docx_

Curso Técnico Profissional em DESENVOLVIMENTO DE SISTEMAS

ANÁLISE E MÉTODO PARA SISTEMAS

1ª SÉRIE

ATIVIDADE PRÁTICA AULA 03

##### 1. Objetivo da Aula Prática

Ao final desta aula prática, o estudante deverá:

- Aprender o que é o ciclo de vida do desenvolvimento de software (SDLC) e seus principais modelos.
- Desenvolver a habilidade prática de planejar e organizar etapas de desenvolvimento de um sistema.
- Ser capaz de executar a representação esquemática de um ciclo de vida de software adequado a um cenário proposto, justificando sua escolha com base em critérios como tempo, custo e qualidade.

##### 2. Ferramentas Recomendadas

Caderno ou Folha A4 (uso manual)

- Para que serve: Registro e organização de esquemas e fluxos de etapas.
- Por que é adequada ao tema: O material da aula orienta explicitamente a representação manual do ciclo de vida.
- Como facilita o aprendizado: Estimula o raciocínio sequencial e a organização lógica das etapas.
Google Docs ou Google Desenhos (https://docs.google.com / https://drawings.google.com)

- Para que serve: Criação de esquemas digitais e tabelas comparativas.
- Por que é adequada ao tema: Permite organizar visualmente as etapas do SDLC.
- Como facilita o aprendizado: Facilita ajustes, revisões e compartilhamento do trabalho.
Planilhas Google (https://sheets.google.com)

- Para que serve: Comparação de modelos de ciclo de vida por critérios (tempo, custo, qualidade).
- Por que é adequada ao tema: Relaciona-se diretamente à proposta interdisciplinar com Matemática.
- Como facilita o aprendizado: Ajuda na análise e tomada de decisão fundamentada.

##### 3. Checklist Inicial

Antes de iniciar a prática, o estudante deve ter:

- Caderno ou folhas para rascunho
- Caneta ou lápis
- Computador ou notebook (opcional, se atividade digital)
- Conexão com a internet (se utilizar ferramentas online)
- Acesso ao material da aula (slides ou PDF)
- Ambiente: sala de aula ou laboratório de informática

##### 4. Passo a Passo do Docente (Aula de até 50 minutos)

###### Como conduzir a aula

- Retome rapidamente os processos de Engenharia de Software vistos na aula anterior.
- Apresente o conceito de ciclo de vida do software, conforme definição do material.
- Explique a importância da gestão do ciclo de vida para tempo, custo e qualidade.
- Apresente os principais modelos de ciclo de vida:
- Cascata
- Incremental
- Evolutivo
- Modelo V
- Prototipagem
- Espiral
- RUP
- Introduza o estudo de caso proposto (Khyonara) e explique a atividade prática.

###### Preparações necessárias

- Ter exemplos visuais de ciclos de vida (SDLC)
- Definir se a atividade será individual ou em duplas
- Preparar quadro ou slide para síntese final

###### Alertas e pontos de atenção

- Alunos podem confundir modelo com etapa
- Reforce que não existe um modelo único, e sim o mais adequado ao contexto
- Oriente para justificar escolhas, não apenas desenhar

###### Dinâmica sugerida

- Explanação → análise de caso → prática orientada → socialização

###### Gerenciamento de tempo (50 minutos)

- Retomada e explicação conceitual: 15 minutos
- Análise do caso e orientações: 10 minutos
- Execução da atividade prática: 15 minutos
- Discussão e fechamento: 10 minutos

##### 5. Atividade Prática — Descrição Geral

O estudante deverá representar o ciclo de vida de desenvolvimento de um software, considerando o seguinte cenário:

Uma empresa deseja desenvolver um site de compras, com alta qualidade, menor custo e menor tempo, utilizando um fluxo de fases bem estruturado.

A atividade simula uma situação real de tomada de decisão em projetos de software.

A habilidade desenvolvida será a capacidade de planejar e justificar etapas de desenvolvimento de sistemas.

##### 6. Metodologia Ativa Utilizada

- Aprendizagem baseada em problemas (PBL)
- Ensino por descoberta
- Experimentação prática
- Colaboração (atividade em duplas, quando aplicado)
Elementos de Lemov aplicados:

- Objetivo claro
- Pensamento estruturado
- Produção visível
- Explicitação do raciocínio

##### 7. Passo a Passo da Atividade Prática (para os alunos)

- Leia atentamente o cenário apresentado pelo professor.
- Identifique o objetivo do projeto (qualidade, custo e tempo).
- Escolha um modelo de ciclo de vida de software que melhor atenda ao cenário.
- Represente o ciclo de vida por meio de um esquema (desenho, fluxograma ou diagrama).
- Indique claramente as etapas do ciclo.
- Explique, em poucas palavras, por que esse modelo foi escolhido.
- Revise o esquema antes da entrega.

##### 8. Exemplo ou Demonstração

Estrutura básica esperada do esquema:

- Levantamento de requisitos
- Projeto do sistema
- Implementação
- Testes
- Implantação
- Manutenção / Evolução
(O professor pode demonstrar um exemplo simples no quadro antes da atividade.)

##### 9. Resultado Esperado

O estudante deverá apresentar:

- Um esquema organizado do ciclo de vida do software
- Etapas bem definidas e em sequência lógica
- Coerência entre o modelo escolhido e o cenário proposto
O professor poderá verificar o aprendizado observando:

- Clareza do esquema
- Correta identificação das etapas
- Justificativa adequada da escolha do modelo

##### 10. Formato de Entrega da Atividade

- Formato: Esquema no caderno, folha ou arquivo digital
- Nome do arquivo (se digital): Ciclo_Vida_Software_NomeAluno
- Local de entrega: Avaliação em sala ou envio via Google Classroom/Drive
- Prazo sugerido: Durante a aula

##### 11. Encerramento e Reflexão

Finalize a aula conduzindo uma reflexão orientada:

- Por que a escolha do ciclo de vida influencia o sucesso de um software?
- O mesmo modelo serve para todos os projetos?
- Como essa escolha impacta tempo, custo e qualidade?
