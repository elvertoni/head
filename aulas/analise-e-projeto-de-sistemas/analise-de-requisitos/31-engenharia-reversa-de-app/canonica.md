---
titulo: Engenharia reversa — desmonte o app que você usa todo dia
tema: Levantamento e priorização de requisitos
disciplina: analise-e-projeto-de-sistemas
serie: 3ª
prerequisitos: [Ter um projeto de TCC em andamento]
objetivos:
  - Identificar os atores de um sistema a partir do produto pronto
  - Diferenciar requisito funcional de requisito não-funcional
  - Extrair regras de negócio que o aplicativo não mostra na tela
  - Priorizar requisitos com a Matriz GUT em vez de por achismo
trilha: analise-de-requisitos
ordem: 31
slug: engenharia-reversa-de-app
modo_origem: tema
fontes: []
revisao: false
status: rascunho
versao: 1
atualizado_em: 2026-08-18
---

Você pediu comida pelo celular essa semana. Abriu o app, escolheu, pagou, chegou. Do lado de fora, três toques. Do lado de dentro, alguém teve que decidir: **e se o restaurante fechar depois que o pedido entrou? E se o cupom for só de primeira compra e o cliente já comprou? E se o entregador aceitar e sumir?** Cada uma dessas perguntas foi respondida por uma pessoa numa reunião, virou uma regra e virou código. Hoje você vai fazer o caminho inverso: pegar um app pronto e desmontar até achar as decisões escondidas nele. É exatamente isso que um analista de sistemas faz — e é isso que falta no TCC de vocês.

## Objetivos

Ao final desta aula, você será capaz de:

- **Identificar** os atores de um sistema olhando para o produto pronto.
- **Diferenciar** requisito funcional (o que o sistema faz) de requisito não-funcional (o quão bem ele faz).
- **Extrair** regras de negócio que não aparecem em nenhuma tela.
- **Priorizar** requisitos com a Matriz GUT, defendendo a nota com argumento.

## Pré-requisitos

Ter um projeto de TCC em andamento e usar pelo menos um aplicativo com frequência. Sem computador hoje: só papel, caneta e o app que já está no seu bolso.

## Desenvolvimento

### Todo app é uma pilha de decisões que alguém tomou

Aplicativo bom parece óbvio. Essa é justamente a armadilha: o que parece óbvio some da nossa vista, e o analista iniciante passa direto por ele.

Faça o teste. Você abre o app de música, aperta play, toca. Simples? Então responda rápido: o que acontece se você apertar play com o celular sem internet? E se a assinatura venceu ontem à noite? E se você já está ouvindo em outro aparelho? E se a música saiu do catálogo no Brasil mas continua nos Estados Unidos, e você viajou?

Nenhuma dessas perguntas aparece na tela. Todas foram respondidas por alguém. **Engenharia reversa de requisitos** é o exercício de recuperar essas respostas a partir do produto pronto.

:::conceito Regra de negócio
Uma **regra de negócio** é uma decisão da área de negócio que o sistema é obrigado a respeitar — não é escolha do programador. *"Cupom de primeira compra só vale para quem nunca fez pedido"* é regra de negócio. *"O botão fica verde"* não é. A regra sobrevive à troca de linguagem, de banco e de time; o botão, não.
:::

:::exemplo A regra que aparece só quando dá errado
No app de transporte, você pede uma corrida e o motorista cancela. O app te devolve para a fila **na frente** de quem pediu depois de você. Isso não está escrito em lugar nenhum da interface — mas alguém decidiu, porque a alternativa (voltar pro fim da fila) fazia o usuário desinstalar o app. Regra de negócio quase sempre mora no caminho do erro, não no caminho feliz.
:::

### Atores: quem usa não é só o usuário

Peça a um aluno para listar quem usa o iFood e ele diz: "o cliente". Falta gente.

