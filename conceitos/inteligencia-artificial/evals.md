---
conceito: Evals
slug: evals
disciplina: inteligencia-artificial
tipo: conceito
aka: [eval, avaliação de IA, evaluation]
status: vivo
fontes:
  - aulas/inteligencia-artificial/fundamentos-de-ia/24-evals-e-economia-de-tokens/canonica.md
aulas: [24]
atualizado_em: 2026-06-15
---

Eval é uma forma **sistemática** de medir a qualidade das respostas de uma IA — em vez de confiar no "achei que ficou bom". Monta-se um conjunto de casos com gabarito e critérios claros, e mede-se quanto a IA acerta. É o equivalente, para IA, ao **teste** que se roda no código antes de confiar nele.

## Em uma frase

Medir a qualidade da IA com método (casos + gabarito), em vez de avaliar no olho.

## O que precisa saber

Avaliar "no olho" engana: a impressão é subjetiva e dá para piorar sem perceber. Junto com qualidade, o profissional acompanha o **custo**, medido em [[tokens]] (entrada + saída são cobrados). Equilibrar qualidade × custo é o que transforma protótipo em produto — e reforça a regra "menos contexto, porém mais relevante" ([[context-engineering]]), que economiza e melhora.

## Erros comuns

- Avaliar mudanças "no olho" sem um conjunto fixo de casos — vira adivinhação.

## Onde aparece

- Aula 24 — *Evals e Economia de Tokens*
- Conceitos vizinhos: [[tokens]], [[context-engineering]], [[alucinacoes]]

## Fontes

- Canônica da Aula 24 (modo Tema).
