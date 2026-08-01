---
conceito: etcd
slug: etcd
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: entidade
aka: [armazenamento do estado Kubernetes]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo III - Cloud Computing/Desenvolvimento Web/11 - Aula 11 - Arquitetando Aplicações para Kubernetes - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

etcd é o armazenamento distribuído de chave-valor usado pelo Kubernetes para persistir o estado do cluster.

## Em uma frase

etcd guarda o estado que permite ao control plane reconciliar o cluster.

## O que precisa saber

Backup, quorum, latência, criptografia e controle de acesso são essenciais. Perder ou corromper o estado compromete decisões do [[control-plane]].

## Erros comuns

- Operar etcd sem backup testado.
- Tratar consistência distribuída como detalhe de infraestrutura.

## Onde aparece

- Aulas 11–12 — Arquitetando aplicações para Kubernetes.

## Fontes

- Aula 11, páginas 2–6 dos slides: armazenamento do control plane.
