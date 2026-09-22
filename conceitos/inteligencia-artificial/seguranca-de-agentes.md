---
conceito: Segurança de agentes
slug: seguranca-de-agentes
disciplina: inteligencia-artificial
tipo: conceito
aka: [segurança de agentes, segurança de agentes de IA, agent security]
status: rascunho
fontes:
  - lake/inteligencia-artificial/elite-wiki/_transcricoes/encontro-elite-03-transcricao.md
  - lake/inteligencia-artificial/elite-wiki/_transcricoes/encontro-elite-05-transcricao.md
  - lake/inteligencia-artificial/elite-wiki/_transcricoes/Encontro_Elite_06_resumo_e_transcricao.pdf
  - lake/inteligencia-artificial/elite-wiki/agentes/encontros-elite/encontro-elite-03-deploy-monitoria-e-observabilidade-de-sistemas-com-ia-parte-1.md
  - lake/inteligencia-artificial/elite-wiki/agentes/encontros-elite/encontro-elite-05-integracoes-e-automacoes-de-ia-com-hermes-agent-parte-1.md
aulas: []
atualizado_em: 2026-09-21
---

Segurança de agentes é delimitar as ferramentas, os dados e as ações que um agente pode usar para que sua autonomia não produza impacto sem controle. O desenho combina [[guardrails]], princípio do menor privilégio, autenticação, isolamento por finalidade e aprovação humana para ações destrutivas ou públicas.

## Em uma frase

Dar autonomia ao agente dentro de limites verificáveis de ferramenta, dados e ação.

## O que precisa saber

Conteúdo externo pode tentar redirecionar o agente por meio de [[prompt-engineering|prompt injection]]. Por isso, cada perfil deve receber apenas as ferramentas necessárias; acesso a shell, escrita ampla e credenciais administrativas precisam ser exceções explícitas. Um servidor [[mcp]] deve exigir autenticação e expor operações com escopo pequeno.

O controle também acontece no fluxo: ações irreversíveis, publicações e mudanças em produção passam por um ponto de aprovação. Em atendimento, o [[handoff-humano]] transfere casos fora do escopo para uma pessoa. A curadoria humana reduz o impacto de uma falha do modelo, mas não substitui limites técnicos no [[harness]].

## Erros comuns

- Dar acesso total ao sistema por padrão porque o agente é mais conveniente assim.
- Expor um servidor MCP sem autenticação ou com operações administrativas desnecessárias.
- Colocar chaves de API em prompts, transcrições ou commits.
- Automatizar publicação sem uma etapa de revisão e sem limite de repetição.

## Onde aparece

- Lacuna catalogada a partir do Encontro Elite #05; candidata a complemento das aulas sobre [[agente]], [[tool-use]] e [[guardrails]].
- Conceitos vizinhos: [[harness]], [[mcp]], [[ia-proativa]], [[loop-engineering]]

## Fontes

- `_transcricoes/encontro-elite-03` — autenticação do MCP da aplicação e cuidado com exposição de dados.
- `_transcricoes/encontro-elite-05` — perfis por finalidade, remoção de shell, OAuth e curadoria antes da publicação.
