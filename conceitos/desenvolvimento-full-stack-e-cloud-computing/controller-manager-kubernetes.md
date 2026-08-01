---
conceito: Controller Manager do Kubernetes
slug: controller-manager-kubernetes
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [kube-controller-manager]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo III - Cloud Computing/Desenvolvimento Web/12 - Aula 12 - Arquitetando Aplicações para Kubernetes II - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Controller Manager reúne controladores que observam recursos do cluster e atuam para aproximar o estado atual do [[estado-desejado-kubernetes]]. Ele participa do control plane.

## Em uma frase

Controller Manager reconcilia recursos Kubernetes com o estado declarado.

## O que precisa saber

Controladores especializados tratam Nodes, réplicas, Jobs e outros recursos. A reconciliação é contínua e depende de API, permissões e observabilidade.

## Erros comuns

- Tratar declaração como execução instantânea.
- Ignorar ciclos de reconciliação e eventos concorrentes.
- Dar permissões amplas aos controladores.

## Onde aparece

- Desenvolvimento Web, Aula 12, página 3; Aula 13, página 5.
- Relaciona-se a [[control-plane]], [[kubernetes]], [[deployment]] e [[estado-desejado-kubernetes]].

## Fontes

- Aula 12, página 3, e Aula 13, página 5 dos slides: Controller Manager.
