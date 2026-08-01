---
conceito: Webhook
slug: webhook
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [gancho Web]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Frameworks e Aplicações/39 - Aula 39 - Novas Abordagens Arquiteturiais de APIs IV - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Webhook é uma notificação HTTP enviada a uma URL de consumidor quando um evento ocorre. Ele permite integração orientada a eventos sem que o consumidor consulte continuamente a origem.

## Em uma frase

Webhook entrega um evento a um endpoint escolhido pelo consumidor.

## O que precisa saber

Assinatura, autenticação, retries, idempotência e replay seguro são essenciais. O receptor deve responder rápido e processar de modo confiável usando [[api]] e [[arquitetura-orientada-a-eventos]].

## Erros comuns

- Confiar na URL sem verificar assinatura e origem.
- Não deduplicar reenvios.
- Fazer trabalho demorado antes de confirmar recebimento.

## Onde aparece

- Frameworks e Aplicações, Aula 39, páginas 1–6.
- Relaciona-se a [[api]], [[event-emitter]], [[idempotencia-http]] e [[websocket]].

## Fontes

- Aula 39, páginas 1–6 dos slides: webhooks e eventos de API.
