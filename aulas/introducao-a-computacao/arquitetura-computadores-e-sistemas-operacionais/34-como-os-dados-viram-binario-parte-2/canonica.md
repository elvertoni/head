---
titulo: Como os Dados Viram Binário - Parte 2
tema: Arrays na memória e ponto flutuante por dentro
disciplina: introducao-a-computacao
serie: 1ª
prerequisitos: [Como os Dados Viram Binário - Parte 1]
objetivos:
  - Explicar como arrays são guardados em memória contígua
  - Relacionar a memória contígua ao custo de aumentar um array
  - Descrever as três partes do padrão de ponto flutuante (sinal, expoente, mantissa)
  - Reconhecer por que o ponto flutuante tem limites de precisão
trilha: arquitetura-computadores-e-sistemas-operacionais
ordem: 34
slug: como-os-dados-viram-binario-parte-2
modo_origem: seed
fontes:
  - lake/introducao-a-computacao/AULA 34_INTRODUÇÃO A COMPUTAÇÃO.pptx
revisao: true
status: aprovada
versao: 1
atualizado_em: 2026-06-21
---

Na aula passada você viu como **um** valor vira binário. Mas nenhum programa interessante usa um valor só. Uma lista de contatos, as notas de uma turma, os quadros de um vídeo, o placar de um jogo — tudo é **monte** de dados juntos. E aí surge a dúvida que o programador iniciante Leo teve: se eu guardo cinco números numa lista, eles ficam **espalhados** pela memória ou **enfileirados** um do lado do outro? E o que acontece se eu quiser adicionar um sexto? A resposta tem consequências práticas enormes — e explica decisões que você vai tomar quando programar de verdade.

## Objetivos

Ao final desta aula, você será capaz de:

- Explicar como **arrays** são guardados em **memória contígua**.
- Relacionar a memória contígua ao **custo de aumentar** um array.
- Descrever as **três partes** do ponto flutuante: sinal, expoente e mantissa.
- Reconhecer por que o ponto flutuante tem **limites de precisão**.

## Pré-requisitos

Ter visto a **Aula 33**: bit e byte, inteiros em binário, a ideia de ponto flutuante e codificação de caracteres.

## Desenvolvimento

### Array: uma fila de caixas lado a lado

Quando você precisa guardar vários dados do mesmo tipo, usa um **array**.

:::conceito Array
É uma **coleção de elementos do mesmo tipo**, guardados em sequência. Pense numa fila de caixas no caixa do supermercado: cada caixa guarda um item (um elemento), e as caixas ficam **uma exatamente ao lado da outra**.
:::

E é aí que está o detalhe importante, que responde à primeira dúvida do Leo:

:::conceito Memória contígua
Os elementos de um array ficam em posições **vizinhas** da memória, sem buracos entre elas — um bloco **contíguo**. Se um array de 5 inteiros começa numa posição, os outros 4 ficam logo em seguida. Isso permite ao computador **calcular** instantaneamente onde está cada elemento, em vez de procurar.
:::

:::exemplo
Um array de 5 números ocupando posições vizinhas da memória:

| Posição na memória | 100 | 101 | 102 | 103 | 104 |
|---|---|---|---|---|---|
| Elemento do array | 12 | 7 | 33 | 9 | 50 |

Quer o **terceiro** elemento? O computador não procura caixa por caixa: ele calcula "começo (100) + 2 posições = 102" e vai direto. É por isso que acessar qualquer item de um array é **rápido** e custa o mesmo, esteja ele no começo ou no fim.
:::

### O preço de crescer: por que não cabe mais um

Agora a segunda dúvida do Leo: e se eu quiser **adicionar** um elemento a um array cheio?

:::importante Crescer um array pode custar caro
Como os elementos precisam ficar **colados** uns nos outros, se o espaço logo depois do array já estiver ocupado por outra coisa, **não dá** simplesmente para "empurrar" mais um. O computador precisa: (1) achar um novo espaço contíguo maior, (2) **copiar** todos os elementos antigos para lá, e (3) só então adicionar o novo. Por isso, em várias linguagens, o tamanho de um array é **definido na criação** e não muda — e estruturas que crescem livremente custam esse trabalho de cópia por baixo dos panos.
:::

:::dica Por que isso vira decisão de programador
Essa é a diferença entre quem escreve código que "funciona" e quem escreve código **eficiente**. Saber que um array tem tamanho fixo e que crescer custa cópia te ajuda a escolher a estrutura de dados certa: se você sabe quantos itens terá, um array é rápido e econômico; se a quantidade muda muito, talvez valha outra estrutura. Essa escolha aparece em entrevistas de emprego de programação e no desempenho real dos sistemas que você vai construir.
:::

:::atencao Erro comum
Imaginar que adicionar um item a uma lista é sempre "de graça" e instantâneo. Por trás de um comando simples pode estar uma cópia inteira do array para um novo lugar da memória. Na maioria das vezes você não percebe, mas em listas enormes, dentro de um laço de repetição, esse custo escondido pode deixar um programa lento sem motivo aparente.
:::

### Olhando o ponto flutuante por dentro

Na Aula 33 você viu que decimais usam ponto flutuante e que ele arredonda. Agora vamos abrir a caixa e ver **como** ele guarda um número quebrado. O padrão usado mundialmente (chamado IEEE 754) divide o espaço em **três partes**:

```diagrama-progressivo
titulo: As três partes de um número de ponto flutuante
camadas:
  - rotulo: 1. Sinal
    conteudo: Um único bit que diz se o número é positivo ou negativo. 0 para positivo, 1 para negativo.
  - rotulo: 2. Expoente
    conteudo: Dá a "escala" do número — se ele é grande (como 1000) ou pequeno (como 0,001). É o que faz o ponto decimal "flutuar".
  - rotulo: 3. Mantissa
    conteudo: Guarda os dígitos significativos, a parte "precisa" do número. É aqui que mora a precisão — e o limite dela.
```

:::conceito Sinal, expoente e mantissa
O **sinal** indica positivo ou negativo. O **expoente** define a escala (quão grande ou pequeno). A **mantissa** carrega os dígitos precisos do número. Juntando os três, o computador representa desde números gigantes até frações minúsculas — mas sempre com um **número limitado** de bits na mantissa.
:::

E é justamente esse limite que explica o arredondamento da aula passada: a mantissa tem **espaço finito**. Quando um número precisaria de mais dígitos do que cabe ali, ele é **cortado e arredondado**. Não tem como representar infinitos dígitos em bits finitos — por isso `0.1 + 0.2` escorrega.

## Prática

**Atividade "memória contígua" (desplugada, 12 a 15 min).** A turma vira a memória e sente o custo de crescer um array.

Use **carteiras enfileiradas** como posições da memória. Cinco alunos, sentados em carteiras vizinhas, seguram cartões com números — esse é um **array de 5 elementos**.

**Cena 1 — acesso rápido:** o professor pede "o elemento da posição 3". A turma conta a partir do início e aponta direto a carteira — sem revistar todas. Mostre que dá para **calcular** a posição.

**Cena 2 — crescer no espaço ocupado:** coloque **outros alunos** sentados logo depois do array. Agora o professor pede para **adicionar um sexto elemento** ao array. Como não há carteira vizinha livre (está ocupada), o array inteiro precisa **se mudar** para uma fileira vazia maior — todos os 5 levantam, copiam-se para o novo lugar, e só então entra o sexto.

Discutam:

- Por que acessar a posição 3 foi tão rápido? (Memória contígua = cálculo direto.)
- Por que crescer o array deu tanto trabalho? (Precisou copiar tudo para um novo bloco.)
- Se você **soubesse de antemão** que precisaria de 6 lugares, o que teria feito diferente?

**Extensão opcional no VSCode:** em Python, crie uma lista `notas = [7, 8, 9]`, acesse `notas[1]` e depois use `notas.append(10)`. Em 3 linhas, relacione o acesso por índice com a "memória contígua" e o `append` com a ideia de crescer o array.

## Avaliação

```quiz
- pergunta: O que significa um array ser guardado em memória contígua?
  alternativas:
    - texto: Seus elementos ficam espalhados aleatoriamente pela memória
    - texto: Seus elementos ficam em posições vizinhas, uma ao lado da outra, sem buracos
      correta: true
    - texto: Ele só pode ser guardado no disco rígido
    - texto: Ele apaga ao desligar o computador
  feedback: >
    Memória contígua significa elementos colados, em posições vizinhas. Isso
    deixa o computador calcular a posição de cada item direto, sem procurar.
- pergunta: Por que adicionar um elemento a um array cheio pode ser custoso?
  alternativas:
    - texto: Porque o array precisa ser impresso antes
    - texto: Porque pode ser necessário achar um novo bloco maior e copiar todos os elementos para lá
      correta: true
    - texto: Porque arrays não aceitam números novos
    - texto: Porque o monitor precisa reiniciar
  feedback: >
    Como os elementos ficam colados, se não há espaço vizinho livre o computador
    cria um bloco maior e copia tudo. Esse custo de cópia fica escondido.
- pergunta: Quais são as três partes de um número em ponto flutuante (IEEE 754)?
  alternativas:
    - texto: Início, meio e fim
    - texto: Sinal, expoente e mantissa
      correta: true
    - texto: Bit, byte e megabyte
    - texto: RAM, cache e disco
  feedback: >
    O sinal diz positivo ou negativo, o expoente define a escala, e a mantissa
    guarda os dígitos precisos. A mantissa é finita — por isso há arredondamento.
```

## Fechamento

Hoje você viu como **coleções** de dados vivem na memória e abriu o ponto flutuante por dentro:

- Um **array** é uma coleção de elementos do mesmo tipo, guardados em **memória contígua**.
- A contiguidade torna o **acesso rápido**, mas faz **crescer** o array custar uma cópia.
- O **ponto flutuante** tem três partes: **sinal**, **expoente** e **mantissa**.
- A **mantissa finita** é a razão dos limites de precisão e do arredondamento.

Com esta aula, você fecha o bloco sobre **como o computador processa, guarda e representa dados**. A partir da próxima aula, a gente sobe um andar inteiro: vamos conhecer o programa que comanda toda essa máquina, organiza a memória, o processador e os arquivos, e torna o computador utilizável — o **sistema operacional**.

:::roteiro
Abrir pela dúvida do Leo (elementos enfileirados ou espalhados? e crescer?). A metáfora da fila de caixas no supermercado é a base — usar carteiras enfileiradas na prática deixa contíguo literal. O momento de ouro é a Cena 2: ver o array inteiro "se mudar" porque o vizinho está ocupado faz o custo de cópia ser inesquecível. Conectar de volta à Aula 33: lá o 0.1+0.2 ficou sem explicação completa; aqui a mantissa finita fecha o porquê. Não entrar em passagem por valor/referência (sem fonte, fora do escopo de 1ª série). Este é o último da sequência de hardware/dados: fechar anunciando a virada para sistemas operacionais (Aula 35).
:::
