---
conceito: API server Kubernetes
slug: api-server-kubernetes
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: entidade
aka: [kube-apiserver]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo III - Cloud Computing/Desenvolvimento Web/11 - Aula 11 - Arquitetando Aplicações para Kubernetes - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

API server Kubernetes é a porta de entrada do plano de controle para clientes, controllers e componentes que consultam ou alteram objetos do cluster.

## Em uma frase

API server centraliza o contrato de controle do cluster.

## O que precisa saber

Autenticação, autorização, admission e persistência em [[etcd]] fazem parte do fluxo. Toda mudança declarativa passa por esse contrato.

## Erros comuns

- Confundir API server com o processo da aplicação.
- Permitir privilégios amplos para clientes ou service accounts.

## Onde aparece

- Aulas 11–12 — Arquitetando aplicações para Kubernetes.

## Fontes

- Aula 11, páginas 2–6 dos slides: componentes do control plane.
