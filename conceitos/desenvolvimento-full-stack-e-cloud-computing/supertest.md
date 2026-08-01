---
conceito: Supertest
slug: supertest
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: entidade
aka: [biblioteca Supertest]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Frameworks e Aplicações/09 - Aula 9 - Ferramentas para Testar Back - End - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Supertest é uma biblioteca usada para enviar requisições HTTP a servidores em testes JavaScript. Ela facilita verificar rotas, status, cabeçalhos e payloads de uma aplicação backend.

## Em uma frase

Supertest testa o contrato HTTP de um servidor JavaScript.

## O que precisa saber

Casos precisam cobrir autenticação, validação, erros e persistência conforme o escopo. A ferramenta apoia [[teste-de-api]] e [[testes-de-integracao]], mas não substitui testes de negócio.

## Erros comuns

- Testar somente status 200.
- Usar banco compartilhado e tornar resultados dependentes da ordem.
- Confundir endpoint acessível com fluxo completo validado.

## Onde aparece

- Frameworks e Aplicações, Aula 9, páginas 2 e 4–5.
- Relaciona-se a [[teste-de-api]], [[testes-de-integracao]] e [[jest]].

## Fontes

- Aula 9, páginas 2 e 4–5 dos slides: Supertest e APIs.
