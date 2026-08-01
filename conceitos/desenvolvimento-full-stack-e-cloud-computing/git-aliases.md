---
conceito: Git aliases
slug: git-aliases
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [aliases do Git]
status: rascunho
fontes:
  - "lake/programacao-front-end/Git--para--iniciantes.pdf"
aulas: []
atualizado_em: 2026-08-01
---

Git aliases são atalhos configuráveis que associam um nome curto a um comando ou sequência de comandos do Git. Eles reduzem repetição no ambiente de uma pessoa, mas não devem esconder efeitos importantes em scripts compartilhados ou tornar procedimentos da equipe dependentes de configuração local.

## Em uma frase

Git aliases encurtam comandos repetidos sem alterar o modelo de histórico do Git.

## O que precisa saber

Aliases são configuração de interface, não novos comandos portáveis do projeto. Para automação compartilhada, prefira scripts versionados e documentação explícita. Um alias deve ter nome claro, evitar efeitos destrutivos inesperados e ser auditável por quem o utiliza.

## Erros comuns

- Criar alias com o mesmo nome de comando conhecido e mudar seu significado.
- Esconder operações destrutivas atrás de um nome inofensivo.
- Documentar um fluxo usando alias que só existe na máquina de uma pessoa.

## Onde aparece

- `Git--para--iniciantes.pdf`, páginas 61–62.
- Relaciona-se a [[git]], [[controle-de-versao]] e [[pipeline-ci-cd]].

## Fontes

- `lake/programacao-front-end/Git--para--iniciantes.pdf`, páginas 61–62.
