---
conceito: Service Kubernetes
slug: service-kubernetes
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: entidade
aka: [Kubernetes Service]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo III - Cloud Computing/Desenvolvimento Web/11 - Aula 11 - Arquitetando Aplicações para Kubernetes - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Service Kubernetes fornece um endereço e uma forma estável de encaminhar tráfego para Pods selecionados.

## Em uma frase

Service desacopla clientes da identidade efêmera dos Pods.

## O que precisa saber

Selectors, portas, tipos de exposição e DNS determinam o caminho do tráfego. [[balanceamento-de-carga]] e readiness ajudam a evitar destinos indisponíveis.

## Erros comuns

- Selecionar pods por label errada.
- Expor serviço externamente sem autenticação ou controle de rede.

## Onde aparece

- Aulas 11–12 — Arquitetando aplicações para Kubernetes.

## Fontes

- Aula 11, páginas 2–6 dos slides: services.
