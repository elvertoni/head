---
conceito: Broker
slug: broker
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [padrão broker]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Frameworks e Aplicações/16 - Aula 16 - Uso de MVC como Padrão de Projeto - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Broker é um intermediário que coordena comunicação, localização ou invocação entre componentes distribuídos. Ele reduz acoplamento direto, mas introduz uma dependência central de descoberta e mediação.

## Em uma frase

Broker intermedeia chamadas e comunicação entre componentes.

## O que precisa saber

Registro, roteamento, serialização, falhas e segurança fazem parte do desenho. O padrão aparece em sistemas distribuídos e se relaciona a [[arquitetura-de-microservicos]] e [[web-services]].

## Erros comuns

- Tratar broker como solução automática para latência e disponibilidade.
- Esconder contratos e falhas remotas atrás de chamadas parecidas com locais.
- Criar ponto único de falha sem redundância.

## Onde aparece

- Frameworks e Aplicações, Aula 16, páginas 2–4.
- Relaciona-se a [[arquitetura-de-microservicos]], [[web-services]] e [[api]].

## Fontes

- Aula 16, páginas 2–4 dos slides: padrão broker.
