---
titulo: "Lean Canvas: a ideia como hipótese"
tema: Usabilidade e Design de Serviços
disciplina: analise-e-metodos-para-sistemas
serie: 1ª
prerequisitos: ["Da entrevista ao requisito: analisando o que os usuários disseram"]
objetivos:
  - Explicar para que serve o Lean Canvas e por que cada bloco é uma hipótese
  - Preencher os nove blocos do Lean Canvas na ordem recomendada, começando pelo problema
  - Escrever uma proposta única de valor e uma métrica-chave para uma ideia
  - Identificar a hipótese mais arriscada de um canvas e propor como testá-la
trilha: usabilidade-e-design-de-servicos
ordem: 95
slug: lean-canvas-a-ideia-como-hipotese
modo_origem: seed
fontes:
  - lake/analise-e-metodos-para-sistemas/seed-87-95/94-lean-canvas-e-blueprint.pptx
  - lake/analise-e-metodos-para-sistemas/seed-87-95/95-lean-canvas-e-blueprint-aplicacao.pptx
revisao: true
status: aprovada
versao: 1
atualizado_em: 2026-11-04
---

Todo mundo já teve uma "ideia de app milionária" no meio do intervalo. Um app que avisa quando a fila da cantina está pequena, um app para dividir a conta do lanche, um app para achar dupla para o trabalho. A ideia parece óbvia, perfeita, só falta programar. E é aí que mora a armadilha: a maioria das ideias não morre por falta de código, morre porque resolvia um problema que **ninguém tinha de verdade**, ou que já estava resolvido com um papel e uma caneta. Nas últimas aulas você aprendeu a descobrir problemas reais ouvindo pessoas. Hoje você vai aprender a colocar uma ideia de solução inteira numa página só, de um jeito que deixa claro **o que você sabe** e **o que você só está apostando**.

## Objetivos

Ao final desta aula, você será capaz de:

- Explicar para que serve o **Lean Canvas** e por que cada bloco é uma **hipótese**.
- Preencher os **nove blocos** na ordem recomendada, começando pelo **problema**.
- Escrever uma **proposta única de valor** e uma **métrica-chave** para uma ideia.
- Identificar a **hipótese mais arriscada** de um canvas e propor como testá-la.

## Pré-requisitos

Ter visto as **Aulas 93 e 94**: entrevistas, análise das falas e o caminho da necessidade ao requisito.

## Desenvolvimento

### Uma página de apostas

:::conceito Lean Canvas
É um quadro de **uma página, com nove blocos**, para organizar uma ideia de produto ou negócio: que problema resolve, para quem, por que alguém escolheria você, como vai chegar às pessoas, quanto custa, como se sustenta e como saber se está funcionando. Foi criado por **Ash Maurya** em 2010, adaptando o Business Model Canvas para quem está começando algo novo e cheio de incerteza.
:::

O ponto mais importante do Lean Canvas não está nos blocos, e sim na atitude: cada coisa que você escreve ali é uma **[[hipotese|hipótese]]**, um palpite que ainda precisa ser confirmado com pessoas reais. O canvas não promete que a ideia vai dar certo; ele mostra, numa página, **em que você está apostando**, para que você teste primeiro as apostas mais perigosas.

:::curiosidade Primo do Business Model Canvas
Se você já viu o **Business Model Canvas**, de Alexander Osterwalder, vai reconhecer o formato. Maurya trocou quatro blocos pensados para empresas já funcionando (parceiros, atividades, recursos e relacionamento) por quatro pensados para quem ainda está testando uma ideia: **problema**, **solução**, **métricas-chave** e **vantagem injusta**.
:::

### Os nove blocos, na ordem certa

A ordem de preenchimento importa: você começa pelas **pessoas e seus problemas** e só depois fala da sua solução.

| Ordem | Bloco | Pergunta que ele responde |
|---|---|---|
| 1 | **Problema** | Quais são os 1 a 3 problemas principais? Como as pessoas se viram hoje (as alternativas existentes)? |
| 2 | **Segmentos de clientes** | Quem tem esse problema? Quem vai usar primeiro (os primeiros adotantes)? |
| 3 | **Proposta única de valor** | Em uma frase, por que alguém escolheria a sua solução? |
| 4 | **Solução** | Quais as 3 funções mais simples que resolvem cada problema? |
| 5 | **Canais** | Como a solução chega até as pessoas? |
| 6 | **Fontes de receita** | Como a solução se paga ou se sustenta? |
| 7 | **Estrutura de custos** | Quanto custa criar e manter? |
| 8 | **Métricas-chave** | Que número mostra que está funcionando? |
| 9 | **Vantagem injusta** | O que você tem que é difícil de copiar ou comprar? |

