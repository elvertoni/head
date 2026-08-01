---
conceito: Implantação contínua
slug: implantacao-continua
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [continuous deployment]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo III - Cloud Computing/Cultura DevOps e Integração Contínua/13 - Aula 13 - Pipeline de CI - CD - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Implantação contínua automatiza a promoção de mudanças aprovadas para ambientes de produção quando os critérios do pipeline são satisfeitos. Ela reduz espera manual, mas eleva a importância de testes, observabilidade e recuperação.

## Em uma frase

Implantação contínua entrega automaticamente mudanças que passaram pelos critérios definidos.

## O que precisa saber

É uma etapa posterior à [[integracao-continua]] e à [[entrega-continua]]. O fluxo precisa tratar feature flags, migrações, rollback, segurança e impacto progressivo; automação rápida não corrige critérios ruins.

## Erros comuns

- Implantar sem testes confiáveis ou plano de reversão.
- Confundir deploy com ativação de funcionalidade.
- Ignorar métricas pós-implantação.

## Onde aparece

- Aulas 4–6 e 13–15 — Cultura DevOps e Pipeline de CI/CD.
- Conecta [[entrega-continua]], [[pipeline-ci-cd]], [[devops]] e [[monitoramento]].

## Fontes

- Aula 13, páginas 2–5 dos slides: pipeline de CI/CD.
