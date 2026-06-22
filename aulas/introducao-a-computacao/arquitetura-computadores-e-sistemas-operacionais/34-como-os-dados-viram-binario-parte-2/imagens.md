# Brief de imagens — Aula 34: Como os Dados Viram Binário - Parte 2

## 1. Array em memória contígua
- **secao:** Desenvolvimento › "Array: uma fila de caixas lado a lado"
- **arquivo:** img/array-memoria-contigua.png
- **objetivo:** Mostrar elementos do array ocupando posições vizinhas da memória, e que a posição de cada um pode ser calculada (acesso direto). Base para entender o custo de crescer.
- **alt:** Cinco células de memória vizinhas e numeradas, cada uma com um valor do array, com destaque para o cálculo da posição de um elemento a partir do início.
- **prompt:** Ilustração educacional vetorial flat, proporção 16:9, fundo claro. Uma fileira de cinco caixas idênticas encostadas umas nas outras (como caixas de supermercado em fila), numeradas com endereços sequenciais (100, 101, 102...), cada uma contendo um número. Uma seta mostra o cálculo "início + posição" apontando direto para a caixa do meio. Paleta índigo e azul-petróleo com acento laranja, estilo limpo de apostila técnica, rótulos curtos.

## 2. Crescer o array exige copiar
- **secao:** Desenvolvimento › "O preço de crescer"
- **arquivo:** img/array-crescer-copia.png
- **objetivo:** Ilustrar que, sem espaço vizinho livre, o array inteiro precisa migrar para um bloco maior, copiando todos os elementos — o custo escondido.
- **alt:** Um array de cinco elementos sem espaço ao lado (ocupado) sendo copiado inteiro para um novo bloco maior com seis posições.
- **prompt:** Ilustração educacional vetorial flat, proporção 16:9, fundo claro. Em cima, uma fileira de cinco caixas com um bloqueio (cadeado/outro dado) logo após, indicando que não há espaço vizinho. Uma seta grande de "mudança" leva, embaixo, a um novo bloco maior de seis caixas para onde os cinco elementos são copiados e o sexto é adicionado. Ícone de cópia/duplicação sobre a seta. Paleta índigo e azul com acento laranja, estilo didático minimalista, rótulos curtos.

## 3. Ponto flutuante: sinal, expoente, mantissa
- **secao:** Desenvolvimento › diagrama "As três partes de um número de ponto flutuante"
- **arquivo:** img/ponto-flutuante-tres-partes.png
- **objetivo:** Decompor o formato IEEE 754 em três campos visuais, ligando a mantissa finita ao limite de precisão.
- **alt:** Uma barra de bits dividida em três regiões rotuladas sinal, expoente e mantissa.
- **prompt:** Ilustração educacional vetorial flat, proporção 16:9, fundo claro. Uma barra horizontal de bits dividida em três segmentos de tamanhos diferentes: um segmento muito pequeno "sinal" (1 bit), um segmento médio "expoente" e um segmento grande "mantissa". Cada segmento com um mini-ícone: sinal de mais/menos, uma escala/régua para o expoente, e dígitos de precisão para a mantissa. Paleta índigo e azul-petróleo com acento laranja, estilo limpo de apostila, rótulos curtos.
