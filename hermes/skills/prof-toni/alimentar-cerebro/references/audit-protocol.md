# Protocolo de Auditoria de Ingestão (3 fases)

Usado quando o Toni pede "audita minha ingestão" ou "revisa o que eu ingeri".
Adaptado da sessão 2026-06-29/30 — auditoria dos 4 encontros elite.

## Fase 1 — baixar atualizações e preparar

1. `cd ~/projetos/head`
2. `git status --short` + `git log --oneline -5` — estado atual
3. `git pull --rebase origin main` — se der conflito, PARAR e reportar
4. Instalar/atualizar skills do `hermes/skills/` se houver
5. Verificar ferramentas: `pdftotext` (poppler-utils) para PDFs

## Fase 2 — auditar contra o protocolo

### Lake (fonte bruta)

Para cada arquivo novo no lake/:
- [ ] Frontmatter completo: `titulo`, `disciplina`, `fonte`, `origem`, `data`, `status: bruto`
- [ ] `fonte` é categoria curta (elite-wiki, ia-coders, pycodebr), não descrição longa
- [ ] `origem` é URL ou canal de transporte (link Notion, YouTube, telegram)
- [ ] Arquivo NÃO foi editado depois de criado (lake imutável)
- [ ] Arquivo está no caminho correto: gitignored (local-only) ou versionado conforme design da fonte

### Conceitos

Para cada conceito criado/atualizado:
- [ ] Frontmatter completo: `conceito, slug, disciplina, tipo, aka, status, fontes, aulas, atualizado_em`
- [ ] Anatomia fixa: Definição → `## Em uma frase` → `## O que precisa saber` → `## Erros comuns` → `## Onde aparece` → `## Fontes`
- [ ] Sem H1 no corpo (título vem do frontmatter)
- [ ] Voz própria — sem trecho colado da fonte
- [ ] Sem duplicata: checar `slug` e `aka` contra conceitos existentes

### Grafo (wikilinks)

- [ ] `[[wikilinks]]` no conceito novo apontam para vizinhos existentes (ou stubs intencionais)
- [ ] **Backlinks recíprocos**: cada conceito referenciado tem `[[novo-conceito]]` no seu `## Onde aparece`
- [ ] Stubs (links sem arquivo) estão declarados no comentário do `index.md`

### Controle (index/log)

- [ ] `conceitos/index.md` tem entrada para o novo conceito
- [ ] `conceitos/log.md` tem linha **anexada** (nunca substituída): `## [YYYY-MM-DD] ingest | ...`
- [ ] Comentário de stubs no `index.md` está atualizado

## Fase 3 — relatório (formato)

Entregar lista, uma linha por achado:

```
<arquivo>: <problema>. <correção proposta>.
```

Agrupar por: **lake**, **conceitos**, **links/grafo**, **controle (index/log)**.

No fim: plano de correção + mensagem de commit proposta. **NUNCA aplicar correções
sem aprovação explícita do Toni** ("aprovado", "aplica", "pode corrigir").

## Armadilhas da auditoria

- **log.md substituído**: diff mostra `-` na última linha antiga + `+` na nova.
  Recuperação (antes do commit): `git checkout -- conceitos/log.md` e re-anexar com `>>`.
- **Backlinks faltando**: comum em ingestões rápidas. Verificar com
  `grep -rn 'novo-slug' conceitos/` e comparar com os `[[links]]` do conceito novo.
- **Stubs desatualizados**: o comentário `<!-- stubs pendentes -->` no index.md
  frequentemente fica defasado. Comparar com `grep -oP '\[\[([^\]|]+)'` nos conceitos
  e verificar quais não têm arquivo.
- **fonte vs origem trocados**: `fonte: "Elite Wiki (Notion publico)"` está errado.
  Deve ser `fonte: elite-wiki` + `origem: https://...notion.site/...`.
