# Registro de Decisões

<!-- Entradas mais recentes no topo. Não apagar entradas antigas. -->
<!-- Numeração cronológica. Entradas "(inferida)" foram reconstruídas do histórico git, do antigo CLAUDE.md e das páginas do ai-memory em 2026-09-28. -->

## #037 — Trilha "Usabilidade e Design de Serviços" redistribuindo as aulas SEED 87–95
- **Data:** 2026-11-04
- **Status:** Aceita; plano de 11 aulas aprovado pelo Toni. Canônicas produzidas em três lotes autorizados (01–04, 05–08, 09–11), todas `rascunho` v1 até a aprovação.
- **Decisão:** Abrir `analise-e-metodos-para-sistemas/usabilidade-e-design-de-servicos`, com numeração própria (01–11), sem seguir os números RCO, porque os 9 decks foram redistribuídos em 11 aulas: as 10 heurísticas viraram 2 aulas de 5 mais um laboratório de avaliação heurística (87–88 → 01–03); 89 → 04; 90/91, que se repetiam, viraram conceito de serviço (05) e jornada/frontstage/backstage (06); 92 → 07; 93 → 08; 94/95 viraram uma aula por ferramenta (09 Lean Canvas, 10 Service Blueprint) mais o projeto integrador FilaZero (11). O rótulo foi registrado em `LABELS_TRILHA`.
- **Fontes:** os PPTX e o docx da SEED ficam em `lake/analise-e-metodos-para-sistemas/seed-87-95/` (binários gitignored, como os decks 34–55 da mesma disciplina), não em `fontes/` das aulas.
- **Correções da origem registradas nas canônicas (`revisao: true`):** comentário da Q1 do docx 87 ("heurísticas não tratam de estética"; a heurística 8 trata); "Erro 504 — operação inválida" no deck 88 (504 é Gateway Timeout); resposta "Lei de Hick" colada no desafio do deck 90; princípios do Design de Serviços atualizados da edição de 2011 (5) para a de 2018 (6).

## #036 — Imagens de aula saem finais, sem marca (prompt v8); action do Photoshop descontinuada
- **Data:** 2026-11-04
- **Status:** Aceita. O Toni informou que a action do Photoshop não existe mais e delegou a decisão ao ASTRA (Codex `gpt-6-astra`), que escolheu a opção B. Substitui a parte de branding externo de #008 e a reserva de cantos do prompt v6/v7.
- **Decisão:** `tools/imagen-generator/prompt.xml` v8, modo `arte_final_sem_branding`. O PNG auditado vai direto para `capa.png`/`img/`, sem normalização de canvas. As zonas reservadas (R1) dão lugar à margem segura de 8% e ao título usando o topo inteiro. Continua proibido o modelo desenhar logo, "TC", nome ou curso, porque o portal e a apostila exibem a marca ao redor da imagem. D7 foi aposentado (o id não é reaproveitado); D6 passa a cobrir também cantos deixados vazios.
- **Evidência:** o importador do ProfessorDash salva os bytes da capa e o card a exibe como está, sem sobrepor marca; as capas aprovadas de `landing-page-mvp` não têm logo aplicada.
- **Consequências:** `montar_prompt.py` exige v8; skills `gerar-imagem-aula`, `aula-estatica` e `prof-toni`, LEIA-ME (renomeado para v8), `schema-wiki.md` e `AGENTS.md` foram atualizados. Os `imagens.md` de aulas já aprovadas ficam como registro histórico. A rubrica ganhou dois itens: sintoma de `:::atencao` verificado e `diagrama-progressivo` onde o processo pede.

## #035 — Trilha JavaScript na prática com retomada preparatória
- **Data:** 2026-11-03
- **Status:** Aceita; sequência de 20 encontros aprovada pelo Toni. As 20 aulas foram produzidas em lotes autorizados (2026-11-03/04), passaram por rubrica independente com correções (v2 nas aulas 12, 16, 17 e 18) e foram aprovadas para publicação em 2026-11-04.
- **Decisão:** Abrir `programacao-front-end/javascript-na-pratica`, com numeração própria (1–20), preservando as identidades das aulas existentes; registrar o rótulo em `LABELS_TRILHA`. A chave do portal inclui a trilha (`disciplina, trilha, ordem, slug`), então as ordens 1–18 das outras trilhas de front-end não colidem.
- **Produção:** Canônica como fonte única; apostila offline derivada pela skill `aula-estatica`, em `saidas/`. Plano e sequência em `docs/plano-apostila-javascript.md`.

## #017 — Texto proporcional opcional e resumo por tema nas apostilas standalone
- **Data:** 2026-10-16
- **Status:** Aceita para a apostila de revisão DS, a pedido do Toni (pontos da revisão do Codex).
- **Contexto:** A apostila DS tem cerca de 43 mil palavras em mono; faltavam um roteiro de estudo, uma revisão de véspera e uma versão impressa sem respostas.
- **Decisão:** O template `aula-estatica` ganha `body[data-texto="proporcional"]` (Archivo 400 no texto corrido; código, rótulos e títulos de parte seguem em JetBrains Mono), o bloco `.resumo` (BLOCOS §19) e o botão "PDF sem respostas" (`data-print-mode="treino"`). A Archivo embutida passa a ser declarada de 400 a 900 (o arquivo já é variável).
- **Consequências:** Outras apostilas continuam em mono, a menos que ativem o atributo. A apostila DS ganhou roteiro de 18 sessões, oito resumos e o PDF completo caiu de 202 para 194 páginas (182 no PDF sem respostas).

