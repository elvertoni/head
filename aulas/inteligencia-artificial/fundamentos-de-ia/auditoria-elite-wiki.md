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

---

# Adendo — 2026-07-24 · Encontros #04/#05 + transcrições completas

Duas entradas novas no lake desde a auditoria original:

| O que | Onde | Volume |
|---|---|---|
| Páginas Notion dos Encontros Elite **#04** e **#05** | `elite-wiki/agentes/encontros-elite/` | 23 KB |
| **Transcrições integrais** dos Encontros **#01–#05** (PDF → md) | `elite-wiki/_transcricoes/` | 800 K chars |

As transcrições mudam a economia do material. Comparação do #05: página Notion 9,3 KB × transcrição 134 KB — **14× mais densa**. As páginas do Notion são a ementa; a carne está na transcrição, que vem estruturada em `Resumo` → `Próximas etapas` → `Detalhes` (bullets com timestamp) → transcrição corrida. **Os bullets de `Detalhes` são o índice de trabalho** — dá pra localizar o trecho exato pelo timestamp sem ler os 674 parágrafos.

## Temas de #04 e #05

- **#04 — Deploy, monitoria e observabilidade (parte 2):** stack Prometheus + Grafana + Loki + Promtail + cAdvisor + Node Exporter; **Django MCP Server** (17 tools expostas: listar/descrever/criar/atualizar/deletar registros); **Grafana MCP** (IA consulta dashboards, roda query no Prometheus, tira print de painel); IA lendo 22.339 linhas de log e achando os erros; *alert fatigue*; LangSmith p/ rastrear tokens e custo por resposta de agente; Sentry como complemento; criação de *skills* de agente ("SCSI Manager").
- **#05 — Integrações e automações (parte 1):** VPS + Cloudflare; Firecrawl com **DuckDuckGo como busca primária e Firecrawl como fallback**; **Composio** como broker de integrações (e a decisão de usar CLI em vez do MCP por limitação de múltiplas contas); Vision + geração de imagem; Central de Operações (portal autenticado); pipeline de conteúdo com **curadoria humana antes de publicar**; cron jobs; **Loop Engineering**; **IA proativa**; **perfis de agente com permissões restritas** contra prompt injection; Evolution API.

## Peças de maior valor (ouro didático) — novas

