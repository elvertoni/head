---
conceito: IA proativa
slug: ia-proativa
disciplina: inteligencia-artificial
tipo: conceito
aka: [IA proativa, inteligência artificial proativa, proactive AI]
status: rascunho
fontes:
  - lake/inteligencia-artificial/elite-wiki/_transcricoes/encontro-elite-05-transcricao.md
  - lake/inteligencia-artificial/elite-wiki/_transcricoes/Encontro_Elite_06_resumo_e_transcricao.pdf
  - lake/inteligencia-artificial/elite-wiki/_transcricoes/Encontro_Elite_08_resumo_e_transcricao.pdf
  - lake/inteligencia-artificial/elite-wiki/agentes/encontros-elite/encontro-elite-05-integracoes-e-automacoes-de-ia-com-hermes-agent-parte-1.md
aulas: []
atualizado_em: 2026-09-21
---

IA proativa é o comportamento de um [[agente]] que acompanha sinais autorizados, identifica uma condição relevante e inicia uma ação sem esperar um pedido explícito. Ela depende de gatilhos, contexto suficiente, limites de execução e uma política clara para decidir quando preparar um rascunho, pedir aprovação ou agir.

## Em uma frase

O agente observa sinais permitidos e age antes de o usuário formular um pedido.

## O que precisa saber

O fluxo típico combina monitoramento de e-mail, CRM, calendário ou conversas com uma regra de decisão e uma ação delimitada. O resultado pode ser um alerta, um relatório, um rascunho ou uma execução. [[harness]], [[evals]] e [[seguranca-de-agentes]] definem como medir, interromper e revisar esse comportamento.

Proatividade não é executar tudo automaticamente. Quanto maior o impacto da ação, mais necessário é um ponto de aprovação humana, uma condição de parada e registro do motivo que disparou o fluxo. Em atendimento, o fluxo deve permitir [[handoff-humano]] quando a conversa sair do escopo.

## Erros comuns

- Confundir um cron que executa sempre a mesma tarefa com decisão proativa baseada em sinais.
- Monitorar fontes demais e produzir ruído, custo e alertas que ninguém revisa.
- Publicar ou alterar dados sem aprovação, escopo e trilha de auditoria.
- Criar gatilhos sem limite de frequência ou condição de parada.

## Onde aparece

- Encontro Elite #05; material candidato a enriquecer [[ai-first-vs-ai-enabled]] e a Aula 22.
- Conceitos vizinhos: [[agente]], [[harness]], [[seguranca-de-agentes]], [[observabilidade-de-agentes]]

## Fontes

- `_transcricoes/encontro-elite-05` — monitoramento contínuo, geração de conteúdo e distinção entre IA reativa e proativa.
- `agentes/encontros-elite/encontro-elite-05` — pipeline de conteúdo com revisão humana antes da publicação.
