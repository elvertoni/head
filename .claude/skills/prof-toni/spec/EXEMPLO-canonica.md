---
titulo: Por que o computador só entende 0 e 1?
tema: Representação de dados (sistema binário)
disciplina: Fundamentos de Computação
serie: 1ª
prerequisitos: [Saber contar no sistema decimal]
objetivos:
  - Explicar por que o computador usa apenas dois estados (0 e 1)
  - Relacionar o 0 e o 1 a um estado físico real (ligado/desligado)
  - Converter números pequenos entre decimal e binário
  - Reconhecer que texto, imagem e som também viram sequências de bits
revisao: false
---

Pega o celular que está no seu bolso. Dentro dele há **bilhões** de peças minúsculas, e cada uma sabe fazer só uma coisa: estar **ligada** ou **desligada**. Nenhuma delas entende a letra "A", a cor azul ou uma música. Mesmo assim, o aparelho faz tudo isso. A aula de hoje responde a um mistério que está na base de *toda* a computação: como um monte de interruptores que só sabem "liga/desliga" consegue representar o mundo inteiro?

## Objetivos

Ao final desta aula, você será capaz de:

- Explicar **por que** o computador trabalha só com 0 e 1 (e não de 0 a 9, como nós).
- Relacionar o 0 e o 1 a um fenômeno **físico** real dentro do hardware.
- Converter números pequenos de decimal para binário e de binário para decimal.
- Entender que letras, imagens e sons também são, no fundo, sequências de bits.

## Pré-requisitos

Nenhum conhecimento de programação. Basta saber **contar no sistema decimal** (0, 1, 2, ... 9), que é o que todos nós usamos no dia a dia.

## Desenvolvimento

### O interruptor: a peça que só sabe duas coisas

Lá no fundo do computador existe um componente chamado **transistor**. Você pode imaginá-lo como um **interruptor de luz** microscópico: ou ele deixa a corrente elétrica passar, ou não deixa.

:::conceito Bit
**Bit** é a menor informação que o computador guarda. Ele tem só dois valores possíveis: **0** (interruptor desligado) ou **1** (interruptor ligado). A palavra vem de *binary digit* — "dígito binário".

:::

Ou seja: o 0 e o 1 **não foram inventados por capricho**. Eles representam o que o interruptor físico consegue fazer de verdade: estar desligado ou ligado.

### Por que não de 0 a 9, como a gente?

Essa é a pergunta do título. A resposta é sobre **confiabilidade**.

Imagine que um fio pode ter tensão de 0 a 5 volts. Seria possível criar 10 "níveis" e dizer: 0V = 0, 0,5V = 1, 1V = 2... até 5V = 9. O problema é que a corrente elétrica **oscila** o tempo todo (calor, interferência, qualidade do material). Distinguir com segurança entre 0,5V e 0,6V é muito difícil — um errinho e o número vira outro.

:::importante O ponto-chave
Distinguir entre **só duas opções** — "tem corrente" ou "não tem" — é muitíssimo mais confiável do que distinguir entre dez. Por isso o computador escolheu o caminho mais simples e seguro: **dois estados**. Velocidade e confiança valem mais que "parecer com a gente".

:::

:::atencao Erro comum
Muita gente acha que "binário é uma linguagem secreta do computador". Não é segredo nenhum — é só uma forma de **contar usando dois algarismos em vez de dez**. E `10` em binário **não** é "dez": vamos ver já que vale **dois**.

:::

### Contando com dois algarismos

No nosso sistema (decimal), cada casa vale **10 vezes** mais que a anterior: unidade, dezena, centena...

No sistema binário, cada casa vale **2 vezes** mais que a anterior:

| Casa | … | 16 | 8 | 4 | 2 | 1 |
|---|---|---|---|---|---|---|
| Vale | | 2⁴ | 2³ | 2² | 2¹ | 2⁰ |

Para ler um número binário, **some os valores das casas onde tem 1**. Exemplos:

- `101` → 4 + 0 + 1 = **5**
- `1010` → 8 + 0 + 2 + 0 = **10**
- `1111` → 8 + 4 + 2 + 1 = **15**

```diagrama-progressivo
titulo: Como a letra "A" vira 0s e 1s
camadas:
  - rotulo: 1. Você digita "A"
    conteudo: No teclado, você aperta a tecla A. O computador precisa guardar isso, mas ele só entende números.
  - rotulo: 2. A tabela de códigos
    conteudo: Existe uma tabela (chamada ASCII) que dá um número para cada caractere. Na tabela, a letra "A" maiúscula é o número 65.
  - rotulo: 3. O número vira binário
    conteudo: O 65 em binário é 1000001 (= 64 + 1). É isso que fica guardado.
  - rotulo: 4. Binário vira eletricidade
    conteudo: Cada 1 é um interruptor ligado e cada 0 é um desligado. A letra "A" virou um padrão de corrente elétrica.
```

