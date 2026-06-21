---
titulo: Planejamento de Releases
tema: Metodologias Ágeis
disciplina: analise-e-metodos-para-sistemas
serie: 1ª
prerequisitos: [Priorização do Backlog]
objetivos:
  - Explicar o que é uma release e por que entregar em partes reduz risco
  - Dividir um projeto em sprints e relacioná-las às entregas
  - Reconhecer que o cronograma ágil é estimado e ajustável, não fixo
trilha: metodologias-ageis
ordem: 38
slug: planejamento-de-releases
modo_origem: seed
fontes:
  - lake/analise-e-metodos-para-sistemas/AULA 38_ANÁLISE E MÉTODO PARA SISTEMAS.pptx
revisao: true
status: aprovada
versao: 2
atualizado_em: 2026-06-21
---

Você toparia comer um bolo inteiro de uma garfada só? Ninguém topa — a gente come em fatias. Entregar software também: jogar o produto inteiro no cliente só no último dia é arriscado (e se estiver errado, descobre tarde demais). O Scrum prefere entregar em fatias que já funcionam, chamadas releases. Você já aprendeu a montar o time, organizar e priorizar o backlog; agora vai aprender a combinar **quando** cada fatia vai para a mesa.

## Objetivos

Ao final desta aula, você será capaz de:

- Explicar o que é uma **release** e por que entregar em partes **reduz risco**.
- **Dividir** um projeto em sprints e relacioná-las às entregas.
- Reconhecer que o cronograma ágil é **estimado e ajustável**, não fixo.

## Pré-requisitos

Ter visto a **Aula 37** (priorização do backlog).

## Desenvolvimento

### Em uma frase

:::importante
Release é a fatia pronta do produto: entregar em partes reduz risco e permite ajuste cedo.
:::

### O que é uma release

:::conceito Release
É uma **entrega** de uma versão do produto com um conjunto de funcionalidades prontas e funcionando, disponibilizada para o usuário. Em vez de uma entrega única no fim, o Scrum faz **entregas incrementais**: várias releases ao longo do projeto, cada uma somando valor à anterior.

:::

:::exemplo
Se o app da cantina fosse um bolo, a Release 1 seria a fatia mais simples que já mata a fome. As próximas fatias acrescentam cobertura, recheio e enfeite sem esperar o bolo inteiro ficar pronto.
:::

Entregar em releases reduz o risco: a cada fatia o cliente usa, dá retorno e o time corrige cedo. Se algo está errado, você descobre na release 1, não seis meses depois.

### De backlog a cronograma

Como se planeja isso? Em quatro movimentos:

```diagrama-progressivo
titulo: Planejando o cronograma de releases
camadas:
  - rotulo: 1. Definir o objetivo de cada release
    conteudo: O que cada entrega deve alcançar, com base no valor e nas prioridades do backlog. Ex.: "Release 1: cliente consegue ver cardápio e fazer pedido."
  - rotulo: 2. Dividir em sprints
    conteudo: Cada release é construída em uma ou mais sprints (ciclos de 2 a 4 semanas). Os itens prioritários entram nas primeiras.
  - rotulo: 3. Estimar trabalho e capacidade
    conteudo: O time estima o esforço dos itens e avalia quanto consegue fazer por sprint (sua capacidade). Isso define o que cabe em cada ciclo.
  - rotulo: 4. Monitorar e ajustar
    conteudo: Ao longo do projeto, compara-se o progresso com o planejado e ajusta-se o cronograma — realocando itens ou revendo prioridades.
```

:::atencao Erro comum
Tratar o cronograma ágil como uma **promessa de pedra**. Em métodos tradicionais, o cronograma é fixo e mudar é "fracasso". No ágil é o contrário: o cronograma é uma **estimativa viva**, feita para ser ajustada conforme o time aprende. Mudar o plano com base em novas informações é sinal de maturidade, não de erro.

:::

### Estimar é diferente de adivinhar

