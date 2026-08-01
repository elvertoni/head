---
conceito: Autenticação federada
slug: autenticacao-federada
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [federated authentication]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo III - Cloud Computing/Desenvolvimento Web/26 - Aula 26 - Projeto Web 4 - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Autenticação federada permite que uma aplicação confie em um provedor externo de identidade para autenticar a pessoa e emitir uma afirmação ou token. Ela reduz senhas locais, mas transfere dependências e responsabilidades ao contrato de identidade.

## Em uma frase

Federação delega autenticação a um provedor de identidade confiável.

## O que precisa saber

Issuer, audience, redirect, escopos, expiração e revogação precisam ser validados. [[oauth]] ajuda a delegar autorização; autorização local ainda decide o que a pessoa pode fazer.

## Erros comuns

- Aceitar token de issuer ou audience incorretos.
- Confundir identidade autenticada com permissão no sistema.
- Não planejar indisponibilidade do provedor.

## Onde aparece

- Desenvolvimento Web, Aula 26, páginas 2–8.
- Relaciona-se a [[oauth]], [[autenticacao]], [[autorizacao]] e [[single-sign-on]].

## Fontes

- Aula 26, páginas 2–8 dos slides: autenticação federada.
