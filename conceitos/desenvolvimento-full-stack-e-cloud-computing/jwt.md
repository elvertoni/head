---
conceito: JWT
slug: jwt
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [JSON Web Token]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Frameworks e Aplicações/31 - Aula 31 - Mecanismo de Segurança_ Cors, Autenticação e Autorização IV - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

JWT é um formato compacto de token que transporta claims assinadas entre partes. A assinatura permite verificar integridade e origem conforme a chave, mas não torna o conteúdo secreto nem substitui expiração, revogação e autorização.

## Em uma frase

JWT transporta claims verificáveis; não é, sozinho, uma política de segurança.

## O que precisa saber

JWT pode participar de [[autenticacao]] e [[autorizacao]], em cookies ou cabeçalhos conforme a arquitetura. Segredos, algoritmo, audiência, emissor, expiração e armazenamento precisam ser definidos. Um token roubado pode ser usado até expirar ou ser revogado.

## Erros comuns

- Armazenar segredo ou senha no payload esperando confidencialidade.
- Aceitar qualquer algoritmo, emissor ou audiência.
- Usar token longo sem rotação, expiração ou revogação.

## Onde aparece

- Aula 31 — Mecanismo de Segurança: CORS, Autenticação e Autorização.
- Conecta [[autenticacao]], [[autorizacao]], [[cookies]] e [[api]].

## Fontes

- Aula 31, páginas 1–7 dos slides: JWT, autenticação e autorização.
