---
conceito: Alta disponibilidade
slug: alta-disponibilidade
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [high availability, HA]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo III - Cloud Computing/Estratégias de Cloud Computing/04 - Aula 4 - Modelos de Nuvem_ Público, Privado e Híbrido - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Alta disponibilidade é a capacidade de manter um serviço acessível durante falhas esperadas ou parciais, usando redundância, detecção e recuperação. Ela é uma propriedade medida por objetivos e acordos, não uma promessa de funcionamento contínuo.

## Em uma frase

Alta disponibilidade reduz o impacto de falhas por redundância e recuperação planejadas.

## O que precisa saber

Arquiteturas de [[computacao-em-nuvem]] usam zonas, réplicas, health checks e automação, mas cada componente pode criar um ponto único de falha. Alta disponibilidade não equivale a durabilidade, segurança ou zero downtime.

## Erros comuns

- Confundir múltiplas instâncias com um plano testado de recuperação.
- Ignorar dependências externas e operações manuais.
- Definir disponibilidade sem métricas, RTO ou RPO.

## Onde aparece

- Aulas 4–6 — Modelos de Nuvem.
- Conecta [[escalabilidade]], [[nuvem-publica]] e [[arquitetura-de-nuvem]].

## Fontes

- Aula 4, páginas 2–5 dos slides: características e benefícios da nuvem.
