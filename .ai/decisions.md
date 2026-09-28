# Registro de Decisões

<!-- Entradas mais recentes no topo. Não apagar entradas antigas. -->
<!-- Numeração cronológica. Entradas "(inferida)" foram reconstruídas do histórico git, do antigo CLAUDE.md e das páginas do ai-memory em 2026-09-28. -->

## #015 — Schema da wiki sai do `AGENTS.md` para `docs/schema-wiki.md`
- **Data:** 2026-09-28
- **Status:** Aceita
- **Contexto:** O padrão de memória portável exige um `AGENTS.md` curto (~150 linhas), carregado em toda sessão por todos os harnesses. O `AGENTS.md` antigo tinha 303 linhas com o schema da wiki Karpathy, e o `CLAUDE.md` tinha mais 210 linhas de arquitetura.
- **Decisão:** O schema vai inteiro para `docs/schema-wiki.md`, com a mesma numeração de seções (§1–§7). O `AGENTS.md` novo guarda o protocolo, as invariantes, as convenções e os comandos. A arquitetura do antigo `CLAUDE.md` vai para `.ai/context.md`. As referências "`AGENTS.md` §N" no README, na skill `prof-toni`, nas skills do Hermes e no `gerar_manifesto.py` foram atualizadas.
- **Alternativas descartadas:** Manter o schema no `AGENTS.md` com o protocolo acrescentado (~350 linhas carregadas em toda sessão).
- **Consequências:** Antes de `ingest`/`query`/`lint` o agente precisa abrir `docs/schema-wiki.md` explicitamente. O Quíron só vê a mudança depois do redeploy das skills na VPS (`git pull` + `cp -r hermes/skills/prof-toni ~/.hermes/skills/`).

