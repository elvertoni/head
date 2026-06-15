---
titulo: Aprendizado Supervisionado na Prática
tema: Fundamentos de IA
disciplina: inteligencia-artificial
serie: Extra
prerequisitos: [Tipos de Aprendizado de Máquina]
objetivos:
  - Diferenciar classificação de regressão pela pergunta que respondem
  - Reconhecer exemplos reais de cada uma
  - Escolher a tarefa certa para um problema dado
trilha: fundamentos-de-ia
ordem: 6
modo_origem: tema
fontes: []
revisao: false
status: aprovada
versao: 1
atualizado_em: 2026-06-15
---

Quase tudo que o [[aprendizado-supervisionado|aprendizado supervisionado]] faz cabe em duas perguntas simples. A primeira é **"qual categoria?"** — isto é spam ou não? esta foto é gato, cachorro ou pássaro? A segunda é **"quanto?"** — quanto vai custar esta casa? qual será a temperatura amanhã? Parecem parecidas, mas exigem coisas diferentes da máquina, e trocar uma pela outra é um erro clássico de quem está começando. Hoje você aprende a distinguir as duas tarefas mais importantes do supervisionado: classificação e regressão.

## Objetivos

Ao final desta aula, você será capaz de:

- **Diferenciar** classificação de regressão pela **pergunta** que cada uma responde.
- Reconhecer **exemplos reais** de cada uma.
- **Escolher** a tarefa certa para um problema dado.

## Pré-requisitos

Ter visto a **Aula 05** (os três tipos de aprendizado; em especial o supervisionado).

## Desenvolvimento

### Duas perguntas, duas tarefas

O supervisionado se divide em duas tarefas, e dá pra saber qual é só olhando o **tipo de resposta** que você quer.

:::conceito Classificação e regressão
**Classificação** responde **"qual categoria?"** — a saída é um rótulo de um conjunto fechado (spam/não-spam; gato/cachorro/pássaro). **Regressão** responde **"quanto?"** — a saída é um **número** dentro de uma faixa contínua (preço, temperatura, nota). A pergunta define a tarefa: categoria → classificação; número → regressão.

:::

| Pergunta | Tarefa | Saída | Exemplo |
|---|---|---|---|
| "Qual categoria?" | **Classificação** | um rótulo | este e-mail é spam? |
| "Quanto?" | **Regressão** | um número | qual o preço deste celular? |

:::atencao Erro comum
Tratar um problema de **número** como se fosse de **categoria** (ou vice-versa). "Prever a nota de 0 a 10" não é escolher entre dez caixinhas — é estimar um valor que pode ser 7,4. Forçar isso a virar classificação joga fora informação e piora o resultado. Antes de escolher a técnica, pergunte: **a resposta é uma categoria ou um número?** Essa única pergunta já decide a tarefa.

:::

### A fronteira nem sempre é óbvia

Tem casos que enganam. "Prever quantas estrelas (1 a 5) um filme vai receber" — parece número, mas as estrelas são categorias ordenadas; dá pra tratar dos dois jeitos, dependendo do objetivo. O ponto não é decorar regrinha, e sim treinar o olhar: **que tipo de resposta o problema pede?**

:::dica No mundo real, isso aparece o tempo todo
Sistemas de recomendação, detecção de fraude, previsão de vendas — quase todo produto de dados é, no fundo, uma classificação ou uma regressão (ou uma combinação delas). Saber enxergar "isto aqui é classificação, aquilo é regressão" é o primeiro passo que um analista dá ao receber um problema novo. É um olhar profissional que você começa a treinar agora.

:::

## Prática

**Atividade "classificação ou regressão?" (em duplas, sem computador, ~15 min).** Para cada problema, decidam a tarefa e escrevam a **pergunta-chave** que justifica ("qual categoria?" ou "quanto?"):

1. Prever o **preço** de venda de um carro usado.
2. Decidir se uma transação no cartão é **fraude ou não**.
3. Estimar **quantos litros** de água um reservatório terá amanhã.
4. Identificar se uma foto de pele tem uma pinta **benigna ou suspeita**.
5. Prever a **nota** (0 a 100) de um aluno no vestibular.
6. Reconhecer em qual de **5 emoções** está um rosto (feliz, triste, bravo, surpreso, neutro).

Cada dupla apresenta dois itens. A turma debate os que geraram dúvida — algum poderia ser os dois?

## Avaliação

```quiz
- pergunta: Qual pergunta caracteriza a CLASSIFICAÇÃO?
  alternativas:
    - texto: "Quanto?" — a resposta é um número
    - texto: "Qual categoria?" — a resposta é um rótulo de um conjunto fechado
      correta: true
    - texto: "Onde?" — a resposta é um lugar
    - texto: "Quando?" — a resposta é uma data
  feedback: >
    Classificação responde "qual categoria?" e devolve um rótulo (spam/não, gato/
    cachorro). Quando a resposta é um número, é regressão.
- pergunta: Prever o PREÇO de uma casa é tarefa de…
  alternativas:
    - texto: Classificação
    - texto: Regressão
      correta: true
    - texto: Aprendizado por reforço
    - texto: Aprendizado não-supervisionado
  feedback: >
    Preço é um número numa faixa contínua, então é regressão ("quanto?"). Não é
    escolher entre categorias fixas.
- pergunta: Por que é um erro tratar "prever uma nota de 0 a 10" como classificação em 10 caixinhas?
  alternativas:
    - texto: Porque joga fora informação — a nota é um número contínuo (pode ser 7,4)
      correta: true
    - texto: Porque notas não podem ser previstas
    - texto: Porque classificação é sempre proibida
    - texto: Porque regressão não existe
  feedback: >
    A nota é um valor contínuo; forçá-la em categorias fixas descarta nuance (o 7,4) e
    piora o resultado. Número → regressão.
```

## Fechamento

Hoje você descobriu que:

- O [[aprendizado-supervisionado|supervisionado]] tem duas tarefas centrais ([[classificacao-e-regressao]]): **classificação** ("qual categoria?") e **regressão** ("quanto?").
- A **pergunta** define a tarefa: categoria → classificação; número → regressão.
- Forçar um número a virar categoria (ou o contrário) é um erro clássico.
- Quase todo produto de dados real é, no fundo, classificação ou regressão.

**Próxima aula:** e quando não há gabarito nenhum? Vamos ao **aprendizado não-supervisionado** — achar grupos e padrões escondidos sem ninguém dizer o que é o quê.

:::roteiro
Abrir com as duas perguntas ("qual categoria?" vs "quanto?") — é o resumo da aula numa frase. A tabela fixa a distinção. O erro de tratar número como categoria é o alvo: o exemplo da nota 7,4 gruda. Os casos-fronteira (estrelas de filme) mostram que o olhar importa mais que decoreba. Na prática, os itens 5 (nota) e 6 (emoções) contrastam bem número vs categoria; deixe debaterem os ambíguos. Conteúdo estável, sem web. 8 min pro quiz.
:::
