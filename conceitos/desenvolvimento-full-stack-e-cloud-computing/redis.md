---
conceito: Redis
slug: redis
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [banco Redis]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Arquitetura e Programação/07 - Aula 7 - Gerenciamento de Sessão e Controle de Cache III - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Redis é um armazenamento de dados em memória usado para cache, sessões, filas e outras estruturas de baixa latência. Ele pode compartilhar estado entre instâncias de uma aplicação.

## Em uma frase

Redis oferece armazenamento em memória rápido para estado e cache.

## O que precisa saber

Expiração, persistência opcional, estruturas de dados e políticas de remoção determinam o comportamento. Pode apoiar [[stateful]], [[cache-http]] e [[cache-de-entidades]], mas não substitui automaticamente um banco durável.

## Erros comuns

- Tratar cache como fonte definitiva sem política de recuperação.
- Ignorar expiração, invalidação e limite de memória.
- Armazenar segredos sem controles de acesso e transporte.

## Onde aparece

- Arquitetura e Programação, Aulas 7–8.
- Relaciona-se a [[cache-http]], [[cache-de-entidades]], [[docker]] e [[gerenciamento-de-sessao]].

## Fontes

- Aula 7, páginas 2–4, e Aula 8, páginas 4–6: Redis em sessão e cache.
