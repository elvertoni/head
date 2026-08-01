---
conceito: GitHub Flow
slug: github-flow
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [fluxo baseado em pull request]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo III - Cloud Computing/Cultura DevOps e Integração Contínua/09 - Aula 9 - Controle de Versão III - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

GitHub Flow é um fluxo leve de desenvolvimento baseado em branch curta, pull request, revisão, integração na branch principal e implantação frequente. Ele reduz cerimônia e favorece entrega contínua, desde que a branch principal permaneça protegida e implantável.

## Em uma frase

GitHub Flow usa branches curtas e revisão para integrar mudanças continuamente.

## O que precisa saber

Uma mudança nasce em branch, passa por revisão e automação e só então entra na linha principal. A prática depende de testes confiáveis, observabilidade e capacidade de reverter; sem isso, integrar rápido apenas acelera falhas. Compare com [[gitflow]] conforme o contexto.

## Erros comuns

- Fazer merge sem revisão ou validação automática.
- Manter branches longas sob um nome de fluxo simples.
- Tratar pull request como burocracia sem feedback técnico.

## Onde aparece

- Cultura DevOps e Integração Contínua, Aula 9, página 5.
- Relaciona-se a [[git]], [[controle-de-versao]], [[integracao-continua]] e [[gitflow]].

## Fontes

- Cultura DevOps e Integração Contínua, Aula 9, slide sobre fluxo de branches curtas.
