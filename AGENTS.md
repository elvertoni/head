# PROF-TONI — Acervo de Conhecimento do Prof. Toni Coimbra

Segundo cérebro (vault Obsidian) e acervo de aulas do Curso Técnico em Desenvolvimento de Sistemas (SEED-PR,
alunos de 14 a 18 anos, aulas de 50 min). Pipeline lake → wiki de conceitos → aulas canônicas → saídas; as aulas
aprovadas são importadas pelo portal ProfessorDash. Status: em produção (89 aulas aprovadas em 2026-09-28).

**Stack:** Markdown + frontmatter YAML (vault Obsidian), Python 3 só com stdlib em `tools/`, faster-whisper
(`tools/transcrever/`, venv própria via uv), API do Notion, Jev/TypeSafe. Sem CI.
**Repositório:** https://github.com/elvertoni/head (**público**, branch `main`)  |  **Ambiente de produção:**
ProfessorDash (repo próprio, Django) importa `manifesto.json` + `aulas/**/canonica.md` do tarball do GitHub.

Arquitetura, estado do vault, comportamento do gerador do manifesto e integrações: `.ai/context.md`.
Schema da wiki (formato de conceito, links, arquivos de controle, workflows `ingest`/`query`/`lint` e o contrato
do portal completo em §5.1): `docs/schema-wiki.md` — **leitura obrigatória antes de qualquer `ingest`, `query`
ou `lint`**.

## Protocolo obrigatório de início de sessão
Antes de qualquer alteração:
1. Leia `.ai/context.md`, `.ai/decisions.md` e `.ai/handoff.md`.
2. Rode `git status` e `git log --oneline -10`.
3. Responda com um resumo de no máximo 5 linhas: objetivo do projeto, estado atual,
   tarefa em andamento e próximo passo sugerido.
4. Aguarde minha confirmação antes de alterar código.

## Checkpoints durante o trabalho
O limite de tokens pode chegar sem aviso. Após cada marco (tarefa concluída,
decisão tomada, bug entendido, antes de uma mudança grande), atualize em
`.ai/handoff.md` apenas as seções "Em andamento" e "Próximos passos" — 3 a 5
linhas, sem reescrever o arquivo inteiro e sem pedir confirmação.

## Protocolo obrigatório de encerramento / troca
Quando eu disser "handoff", "vou trocar", "encerrar sessão" ou similar,
execute as instruções de `.ai/prompts/handoff.md`.

