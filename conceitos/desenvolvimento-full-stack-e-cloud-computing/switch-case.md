---
conceito: Switch case
slug: switch-case
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [estrutura switch]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Padrões Web - HTML e CSS/07 - Aula 7 - Switch Case - Resumo (Aula em PDF).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Switch case é uma estrutura de seleção que compara uma expressão com vários casos e executa o bloco correspondente. break interrompe a continuação para o caso seguinte e default trata valores sem correspondência.

## Em uma frase

Switch organiza várias alternativas baseadas no valor de uma expressão.

## O que precisa saber

Ele é uma alternativa a cadeias longas de [[estruturas-condicionais]] quando a decisão depende de valores discretos. O comportamento de comparação e a necessidade de break devem ser explícitos; casos podem ser agrupados quando compartilham uma ação.

## Erros comuns

- Esquecer break e provocar fall-through involuntário.
- Usar switch para condições relacionais complexas.
- Omitir default quando entradas inesperadas são possíveis.

## Onde aparece

- Aula 7 — Switch Case.
- É uma forma de [[estruturas-condicionais]] em [[javascript]].

## Fontes

- Resumo da Aula 7, páginas 1–6: cases, break e default.
