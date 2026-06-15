---
conceito: Tool Use
slug: tool-use
disciplina: inteligencia-artificial
tipo: conceito
aka: [function calling, uso de ferramentas, chamada de funções]
status: vivo
fontes:
  - aulas/inteligencia-artificial/fundamentos-de-ia/19-tool-use-e-function-calling/canonica.md
aulas: [19]
atualizado_em: 2026-06-15
---

Tool use (function calling) é a capacidade de um [[llm]] **chamar ferramentas** para fazer o que sozinho não consegue: calcular, buscar na web, ler arquivos, enviar mensagens. O segredo: o modelo **não executa** — ele gera, num formato estruturado, o pedido "use a ferramenta X com estes dados", e um sistema externo ([[harness]]) executa de verdade.

## Em uma frase

O modelo pede uma ação em formato estruturado; o sistema executa e devolve o resultado.

## O que precisa saber

O LLM só gera texto (inclusive o texto que pede a ação) — quem executa é o sistema ao redor. O pedido precisa ser **estruturado** (qual ferramenta, quais dados). Ferramentas compensam limitações do modelo: calculadora para contas, busca para o [[cutoff]], [[rag]] para material próprio. É como o [[agente]] age no mundo, e o [[mcp]] é um padrão para conectar essas ferramentas.

## Erros comuns

- "O modelo roda o código/acessa a internet sozinho" — ele pede; o sistema faz.

## Onde aparece

- Aula 19 — *Tool Use e Function Calling*
- Conceitos vizinhos: [[agente]], [[llm]], [[mcp]], [[harness]]

## Fontes

- Canônica da Aula 19 (modo Tema).