:::conceito Ator
**Ator** é qualquer papel que interage com o sistema — pessoa, setor ou até outro sistema. O que define o ator não é a pessoa, é o **papel**: a mesma pessoa pode ser cliente num momento e entregador em outro, e são dois atores diferentes porque querem coisas diferentes.
:::

No app de entrega existem, no mínimo: **cliente**, **restaurante**, **entregador**, **atendimento** (quem resolve o pedido que deu errado), **administrador** (quem cadastra taxa e comissão) — e o **sistema de pagamento**, que é outro sistema conversando com esse. Seis atores num app que "só entrega comida".

E aqui está o pulo do gato: **cada ator quer uma coisa diferente, e às vezes uma coisa contrária.** O cliente quer frete grátis. O entregador quer receber por entrega. O restaurante quer comissão baixa. A plataforma quer margem. Requisito nasce dessa briga, não de uma lista harmoniosa.

:::atencao Erro comum no TCC
Desenhar o sistema inteiro pensando só no ator principal. Aí, na banca, alguém pergunta *"e quem cadastra os produtos?"* e o grupo descobre na hora que não existe tela de administrador, nem login de administrador, nem nada. **Se um ator não tem tela, ele não existe no seu sistema** — e alguém vai perguntar por ele.
:::

### O que ele faz × o quão bem ele faz

Agora separe o que você descobriu em duas caixas.

:::conceito Requisito funcional e não-funcional
**Funcional** é o que o sistema **faz**: "o cliente pode acompanhar o pedido em tempo real". **Não-funcional** é a **qualidade** com que ele faz: desempenho, [[seguranca-da-informacao|segurança]], [[acessibilidade|acessibilidade]], [[alta-disponibilidade|disponibilidade]]. Regra prática: se dá pra desenhar uma tela pra ele, é funcional; se é um advérbio (rápido, seguro, sempre disponível), é não-funcional.
:::

| Requisito | Tipo | Por quê |
|---|---|---|
| Cliente acompanha o pedido no mapa | Funcional | Dá pra desenhar a tela |
| O mapa atualiza a posição a cada 5 segundos | Não-funcional | É a qualidade do "acompanhar" |
| Cliente paga com Pix | Funcional | É uma ação |
| O pagamento nunca guarda o número do cartão no aplicativo | Não-funcional | É segurança |
| App funciona em celular antigo com internet ruim | Não-funcional | É desempenho e alcance |

:::atencao O requisito não-funcional que não vale nada
*"O sistema deve ser rápido."* Rápido quanto? Pra quem? Em que rede? Esse requisito é impossível de testar, então ninguém consegue dizer se foi cumprido — e o que não dá pra testar não dá pra cobrar. Reescreva com **número**: *"a tela de busca responde em menos de 2 segundos numa conexão 4G comum"*. Agora existe um teste, e existe conversa.
:::

:::dica Como o analista arranca isso do cliente
Cliente nunca chega dizendo a regra de negócio — ele descreve o caminho feliz e acha que acabou. A ferramenta do analista é uma pergunta só, repetida: **"e se…?"**. E se o produto acabar? E se o cliente cancelar depois de pago? E se dois usuários pedirem a última unidade ao mesmo tempo? Cada "e se" que faz o cliente parar e pensar é uma regra de negócio que ele nunca teria contado sozinho.
:::

### Quando tudo é prioridade, nada é

Terminada a lista, todo grupo tem o mesmo problema: quarenta requisitos e seis meses de TCC. Aí vem a pergunta de sempre — *"por onde a gente começa?"* — e a resposta de sempre, que é péssima: *"pelo que a gente acha mais legal de fazer"*.

A [[matriz-gut|Matriz GUT]] existe para trocar achismo por argumento. Ela dá três notas de 1 a 5 pra cada item e multiplica:

