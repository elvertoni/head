---
conceito: Pod
slug: pod
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [Kubernetes Pod]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo III - Cloud Computing/Desenvolvimento Web/11 - Aula 11 - Arquitetando Aplicações para Kubernetes - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Pod é a menor unidade implantável do Kubernetes, agrupando um ou mais containers que compartilham rede e volumes.

## Em uma frase

Pod encapsula containers que precisam compartilhar um contexto de execução.

## O que precisa saber

Pods são efêmeros; [[replicaset]] e [[deployment]] cuidam de réplicas e atualização. A maioria das aplicações usa um container principal por pod.

## Erros comuns

- Tratar pod como servidor permanente.
- Colocar containers sem ciclo de vida relacionado no mesmo pod.

## Onde aparece

- Aulas 11–12 — Arquitetando aplicações para Kubernetes.

## Fontes

- Aula 11, páginas 2–6 dos slides: pods e arquitetura.
