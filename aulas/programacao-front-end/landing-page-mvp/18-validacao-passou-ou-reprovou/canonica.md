---
titulo: "Validação: o MVP passou ou reprovou?"
tema: Métricas de validação
disciplina: programacao-front-end
serie: 2ª
prerequisitos: [Landing page publicada, Respostas do teste de corredor coletadas na Aula 17, Briefing com a hipótese e o número da Aula 08]
objetivos:
  - Diferenciar métrica de vaidade de métrica acionável
  - Explicar por que o critério de sucesso precisa ser definido antes da coleta
  - Ler as respostas do teste de corredor separando falha de mensagem de falha de produto
  - Decidir entre perseverar, pivotar ou encerrar, justificando com o dado coletado
trilha: landing-page-mvp
ordem: 18
slug: validacao-passou-ou-reprovou
modo_origem: tema
fontes: []
revisao: false
status: aprovada
versao: 2
atualizado_em: 2026-08-21
---

Na aula 08 vocês escreveram um número em um papel. Alguma coisa como "pelo menos 3 de cada 5". Naquele momento era só uma linha de formulário, meio chata de preencher. Hoje esse número volta com um poder desagradável: ele é a única coisa que impede vocês de olhar para cinco respostas e concluir, com toda a sinceridade do mundo, que deu certo. Porque é isso que a gente faz, e é involuntário — a gente lê o resultado procurando confirmação. A aula de hoje é sobre ler o que aconteceu de verdade, inclusive quando o que aconteceu foi a sua ideia levar um não.

## Objetivos

Ao final desta aula, você será capaz de:

- Distinguir uma métrica que **faz bem** de uma métrica que **serve para decidir**.
- Explicar por que o critério definido **depois** do resultado não vale nada.
- Ler as respostas do teste de corredor separando **falha de mensagem** de **falha de produto** — que exigem soluções opostas.
- Decidir, com o dado na mão: **perseverar, pivotar ou encerrar** — e justificar a decisão.

## Pré-requisitos

A landing page publicada, as cinco respostas do teste de corredor coletadas na aula 17, e o briefing da aula 08 com o número da hipótese. Sem o número original, a aula de hoje não tem contra o que comparar — e o trio que "não anotou" vai descobrir hoje por que isso importa.

## Desenvolvimento

### Números que fazem bem e números que servem para alguma coisa

Existem dois tipos de número, e eles se parecem muito no slide de apresentação.

O primeiro tipo sempre sobe e nunca dói: total de visitas, total de seguidores, total de curtidas, total de downloads. Repare no padrão — são todos **acumulados**, então só podem crescer. Isso é ótimo para o ânimo e péssimo para decidir, porque nenhum deles responde a única pergunta que importa: *o que eu faço amanhã com essa informação?*

:::conceito Métrica de vaidade
**Métrica de vaidade** é o número que só sobe, faz a equipe se sentir bem e não muda decisão nenhuma. Um aplicativo pode ter cem mil downloads e nenhum usuário que volte no dia seguinte. O número é verdadeiro — e é inútil, porque nenhum resultado dele levaria alguém a mudar de rumo.
:::

O segundo tipo é uma **proporção** e pode piorar: quantos dos que abriram entenderam, quantos dos que entenderam clicaram, quantos dos que se inscreveram voltaram na semana seguinte. Esses números têm denominador, e é o denominador que dá poder de reprovação.

| Métrica de vaidade | Métrica acionável |
|---|---|
| 200 pessoas visitaram a página | 2 de cada 10 visitantes clicaram no botão |
| 500 seguidores no perfil | 12 dos 500 seguidores entraram na lista |
| A página teve 1.000 acessos | 7 de 10 pessoas souberam dizer o que o produto faz |

:::importante A regra que separa as duas
Diante de qualquer número, faça uma pergunta: **existe um resultado desse número que me faria mudar de plano?** Se não existe, o número é decoração — pode ir para o pitch, mas não entra na decisão. Métrica que só pode dar boa notícia não é medição, é elogio.
:::

