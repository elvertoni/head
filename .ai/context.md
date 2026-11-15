# Contexto do Projeto
_Última atualização: 2026-11-04_

## Objetivo e escopo
Acervo de conhecimento do Prof. Toni Coimbra para o Curso Técnico em Desenvolvimento de Sistemas (SEED-PR).
Faz duas coisas:
- **Segundo cérebro:** wiki de conceitos no modelo llm-wiki do Karpathy, mantida por LLM e navegável no Obsidian.
- **Warehouse de aulas:** Aulas Canônicas (`canonica.md`) neutras de plataforma, que o ProfessorDash importa e
  que as skills convertem em apostila HTML/PDF.

Fora do escopo: o portal ProfessorDash (repo próprio, Django); o setup do agente Quíron (`hermes-toni/`, fora
deste repo); o repo legado `elvertoni/ProfToniCoimbra` (só referência histórica da grade de disciplinas).

## Arquitetura
Pipeline em 4 camadas, cada uma com dono e regra de escrita (detalhe em `docs/schema-wiki.md` §1):

```mermaid
flowchart LR
  L[lake/ — fontes brutas, imutáveis] -->|ingest| C[conceitos/ — wiki atômica]
  L -->|skill prof-toni| A[aulas/.../canonica.md — fonte única]
  C -. "[[slug]]" .- A
  A -->|gerar_manifesto.py| M[manifesto.json]
  M --> P[ProfessorDash — import_acervo]
  A -->|aula-estatica| S[saidas/ — HTML/PDF, não versionado]
```

| Camada | Caminho | Papel |
|---|---|---|
| Lake | `lake/{disciplina}/` | Fontes brutas imutáveis (`status: bruto`) |
| Conceitos | `conceitos/{disciplina}/{slug}.md` | Nós atômicos da wiki; LLM escreve, Toni aprova fusão/obsolescência |
| Aulas | `aulas/{disciplina}/{trilha}/{NN-slug}/canonica.md` | Aula canônica — **fonte única de verdade** |
| Saídas | `aulas/**/{NN-slug}/saidas/` | Artefatos gerados (HTML, PDF) — não versionados, sempre regeneráveis |

Proveniência tem três papéis: arquivos brutos em `lake/` são a fonte e continuam imutáveis;
`lake/**/graphify-out/` é cache derivado de extração do Graphify, que ajuda a recuperar ou auditar texto mas
nunca substitui a fonte bruta ausente; `conceitos/`, `aulas/`, `tools/` e `docs/` são conteúdo versionado. Quando
a fonte bruta falta mas existe cache, manter a lacuna de proveniência explícita.

