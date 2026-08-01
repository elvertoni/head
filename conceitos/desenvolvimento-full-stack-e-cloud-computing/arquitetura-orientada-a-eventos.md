---
conceito: Arquitetura orientada a eventos
slug: arquitetura-orientada-a-eventos
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [event-driven architecture, EDA]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Frameworks e Aplicações/16 - Aula 16 - Uso de MVC como Padrão de Projeto - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Arquitetura orientada a eventos organiza componentes que publicam e reagem a mudanças ou fatos por mensagens. O produtor não precisa conhecer todos os consumidores, favorecendo desacoplamento e processamento assíncrono.

## Em uma frase

Arquitetura orientada a eventos integra componentes por fatos publicados.

## O que precisa saber

Contratos, entrega, ordenação, duplicação e observabilidade são decisões centrais. O padrão amplia [[event-emitter]] para comunicação arquitetural e pode usar brokers.

## Erros comuns

- Confundir evento local com mensagem durável entre serviços.
- Assumir entrega exatamente uma vez sem mecanismo correspondente.
- Não projetar idempotência e rastreamento de causalidade.

## Onde aparece

- Frameworks e Aplicações, Aula 16, páginas 2–5.
- Relaciona-se a [[event-emitter]], [[programacao-assincrona]] e [[broker]].

## Fontes

- Aula 16, páginas 2–5 dos slides: arquitetura orientada a eventos.