### O critério vem antes — e é por isso que dói

Vocês escreveram "3 de cada 5" antes de saber o que ia acontecer. Hoje, com o resultado na mão, vai aparecer a tentação — e ela é honesta, quase inocente. Deu 2 de 5, e alguém do trio observa, com razão: "mas uma das cinco pessoas era de outra turma, não é bem o nosso público". Talvez seja verdade. E mesmo assim está errado, porque a regra mudou **depois** de ver o placar.

:::atencao O critério que anda para trás
Alterar o critério depois do resultado é o erro mais comum e mais difícil de perceber, porque cada ajuste tem uma justificativa razoável: descartar uma resposta atípica, arredondar para cima, considerar que "quase clicou" conta. Nenhum desses movimentos parece desonesto isoladamente. Juntos, eles garantem que a hipótese nunca seja reprovada — e um teste que não pode reprovar nada não testou coisa nenhuma. Diagnóstico: se você está discutindo a régua depois de conhecer a medida, pare. Anote o resultado como ele veio, e discuta a régua para a **próxima** rodada.
:::

Isso não significa que o número original era sagrado. Significa que ele valia **para esta rodada**. Achou o critério mal calibrado? Ótimo — registre isso no relatório e defina outro para o próximo teste, antes de coletar.

### Cinco pessoas dizendo coisas diferentes

O teste de corredor deu duas informações por pessoa: **o que ela entendeu** e **se clicaria**. A ordem entre as duas é o coração da leitura, porque elas diagnosticam problemas opostos.

Se a pessoa não soube dizer o que o produto faz, a resposta dela sobre clicar **não vale nada** — ela estava chutando sobre uma coisa que não entendeu. Antes de qualquer conclusão sobre o produto, separe as respostas em dois montes: quem entendeu e quem não entendeu. Só o primeiro monte tem opinião sobre a ideia.

![Funil de duas etapas com cinco figuras entrando no topo. Na primeira etapa, a pergunta sobre o que o produto faz separa as figuras em dois grupos, e o grupo que não entendeu sai do funil por uma saída lateral marcada como falha de mensagem, sem chegar à segunda pergunta. Apenas o grupo que entendeu segue para a segunda etapa, onde a pergunta sobre clicar divide de novo, e é sobre esse grupo menor que a taxa é calculada.](img/entendeu-antes-de-clicaria.png)

```diagrama-progressivo
titulo: Lendo o resultado — o mesmo teste, quatro diagnósticos diferentes
camadas:
  - rotulo: Quase ninguém soube dizer o que era
    conteudo: "O problema está no texto, não no produto. A ideia não foi julgada, porque não chegou a ser compreendida. A correção é reescrever a headline e testar de novo com outras cinco pessoas. Trocar a ideia aqui seria abandonar algo que nunca foi avaliado."
  - rotulo: Entenderam, mas disseram que não é para elas
    conteudo: "A mensagem funcionou e o público está errado. A solução pode estar certíssima para outra pessoa. Aqui se muda a quem a página fala, não o que ela oferece — e às vezes basta trocar as cinco pessoas do teste para o resultado virar."
  - rotulo: Entenderam, é para elas, e mesmo assim não clicariam
    conteudo: "Este é o resultado mais valioso e o mais amargo. Significa que a dor existe mas é pequena demais, ou que a solução proposta não convence quem a sente. É a hora de perguntar o que essas pessoas fazem hoje para se virar — e por que continuar assim ainda parece melhor."
  - rotulo: Entenderam, é para elas, e clicariam
    conteudo: "A hipótese passou nesta rodada. Isso não prova que o produto vai dar certo — prova que a promessa convence cinco pessoas. É licença para construir o próximo pedaço e testar de novo, com mais gente e uma pergunta mais difícil."
  - rotulo: E quando encerrar de vez
    conteudo: "Encerrar não é o resultado de uma rodada ruim. É o que se faz quando várias rodadas seguidas, com públicos diferentes e textos diferentes, continuam dando não — sinal de que a dor não existe no tamanho que vocês imaginaram. Encerrar cedo devolve tempo para o próximo teste, e isso é vitória, não fracasso."
```

