---
conceito: Flux
slug: flux
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [arquitetura Flux]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Frameworks e Aplicações/17 - Aula 17 - Uso de MVC como Padrão de Projeto II - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Flux é um modelo de fluxo unidirecional para organizar estado de interfaces: ações são despachadas, uma lógica de atualização produz novo estado e a visão reage a ele.

## Em uma frase

Flux mantém estado de UI seguindo um fluxo explícito e unidirecional.

## O que precisa saber

O modelo torna transições rastreáveis e reduz atualizações arbitrárias. Ele se relaciona a [[state]], [[use-reducer]] e [[use-context]], mas pode ser excessivo para estado local simples.

## Erros comuns

- Criar store global para todo estado da aplicação.
- Mutar estado diretamente e perder rastreabilidade.
- Confundir fluxo unidirecional com ausência de efeitos assíncronos.

## Onde aparece

- Frameworks e Aplicações, Aula 17, página 2.
- Relaciona-se a [[state]], [[use-reducer]] e [[use-context]].

## Fontes

- Aula 17, página 2 dos slides: Flux e gerenciamento de estado.
