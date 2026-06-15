---
conceito: Tokens
slug: tokens
disciplina: inteligencia-artificial
tipo: conceito
aka: [token, tokenização, tokenizador]
status: vivo
fontes:
  - aulas/inteligencia-artificial/fundamentos-de-ia/10-tokens-embeddings-e-vetores/canonica.md
aulas: [10]
atualizado_em: 2026-06-15
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
- Conceitos vizinhos: [[llm]], [[embeddings]]

## Fontes

- Canônica da Aula 10 (modo Tema).
