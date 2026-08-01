---
conceito: Callback queue
slug: callback-queue
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [fila de callbacks, task queue]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Arquitetura e Programação/17 - Aula 17 - Call Stack e Evento Loop III - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Callback queue é a fila na qual callbacks prontos aguardam uma oportunidade de execução quando a [[call-stack]] está livre. O [[event-loop]] coordena essa passagem no modelo assíncrono do JavaScript.

## Em uma frase

Callback queue aguarda callbacks até a pilha de chamadas poder executá-los.

## O que precisa saber

A fila não interrompe uma função que já está na pilha. O comportamento combinado com filas de microtarefas, timers e I/O afeta a ordem observada.

## Erros comuns

- Esperar preempção de uma função síncrona longa.
- Confundir fila de callbacks com a pilha de chamadas.
- Assumir ordem entre fontes assíncronas sem conhecer suas filas.

## Onde aparece

- Arquitetura e Programação, Aula 17, páginas 1–4.
- Relaciona-se a [[event-loop]], [[call-stack]] e [[programacao-assincrona]].

## Fontes

- Aula 17, páginas 1–4 dos slides: fila, pilha e event loop.
