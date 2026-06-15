---
titulo: Treino, Fine-tuning e Cutoff
tema: Fundamentos de IA
disciplina: inteligencia-artificial
serie: Extra
prerequisitos: [O que é um LLM]
objetivos:
  - Distinguir o pré-treino do fine-tuning
  - Explicar o que é o cutoff e por que o modelo não sabe o que é recente
  - Reconhecer que o LLM não aprende sozinho com as conversas do dia a dia
trilha: fundamentos-de-ia
ordem: 12
modo_origem: tema
fontes: []
revisao: false
status: aprovada
versao: 1
atualizado_em: 2026-06-15
---

Pergunta pro ChatGPT o placar do jogo de ontem. Ele provavelmente vai dizer que não sabe — ou, pior, vai **inventar** um. Estranho, né? Uma máquina que sabe explicar física quântica não sabe um resultado de futebol de ontem. A explicação tem nome e está no coração desta aula: **cutoff**, a data em que o conhecimento do modelo "congelou". Pra entender isso, você precisa saber como um [[llm]] é construído — e descobrir que ele **não** fica mais esperto sozinho conversando com você. Vamos abrir o calendário de vida de um modelo.

## Objetivos

Ao final desta aula, você será capaz de:

- Distinguir o **pré-treino** do **fine-tuning**.
- Explicar o que é o **cutoff** e por que o modelo não sabe o que é recente.
- Reconhecer que o LLM **não aprende sozinho** com as conversas do dia a dia.

## Pré-requisitos

Ter visto a **Aula 09** (o que é um LLM).

## Desenvolvimento

### Duas fases de construção

Um LLM não nasce pronto numa tacada. Ele passa por fases.

:::conceito Pré-treino e fine-tuning
O **pré-treino** é a fase pesada: o modelo lê uma quantidade gigantesca de texto e aprende os padrões gerais da linguagem. Custa meses e milhões. Depois vem o **fine-tuning** ("ajuste fino"): um treino menor e direcionado, que molda o modelo para uma tarefa ou estilo específico — ser um bom assistente, seguir instruções, evitar respostas ofensivas. Pré-treino dá o conhecimento amplo; fine-tuning dá o "jeito" e a especialização.

:::

### O conhecimento congela: cutoff

Aqui está a peça que explica o jogo de ontem.

:::conceito Cutoff (data de corte)
É a **data até onde vão os dados de treino** do modelo. Tudo que aconteceu **depois** do cutoff o modelo simplesmente não conhece — porque não estava nos textos com que ele treinou. É como um livro impresso: ele só contém o que se sabia até o dia em que foi para a gráfica. Por isso o modelo "não sabe" o placar de ontem.

:::

```diagrama-progressivo
titulo: A linha do tempo de um LLM
camadas:
  - rotulo: 1. Coleta de dados (até o cutoff)
    conteudo: Junta-se uma montanha de texto, mas só até certa data. Essa data é o cutoff - o limite do conhecimento do modelo.
  - rotulo: 2. Pré-treino
    conteudo: O modelo estuda esses textos por meses e aprende os padrões gerais da linguagem e do mundo até ali.
  - rotulo: 3. Fine-tuning
    conteudo: Um ajuste direcionado molda o comportamento - virar assistente útil, seguir instruções, ser seguro.
  - rotulo: 4. Uso (depois do cutoff)
    conteudo: Você conversa com o modelo. Mas o conhecimento dele parou no cutoff: eventos posteriores são desconhecidos, a menos que você forneça a informação.
```

:::atencao Erro comum
"O LLM aprende com as nossas conversas e fica mais esperto sozinho em tempo real." Não. Por padrão, conversar com o modelo **não muda** o que ele sabe — o conhecimento foi fixado no treino e congelado no cutoff. Para o modelo "saber" algo novo, é preciso **retreiná-lo** (caro e demorado) ou **fornecer a informação na hora** (no próprio prompt, ou via técnicas como o [[rag]]). A conversa de hoje não vira conhecimento permanente dele.

:::

