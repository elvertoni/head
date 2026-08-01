---
conceito: Docker Engine
slug: docker-engine
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: entidade
aka: [motor Docker]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo III - Cloud Computing/Desenvolvimento Web/02 - Aula 2 - Docker II - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Docker Engine é o conjunto de componentes que constrói imagens e cria, executa e gerencia containers Docker.

## Em uma frase

Docker Engine fornece o runtime e a API local para operar containers.

## O que precisa saber

O cliente conversa com um daemon ou runtime; volumes, redes e imagens são recursos distintos. Em produção, [[kubernetes]] pode coordenar múltiplos nós.

## Erros comuns

- Expor o socket do daemon sem proteção.
- Assumir que um engine local resolve operação distribuída.

## Onde aparece

- Aulas 1–7 — Docker.

## Fontes

- Aula 2, páginas 2–10 dos slides: componentes Docker.
