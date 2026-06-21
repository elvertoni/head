---
titulo: Desenvolvimento AI-First vs AI-Enabled
tema: Fundamentos de IA
disciplina: inteligencia-artificial
serie: Extra
prerequisitos: [Harness Engineering, Agentes e Subagentes]
objetivos:
  - Diferenciar uma empresa AI-enabled de uma AI-first
  - Explicar por que habilitar a ferramenta não basta sem mudar o processo
  - Reconhecer o papel do humano que orquestra, revisa e valida
trilha: fundamentos-de-ia
ordem: 22
slug: desenvolvimento-ai-first-vs-ai-enabled
modo_origem: material
fontes:
  - lake/inteligencia-artificial/ia-coders/desenvolvimento-ai-first-vs-ai-enabled.md
  - lake/inteligencia-artificial/ia-master
revisao: true
status: aprovada
versao: 1
atualizado_em: 2026-06-15
---

Hoje quase toda empresa diz que "usa IA". Mas tem duas formas muito diferentes de fazer isso, e a diferença decide quem vai prosperar e quem vai ficar para trás. A primeira: pegar o jeito antigo de trabalhar e **colar uma ferramenta de IA por cima** — continua tudo igual, só com um assistente ajudando. A segunda: **repensar o processo inteiro** em torno da IA, desde o planejamento. A primeira é AI-enabled; a segunda é AI-first. Entender essa diferença é entender o futuro do trabalho que **vocês** vão pegar — porque ele já está mudando.

## Objetivos

Ao final desta aula, você será capaz de:

- Diferenciar uma empresa **AI-enabled** de uma **AI-first**.
- Explicar por que **habilitar a ferramenta** não basta sem **mudar o processo**.
- Reconhecer o papel do **humano que orquestra, revisa e valida**.

## Pré-requisitos

Ter visto as **Aulas 18 e 21** (agentes e harness).

## Desenvolvimento

### Duas formas de "usar IA"

:::conceito AI-enabled e AI-first
**AI-enabled:** você mantém o processo de sempre (o mesmo time, a mesma rotina) e apenas **habilita uma ferramenta** de IA por cima. **AI-first:** você **repensa o processo inteiro** assumindo a IA desde o começo — do planejamento à execução. No AI-enabled a IA ajuda; no AI-first a IA muda como o trabalho é feito.

:::

:::atencao Erro comum
"Instalei uma ferramenta de IA, logo sou AI-first." Não. Só ligar a ferramenta no mesmo processo de antes é **AI-enabled** — e tem um **teto baixo** de ganho, porque o processo continua desenhado para humanos fazendo tudo na mão. AI-first exige **mudar o processo**: às vezes times menores, novas etapas automatizadas, outra forma de organizar o trabalho. Ferramenta nova em processo velho rende pouco.

:::

### O que o AI-first traz: velocidade

O ganho central do AI-first é **velocidade** em tudo — planejar, prototipar, corrigir bugs, resolver crises. Um exemplo real do dia a dia de quem programa:

```diagrama-progressivo
titulo: Um bug em produção, dois mundos
camadas:
  - rotulo: 1. O problema
    conteudo: Madrugada, um sistema quebra. Alguém precisa investigar o que aconteceu.
  - rotulo: 2. Jeito tradicional (AI-enabled)
    conteudo: A pessoa acorda, abre os logs na mão, procura pistas em vários lugares, junta os dados. Perde um tempão só coletando informação antes de decidir.
  - rotulo: 3. Jeito AI-first
    conteudo: No mesmo instante do alerta, um agente já coleta os logs, cruza os dados e monta um relatório. Quando a pessoa senta no computador, a análise já está pronta.
  - rotulo: 4. A diferença
    conteudo: Não é "a ferramenta ajudou a ler o log". É o processo inteiro redesenhado para a IA agir antes, e o humano só decidir. Isso é velocidade de verdade.
```

### O humano não some — ele sobe de papel

