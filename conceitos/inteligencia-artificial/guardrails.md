---
conceito: Guardrails
slug: guardrails
disciplina: inteligencia-artificial
tipo: conceito
aka: [freios de segurança, guarda-corpos, políticas do agente]
status: vivo
fontes:
  - aulas/inteligencia-artificial/fundamentos-de-ia/21-harness-engineering/canonica.md
aulas: [21]
atualizado_em: 2026-06-15
---

Guardrails são as **regras do que um [[agente]] pode e não pode fazer** — os freios de segurança dentro do [[harness]]. Exemplos: não apagar arquivos importantes, não gastar acima de um limite, pedir **aprovação humana** antes de ações sérias. São o cinto de segurança da IA que age.

## Em uma frase

Os freios que limitam o que o agente pode fazer e exigem aprovação humana em ações sérias.

## O que precisa saber

Quanto mais autônomo o [[agente]], mais essenciais os guardrails — sem eles, um agente pode causar estrago em escala (apagar dados, gastar demais, agir errado). Incluem limites de custo, listas de permissão e *human approval gates* (pontos em que um humano precisa aprovar). Fazem parte da infraestrutura do [[harness]].

## Erros comuns

- Dar autonomia ao agente sem freios, confiando que "vai dar tudo certo".

## Onde aparece

- Aula 21 — *Harness Engineering*
- Conceitos vizinhos: [[harness]], [[agente]]

## Fontes

- Canônica da Aula 21 (modo Material).
