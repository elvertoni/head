---
conceito: Conflito de merge
slug: conflito-de-merge
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [merge conflict]
status: rascunho
fontes:
  - "lake/programacao-front-end/Git--para--iniciantes.pdf"
aulas: [3]
atualizado_em: 2026-09-24
---

Conflito de merge ocorre quando o Git não consegue combinar automaticamente alterações concorrentes porque elas afetam a mesma região ou possuem histórico incompatível. A ferramenta marca o conflito; a decisão correta depende da intenção do código e deve ser validada antes do commit.

## Em uma frase

Conflito de merge exige decidir manualmente como combinar alterações concorrentes.

## O que precisa saber

Resolver conflito envolve ler os dois lados, consultar o contexto, editar o resultado e executar testes. [[gitflow]] e [[github-flow]] reduzem conflitos por estratégias diferentes, mas nenhum fluxo os elimina. O histórico deve registrar a decisão sem apagar trabalho válido.

## Erros comuns

- Aceitar automaticamente um lado sem entender a mudança.
- Remover marcadores e não executar testes ou revisão.
- Resolver conflito de texto sem verificar comportamento e dados.

## Onde aparece

- `Git--para--iniciantes.pdf`, páginas 36–37.
- Aula 3 — *Branches: testando uma ideia arriscada sem bagunçar o que já funciona* `aulas/programacao-front-end/controle-de-versao-git-github/03-branches-modernas-e-merge/canonica.md` — marcadores `<<<<<<<`/`=======`/`>>>>>>>` e resolução manual.
- Relaciona-se a [[git]], [[controle-de-versao]], [[gitflow]], [[github-flow]], [[branch]] e [[merge]].

## Fontes

- `lake/programacao-front-end/Git--para--iniciantes.pdf`, páginas 36–37.
