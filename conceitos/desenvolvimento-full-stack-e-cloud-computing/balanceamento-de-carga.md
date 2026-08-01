---
conceito: Balanceamento de carga
slug: balanceamento-de-carga
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [load balancing]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo III - Cloud Computing/Aplicações em Cloud Computing/08 - Aula 8 - Escalonamento, Balanceamento de Carga e Mecanismo de Segurança - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Balanceamento de carga distribui requisições entre instâncias ou serviços para usar capacidade, reduzir concentração e aumentar disponibilidade.

## Em uma frase

Balancear distribui tráfego entre destinos capazes de atender.

## O que precisa saber

Algoritmos podem usar round-robin, peso, saúde ou afinidade. O balanceador trabalha junto com [[escalonamento]], [[alta-disponibilidade]] e gestão de sessão.

## Erros comuns

- Enviar tráfego para instância doente.
- Ignorar sessões, conexões persistentes e cache.

## Onde aparece

- Aulas 8–10 — Escalonamento, balanceamento e segurança.

## Fontes

- Aula 8, páginas 2–6 dos slides: balanceamento de carga.
