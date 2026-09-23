---
conceito: Interpretador
slug: interpretador
disciplina: introducao-a-computacao
tipo: conceito
aka: [interpreter]
status: rascunho
fontes:
  - "lake/introducao-a-computacao/AULA 25_INTRODUÇÃO A COMPUTAÇÃO.pptx"
  - "lake/introducao-a-computacao/AULA 26_INTRODUÇÃO A COMPUTAÇÃO.pptx"
aulas: [25, 26]
atualizado_em: 2026-09-22
---

Interpretador é um tradutor de código que converte e executa cada instrução em [[linguagem-de-alto-nivel]] linha por linha, durante a própria execução do programa: lê uma instrução, traduz para [[linguagem-de-maquina]], executa na hora, e só então segue para a próxima.

## Em uma frase

Interpretador traduz e executa o código uma linha de cada vez, em tempo real.

## O que precisa saber

Como não existe etapa de tradução separada antes de rodar, o interpretador oferece um ciclo de teste imediato: mudou o código, roda de nova na hora, o que acelera muito a [[depuracao]] e o aprendizado. O custo é velocidade de execução — como a tradução se repete a cada execução, um programa interpretado costuma rodar mais devagar que o mesmo programa já compilado por um [[compilador]]. Essa troca não é um veredito de qual estratégia é "melhor": é um trade-off entre agilidade de teste e desempenho final, e a escolha depende de em que etapa do projeto o desenvolvedor está. Linguagens como Python e Java, na prática, combinam as duas estratégias: compilam para [[bytecode]] e depois interpretam ou executam esse formato intermediário.

## Erros comuns

- Concluir que interpretador é "pior" só porque costuma ser mais lento na execução — a agilidade de testar e corrigir código vale mais que alguns milissegundos de execução em contextos de aprendizado e prototipação.
- Achar que um interpretador nunca compila nada — muitas implementações compilam o código para um formato intermediário antes de interpretá-lo.

## Onde aparece

- Aula 25 — *Como o Computador Lê o seu Código - Parte 1* `aulas/introducao-a-computacao/arquitetura-computadores-e-sistemas-operacionais/25-como-o-computador-le-o-codigo-parte-1/canonica.md`
- Aula 26 — *Como o Computador Lê o seu Código - Parte 2* `aulas/introducao-a-computacao/arquitetura-computadores-e-sistemas-operacionais/26-como-o-computador-le-o-codigo-parte-2/canonica.md`
- Conceitos vizinhos: [[compilador]], [[depuracao]], [[linguagem-de-maquina]], [[bytecode]]

## Fontes

- Slides SEED da aula 25 (`lake/introducao-a-computacao/AULA 25_INTRODUÇÃO A COMPUTAÇÃO.pptx`), slide 16, e da aula 26 (`lake/introducao-a-computacao/AULA 26_INTRODUÇÃO A COMPUTAÇÃO.pptx`), slides 12–13: tradução linha a linha e o ganho em depuração.
- Base da canônica aprovada das aulas 25 e 26, blocos :::conceito Interpretador e :::atencao "Erro comum" da aula 26.
