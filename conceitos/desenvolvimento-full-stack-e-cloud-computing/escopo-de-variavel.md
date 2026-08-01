---
conceito: Escopo de variável
slug: escopo-de-variavel
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [escopo léxico]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Padrões Web - HTML e CSS/04 - Aula 4 - Variáveis, Comandos de Entrada e Saída e Operadores - Resumo (Aula em PDF).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Escopo de variável é a região do programa em que um nome pode ser resolvido e usado. Em JavaScript, blocos e funções criam limites importantes; a forma de declaração influencia se uma variável fica restrita ao bloco, à função ou a um escopo mais amplo.

## Em uma frase

Escopo define onde um nome existe e pode ser acessado.

## O que precisa saber

O escopo organiza dependências e reduz colisões entre nomes. [[var-let-const]] e [[variaveis-em-javascript]] explicam como as declarações alteram a visibilidade; funções e blocos podem esconder nomes externos. Entender escopo é essencial para prever efeitos em [[javascript]] e evitar estado global acidental.

## Erros comuns

- Esperar que uma variável declarada em um bloco esteja disponível fora dele.
- Criar dependência implícita de variáveis globais.
- Confundir escopo com o tempo de vida ou com o valor atual da variável.

## Onde aparece

- Aula 4 — Variáveis, Comandos de Entrada e Saída e Operadores.
- Explica parte do comportamento de [[variaveis-em-javascript]] e [[var-let-const]].

## Fontes

- Resumo da Aula 4, páginas 1–5: escopo e formas de declaração.
