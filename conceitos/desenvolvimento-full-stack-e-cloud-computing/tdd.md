---
conceito: Desenvolvimento orientado a testes
slug: tdd
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [Test-Driven Development]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo III - Cloud Computing/Cultura DevOps e Integração Contínua/25 - Aula 25 - Desenvolvimento Orientado a Testes (TDD) - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Desenvolvimento orientado a testes é um ciclo em que a pessoa escreve um teste que falha, implementa o mínimo para fazê-lo passar e refatora mantendo o comportamento. O teste guia design e feedback, mas não substitui testes de integração e aceitação.

## Em uma frase

TDD usa testes pequenos para orientar implementação e refatoração.

## O que precisa saber

O ciclo red-green-refactor favorece feedback rápido e interfaces menores. Ele pode compor [[integracao-continua]] e [[pipeline-ci-cd]], mas a pirâmide de testes precisa cobrir riscos além de unidades.

## Erros comuns

- Escrever testes acoplados à implementação e chamar isso de especificação.
- Só testar o caminho feliz.
- Confundir cobertura de linhas com confiança no comportamento.

## Onde aparece

- Aulas 25–28 — Desenvolvimento Orientado a Testes.
- Conecta [[integracao-continua]], [[pipeline-ci-cd]], testes unitários e [[devops]].

## Fontes

- Aula 25, páginas 2–5 dos slides: ciclo e princípios de TDD.
