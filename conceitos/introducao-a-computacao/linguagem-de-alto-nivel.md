---
conceito: Linguagem de alto nível
slug: linguagem-de-alto-nivel
disciplina: introducao-a-computacao
tipo: conceito
aka: [linguagem de programação de alto nível, high-level language]
status: rascunho
fontes:
  - "lake/introducao-a-computacao/AULA 25_INTRODUÇÃO A COMPUTAÇÃO.pptx"
aulas: [25]
atualizado_em: 2026-09-22
---

Linguagem de alto nível é uma linguagem de programação projetada para ser lida e escrita por pessoas, não pelo processador: usa palavras-chave, símbolos matemáticos e estruturas de controle que se aproximam do raciocínio humano em vez do binário da máquina. Python, Java, C++ e JavaScript são exemplos; nenhum processador executa esse código diretamente.

## Em uma frase

Linguagem de alto nível é código escrito para o programador entender, que precisa ser traduzido antes de rodar.

## O que precisa saber

"Alto nível" descreve distância do hardware, não dificuldade: quanto mais alto o nível, mais longe da [[linguagem-de-maquina]] e mais perto da forma como uma pessoa pensa o problema. Um código em alto nível só roda depois de passar por um [[compilador]] ou um [[interpretador]], que fazem a ponte até as instruções que a [[cpu]] consegue executar. Essa distância também é o que torna o código mais portável entre arquiteturas diferentes: o mesmo código-fonte em alto nível pode gerar linguagens de máquina distintas dependendo do processador de destino, desde que exista um tradutor para aquela arquitetura.

## Erros comuns

- Achar que "alto nível" significa mais difícil ou mais sofisticado — é o oposto: quanto mais alto o nível, mais a linguagem se afasta do binário e se aproxima do raciocínio humano.
- Supor que o processador consegue interpretar palavras como `print` ou `if` diretamente, sem qualquer tradução prévia.

## Onde aparece

- Aula 25 — *Como o Computador Lê o seu Código - Parte 1* `aulas/introducao-a-computacao/arquitetura-computadores-e-sistemas-operacionais/25-como-o-computador-le-o-codigo-parte-1/canonica.md`
- Conceitos vizinhos: [[linguagem-de-maquina]], [[compilador]], [[interpretador]]

## Fontes

- Slides SEED da aula 25 (`lake/introducao-a-computacao/AULA 25_INTRODUÇÃO A COMPUTAÇÃO.pptx`), slides 9 e 13: contraste entre linguagem de alto nível e linguagem de máquina.
- Base da canônica aprovada da aula 25, bloco :::conceito Linguagem de alto nível.
