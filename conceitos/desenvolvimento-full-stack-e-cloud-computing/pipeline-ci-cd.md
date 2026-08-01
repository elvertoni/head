---
conceito: Pipeline CI/CD
slug: pipeline-ci-cd
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [pipeline de integração e entrega contínuas]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo III - Cloud Computing/Cultura DevOps e Integração Contínua/13 - Aula 13 - Pipeline de CI - CD - Apostila (Slides).pdf"
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo III - Cloud Computing/Cultura DevOps e Integração Contínua/22 - Aula 22 - Implementando um Pipeline de CI_CD - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Pipeline CI/CD é uma sequência automatizada de etapas que recebe uma mudança, executa verificações e produz ou promove artefatos entre ambientes. Ele transforma o fluxo de entrega em um processo repetível e observável.

## Em uma frase

Pipeline CI/CD automatiza verificações e promoções do software entre etapas.

## O que precisa saber

Um pipeline pode incluir checkout, build, testes, análise, empacotamento, segurança, aprovação e deploy. [[integracao-continua]], [[entrega-continua]] e [[implantacao-continua]] são práticas diferentes dentro do fluxo. O pipeline deve falhar de forma informativa.

## Erros comuns

- Criar pipeline longo sem feedback rápido ou diagnóstico.
- Colocar segredo em logs e variáveis sem proteção.
- Promover artefato diferente daquele testado.

## Onde aparece

- Aulas 13–15 — Pipeline de CI/CD.
- Conecta [[devops]], [[controle-de-versao]], [[integracao-continua]], [[entrega-continua]] e [[implantacao-continua]].

## Fontes

- Aula 13, páginas 2–5 dos slides: elementos e etapas de pipeline.
