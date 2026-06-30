# hermes/ — skills do Quíron (agente Hermes na VPS)

Skills do agente **Quíron** (Hermes Agent, Nous) que operam este acervo na VPS.
Versionadas aqui para distribuir via `git pull` em vez de `scp`.

## Skills

| Skill | Papel |
|---|---|
| `skills/prof-toni/operar-acervo/` | Operar o warehouse: estado, manifesto, render, ops de aula. |
| `skills/prof-toni/alimentar-cerebro/` | Workflow `ingest`: intake no `lake/` + curar o grafo `conceitos/`. |

## Instalar/atualizar na VPS

O Hermes carrega skills de `~/.hermes/skills/`. Após `git pull` do repo, copie:

```bash
cd ~/projetos/PROF-TONI && git pull
cp -r hermes/skills/prof-toni ~/.hermes/skills/
```

No chat do Hermes: `/reset` e confirme com `/skills` (devem listar `operar-acervo`
e `alimentar-cerebro`). Pré-requisito para ingestão de PDF: `sudo apt install -y
poppler-utils`.

> O pacote-fonte de setup do Quíron (SOUL, memória, config, RUNBOOK) vive separado
> em `hermes-toni/` no Windows; aqui ficam só as skills que operam o acervo.
