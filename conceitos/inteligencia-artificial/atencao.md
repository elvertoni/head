---
conceito: Atenção
slug: atencao
disciplina: inteligencia-artificial
tipo: conceito
aka: [attention, mecanismo de atenção, self-attention]
status: vivo
fontes:
  - aulas/inteligencia-artificial/fundamentos-de-ia/11-transformers-e-atencao/canonica.md
aulas: [11]
atualizado_em: 2026-06-15
---

Atenção é o mecanismo que permite a um modelo, ao processar uma palavra, **pesar quais outras palavras do texto importam** para entendê-la. Ao processar "ela" em "colocou o livro na mochila porque ela estava pesada", a atenção ilumina "mochila" mais que "livro". É o coração do [[transformers|transformer]].

## Em uma frase

Pesar, para cada palavra, quais outras do contexto importam — como um marca-texto do que é relevante.

## O que precisa saber

A atenção age sobre todas as palavras **simultaneamente** (em paralelo), o que diferencia o transformer dos modelos antigos que liam em fila. É o que dá ao [[llm]] a noção de contexto. Consequência prática: dar **mais e melhor contexto** num prompt melhora a resposta (ver [[context-engineering]] adiante na trilha).

## Erros comuns

- Confundir com "ler em ordem" — a atenção avalia relações entre todas as palavras de uma vez.

## Onde aparece

- Aula 11 — *Transformers e Atenção*
- Conceitos vizinhos: [[transformers]], [[llm]], [[context-engineering]]

## Fontes

- Canônica da Aula 11 (modo Tema).
