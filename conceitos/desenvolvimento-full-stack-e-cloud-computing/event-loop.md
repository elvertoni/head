---
conceito: Event loop
slug: event-loop
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [laço de eventos]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Arquitetura e Programação/17 - Aula 17 - Call Stack e Evento Loop III - Apostila (Slides).pdf"
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Arquitetura e Programação/21 - Aula 21 - Programação Assíncrona III - Apostila (Slides).pdf"
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Arquitetura e Programação/22 - Aula 22 - Programação Assíncrona IV - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Event loop é o mecanismo que coordena a execução da pilha de chamadas e o processamento de filas de callbacks e tarefas assíncronas. Ele permite que o runtime continue atendendo eventos enquanto operações de I/O aguardam fora da pilha.

## Em uma frase

Event loop coordena pilha, filas e operações assíncronas em um runtime orientado a eventos.

## O que precisa saber

No [[nodejs]], callbacks, promises e APIs de I/O são agendados para execução conforme regras do runtime. O event loop não cria paralelismo ilimitado: trabalho síncrono longo bloqueia o processamento de outros eventos.

## Erros comuns

- Dizer que event loop torna CPU-bound automaticamente assíncrono.
- Ignorar ordem entre microtasks, timers e I/O.
- Criar callback que bloqueia por muito tempo.

## Onde aparece

- Aulas 15–18 — Call Stack e Event Loop.
- Conecta [[call-stack]], [[nodejs]], [[programacao-assincrona]] e callbacks.

## Fontes

- Aula 17, páginas 1–6 dos slides: callback queue, FIFO e Event Loop.
