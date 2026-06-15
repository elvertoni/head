# Auditoria — Elite Wiki (referência para a trilha Fundamentos de IA)

> Auditoria multi-agente (4 especialistas em paralelo) sobre as 40 páginas extraídas do Notion "Elite Wiki" (curso pago, local-only em `lake/inteligencia-artificial/elite-wiki/`).
> Material é **referência** — informa as aulas, não vira cópia (a Canônica reescreve com voz própria).

## Taxonomia aplicada (8 pastas)

| Pasta | Arq. | Conteúdo |
|---|---|---|
| `fundamentos/` | 5 | conceito didático curto: o que é IA, prompt eng. básico, tags XML, MCP vs plugin vs skill, guia inicial |
| `prompts/` | 7 | bibliotecas e prompts exemplares (curados PycodeBR, SCSI, imersão, anti-IA, design system, landing page, conversar com IA) |
| `agentes/` | 5 | agentes pessoais, multi-agent Slack (Hermes), segundo cérebro + `encontros-elite/` (#01-03) |
| `arquitetura/` | 5 | blueprints (Django, RAG, chatbot WhatsApp), MentorIA PRD, arquitetura-base |
| `skills-ferramentas/` | 10 | toolkit `imersao-skills/` (5 skills + guia), setups, plugins, recursos |
| `workflows/` | 5 | SDD, validação de respostas, refatoração, checklist produção, imersão aula 02 |
| `_indice/` | 2 | mapas de navegação Notion (proveniência) |
| `_descartar/` | 1 | `sem-titulo.md` (stub vazio) |

## Peças de maior valor (ouro didático)

- **`prompts/prompts-curados-pycodebr.md`** — biblioteca-mestre de ~51 prompts XML mandatórios (PRD, RAG, agentes, code review, OWASP, LGPD, testes, deploy). Superset das demais bibliotecas. → aulas 14, 16, 18, 19, 24, 25.
- **`prompts/system-prompt-anti-ia.md`** — humanização de texto / "assinatura de IA". Único, transversal. → 14, 23.
- **`fundamentos/mcp-plugin-e-skill-o-que-muda-na-pratica.md`** — resolve a confusão MCP × plugin × skill em uma frase cada. → 19, 20, 21.
- **`workflows/como-validar-respostas-da-ia-antes-de-aplicar.md`** + **`prompts/como-conversar-com-a-ia...`** — repertório anti-alucinação (checklist 5 níveis, template de debug). → 23, 14.
- **`agentes/guia-completo-time-multi-agent-no-slack-com-hermes.md`** — anatomia de sistema multi-agente: orquestrador + subordinados, system prompt (SOUL/IDENTITY/TEAM), toolsets, protocolo delegação→execução→auditoria. → 18, 19, 20.
- **`arquitetura/mentoria-pyia-pycodeia.md`** — pipeline RAG canônico (FAISS, chunk 1000 / overlap 200, token counting, billing). → 16, 17, 24.
- **`skills-ferramentas/imersao-skills/`** — ciclo SDD operacional (prompt-refiner → prd-creator → bootstrap → sprint-executor ↔ feature-planner). → 14, 22.

## Mapa fonte → aula (onde puxar na geração)

| Aula | Fontes principais na wiki |
|---|---|
| 01 O que é IA | fundamentos/imersao-ia-para-devs-aula-01, fundamentos/guia-inicial-usando-ia |
| 12 Treino/cutoff/modelos | prompts/imersao-...-prompts (comparativo de modelos), skills-ferramentas/setups |
| 14 Prompt Engineering | fundamentos/fundamentos-praticos, fundamentos/...tags-xml, imersao-skills/prompt-refiner, prompts/prompts-curados, prompts/system-prompt-anti-ia, prompts/como-conversar |
| 15 Context Engineering | agentes/segundo-cerebro, imersao-skills/prd-creator, fundamentos/...tags-xml, prompts/prompts-scsi |
| 16 RAG | prompts/prompts-curados, arquitetura/mentoria, arquitetura/blueprint-sistema-rag, arquitetura/blueprint |
| 17 Chunking/embeddings/vector | arquitetura/mentoria (FAISS), arquitetura/blueprint-sistema-rag, skills-ferramentas/recursos-uteis |
| 18 Agentes/subagentes | agentes/guia-multi-agent-slack, agentes/encontros-elite/01, arquitetura/mentoria, arquitetura/blueprint-chatbot |
| 19 Tool use/function calling | agentes/guia-multi-agent-slack (toolsets/mcp_servers), fundamentos/mcp-plugin-e-skill, skills-ferramentas/plugins |
| 20 MCP | fundamentos/mcp-plugin-e-skill, agentes/guia-multi-agent-slack, agentes/encontros-elite/01 |
| 21 Harness Engineering | agentes/encontros-elite/01-03, arquitetura/blueprint (AGENTS/CLAUDE.md), skills-ferramentas/imersao-skills/bootstrap, skills-ferramentas/setups |
| 22 AI-First vs AI-Enabled | workflows/spec-driven-development, imersao-skills (prd-creator/feature-planner/sprint-executor), workflows/imersao-aula-02, fundamentos/guia-inicial |
| 23 Alucinações | workflows/como-validar-respostas, prompts/como-conversar, prompts/system-prompt-anti-ia, arquitetura/blueprint-chatbot (guardrails) |
| 24 Evals/economia de tokens | prompts/prompts-curados, arquitetura/mentoria (billing/token), workflows/checklist-producao, arquitetura/blueprint (cost snapshot) |
| 25 Ética/LGPD | workflows/checklist-producao, prompts/prompts-curados (prompt LGPD) |

## Redundâncias (consolidar na curadoria, não agora)

- **Meta-prompt de refino XML** repetido 4×: `...tags-xml`, `prompts-curados` (#1), `imersao-prompts`, `prompts-scsi`. Fonte canônica = `prompts-curados`.
- **Extração de Design System / template de Landing Page** duplicados entre `imersao-prompts` e `prompts-curados`/arquivos dedicados. Versão limpa = arquivos dedicados em `prompts/`.
- **Ciclo PRD (bruto→refino→refinado→PRD)** em 3 instâncias: `prompts-scsi` (SCSI), `mentoria` (MentorIA), template genérico em `prompts-curados` (#8).
- **Setups de IA** ~70% sobrepostos em 4 arquivos: `setups-de-ia-pycodebr`, `setup-recomendado`, `plugins-recomendados`, `recursos-uteis`. Consolidar numa referência só.
- **Instalação Hermes / setup VPS** repetidos entre encontros 01/02/03 e guia-Slack.
- **Higiene:** `agentes/encontros-elite/...parte-01.md` tem auto-duplicação (seção "multi-canais" escrita 2×) — material bruto não-editado.

## ⚠️ Aviso de obsolescência (regra de honestidade)

Os arquivos citam **versões fictícias/futuras** como se fossem fato: GPT-5.5, Opus 4.7/4.8, Gemini 3.1, GLM-5.1, Django 6, LangChain 1.0, "GPT-5.5 lançou 23/04/2026". Na geração das aulas, tratar esses nomes como **placeholders ilustrativos do método de escolha de modelo** — nunca como tabela factual de versões. Números de preço/limite também envelhecem rápido: usar como exemplo, não como verdade.
