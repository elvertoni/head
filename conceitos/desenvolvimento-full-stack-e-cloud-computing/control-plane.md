---
conceito: Control plane
slug: control-plane
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [plano de controle]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo III - Cloud Computing/Desenvolvimento Web/11 - Aula 11 - Arquitetando Aplicações para Kubernetes - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Control plane é o conjunto de componentes que expõe a API, armazena estado e decide como o cluster Kubernetes deve convergir para o estado desejado.

## Em uma frase

Plano de controle decide e coordena; nós de trabalho executam.

## O que precisa saber

Ele envolve [[api-server-kubernetes]], scheduler, controllers e [[etcd]]. Alta disponibilidade e segurança do plano de controle são críticas para o cluster.

## Erros comuns

- Tratar control plane como um único processo.
- Expor sua API sem autenticação e autorização fortes.

## Onde aparece

- Aulas 11–12 — Arquitetando aplicações para Kubernetes.

## Fontes

- Aula 11, páginas 2–6 dos slides: arquitetura Kubernetes.
