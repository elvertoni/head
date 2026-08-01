---
conceito: Arquitetura de três esquemas
slug: arquitetura-de-tres-esquemas
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [arquitetura ANSI-SPARC]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Modelagem de Banco de Dados/19 - Aula 19 - Modelo Relacional II - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Arquitetura de três esquemas separa a visão externa das aplicações, o esquema conceitual do banco e o nível interno de armazenamento. A separação cria pontos de abstração e fundamenta a discussão sobre [[independencia-de-dados]].

## Em uma frase

Três esquemas separam visões, modelo global e armazenamento físico.

## O que precisa saber

O nível externo atende necessidades de usuários e aplicações; o conceitual descreve o banco como um todo; o interno trata implementação. A separação não elimina contratos: mudanças semânticas podem afetar todos os níveis. Relaciona-se a [[modelo-conceitual]], [[modelo-logico]] e [[modelo-fisico]].

## Erros comuns

- Confundir os três níveis com três cópias do mesmo banco.
- Supor que toda mudança física será invisível sem configuração.
- Usar visão externa como substituto de modelagem conceitual.

## Onde aparece

- Aula 19 — Modelo Relacional II.
- Conecta [[independencia-de-dados]], [[modelo-conceitual]], [[modelo-logico]] e [[modelo-fisico]].

## Fontes

- Aula 19, slides: níveis externo, conceitual e interno.
