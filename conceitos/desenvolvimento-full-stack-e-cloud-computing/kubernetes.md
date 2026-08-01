---
conceito: Kubernetes
slug: kubernetes
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: entidade
aka: [K8s, orquestrador de containers]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo III - Cloud Computing/Estratégias de Cloud Computing/26 - Aula 26 - Docker e Kubernetes - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Kubernetes é uma plataforma de orquestração que agenda, configura, escala e recupera workloads containerizados em um cluster. Ela declara um estado desejado e usa controladores para aproximar o estado real desse objetivo.

## Em uma frase

Kubernetes coordena containers e serviços por configuração declarativa e controladores.

## O que precisa saber

O cluster administra workloads, rede, descoberta e atualização, mas a aplicação precisa ser observável e adequada a falhas distribuídas. Kubernetes estende [[conteinerizacao]] e pode apoiar [[escalabilidade]] e [[alta-disponibilidade]], sem garanti-las sozinho.

## Erros comuns

- Confundir cluster saudável com aplicação correta.
- Expor serviços e permissões sem limitar escopo.
- Criar autoscaling sem métricas e limites coerentes.

## Onde aparece

- Aulas 26–28 — Docker e Kubernetes.
- Conecta [[docker]], [[conteinerizacao]], [[escalabilidade]] e [[alta-disponibilidade]].

## Fontes

- Aula 26, páginas 2–5 dos slides: Docker, Kubernetes e orquestração.
