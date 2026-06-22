---
titulo: Nivelamento - Convertendo Decimal para Binário
tema: Conversão de base decimal para binária
disciplina: introducao-a-computacao
serie: 1ª
prerequisitos: [Como os Dados Viram Binário - Parte 1]
objetivos:
  - Aplicar o método das divisões sucessivas por 2
  - Converter um número decimal em sua representação binária
  - Conferir a conversão somando potências de dois
trilha: nivelamento-e-retomada
ordem: 1
slug: nivelamento-conversao-decimal-para-binario
modo_origem: seed
fontes:
  - lake/introducao-a-computacao/AULA NIVELAMENTO 01_INTRODUÇÃO A COMPUTAÇÃO.pptx
revisao: true
status: aprovada
versao: 1
atualizado_em: 2026-06-21
---

Você já sabe **por que** o computador usa binário (Aula 33): os circuitos têm dois estados, ligado e desligado, 1 e 0. Mas saber o porquê não é o mesmo que saber **fazer**. Esta é uma aula de nivelamento, de pôr a mão na massa: pegar um número que você usa todo dia, como 26, e transformá-lo na fileira de zeros e uns que o computador entende. Não tem mágica nem decoreba — tem um método simples, de dividir por 2 várias vezes, que sempre funciona. No fim da aula, você converte qualquer número decimal em binário no papel, sozinho.

## Objetivos

Ao final desta aula, você será capaz de:

- Aplicar o método das **divisões sucessivas** por 2.
- Converter um **número decimal** na sua representação **binária**.
- **Conferir** a conversão somando potências de dois.

## Pré-requisitos

Ter visto a **Aula 33** (bit, byte, e a ideia de que inteiros são guardados em base 2). Saber fazer **divisão com resto** já basta para o resto.

## Desenvolvimento

### Relembrando: o que é base 2

Você conta em **base 10**: dez dígitos (0 a 9), e cada casa vale dez vezes mais que a anterior (unidade, dezena, centena). O computador conta em **base 2**: só dois dígitos (0 e 1), e cada casa vale **o dobro** da anterior.

:::conceito Número binário
É a representação de **qualquer** número usando apenas dois dígitos: **0 e 1**. Cada posição, da direita para a esquerda, vale o dobro da anterior: 1, 2, 4, 8, 16, 32... Com essas potências de dois dá para montar qualquer número.
:::

### O método: divide por 2 e anota o resto

Existe uma receita infalível para converter de decimal para binário. Ela usa só divisão por 2 e a anotação dos **restos**.

:::importante O passo a passo da conversão
1. Divida o número por **2** e anote o **resto** (será 0 ou 1).
2. Pegue o **resultado inteiro** da divisão e divida por 2 de novo; anote o resto.
3. Continue dividindo e anotando os restos **até o resultado chegar a 0**.
4. Escreva os restos na **ordem reversa** — do **último** para o **primeiro**.
Essa sequência de restos, de trás para frente, é o número em binário.
:::

A parte que mais confunde é a **ordem reversa**: o último resto que você anotou é o **primeiro** dígito do binário. Guarde isso.

### Fazendo junto: o número 26

Vamos converter **26** passo a passo.

:::exemplo
| Divisão | Resultado | Resto |
|---|---|---|
| 26 ÷ 2 | 13 | **0** |
| 13 ÷ 2 | 6 | **1** |
| 6 ÷ 2 | 3 | **0** |
| 3 ÷ 2 | 1 | **1** |
| 1 ÷ 2 | 0 | **1** |

Os restos, na ordem em que saíram, foram: 0, 1, 0, 1, 1. Agora leia de **baixo para cima** (ordem reversa): **11010**.

Então **26 em binário é 11010**.
:::

### A prova real: somando potências de dois

Como ter certeza de que `11010` é mesmo 26? Faça o caminho de volta, somando as potências de dois das casas que têm **1** (a técnica da Aula 33).

:::exemplo
| Posição vale | 16 | 8 | 4 | 2 | 1 |
|---|---|---|---|---|---|
| Dígito (11010) | 1 | 1 | 0 | 1 | 0 |
| Conta | 16 | 8 | 0 | 2 | 0 |

Some onde há 1: 16 + 8 + 2 = **26**. Bateu! Sempre que terminar uma conversão, faça essa prova real: ela pega qualquer erro de conta na hora.
:::

:::atencao Erro comum
Escrever os restos na ordem em que saíram, **sem inverter**. Se você anotar 26 como `01011` (ordem direta) em vez de `11010` (ordem reversa), o número fica completamente errado. O resto da **última** divisão é o dígito mais à **esquerda**. Quando errar uma conversão, o primeiro lugar para olhar é se você inverteu a ordem.
:::

