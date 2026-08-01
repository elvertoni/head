---
conceito: libuv
slug: libuv
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [biblioteca libuv]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Arquitetura e Programação/11 - Aula 11 - Fundamentos da Plataforma NodeJS III - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

libuv é a biblioteca multiplataforma que sustenta boa parte do I/O assíncrono e do loop de eventos do [[nodejs]]. Ela integra operações de sistema, rede e threads auxiliares ao runtime JavaScript.

## Em uma frase

libuv conecta o Node.js a I/O assíncrono multiplataforma.

## O que precisa saber

Operações não bloqueantes retornam ao fluxo enquanto o sistema trabalha; callbacks são encaminhados ao [[event-loop]] quando há resultado. Nem todo trabalho pesado deixa de consumir recursos do processo.

## Erros comuns

- Achar que todo código Node.js é automaticamente não bloqueante.
- Fazer processamento CPU-intensivo no thread principal.
- Confundir libuv com o interpretador JavaScript.

## Onde aparece

- Arquitetura e Programação, Aula 11, páginas 2–4.
- Relaciona-se a [[nodejs]], [[event-loop]] e [[programacao-assincrona]].

## Fontes

- Aula 11, páginas 2–4 dos slides: plataforma NodeJS e libuv.
