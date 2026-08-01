---
conceito: INNER JOIN
slug: inner-join
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [junção interna]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Linguagens e Aplicações de Banco de Dados/22 - Aula 22 - Junções II - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

INNER JOIN retorna apenas as combinações de linhas que satisfazem a condição de junção. É a forma SQL mais direta da [[juncao-relacional]] com correspondência obrigatória.

## Em uma frase

INNER JOIN mantém somente linhas relacionadas dos dois lados.

## O que precisa saber

A condição costuma ligar [[chave-primaria]] a [[chave-estrangeira]], mas pode usar outras expressões. O resultado pode multiplicar linhas quando a relação é um-para-muitos.

## Erros comuns

- Confundir ausência de correspondência com erro de consulta.
- Esquecer a condição e gerar [[produto-cartesiano-relacional]].
- Selecionar colunas sem qualificar nomes ambíguos.

## Onde aparece

- Linguagens e Aplicações de Banco de Dados, Aula 22, páginas 1–4.
- Relaciona-se a [[juncao-relacional]], [[left-join]] e [[right-join]].

## Fontes

- Aula 22, páginas 1–4 dos slides: junção interna.