:::dica Por que essa habilidade vale a pena
Converter entre bases parece "conta de escola", mas é o tipo de fundamento que aparece o tempo todo: ao trabalhar com cores (que são números), endereços de rede, permissões de arquivos e depuração de dados. Quem tem essa conversão na ponta do lápis lê o "idioma da máquina" com naturalidade — e isso dá confiança em tudo que vem depois na carreira de desenvolvimento.
:::

## Prática

**Atividade "conversores de plantão" (desplugada, 12 a 15 min).** Só papel, lápis e o método.

**Rodada 1 — aquecimento (individual):** converta para binário, usando as divisões sucessivas, e faça a prova real de cada um:

- 2 → ?
- 5 → ?
- 10 → ?

**Rodada 2 — o seu número (individual):** pegue os **três primeiros dígitos do seu CPF** (ou três números que o professor ditar) e converta cada um para binário. Confira com a prova real.

**Rodada 3 — caça ao erro (em duplas):** troque suas conversões com um colega e confira as dele somando as potências de dois. Achou um número que não bate? Descubra **juntos** onde foi o deslize — quase sempre é a ordem invertida ou um resto trocado.

Fechem com a discussão:

- O resultado da divisão sempre chega a 0? Por quê isso garante que o método termina?
- O que o **último** resto representa no número binário final?

**Extensão opcional no VSCode:** em Python, rode `print(bin(26))`. Você verá `0b11010`. Em 2 linhas, explique o que o `0b` indica e por que os dígitos batem com a sua conversão feita à mão.

## Avaliação

```quiz
- pergunta: No método das divisões sucessivas, como se monta o número binário a partir dos restos?
  alternativas:
    - texto: Escrevendo os restos na mesma ordem em que saíram
    - texto: Escrevendo os restos na ordem reversa, do último para o primeiro
      correta: true
    - texto: Somando todos os restos
    - texto: Multiplicando os restos por 2
  feedback: >
    Os restos são lidos de trás para frente: o resto da última divisão é o dígito
    mais à esquerda. Inverter a ordem é o passo que mais gera erro.
- pergunta: Qual é a representação binária do número decimal 10?
  alternativas:
    - texto: 1010
      correta: true
    - texto: 0101
    - texto: 1111
    - texto: 1001
  feedback: >
    10 ÷ 2 = 5 resto 0; 5 ÷ 2 = 2 resto 1; 2 ÷ 2 = 1 resto 0; 1 ÷ 2 = 0 resto 1.
    Restos em ordem reversa: 1010. Prova real: 8 + 2 = 10.
- pergunta: Como conferir se a conversão para binário está correta?
  alternativas:
    - texto: Contando quantos dígitos tem o resultado
    - texto: Somando as potências de dois das posições que têm o dígito 1
      correta: true
    - texto: Multiplicando o binário por 10
    - texto: Não há como conferir
  feedback: >
    A prova real é voltar do binário para o decimal: some os valores das casas com
    dígito 1 (1, 2, 4, 8, 16...). Se bater com o número original, está certo.
```

## Fechamento

Hoje você ganhou uma habilidade prática que vai usar muito:

- **Binário** representa qualquer número com só dois dígitos: **0 e 1**.
- O método das **divisões sucessivas por 2** converte decimal em binário: divida, anote os restos, leia na **ordem reversa**.
- A **prova real** (somar as potências de dois) confere o resultado e pega erros.
- O erro mais comum é **esquecer de inverter** a ordem dos restos.

Com a conversão de bases na ponta do lápis, você fecha uma lacuna importante dos fundamentos. Esse tipo de fluência com números é o que torna tranquilo tudo o que envolve dados, cores, redes e depuração mais adiante.

:::roteiro
Aula de nivelamento: o objetivo é FAZER, não teorizar. Apresentar o método como uma receita e fazer o 26 ao vivo no quadro, passo a passo, sublinhando a ordem reversa — que é onde todos tropeçam. A prova real (soma de potências) deve virar hábito: peça que confiram SEMPRE. A atividade do CPF engaja porque o número é "deles". Na rodada de caça ao erro, deixar as duplas acharem o deslize sozinhas — costuma ser ordem invertida. Conectar de volta à Aula 33 (lá viram o porquê; aqui, o como). O `bin()` no VSCode fecha com a ferramenta real. Não introduzir conversão de fração ou binário→decimal por divisão; manter foco em decimal→binário inteiro.
:::
