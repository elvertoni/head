---
conceito: Horizontal Pod Autoscaler
slug: horizontal-pod-autoscaler
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: entidade
aka: [HPA]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo III - Cloud Computing/Desenvolvimento Web/13 - Aula 13 - Arquitetando Aplicações para Kubernetes III - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Horizontal Pod Autoscaler ajusta o número de réplicas de um workload conforme métricas e limites configurados.

## Em uma frase

HPA escala horizontalmente Pods a partir de sinais de carga.

## O que precisa saber

Métricas, janela de estabilização, limites e capacidade do cluster determinam o resultado. HPA pode usar CPU, memória ou métricas customizadas; [[escalonamento]] não é automático sem sinais confiáveis.

## Erros comuns

- Escalar por métrica que não representa saturação.
- Criar oscilação por limiares e janelas mal calibrados.

## Onde aparece

- Aulas 13–15 — Deployment e aplicações.

## Fontes

- Aula 13, páginas 2–5 dos slides: HPA e autoscaling.
