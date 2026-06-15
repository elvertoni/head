---
titulo: Harness Engineering
tema: Fundamentos de IA
disciplina: inteligencia-artificial
serie: Extra
prerequisitos: [Agentes e Subagentes, Tool Use e Function Calling]
objetivos:
  - Explicar o que é o harness e diferenciá-lo do modelo
  - Reconhecer componentes essenciais do harness, em especial os guardrails
  - Entender que o salto da demo para a produção mora no harness
trilha: fundamentos-de-ia
ordem: 21
modo_origem: material
fontes:
  - lake/inteligencia-artificial/ia-coders/o-que-e-harness-engineering.md
revisao: true
status: aprovada
versao: 1
atualizado_em: 2026-06-15
---

Pega o motor de uma Ferrari e bota num Fusca. Você tem um motorzão — mas sem a carroceria, os freios, o câmbio e o painel certos, esse motor não te leva a lugar nenhum com segurança. O [[llm]] é exatamente isso: um motor. Sozinho, ele só gera texto. Tudo que vimos neste módulo — o loop do agente, as ferramentas, a memória, os freios — é a **carroceria** que transforma o motor num carro que anda. Esse conjunto ao redor do modelo tem nome: harness. E tem uma tese provocadora por trás: a diferença entre uma demo bonita e um produto que funciona de verdade quase nunca está no modelo — está no harness. Fechamos o módulo de agentes pela infraestrutura que faz tudo girar.

## Objetivos

Ao final desta aula, você será capaz de:

- Explicar o que é o **harness** e diferenciá-lo do **modelo**.
- Reconhecer **componentes essenciais** do harness, em especial os **guardrails**.
- Entender que o salto da **demo para a produção** mora no harness.

## Pré-requisitos

Ter visto as **Aulas 18 e 19** (agentes, loop de decisão e tool use).

## Desenvolvimento

### Motor x carro

:::conceito Harness
É **toda a infraestrutura ao redor do [[llm]]**: o loop de decisão do [[agente]], as ferramentas que ele chama ([[tool-use]]), a memória, os limites e o feedback. O modelo sozinho é o **motor** (só gera texto, não lembra nada, não age). O harness é o **carro inteiro** — é ele que dá ao modelo a capacidade de **agir no mundo** de forma útil e controlada.

:::

A diferença é nítida: o **modelo** recebe texto e devolve texto, sem memória e sem fazer nada sozinho. O **harness** chama o modelo em loop, executa as ferramentas, guarda o estado, valida os resultados e sabe a hora de parar.

### Os freios: guardrails

De todos os componentes do harness, um é especialmente importante para você entender hoje.

:::conceito Guardrails
São as **regras do que o agente pode e não pode fazer** — os freios de segurança. Exemplos: não apagar arquivos importantes, não gastar acima de um limite, **pedir aprovação humana** antes de uma ação séria. Sem guardrails, um agente autônomo (Aula 18) pode causar estrago: apagar o que não devia, gastar demais, agir errado em escala. Os guardrails são o cinto de segurança da IA que age.

:::

```diagrama-progressivo
titulo: O que o harness faz ao redor do modelo
camadas:
  - rotulo: 1. Chama o modelo em loop
    conteudo: O harness roda o loop observar-pensar-agir do agente, chamando o modelo a cada rodada.
  - rotulo: 2. Executa as ferramentas
    conteudo: Quando o modelo pede uma ferramenta (Aula 19), é o harness que executa de verdade e devolve o resultado.
  - rotulo: 3. Guarda memória e estado
    conteudo: O modelo não lembra nada sozinho. O harness mantém o que já foi feito e o contexto relevante.
  - rotulo: 4. Aplica guardrails e para
    conteudo: Verifica o que é permitido, pede aprovação quando preciso e define a condição de parada. É o freio e o juiz.
```

:::atencao Erro comum
Achar que "o que importa é só o modelo — basta usar o melhor". Falso. Um modelo excelente num harness ruim entrega mal; um modelo mediano num harness ótimo pode brilhar. A tese central: **o salto da demo para a produção está no harness**, não no modelo. É por isso que ferramentas com o mesmo modelo por baixo entregam resultados tão diferentes — o que muda é a infraestrutura ao redor.

:::