## #016 — Leitura ampla opcional nas apostilas standalone
- **Data:** 2026-10-16
- **Status:** Aceita para a apostila de revisão DS, a pedido do Toni.
- **Contexto:** A página tinha 1120 px disponíveis no desktop, mas os parágrafos usavam apenas 682 px e os exercícios tinham outra largura.
- **Decisão:** O template `aula-estatica` oferece `body[data-layout="amplo"]`: texto e componentes alinhados na largura disponível, com limite de 1200 px, adaptação ao celular e regras de impressão A4. Aplicado à apostila DS por regeneração do CSS a partir do template, preservando conteúdo e JavaScript.
- **Consequências:** Outras apostilas só usam a largura ampla quando ativada explicitamente. Mantidas as fontes Archivo e JetBrains Mono. A revisão DS continua standalone; cópia anterior, regenerador e evidências visuais ficam em `scratch/revisao-visual/` (local-only).

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
- **Decisão:** Publicar = `gerar_manifesto.py` → push do acervo → deploy do portal → reimport com `--force`. Confirmada pelo Toni em 2026-09-28.
- **Alternativas descartadas:** — (nenhuma considerada)
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
- **Status:** Aceita quanto aos perfis; o local de geração foi substituído por #010; o branding externo pelo Photoshop foi substituído por #036
- **Contexto:** A auditoria das 54 imagens aprovadas mostrou que o prompt v5 estava calibrado abaixo do acervo, e a ferramenta de imagem do Claude Code saía pior que o ChatGPT (commit `c12bac6`).
- **Decisão:** `tools/imagen-generator/prompt.xml` v6 tem dois perfis — `capa` (3:2, 4–10 blocos com micro-parágrafo, subtítulo e faixa de rodapé) e `infografico` (16:9, 2–5 blocos só com rótulos). Declarar o perfil é o passo 0. Paleta com fundo navy quase preto e ciano como âncora. `imagens.md` traz um brief de `capa` e no máximo um de `infografico`, sem prompt escrito à mão. O branding é aplicado depois pelo Photoshop.
- **Alternativas descartadas:** Fundir os dois formatos num spec só; manter a geração no Claude Code; proibir render 3D (aparece em ~15 das 54 aprovadas).
- **Consequências:** Auditoria objetiva pela regra `R3` (12 defeitos reais já publicados).

## #007 — Manifesto exporta `conceitos[]` para o portal
- **Data:** 2026-07-27 (inferida)
- **Status:** Aceita
- **Contexto:** Slugs não têm acento, então o portal mostraria "aprendizado de maquina" ao derivar o nome do slug (commit `38da690`).
- **Decisão:** `manifesto.json` leva `conceitos[]` com `{slug, nome, disciplina}` de todo nó não obsoleto. Nas aulas, preferir `[[slug|rótulo]]`; o mapa é a rede de segurança.
- **Alternativas descartadas:** O portal derivar o nome do slug (sem acento; mostraria "aprendizado de maquina" ao aluno).
- **Consequências:** O contrato do portal (§5.1 do schema) inclui `conceitos[]`.

## #006 — Notion como projeção de mão única do índice de aulas
- **Data:** 2026-07-27 (inferida)
- **Status:** Aceita
- **Contexto:** O workspace "Toni's Brain" precisava listar as aulas sem virar segunda fonte de verdade (commit `97cb97e`).
- **Decisão:** `sync_notion.py` espelha só metadados + link do ProfessorDash na base `Aulas`, com chave `Caminho`. O Notion nunca é entrada. A escrita é opt-in (`--apply`).
- **Alternativas descartadas:** Notion como lugar regular de autoria de aulas. Usar o Notion para uma aula é só pontual, quando o Toni quer algo bem rápido — não é regra (confirmado pelo Toni em 2026-09-28).
- **Consequências:** Toda mudança de aula nasce no repo; o Notion é regenerável. Uma aula feita pontualmente no Notion não é fonte de verdade nem aparece no portal enquanto não virar `canonica.md`.

## #005 — Nunca rebaixar a canônica para o formato do repo legado
- **Data:** 2026-06-14 (inferida — data da memória legada `acervo-legado-regerar-do-zero.md`)
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
- **Alternativas descartadas:** Manifesto mantido à mão, como no commit `71f6e21` (inferida).
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
- **Contexto:** As aulas precisavam sair em vários formatos (portal, apostila HTML, PDF) sem divergir (commits `a066e59`, `71f6e21`). Também era preciso um lugar de ingestão inicial: o conhecimento de um material tem que continuar no vault mesmo que o original seja apagado depois (motivo confirmado pelo Toni em 2026-09-28).
- **Decisão:** `lake/` é o ponto de entrada e guarda o bruto imutável; o conhecimento extraído vive em `conceitos/` e `aulas/.../canonica.md`, que é a fonte única da aula; `**/saidas/` é derivado e não versionado.
- **Alternativas descartadas:** Trabalhar direto sobre os arquivos originais, sem etapa de ingestão — o conhecimento ficaria preso ao original e se perderia junto com ele.
- **Consequências:** Erro de conteúdo se corrige na canônica e a saída é regerada; nunca se edita o `.html`. Perder o bruto não apaga o conhecimento: os avisos `source-missing` do lint (fonte que não está nesta máquina) são esperados e não significam conteúdo perdido; a lacuna de proveniência só precisa ficar explícita.