```diagrama-progressivo
titulo: Matriz GUT — as três perguntas
camadas:
  - rotulo: Gravidade
    conteudo: "O tamanho do estrago se isso não for feito. Nota 5 quando o sistema perde o sentido sem esse item; nota 1 quando ninguém sente falta."
  - rotulo: Urgência
    conteudo: "O quanto o prazo aperta. Nota 5 quando outras coisas estão paradas esperando por isso; nota 1 quando pode ficar pro fim do ano."
  - rotulo: Tendência
    conteudo: "O que acontece se deixar quieto. Nota 5 quando o problema piora sozinho e vai ficando mais caro de resolver; nota 1 quando fica do mesmo tamanho pra sempre."
  - rotulo: A conta
    conteudo: "Multiplique as três notas — o resultado vai de 1 a 125. A lista ordenada por esse número é a sua ordem de trabalho, e cada posição tem três argumentos escritos por trás dela."
```

Exemplo com um sistema de agendamento de barbearia:

| Requisito | G | U | T | GUT | Leitura |
|---|---|---|---|---|---|
| Impedir dois agendamentos no mesmo horário | 5 | 5 | 5 | **125** | Sem isso o sistema não serve pra nada, e piora com mais clientes |
| Login do barbeiro | 5 | 4 | 3 | **60** | Ninguém agenda sem alguém do outro lado |
| Notificação por WhatsApp | 3 | 2 | 3 | **18** | Ajuda muito, mas dá pra viver sem |
| Tema escuro | 1 | 1 | 1 | **1** | O que todo grupo quer fazer na primeira semana |

:::importante O valor da GUT não é o número
A nota importa menos que a **conversa** que ela obriga. Quando alguém do grupo diz "tema escuro é urgência 5", a matriz força a pergunta *"urgente por quê?"* — e a discussão morre em dez segundos com todo mundo concordando. A GUT não decide por você; ela impede que a decisão seja tomada por quem fala mais alto.
:::

## Prática

**Atividade "consultoria relâmpago" (desplugada, ~18 min).** Turma dividida em grupos de 4. Cada grupo sorteia um app: **iFood**, **Spotify**, **Instagram**, **Uber**, **Pix do banco** ou **Mercado Livre**. Uma folha por grupo, dividida em quatro partes.

**Rodada 1 — atores (3 min).** Listem **todos** os papéis que interagem com o app. Meta: passar de quatro. Quem parar em dois ainda está enxergando só o próprio umbigo.

**Rodada 2 — regras escondidas (5 min).** Escrevam **cinco regras de negócio** que o app cumpre e que **não aparecem escritas em nenhuma tela**. Dica de caça: pensem no que dá errado (cancelamento, estoque acabando, cupom, pagamento recusado, dois usuários ao mesmo tempo).

**Rodada 3 — funcional × não-funcional (4 min).** Escrevam três requisitos funcionais e três não-funcionais. Cada não-funcional **precisa** ter um número — sem número, o requisito é anulado.

**Rodada 4 — GUT (3 min).** Peguem os três requisitos funcionais e deem as notas G, U e T. Multipliquem. Ordenem.

**Pitch e ataque (3 min por grupo, quantos couberem).** Cada grupo tem **90 segundos** para apresentar: o app, o requisito de GUT mais alta e por que a nota é essa. Os outros grupos têm 60 segundos para **atacar**: apontar um ator esquecido, uma regra inventada (que o app não cumpre de verdade) ou uma nota de GUT que não se sustenta. Vale ponto quem derruba um argumento com evidência — "abre o app aí e mostra".

**Levar pro TCC (dever de casa, 10 min):** repitam as quatro rodadas com o **sistema de vocês**. A tabela GUT que sair disso é literalmente o cronograma do próximo bimestre.

## Avaliação