## #014 — Handoff local-only porque o repo é público
- **Data:** 2026-09-28
- **Status:** Aceita
- **Contexto:** `elvertoni/head` é público (confirmado com `gh repo view` em 2026-09-28). O portal lê o tarball do GitHub, então o repo precisa continuar acessível.
- **Decisão:** `.ai/handoff.md` e `.ai/sessions/` ficam no `.gitignore`. `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `.ai/context.md`, `.ai/decisions.md` e `.ai/prompts/` são versionados.
- **Alternativas descartadas:** Versionar o handoff como no ESIMBA (exporia o estado de sessão publicamente).
- **Consequências:** A continuidade entre harnesses funciona na mesma máquina. Outra máquina não recebe o handoff pelo git.

## #013 — Memória portável no repositório; ai-memory passa a ser complemento
- **Data:** 2026-09-28
- **Status:** Aceita
- **Contexto:** Desde a #009 a memória durável vivia no ai-memory (MCP). O padrão de memória portável põe o contexto no repositório para qualquer harness, conta ou modelo retomar sem depender de um servidor.
- **Decisão:** `AGENTS.md` + `.ai/` são a memória primária. Decisões técnicas vão para este arquivo; arquitetura para `.ai/context.md`; estado de sessão para `.ai/handoff.md`. O ai-memory guarda só conhecimento revisado e útil entre projetos, sem duplicar handoff nem decisões.
- **Alternativas descartadas:** Manter o ai-memory como primário e usar `.ai/` só para handoff e contexto.
- **Consequências:** As ADRs e regras pinadas do ai-memory deste projeto foram trazidas para cá como entradas inferidas (#002, #005, #008, #009). Substitui a #009.

## #012 — Triagem RCO: o código decide, o Jev só ordena
- **Data:** 2026-09-22 (inferida)
- **Status:** Aceita
- **Contexto:** Chegaram 516 aulas RCO da SEED, e era preciso saber quais já têm aula aprovada equivalente (commit `bed391d`).
- **Decisão:** `extrair_rco.py` extrai de forma determinística para `lake/{disciplina}/rco/`. `triar_rco.py` casa títulos idênticos no código e pergunta o resto ao Jev (TypeSafe), com os `objetivos` de cada aula aprovada como contexto. Equivalência abaixo de 0,7 recebe ⚠. A saída (`docs/rco-triagem.md`) nunca cria, promove nem edita conceito ou aula.
- **Alternativas descartadas:** Comparar só com títulos das aulas aprovadas (o Jev dava confiança baixa até em pares corretos).
- **Consequências:** Custo de cerca de US$ 0,07 na triagem inteira. Ainda há pares errados com confiança alta (0,88–0,96), então a triagem é auxílio, nunca decisão.

## #011 — Publicação em quatro passos com reimport forçado
- **Data:** 2026-08-23 (inferida)
- **Status:** Aceita
- **Contexto:** O portal ficou 13 aulas e 14 capas defasado sem erro nenhum, porque o reimport não foi feito (commit `f910e52`).
- **Decisão:** Publicar = `gerar_manifesto.py` → push do acervo → deploy do portal → reimport com `--force`.
- **Alternativas descartadas:** <!-- TODO: confirmar -->
- **Consequências:** O reimport é passo explícito do fluxo (invariante 6 do `AGENTS.md`).

## #010 — Geração de imagem delegada ao Codex CLI
- **Data:** 2026-08-10 (inferida)
- **Status:** Aceita
- **Contexto:** A #008 tirou a geração de dentro do agente por qualidade. A ferramenta nativa de imagem do Codex CLI passou a entregar arte no padrão (commit `2bc296e`).
- **Decisão:** O agente monta o prompt v6 resolvido, delega a geração ao Codex CLI e audita o PNG contra os 12 defeitos da regra `R3`. O Projeto do ChatGPT no navegador continua como alternativa. Entregar o XML cru ao modelo é proibido, porque gera fundo claro e cantos ocupados.
- **Alternativas descartadas:** Ferramenta de imagem interna do Claude Code (qualidade abaixo do acervo).
- **Consequências:** O loop de geração volta a ser automatizável. A logo continua fora do modelo.

## #009 — Memória do projeto no ai-memory, não nos arquivos locais
- **Data:** 2026-07-29
- **Status:** Substituída por #013
- **Contexto:** O ai-memory (MCP) e o `MEMORY.md` local do Claude Code rodavam em paralelo e desalinhados.
- **Decisão:** O ai-memory virou o sistema de memória do projeto; a pasta `~/.claude/projects/C--PROJETOS-PROF-TONI/memory/` foi congelada como histórico.
- **Alternativas descartadas:** Manter os dois sistemas.
- **Consequências:** O ai-memory passou a ter ADRs pinadas e regras deste projeto; os arquivos locais não recebem mais nada.

## #008 — Prompt de imagem v6 com dois perfis; geração fora do agente
- **Data:** 2026-07-29
- **Status:** Aceita quanto aos perfis; o local de geração foi substituído por #010
- **Contexto:** A auditoria das 54 imagens aprovadas mostrou que o prompt v5 estava calibrado abaixo do acervo, e a ferramenta de imagem do Claude Code saía pior que o ChatGPT (commit `c12bac6`).
- **Decisão:** `tools/imagen-generator/prompt.xml` v6 tem dois perfis — `capa` (3:2, 4–10 blocos com micro-parágrafo, subtítulo e faixa de rodapé) e `infografico` (16:9, 2–5 blocos só com rótulos). Declarar o perfil é o passo 0. Paleta com fundo navy quase preto e ciano como âncora. `imagens.md` traz um brief de `capa` e no máximo um de `infografico`, sem prompt escrito à mão. O branding é aplicado depois pelo Photoshop.
- **Alternativas descartadas:** Fundir os dois formatos num spec só; manter a geração no Claude Code; proibir render 3D (aparece em ~15 das 54 aprovadas).
- **Consequências:** Auditoria objetiva pela regra `R3` (12 defeitos reais já publicados).

## #007 — Manifesto exporta `conceitos[]` para o portal
- **Data:** 2026-07-27 (inferida)
- **Status:** Aceita
- **Contexto:** Slugs não têm acento, então o portal mostraria "aprendizado de maquina" ao derivar o nome do slug (commit `38da690`).
- **Decisão:** `manifesto.json` leva `conceitos[]` com `{slug, nome, disciplina}` de todo nó não obsoleto. Nas aulas, preferir `[[slug|rótulo]]`; o mapa é a rede de segurança.
- **Alternativas descartadas:** <!-- TODO: confirmar -->
- **Consequências:** O contrato do portal (§5.1 do schema) inclui `conceitos[]`.

## #006 — Notion como projeção de mão única do índice de aulas
- **Data:** 2026-07-27 (inferida)
- **Status:** Aceita
- **Contexto:** O workspace "Toni's Brain" precisava listar as aulas sem virar segunda fonte de verdade (commit `97cb97e`).
- **Decisão:** `sync_notion.py` espelha só metadados + link do ProfessorDash na base `Aulas`, com chave `Caminho`. O Notion nunca é entrada. A escrita é opt-in (`--apply`).
- **Alternativas descartadas:** <!-- TODO: confirmar -->
- **Consequências:** Toda mudança de aula nasce no repo; o Notion é regenerável.

## #005 — Nunca rebaixar a canônica para o formato do repo legado
- **Data:** <!-- TODO: confirmar --> (registrada no ai-memory antes de 2026-07-29)
- **Status:** Aceita
- **Contexto:** O repo `elvertoni/ProfToniCoimbra` tem ~70 aulas no formato antigo do ProfessorDash, sem callouts, quiz, diagrama nem roteiro.
- **Decisão:** O repo legado é só referência histórica da grade de disciplinas. As aulas seguem a skill `prof-toni`; nunca retrofitar para o frontmatter mínimo antigo. Em conflito entre "compatível com o antigo" e "melhor para o aluno", ganha o aluno.
- **Alternativas descartadas:** Adaptar a canônica ao formato antigo para ter paridade (o Toni prefere refazer tudo do zero).
- **Consequências:** Aulas antigas são refeitas, não convertidas.

## #004 — Manifesto gerado por script, tools só com stdlib
- **Data:** 2026-06-21 (inferida)
- **Status:** Aceita
- **Contexto:** O ProfessorDash importa pelo `manifesto.json`; edição manual divergia dos arquivos (commit `a7eb0b7`).
- **Decisão:** `tools/gerar_manifesto.py` é a única fonte do manifesto, deriva a identidade do caminho e valida com `--check`. As tools usam só stdlib (parser YAML mínimo em `wiki_core.py`, sem PyYAML).
- **Alternativas descartadas:** <!-- TODO: confirmar -->
- **Consequências:** Contrato de import inviolável (§5.1 do schema). As tools rodam em qualquer Python sem instalar nada.

## #003 — Wiki de conceitos no modelo llm-wiki do Karpathy
- **Data:** 2026-06-15 (inferida)
- **Status:** Aceita
- **Contexto:** O conhecimento era reextraído a cada material, sem compor entre disciplinas (commit `0b7e337`).
- **Decisão:** Camada `conceitos/` com nós atômicos ligados por `[[slug]]`, `index.md` regenerável, `log.md` append-only e workflows `ingest`/`query`/`lint`; o LLM mantém e o Toni aprova fusão e obsolescência.
- **Alternativas descartadas:** Plugin *Karpathy LLM Wiki* do Obsidian como motor (fica só como navegação opcional).
- **Consequências:** Schema em `docs/schema-wiki.md`; o lint só propõe, nunca corrige conteúdo.

## #002 — `elite-wiki/` fica só local
- **Data:** 2026-06-14 (inferida)
- **Status:** Aceita
- **Contexto:** `lake/inteligencia-artificial/elite-wiki/` é material literal de curso pago de terceiro, puxado do Notion público (commit `4ef537d`).
- **Decisão:** `lake/**/elite-wiki/` é gitignored. Informa as aulas, mas a canônica reescreve com voz própria.
- **Alternativas descartadas:** —
- **Consequências:** Um clone novo não tem esses arquivos; recriar com `python tools/notion-wiki/puxar_notion.py`.

## #001 — Arquitetura lake → warehouse com a canônica como fonte única
- **Data:** 2026-06-14 (inferida)
- **Status:** Aceita
- **Contexto:** As aulas precisavam sair em vários formatos (portal, apostila HTML, PDF) sem divergir (commits `a066e59`, `71f6e21`).
- **Decisão:** `lake/` guarda o bruto imutável; `aulas/.../canonica.md` é a fonte única; `**/saidas/` é derivado e não versionado.
- **Alternativas descartadas:** <!-- TODO: confirmar -->
- **Consequências:** Erro de conteúdo se corrige na canônica e a saída é regerada; nunca se edita o `.html`.
