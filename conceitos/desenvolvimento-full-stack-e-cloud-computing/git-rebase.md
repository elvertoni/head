---
conceito: Git rebase
slug: git-rebase
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [rebase]
status: rascunho
fontes:
  - "lake/programacao-front-end/Git--para--iniciantes.pdf"
aulas: []
atualizado_em: 2026-08-01
---

Git rebase reaplica commits de uma branch sobre uma nova base, produzindo uma linha de histórico mais linear ao reescrever seus identificadores. Ele pode atualizar uma branch local antes da integração, mas exige cuidado porque altera o histórico que outras pessoas podem já ter compartilhado.

## Em uma frase

Rebase reaplica commits sobre outra base e reescreve a história resultante.

## O que precisa saber

O rebase pode revelar conflitos um a um e exigir resolução, continuação ou aborto. Não deve reescrever a branch pública sem acordo; depois de publicar histórico alterado, o push pode exigir força e causar perda de contexto. [[git]] registra o resultado, não a intenção original automaticamente.

## Erros comuns

- Fazer rebase de commits compartilhados sem coordenação.
- Confundir rebase com merge e esquecer que o histórico muda.
- Resolver conflitos sem testar a sequência reaplicada.

## Onde aparece

- `Git--para--iniciantes.pdf`, páginas 59–60.
- Relaciona-se a [[git]], [[controle-de-versao]], [[conflito-de-merge]] e [[github-flow]].

## Fontes

- `lake/programacao-front-end/Git--para--iniciantes.pdf`, páginas 59–60.
