---
conceito: Git hooks
slug: git-hooks
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [ganchos do Git]
status: rascunho
fontes:
  - "lake/programacao-front-end/Git--para--iniciantes.pdf"
aulas: []
atualizado_em: 2026-08-01
---

Git hooks são scripts executados automaticamente em eventos do Git, como antes de um commit, depois de um merge ou antes de um push. Eles podem reforçar verificações locais e automatizar tarefas, mas precisam ser reproduzíveis e não podem ser a única barreira de qualidade do repositório.

## Em uma frase

Git hooks conectam eventos do Git a scripts de validação ou automação.

## O que precisa saber

Hooks locais podem rodar lint, testes ou formatação; hooks do lado do servidor podem impor políticas de recebimento. Como alguns não são versionados automaticamente, a equipe precisa documentar instalação e manter validações no [[pipeline-ci-cd]]. Segurança exige tratar scripts como código executável confiável.

## Erros comuns

- Depender de hook local que não está instalado para toda a equipe.
- Colocar tarefas lentas e opacas no commit.
- Executar script não revisado com privilégios excessivos.

## Onde aparece

- `Git--para--iniciantes.pdf`, página 61.
- Relaciona-se a [[git]], [[pipeline-ci-cd]], [[devsecops]] e [[controle-de-versao]].

## Fontes

- `lake/programacao-front-end/Git--para--iniciantes.pdf`, página 61.
