---
conceito: Deployment Kubernetes
slug: deployment
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: entidade
aka: [Kubernetes Deployment]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo III - Cloud Computing/Desenvolvimento Web/13 - Aula 13 - Arquitetando Aplicações para Kubernetes III - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Deployment declara a versão e a quantidade desejadas de Pods e coordena atualizações e rollbacks por meio de ReplicaSets.

## Em uma frase

Deployment transforma uma declaração de aplicação em rollout controlado.

## O que precisa saber

Imagem, labels, réplicas, estratégia e probes definem o comportamento. [[replicaset]] mantém as réplicas, enquanto o Deployment gerencia versões.

## Erros comuns

- Atualizar tag mutável sem controlar a imagem.
- Confundir pod pronto com aplicação funcional.

## Onde aparece

- Aulas 13–15 — Deployment e aplicações.

## Fontes

- Aula 13, páginas 2–5 dos slides: deployments e estado desejado.
