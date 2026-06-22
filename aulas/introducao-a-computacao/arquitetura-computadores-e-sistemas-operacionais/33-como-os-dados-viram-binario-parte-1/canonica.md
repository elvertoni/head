---
titulo: Como os Dados Viram Binário - Parte 1
tema: Representação de inteiros, decimais e caracteres
disciplina: introducao-a-computacao
serie: 1ª
prerequisitos: [A Memória do Computador - Parte 2 - a Hierarquia]
objetivos:
  - Explicar que todo dado é armazenado em binário (bits e bytes)
  - Descrever como números inteiros são representados em binário
  - Reconhecer a ideia de ponto flutuante para números decimais
  - Entender como caracteres são codificados (ASCII e Unicode)
trilha: arquitetura-computadores-e-sistemas-operacionais
ordem: 33
slug: como-os-dados-viram-binario-parte-1
modo_origem: seed
fontes:
  - lake/introducao-a-computacao/AULA 33_INTRODUÇÃO A COMPUTAÇÃO.pptx
revisao: true
status: aprovada
versao: 1
atualizado_em: 2026-06-21
---

A esta altura você já ouviu mil vezes que o computador só trabalha com 0 e 1. Mas pare para pensar no que isso significa de verdade: a sua mensagem, a sua foto, a sua nota da prova, a música que você ouve — **tudo** isso, lá no fundo, é só uma fileira gigante de zeros e uns. Aí surge a pergunta que a estudante Letícia fez e que trava muita gente: se é **tudo** 0 e 1, como o computador sabe que uma sequência é o número **7**, outra é a letra **A** e outra é um número quebrado como **3,5**? Como ele não confunde tudo? Hoje você descobre o sistema por trás disso.

## Objetivos

Ao final desta aula, você será capaz de:

- Explicar que **todo dado** é armazenado em **binário** (bits e bytes).
- Descrever como **números inteiros** são representados em binário.
- Reconhecer a ideia de **ponto flutuante** para números decimais.
- Entender como **caracteres** são codificados (**ASCII** e **Unicode**).

## Pré-requisitos

Ter visto que a memória guarda dados (Aulas 27, 31 e 32) e a ideia, das primeiras aulas, de que a linguagem de máquina é feita de **0 e 1**.

## Desenvolvimento

### A unidade de tudo: bit e byte

Antes de tudo, dois nomes que você vai usar para sempre:

:::conceito Bit e byte
Um **bit** é a menor unidade de informação: um único **0 ou 1**. Sozinho, ele diz pouco. Mas juntando **8 bits** formamos um **byte**, e um byte já consegue representar muita coisa — um número, uma letra, uma cor. O byte é a **unidade fundamental** de armazenamento: quando você vê "MB", "GB", está contando bytes aos montes.
:::

A sacada genial da computação é que, com apenas dois símbolos (0 e 1) e combinações suficientes, dá para representar **qualquer** informação. O segredo está em **como** interpretar cada grupo de bits.

### Números inteiros: contar em base 2

Você conta em base 10 (dez dígitos: 0 a 9) porque tem dez dedos. O computador conta em **base 2** (dois dígitos: 0 e 1) porque seus circuitos têm dois estados: ligado e desligado.

:::conceito Número inteiro em binário
Números inteiros são guardados como sua representação em **base 2**. Cada posição vale o dobro da anterior. Por exemplo, o número **7** é `0111` e o número **15** é `1111`. Mesma lógica do nosso sistema, só que com dois dígitos em vez de dez.
:::

:::exemplo
Veja como `0111` vale 7. Da direita para a esquerda, cada posição vale 1, 2, 4, 8...

| Posição vale | 8 | 4 | 2 | 1 |
|---|---|---|---|---|
| Bit | 0 | 1 | 1 | 1 |
| Soma | 0 | 4 | 2 | 1 |

Some os que têm bit 1: 4 + 2 + 1 = **7**. É só isso. Contar em binário é somar potências de dois.
:::

### Números decimais: o ponto que flutua

E um número quebrado, como 3,5 ou 0,001? Aí entra uma estratégia mais esperta, o **ponto flutuante**.

:::conceito Ponto flutuante
É a forma de guardar números **com casas decimais**. A ideia é separar o número em duas partes — a parte inteira e a parte fracionária — e representar cada uma em binário. O nome "flutuante" vem do ponto decimal poder "se mover" para representar números muito grandes ou muito pequenos com a mesma técnica.
:::

:::atencao Erro comum que vai te assombrar na programação
Nem todo número decimal cabe **com exatidão** em binário. Assim como `1/3` vira `0,3333...` (dízima que nunca termina) em base 10, muitos decimais simples viram dízimas infinitas em base 2 e precisam ser **arredondados**. É por isso que, em quase toda linguagem de programação, `0.1 + 0.2` não dá exatamente `0.3`, e sim algo como `0.30000000000000004`. Não é bug da linguagem: é o limite de representar fração em binário. Guarde isso — um dia vai te salvar horas de confusão.
:::

### Caracteres: uma tabela que combina número com letra

Falta o caso da Letícia: como uma letra vira binário? A resposta é uma **combinação prévia** — uma tabela que todo mundo concorda em usar.

:::conceito Codificação de caracteres (ASCII e Unicode)
É um padrão que dá a cada caractere um **número**, que então é guardado em binário. Na tabela **ASCII**, por exemplo, a letra **'A'** é o número **65**. O **Unicode** é uma tabela muito maior, que cobre praticamente todos os alfabetos, símbolos e até emojis do mundo. Quando o computador lê os bits, ele usa a tabela para saber qual caractere mostrar.
:::

