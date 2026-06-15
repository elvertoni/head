---
titulo: Análise de Resultados
tema: Marketing Digital
disciplina: analise-e-projeto-de-sistemas
serie: 3ª
prerequisitos: [O que é marketing digital, Planejamento de marketing]
objetivos:
  - Explicar o que é análise de resultados e por que ela fecha o ciclo do marketing
  - Interpretar as principais métricas — CTR, taxa de conversão, CPC e ROI
  - Reconhecer as ferramentas de análise e diferenciar métrica de vaidade de métrica de negócio
trilha: marketing-digital
ordem: 29
modo_origem: seed
fontes:
  - lake/analise-e-projeto-de-sistemas/AULA 29_ANÁLISE E PROJETO DE SISTEMAS.pptx
revisao: true
status: aprovada
versao: 1
atualizado_em: 2026-06-15
---

Você lembra do maior superpoder do marketing digital, lá da Aula 25? A **mensurabilidade**. Pois chegou a hora de usá-la de verdade. Imagine que você rodou uma campanha lindíssima: o post bombou, 10 mil curtidas, todo mundo comentando. Sucesso total, né? Talvez não. E se nenhuma dessas 10 mil pessoas comprou nada? Curtida não paga conta. Hoje você aprende a separar o que **parece** sucesso do que **é** sucesso — lendo os números que realmente importam.

## Objetivos

Ao final desta aula, você será capaz de:

- Explicar **o que é** análise de resultados e como ela fecha o ciclo planejar → executar → medir.
- Interpretar as principais **métricas**: CTR, taxa de conversão, CPC e ROI.
- Reconhecer as **ferramentas** de análise e distinguir **métrica de vaidade** de **métrica de negócio**.

## Pré-requisitos

Ter visto a **Aula 28** (planejamento de marketing — objetivos, metas e mensurabilidade).

## Desenvolvimento

### Fechando o ciclo

:::conceito Análise de resultados
É a coleta, medição e **interpretação** de dados para avaliar o desempenho das campanhas. Ela responde três perguntas: o que funcionou, onde estão os problemas e como melhorar. É a etapa que transforma a meta SMART da aula passada em **veredito**: bateu ou não bateu?

:::

Sem essa etapa, o planejamento fica incompleto — você teria definido o destino mas nunca olharia o GPS para saber se chegou.

### As quatro métricas que você precisa ler

Quatro números aparecem em quase toda campanha. Veja como eles se encadeiam, do primeiro contato até o lucro:

```diagrama-progressivo
titulo: Do clique ao lucro — as quatro métricas
camadas:
  - rotulo: 1. CTR (Taxa de Cliques)
    conteudo: De quem VIU o anúncio, quantos clicaram? CTR = cliques ÷ visualizações. CTR baixo significa que o anúncio não chamou atenção.
  - rotulo: 2. Taxa de Conversão
    conteudo: De quem CLICOU, quantos fizeram o que você queria (comprar, cadastrar)? Conversão baixa indica problema na página de destino, não no anúncio.
  - rotulo: 3. CPC (Custo por Clique)
    conteudo: Quanto você pagou, em média, por cada clique? Ajuda a saber se o tráfego está caro demais.
  - rotulo: 4. ROI (Retorno sobre Investimento)
    conteudo: O número final. ROI = (Receita − Custo) ÷ Custo. Diz se a campanha deu lucro ou prejuízo. É a métrica que decide tudo.
```

:::importante O perigo das métricas de vaidade
**Curtidas e seguidores são métricas de vaidade**: incham o ego, mas não provam resultado. **Conversão e ROI são métricas de negócio**: dizem se entrou dinheiro. Uma campanha com 10 mil curtidas e ROI negativo está **dando prejuízo**, por mais bonita que pareça. Aprenda a olhar primeiro para a métrica que paga a conta.

:::

:::atencao Erro comum
Comemorar o número errado. Um anúncio com CTR altíssimo (todo mundo clica) mas conversão zero (ninguém compra) não é vitória — é dinheiro vazando. O clique custou, e não virou venda. Sempre leia as métricas **em conjunto**: uma sozinha engana.

:::

### As ferramentas que mostram os números

- **Google Analytics** — gratuita; mostra tráfego, comportamento do usuário e desempenho do site.
- **SEMrush** — análise de concorrentes, palavras-chave e auditoria de SEO.
- **Tableau** — transforma planilhas de dados em gráficos e *dashboards* fáceis de interpretar.

