---
conceito: Autorização
slug: autorizacao
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [authorization, controle de acesso]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Frameworks e Aplicações/28 - Aula 28 - Mecanismo de Segurança_ Cors, Autenticação e Autorização - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Autorização é o processo de decidir quais recursos e operações uma identidade autenticada pode acessar. Ela transforma políticas em verificações aplicadas ao contexto da requisição.

## Em uma frase

Autorização verifica o que uma identidade pode fazer.

## O que precisa saber

Autorização depende de [[autenticacao]], identidade, recurso, ação e contexto. Pode usar papéis, atributos ou políticas; [[middleware]] e APIs são pontos de aplicação, mas a política precisa permanecer compreensível e auditável.

## Erros comuns

- Considerar que estar autenticado implica poder fazer tudo.
- Confiar em papel enviado pelo cliente sem verificar no servidor.
- Esquecer autorização por objeto e permitir acesso horizontal indevido.

## Onde aparece

- Aulas 28–31 — Segurança, CORS, Autenticação e Autorização.
- Conecta [[autenticacao]], [[middleware]], [[api]], [[endpoint]] e segurança Web.

## Fontes

- Aula 28, páginas 1–6 dos slides: autenticação, autorização e mecanismos de segurança.