Então a resposta para "como o computador não confunde 65 com 'A'?" é: **ele só sabe que é uma letra porque o programa diz que aquela posição da memória deve ser lida como caractere**, e aí usa a tabela de codificação. O mesmo padrão de bits pode ser o número 65 ou a letra 'A' — quem decide a interpretação é o **tipo de dado** que o programa espera ali.

:::dica Por que isso aparece quando você menos espera
Já viu um site mostrar "Ã§" no lugar de "ç", ou um nome aparecer todo quebrado com símbolos estranhos? Isso é um choque de **codificação**: o texto foi guardado com uma tabela e lido com outra. Saber que letra é número-virado-binário-via-tabela é o que permite a um profissional entender e corrigir esses erros de acentuação — pesadelo comum em sites, bancos de dados e arquivos.
:::

## Prática

**Atividade "decodificadores" (desplugada, 12 a 15 min).** A turma vira tradutora de binário, usando uma tabela simples.

O professor entrega uma mini-tabela de codificação combinada para a brincadeira (pode ser um recorte real do ASCII):

| Letra | Número | Binário (1 byte) |
|---|---|---|
| A | 65 | 01000001 |
| B | 66 | 01000010 |
| C | 67 | 01000011 |
| ... | ... | ... |

**Parte 1 — números:** o professor escreve binários curtos (`0101`, `1000`, `0011`) e os grupos convertem para decimal somando as potências de dois.

**Parte 2 — letras:** o professor "envia uma mensagem secreta" em binário (várias sequências de 1 byte) e os grupos usam a tabela para decodificar a palavra escondida.

Depois, discutam:

- O mesmo binário `01000001` é o número 65 **ou** a letra 'A'. O que decide qual deles é? (A tabela/o tipo de dado escolhido.)
- Por que uma tabela só (ASCII) não bastaria para escrever em japonês ou usar emoji? (Precisa do Unicode, bem maior.)

**Extensão opcional no VSCode:** em Python, rode `print(ord('A'))` e depois `print(chr(65))`. Em 2 linhas, explique o que cada um fez e como isso se liga à tabela de codificação que você usou na prática.

## Avaliação

```quiz
- pergunta: Quantos bits formam um byte, a unidade fundamental de armazenamento?
  alternativas:
    - texto: 2 bits
    - texto: 8 bits
      correta: true
    - texto: 100 bits
    - texto: 1 bit
  feedback: >
    Um bit é um único 0 ou 1. Oito bits formam um byte, que já representa um
    número, uma letra ou uma cor. "GB" e "MB" contam bytes aos montes.
- pergunta: Como o computador diferencia o número 65 da letra 'A', se os dois podem ter o mesmo binário?
  alternativas:
    - texto: A letra usa eletricidade diferente do número
    - texto: Pela interpretação: o programa decide se aquela posição é lida como número ou como caractere (usando uma tabela de codificação)
      correta: true
    - texto: O computador nunca confunde porque letras não viram binário
    - texto: Letras ficam no disco e números na RAM
  feedback: >
    O mesmo padrão de bits pode ser o número 65 ou a letra 'A'. Quem decide é o
    TIPO de dado que o programa espera ali, usando a tabela (como ASCII).
- pergunta: Por que 0.1 + 0.2 costuma não dar exatamente 0.3 nos computadores?
  alternativas:
    - texto: Porque a linguagem de programação tem um bug
    - texto: Porque muitos decimais viram dízimas infinitas em binário e precisam ser arredondados (ponto flutuante)
      correta: true
    - texto: Porque a CPU está com defeito
    - texto: Porque falta memória RAM
  feedback: >
    Nem todo decimal cabe com exatidão em binário, igual a 1/3 em base 10. O
    ponto flutuante arredonda, e o arredondamento aparece nessas continhas.
```

## Fechamento

Hoje você desceu até o nível do bit e viu a lógica por trás do "tudo é 0 e 1":

- Um **bit** é 0 ou 1; **8 bits** formam um **byte**, a unidade fundamental.
- **Inteiros** são guardados em **base 2** (somando potências de dois).
- **Decimais** usam **ponto flutuante**, que arredonda — daí o famoso `0.1 + 0.2`.
- **Caracteres** viram número por uma tabela (**ASCII**, **Unicode**); o tipo de dado decide a interpretação.

Você viu como **um** valor — um número, uma letra — é representado. Mas programas trabalham com **coleções** de valores: listas, sequências, tabelas inteiras. Na próxima aula, a gente vê como o computador organiza vários dados juntos na memória, conhecendo os **arrays** e voltando, com mais profundidade, ao ponto flutuante.

:::roteiro
Abrir pela pergunta da Letícia (se é tudo 0 e 1, como não confunde número, letra e decimal?). Não despejar conversão binária como matemática seca: usar a tabela de potências de dois e deixar a turma somar. O :::atencao do 0.1+0.2 costuma gerar espanto — pode até demonstrar ao vivo no VSCode; é memorável e desmistifica "bug". A grande sacada conceitual é: o mesmo binário pode ser número OU letra, e quem decide é o TIPO/a tabela. A prática da mensagem secreta torna a codificação divertida e concreta. A dica do "Ã§" liga a um erro real que eles já viram. Fechar ganchando arrays (Aula 34).
:::
