---
conceito: Context Engineering
slug: context-engineering
disciplina: inteligencia-artificial
tipo: conceito
aka: [engenharia de contexto, context engineering]
status: vivo
fontes:
  - aulas/inteligencia-artificial/fundamentos-de-ia/15-context-engineering/canonica.md
  - lake/inteligencia-artificial/ia-coders/o-que-e-context-engineering.md
aulas: [15]
atualizado_em: 2026-06-15
---

Context engineering é decidir **o que colocar junto da pergunta** ao [[llm]]: quais instruções, documentos, exemplos e histórico entram, e em que ordem. Se o [[prompt-engineering]] é "como perguntar", o context engineering é "o que vai ao lado". Tese central: o modelo não sabe nada além do que está no contexto — "contexto é o novo código".

## Em uma frase

Montar o que entra na janela de contexto — o input certo determina a qualidade da resposta.

## O que precisa saber

Tudo entra na **janela de contexto** (medida em [[tokens]]), que é limitada. Encher de coisa irrelevante dilui a atenção ("lost in the middle"), piora a resposta e custa mais: vale **menos contexto, porém mais relevante**. O modelo presta mais atenção aos extremos (começo/fim). Resolve o [[cutoff]] ao fornecer material fresco; o [[rag]] é a forma automática de fazer isso.

## Erros comuns

- "Colar tudo pra garantir" (context stuffing) — dilui atenção, piora e encarece.

## Onde aparece

- Aula 15 — *Context Engineering*
- Conceitos vizinhos: [[prompt-engineering]], [[llm]], [[tokens]], [[cutoff]], [[rag]], [[atencao]]

## Fontes

- Canônica da Aula 15 (modo Material); transcrição do curso ia-coders (lake).
