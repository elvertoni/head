---
conceito: Cookies HTTP
slug: cookies
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [HTTP cookies]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Arquitetura e Programação/06 - Aula 6 - Gerenciamento de Sessão e Controle de Cache II - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Cookies HTTP são pequenos dados associados a um domínio que o navegador envia em requisições conforme regras de escopo, expiração e segurança. Eles podem identificar uma sessão, guardar preferências ou apoiar mecanismos de autenticação.

## Em uma frase

Cookie é um dado controlado pelo navegador e enviado ao servidor dentro de regras HTTP.

## O que precisa saber

Atributos como Secure, HttpOnly, SameSite, Domain e Path limitam riscos e escopo. Cookies participam de [[gerenciamento-de-sessao]], mas não devem carregar segredo desnecessário. Privacidade, consentimento e proteção contra CSRF precisam ser considerados.

## Erros comuns

- Guardar senha ou token de longa duração em cookie inseguro.
- Ignorar SameSite, Secure e HttpOnly.
- Presumir que cookie é invisível à pessoa usuária ou ao navegador.

## Onde aparece

- Aulas 5–8 — Gerenciamento de Sessão e Controle de Cache.
- Conecta [[gerenciamento-de-sessao]], [[http]] e autenticação.

## Fontes

- Aula 6, páginas 2–6 dos slides: cookies e sessões HTTP.
