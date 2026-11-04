---
titulo: "Avaliação heurística na prática"
tema: Usabilidade e Design de Serviços
disciplina: analise-e-metodos-para-sistemas
serie: 1ª
prerequisitos: ["Usabilidade e as heurísticas de Nielsen (1 a 5)", "Heurísticas de Nielsen (6 a 10) e a boa mensagem de erro"]
objetivos:
  - Descrever as etapas de uma avaliação heurística
  - Registrar um problema de usabilidade com tela, problema, heurística, evidência, gravidade e recomendação
  - Classificar a gravidade de um problema de 0 a 4
  - Explicar por que a avaliação usa vários avaliadores e não substitui o teste com usuários
trilha: usabilidade-e-design-de-servicos
ordem: 3
slug: avaliacao-heuristica-na-pratica
modo_origem: seed
fontes:
  - lake/analise-e-metodos-para-sistemas/seed-87-95/88-heuristicas-de-usabilidade-avancado.pptx
  - lake/analise-e-metodos-para-sistemas/seed-87-95/87-heuristicas-de-nielsen-introducao.pptx
revisao: true
status: aprovada
versao: 1
atualizado_em: 2026-11-04
---

"Essa tela tá ruim." Todo mundo já disse isso de algum app, e todo mundo já ouviu de volta: "ruim por quê?". Aí a conversa trava, porque "ruim" é opinião, e opinião contra opinião ninguém ganha. Nas duas últimas aulas você ganhou dez lentes para olhar uma interface. Hoje você vai usá-las do jeito que um profissional usa: transformando "essa tela tá ruim" num registro que aponta o problema, prova com evidência, diz o quanto ele é grave e propõe o conserto. É a diferença entre reclamar e consertar.

## Objetivos

Ao final desta aula, você será capaz de:

- Descrever as **etapas** de uma avaliação heurística.
- **Registrar** um problema de usabilidade com tela, problema, heurística, evidência, gravidade e recomendação.
- Classificar a **gravidade** de um problema de 0 a 4.
- Explicar por que a avaliação usa **vários avaliadores** e por que **não substitui** o teste com usuários.

## Pré-requisitos

Ter visto as **Aulas 01 e 02**: as dez heurísticas de Nielsen. Deixe a lista à mão, no caderno, porque hoje ela vira ferramenta de trabalho.

## Desenvolvimento

### O que é uma avaliação heurística

:::conceito Avaliação heurística
É um método de inspeção em que avaliadores percorrem uma interface comparando cada tela com uma lista de heurísticas e **registram cada violação encontrada**. É rápida, barata e pode ser feita até num protótipo de papel, antes de existir uma linha de código.
:::

Ela costuma seguir quatro etapas:

1. **Preparar.** Definir o que será avaliado (o app inteiro? só o fluxo de reserva?) e quais tarefas o avaliador vai simular, como "reservar um livro" ou "renovar um empréstimo".
2. **Avaliar sozinho.** Cada avaliador percorre as telas **individualmente**, de preferência duas vezes: uma para entender o fluxo, outra para caçar problemas.
3. **Consolidar.** Os avaliadores juntam as listas, eliminam repetições e discutem divergências.
4. **Classificar e recomendar.** O grupo dá uma gravidade a cada problema e propõe correções, começando pelos mais graves.

:::importante Por que mais de um avaliador
Os estudos do próprio Nielsen mostram que **uma pessoa sozinha costuma encontrar só cerca de um terço** dos problemas de uma interface, e que **três a cinco avaliadores** juntos já encontram a maior parte. Cada um tem um "ponto cego" diferente. Por isso a etapa 2 é individual: se todos avaliam juntos desde o começo, a primeira opinião contamina as outras e o grupo enxerga como uma pessoa só.
:::

### Da opinião ao registro

O coração do método é o registro. Ele segue sempre a mesma sequência:

**Tela → Problema → Heurística → Evidência → Gravidade → Recomendação**

```diagrama-progressivo
titulo: Transformando "essa tela tá ruim" num registro profissional
camadas:
  - rotulo: A opinião
    conteudo: "\"A tela de cadastro tá ruim.\" Ninguém consegue agir a partir disso. Ruim onde? Para quem? Quanto?"
  - rotulo: Tela e problema
    conteudo: "Tela de cadastro do aluno. O botão Excluir tem o mesmo tamanho e a mesma cor do botão Salvar e fica colado nele."
  - rotulo: Heurística violada
    conteudo: Prevenção de erros (heurística 5). Também toca em controle e liberdade (3), porque não há desfazer.
  - rotulo: Evidência
    conteudo: Ao simular a tarefa de salvar, o toque no botão vizinho apaga o cadastro na hora, sem confirmação.
  - rotulo: Gravidade
    conteudo: "Nota 3, problema grave: acontece com facilidade e faz a pessoa perder todos os dados digitados."
  - rotulo: Recomendação
    conteudo: Afastar o Excluir, dar a ele cor de ação perigosa e pedir confirmação antes de apagar. Isso é algo que a equipe consegue fazer amanhã.
```

