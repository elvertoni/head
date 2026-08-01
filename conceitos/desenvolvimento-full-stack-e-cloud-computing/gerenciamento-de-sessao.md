---
conceito: Gerenciamento de sessão
slug: gerenciamento-de-sessao
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [session management]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Arquitetura e Programação/05 - Aula 5 - Gerenciamento de Sessão e Controle de Cache - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Gerenciamento de sessão mantém contexto associado a interações de uma pessoa ou cliente ao longo de várias requisições. Como HTTP é stateless, a aplicação usa cookies, tokens ou armazenamento no servidor para reconhecer e proteger esse contexto.

## Em uma frase

Sessão conecta requisições relacionadas sem transformar HTTP em um protocolo stateful.

## O que precisa saber

[[cookies]] podem carregar um identificador; o estado real pode permanecer no servidor. Sessões exigem expiração, rotação, proteção contra fixação e associação com [[autenticacao]] e autorização. Cache e sessão respondem a problemas diferentes.

## Erros comuns

- Armazenar dados sensíveis diretamente no cookie.
- Não invalidar sessão após logout ou mudança de credencial.
- Confundir cache público com estado privado de sessão.

## Onde aparece

- Aulas 5–8 — Gerenciamento de Sessão e Controle de Cache.
- Conecta [[cookies]], [[http]], autenticação e cache HTTP.

## Fontes

- Aula 5, páginas 1–5 dos slides: estado, sessões e HTTP stateless.
