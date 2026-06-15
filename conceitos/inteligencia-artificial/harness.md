---
conceito: Harness
slug: harness
disciplina: inteligencia-artificial
tipo: conceito
aka: [harness engineering, infraestrutura do agente]
status: vivo
fontes:
  - aulas/inteligencia-artificial/fundamentos-de-ia/21-harness-engineering/canonica.md
  - lake/inteligencia-artificial/ia-coders/o-que-e-harness-engineering.md
aulas: [21]
atualizado_em: 2026-06-15
---

Harness é **toda a infraestrutura ao redor do [[llm]]**: o loop de decisão do [[agente]], as ferramentas que ele chama ([[tool-use]]), a memória, os [[guardrails]] e o feedback. O modelo sozinho é o **motor** (só gera texto); o harness é o **carro inteiro** que o faz agir no mundo de forma útil e controlada.

## Em uma frase

A infra ao redor do modelo (loop, ferramentas, memória, freios) que transforma o motor num carro.

## O que precisa saber

O modelo é stateless (recebe texto, devolve texto, não lembra, não age sozinho); o harness chama o modelo em loop, executa ferramentas, guarda estado, aplica [[guardrails]] e sabe parar. Tese central: **o salto da demo para a produção mora no harness**, não no modelo — mesmo modelo + harness melhor = resultado muito melhor. É por isso que ferramentas com o mesmo modelo por baixo entregam tão diferente.

## Erros comuns

- "O que importa é só o modelo, basta usar o melhor" — o diferencial está no harness.

## Onde aparece

- Aula 21 — *Harness Engineering*
- Conceitos vizinhos: [[llm]], [[agente]], [[tool-use]], [[guardrails]], [[mcp]]

## Fontes

- Canônica da Aula 21 (modo Material); transcrição ia-coders (lake).
