---
name: operar-acervo
description: >
  Operar o acervo de aulas do Prof. Toni (repo PROF-TONI, pipeline lake→warehouse)
  na VPS: ler estado, validar/regenerar o manifesto, criar/renderizar/atualizar
  aulas respeitando as invariantes, e versionar com disciplina. Use quando o Toni
  pedir algo sobre aulas, acervo, manifesto, canônica, conceitos, ou os projetos
  PROF-TONI/ProfessorDash.
version: 1.1.0
platforms: [linux, macos]
metadata:
  hermes:
    tags: [acervo, aulas, prof-toni, manifesto, pipeline]
    category: prof-toni
    requires_toolsets: [terminal]
---

# Operar o acervo PROF-TONI

Procedimento para o Quíron operar o acervo de aulas do Prof. Toni com segurança.
O repositório está clonado na VPS em `~/projetos/head`. **Sempre opere de
dentro da raiz do repo** — lá o `AGENTS.md`/`CLAUDE.md` do projeto já é carregado (o schema da wiki está em `docs/schema-wiki.md`).

## Quando usar

Pedidos sobre: aulas, acervo, manifesto, aula canônica, conceitos, trilhas,
disciplinas, exportar/renderizar aula, ou os projetos PROF-TONI / ProfessorDash.

## Modelo mental (pipeline lake→warehouse)

```
lake/        fontes brutas IMUTÁVEIS  (status: bruto) — só leitura
conceitos/   wiki atômica de conceitos (Karpathy llm-wiki)
aulas/       aula canônica = FONTE ÚNICA DE VERDADE
aulas/**/saidas/  artefatos gerados (HTML/PDF) — nunca editar à mão
```

Caminho da aula: `aulas/{disciplina}/{trilha}/{NN-slug}/canonica.md`, onde `NN`
(2 dígitos) **bate** com `ordem` na frontmatter e no `manifesto.json`. Cada pasta
de aula tem `canonica.md`, `imagens.md` (briefing visual — regra do Toni) e `capa.png`.

## Invariantes (NUNCA violar)

1. **Canônica é SOT** — todas as saídas derivam dela; nunca editar saída direto.
2. **Nunca editar `lake/`** — só ler para extrair material.
3. **`manifesto.json` é gerado** — nunca editar à mão. Só aulas `status: aprovada`
   entram em `lessons[]`. É o contrato de import do ProfessorDash.
4. **Toda aula tem `imagens.md`.**
5. **Editar aula aprovada → bump** de `versao` ou avançar `atualizado_em`.
6. **Contrato de frontmatter do portal:** `titulo, disciplina, trilha, ordem,
   slug, status, versao, atualizado_em` completos.
7. **Nunca renumerar** aula já importada: `NN`/`ordem` faz parte da chave do
   portal e gera duplicata.
8. **`aulas/**/fontes/` é imutável**, como o `lake/`.

## Passo 0 — ler estado antes de agir

```bash
cd ~/projetos/head && git pull
python3 tools/gerar_manifesto.py --check   # valida manifesto vs aulas/
git status --short                         # não misturar trabalho humano não versionado
```

Não inventar fato sobre o acervo — ler o repo, `spec/` e a frontmatter primeiro.

## Criar / planejar aula

A criação de aula canônica **é da skill `prof-toni`** (segue
`.claude/skills/prof-toni/spec/`, com auditoria pela rubrica 7/7 em
`spec/02-RUBRICA.md` como gate de aprovação; plano → OK do Toni → aula, uma por
vez, mesmo quando é aula única). **Não burlar** — ler `spec/00-PROTOCOLO.md`
antes. Cobre 3 modos: Tema, Material, SEED.

Conferir o corpo contra o catálogo fechado de blocos antes de aprovar:

```bash
python3 tools/lint_canonica.py aulas/<disciplina>/<trilha>/<NN-slug>/canonica.md
```

Depois de criar/aprovar aula: **regenerar o manifesto** (passo abaixo).

## Renderizar aula (HTML/apostila)

Renderização é da skill `aula-estatica` (`canonica.md` → `.html` standalone,
dark/light, A4-print). Saída vai em `saidas/` (não versionada, sempre regenerável).

## Regenerar o manifesto (após QUALQUER mudança de aula)

```bash
python3 tools/gerar_manifesto.py
python3 tools/gerar_manifesto.py --check   # confirmar 0 divergências
```

## Publicar no portal (quatro passos, nesta ordem)

1. `python3 tools/gerar_manifesto.py`
2. push do acervo (`git push origin main`, só se o Toni pediu o commit)
3. deploy do ProfessorDash (automático pelo Easypanel quando o portal mudou)
4. reimport com `--force` (botão "Importar do GitHub" em `/catalogo/` ou
   `import_acervo --force` no container)

Pular o passo 4 deixa o portal defasado sem erro nenhum.

## Conceitos (wiki)

`conceitos/{disciplina}/{slug}.md`. Aulas referenciam via `[[slug]]`. Não reescrever
`conceitos/log.md` (append-only). `conceitos/index.md` é regenerável. Ingerir
material novo no cérebro é da skill `alimentar-cerebro`. Detalhes do
`puxar_notion.py` (endpoint, IDs, limites): `references/notion-ingestion.md`.

## Segurança operacional

- **Commit é decisão do Toni.** Mostrar diff e propor a mensagem; só commitar se
  ele pedir. Commit direto na `main`, sem branch nem PR (regra do repo), em
  Conventional Commits pt-BR com os escopos do acervo (`aula(<disciplina>)` etc.).
- Git remoto usa SSH dual-account → este repo usa a conta **elvertoni**.
- Mudou aula aprovada sem bump de versão? Corrigir antes de regenerar manifesto.

## Checklist de saída

- [ ] `imagens.md` presente na aula
- [ ] frontmatter completo (contrato do portal) e `NN` == `ordem`
- [ ] `versao`/`atualizado_em` bumpados se a aula era aprovada
- [ ] `python3 tools/gerar_manifesto.py --check` → 0 divergências
- [ ] diff revisado; commit proposto ao Toni (não auto-commitado)
