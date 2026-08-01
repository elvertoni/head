---
conceito: Event emitter
slug: event-emitter
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [emissor de eventos]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Arquitetura e Programação/17 - Aula 17 - Call Stack e Evento Loop III - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Event emitter é o padrão usado no Node.js para publicar eventos e notificar listeners registrados. Ele desacopla quem produz um evento de quem reage a ele.

## Em uma frase

Event emitter distribui eventos para listeners interessados.

## O que precisa saber

Listeners são chamados quando o emissor publica um nome de evento. O padrão combina com I/O e [[event-loop]], mas não substitui uma fila durável nem garante processamento exatamente uma vez.

## Erros comuns

- Acumular listeners e provocar vazamento de memória.
- Não tratar o evento error.
- Confundir evento local do processo com mensagem persistida entre serviços.

## Onde aparece

- Arquitetura e Programação, Aula 17, página 5.
- Relaciona-se a [[nodejs]], [[event-loop]] e [[programacao-assincrona]].

## Fontes

- Aula 17, página 5 dos slides: emissão e tratamento de eventos.
