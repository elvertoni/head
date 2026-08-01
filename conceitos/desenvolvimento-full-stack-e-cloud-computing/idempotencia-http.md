---
conceito: Idempotência HTTP
slug: idempotencia-http
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [idempotência de método HTTP]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Desafio_ Desenvolvimento Front - End/01 - Aula 1 - Hands on_ Desenvolvimento Front - End - Contextualização - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Idempotência HTTP é a propriedade de uma operação produzir o mesmo efeito pretendido quando repetida com a mesma requisição, ainda que cada resposta possa variar. Ela é importante para retries e integrações confiáveis.

## Em uma frase

Operação idempotente tolera repetição sem acumular o mesmo efeito.

## O que precisa saber

GET, PUT e DELETE têm semânticas idempotentes no modelo HTTP, mas a implementação deve respeitar isso. POST pode exigir chave de idempotência de negócio, como em [[webhook]].

## Erros comuns

- Confundir idempotência com operação sem efeito.
- Repetir POST sem proteger criação duplicada.
- Ignorar concorrência e efeitos externos não idempotentes.

## Onde aparece

- Desafio Desenvolvimento Front-End, Aula 1, página 5.
- Relaciona-se a [[http]], [[api-rest]], [[codigos-de-status-http]] e [[webhook]].

## Fontes

- Aula 1, página 5 dos slides: semântica e repetição de requisições.