:::atencao Erro comum: registrar gosto em vez de problema
Na primeira avaliação, metade dos registros costuma ser "não gostei da fonte", "essa cor é estranha", "eu faria diferente". Isso não é problema de usabilidade, é preferência. O teste que separa as duas coisas: **dá para apontar qual heurística foi violada e mostrar a evidência numa tarefa?** Se não dá, o registro sai da lista (ou recebe gravidade 0).
:::

### Quanto o problema pesa: a escala de gravidade

Nem todo problema merece a mesma pressa. Nielsen propôs uma escala de 0 a 4:

| Nota | Significado | O que fazer |
|---|---|---|
| **0** | Não é problema de usabilidade | Descartar |
| **1** | Cosmético | Corrigir se sobrar tempo |
| **2** | Menor | Corrigir com prioridade baixa |
| **3** | Grave | Prioridade alta |
| **4** | Catástrofe | Corrigir antes de lançar |

Para dar a nota, pese três perguntas: **com que frequência** o problema aparece? **Qual o estrago** quando aparece? A pessoa **consegue contornar** depois que aprende, ou tropeça sempre?

### Os limites do método

A avaliação heurística encontra muito problema com pouco custo, mas quem avalia **não é o usuário real**. Ela não descobre, por exemplo, que os alunos nem usam a função que você caprichou, ou que eles abrem o app no ônibus, com uma mão só. Por isso ela vem **antes** do teste com usuários, para limpar os problemas óbvios, e não **no lugar** dele.

:::dica Isso é trabalho de verdade
Em empresas de software, o relatório de avaliação heurística vira uma lista de tarefas para o time, muitas vezes como *issues* no GitHub ou cartões no quadro Kanban, cada um com o registro completo e a gravidade como prioridade. No seu TCC, uma avaliação heurística do próprio protótipo, feita por colegas de outro grupo, é um argumento forte na banca: mostra que a interface foi testada com método, não no "achômetro".
:::

## Prática

**Laboratório "auditoria do BiblioTec" (grupos de 3, sem computador, ~15 min).**

Vocês são a equipe de UX contratada para avaliar a tela abaixo, do app da biblioteca da escola.

```text
┌───────────────────────────────────────┐
│ BiblioTec                         [☰] │
│ ███ BANNER: Semana do Livro! ███████  │
│ ███ BANNER: Concurso de Poesia! ████  │
│ ███ BANNER: Baixe nosso outro app ██  │
│                                       │
│ Buscar livro: [ digite o ISBN ____ ]  │
│                                       │
│ Meus empréstimos                      │
│  Dom Casmurro   vence 2026-11-12T00Z  │
│     [Renovar] [Devolver] [Cancelar]   │
│  O Hobbit       vence 2026-11-09T00Z  │
│     [Renovar] [Devolver] [Cancelar]   │
└───────────────────────────────────────┘
```

O que acontece quando a pessoa usa:

- Ao tocar em **Renovar**, a tela não muda e nenhuma mensagem aparece.
- **Cancelar** apaga a reserva na hora, sem confirmação e sem desfazer.
- Se a renovação falha, aparece só `ERR_RENOV_409`.
- Na tela de detalhes do livro não existe botão de voltar.
- Nesta tela o ❤ reserva o livro; na tela de busca, o ❤ só favorita.

**Etapas:**

1. **Sozinho (5 min):** cada integrante lista os problemas que encontrar, sem conversar.
2. **Em grupo (5 min):** juntem as listas, tirem repetições e montem a tabela *Tela · Problema · Heurística · Evidência · Gravidade · Recomendação*.
3. **Prioridade (5 min):** escolham os **três problemas mais graves** e escrevam a recomendação de cada um como se fosse para o time de desenvolvimento.

No fim, comparem: quantos problemas cada pessoa achou sozinha e quantos o grupo achou junto?

## Avaliação