- **Loop Engineering (#05, 01:49:02)** — a IA gera a imagem, chama a ferramenta de Vision pra conferir se saiu dentro do padrão e **pede ajuste a si mesma** até passar. É o exemplo mais limpo de auto-verificação em ciclo fechado do acervo inteiro. → aulas 23, 24.
- **Django MCP Server + Grafana MCP (#04)** — MCP deixa de ser diagrama e vira "a IA criou 11 notificações reais no banco, cada uma com link pro registro". Melhor exemplo concreto de MCP e de tool use que existe no material. → aulas 19, 20.
- **Economia de tokens com decisão de produto (#05, 01:14:32)** — o relatório sugere 5 ideias de carrossel, mas só gera imagem pras 2 de maior potencial de engajamento. Economia de token como escolha de engenharia, não como sovinice. → aula 24.
- **Observabilidade de agente (#04, 01:23:07)** — LangSmith medindo tokens de entrada/saída e custo médio por resposta. Fecha o par "avaliar qualidade (evals) + medir custo". → aula 24.
- **Segurança de agente por remoção de ferramenta (#05, 01:58:03)** — tirar ferramentas do perfil pro agente **não ter shell**, prevenindo prompt injection; perfis isolados por finalidade. Princípio do menor privilégio aplicado a agente. → ver lacuna abaixo.
- **IA proativa (#05, 01:38:50 e 01:43:04)** — o agente acompanha o grupo de WhatsApp, vê a discussão sobre campanha nova e **gera os criativos sem ninguém pedir**. Vira a pergunta "IA responde ou IA age?". → aula 22.
- **Fallback de ferramenta (#05, 00:24:29)** — DuckDuckGo primeiro, Firecrawl só no caso difícil. Degradação graciosa + controle de custo em uma decisão só. → aula 19.
- **Alert fatigue (#04, 01:27:12)** — coletar tudo não é observar; excesso de alerta treina o humano a ignorar. Transversal, boa analogia para excesso de contexto. → aulas 15, 24.

## Mapa fonte → aula (adendo)

| Aula | Fontes novas |
|---|---|
| 15 Context Engineering | `_transcricoes/04` (alert fatigue como analogia de ruído de contexto) |
| 18 Agentes e Subagentes | `_transcricoes/05` (perfis de agente por finalidade, permissões isoladas), `_transcricoes/04` (skills de agente) |
| 19 Tool Use e Function Calling | `_transcricoes/04` (17 tools do Django MCP, o que cada uma faz), `_transcricoes/05` (fallback DuckDuckGo→Firecrawl, Composio CLI × MCP) |
| 20 MCP | `_transcricoes/04` (Django MCP Server + Grafana MCP na prática, autenticação, o que a IA consegue fazer), `encontros-elite/04` |
| 21 Harness Engineering | `_transcricoes/04` (criação de skill "SCSI Manager"), `_transcricoes/05` (Central de Operações, versionamento automático) |
| 22 AI-First vs AI-Enabled | `_transcricoes/05` (IA proativa × reativa — o melhor material do acervo pra essa aula) |
| 23 Alucinações | `_transcricoes/05` (Loop Engineering: gerar → validar → auto-corrigir) |
| 24 Evals e Economia de Tokens | `_transcricoes/04` (LangSmith, custo/resposta), `_transcricoes/05` (gerar 2 imagens de 5 ideias; alert fatigue) |
| 25 Ética e IA no Brasil | `_transcricoes/05` (OAuth × scraping, limite de dados de terceiros, política de uso e risco de banimento) |

## Fora de escopo (não puxar para Fundamentos de IA)

Boa parte de #04 e #05 é **infraestrutura**, não IA — nível muito acima de aluno de 14–18 anos e fora da ementa: Traefik, Docker Swarm, DNS Cloudflare, Basic Auth com hash, `deploymonitoring.sh`, IDs de dashboard do Grafana, Nginx, Evolution API. Se algum dia render aula, é de outra disciplina (arquitetura/SO), não daqui.

Descartar também: links de afiliado (OpenCode Go, "5 dólares no primeiro mês"), divulgação da Elite Week, grupo VIP de WhatsApp. É material comercial do curso, não conteúdo.

## Lacuna identificada — decisão do Toni

A trilha tem 25 aulas e fecha em Ética/LGPD. O material novo cobre bem as aulas existentes, com **uma exceção**: *segurança de agentes* não tem casa clara.

Prompt injection, princípio do menor privilégio na escolha de ferramentas, isolamento de perfis, e "por que o agente não deve ter acesso ao shell" não estão na aula 19 (que é sobre *como* a ferramenta funciona) nem na 25 (que é ética e lei, não ataque técnico). É um tema que só cresce e o material de #05 dá exemplo concreto.

Duas saídas:
1. **Enriquecer a 19 e a 25** — mais barato, mantém a trilha fechada em 25, mas o tema fica diluído.
2. **Aula 26 — Segurança de Agentes de IA** — trilha vira 26 aulas. Tem conteúdo pra 50 min com folga.

Não decidi nada; a trilha parece deliberadamente fechada em 25.

## Obsolescência (mesma regra)

As transcrições citam GPT-5.6 (Sol/Luna/Terra), DeepSeek V4 Flash/Pro, GLM 5.2, GPT Image 2, Whisper 1. Mesma regra do aviso acima: **placeholder do método de escolha de modelo**, nunca tabela factual.

## Dado pessoal

As transcrições trazem **nomes reais de participantes** do curso pago (perguntas atribuídas a alunos). O material é local-only e gitignored, o que resolve por ora — mas nenhum desses nomes pode atravessar para a Canônica.

---

# Verificação de integridade — 2026-07-24

Varredura de 42 arquivos: cada cópia local rebaixada do Notion pelo `page_id` do frontmatter e comparada corpo a corpo. Rodada por 4 agentes em fatias disjuntas.

| Veredito | Qtd |
|---|---|
| Idêntico à fonte | 38 |
| Drift real | 3 |
| Truncado no crawler (lake é a versão boa) | 1 |
| Erro de download | 0 |

**O acervo é fiel.** Arquivos de 178 KB e 161 KB bateram char-a-char. A ingestão não corrompeu nada.

## Os 3 drifts

1. **`workflows/workflow-com-ia-assistida.md`** — o comando de instalação do opencode mudou na fonte: `npm install -g @opencode/cli` → `npm i -g opencode-ai`. **É o único drift acionável**: comando de instalação errado quebra na mão do aluno. Corrigir antes de qualquer uso didático.
2. **`agentes/encontros-elite/encontro-elite-03-...md`** — ganhou uma linha `Desenhos: ‣` (embed externo, ver abaixo).
3. **`_indice/elite-wiki.md`** — 2 marcadores `‣` novos, sem conteúdo resolvível.

## Ponto cego do crawler: 81 links externos perdidos

O `puxar_notion.py` renderiza embeds de link externo (`eoi`, *external object instance*) como o caractere `‣` **sem preservar a URL**. Todo link para GitHub, diagrama, vídeo ou ferramenta externa vira um símbolo mudo.

São **81 ocorrências** no acervo. Concentração:

| Arquivo | `‣` perdidos |
|---|---|
| `fundamentos/imersao-ia-para-devs-aula-01.md` | 22 |
| `agentes/encontros-elite/...01.md` | 20 |
| `agentes/encontros-elite/...03.md` | 11 |
| `workflows/workflow-com-ia-assistida.md` | 9 |
| demais (5 arquivos) | 19 |

Exemplos do que se perdeu: `Repositório do projeto: ‣` e `Desenhos: ‣` no Encontro #03 — provavelmente o repo do SCSI e o diagrama da arquitetura de deploy.

Resolver exige outra chamada de API (`syncRecordValues` sobre o registro `external_object_instance`), não implementada no script. **Enquanto isso, todo link citado em aula precisa ser conferido na fonte, não no lake.**

## Limitação do crawler: conteúdo dentro de toggle

O crawler traz **910 chars** de `prompts/prompts-scsi.md`; a cópia do lake tem **202.006** — 0,5%.

**Causa exata, diagnosticada:** o `loadPageChunk` devolve os blocos `toggle` de topo e declara os ids dos filhos em `content[]`, mas **não inclui esses filhos na resposta**. Nessa página são 12 toggles, cada um com 1 filho não retornado. O conteúdo real dos prompts está nesses 12 blocos ausentes.

**É recuperável.** O endpoint `POST /api/v3/syncRecordValues` busca cada bloco órfão por id, sem autenticação:

```
{"requests": [{"pointer": {"table": "block", "id": "<uuid-do-filho>"}, "version": -1}]}
```

Testado no primeiro órfão: devolveu um bloco `code` com **17.971 chars** — o prompt bruto do SCSI. 12 toggles × ~17 K ≈ os 202 KB da cópia do lake. Ou seja: o arquivo **é reproduzível**, só exige implementar essa segunda chamada no `puxar_notion.py`.

Duas correções ao que estava escrito antes nesta auditoria:
- "esse arquivo não é reproduzível" — **errado**, ver acima.
- "toggles colapsados que o crawler não abre" — a formulação certa é *filhos declarados mas não retornados pela API*, resolvível com `syncRecordValues`.

Enquanto o script não for corrigido, permanece o risco de **backup**: `lake/**/elite-wiki/` é gitignored, então esses 202 KB não têm versionamento. É a biblioteca-mestre de prompts XML citada acima como peça de maior valor do acervo.

## Correções aplicadas no `puxar_notion.py` (2026-07-24)

As três limitações foram corrigidas e verificadas:

1. **Filhos de toggle** — `syncRecordValues` busca em cascata os ids declarados em `content[]` que não vêm no `recordMap`.
2. **Links** — três mecanismos, todos tratados: `eoi` (registro externo, precisa de fetch), `p` (menção a página, vira `[[Título]]`), `lm` (link mention, já traz `href` e `title` embutidos — sem chamada extra).
3. **`render_md` recursivo** — desce nos blocos aninhados. Lista indenta os filhos; toggle não, para não quebrar cerca de código.

Resultado medido:

| Página | Antes | Depois |
|---|---|---|
| `prompts-scsi` | 910 chars | 172.035 chars |
| `imersao-ia-para-devs-aula-01` | 10.934 chars, 22 links mudos | 17.595 chars, 76 links resolvidos |
| `prompts-curados-pycodebr` | 111.512 chars | 117.361 chars, zero `‣` |
| `encontro-elite-01` | 39.248 chars | 42.462 chars, zero `‣` |

Filhos órfãos: **0**. Links resolvidos: **80 dos 81** — o único irrecuperável é um embed de `imersao-ia-para-devs-aula-01` cujo registro volta vazio (deletado na origem). Ali o `‣` permanece, e é a representação honesta.

Efeito colateral: mais chamadas por página, então mais 429. O backoff exponencial absorve, mas um re-crawl completo demora bem mais que antes.

**Refresh de arquivo inteiro continua sendo decisão de risco.** As cópias atuais do lake foram feitas com o crawler antigo e algumas receberam correção manual — `workflows/workflow-com-ia-assistida.md` tinha `https://opencode.ai` no lake onde o crawler devolvia `‣`. Antes de re-crawlear em massa, comparar arquivo a arquivo.

## Consistência interna

**Nenhuma contradição técnica real.** Duas candidatas foram levantadas e as duas caem sob análise: "não use Docker local" × "Docker na VPS" são contextos distintos; "LLM local é ruim" × "use modelo barato na nuvem" também (o primeiro é limite de hardware, o segundo roda em datacenter). O material é coerente consigo mesmo.

**Duplicação confirmada** — prompt XML de landing page e meta-prompt de refino, ambos replicados entre o arquivo dedicado e `prompts-curados-pycodebr.md` (canônico). **Correção à auditoria original:** o prompt de Design System **não** está duplicado — `prompts-curados` só o indexa, o arquivo dedicado tem a versão explicada. Propósitos diferentes.

**Ajuste de enquadramento no aviso de obsolescência:** a seção acima chama as versões citadas de "fictícias". Isso afirma demais — não há como verificar. O correto é tratá-las como **afirmações datáveis que envelhecem rápido**. Inventário ampliado: GPT-5.3-codex/5.4/5.5/5.6/5-mini, GPT Image 2, Opus 4.6/4.7/4.8, Sonnet 4.6, Gemini 3.1 Pro, GLM-5/5.1/5.2, Qwen 3.7 Max, Kimi K2.6, DeepSeek V4/Flash/Pro, Django 6.0, LangChain 1.0. (Ubuntu 24.04 LTS, Docker Compose 3.9 e Python 3.11–3.13 são correntes e não entram nessa lista.)

**Preços afirmados como fato** — envelhecem igual: planos MentorIA (R$ 0/97/297/697), Hostinger KVM2 (R$ 43–70/mês), Open Code Go (US$ 5 no 1º mês, US$ 10 depois), "Claude Max 5X R$ 550, cancelado em 27/06/2026".
