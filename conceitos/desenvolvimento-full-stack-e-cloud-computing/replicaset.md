---
conceito: ReplicaSet
slug: replicaset
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [Kubernetes ReplicaSet]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo III - Cloud Computing/Desenvolvimento Web/11 - Aula 11 - Arquitetando Aplicações para Kubernetes - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

ReplicaSet mantém um número desejado de Pods compatíveis por meio de seleção e reconciliação.

## Em uma frase

ReplicaSet mantém réplicas disponíveis de um pod.

## O que precisa saber

Normalmente é criado e gerenciado por [[deployment]], que também coordena versões. Labels e selectors precisam coincidir com cuidado.

## Erros comuns

- Editar ReplicaSet gerado por Deployment como se fosse a fonte principal.
- Usar selector amplo e capturar pods errados.

## Onde aparece

- Aulas 11–12 — Arquitetando aplicações para Kubernetes.

## Fontes

- Aula 11, páginas 2–6 dos slides: ReplicaSet.
