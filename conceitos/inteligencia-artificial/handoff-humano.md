---
conceito: Handoff humano
slug: handoff-humano
disciplina: inteligencia-artificial
tipo: conceito
aka: [handoff humano, transferência para humano, human handoff]
status: rascunho
fontes:
  - lake/inteligencia-artificial/elite-wiki/_transcricoes/Encontro_Elite_06_resumo_e_transcricao.pdf
  - lake/inteligencia-artificial/elite-wiki/_transcricoes/Encontro_Elite_08_resumo_e_transcricao.pdf
aulas: []
atualizado_em: 2026-09-21
---

Handoff humano é a transferência explícita de uma conversa ou tarefa de um agente para uma pessoa quando o caso ultrapassa o escopo, a confiança ou a autorização definidos. O agente preserva o contexto necessário e sinaliza o ponto de transferência para que a pessoa continue sem recomeçar o atendimento.

## Em uma frase

Passar o controle ao humano no momento certo, com contexto suficiente para continuar a tarefa.

## O que precisa saber

O fluxo precisa declarar gatilhos: pedido de exceção, baixa confiança, assunto sensível, conflito, solicitação do cliente ou limite de tempo. O agente deve informar que transferiu, evitar agir em paralelo e registrar o estado. [[ia-proativa]] pode detectar o momento; [[seguranca-de-agentes]] define quando a transferência é obrigatória.

## Erros comuns

- Esconder a transferência e deixar a pessoa repetir todo o contexto.
- Transferir sem informar o motivo, o histórico e a próxima ação esperada.
- Manter o agente executando ações enquanto o humano assume o caso.
- Tratar handoff como falha do produto, em vez de projetá-lo como controle.

## Onde aparece

- Encontro Elite #06, no chatbot de atendimento com transição e retomada humana.
- Conceitos vizinhos: [[agente]], [[guardrails]], [[ia-proativa]], [[seguranca-de-agentes]]

## Fontes

- `Encontro_Elite_06_resumo_e_transcricao.pdf` — debouncer, transição para humanos e retomada do atendimento.
- `Encontro_Elite_08_resumo_e_transcricao.pdf` — projeto piloto com salvaguardas de revisão humana.
