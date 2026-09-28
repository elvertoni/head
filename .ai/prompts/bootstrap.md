# Bootstrap de memória portável

Você vai preparar este repositório para que qualquer agente de IA consiga retomar o trabalho sem perda de contexto.

1. Explore o projeto: estrutura de pastas, README, arquivos de dependência
   (pyproject, requirements, package.json), settings, docker-compose, CI,
   `git log --oneline -30` e quaisquer CLAUDE.md, AGENTS.md, GEMINI.md,
   .cursorrules ou docs de IA já existentes.
2. Crie ou atualize os arquivos seguindo os templates:
   - `AGENTS.md` (incorporando instruções úteis de arquivos de IA já existentes)
   - `CLAUDE.md` e `GEMINI.md` contendo apenas `@AGENTS.md`
   - `.ai/context.md`
   - `.ai/decisions.md` (registre decisões que dá para inferir com segurança do
     código/histórico, marcando-as com "(inferida)")
   - `.ai/handoff.md` com o estado atual do repositório
3. Regras:
   - Não invente nada. O que não puder confirmar, marque como `<!-- TODO: confirmar -->`.
   - Não inclua segredos, tokens ou valores do .env.
   - Seja conciso: AGENTS.md com no máximo ~150 linhas.
4. Ao final, liste os TODOs que precisam da minha confirmação.
