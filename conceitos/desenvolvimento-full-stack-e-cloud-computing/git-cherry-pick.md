---
conceito: Git cherry-pick
slug: git-cherry-pick
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [cherry-pick]
status: rascunho
fontes:
  - "lake/programacao-front-end/Git--para--iniciantes.pdf"
aulas: []
atualizado_em: 2026-08-01
---

Git cherry-pick aplica em uma branch as mudanças de um commit escolhido de outra linha de histórico, sem incorporar necessariamente todos os commits intermediários. É útil para correções seletivas, mas pode duplicar mudanças e criar divergência se a mesma solução continuar sendo desenvolvida em paralelo.

## Em uma frase

Cherry-pick transporta seletivamente um commit para outra branch.

## O que precisa saber

O comando cria um novo commit com mudança equivalente, não move o objeto original. Conflitos e dependências precisam ser tratados, e a mensagem deve explicar por que a seleção é necessária. Fluxos como [[gitflow]] podem usar a técnica para hotfixes; revisão e testes continuam obrigatórios.

## Erros comuns

- Aplicar commit sem suas dependências e quebrar compilação.
- Usar cherry-pick para mascarar branches divergentes continuamente.
- Esquecer que o mesmo conteúdo pode ter dois commits diferentes.

## Onde aparece

- `Git--para--iniciantes.pdf`, páginas 59–60.
- Relaciona-se a [[git]], [[controle-de-versao]], [[gitflow]] e [[conflito-de-merge]].

## Fontes

- `lake/programacao-front-end/Git--para--iniciantes.pdf`, páginas 59–60.