:::dica Aqui mora o seu futuro emprego
Quem você acha que **constrói** esses dashboards e conecta os dados? O analista e o desenvolvedor. Registrar o evento de "compra concluída", montar a consulta que calcula o ROI, ligar o banco de dados ao Tableau — isso é trabalho técnico, não de marketing. A área que mais cresce hoje é justamente a de **dados**: profissionais que sabem transformar números brutos em decisão. Esta aula é um aperitivo dela.

:::

## Prática

**Atividade "detetive de campanha" (em duplas, sem computador obrigatório, ~15 min).** Lucas rodou duas campanhas. No caderno, analisem e decidam:

- **Campanha A:** 1.000 cliques · R$ 500 gastos · 50 vendas · R$ 2.000 de receita.
- **Campanha B:** 5.000 cliques · R$ 500 gastos · 10 vendas · R$ 400 de receita.

1. Calculem o **ROI** de cada uma: (Receita − Custo) ÷ Custo.
2. Qual teve mais cliques? Qual deu mais **lucro**? São a mesma?
3. A Campanha B teve 5x mais cliques. Por que ainda assim foi a pior?
4. **Veredito:** em qual Lucas deveria investir mais? Justifiquem com o número.

Cada dupla anuncia o ROI que calculou. A turma confere: a campanha "mais popular" foi a mais lucrativa? (Spoiler: A tem ROI = 3,0; B tem ROI = −0,2 — prejuízo.)

## Avaliação

```quiz
- pergunta: Qual métrica mede o percentual de pessoas que clicam no anúncio em relação a quantas o viram?
  alternativas:
    - texto: Taxa de Conversão
    - texto: Custo por Clique (CPC)
    - texto: Taxa de Cliques (CTR)
      correta: true
    - texto: Retorno sobre Investimento (ROI)
  feedback: >
    CTR = cliques ÷ visualizações. Mede se o anúncio chamou atenção de quem o viu.
    Conversão é o passo seguinte (de quem clicou, quantos compraram).
- pergunta: Uma campanha tem 10 mil curtidas mas ROI negativo. Como interpretá-la?
  alternativas:
    - texto: É um sucesso, porque teve muito engajamento
    - texto: Está dando prejuízo — curtida é métrica de vaidade, ROI é métrica de negócio
      correta: true
    - texto: As curtidas compensam o prejuízo
    - texto: Faltou publicar mais posts
  feedback: >
    Curtida não paga conta. ROI negativo significa que saiu mais dinheiro do que
    entrou — a campanha é bonita e deficitária ao mesmo tempo.
- pergunta: Uma campanha tem CTR altíssimo, mas taxa de conversão zero. O que isso indica?
  alternativas:
    - texto: A campanha é perfeita
    - texto: Muita gente clica, mas ninguém compra — o clique está custando sem virar venda
      correta: true
    - texto: O anúncio não está sendo visto
    - texto: O ROI com certeza é positivo
  feedback: >
    Clique sem conversão é dinheiro vazando. Métricas precisam ser lidas em conjunto:
    CTR alto + conversão zero costuma apontar problema na página de destino.
```

## Fechamento

Hoje você descobriu que:

- **Análise de resultados** fecha o ciclo do marketing: diz o que funcionou, o que falhou e como melhorar.
- As quatro métricas se encadeiam: **CTR** (chamou atenção?) → **conversão** (virou ação?) → **CPC** (custou quanto?) → **ROI** (deu lucro?).
- **Métricas de vaidade** (curtidas) enganam; **métricas de negócio** (conversão, ROI) decidem.
- Construir os **dashboards** e o rastreamento é trabalho técnico — a área de **dados** é uma das que mais cresce para quem desenvolve.

**Próxima aula:** números convencem a razão, mas não emocionam. Para a campanha — e para a sua carreira — faltam histórias. Na Aula 30 fechamos a trilha com **storytelling**.

:::roteiro
Abrir com o paradoxo das 10 mil curtidas sem venda — provoca antes de qualquer definição. As quatro métricas funcionam melhor desenhadas como funil no quadro (viu → clicou → comprou → lucrou). A prática do "detetive" é o coração: deixe-os calcular o ROI sozinhos antes de revelar; o choque de a campanha com 5x mais cliques ser a pior fixa a lição de "métrica em conjunto". Tenha a conta pronta: A = (2000−500)/500 = 3,0; B = (400−500)/500 = −0,2. A `:::dica` de dados é a ponte de carreira — vale citar que analista de dados é vaga quente. Alura ("Conceitos e principais métricas") opcional. 8 min para o quiz.
:::