:::dica É por isso que existe RAG e busca
Essa limitação é tão importante que criou áreas inteiras. Como dar informação **fresca** a um modelo que parou no cutoff? Conectando-o a uma busca na web ou injetando documentos atualizados no contexto — exatamente o [[rag]] que você verá na Aula 16. Entender o cutoff agora é entender **por que** essas soluções existem. Em 2026 os modelos mudam de versão a todo momento, justamente para empurrar o cutoff para frente — mas sempre há um limite.

:::

## Prática

**Atividade "achando o limite" (em duplas, sem computador, ~15 min).**

1. **Listem 3 perguntas** que um LLM responderia bem (conhecimento estável: "o que é fotossíntese?", "quem foi Santos Dumont?").
2. **Listem 3 perguntas** que provavelmente esbarrariam no cutoff (algo recente: o resultado de um campeonato deste mês, a última atualização de um app, a notícia de ontem).
3. Para as do grupo 2, discutam: o que seria **mais perigoso** — o modelo dizer "não sei" ou **inventar** uma resposta confiante? Por quê?
4. **Solução:** se vocês *precisassem* que o modelo respondesse as do grupo 2, o que dariam a ele? (resposta esperada: a informação atualizada, no próprio prompt.)

Socializem: como saber se uma pergunta caiu "depois do cutoff"? Que sinais de resposta levantam suspeita?

## Avaliação

```quiz
- pergunta: Qual a diferença entre pré-treino e fine-tuning?
  alternativas:
    - texto: São a mesma fase com nomes diferentes
    - texto: Pré-treino dá o conhecimento amplo da linguagem; fine-tuning ajusta o modelo para uma tarefa ou estilo
      correta: true
    - texto: Fine-tuning vem antes do pré-treino
    - texto: Pré-treino é feito pelo usuário no chat
  feedback: >
    Primeiro o pré-treino (pesado, conhecimento geral), depois o fine-tuning (ajuste
    direcionado: virar assistente, seguir instruções, ser seguro).
- pergunta: O que é o cutoff de um modelo?
  alternativas:
    - texto: O preço para usar o modelo
    - texto: A data até onde vão os dados de treino — o limite do que ele conhece
      correta: true
    - texto: O tempo que ele leva para responder
    - texto: O número máximo de usuários
  feedback: >
    Cutoff é a data de corte do conhecimento. Eventos posteriores não estavam no
    treino, então o modelo não os conhece.
- pergunta: Conversar com um LLM faz ele aprender e ficar mais esperto sozinho, em tempo real?
  alternativas:
    - texto: Sim, ele aprende com cada conversa automaticamente
    - texto: Não — por padrão o conhecimento é fixado no treino; é preciso retreinar ou fornecer a informação na hora
      correta: true
    - texto: Sim, mas só aos domingos
    - texto: Não, ele nunca pode receber informação nova
  feedback: >
    A conversa não vira conhecimento permanente. Para saber algo novo, retreina-se o
    modelo ou fornece-se a informação no contexto (ex.: RAG).
```

## Fechamento

Hoje você descobriu que:

- Um LLM é construído em fases: **pré-treino** (conhecimento amplo) e **[[fine-tuning]]** (ajuste de tarefa/estilo).
- O **[[cutoff]]** é a data em que o conhecimento do modelo **congela** — por isso ele não sabe o que é recente.
- O LLM **não aprende sozinho** com as conversas; precisa ser retreinado ou receber a informação na hora.
- Essa limitação é o motivo de existir **busca** e **[[rag|RAG]]** (Aula 16).

**Próxima aula:** fechamos o módulo mostrando que a IA hoje não é só texto — ela **vê e ouve**. Aula 13: **multimodalidade**.

:::roteiro
Abrir com o placar do jogo de ontem — concreto e surpreendente (a máquina sábia que não sabe futebol recente). Pré-treino vs fine-tuning rápido; o foco é o cutoff. O erro "aprende com nossas conversas" é crucial e muito comum — derrube com clareza (conversa não retreina). A `:::dica` planta o RAG (aula 16) como solução do cutoff. Na prática, a discussão "dizer não sei vs inventar" prepara alucinações (23). Cuidado ao citar versões/datas específicas — conteúdo verificado na web (2026), mas mantido version-agnóstico. 8 min pro quiz.
:::
