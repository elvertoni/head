---
conceito: Tool Use
slug: tool-use
disciplina: inteligencia-artificial
tipo: conceito
aka: [function calling, uso de ferramentas, chamada de funções]
status: vivo
fontes:
  - lake/inteligencia-artificial/elite-wiki/_transcricoes/encontro-elite-01-transcricao.md
  - lake/inteligencia-artificial/elite-wiki/_transcricoes/encontro-elite-03-transcricao.md
  - lake/inteligencia-artificial/elite-wiki/_transcricoes/encontro-elite-04-transcricao.md
  - lake/inteligencia-artificial/elite-wiki/_transcricoes/encontro-elite-05-transcricao.md
  - lake/inteligencia-artificial/elite-wiki/_transcricoes/Encontro_Elite_06_resumo_e_transcricao.pdf
  - lake/inteligencia-artificial/elite-wiki/_transcricoes/Encontro_Elite_09_resumo_e_transcricao.pdf
  - "lake/inteligencia-artificial/elite-wiki/_transcricoes/Imersão IA para Devs PycodeBR [Aula 01] - 2026_04_22 17_49 GMT-03_00 - Anotações do Gemini.docx"
aulas: [19, 20, 21]
atualizado_em: 2026-09-21
---

Tool use (function calling) é a capacidade de um [[llm]] **chamar ferramentas** para fazer o que sozinho não consegue: calcular, buscar na web, ler arquivos, enviar mensagens. O segredo: o modelo **não executa** — ele gera, num formato estruturado, o pedido "use a ferramenta X com estes dados", e um sistema externo ([[harness]]) executa de verdade.

## Em uma frase

O modelo pede uma ação em formato estruturado; o sistema executa e devolve o resultado.

## O que precisa saber

O LLM só gera texto (inclusive o texto que pede a ação) — quem executa é o sistema ao redor. O pedido precisa ser **estruturado** (qual ferramenta, quais dados). Ferramentas compensam limitações do modelo: calculadora para contas, busca para o [[cutoff]], [[rag]] para material próprio. É como o [[agente]] age no mundo, e o [[mcp]] é um padrão para conectar essas ferramentas. Um [[hub-de-integracoes]] pode administrar várias delas, desde que os escopos sejam controlados por [[seguranca-de-agentes]].

## Erros comuns

- "O modelo roda o código/acessa a internet sozinho" — ele pede; o sistema faz.

## Onde aparece
- [[segundo-cerebro]] — vault pessoal versionado como memória de longo prazo do agente

- Aula 19 — *Tool Use e Function Calling*
- `aulas/inteligencia-artificial/fundamentos-de-ia/19-tool-use-e-function-calling/canonica.md`
- `aulas/inteligencia-artificial/fundamentos-de-ia/20-mcp-model-context-protocol/canonica.md`
- `aulas/inteligencia-artificial/fundamentos-de-ia/21-harness-engineering/canonica.md`
- Conceitos vizinhos: [[agente]], [[llm]], [[mcp]], [[harness]], [[hub-de-integracoes]], [[seguranca-de-agentes]], [[handoff-humano]]

## Fontes

- Canônica da Aula 19 (modo Tema).