### Perseverar, pivotar ou encerrar

Essas são as três saídas, e a palavra do meio é a que costuma ser mal usada.

**Perseverar** é seguir com a aposta e aumentar a dificuldade do próximo teste. **Pivotar** é mudar **uma** peça — o público, ou a solução, ou o problema — mantendo o resto e o aprendizado. Pivô não é recomeçar do zero, não é trocar de assunto e definitivamente não é ter outra ideia porque a primeira deu trabalho: é uma correção de rota apoiada em uma informação nova. **Encerrar** é reconhecer, depois de mais de uma rodada, que a dor não sustenta o projeto.

:::dica O que isso vale fora daqui
Esse trio de decisões é literalmente o que uma equipe de produto faz toda semana, e a taxa que vocês calcularam tem nome no mercado: **taxa de conversão** — quantos, dos que viram, fizeram. É o número que aparece em toda reunião de produto e em todo relatório de marketing. E vale para o TCC do ano que vem: chegar na banca dizendo "testamos com cinco pessoas, três não entenderam, reescrevemos e na segunda rodada quatro entenderam" é uma resposta que muda o nível da defesa — porque mostra método, e método é o que separa projeto de palpite.
:::

:::curiosidade O número que engana com a verdade
Um aplicativo pode anunciar cem mil downloads no mesmo mês em que quase ninguém o abre pela segunda vez. Os dois fatos convivem, e o primeiro é verdadeiro. É por isso que empresas sérias olham para quantos **voltam**, e não para quantos chegaram: o download mede a propaganda, o retorno mede o produto. Quando você vir um número grande em uma apresentação, procure o denominador que não foi mostrado — ele costuma ser a informação de verdade.
:::

## Prática

**Relatório de validação (em trios, ~15 min).** Uma página, escrita à mão, entregue no fim da aula.

```
1. A HIPÓTESE (copiada do briefing, sem editar):
   Pelo menos ...... de cada 5 ................ iam ................

2. O RESULTADO CRU (das 5 pessoas):
   Entenderam o que o produto faz: ...... de 5
   Disseram que clicariam: ...... de 5   (contar SÓ entre quem entendeu)
   A frase mais repetida quando erraram o que era: ....................

3. VEREDITO — circule: (  ) PASSOU   (  ) REPROVOU

4. O DIAGNÓSTICO — circule um:
   ( ) falha de mensagem  ( ) público errado  ( ) dor pequena demais  ( ) passou

5. A DECISÃO — circule uma e justifique em 2 linhas com o dado do item 2:
   ( ) PERSEVERAR   ( ) PIVOTAR (o quê: ..........)   ( ) ENCERRAR
   Porque .............................................................

6. O PRÓXIMO TESTE — o que mudaria e qual seria o novo critério:
   ......................................................................
```

Duas regras: o item 1 é **copiado**, não reescrito; e o item 5 precisa citar o item 2 — justificativa que não menciona o dado é opinião com aparência de conclusão.

**Entrega:** o relatório completo. Ele é a base da apresentação do projeto e alimenta direto o pitch das próximas aulas.

## Avaliação

