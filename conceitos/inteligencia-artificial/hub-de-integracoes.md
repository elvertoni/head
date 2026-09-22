---
conceito: Hub de integrações
slug: hub-de-integracoes
disciplina: inteligencia-artificial
tipo: conceito
aka: [hub de integrações, broker de integrações, integration hub]
status: rascunho
fontes:
  - lake/inteligencia-artificial/elite-wiki/_transcricoes/encontro-elite-05-transcricao.md
  - lake/inteligencia-artificial/elite-wiki/agentes/encontros-elite/encontro-elite-05-integracoes-e-automacoes-de-ia-com-hermes-agent-parte-1.md
  - lake/inteligencia-artificial/elite-wiki/_transcricoes/Encontro_Elite_06_resumo_e_transcricao.pdf
aulas: []
atualizado_em: 2026-09-21
---

Hub de integrações é uma camada que centraliza a conexão, autenticação e descoberta de vários serviços externos usados por um agente. Ele reduz integrações ponto a ponto e pode oferecer interfaces como CLI e [[mcp]], mas continua sujeito a permissões, limites e falhas de cada serviço.

## Em uma frase

Uma camada comum para conectar e administrar várias ferramentas externas de um agente.

## O que precisa saber

O hub concentra OAuth, contas, conectores e operações reutilizáveis. A escolha entre CLI, MCP ou API direta depende de quem chama a integração, da necessidade de trocar contas e do nível de controle exigido. [[tool-use]] define a ação; o hub fornece parte das ferramentas e credenciais para executá-la.

Centralizar reduz configuração repetida, mas aumenta o impacto de uma permissão ampla ou de uma falha no broker. O desenho deve aplicar [[seguranca-de-agentes]], escopos mínimos e revogação por serviço.

## Erros comuns

- Tratar o hub como substituto de autenticação, governança ou revisão de permissões.
- Conceder acesso a todas as contas e operações para simplificar a configuração.
- Escolher MCP ou CLI sem testar troca de contas, limites e recuperação de falhas.
- Codificar o nome de um produto como se fosse o conceito arquitetural.

## Onde aparece

- Encontro Elite #05; Composio é o exemplo de fonte, enquanto o conceito é o padrão de integração.
- Conceitos vizinhos: [[mcp]], [[tool-use]], [[harness]], [[seguranca-de-agentes]]

## Fontes

- `_transcricoes/encontro-elite-05` — hub de integrações, comparação CLI/MCP e autenticação OAuth.
- `agentes/encontros-elite/encontro-elite-05` — conexão de serviços e automação de conteúdo.
