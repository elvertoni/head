---
conceito: Cloud Functions
slug: cloud-functions
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [funções serverless]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo III - Cloud Computing/Aplicações em Cloud Computing/17 - Aula 17 - Projeto Web - Parte 1 - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Cloud Functions executa funções orientadas a eventos ou requisições sem que a equipe gerencie diretamente os servidores subjacentes.

## Em uma frase

Funções serverless delegam infraestrutura e cobram por execução e recursos consumidos.

## O que precisa saber

Cold start, tempo limite, idempotência, observabilidade e permissões são essenciais. O modelo complementa [[firebase]] e pode integrar dados e eventos.

## Erros comuns

- Assumir latência constante ou estado local persistente.
- Fazer função não idempotente reagir a evento duplicado.

## Onde aparece

- Aulas 17–31 — Projeto Web.

## Fontes

- Aula 17, páginas 2–5 dos slides: serviços Firebase.
