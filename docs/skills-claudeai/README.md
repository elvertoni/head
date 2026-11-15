# Skills só do claude.ai

Skills que vivem no claude.ai mas **não** no Claude Code deste vault. Ficam fora de
`.claude/skills/` de propósito: o Claude Code já recebe a cópia sincronizada do
claude.ai e as carregaria duas vezes.

| Skill | Papel | Fonte de verdade |
|---|---|---|
| `caderno-noturno/` | Caderno Noturno (DS v4) aplicado a artifacts do claude.ai | Derivada: tokens do `caderno.css` do ProfessorDash e da `aula-estatica` (decisão #042). Se divergir, vale o portal. |

Empacotar junto com as outras: `python3 tools/empacotar_skills.py` → `saidas/skills/*.zip`.
Depois, no claude.ai: Settings → Capabilities → Skills → Upload (substitui a versão anterior).
