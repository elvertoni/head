---
conceito: HTTP streaming
slug: http-streaming
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [streaming por HTTP]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Frameworks e Aplicações/40 - Aula 40 - Novas Abordagens Arquiteturiais de APIs V - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

HTTP streaming mantém uma resposta ou conexão aberta para entregar dados em partes ao cliente, em vez de esperar todo o conteúdo antes de enviar o primeiro byte. O padrão é útil para respostas grandes, eventos ou geração progressiva, mas exige controle de buffers, encerramento, timeout e reconexão.

## Em uma frase

HTTP streaming entrega uma resposta progressivamente por uma conexão HTTP mantida aberta.

## O que precisa saber

O servidor envia chunks conforme os dados ficam disponíveis e o cliente processa o fluxo. A estratégia é diferente de baixar um arquivo completo e pode coexistir com [[streams-nodejs]], [[http]] e [[websocket]], que têm semânticas distintas. Observabilidade e limites de conexão são parte do contrato.

## Erros comuns

- Manter conexões sem timeout, limite ou cancelamento.
- Supor que o cliente receberá cada chunk no mesmo momento em todos os proxies.
- Usar streaming quando uma resposta paginada seria mais simples.

## Onde aparece

- Frameworks e Aplicações, Aula 40, páginas 2–4.
- Relaciona-se a [[http]], [[streams-nodejs]], [[websocket]] e [[api]].

## Fontes

- Frameworks e Aplicações, Aula 40, slides sobre novas abordagens de APIs.
