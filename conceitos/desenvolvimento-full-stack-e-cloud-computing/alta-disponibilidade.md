---
conceito: Alta disponibilidade
slug: alta-disponibilidade
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [high availability, HA]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo III - Cloud Computing/Estratégias de Cloud Computing/04 - Aula 4 - Modelos de Nuvem_ Público, Privado e Híbrido - Apostila (Slides).pdf"
aulas: [1, 2, 5, 7, 9, 31]
atualizado_em: 2026-09-24
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

- Aula canônica 31 — `aulas/analise-e-projeto-de-sistemas/analise-de-requisitos/31-engenharia-reversa-de-app/canonica.md`.
- Aula 1 — *Blueprint · A.N.N Beauty* `aulas/tcc/blueprint-tcc/01-blueprint-a-n-n-beauty/canonica.md` — RNF04, disponibilidade de 99,9%.
- Aula 2 — *Blueprint · Alexandria* `aulas/tcc/blueprint-tcc/02-blueprint-alexandria/canonica.md` — RNF04, disponibilidade mínima de 95%.
- Aula 5 — *Blueprint · Gold Fit* `aulas/tcc/blueprint-tcc/05-blueprint-gold-fit/canonica.md` — RNF01, disponibilidade e modo offline.
- Aula 7 — *Blueprint · HobbyQuest* `aulas/tcc/blueprint-tcc/07-blueprint-hobbyquest/canonica.md` — RNF04, funcionamento estável durante testes e apresentação.
- Aula 9 — *Blueprint · ResumeTech* `aulas/tcc/blueprint-tcc/09-blueprint-resumetech/canonica.md` — RNF de disponibilidade para acesso a qualquer momento.

- Aulas 4–6 — Modelos de Nuvem.
- Conecta [[escalabilidade]], [[nuvem-publica]] e [[arquitetura-de-nuvem]].

## Fontes

- Aula 4, páginas 2–5 dos slides: características e benefícios da nuvem.