:::dica Onde mora a engenharia de verdade
Essa é uma das ideias mais valiosas do módulo para a sua carreira: o diferencial competitivo raramente é "ter acesso ao melhor modelo" (todo mundo tem). O diferencial é construir o **harness** certo — boas ferramentas, boa memória, bons guardrails. Quem entende isso para de caçar o "modelo mágico" e foca em construir a infraestrutura que faz qualquer modelo render. É aí que está o trabalho de engenharia que o mercado paga bem.

:::

## Prática

**Atividade "projete o harness" (em grupos de 4, sem computador, ~15 min).**

Vocês vão dar a um agente a tarefa de **"responder e-mails dos clientes de uma loja"**. O modelo (motor) já existe; vocês projetam o harness ao redor.

1. **Ferramentas:** quais ferramentas o agente precisa? (ex.: ler e-mails, consultar pedidos, enviar resposta)
2. **Memória:** o que ele precisa lembrar entre um e-mail e outro?
3. **Guardrails (o ponto central):** listem **3 coisas que o agente NÃO pode fazer** sem aprovação humana (ex.: dar reembolso, prometer prazo, apagar dados).
4. **Condição de parada:** quando o agente considera o e-mail "resolvido"?
5. **Falha:** o que deveria acontecer se uma ferramenta falhar — o agente pode **inventar** o resultado? (resposta: não!)

Cada grupo apresenta seus **3 guardrails**. A turma vota: qual seria o mais perigoso de esquecer?

## Avaliação

```quiz
- pergunta: Qual a diferença entre o modelo e o harness?
  alternativas:
    - texto: São a mesma coisa
    - texto: O modelo é o "motor" (só gera texto); o harness é o "carro" ao redor que o faz agir
      correta: true
    - texto: O harness é um modelo mais inteligente
    - texto: O modelo executa ferramentas e o harness só conversa
  feedback: >
    Modelo = motor (gera texto, sem memória, não age). Harness = a infra ao redor
    (loop, ferramentas, memória, freios) que dá ao modelo a capacidade de agir.
- pergunta: Para que servem os guardrails?
  alternativas:
    - texto: Para deixar o agente mais rápido
    - texto: Para limitar o que o agente pode fazer, com freios e aprovação humana
      correta: true
    - texto: Para treinar o modelo
    - texto: Para aumentar a memória
  feedback: >
    Guardrails são os freios de segurança: definem o que o agente NÃO pode fazer e
    exigem aprovação humana em ações sérias. Essenciais para agentes autônomos.
- pergunta: Onde costuma estar o salto da "demo bonita" para o "produto que funciona"?
  alternativas:
    - texto: Sempre no modelo — basta usar o melhor
    - texto: No harness — a infraestrutura ao redor do modelo
      correta: true
    - texto: No preço do computador
    - texto: Na cor da interface
  feedback: >
    A tese central: o gap demo→produção mora no harness, não no modelo. Mesmo modelo +
    harness melhor = resultado muito melhor.
```

## Fechamento

Hoje você descobriu que:

- O **[[harness]]** é toda a infraestrutura ao redor do [[llm]]: loop, ferramentas, memória e freios.
- O **modelo é o motor**; o **harness é o carro** que o faz andar com segurança.
- Os **[[guardrails]]** são os freios — definem o que o agente pode/não pode e quando pedir aprovação humana.
- O salto da **demo para a produção** mora no **harness**, não no modelo.

**Próximo módulo (Desenvolver com IA + Responsabilidade):** você já entende a IA por dentro e por fora. Hora de usá-la com juízo. No módulo final: como **construir com IA**, lidar com **alucinações**, medir qualidade e a **responsabilidade** de tudo isso.

:::roteiro
Vem da transcrição ia-coders (modo Material), bem simplificada — o original é denso (7 componentes, 4 topologias, contextual layer). Mantive o essencial para 14-18: motor vs carro, o que o harness faz, e guardrails. A analogia motor-da-Ferrari-no-Fusca abre forte. Guardrails são o foco prático e amarram com o "freio humano" da aula 18. O erro "só o modelo importa" + a tese demo→produção são a sacada que muda a cabeça do aluno. A prática "projete o harness" com os 3 guardrails é o ápice. Fecha o módulo de agentes e abre o de responsabilidade. 8 min pro quiz.
:::