### Juntando bits: o byte

Um bit sozinho informa pouco (só liga/desliga). Mas juntando bits dá pra representar muita coisa.

:::conceito Byte
Um **byte** é um grupo de **8 bits**. Com 8 bits dá para fazer 256 combinações diferentes (de `00000000` a `11111111`) — o suficiente para todas as letras, números e símbolos do teclado.

:::

:::dica Onde você vai ver isso programando
Quando você for mexer com cores em um site, vai escrever algo como `#FF0000` para vermelho. Esse `FF` é só um jeito curto de escrever **11111111** em binário (o vermelho no máximo). Entender bits agora deixa cor, permissões de arquivo e tamanho de memória (KB, MB, GB) muito mais fáceis depois.

:::

## Prática

**Atividade "mãos = bits" (sem computador, ~10 min).** Em grupos de 4, cada aluno é um bit, valendo (da esquerda para a direita) **8, 4, 2 e 1**. Mão **levantada = 1**, mão **abaixada = 0**.

1. Representem o número **5** (resposta: abaixada, levantada, abaixada, levantada → `0101`).
2. Representem **10** e depois **13**.
3. Qual é o **maior** número que o grupo consegue formar? (Todas levantadas: `1111` = 15.)

**Extensão no VSCode (se a turma já viu Python):** digite e rode o trecho abaixo, trocando pela inicial do seu nome.

```python
letra = "A"
print(ord(letra))        # mostra o número da letra na tabela ASCII
print(bin(ord(letra)))   # mostra esse número em binário (o 0b na frente quer dizer "binário")
```

## Avaliação

```quiz
- pergunta: Por que o computador usa só 0 e 1, em vez de contar de 0 a 9 como nós?
  alternativas:
    - texto: Porque é uma linguagem secreta criada pelos engenheiros
    - texto: Porque distinguir entre "ligado" e "desligado" é muito mais confiável que distinguir 10 níveis de tensão
      correta: true
    - texto: Porque o computador não consegue guardar o número 2
    - texto: Porque assim o computador fica mais bonito
  feedback: >
    É uma questão de confiabilidade física: dois estados (tem corrente / não tem)
    são fáceis de distinguir sem erro, mesmo com a oscilação da corrente elétrica.
- pergunta: Quanto vale o número binário 1011 em decimal?
  alternativas:
    - texto: "11"
      correta: true
    - texto: "1011"
    - texto: "8"
    - texto: "101"
  feedback: >
    Some as casas onde há 1: 8 + 0 + 2 + 1 = 11. Lembre que cada casa, da direita
    para a esquerda, vale 1, 2, 4, 8...
- pergunta: O que é um byte?
  alternativas:
    - texto: Um único interruptor ligado
    - texto: Um grupo de 8 bits
      correta: true
    - texto: O mesmo que um número decimal
    - texto: Uma cor da tela
  feedback: >
    Byte = 8 bits juntos, o que dá 256 combinações — suficiente para representar
    cada caractere do teclado.
```

## Fechamento

Hoje a gente descobriu que:

- O computador é feito de **bilhões de interruptores** (transistores) que só sabem ligar/desligar.
- Por isso ele usa **bits**: 0 (desligado) e 1 (ligado) — escolha feita por **confiabilidade**, não por capricho.
- Juntando bits dá pra representar números, e juntando 8 bits temos um **byte**, que representa letras e símbolos.
- **Tudo** — texto, imagem, som — vira, no fundo, sequência de 0s e 1s.

**Próxima aula:** se o computador só guarda 0 e 1, como é que ele faz **contas** e **toma decisões** com esses bits? Vamos conhecer as **portas lógicas** — as peças que transformam bits em raciocínio.

:::roteiro
Abrir com o celular na mão de verdade (ou pedir que peguem o deles) — o "bilhões de interruptores" causa mais impacto sentindo o objeto. Não entregar a resposta do "por que não 0 a 9": deixe a turma chutar primeiro ("por que vocês acham?"), só depois revele a confiabilidade. Na atividade das mãos, escolha grupos na frente da sala para representar — o erro de quem levanta a mão errada é ótimo momento de aprendizagem, conduza sem constranger. Se a turma ainda não viu Python, pule a extensão sem culpa: a atividade desplugada já cumpre o objetivo. Guardar uns 8 min finais para o quiz coletivo, lendo o feedback de cada questão em voz alta.
:::
