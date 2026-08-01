---
conceito: Tolerância a falhas
slug: tolerancia-a-falhas
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [fault tolerance]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo III - Cloud Computing/Aplicações em Cloud Computing/09 - Aula 9 - Escalonamento, Balanceamento de Carga e Mecanismo de Segurança II - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Tolerância a falhas é a capacidade de continuar prestando serviço, ainda que componentes, rede ou dependências falhem.

## Em uma frase

Um sistema tolerante limita o impacto de falhas inevitáveis.

## O que precisa saber

Redundância, health checks, timeout, retry, circuit breaker e recuperação se relacionam a [[alta-disponibilidade]]. Tolerar uma falha não significa esconder todo erro do usuário.

## Erros comuns

- Criar réplicas sem testar a falha real.
- Fazer retries sincronizados e amplificar a pane.

## Onde aparece

- Aulas 8–10 — Escalonamento, balanceamento e segurança.

## Fontes

- Aula 9, páginas 2–6 dos slides: redundância e tolerância.
