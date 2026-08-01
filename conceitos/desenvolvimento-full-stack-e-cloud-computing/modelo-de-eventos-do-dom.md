---
conceito: Modelo de eventos do DOM
slug: modelo-de-eventos-do-dom
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [DOM event model]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/JavaScript e Aplicações Práticas/05 - Aula 5 - Imersão JavaScript - Coleções e Funções - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Modelo de eventos do DOM define como o navegador cria, distribui e entrega eventos de interação e mudança aos listeners. Ele conecta a árvore de documentos ao comportamento da interface.

## Em uma frase

O modelo de eventos entrega interações do documento ao código.

## O que precisa saber

Captura, alvo, propagação e cancelamento compõem o fluxo. [[delegacao-de-eventos]] e [[propagacao-de-eventos]] ajudam a controlar handlers sem registrar um por elemento.

## Erros comuns

- Adicionar listeners repetidos a cada renderização.
- Ignorar cancelamento e propagação quando necessário.
- Usar evento sem fornecer alternativa de teclado.

## Onde aparece

- JavaScript e Aplicações Práticas, Aula 5, páginas 2–3.
- Relaciona-se a [[manipulacao-do-dom]], [[propagacao-de-eventos]] e [[delegacao-de-eventos]].

## Fontes

- Aula 5, páginas 2–3 dos slides: eventos do DOM.
