# Acervo de Aulas — skills do Prof. Toni

Duas skills que trabalham em sequência. Uma **cria** o conteúdo, a outra o **veste**.

```
prof-toni       ──cria──►   canonica.md   ──veste──►   aula-estatica   ──►  apostila.html
(o quê ensinar)            (fonte única)              (como aparece)        (arquivo p/ aluno)
```

## As duas skills

| Skill | O que faz | Entrada → Saída |
|---|---|---|
| **`prof-toni`** | Gera a **Aula Canônica**: o conteúdo pedagógico no padrão (protocolo + rubrica). É onde mora a inteligência. | tema / material / SEED → `canonica.md` |
| **`aula-estatica`** | Transforma a Canônica numa **apostila HTML standalone** no visual de aulas.tonicoimbra.com (dark/light, A4, offline). | `canonica.md` → `aula.html` |

São independentes de propósito: você pode gerar a Canônica hoje e vesti-la semana que vem, sem regerar conteúdo. E a Canônica também alimenta o ProfessorDash — a apostila é só uma das saídas possíveis.

## Fluxo no dia a dia

1. **Criar** — peça ao Claude Code: *"cria uma aula sobre X, série 3ª, trilha programacao"*. A `prof-toni` planeja, espera seu OK, gera e audita → salva `canonica.md`.
2. **(Opcional) Vestir** — quando quiser distribuir offline/PDF: *"aplica a skill aula-estatica na canônica da Aula NN"* → sai um `.html` único.
3. **Publicar** — a Canônica vai pro ProfessorDash; a apostila `.html` vai pro aluno baixar. (No seu caso atual: publicar pelo ProfessorDash como já faz.)

## Instalação (Claude Code)

```bash
# pessoal — vale em qualquer projeto
mkdir -p ~/.claude/skills
cp -r prof-toni aula-estatica ~/.claude/skills/

# OU por projeto — junto da pasta do acervo (recomendado)
mkdir -p .claude/skills
cp -r prof-toni aula-estatica .claude/skills/
```

Rode o Claude Code **dentro da pasta do seu acervo** para os caminhos
`aulas/{disciplina}/{trilha}/{NN-slug}/canonica.md` baterem.

### Outros agentes (Codex, GLM)
Sem formato de skill nativo. Aponte o arquivo na conversa:
> "Leia prof-toni/SKILL.md e siga as instruções."
> "Leia aula-estatica/SKILL.md e aplique no arquivo canonica.md."

## Regra que amarra tudo

A `canonica.md` é a **fonte única de verdade**. Erro de conteúdo? Corrige a Canônica
e regenera a apostila — nunca edita o `.html` na mão. Conteúdo se escreve uma vez,
se consome em muitos formatos.
