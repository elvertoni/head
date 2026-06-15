---
conceito: Cutoff
slug: cutoff
disciplina: inteligencia-artificial
tipo: conceito
aka: [data de corte, knowledge cutoff, cutoff de conhecimento]
status: vivo
fontes:
  - aulas/inteligencia-artificial/fundamentos-de-ia/12-treino-fine-tuning-e-cutoff/canonica.md
aulas: [12]
atualizado_em: 2026-06-15
---

Cutoff é a **data até onde vão os dados de treino** de um [[llm]]. Tudo que aconteceu depois o modelo não conhece, porque não estava nos textos com que treinou. É como um livro impresso: só contém o que se sabia até ir para a gráfica. Por isso o modelo "não sabe" notícias recentes.

## Em uma frase

A data em que o conhecimento do modelo congela; eventos posteriores são desconhecidos.

## O que precisa saber

O LLM **não aprende sozinho** com as conversas — o conhecimento fica fixado no treino e congelado no cutoff. Para "saber" algo novo, é preciso retreinar (caro) ou fornecer a informação na hora, via prompt ou [[rag]]. É justamente o cutoff que motiva a existência de busca e RAG. Em 2026 as versões mudam rápido para empurrar o cutoff adiante, mas sempre há um limite.

## Erros comuns

- "O LLM aprende com nossas conversas em tempo real" — não; o conhecimento é congelado no cutoff.
- Confiar em datas/eventos recentes dados pelo modelo sem checar.

## Onde aparece

- Aula 12 — *Treino, Fine-tuning e Cutoff*
- Conceitos vizinhos: [[llm]], [[fine-tuning]], [[rag]], [[alucinacoes]]

## Fontes

- Canônica da Aula 12 (modo Tema).
