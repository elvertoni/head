# AGENTS.md — Schema do Segundo Cérebro PROF-TONI

> **O que é este arquivo.** A *camada-schema* do segundo cérebro, no modelo
> [llm-wiki do Karpathy](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f):
> um documento de governança que diz a qualquer LLM (Claude Code é o mantenedor
> principal) **como** ler as fontes, **o que** escrever na wiki e **como** mantê-la
> saudável. O humano (Toni) cura fontes e dirige; o LLM faz a manutenção:
> sintetizar, cruzar referências e bookkeeping.
>
> Leitura obrigatória antes de qualquer operação de `ingest`, `query` ou `lint`.

---

## 1. As quatro camadas

O acervo é um pipeline. Cada camada tem dono e regra de escrita distintos.

| # | Camada | Pasta | Dono / escreve | Versionada? |
|---|---|---|---|---|
| 1 | **Fontes** (raw, imutável) | `lake/{disciplina}/` | Humano coloca; LLM **lê, nunca edita** | ❌ binários e elite-wiki gitignored |
| 2 | **Conceitos** (wiki sintetizada) | `conceitos/{disciplina}/` | **LLM mantém** (este schema) | ✅ sim |
| 3 | **Aulas** (warehouse canônico) | `aulas/{disciplina}/{trilha}/{NN-slug}/canonica.md` | LLM via skill `prof-toni` | ✅ sim |
| 4 | **Saídas** (derivadas) | `**/saidas/` | Renderers (skill `aula-estatica`, ProfessorDash) | ❌ regeneráveis |

Mapeamento Karpathy → aqui:
- *Raw Sources* = camada 1 (`lake/`).
- *The Wiki* = camadas 2 **e** 3. Conceitos são os nós atômicos reusáveis; Aulas
  são páginas de síntese pedagógica que **consomem** conceitos.
- *The Schema* = este arquivo (`AGENTS.md`).

**Diferença central vs. um lake→warehouse puro:** a camada 2 (`conceitos/`) é um
**grafo de nós atômicos** (`[[rag]]`, `[[chunking]]`, `[[acoplamento]]`) que cruza
as 7 disciplinas. Uma Aula referencia conceitos; um conceito pode aparecer em
várias aulas e várias disciplinas. Isso é o que faz o conhecimento **compor** em
vez de ser re-extraído a cada material.

---

## 2. Página de conceito — formato

Arquivo: `conceitos/{disciplina}/{slug}.md`. Um conceito = um arquivo. Atômico.

> **Wikilinks resolvem por nome de arquivo no Obsidian.** Por isso `slug` é único
> em todo o vault. Namespace por pasta (`{disciplina}/`) organiza visualmente, mas
> `[[rag]]` resolve de qualquer disciplina.

### Frontmatter (obrigatório e completo)

```yaml
---
conceito: RAG                                  # nome humano
slug: rag                                       # = nome do arquivo, único no vault
disciplina: inteligencia-artificial             # disciplina-dona (origem)
tipo: conceito                                  # conceito | entidade | sintese
aka: [retrieval-augmented generation]           # apelidos p/ busca/merge; [] se nenhum
status: vivo                                    # vivo | rascunho | obsoleto
fontes:                                          # caminhos lake/ ou URLs que sustentam o conceito
  - lake/inteligencia-artificial/elite-wiki/arquitetura/blueprint-sistema-rag-para-suporte-a-alunos.md
aulas: [16, 17]                                 # ordens de aula que usam o conceito (na trilha)
atualizado_em: 2026-06-15
---
```

### Anatomia (ordem fixa)

1. **Frontmatter** — acima.
2. **Definição** — 1 parágrafo, primeiro, denso. O que é, em voz própria. Sem heading.
3. **`## Em uma frase`** — a versão de 1 linha que cabe num slide. (boa p/ query/RAG futuro)
4. **`## O que precisa saber`** — corpo: como funciona, partes, quando usar. Liga
   conceitos vizinhos com `[[wikilinks]]` no fluxo do texto, não numa lista solta.
5. **`## Erros comuns`** — armadilhas reais e diagnosticáveis (alimenta `:::atencao` das aulas).
6. **`## Onde aparece`** — backlinks: aulas e outros conceitos que dependem deste.
7. **`## Fontes`** — proveniência: de qual material do `lake/` veio cada afirmação.

