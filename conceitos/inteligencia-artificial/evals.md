---
conceito: Evals
slug: evals
disciplina: inteligencia-artificial
tipo: conceito
aka: [eval, avaliação de IA, evaluation]
status: vivo
fontes:
  - lake/inteligencia-artificial/elite-wiki/_transcricoes/encontro-elite-04-transcricao.md
  - lake/inteligencia-artificial/elite-wiki/_transcricoes/encontro-elite-05-transcricao.md
  - lake/inteligencia-artificial/elite-wiki/_transcricoes/Encontro_Elite_09_resumo_e_transcricao.pdf
aulas: [24]
atualizado_em: 2026-09-21
---

Eval é uma forma **sistemática** de medir a qualidade das respostas de uma IA — em vez de confiar no "achei que ficou bom". Monta-se um conjunto de casos com gabarito e critérios claros, e mede-se quanto a IA acerta. É o equivalente, para IA, ao **teste** que se roda no código antes de confiar nele.

## Em uma frase

Medir a qualidade da IA com método (casos + gabarito), em vez de avaliar no olho.

## O que precisa saber

Avaliar "no olho" engana: a impressão é subjetiva e dá para piorar sem perceber. Junto com qualidade, o profissional acompanha o **custo**, medido em [[tokens]] (entrada + saída são cobrados). Em agentes, os casos de teste devem incluir chamadas de ferramenta, falhas e efeitos observáveis; [[observabilidade-de-agentes]] fornece evidência para investigar o resultado. Equilibrar qualidade × custo é o que transforma protótipo em produto — e reforça a regra "menos contexto, porém mais relevante" ([[context-engineering]]), que economiza e melhora.

## Erros comuns

- Avaliar mudanças "no olho" sem um conjunto fixo de casos — vira adivinhação.

## Onde aparece

- Aula 24 — *Evals e Economia de Tokens*
- `aulas/inteligencia-artificial/fundamentos-de-ia/24-evals-e-economia-de-tokens/canonica.md`
- Conceitos vizinhos: [[tokens]], [[context-engineering]], [[alucinacoes]], [[observabilidade-de-agentes]], [[loop-engineering]], [[selecao-de-modelo]]

## Fontes

- Canônica da Aula 24 (modo Tema).
