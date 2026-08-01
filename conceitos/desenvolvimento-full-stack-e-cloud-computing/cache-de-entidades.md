---
conceito: Cache de entidades
slug: cache-de-entidades
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [cache de registros]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Arquitetura e Programação/29 - Aula 29 - Consumindo Dados de um Banco de Dados Relacional IV - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Cache de entidades guarda temporariamente representações de registros ou objetos para evitar leituras repetidas no banco. Ele reduz latência e carga quando a política de validade é adequada.

## Em uma frase

Cache de entidades acelera leituras repetidas de dados persistidos.

## O que precisa saber

Chave, TTL, invalidação e consistência definem o comportamento. [[redis]] é uma opção de armazenamento; cache não deve ultrapassar as regras de autorização nem se tornar fonte única sem estratégia.

## Erros comuns

- Servir dados obsoletos depois de uma escrita.
- Usar chave sem considerar identidade, tenant ou permissão.
- Fazer cache de resposta personalizada como se fosse pública.

## Onde aparece

- Arquitetura e Programação, Aula 29, páginas 1–5.
- Relaciona-se a [[redis]], [[cache-http]] e [[banco-de-dados-relacional]].

## Fontes

- Aula 29, páginas 1–5 dos slides: cache de dados relacionais.
