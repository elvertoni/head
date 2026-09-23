---
conceito: Ponto flutuante
slug: ponto-flutuante
disciplina: introducao-a-computacao
tipo: conceito
aka: [IEEE 754]
status: rascunho
fontes:
  - "lake/introducao-a-computacao/AULA 33_INTRODUÇÃO A COMPUTAÇÃO.pptx"
  - "lake/introducao-a-computacao/AULA 34_INTRODUÇÃO A COMPUTAÇÃO.pptx"
aulas: [33, 34]
atualizado_em: 2026-09-22
---

Ponto flutuante é a técnica padrão para guardar números com casas decimais em binário, separando o valor em partes e deixando o ponto decimal "flutuar" para cobrir tanto números muito grandes quanto muito pequenos com a mesma estrutura. O padrão adotado mundialmente, IEEE 754, divide o espaço de bits em três campos: sinal, expoente e mantissa.

## Em uma frase

Ponto flutuante é como o binário representa números decimais, dividindo os bits em sinal, expoente e mantissa.

## O que precisa saber

O sinal (1 bit) indica positivo ou negativo; o expoente define a escala do número, grande ou pequeno; a mantissa carrega os dígitos significativos — e é justamente o tamanho finito da mantissa que limita a precisão. Como no [[sistema-binario]] nem toda fração decimal tem representação exata em base 2 (do mesmo jeito que 1/3 é dízima infinita em base 10), muitos valores precisam ser arredondados ao serem guardados em ponto flutuante. É por isso que, em praticamente qualquer linguagem, `0.1 + 0.2` não fecha em `0.3` exato, mas em algo como `0.30000000000000004` — não é falha da linguagem, é o limite de representar fração em [[bit]]s finitos.

## Erros comuns

- Achar que `0.1 + 0.2 != 0.3` é bug da linguagem de programação; é consequência do arredondamento inerente à representação binária de frações.
- Tratar ponto flutuante como se tivesse precisão infinita, ignorando que a mantissa finita corta e arredonda dígitos que não cabem.
- Rotular como "erro" o resultado levemente diferente do esperado em comparações de igualdade entre decimais — o diagnóstico correto é comparar com tolerância, não com igualdade exata.

## Onde aparece

- Aula 33 — *Como os Dados Viram Binário - Parte 1* `aulas/introducao-a-computacao/arquitetura-computadores-e-sistemas-operacionais/33-como-os-dados-viram-binario-parte-1/canonica.md`
- Aula 34 — *Como os Dados Viram Binário - Parte 2* `aulas/introducao-a-computacao/arquitetura-computadores-e-sistemas-operacionais/34-como-os-dados-viram-binario-parte-2/canonica.md`
- Conceitos vizinhos: [[bit]], [[sistema-binario]], [[array]]

## Fontes

- Introdução ao ponto flutuante e ao exemplo de arredondamento de 0.1 + 0.2: slides SEED da aula 33 (`lake/introducao-a-computacao/AULA 33_INTRODUÇÃO A COMPUTAÇÃO.pptx`), base da canônica aprovada da aula 33 (blocos `:::conceito Ponto flutuante` e `:::atencao Erro comum que vai te assombrar na programação`).
- As três partes do padrão IEEE 754 (sinal, expoente, mantissa): slides SEED da aula 34 (`lake/introducao-a-computacao/AULA 34_INTRODUÇÃO A COMPUTAÇÃO.pptx`), base da canônica aprovada da aula 34 (bloco `diagrama-progressivo` e `:::conceito Sinal, expoente e mantissa`).
