---
conceito: OAuth
slug: oauth
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [Open Authorization]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Frameworks, Programação e Estratégias/22 - Aula 22 - Autenticação e Segurança I - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

OAuth é um protocolo de delegação de autorização que permite a um cliente obter acesso limitado a recursos sem receber a senha do usuário.

## Em uma frase

OAuth delega acesso por tokens e escopos, não compartilha a senha.

## O que precisa saber

Fluxos, redirecionamento, state, PKCE, escopos e armazenamento seguro são essenciais. OAuth não é, sozinho, uma prova completa de identidade; [[autenticacao]] e autorização devem ser distinguidas.

## Erros comuns

- Usar fluxo inadequado para o tipo de cliente.
- Aceitar callback sem validar state ou redirect URI.

## Onde aparece

- Aulas 22–24 — Autenticação e segurança.

## Fontes

- Aula 22, página 4; Aula 23, páginas 2–3 dos slides: OAuth.
