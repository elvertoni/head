# Acervo de Aulas — skills do Prof. Toni

Três skills separam conteúdo, arte-base e renderização.

```
prof-toni ──cria──► canonica.md ──veste──► aula-estatica ──► apostila.html
       └──────────► imagens.md ──gera───► gerar-imagem-aula ──► arte-base PNG
```

## As três skills

| Skill | O que faz | Entrada → Saída |
|---|---|---|
| **`prof-toni`** | Gera a **Aula Canônica**: o conteúdo pedagógico no padrão (protocolo + rubrica). É onde mora a inteligência. | tema / material / SEED → `canonica.md` |
| **`aula-estatica`** | Transforma a Canônica numa **apostila HTML standalone** no visual de aulas.tonicoimbra.com (dark/light, A4, offline). | `canonica.md` → `aula.html` |
| **`gerar-imagem-aula`** | Declara o perfil (`capa` 3:2 ou `infografico` 16:9), monta o prompt v6 pronto pra colar no ChatGPT do navegador e depois audita o PNG contra 12 defeitos conhecidos. **Não gera imagem** — a geração é no navegador. | `canonica.md` + `imagens.md` → prompt colável → (navegador) → arte-base PNG validada |

São independentes de propósito: você pode gerar a Canônica hoje e vesti-la semana que vem, sem regerar conteúdo. E a Canônica também alimenta o ProfessorDash — a apostila é só uma das saídas possíveis.

## Fluxo no dia a dia

1. **Criar** — peça ao Claude Code: *"cria uma aula sobre X, série 3ª, trilha programacao"*. A `prof-toni` planeja, espera seu OK, gera e audita → salva `canonica.md`.
2. **(Opcional) Arte-base** — peça para aplicar `gerar-imagem-aula` ao `imagens.md`. Ela devolve o prompt v5 colável; você gera no ChatGPT do navegador, salva em `img/` e pede a validação. Cantos superiores ficam vazios; Photoshop aplica branding depois.
3. **(Opcional) Vestir** — quando quiser distribuir offline/PDF: *"aplica a skill aula-estatica na canônica da Aula NN"* → sai um `.html` único.
4. **Publicar** — a Canônica vai pro ProfessorDash; a apostila `.html` vai pro aluno baixar. (No seu caso atual: publicar pelo ProfessorDash como já faz.)

## Instalação (Claude Code)

```bash
# pessoal — vale em qualquer projeto
mkdir -p ~/.claude/skills
cp -r prof-toni aula-estatica gerar-imagem-aula ~/.claude/skills/

# OU por projeto — junto da pasta do acervo (recomendado)
mkdir -p .claude/skills
cp -r prof-toni aula-estatica .claude/skills/
```

Rode o Claude Code **dentro da pasta do seu acervo** para os caminhos
`aulas/{disciplina}/{trilha}/{NN-slug}/canonica.md` baterem.

### Outros agentes (Codex, GLM)
O `AGENTS.md` encaminha a geração visual para `gerar-imagem-aula`. Em ambientes
que não descobrem `.claude/skills/` automaticamente, aponte o arquivo na conversa:
> "Leia prof-toni/SKILL.md e siga as instruções."
> "Leia aula-estatica/SKILL.md e aplique no arquivo canonica.md."
> "Leia gerar-imagem-aula/SKILL.md e execute o brief imagens.md."

## Regra que amarra tudo

A `canonica.md` é a **fonte única de verdade**. Erro de conteúdo? Corrige a Canônica
e regenera a apostila — nunca edita o `.html` na mão. Conteúdo se escreve uma vez,
se consome em muitos formatos.
