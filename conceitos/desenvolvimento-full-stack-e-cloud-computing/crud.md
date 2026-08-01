---
conceito: CRUD
slug: crud
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [Create Read Update Delete]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Frameworks e Aplicações/20 - Aula 20 - Desenvolvimento de Funcionalidades Crud - Create e List - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

CRUD é o conjunto de operações Create, Read, Update e Delete usado para criar, consultar, alterar e remover recursos ou dados. Ele é uma lente de comportamento de uma aplicação, não uma arquitetura completa: cada operação ainda precisa de contrato, validação, autorização, persistência e tratamento de falhas.

## Em uma frase

CRUD organiza as operações básicas de ciclo de vida de um recurso.

## O que precisa saber

Em uma API, as operações podem ser expostas por [[metodos-http]] e [[api-rest]] e implementadas por um [[data-access-object]], ORM ou serviço. O modelo deve considerar idempotência, concorrência, validação e regras de negócio, não apenas mapear quatro endpoints mecanicamente.

## Erros comuns

- Expor CRUD direto e ignorar autorização ou regras do domínio.
- Tratar exclusão como sempre reversível.
- Misturar nomes, efeitos e códigos HTTP sem contrato consistente.

## Onde aparece

- Frameworks e Aplicações, Aula 20, páginas 1–4.
- Relaciona-se a [[data-access-object]], [[sequelize]], [[api-rest]] e [[metodos-http]].

## Fontes

- Frameworks e Aplicações, Aula 20, slides sobre operações de recursos.
