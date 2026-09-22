---
conceito: Guardrails
slug: guardrails
disciplina: inteligencia-artificial
tipo: conceito
aka: [freios de segurança, guarda-corpos, políticas do agente]
status: vivo
fontes:
  - aulas/inteligencia-artificial/fundamentos-de-ia/21-harness-engineering/canonica.md
  - lake/inteligencia-artificial/elite-wiki/_transcricoes/encontro-elite-03-transcricao.md
  - lake/inteligencia-artificial/elite-wiki/_transcricoes/encontro-elite-05-transcricao.md
  - lake/inteligencia-artificial/elite-wiki/_transcricoes/Encontro_Elite_06_resumo_e_transcricao.pdf
aulas: [21]
atualizado_em: 2026-09-21
---

Guardrails são as **regras do que um [[agente]] pode e não pode fazer** — os freios de segurança dentro do [[harness]]. Exemplos: não apagar arquivos importantes, não gastar acima de um limite, pedir **aprovação humana** antes de ações sérias. São o cinto de segurança da IA que age.

## Em uma frase

Os freios que limitam o que o agente pode fazer e exigem aprovação humana em ações sérias.

## O que precisa saber

Quanto mais autônomo o [[agente]], mais essenciais os guardrails — sem eles, um agente pode causar estrago em escala (apagar dados, gastar demais, agir errado). Incluem limites de custo, listas de permissão e *human approval gates* (pontos em que um humano precisa aprovar). Fazem parte da infraestrutura do [[harness]]. A aplicação técnica desses limites é o campo de [[seguranca-de-agentes]].

## Erros comuns

- Dar autonomia ao agente sem freios, confiando que "vai dar tudo certo".

## Onde aparece

- Aula 21 — *Harness Engineering*
- `aulas/inteligencia-artificial/fundamentos-de-ia/21-harness-engineering/canonica.md`
- Conceitos vizinhos: [[harness]], [[agente]], [[seguranca-de-agentes]], [[ia-proativa]], [[handoff-humano]]

## Fontes

- Canônica da Aula 21 (modo Material).