```quiz
- pergunta: Qual destes é uma métrica de vaidade?
  alternativas:
    - texto: "Dos 10 que abriram a página, 7 souberam dizer o que o produto faz"
    - texto: A página recebeu 1.000 acessos no primeiro mês
      correta: true
    - texto: "2 de cada 10 visitantes clicaram no botão de inscrição"
    - texto: "Dos 40 inscritos, 9 voltaram na semana seguinte"
  feedback: >
    Só uma delas é um total acumulado, que por definição nunca cai e não tem
    denominador. Nenhum resultado dela mudaria a decisão do trio. As outras três
    são proporções — podem piorar, e é justamente por isso que servem para decidir.
- pergunta: A hipótese era "3 de cada 5 clicariam" e o resultado foi 2 de 5. O trio propõe descartar uma das respostas por ser de alguém de outra turma, o que faria virar 2 de 4. O que está errado nisso?
  alternativas:
    - texto: Nada, faz sentido excluir quem não é do público-alvo
    - texto: "O critério está sendo alterado depois de conhecer o resultado, o que garante que a hipótese nunca seja reprovada"
      correta: true
    - texto: O erro é ter testado com apenas 5 pessoas
    - texto: "O certo seria arredondar 2 de 4 para 3 de 5"
  feedback: >
    A observação pode até ser correta, mas chegou tarde. Régua discutida depois da
    medida sempre acaba favorecendo quem mede. O caminho honesto é registrar o
    resultado como veio e definir o novo critério antes da próxima coleta.
- pergunta: Quatro das cinco pessoas não souberam dizer o que o produto faz. Qual é o diagnóstico?
  alternativas:
    - texto: A ideia foi reprovada e o trio deve escolher outro problema
    - texto: "A mensagem falhou; a ideia não chegou a ser avaliada, então o certo é reescrever a headline e testar de novo"
      correta: true
    - texto: O público estava errado e é preciso trocar de segmento
    - texto: A dor é pequena demais e o projeto deve ser encerrado
  feedback: >
    Quem não entendeu o que era não julgou a ideia — julgou um texto confuso.
    Abandonar o projeto aqui seria descartar algo que nunca foi testado. Falha de
    mensagem se corrige com escrita, não com mudança de rumo.
```

## Fechamento

O que ficou de hoje:

- **Métrica de vaidade sobe sempre e não decide nada.** Métrica acionável é proporção, tem denominador e pode dar má notícia.
- **O critério vale para a rodada em que foi definido.** Mudou depois de ver o placar, não testou nada.
- **Quem não entendeu não tem opinião sobre a ideia.** Separe os dois montes antes de concluir qualquer coisa.
- As saídas são três: **perseverar, pivotar ou encerrar** — e pivotar é mudar uma peça mantendo o aprendizado, não recomeçar do zero.
- **Reprovar cedo é resultado bom.** Custou uma aula descobrir o que teria custado um semestre.

**Para as próximas aulas:** com este relatório na mão, vocês têm o que quase nenhum projeto de escola tem — evidência. O pitch deixa de ser "achamos que seria útil" e passa a ser "testamos, deu isso, decidimos assim". É essa frase que a banca lembra.

:::roteiro
Comece cobrando o papel do briefing com o número. Trio que não tem vive hoje a lição na pele — deixe viver, sem resgatar, e nomeie em voz alta o que aconteceu: sem critério anterior, qualquer resultado vira sucesso. Vale mais que dez minutos de explicação.

Prepare-se para o clima. Vai ter trio decepcionado e vai ter trio querendo negociar o número. A postura da aula precisa ser dita explicitamente logo no início: **aqui, reprovar cedo vale nota igual a passar** — o que se avalia é a leitura do dado e a decisão, não o resultado. Sem isso a turma inteira maquia a coleta e a aula morre.

No diagrama, revele uma camada por vez e peça o diagnóstico antes de abrir. A camada 1 (falha de mensagem) é a que mais salva projeto: metade dos trios vai querer trocar de ideia quando o problema era a headline.

Circule na Prática caçando justificativa sem dado no item 5. Devolva sempre a mesma pergunta: "qual número do item 2 sustenta isso?".

Se algum trio tiver dado forte, leia em voz alta no fim — inclusive um caso de reprovação bem lida. Terminar a aula elogiando publicamente quem reprovou com honestidade é o que faz o método pegar na turma toda.
:::
