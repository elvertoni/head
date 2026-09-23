---
conceito: Byte
slug: byte
disciplina: introducao-a-computacao
tipo: conceito
aka: []
status: rascunho
fontes:
  - "lake/introducao-a-computacao/AULA 33_INTRODUÇÃO A COMPUTAÇÃO.pptx"
aulas: [33]
atualizado_em: 2026-09-22
---

Byte é o agrupamento de 8 [[bit]]s e a unidade fundamental de armazenamento em computação: já é grande o bastante para representar um número, uma letra ou uma cor. É a unidade em que praticamente toda medida de armazenamento (KB, MB, GB, TB) é contada.

## Em uma frase

Byte é o grupo de 8 bits que serve de unidade padrão para medir e guardar dados.

## O que precisa saber

Um bit sozinho distingue só duas opções; agrupar 8 deles em um byte já cobre 256 combinações possíveis — o suficiente, por exemplo, para toda a tabela ASCII de [[codificacao-de-caracteres]], que usa exatamente 1 byte por caractere no exemplo dado em aula. É também no byte que a lógica do [[sistema-binario]] vira prática: cada byte é lido como um número em base 2 e depois interpretado — como inteiro, como caractere, como parte de um [[ponto-flutuante]] — conforme o tipo de dado que o programa espera naquela posição de memória.

## Erros comuns

- Confundir byte com bit ao ler prefixos de armazenamento — "MB" e "GB" contam bytes, não bits.
- Assumir que todo caractere sempre ocupa exatamente 1 byte: isso vale para a tabela ASCII usada em aula, mas não é garantia geral de todo esquema de codificação de caracteres.

## Onde aparece

- Aula 33 — *Como os Dados Viram Binário - Parte 1* `aulas/introducao-a-computacao/arquitetura-computadores-e-sistemas-operacionais/33-como-os-dados-viram-binario-parte-1/canonica.md`
- Conceitos vizinhos: [[bit]], [[sistema-binario]], [[codificacao-de-caracteres]]

## Fontes

- Definição de byte, a relação 8 bits = 1 byte e o exemplo de 1 byte por caractere ASCII: slides SEED da aula 33 (`lake/introducao-a-computacao/AULA 33_INTRODUÇÃO A COMPUTAÇÃO.pptx`), base da canônica aprovada da aula 33 (blocos `:::conceito Bit e byte` e `:::conceito Codificação de caracteres (ASCII e Unicode)`).
