---
conceito: Node do Kubernetes
slug: node-kubernetes
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [Kubernetes node, nó de cluster]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo III - Cloud Computing/Desenvolvimento Web/10 - Aula 10 - Kubernetes III - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Node do Kubernetes é uma máquina de trabalho que fornece recursos para executar Pods em um cluster. Ele participa do plano de dados e é coordenado pelo control plane.

## Em uma frase

Node fornece capacidade de execução para Pods do cluster.

## O que precisa saber

CPU, memória, rede, kubelet e runtime influenciam a execução. [[scheduler-kubernetes]] escolhe o node conforme recursos, restrições e políticas.

## Erros comuns

- Confundir node com Pod ou Deployment.
- Dimensionar apenas CPU e ignorar memória e rede.
- Colocar todos os workloads em um único node.

## Onde aparece

- Desenvolvimento Web, Aula 10, páginas 5–6; Aula 11, página 3.
- Relaciona-se a [[kubernetes]], [[pod]], [[cluster-kubernetes]] e [[scheduler-kubernetes]].

## Fontes

- Aula 10, páginas 5–6, e Aula 11, página 3 dos slides: nodes Kubernetes.
