---
conceito: Funções de primeira classe
slug: funcoes-de-primeira-classe
disciplina: inovacao-inteligencia-artificial-e-robotica-educacional
tipo: conceito
aka: [first-class functions, funções como valores]
status: rascunho
fontes:
  - "lake/Inovacao-Inteligencia-Artificial-e-Robotica-Educacional/Módulo II - Inteligência Artificial/Conceitos Avançados em IA e Blockchain/01 - Aula 1 - Paradigmas de programação_ Lógico Funcional - Resumo (Aula em PDF).pdf"
  - "lake/Inovacao-Inteligencia-Artificial-e-Robotica-Educacional/Módulo II - Inteligência Artificial/Conceitos Avançados em IA e Blockchain/02 - Aula 2 - Paradigmas de programação_ Lógico Funcional II - Resumo (Aula em PDF).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Funções de primeira classe são funções tratadas como valores: podem ser armazenadas em variáveis, passadas como argumentos, retornadas por outras funções e combinadas para construir novos comportamentos. A ideia permite separar uma operação da decisão sobre quando e onde ela será aplicada.

## Em uma frase

Funções de primeira classe permitem usar funções como dados que circulam e são compostos pelo programa.

## O que precisa saber

Esse recurso é central para o [[paradigma-funcional|paradigma funcional]] e favorece composição, abstração e reutilização. Ele não exige que a linguagem seja puramente funcional, nem elimina efeitos colaterais: uma função pode carregar ou produzir efeitos dependendo do ambiente.

Funções como valores ajudam a expressar transformações sobre coleções, callbacks e estratégias variáveis. O ganho depende de nomes, tipos, testes e clareza; abstração excessiva pode tornar o fluxo difícil de acompanhar.

## Erros comuns

- Confundir função de primeira classe com função anônima ou método de uma classe.
- Achar que passar uma função como argumento torna o código automaticamente funcional.
- Esconder estado e efeitos dentro de funções e presumir que a composição é pura.

## Onde aparece

- Aulas 1–2 — Paradigmas de Programação: Lógico e Funcional, no Módulo II.
- É um recurso central do [[paradigma-funcional]] e do pensamento declarativo.

## Fontes

- Aula 1, página 6 do resumo em PDF: funções como valores e características funcionais.
- Aula 2, página 6 do resumo em PDF: funções, composição e efeitos colaterais.

