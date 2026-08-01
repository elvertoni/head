---
conceito: Promises
slug: promises
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [promessas JavaScript, Promise]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Arquitetura e Programação/18 - Aula 18 - Call Stack e Evento Loop IV - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Promise é um objeto que representa a conclusão ou falha futura de uma operação assíncrona. Sua API permite encadear transformações e tratamento de erros sem expor diretamente a callback de conclusão.

## Em uma frase

Promise modela um resultado assíncrono que ainda será resolvido.

## O que precisa saber

Uma promise pode estar pendente, realizada ou rejeitada. then, catch e finally compõem fluxos; async/await oferece uma sintaxe de consumo, sem tornar a operação síncrona.

## Erros comuns

- Esquecer de retornar uma promise dentro do encadeamento.
- Não tratar rejeições.
- Confundir await com paralelismo automático.

## Onde aparece

- Arquitetura e Programação, Aula 18, páginas 1–4.
- Relaciona-se a [[programacao-assincrona]], [[event-loop]] e [[callback-queue]].

## Fontes

- Aula 18, páginas 1–4 dos slides: promises e execução assíncrona.
