---
conceito: Replication Controller do Kubernetes
slug: replication-controller-kubernetes
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [ReplicationController]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo III - Cloud Computing/Desenvolvimento Web/11 - Aula 11 - Arquitetando Aplicações para Kubernetes - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Replication Controller é um controlador do Kubernetes que mantém o número desejado de réplicas de Pods, criando ou removendo instâncias quando o estado observado diverge. Em projetos atuais, ReplicaSet e Deployment costumam assumir essa função.

## Em uma frase

Replication Controller mantém a quantidade declarada de Pods em execução.

## O que precisa saber

Seletores, réplicas e estado desejado orientam a reconciliação. [[replicaset]] e [[deployment]] oferecem abstrações mais atuais para evolução e atualização.

## Erros comuns

- Confundir réplica com cópia de dados persistentes.
- Alterar Pod manualmente e esperar permanência.
- Usar controlador sem definir seleção correta.

## Onde aparece

- Desenvolvimento Web, Aula 11, página 3; Aula 12, página 3.
- Relaciona-se a [[replicaset]], [[deployment]], [[pod]] e [[estado-desejado-kubernetes]].

## Fontes

- Aula 11, página 3, e Aula 12, página 3 dos slides: Replication Controller.