```quiz
- pergunta: Por que, numa avaliação heurística, cada avaliador começa trabalhando sozinho?
  alternativas:
    - texto: Para terminar mais rápido
    - texto: Para que a opinião de um não contamine os outros e cada um encontre problemas diferentes
      correta: true
    - texto: Porque o método proíbe discussão em grupo
    - texto: Para ver quem é o melhor avaliador da equipe
  feedback: >
    Cada pessoa tem pontos cegos diferentes. Avaliando sozinhas primeiro e
    consolidando depois, a equipe soma descobertas em vez de repetir a primeira opinião.
- pergunta: Qual destes registros está no formato de uma avaliação heurística?
  alternativas:
    - texto: A tela inicial é feia e eu faria tudo diferente
    - texto: "Tela de login. Problema: a mensagem \"Erro 401\" não explica nada. Heurística 9. Evidência: com senha errada, só aparece o código. Gravidade 3. Recomendação: dizer que a senha está incorreta e oferecer recuperação."
      correta: true
    - texto: O app precisa ser refeito do zero com outra linguagem
    - texto: Achei a fonte pequena e a cor estranha
  feedback: >
    Um registro útil aponta tela, problema, heurística, evidência, gravidade e
    recomendação. Os outros são opinião ou gosto.
- pergunta: Por causa de uma falha de tela, nenhum aluno consegue renovar empréstimos pelo app. Que gravidade esse problema merece?
  alternativas:
    - texto: 1, cosmético
    - texto: 2, menor
    - texto: 3, grave
    - texto: 4, catástrofe
      correta: true
  feedback: >
    Afeta todo mundo, impede uma tarefa principal e não tem contorno. É problema
    para corrigir antes de lançar.
- pergunta: Uma equipe fez avaliação heurística com cinco avaliadores. Ela pode dispensar o teste com usuários reais?
  alternativas:
    - texto: Sim, cinco avaliadores encontram todos os problemas
    - texto: Sim, porque as heurísticas são leis de usabilidade
    - texto: Não, porque os avaliadores não são os usuários reais e não descobrem tudo sobre o contexto de uso
      correta: true
    - texto: Não, porque avaliação heurística só funciona com código pronto
  feedback: >
    A avaliação limpa os problemas óbvios a baixo custo, mas quem avalia não vive
    a rotina do usuário. Ela vem antes do teste, não no lugar dele.
- pergunta: Num app, "Excluir projeto" fica ao lado de "Editar projeto", igual a ele, apaga sem confirmar e não tem desfazer. Qual heurística está mais diretamente ligada ao problema principal?
  alternativas:
    - texto: Correspondência entre o sistema e o mundo real
    - texto: Ajuda e documentação
    - texto: Prevenção de erros
      correta: true
    - texto: Flexibilidade e eficiência de uso
  feedback: >
    O problema central é deixar a ação destrutiva acidental acontecer. A falta de
    desfazer também toca em controle e liberdade: um problema pode violar mais de uma.
```

## Fechamento

Hoje você descobriu que:

- A **avaliação heurística** tem quatro etapas: preparar, avaliar sozinho, consolidar, classificar e recomendar.
- Um bom registro segue **Tela → Problema → Heurística → Evidência → Gravidade → Recomendação**, e é isso que separa análise de opinião.
- A **gravidade** de 0 a 4 decide o que se corrige primeiro, pesando frequência, estrago e persistência.
- **Vários avaliadores** encontram muito mais do que um, e o método **não substitui** o teste com usuários reais.

**Próxima aula:** as heurísticas avaliam a tela; agora você vai conhecer **leis** que explicam o comportamento humano por trás dela: por que muitas opções travam a decisão e por que um botão pequeno demais vira erro.

:::roteiro
Abrir escrevendo "essa tela tá ruim" no quadro e perguntar "e agora, o que o programador faz com isso?". O diagrama é o modelo da prática: revele camada por camada pedindo que a turma preveja o próximo campo. A tabela de gravidade cabe numa olhada; não se demore. O ponto central da aula é a prática; se o tempo apertar, encurte a seção dos limites para uma frase oral. Gabarito do BiblioTec (aceite outros bem fundamentados): banners (8, gravidade 2), busca só por ISBN (2 e 6, gravidade 3), data em formato técnico (2, gravidade 2), Renovar sem retorno (1, gravidade 3), Cancelar sem confirmação nem desfazer (5 e 3, gravidade 3 ou 4), ERR_RENOV_409 (9, gravidade 3), sem voltar nos detalhes (3, gravidade 2), coração com dois significados (4, gravidade 2), três botões iguais lado a lado (5, gravidade 3). No fechamento da prática, pergunte quem achou mais de 5 problemas sozinho: quase ninguém, e o grupo quase sempre passa de 7. É a demonstração viva do porquê de vários avaliadores. A sequência Tela → problema → heurística → evidência → impacto → recomendação vem do deck 88 da SEED; a escala 0–4 e o número de avaliadores foram acrescentados aqui.
:::
