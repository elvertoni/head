---
conceito: DCL
slug: dcl
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [Data Control Language, linguagem de controle de dados]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Modelagem de Banco de Dados/34 - Aula 34 - Modelo Físico de Dados III - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

DCL é a classificação de comandos SQL que controlam permissões e privilégios de acesso a objetos e dados. Ela ajuda a separar o que uma identidade pode consultar, alterar ou administrar.

## Em uma frase

DCL governa permissões sobre estruturas e operações do banco.

## O que precisa saber

Autorização deve seguir menor privilégio e necessidades do domínio. DCL complementa, mas não substitui autenticação, auditoria, segurança da aplicação e proteção de dados; seu comportamento depende do [[sgbd]].

## Erros comuns

- Dar privilégios administrativos para toda aplicação.
- Confundir usuário autenticado com usuário autorizado.
- Conceder acesso amplo e nunca revisar.

## Onde aparece

- Aula 34 — Modelo Físico de Dados III.
- É uma categoria de [[sql]] relacionada à segurança do [[sgbd]].

## Fontes

- Aula 34, slides: controle de acesso e privilégios SQL.
