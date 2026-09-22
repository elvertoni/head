---
conceito: Observabilidade de agentes
slug: observabilidade-de-agentes
disciplina: inteligencia-artificial
tipo: conceito
aka: [observabilidade de agentes, agent observability]
status: rascunho
fontes:
  - lake/inteligencia-artificial/elite-wiki/_transcricoes/encontro-elite-03-transcricao.md
  - lake/inteligencia-artificial/elite-wiki/_transcricoes/encontro-elite-04-transcricao.md
  - lake/inteligencia-artificial/elite-wiki/_transcricoes/encontro-elite-05-transcricao.md
  - lake/inteligencia-artificial/elite-wiki/_transcricoes/Encontro_Elite_06_resumo_e_transcricao.pdf
  - lake/inteligencia-artificial/elite-wiki/_transcricoes/Encontro_Elite_08_resumo_e_transcricao.pdf
  - lake/inteligencia-artificial/elite-wiki/_transcricoes/Encontro_Elite_09_resumo_e_transcricao.pdf
  - lake/inteligencia-artificial/elite-wiki/agentes/encontros-elite/encontro-elite-03-deploy-monitoria-e-observabilidade-de-sistemas-com-ia-parte-1.md
  - lake/inteligencia-artificial/elite-wiki/agentes/encontros-elite/encontro-elite-04-deploy-monitoria-e-observabilidade-de-sistemas-com-ia-parte-2.md
  - lake/inteligencia-artificial/elite-wiki/agentes/encontros-elite/encontro-elite-05-integracoes-e-automacoes-de-ia-com-hermes-agent-parte-1.md
aulas: []
atualizado_em: 2026-09-21
---

Observabilidade de agentes é acompanhar o que um agente recebeu, decidiu, chamou, gastou e produziu para inferir seu estado e diagnosticar falhas. Ela combina [[observabilidade]], logs, métricas, eventos de ferramenta, custos em [[tokens]] e avaliações de qualidade.

## Em uma frase

Tornar visível o caminho do agente para explicar comportamento, custo e falhas.

## O que precisa saber

Monitoramento mostra indicadores; observabilidade ajuda a investigar por que um resultado aconteceu. Para um agente, isso inclui chamadas de ferramentas, duração, erros, contexto usado, tentativas do [[loop-engineering]], tokens e efeito da ação. Dashboards e integrações MCP podem facilitar a consulta, mas não substituem retenção, controle de acesso e perguntas operacionais claras.

O objetivo não é coletar tudo. Alertas precisam de limiar, responsável e ação; excesso de alertas produz alert fatigue e reduz a atenção da equipe.

## Erros comuns

- Medir apenas disponibilidade da infraestrutura e ignorar decisões e chamadas do agente.
- Coletar prompts, logs e dados pessoais sem retenção ou controle de acesso.
- Criar dashboards sem definir qual decisão cada indicador apoia.
- Confundir mais alertas com mais confiabilidade.

## Onde aparece

- Encontros Elite #03–#05; material candidato a complementar [[evals]], [[mcp]] e [[harness]].
- Conceitos vizinhos: [[observabilidade]], [[monitoramento]], [[logging]], [[tokens]], [[seguranca-de-agentes]]

## Fontes

- `_transcricoes/encontro-elite-03` e `_04` — métricas, logs, Grafana, MCP e investigação de sistemas.
- `_transcricoes/encontro-elite-05` — portal central, relatórios de automação e custo operacional.