```diagrama-progressivo
titulo: Preenchendo o canvas do app Prazo Certo
camadas:
  - rotulo: Problema
    conteudo: "Alunos perdem prazos de trabalhos porque as datas estão espalhadas (caderno, grupo da turma, quadro, plataforma). Alternativa existente: anotar no caderno e torcer para lembrar."
  - rotulo: Segmentos de clientes
    conteudo: Alunos do ensino médio técnico. Primeiros adotantes, os representantes de turma, que já juntam as datas para os colegas.
  - rotulo: Proposta única de valor
    conteudo: "\"Todos os seus prazos da escola num lugar só, com aviso antes de vencer.\""
  - rotulo: Solução
    conteudo: Lista única de prazos da turma, cadastro feito pelo representante e lembrete um dia antes.
  - rotulo: Canais, receitas e custos
    conteudo: Divulgação pelos representantes de turma. Projeto escolar sem cobrança, sustentado pela escola; custo de hospedagem baixo e manutenção feita pela própria turma de Desenvolvimento de Sistemas.
  - rotulo: Métrica-chave
    conteudo: Quantidade de trabalhos entregues fora do prazo por bimestre. Se o número não cair, o app não está resolvendo o problema, por mais downloads que tenha.
  - rotulo: Vantagem injusta
    conteudo: Feito por alunos da própria escola, com os representantes de turma já engajados. Uma empresa de fora não tem esse acesso.
```

:::importante Projeto da escola não tem receita?
Em sistemas escolares ou sociais, o bloco **Fontes de receita** pode parecer sem sentido. Leia-o como **sustentabilidade**: quem paga a hospedagem? quem mantém o sistema quando a turma se formar? Uma ideia sem resposta para isso morre no ano seguinte, mesmo que seja ótima.
:::

### Proposta de valor, métrica e vantagem

Três blocos costumam dar mais trabalho e merecem atenção especial. A **[[proposta-de-valor|proposta única de valor]]** é uma frase que um desconhecido entende em cinco segundos e que diz o **benefício**, não a tecnologia. "Aplicativo com banco de dados e notificações" é descrição técnica. "Seu lanche pronto quando você chegar ao balcão" é proposta de valor.

A **métrica-chave** é o número que mostra se o **problema** está sendo resolvido. Número de downloads quase nunca é: um app pode ter mil downloads e não mudar nada. Prefira medir o efeito no problema: tempo de fila, prazos perdidos, faltas a consultas.

A **vantagem injusta** é o que não se copia com dinheiro nem com uma semana de programação: acesso a um público, conhecimento de dentro, uma comunidade já formada. "Nosso app é melhor" não é vantagem injusta. Se você não tiver uma ainda, deixe o bloco em branco: é honesto, e é comum no começo.

:::atencao Erro comum: o problema é "falta do meu app"
O erro mais frequente no primeiro canvas é começar pela solução e escrever no bloco Problema algo como "não existe um app para pedir lanche". Isso não é problema, é a sua solução disfarçada. O problema é o que as pessoas vivem **hoje**, com ou sem app: "a fila da cantina toma metade do intervalo". Diagnóstico fácil: se o texto do bloco Problema menciona a sua solução, reescreva.
:::

### Do papel para o teste

Um canvas pronto é uma lista de apostas. O próximo passo é escolher a **mais arriscada**, aquela que, se estiver errada, derruba todo o resto, e testá-la do jeito mais barato possível. Quase sempre é o **Problema** ou o **Segmento**: "será que os alunos realmente perdem prazos por causa das datas espalhadas?". E você já sabe como testar isso: com as **entrevistas** das aulas 93 e 94, antes de escrever uma linha de código.

:::dica Na profissão
O Lean Canvas é usado por startups, incubadoras e programas de inovação para apresentar e discutir ideias rapidamente; muitos pitches começam com ele. No seu TCC, um Lean Canvas com cada bloco marcado como **evidência** (veio de entrevista ou observação) ou **hipótese** (ainda é palpite) mostra para a banca que o projeto foi pensado com método. É também a base natural para definir o [[mvp|MVP]].
:::

## Prática

**Atividade "canvas em 15 minutos" (grupos de 4, sem computador, ~15 min).** Cada grupo escolhe um problema da escola: **fila da cantina**, **achar dupla para trabalho**, **saber o cardápio da merenda**, **combinar carona para o curso** ou outro aprovado pelo professor.