:::dica O seu lugar nesse futuro
Atenção a este ponto, porque é sobre o **seu** emprego: no AI-first, o desenvolvedor não desaparece — ele **muda de função**. Em vez de fazer tudo na mão, ele passa a **orquestrar, revisar e validar** o que os agentes produzem. Decide o que automatizar, confere a qualidade, assume a responsabilidade. Quem só sabia "fazer na mão" fica para trás; quem sabe **dirigir a IA** (tudo que você aprendeu nesta trilha: prompt, contexto, ferramentas, freios) sobe de nível. A IA não tira o seu lugar — ela muda o que se espera de você.

:::

## Prática

**Atividade "enabled ou first?" (em duplas, sem computador, ~15 min).**

1. **Classifiquem** cada cenário como AI-enabled ou AI-first, justificando:
   - a) Uma escola que pede para os professores usarem ChatGPT para corrigir redações mais rápido, mas mantém todo o resto igual.
   - b) Uma escola que redesenhou o atendimento: um agente tria as dúvidas dos alunos 24h, resolve as simples e escala as difíceis para um humano.
   - c) Um jornal onde cada repórter usa IA para revisar o próprio texto.
   - d) Um jornal que montou uma redação onde a IA gera rascunhos e os jornalistas só editam e validam.
2. **Repensem um processo:** escolham uma rotina da escola (matrícula, biblioteca, eventos) e descrevam como seria a versão **AI-first** dela. O que mudaria no processo, não só na ferramenta?
3. Onde, nessa versão AI-first, **o humano** precisa orquestrar/revisar/validar?

Cada dupla apresenta seu processo AI-first. A turma avalia: mudou o processo ou só colou uma ferramenta?

## Avaliação

```quiz
- pergunta: Qual a diferença entre AI-enabled e AI-first?
  alternativas:
    - texto: AI-enabled é mais caro
    - texto: AI-enabled habilita uma ferramenta no processo antigo; AI-first repensa o processo todo em torno da IA
      correta: true
    - texto: São a mesma coisa
    - texto: AI-first não usa humanos
  feedback: >
    Enabled = ferramenta por cima do processo antigo (teto baixo). First = processo
    redesenhado assumindo a IA desde o começo.
- pergunta: Por que só "instalar uma ferramenta de IA" rende pouco?
  alternativas:
    - texto: Porque a ferramenta é ruim
    - texto: Porque o processo continua desenhado para humanos fazendo tudo na mão (teto baixo)
      correta: true
    - texto: Porque IA não funciona em empresas
    - texto: Porque ninguém sabe usar
  feedback: >
    Ferramenta nova em processo velho tem teto baixo. O ganho real vem de redesenhar o
    processo (AI-first), não só de habilitar a ferramenta.
- pergunta: No modelo AI-first, qual passa a ser o papel do humano?
  alternativas:
    - texto: Desaparece completamente
    - texto: Orquestrar, revisar e validar o que os agentes produzem
      correta: true
    - texto: Apenas observar sem fazer nada
    - texto: Fazer tudo na mão como antes
  feedback: >
    O humano sobe de papel: decide o que automatizar, dirige os agentes e valida a
    qualidade. Quem sabe dirigir a IA sobe de nível.
```

## Fechamento

Hoje você descobriu que:

- **[[ai-first-vs-ai-enabled|AI-enabled]]** cola uma ferramenta no processo antigo; **AI-first** repensa o processo inteiro em torno da IA.
- Só habilitar a ferramenta tem **teto baixo** — o ganho vem de **mudar o processo**.
- O ganho central do AI-first é **velocidade** em tudo (planejar, corrigir, prototipar).
- O humano **não some**: ele passa a **orquestrar, revisar e validar**.

**Próxima aula:** a IA é poderosa, mas falha — e às vezes mente com toda a confiança. Na Aula 23 encaramos o maior risco de usar IA: as **alucinações**.

:::roteiro
Vem da transcrição ia-coders (modo Material), simplificada do contexto corporativo de dev para 14-18. Abrir com "toda empresa diz que usa IA — mas tem dois jeitos". O erro "instalei ferramenta = AI-first" é o coração. O exemplo do bug em produção (tradicional vs AI-first) é concreto e ilustra velocidade. A `:::dica` sobre o papel do humano é a mais importante para a faixa — fala do futuro do trabalho deles, sem alarmismo. Revisão aplicada: cortei feedforward/spec-driven/contextual-layer (acima da faixa). 8 min pro quiz.
:::
