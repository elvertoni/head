---
conceito: Mock server
slug: mock-server
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [servidor simulado]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Frameworks e Aplicações/11 - Aula 11 - Ferramentas para Testar Back - End III - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Mock server é um servidor simulado que responde com contratos e dados controlados para testar consumidores ou fluxos sem depender do serviço real. Ele torna cenários de erro e ausência reproduzíveis.

## Em uma frase

Mock server simula uma API para testar integrações de forma controlada.

## O que precisa saber

Respostas simuladas devem acompanhar o contrato real e ter cenários explícitos. O mock não prova disponibilidade, latência ou comportamento do serviço de produção.

## Erros comuns

- Deixar o mock divergir do contrato real.
- Simular apenas o caminho feliz.
- Usar mock para esconder uma integração que nunca foi testada.

## Onde aparece

- Frameworks e Aplicações, Aula 11, página 2.
- Relaciona-se a [[teste-de-api]], [[testes-de-integracao]] e [[openapi]].

## Fontes

- Aula 11, página 2 dos slides: mock server e testes de backend.
