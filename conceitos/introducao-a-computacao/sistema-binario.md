---
conceito: Sistema binário
slug: sistema-binario
disciplina: introducao-a-computacao
tipo: conceito
aka: [base 2]
status: rascunho
fontes:
  - "lake/introducao-a-computacao/AULA 25_INTRODUÇÃO A COMPUTAÇÃO.pptx"
  - "lake/introducao-a-computacao/AULA 33_INTRODUÇÃO A COMPUTAÇÃO.pptx"
  - "lake/introducao-a-computacao/AULA NIVELAMENTO 01_INTRODUÇÃO A COMPUTAÇÃO.pptx"
aulas: [1, 25, 33]
atualizado_em: 2026-09-22
---

Sistema binário é o sistema de numeração posicional em base 2, que representa qualquer número usando só dois dígitos (0 e 1), cada posição valendo o dobro da anterior. É adotado pela computação porque um circuito digital sustenta naturalmente dois estados (ligado/desligado), o mesmo par de símbolos do sistema.

## Em uma frase

Sistema binário é a base 2 — só 0 e 1, cada casa valendo o dobro da anterior — em que o computador representa tudo.

## O que precisa saber

Assim como a base 10 tem dez dígitos e casas que valem dez vezes mais que a anterior, a base 2 tem dois dígitos e casas que valem o dobro (1, 2, 4, 8, 16...). Um número em base 2 é lido somando as potências de dois das posições com dígito 1 — por exemplo, `11010` vale 16+8+2 = 26. A conversão inversa, de decimal para binário, segue um método de divisões sucessivas por 2, lendo os restos em ordem reversa. É nesse sistema que um [[bit]] ganha valor posicional, que grupos de bits formam um [[byte]], e sobre o qual se apoia a própria [[linguagem-de-maquina]] que o processador executa.

## Erros comuns

- Escrever os restos da divisão sucessiva na ordem em que saíram, sem inverter — o resto da última divisão é o dígito mais à esquerda do binário.
- Esquecer que cada posição vale o dobro da anterior e somar potências erradas ao converter de volta para decimal.

## Onde aparece

- Aula 1 — *Nivelamento - Convertendo Decimal para Binário* `aulas/introducao-a-computacao/nivelamento-e-retomada/01-nivelamento-conversao-decimal-para-binario/canonica.md`
- Aula 25 — *Como o Computador Lê o seu Código - Parte 1* `aulas/introducao-a-computacao/arquitetura-computadores-e-sistemas-operacionais/25-como-o-computador-le-o-codigo-parte-1/canonica.md`
- Aula 33 — *Como os Dados Viram Binário - Parte 1* `aulas/introducao-a-computacao/arquitetura-computadores-e-sistemas-operacionais/33-como-os-dados-viram-binario-parte-1/canonica.md`
- Conceitos vizinhos: [[bit]], [[byte]], [[linguagem-de-maquina]], [[codificacao-de-caracteres]]

## Fontes

- Método das divisões sucessivas por 2 e prova real por soma de potências: slides SEED da aula nivelamento 01 (`lake/introducao-a-computacao/AULA NIVELAMENTO 01_INTRODUÇÃO A COMPUTAÇÃO.pptx`), base da canônica aprovada da aula 1 (bloco `:::conceito Número binário` e `:::importante O passo a passo da conversão`).
- Ligação entre binário e linguagem de máquina executada pelo processador: slides SEED da aula 25 (`lake/introducao-a-computacao/AULA 25_INTRODUÇÃO A COMPUTAÇÃO.pptx`), base da canônica aprovada da aula 25.
- Representação de inteiros em base 2 (exemplo 0111 = 7): slides SEED da aula 33 (`lake/introducao-a-computacao/AULA 33_INTRODUÇÃO A COMPUTAÇÃO.pptx`), base da canônica aprovada da aula 33 (bloco `:::conceito Número inteiro em binário`).