## Regras de memória
- Decisão técnica relevante tomada na sessão → registrar em `.ai/decisions.md`.
- Mudança de arquitetura, dependência nova ou módulo novo → atualizar `.ai/context.md`.
- Nunca apagar entradas de `decisions.md`; decisões revogadas são marcadas como "Substituída por #N".
- `.ai/handoff.md` e `.ai/sessions/` são **local-only** (gitignored): o repo é público.
- O ai-memory (MCP) complementa, não substitui estes arquivos: guarda só conhecimento revisado e útil entre
  projetos. Não duplicar nele o handoff nem as decisões (ver decisão #013).
- `conceitos/log.md` é o diário da wiki (append-only), não o log de decisões do projeto.

## Invariantes do acervo (contrato do portal — INVIOLÁVEL)
1. **A canônica é a fonte única de verdade.** HTML, PDF e import do portal derivam de `canonica.md`; nunca
   editar uma saída — corrigir a canônica e regerar.
2. **Regerar o manifesto** com `python tools/gerar_manifesto.py` após adicionar, aprovar ou editar aula, ou
   mudar frontmatter. Nunca editar `manifesto.json` à mão.
3. **Bump de versão:** toda edição em aula `status: aprovada` incrementa `versao` ou avança `atualizado_em`;
   sem isso o portal pula a aula.
4. **O lake é imutável:** nenhum agente edita `lake/` nem `aulas/**/fontes/`; só lê.
5. **Frontmatter e caminho do contrato:** `titulo`, `disciplina`, `trilha`, `ordem`, `slug`, `status`,
   `versao`, `atualizado_em`; caminho `aulas/{disciplina}/{trilha}/{NN}-{slug}/canonica.md` com `NN` = `ordem`
   em 2 dígitos, casando com o manifesto. O portal só importa `status: aprovada`.
6. **Publicar são quatro passos, nesta ordem:** `gerar_manifesto.py` → push do acervo → deploy do portal →
   reimport com `--force` (botão "Importar do GitHub" em `/catalogo/` ou `import_acervo --force` no
   container). Pular o passo 4 deixa o portal defasado sem erro nenhum.

## Convenções do projeto
- Conteúdo, docs, comentários e commits em português (pt-BR); identificadores das tools também em pt-BR.
- Commits: Conventional Commits em pt-BR com os escopos do acervo — `aula(<disciplina>)`,
  `imagem(<disciplina>)`, `design(...)`, `feat(wiki)`, `feat(tools)`, `fix(...)`, `docs(...)`, `chore(...)`.
  Direto na `main`, sem fluxo de PR.
- Git sempre por SSH com a conta `elvertoni` (`git@github.com:elvertoni/...`); nunca HTTPS.
- Pasta de aula: `canonica.md`, `imagens.md` (sempre gerado), `capa.png`, `img/` (figuras do corpo, só
  aparecem se referenciadas como `![alt](img/arquivo.png)`) e `fontes/` (imutável).
- **Nunca renumerar** aula já importada: `NN`/`ordem` faz parte da chave do portal e gera duplicata.
- O corpo da canônica usa catálogo **fechado** de blocos (6 callouts, `:::roteiro`, ` ```quiz `,
  ` ```diagrama-progressivo `) — `.claude/skills/prof-toni/spec/01-CANONICA.md` §5–§7. Interativos são YAML
  real; cada pergunta de quiz tem exatamente uma `correta: true`; `rotulo` de diagrama sem número próprio.
- Aula nova só pela skill `prof-toni` (plano → OK do Toni → rubrica 7/7 de `spec/02-RUBRICA.md`), uma por vez.
  Imagens só pela skill `gerar-imagem-aula`; apostila HTML standalone pela `aula-estatica`.
- Ingestão não é publicação: fonte no `lake/` pode alimentar conceitos sem virar aula. Aula nasce só de decisão
  pedagógica explícita.
- Wiki: `slug` único em todo o vault; atualizar conceito existente (por `slug`/`aka`) antes de criar duplicata;
  nas aulas, preferir `[[slug|rótulo]]`.
- Tools continuam stdlib-only (sem PyYAML). Rodar os testes antes de commitar mudança em `tools/`.
- Antes de editar qualquer `mapas/*.base`, ler a skill `obsidian-bases` (plugin kepano em `.claude/settings.json`).
- `hermes/skills/` são skills do agente Quíron (Hermes, na VPS), não do Claude Code — ver `hermes/README.md`.
- Ao tocar no acervo, rode também `python tools/gerar_manifesto.py --check` e `git status --short` para não
  misturar trabalho humano não versionado com mudanças do agente.

## Comandos úteis
- Subir ambiente: não há servidor — a raiz é o vault do Obsidian (`mapas/index.md` é a página de entrada).
  Venv do transcritor numa máquina nova: `cd tools\transcrever; uv venv --python 3.12; uv pip install -r requirements.txt`
- Testes: `python -m unittest discover -s tests -v` (um módulo: `python -m unittest tests.test_wiki -v`)
- Manifesto (no lugar de migrações): `python tools/gerar_manifesto.py --check` · `python tools/gerar_manifesto.py`
- Wiki: `python tools/lint_wiki.py` (`--format json`, `--fail-on error`) · `python tools/gerar_indice.py --check|--write`
  · `python tools/gerar_mapas.py [--check]`
- RCO (SEED): `python tools/extrair_rco.py [--sigla AMS] [--check]` · `python tools/triar_rco.py` (precisa de
  `$env:TYPESAFE_API_KEY`)
- Notion (repo → Notion, precisa de `$env:NOTION_TOKEN`): `python tools/sync_notion.py` (só plano) · `--check` ·
  `--apply` · `--apply --prune`. Entrada do Notion para o lake: `python tools/notion-wiki/puxar_notion.py`
- Transcrever áudio/vídeo para o lake: `.\tools\transcrever\transcrever.ps1 "C:\videos\aula.mp4" --disciplina <slug> --fonte <fonte> --titulo "<título>"`

## Não fazer
- Não editar `lake/`, `aulas/**/fontes/` nem saídas geradas (`**/saidas/`, apostilas `.html`).
- Não editar à mão arquivos derivados: `manifesto.json`, `conceitos/index.md`, `mapas/*.md` (exceção única: o
  seed de disciplina nova no manifesto — ver `.ai/context.md`).
- Não reescrever linhas antigas de `conceitos/log.md`.
- Não aplicar sozinho correção de conteúdo apontada pelo lint: fusão e obsolescência exigem aprovação do Toni.
- Não republicar trecho literal de `lake/**/elite-wiki/` (curso pago de terceiro, local-only).
- Não rebaixar a canônica para o formato do repo legado `elvertoni/ProfToniCoimbra`.
- Não tratar o material das duas pós-graduações no `lake/` como fonte de aula sem pedido explícito.
- Não anexar a logo ao modelo de imagem: logo, curso e canvas são aplicados depois pela action do Photoshop.
- Não commitar segredos (`NOTION_TOKEN`, `TYPESAFE_API_KEY`, tokens de painel), `.env`, `.ai/handoff.md` nem
  `.ai/sessions/`.
