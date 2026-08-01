---
conceito: Dependência de conectividade
slug: dependencia-de-conectividade
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [network dependency]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo III - Cloud Computing/Aplicações em Cloud Computing/04 - Aula 4 - Soluções de Cloud Computing - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Dependência de conectividade é a necessidade de uma aplicação alcançar rede, provedor ou serviço remoto para funcionar plenamente.

## Em uma frase

Na nuvem, rede disponível e latência fazem parte do desenho da aplicação.

## O que precisa saber

Falhas de rede exigem timeout, retry, cache e degradação controlada. [[pwa]] e [[service-workers]] podem reduzir dependência em experiências Web, mas não eliminam o problema.

## Erros comuns

- Supor que a rede é estável ou gratuita.
- Repetir requisições sem limite e agravar a indisponibilidade.

## Onde aparece

- Aulas 4–7 — Soluções de Cloud Computing.

## Fontes

- Aula 4, páginas 2–6 dos slides: desafios de cloud e conectividade.
