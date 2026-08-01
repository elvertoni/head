---
conceito: Call stack
slug: call-stack
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [pilha de chamadas]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Arquitetura e Programação/15 - Aula 15 - Call Stack e Evento Loop I - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Call stack é a estrutura LIFO que registra funções ativas durante a execução de JavaScript. Cada chamada cria um quadro; quando termina, o quadro é removido, e uma pilha excessiva pode produzir stack overflow.

## Em uma frase

Call stack acompanha a sequência de chamadas ativas de uma execução.

## O que precisa saber

No Node.js, o [[event-loop]] coordena tarefas e a [[programacao-assincrona]] evita esperar I/O de modo bloqueante. Funções recursivas e chamadas longas ocupam a pilha; compreender a ordem ajuda a depurar callbacks e promises.

## Erros comuns

- Confundir call stack com fila de eventos.
- Bloquear a pilha com trabalho síncrono pesado.
- Ignorar a ordem LIFO ao ler rastreamentos de erro.

## Onde aparece

- Aulas 15–18 — Call Stack, callbacks, Event Loop e Promises.
- Conecta [[nodejs]], [[event-loop]] e [[programacao-assincrona]].

## Fontes

- Aula 15, páginas 1–4 dos slides: call stack e ordem LIFO.