```quiz
- pergunta: Qual destes é um requisito NÃO-funcional bem escrito?
  alternativas:
    - texto: O sistema deve ser rápido e seguro
    - texto: A tela de busca deve responder em menos de 2 segundos numa conexão 4G
      correta: true
    - texto: O cliente deve conseguir cancelar o pedido
    - texto: O administrador cadastra novos produtos
  feedback: >
    Não-funcional exige número testável. "Rápido e seguro" não dá pra medir, logo
    não dá pra cobrar. As outras duas opções são funcionais — dá pra desenhar tela.
- pergunta: "\"Cupom de primeira compra só vale para quem nunca fez pedido.\" O que é isso?"
  alternativas:
    - texto: Um requisito não-funcional, porque trata de segurança
    - texto: Uma regra de negócio
      correta: true
    - texto: Um ator do sistema
    - texto: Uma decisão de interface
  feedback: >
    É uma decisão da área de negócio que o sistema é obrigado a respeitar, e que
    sobrevive à troca de linguagem, de banco e de equipe.
- pergunta: Num app de entrega de comida, qual destes também é um ator?
  alternativas:
    - texto: Só o cliente, que é quem paga
    - texto: O restaurante, que recebe e aceita os pedidos
      correta: true
    - texto: O banco de dados de pedidos
    - texto: A tela de checkout
  feedback: >
    Ator é um papel que interage com o sistema. Restaurante, entregador,
    atendimento e administrador são atores; tela e banco são partes do sistema.
- pergunta: Na Matriz GUT, o que a nota de Tendência mede?
  alternativas:
    - texto: O quanto a equipe tem vontade de fazer o item
    - texto: O quanto o problema piora se for deixado para depois
      correta: true
    - texto: Quantos usuários pediram aquela função
    - texto: A dificuldade técnica de implementar
  feedback: >
    Tendência é a piora ao longo do tempo. É ela que distingue o problema que
    fica do mesmo tamanho daquele que fica mais caro a cada semana parada.
```

## Fechamento

Hoje você virou analista por 50 minutos:

- Todo app pronto é uma **pilha de decisões** que alguém tomou; engenharia reversa é recuperá-las.
- **Ator** é papel, não pessoa — e ator sem tela não existe no seu sistema.
- **Funcional** é o que faz; **não-funcional** é o quão bem faz, e só vale com número.
- A **Matriz GUT** não decide por você: ela obriga a defender a prioridade com argumento em vez de gosto pessoal.

**Próxima aula:** com os requisitos na mão e priorizados, falta amarrar cada um a um passo a passo verificável. Vamos escrever **casos de uso** — o roteiro do que o ator faz, o que o sistema responde e o que acontece quando o caminho dá errado.

:::roteiro
Aula de conversa e disputa — o professor fala pouco depois dos primeiros 15 minutos.

**Abertura (4 min).** Pergunte quem pediu comida por app essa semana. Escolha um aluno e faça a sequência de "e se": e se o restaurante fechar depois do pedido? e se o entregador sumir? e se o cupom já tiver sido usado? Deixe a turma chutar as respostas — elas variam, e a variação é o argumento: *alguém teve que decidir isso.*

**Atores (8 min).** Peça a lista no quadro e **não complete**. Deixe parar em "cliente" e "entregador", espere o silêncio e pergunte: "quem cadastra a taxa de entrega?". A cara de quem percebeu vale mais que a explicação. Só então feche com os seis atores.

**Funcional × não-funcional (8 min).** Escreva "o sistema deve ser rápido" no quadro e pergunte "como eu testo isso?". Deixe a turma reescrever com número — três tentativas ruins até sair uma boa é o esperado, não corrija cedo demais.

**GUT (7 min).** Use a tabela da barbearia, mas **apague a última linha** antes de mostrar. Pergunte onde entra "tema escuro" e deixe alguém defender nota alta — é a hora mais útil da aula. Só depois revele o 1×1×1.

**Prática (18 min).** Cronometre as rodadas em voz alta, é o que mantém o ritmo. Circule fazendo uma pergunta por mesa: "e se dois clientes pedirem a última unidade ao mesmo tempo?". Na fase de ataque, autorize explicitamente abrir o celular pra checar o app — a evidência é o que separa palpite de análise. Se a turma for grande, só três grupos apresentam e os outros entregam a folha.

**Se o tempo apertar:** corte a Rodada 3 e mande junto com o dever de casa. Não corte o ataque entre grupos — é ele que ensina a defender requisito.
:::