Para planejar releases, o time precisa **estimar** quanto esforço cada item dá e quanta coisa consegue entregar por sprint (a **capacidade**). Estimativa não é chute aleatório nem promessa exata — é uma previsão informada que melhora a cada sprint, quando o time compara o que planejou com o que realmente entregou.

:::dica O cronograma físico-financeiro
No mundo profissional, esse planejamento de entregas vira o **cronograma do projeto** — documento que clientes e gestores cobram. Saber dividir um trabalho grande em entregas datadas e ajustáveis é exatamente a habilidade de "acompanhar o cronograma de um projeto" que aparece no perfil do técnico em desenvolvimento de sistemas.

:::

## Prática

**Atividade "montando as releases" (em duplas, sem computador, ~15 min).** O **app da cantina** será construído em **3 sprints de 2 semanas**. Usando a priorização que vocês já fizeram, planejem:

1. **Release 1** (fim da sprint 1): o **mínimo** que já entrega valor de verdade ao usuário. O que entra?
2. **Release 2** (fim da sprint 2): o que somar em cima da primeira?
3. **Release 3** (fim da sprint 3): os complementos que melhoram a experiência.
4. **Imprevisto:** na sprint 2, um item revelou-se o dobro do trabalho esperado. O que vocês ajustam no cronograma?

Cada dupla apresenta sua Release 1. A turma debate: foi mínima de verdade ou colocaram coisa demais?

## Avaliação

```quiz
- pergunta: O que é uma release no Scrum?
  alternativas:
    - texto: A reunião diária do time
    - texto: Uma entrega de uma versão do produto com funcionalidades prontas e funcionando
      correta: true
    - texto: A lista de todos os bugs
    - texto: O papel responsável por priorizar
  feedback: >
    Release é uma entrega incremental — uma fatia do produto pronta para o usuário.
    Várias releases ao longo do projeto reduzem o risco.
- pergunta: Por que entregar em releases reduz o risco do projeto?
  alternativas:
    - texto: Porque o cliente usa e dá retorno cedo, permitindo corrigir antes
      correta: true
    - texto: Porque ninguém precisa testar o produto
    - texto: Porque o projeto fica mais lento de propósito
    - texto: Porque elimina a necessidade de planejar
  feedback: >
    Como comer o bolo em fatias: a cada entrega o cliente experimenta e o time
    corrige cedo, em vez de descobrir o erro só no final.
- pergunta: Como o cronograma de releases deve ser tratado no ágil?
  alternativas:
    - texto: Como uma promessa fixa que nunca pode mudar
    - texto: Como uma estimativa viva, ajustada conforme o time aprende
      correta: true
    - texto: Como algo irrelevante que ninguém acompanha
    - texto: Como responsabilidade exclusiva do cliente
  feedback: >
    O cronograma ágil é estimado e ajustável. Mudá-lo com base em novas informações
    é maturidade, não fracasso.
```

## Fechamento

Hoje você descobriu que:

- **Release** é uma entrega incremental do produto — e entregar em fatias **reduz o risco**.
- Planejar releases é: definir o objetivo de cada uma, **dividir em sprints**, **estimar** trabalho e capacidade, e **monitorar/ajustar**.
- O cronograma ágil é uma **estimativa viva**, não uma promessa de pedra.
- **Estimar** é prever de forma informada — e melhora a cada sprint.

**Próxima aula:** já vimos as peças do Scrum separadas. Hora de juntar tudo numa visão só e olhar, com honestidade, os **benefícios e os desafios** de planejar com Scrum.

:::roteiro
Abrir com o bolo em fatias — entrega incremental fica óbvia. O diagrama dos 4 passos dá a mecânica; o passo 3 (capacidade) conecta com a próxima aula sobre estimativa. O erro "cronograma de pedra" é a diferença-chave entre tradicional e ágil — vale contrastar no quadro. Na prática, o ponto alto é a Release 1 "mínima de verdade": quase todo grupo coloca coisa demais; o imprevisto da sprint 2 ensina o ajuste. Conecte com "cronograma físico-financeiro" do perfil profissional. Alura ("Cronograma de release") opcional. 8 min pro quiz.
:::
