---
conceito: Integração contínua
slug: integracao-continua
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [continuous integration, CI]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo III - Cloud Computing/Cultura DevOps e Integração Contínua/13 - Aula 13 - Pipeline de CI - CD - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Integração contínua é a prática de integrar mudanças pequenas frequentemente em uma linha principal, executando compilação, testes e verificações automatizadas. Ela reduz o tempo entre mudança e feedback.

## Em uma frase

Integração contínua detecta cedo problemas introduzidos por mudanças integradas.

## O que precisa saber

CI usa [[controle-de-versao]] e [[pipeline-ci-cd]] para tornar verificações repetíveis. Ela não exige que toda mudança chegue imediatamente à produção; [[entrega-continua]] e [[implantacao-continua]] tratam etapas posteriores.

## Erros comuns

- Ter pipeline que só compila e chamar isso de integração contínua.
- Ignorar testes instáveis e aceitar falsos positivos.
- Acumular branches longas e integrar raramente.

## Onde aparece

- Aulas 4–6 e 13–15 — Cultura DevOps e Pipeline de CI/CD.
- Conecta [[devops]], [[controle-de-versao]], [[entrega-continua]] e [[pipeline-ci-cd]].

## Fontes

- Aula 13, páginas 2–5 dos slides: pipeline de CI/CD.
