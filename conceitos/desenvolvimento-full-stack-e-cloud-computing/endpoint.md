---
conceito: Endpoint
slug: endpoint
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [ponto de extremidade de API]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Frameworks e Aplicações/05 - Aula 5 - Roteamento_Endpoints - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Endpoint é um ponto de entrada definido por uma API para receber uma operação, normalmente identificado por método e caminho. Ele faz parte do contrato, mas não descreve sozinho dados, autorização, erros ou regras da operação.

## Em uma frase

Endpoint combina um endereço e uma operação dentro do contrato de uma API.

## O que precisa saber

Em [[api-rest]], o endpoint pode representar um recurso acessado por [[http]]; [[roteamento]] encaminha a requisição para o handler. O contrato deve documentar entradas, saídas, status, autenticação e limites.

## Erros comuns

- Tratar endpoint como sinônimo de API inteira.
- Criar URL sem definir método, idempotência ou erros.
- Expor rota sem autenticação ou validação.

## Onde aparece

- Aulas 5–8 — Roteamento e Endpoints.
- Conecta [[expressjs]], [[roteamento]], [[api]], [[api-rest]] e [[http]].

## Fontes

- Aula 5, páginas 1–4 dos slides: rotas e endpoints.
