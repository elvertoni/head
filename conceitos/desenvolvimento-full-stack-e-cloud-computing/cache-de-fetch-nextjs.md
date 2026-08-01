---
conceito: Cache de fetch no Next.js
slug: cache-de-fetch-nextjs
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [fetch cache do Next.js]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Frameworks, Programação e Estratégias/07 - Aula 7 - Busca de Dados e Roteamento Dinâmico I - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

O cache de fetch no Next.js estende a busca de dados para armazenar e revalidar respostas conforme opções da aplicação. Ele integra cache, renderização e atualização de dados no framework.

## Em uma frase

Fetch cache controla reuso e revalidação de dados buscados no Next.js.

## O que precisa saber

TTL, invalidação, conteúdo personalizado e consistência precisam ser explícitos. O mecanismo se relaciona a [[cache-http]], [[revalidacao-de-dados]] e [[busca-de-dados-no-servidor]].

## Erros comuns

- Cachear resposta dependente de usuário como se fosse pública.
- Esperar atualização imediata sem revalidação configurada.
- Confundir cache do fetch com cache HTTP de uma CDN.

## Onde aparece

- Frameworks, Programação e Estratégias, Aula 7, página 2.
- Relaciona-se a [[cache-http]], [[revalidacao-de-dados]] e [[nextjs]].

## Fontes

- Aula 7, página 2 dos slides: cache de fetch e revalidação.