Restrições:
- Voz própria. **Nunca** colar trechos longos da fonte — reescrever.
- Sem `#` H1 no corpo (título vem do frontmatter).
- Um conceito não vira aula nem ao contrário: conceito é o tijolo, aula é a parede.
- `tipo: entidade` para pessoas/orgs/produtos (ex: `[[karpathy]]`, `[[claude-code]]`);
  `tipo: sintese` para páginas que respondem uma pergunta cruzando vários conceitos.

---

## 3. Convenção de links

- `[[slug]]` — link para conceito. Use o slug exato do arquivo.
- `[[slug|texto exibido]]` — quando a frase pede outra forma.
- Linkar **liberalmente**. Um `[[slug]]` cujo arquivo ainda não existe é um *stub
  intencional* — marca dívida, vira tarefa de `ingest`, não é erro.
- Aulas (`canonica.md`) **também** linkam conceitos com `[[slug]]`. É assim que o
  `lint` cruza aula↔conceito e mantém a seção `## Onde aparece` correta.

---

## 4. Arquivos de controle da wiki

### `conceitos/index.md` — catálogo
Uma linha por conceito, agrupado por disciplina. Formato:
`- [[slug]] — resumo de uma linha · status · aulas [16,17]`
Regenerável por completo a partir dos frontmatters (operação `regenerar-index`).

### `conceitos/log.md` — diário append-only
Registro cronológico, prefixo parseável. **Nunca reescrever linhas antigas.**
```
## [2026-06-15] ingest | blueprint-sistema-rag (elite-wiki) → [[rag]], [[chunking]], [[embeddings]]
## [2026-06-15] lint | 2 órfãos, 1 link morto [[vector-store]] → criado stub
## [2026-06-16] query | "RAG vs fine-tuning" → resposta promovida a [[rag-vs-fine-tuning]] (sintese)
```

---

## 5. Workflows — ingest · query · lint

### `ingest` — material novo entra
1. Ler a fonte no `lake/` (nunca editá-la).
2. Extrair conceitos/entidades. Para cada um: criar ou **atualizar** a página em
   `conceitos/{disciplina}/`. Atualizar é o caso comum — checar se já existe (por
   `slug` ou `aka`) antes de criar duplicata.
3. Cruzar referências: adicionar `[[wikilinks]]` nos vizinhos; atualizar `## Onde aparece`.
4. Atualizar `index.md` e anexar linha em `log.md`.
5. Tipicamente toca 5–15 arquivos numa ingestão. Normal.

### `query` — pergunta do humano
1. Buscar nas páginas de conceito relevantes (não no lake bruto).
2. Sintetizar resposta **com citações** (`[[slug]]` + fonte).
3. Se a resposta tem valor durável, **promovê-la** a página `tipo: sintese` e logar.

### `lint` — saúde periódica (substitui auditoria manual)
Varre `conceitos/` e `aulas/` e reporta (uma linha por achado):
- **Link morto** — `[[slug]]` sem arquivo correspondente.
- **Órfão** — página sem nenhum inlink (ninguém aponta pra ela).
- **Backlink faltando** — aula cita `[[slug]]` mas o conceito não lista a aula em `## Onde aparece` (ou vice-versa).
- **Stale** — `atualizado_em` antigo e a `fonte` mudou depois.
- **Contradição** — duas páginas afirmam coisas incompatíveis sobre o mesmo conceito.
- **Duplicata** — duas páginas mesmo conceito (checar `aka`, inclusive entre idiomas).
- **Frontmatter incompleto** — campo obrigatório faltando.
Saída do lint nunca aplica correção sozinha em conteúdo — propõe; Toni aprova merge/obsolescência.

---

## 6. Relação com a skill `prof-toni`

`prof-toni` governa a camada 3 (aulas canônicas) — ver `.claude/skills/prof-toni/spec/`.
Este AGENTS.md governa a camada 2 (conceitos) e o pipeline inteiro. Quando uma
aula é gerada, ela deve linkar os conceitos que usa; quando um conceito muda, o
`lint` aponta as aulas afetadas. As duas specs são complementares, não concorrentes.

---

## 7. Navegação humana (Obsidian)

O vault abre no Obsidian. O grafo de `[[wikilinks]]` é navegável visualmente
(Graph View) e consultável no celular. O plugin comunitário *Karpathy LLM Wiki*
pode rodar `ingest/query/lint` pelo GUI, mas o **motor canônico é o Claude Code**
seguindo este schema — mais dirigível e dentro do versionamento git. O plugin é
opcional, para navegação/consulta, não fonte de verdade.
