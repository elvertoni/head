---
conceito: Scheduler do Kubernetes
slug: scheduler-kubernetes
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [kube-scheduler]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo III - Cloud Computing/Desenvolvimento Web/12 - Aula 12 - Arquitetando Aplicações para Kubernetes II - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Scheduler do Kubernetes escolhe um Node para cada Pod ainda não alocado, considerando recursos, afinidades, restrições e políticas. Ele decide posicionamento; não executa o processo diretamente.

## Em uma frase

Scheduler escolhe onde Pods devem ser executados no cluster.

## O que precisa saber

Capacidade, taints, tolerations, afinidade e prioridades influenciam a decisão. [[node-kubernetes]] precisa ter recursos e condições compatíveis.

## Erros comuns

- Confundir agendamento com execução ou autoscaling.
- Ignorar requests e limits de recursos.
- Criar restrições que tornam Pods impossíveis de alocar.

## Onde aparece

- Desenvolvimento Web, Aula 13, página 6.
- Relaciona-se a [[node-kubernetes]], [[pod]], [[cluster-kubernetes]] e [[control-plane]].

## Fontes

- Aula 13, página 6 dos slides: Scheduler Kubernetes.