## Mapa do código
| Caminho | Responsabilidade |
|---|---|
| `lake/` | Fontes brutas (transcrições, PDFs, dumps do Notion, export RCO da SEED). Binários pesados são gitignored |
| `conceitos/` | Wiki de conceitos; `index.md` (catálogo regenerável) e `log.md` (diário append-only) |
| `aulas/` | Aulas canônicas por disciplina/trilha; pasta de aula = `canonica.md`, `imagens.md`, `capa.png`, `img/`, `fontes/` |
| `mapas/` | Navegação do Obsidian: MOCs gerados (`index.md` + um por disciplina) e vistas `.base` escritas à mão |
| `manifesto.json` | Índice máquina do acervo, gerado — contrato de import do portal |
| `tools/gerar_manifesto.py` | Gera e valida o `manifesto.json` |
| `tools/wiki_core.py` | Parser stdlib do subconjunto YAML do vault; usado por `lint_wiki.py` e `gerar_indice.py` |
| `tools/lint_wiki.py` · `tools/gerar_indice.py` · `tools/gerar_mapas.py` | Lint da wiki (somente leitura), catálogo e MOCs |
| `tools/lint_canonica.py` | Lint do corpo das canônicas contra a spec e o parser do portal (somente leitura) |
| `tools/empacotar_skills.py` | Gera `saidas/skills/*.zip` das skills de `.claude/skills/` para o claude.ai (valida o frontmatter; leva o `prompt.xml` para dentro da `gerar-imagem-aula`) |
| `tools/extrair_rco.py` · `tools/triar_rco.py` · `tools/jev.py` | Intake das aulas RCO da SEED e triagem com o Jev |
| `tools/sync_notion.py` | Espelha o índice de aulas na base "Aulas" do Notion (mão única repo → Notion) |
| `tools/notion-wiki/` | Puxa páginas do Notion para o lake |
| `tools/transcrever/` | Transcrição local (faster-whisper, GPU com fallback CPU) para o lake |
| `tools/imagen-generator/` | **Não é script:** `prompt.xml` v9 no Caderno Noturno (fonte de verdade visual, decisão #043) + logo + guia |
| `tests/` | `unittest` stdlib (67 testes em 2026-11-15) |
| `docs/` | `schema-wiki.md` (schema da wiki), manutenção da wiki, backlog de proveniência, triagem RCO |
| `.claude/skills/` | `prof-toni`, `aula-estatica`, `gerar-imagem-aula` |
| `aulas/robotica/` (**local-only**, gitignored pela #044; as linhas abaixo são mapa local) | Protótipos de robótica e cartazes, fora do fluxo de aulas; `automacao_zap_esp32/` é repo git próprio (`elvertoni/automatiza_zap`) |
| `aulas/robotica/automacao_zap_esp32/firmware/` | Protótipo C++/Arduino ESP32, configuração Wi-Fi local, WSS e preparador Python stdlib; não é aula canônica |
| `aulas/robotica/trena_digital_arduino/` | Protótipo de altura com Uno R3 para a feira; testes de HC-SR04, scanner I²C e OLED com U8g2 2.36.19/buffer paginado e título TRENA DIGITAL 1A. Controlador do OLED em validação; não é aula canônica |
| `aulas/robotica/campainha_esp32/` | Sinal escolar publicado em `sinal.tonicoimbra.com`, separado por turma; firmware RTC/NVS gravado em 2026-10-21 no ESP32 COM6/MAC 4c:c3:82:ed:44:18, Wi-Fi S24+ e MQTT confirmados; acesso local/remoto WSS; ver decisão #023 e README |
| `aulas/robotica/automacao_zap_esp32/infra/painel/` | Painel Node-RED/FlowFuse com Volta Atelier do portfólio, temas claro/escuro com preferência local, fontes/marca incorporadas e publicação visual parcial por API |
| `aulas/robotica/automacao_zap_esp32/infra/mensagens/` | Caixa de mensagens do WhatsApp (laboratório): webhook global da Evolution Go → SQLite + mídias em disco → painel `/mensagens/` só para o professor; stdlib, testes `test_app.py` |
| `hermes/skills/prof-toni/` | Skills do Quíron (`operar-acervo`, `alimentar-cerebro`), implantadas na VPS por `git pull` + cópia |

Gitignored por decisão: `**/saidas/`, `aulas/**/atividades/*.pdf` (o `.html` é a fonte editável),
`lake/**/elite-wiki/`, uma lista explícita de extensões pesadas do `lake/` (vídeo, áudio, PDF, Office, imagens —
formato novo não fica coberto até entrar no `.gitignore`), `graphify-out/`, `scratch/`, `.playwright-mcp/`,
`.obsidian/`, `codex-session-*.md`, `.ai/handoff.md` e `.ai/sessions/`. Uma disciplina do `lake/` que parece
vazia no git costuma ter PDFs só locais — conferir o disco antes de concluir que não há material.

## Integrações externas
- **ProfessorDash** — portal das aulas; `import_acervo` baixa o tarball do GitHub e lê `manifesto.json` +
  `aulas/**/canonica.md`. Contrato completo em `docs/schema-wiki.md` §5.1. Publicação em 4 passos (invariante 6
  do `AGENTS.md`).
- **Notion ("Toni's Brain")** — `sync_notion.py` projeta o índice de aulas (metadados + link do ProfessorDash,
  sem corpo) na base `Aulas`, com chave na propriedade `Caminho`. Mão única: o Notion nunca é entrada. Escrita
  só com `--apply`. As bases `Aulas` e `Projetos` precisam estar compartilhadas com a integração.
- **Jev (TypeSafe)** — modelo de julgamento: devolve respostas tipadas `noul`, `choice` ou `score` com
  probabilidade e nunca gera texto. Usado na triagem em massa em que o código decide; lê só texto, é mais forte
  em inglês. A triagem das 516 aulas RCO custou cerca de US$ 0,07. Respostas ficam em cache em `scratch/jev-rco/`.
- **Codex CLI** — gera as imagens de aula: o agente monta o prompt resolvido (`montar_prompt.py`), delega à ferramenta nativa de
  imagem do Codex e audita o PNG (verificado em 2026-07-29). O Projeto do ChatGPT no navegador é o caminho
  alternativo. Ler `.claude/skills/gerar-imagem-aula/SKILL.md` antes.
- **Imagens de aula** — prompt v9 (Caderno Noturno, decisão #043): azul-noite + âncora amarela, coral só em erro. Desde o v8 a peça gerada pelo Codex é final e sem marca (decisão #036). Arte já publicada em v8 (grafite/vermelho) fica até o Toni pedir regeração.
- **Design system** — portal, apostila e (após o piloto) imagens seguem o **Caderno Noturno** (DS v4) do ProfessorDash: azul-noite + amarelo, aluno no claro, vermelho só para erro (decisão #042). A `aula-estatica` embute Archivo, Geist e JetBrains Mono (SIL OFL, `assets/fonts/OFL.txt`); o `build.py` recusa `<em>` no título e `.roteiro` fora de `--professor`.
- **Exercícios de Python (2026-11-05)** — site estático fora deste repo: `elvertoni/exercicios-python` (público, `~/PROJETOS/PESSOAL/exercicios-python`), publicado em https://elvertoni.github.io/exercicios-python/ pelo GitHub Pages. Os 177 exercícios da lista Python Brasil/dunossauro, com Pyodide em Web Worker, progresso no `localStorage` e exportar/importar. Não é aula canônica nem entra no manifesto; integração futura com o login do ProfessorDash depende do parecer ASTRA (editor em origem separada, salvamento remoto).
- **Quíron (Hermes Agent na VPS)** — opera o acervo a partir de um clone na VPS com as skills de `hermes/`.
- **Automação ESP32/WhatsApp (2026-10-20)** — protótipo em `aulas/robotica/automacao_zap_esp32/` (local-only no acervo, repo próprio `elvertoni/automatiza_zap`; #044), fora do fluxo de aulas canônicas. Compose independente do EasyPanel na VPS `vmi2626506`, `/opt/automacao-zap-esp32`: Mosquitto 2.1.2, Node-RED 5.0.8/FlowFuse Dashboard 1.33.0, Nginx e túnel Cloudflare dedicado. Painel em `https://automacao.tonicoimbra.com/dashboard/inicio` e MQTT/WSS em `/mqtt` (443); broker direto 8883/TLS com CA própria preservado. Configuração/scripts stdlib em `infra/`, interface/regras/testes JS em `infra/painel/`; senhas, credenciais Cloudflare e contexto persistente fora do Git. Editor só na VPS/SSH. Firmware Arduino em `firmware/`, gravado no DevKit COM6 (core 3.3.12; WiFiManager/WebSockets/MQTTPubSubClient), com portal Wi-Fi protegido `Toni-ESP32-01` em 192.168.4.1 e configuração também pelo IP local (HTTP Digest; decisão #024). Firmware wifi-2 separa o portal das tentativas de reconexão, preservando NVS; segredos de compilação fora do repo. Ver READMEs e decisões #018–#022; firmware online com estados confirmados por MQTT, painel com Volta Atelier do portfólio e publicação visual parcial. Ponte WhatsApp na Evolution Go (decisão #033).
- **Ponte WhatsApp / Evolution Go (2026-10-27)** — `evoapicloud/evolution-go` 0.7.2 + Postgres próprio no Compose `/opt/automacao-zap-esp32` (Manager/API em `https://evolution.tonicoimbra.com` com login do painel, só `toni`; `127.0.0.1:8090` na VPS; webhook interno `painel:1880/zap/webhook`). Licença gratuita ativada pelo Toni. Segredos em `segredos/evolution.env`/`postgres.env` e `painel/segredos/zap.json` (fora do Git); preparo por `painel/preparar_zap.py`. A Evolution 2.3.7 (`evolution-teste` no EasyPanel), o Manager customizado e o MinIO foram todos removidos. Ver decisão #033 e `infra/painel/README.md`.
- **ai-memory (MCP local)** — memória semântica complementar (decisão #001).
- **Obsidian** — a raiz é o vault; o plugin kepano `obsidian` (obsidian-bases, obsidian-markdown, json-canvas,
  obsidian-cli, defuddle) está habilitado no escopo do projeto em `.claude/settings.json`.

## Modelo de dados (resumo)
- **Aula** (`canonica.md`) → frontmatter do contrato (`titulo`, `disciplina`, `trilha`, `ordem`, `slug`,
  `status`, `versao`, `atualizado_em`) + campos da skill (`tema`, `serie`, `prerequisitos`, `objetivos`,
  `modo_origem`, `fontes`); cita conceitos por `[[slug]]`.
- **Conceito** (`conceitos/{disciplina}/{slug}.md`) → `conceito`, `slug`, `disciplina`, `tipo`
  (`conceito|entidade|sintese`), `aka`, `status` (`vivo|rascunho|obsoleto`), `fontes`, `aulas`,
  `atualizado_em`; lista as aulas que o citam em `## Onde aparece`.
- **Manifesto** → `disciplinas[]` (com `trilhas[]`), `lessons[]` (só `aprovada`) e `conceitos[]`
  (`{slug, nome, disciplina}` de todo nó não obsoleto — o portal troca `[[slug]]` pelo nome com acento por aí).
- **Nota RCO** (`lake/{disciplina}/rco/{n}tri/*.md`) → `tipo: rco-seed`, `status: bruto`, `fontes` apontando
  para os `.pptx`/`.docx` originais. É matéria-prima, não aula: virar `canonica.md` passa pela `prof-toni` em
  modo SEED.

### Vocabulário do corpo da canônica (catálogos fechados)
Especificado em `.claude/skills/prof-toni/spec/01-CANONICA.md` §5–§7; bloco inventado aparece como texto cru
para o aluno.
- **Callouts (6):** `:::conceito`, `:::exemplo`, `:::importante`, `:::atencao`, `:::dica`, `:::curiosidade`;
  abertos como `:::tipo Título`, fechados com `:::`.
- **`:::roteiro`:** direção de cena só do professor. A apostila do aluno o omite (versão do professor só a pedido) — nunca pôr ali algo que o aluno
  precise.
- **Interativos (2):** ` ```quiz ` e ` ```diagrama-progressivo `. O corpo é YAML real: valor com `: ` ou que
  começa com aspas vai entre aspas duplas. Cada pergunta tem exatamente uma alternativa `correta: true` (duas
  viram duas certas; nenhuma degrada a lista). `rotulo` de diagrama não leva número próprio ("1 · 1. Navegador").
- O `feedback` do quiz não é renderizado hoje; continuar escrevendo, mas nunca ensinar por ele.
- Uso em 2026-09-21: 80 quizzes e 73 diagramas progressivos nas 89 aulas.

### Comportamento do gerador do manifesto (`tools/gerar_manifesto.py`)
- A identidade vem do **caminho**; o frontmatter é validado contra ele. Divergência é reportada, nunca
  corrigida em silêncio.
- `slug` precisa ser único **em todo o vault**, mas o gerador só impõe isso entre aulas aprovadas
  (`vistos_slug` em `coletar()`): colisão com rascunho ou com nó de `conceitos/` passa no `--check` e quebra
  a resolução de wikilink.
- O parser de frontmatter é mínimo de propósito: só chaves escalares de topo; campos do contrato ficam planos.
- O gerador parte do `manifesto.json` existente: `version`, `vault`, `descricao`, `arquitetura`, `series[]` e
  `serie`/`status`/`lake`/`warehouse` de cada disciplina vêm do arquivo, e `disciplinas[]` só emite slugs que já
  estão lá. Disciplina nova gera aulas em `lessons[]` sem entrada em `disciplinas[]` até alguém semear os
  metadados — a única exceção ao "nunca editar à mão".
- Rótulos de exibição ficam em `LABELS_DISCIPLINA` / `LABELS_TRILHA` no próprio gerador; registrar ali ao criar
  disciplina ou trilha.
- `sync_notion.py` importa `parse_frontmatter` do gerador: mudar esse parser afeta os dois.

Validadores: `gerar_manifesto.py --check`, `lint_wiki.py`, `lint_canonica.py` e `sync_notion.py --check`. Frescor de derivados:
`gerar_indice.py --check`, `gerar_mapas.py --check`, `extrair_rco.py --check`.

## Estado atual do vault
Snapshot de 2026-09-21, com a trilha JavaScript acrescentada em 2026-11-04; `gerar_manifesto.py --check`
confirmou **120 aulas aprovadas, 0 divergências** em 2026-11-04. O manifesto e o `--check` mandam — revalidar antes de confiar nos números.

| Disciplina | Trilha | Estado |
|---|---|---|
| `inteligencia-artificial` | `fundamentos-de-ia` | aulas 1–25 aprovadas (25) + grafo de 37 conceitos |
| `introducao-a-computacao` | `arquitetura-computadores-e-sistemas-operacionais` | aulas 23–38 aprovadas (16) |
| `programacao-front-end` | `javascript-na-pratica` | aulas 19–38 aprovadas (20) — da retomada de HTML/CSS à lista de tarefas com filtros; plano em `docs/plano-apostila-javascript.md` |
| `programacao-front-end` | `landing-page-mvp` | aulas 7–18 aprovadas (12) — startup/MVP até publicar e validar; 12 infográficos em `img/` |
| `analise-e-metodos-para-sistemas` | `metodologias-ageis` | aulas 33–41 + 53–54 aprovadas (11) (Scrum/agilidade, Kanban) |
| `tcc` | `blueprint-tcc` | aulas 1–9 aprovadas (9) |
| `analise-e-projeto-de-sistemas` | `marketing-digital` | aulas 25–30 aprovadas (6) |
| `programacao-front-end` | `controle-de-versao-git-github` | aulas 2–6 aprovadas (5) + `atividades/` (apoio impresso, fora do manifesto) |
| `introducao-a-computacao` | `nivelamento-e-retomada` | aulas 1–2 aprovadas (2) |
| `analise-e-projeto-de-sistemas` | `analise-de-requisitos` | aula 31 aprovada (1) |
| `programacao-front-end` | `fundamentos-html-css` | aula 1 aprovada (1) |
| `programacao-no-desenvolvimento-de-sistemas` | `arquitetura-e-fluxo-de-sistemas` | aula 1 aprovada (1) |
| `programacao-front-end` | `projeto petfinder` | **só HTML** (9 arquivos), sem `canonica.md` — não importável |
| `programacao-no-desenvolvimento-de-sistemas` | `blueprint-tcc` | HTML de apoio; as canônicas vivem em `tcc/blueprint-tcc` |
| `inovacao-tecnologia-e-empreendedorismo` | — | sem aulas canônicas |

A wiki tem cerca de 1.042 nós ativos, concentrados nas ingestões das duas pós-graduações
(`inovacao-inteligencia-artificial-e-robotica-educacional` e `desenvolvimento-full-stack-e-cloud-computing`) e
nos grafos menores por disciplina. A maioria está `status: rascunho`. As aulas aprovadas usam um subconjunto
pequeno; `lint_wiki.py` mostra cobertura e backlinks faltando.

## Variáveis de ambiente relevantes
- `NOTION_TOKEN` — token da integração interna do Notion usada por `sync_notion.py` (valores reais nunca aqui)
- `TYPESAFE_API_KEY` — chave do Jev usada por `triar_rco.py`

## Pontos de atenção / dívida técnica
- Não há CI (`.github/` não existe): testes e validadores só rodam quando alguém roda.
- Cerca de 186 camadas de diagrama em aulas aprovadas têm numeração manual no `rotulo`, contra o contrato — não
  copiar aula existente como referência de diagrama.
- Lint em 2026-09-28: 0 erros, 1.452 avisos (1.264 `source-missing`, 189 `orphan`) e 538 infos — a maior parte é
  fonte bruta que só existe em outra máquina ou virou cache.
- A triagem RCO (`docs/rco-triagem.md`) é auxílio de ordenação: pares errados voltaram com confiança de 0,88 a
  0,96. Equivalência abaixo de 0,7 vem marcada com ⚠.
- `lake/**/elite-wiki/` não vem no clone; recriar com `python tools/notion-wiki/puxar_notion.py`.
- Memória legada congelada em `~/.claude/projects/C--PROJETOS-PROF-TONI/memory/` (só histórico).