1. **Monte o quadro (2 min).** Dobrem uma folha grande em nove partes e escrevam o nome de cada bloco.
2. **Preencha na ordem (8 min).** Sigam a ordem da tabela, de 1 a 9. Uma ou duas frases por bloco, no máximo.
3. **Marque as apostas (2 min).** Em cada bloco, escrevam **E** (temos evidência: alguém nos contou ou vimos acontecer) ou **H** (é hipótese).
4. **Escolha a mais arriscada (3 min).** Circulem a hipótese que, se estiver errada, derruba o canvas inteiro, e escrevam **uma pergunta de entrevista** (aberta, sobre o passado) para testá-la.

Cada grupo lê sua proposta única de valor. A turma responde: deu para entender em cinco segundos?

## Avaliação

```quiz
- pergunta: Por que se diz que cada bloco do Lean Canvas é uma hipótese?
  alternativas:
    - texto: Porque o canvas é preenchido com números inventados
    - texto: Porque cada bloco é um palpite que ainda precisa ser confirmado com pessoas reais
      correta: true
    - texto: Porque o canvas só pode ser usado em aulas de ciências
    - texto: Porque nenhum bloco do canvas pode mudar depois de preenchido
  feedback: >
    O canvas organiza apostas. Ele mostra o que você supõe, para que você teste
    primeiro o que é mais arriscado.
- pergunta: Qual é o bloco por onde se recomenda começar o Lean Canvas?
  alternativas:
    - texto: Solução
    - texto: Fontes de receita
    - texto: Problema
      correta: true
    - texto: Vantagem injusta
  feedback: >
    Começar pelo problema (e por quem o tem) evita que a equipe se apaixone pela
    solução antes de saber se ela resolve algo real.
- pergunta: Uma equipe escreveu no bloco Problema que não existe um app para pedir lanche na escola. O que está errado?
  alternativas:
    - texto: Nada, esse é um ótimo problema
    - texto: O texto descreve a solução disfarçada, e não o que as pessoas vivem hoje
      correta: true
    - texto: O problema deveria estar no bloco Canais
    - texto: O problema deveria citar a linguagem de programação
  feedback: >
    O problema é a dor atual, por exemplo a fila que toma metade do intervalo.
    "Falta do meu app" é a solução escrita no lugar errado.
- pergunta: Qual destas frases é a melhor proposta única de valor para um app de pedidos da cantina?
  alternativas:
    - texto: Aplicativo em React com banco de dados na nuvem
    - texto: O app mais moderno do Brasil
    - texto: Seu lanche pronto quando você chegar ao balcão
      correta: true
    - texto: Sistema de gerenciamento integrado de pedidos alimentícios
  feedback: >
    Proposta de valor diz o benefício em linguagem simples, não a tecnologia nem um
    elogio vago.
- pergunta: Para o app Prazo Certo, qual seria a melhor métrica-chave?
  alternativas:
    - texto: Número de downloads na loja
    - texto: Quantidade de trabalhos entregues fora do prazo por bimestre
      correta: true
    - texto: Quantidade de cores da interface
    - texto: Número de linhas de código do projeto
  feedback: >
    A métrica-chave mede se o problema está sendo resolvido. Downloads podem crescer
    sem que nenhum prazo deixe de ser perdido.
```

## Fechamento

Hoje você descobriu que:

- O **Lean Canvas** coloca uma ideia inteira numa página, em **nove blocos**, e cada bloco é uma **hipótese**.
- A ordem importa: **problema e segmentos primeiro**, solução depois.
- **Proposta de valor** diz o benefício, **métrica-chave** mede o efeito no problema e **vantagem injusta** é o que não se copia.
- O próximo passo de um canvas é **testar a aposta mais arriscada**, de preferência com entrevistas, antes de programar.

**Próxima aula:** o canvas diz **o que** você propõe e **por quê**. Falta ver **como** isso vai acontecer na prática, com todas as pessoas e sistemas envolvidos. Para isso existe o **Service Blueprint**.

:::roteiro
Abrir pedindo que dois ou três alunos contem sua "ideia de app milionária" em uma frase; anote no canto do quadro, porque elas voltam no fim como teste do erro comum (quase sempre o problema é a falta do app). No diagrama, peça que a turma proponha cada bloco do Prazo Certo antes de revelar; a camada da métrica-chave é a que mais surpreende. Diferenças em relação à origem: os decks 94 e 95 da SEED misturavam Lean Canvas e Blueprint nas duas aulas; aqui o canvas tem aula própria, com a ordem de preenchimento, a leitura de "fontes de receita" como sustentabilidade em projeto escolar e a marcação E/H de evidência e hipótese. O deck 94 trazia o exemplo de sistema de tarefas e lembretes, que virou o Prazo Certo. A cantina ficou fora de propósito: ela é o caso integrador da aula 97, então desaconselhe o grupo que escolher "fila da cantina" a se apegar demais, ou deixe e use o canvas dele como ponto de partida na aula 97.
:::
