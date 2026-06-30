---
conceito: Agente de IA
slug: agente
disciplina: inteligencia-artificial
tipo: conceito
aka: [agente, AI agent, agentes, subagentes]
status: vivo
fontes:
  - aulas/inteligencia-artificial/fundamentos-de-ia/18-agentes-e-subagentes/canonica.md
aulas: [18]
atualizado_em: 2026-06-15
---

Agente de IA é um sistema que usa um [[llm]] não só para responder, mas para **perseguir um objetivo agindo**: decide os passos, executa ações e ajusta o rumo até concluir. O chatbot responde e para; o agente entra num **loop** (observar → pensar → agir → repetir) até terminar a tarefa.

## Em uma frase

IA que age em ciclo rumo a um objetivo, em vez de só responder e parar.

## O que precisa saber

Como o agente age é via [[tool-use]] (chamar ferramentas). Tarefas grandes usam **subagentes**: um orquestrador divide o trabalho entre agentes especializados. Risco real: sem **condição de parada** e [[guardrails]], o agente pode entrar em loop infinito. Toda a infra que faz o agente funcionar é o [[harness]]. Mais autonomia = menos controle.

## Erros comuns

- Confundir agente com chatbot (um age em ciclo; o outro responde e para).
- Dar autonomia sem freios — risco de loop infinito e ações erradas em escala.

## Onde aparece
- [[segundo-cerebro]] — vault pessoal versionado como memória de longo prazo do agente

- Aula 18 — *Agentes e Subagentes*
- Conceitos vizinhos: [[llm]], [[tool-use]], [[harness]], [[guardrails]]

## Fontes

- Canônica da Aula 18 (modo Tema).
