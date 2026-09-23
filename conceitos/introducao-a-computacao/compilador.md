---
conceito: Compilador
slug: compilador
disciplina: introducao-a-computacao
tipo: conceito
aka: [compiler]
status: rascunho
fontes:
  - "lake/introducao-a-computacao/AULA 25_INTRODUÇÃO A COMPUTAÇÃO.pptx"
  - "lake/introducao-a-computacao/AULA 26_INTRODUÇÃO A COMPUTAÇÃO.pptx"
aulas: [25, 26]
atualizado_em: 2026-09-22
---

Compilador é um tradutor de código que converte todo o código-fonte escrito em [[linguagem-de-alto-nivel]] para [[linguagem-de-maquina]] de uma só vez, antes da execução, gerando um arquivo executável. A tradução acontece uma única vez; depois disso, o executável roda quantas vezes for preciso sem passar de novo pelo compilador.

## Em uma frase

Compilador traduz o programa inteiro antes de rodar e entrega um executável pronto.

## O que precisa saber

O trade-off central do compilador é tempo de tradução contra velocidade de execução: como o binário já está pronto, o programa executa direto, sem parar para traduzir — por isso é a escolha típica quando desempenho final e distribuição fechada do código-fonte importam. O custo é que qualquer mudança exige recompilar tudo antes de testar de novo, o que torna o ciclo de teste mais lento que o de um [[interpretador]]. Muitas linguagens modernas não são puramente uma coisa ou outra: compilam o código para um formato intermediário — [[bytecode]] — que depois é interpretado ou executado por uma máquina virtual, combinando parte da agilidade do interpretador com parte da velocidade do compilador.

## Erros comuns

- Decorar pares fixos como "C é compilado, Python é interpretado" como se cada linguagem usasse só uma estratégia — muitas linguagens compilam para um formato intermediário e depois interpretam esse formato.
- Esperar que erros de um programa compilado apareçam durante a execução, como no interpretador — parte deles é detectada já na compilação, antes de o programa rodar.

## Onde aparece

- Aula 25 — *Como o Computador Lê o seu Código - Parte 1* `aulas/introducao-a-computacao/arquitetura-computadores-e-sistemas-operacionais/25-como-o-computador-le-o-codigo-parte-1/canonica.md`
- Aula 26 — *Como o Computador Lê o seu Código - Parte 2* `aulas/introducao-a-computacao/arquitetura-computadores-e-sistemas-operacionais/26-como-o-computador-le-o-codigo-parte-2/canonica.md`
- Conceitos vizinhos: [[interpretador]], [[linguagem-de-maquina]], [[linguagem-de-alto-nivel]], [[bytecode]], [[depuracao]]

## Fontes

- Slides SEED da aula 25 (`lake/introducao-a-computacao/AULA 25_INTRODUÇÃO A COMPUTAÇÃO.pptx`), slide 15, e da aula 26 (`lake/introducao-a-computacao/AULA 26_INTRODUÇÃO A COMPUTAÇÃO.pptx`), slides 9 e 11: definição de compilador e vantagem de desempenho por tradução única.
- Base da canônica aprovada das aulas 25 e 26, blocos :::conceito Compilador e :::atencao sobre a divisão "compilado × interpretado".
