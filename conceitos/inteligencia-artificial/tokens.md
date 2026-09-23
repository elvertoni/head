---
conceito: Tokens
slug: tokens
disciplina: inteligencia-artificial
tipo: conceito
aka: [token, tokenização, tokenizador]
status: vivo
fontes:
  - lake/inteligencia-artificial/elite-wiki/_transcricoes/Encontro_Elite_09_resumo_e_transcricao.pdf
  - "lake/inteligencia-artificial/elite-wiki/_transcricoes/Imersão IA para Devs PycodeBR [Aula 01] - 2026_04_22 17_49 GMT-03_00 - Anotações do Gemini.docx"
aulas: [10, 15, 17, 24]
atualizado_em: 2026-09-21
---

Token é a **unidade de texto** que um [[llm]] processa — pode ser uma palavra inteira, um pedaço de palavra ou um sinal de pontuação. Um tokenizador quebra o texto em tokens antes do modelo trabalhar e remonta no fim. Regra prática: **token não é palavra**.

## Em uma frase

O pedaço de texto que o modelo processa; uma palavra pode virar vários tokens.

## O que precisa saber

Palavras comuns viram um token; longas ou raras viram vários ("incrivelmente" → "incrivel" + "mente"). Contexto e custo de uma IA são medidos em tokens, não palavras — 1 milhão de tokens ≈ 750 mil palavras. Depois de tokenizado, cada token vira [[embeddings|vetor]] para o modelo capturar significado.

## Erros comuns

- Assumir "1 token = 1 palavra" — espaços, pontuação e subpalavras contam.

## Onde aparece

- Aula 10 — *Tokens, Embeddings e Vetores*
- Canônica: `aulas/inteligencia-artificial/fundamentos-de-ia/10-tokens-embeddings-e-vetores/canonica.md`
- Canônica: `aulas/inteligencia-artificial/fundamentos-de-ia/15-context-engineering/canonica.md`
- Canônica: `aulas/inteligencia-artificial/fundamentos-de-ia/17-chunking-embeddings-e-vector-stores/canonica.md`
- Canônica: `aulas/inteligencia-artificial/fundamentos-de-ia/24-evals-e-economia-de-tokens/canonica.md`
- Conceitos vizinhos: [[llm]], [[embeddings]], [[selecao-de-modelo]], [[provedor-de-modelo]]

## Fontes

- Canônica da Aula 10 (modo Tema).
