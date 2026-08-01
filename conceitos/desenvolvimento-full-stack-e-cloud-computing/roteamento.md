---
conceito: Roteamento
slug: roteamento
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [routing]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Frameworks e Aplicações/07 - Aula 7 - Roteamento_Endpoints III - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Roteamento é o mecanismo que associa uma requisição, caminho e método a um handler ou componente responsável por processá-la. Ele organiza a superfície de uma aplicação e define como recursos e operações são encontrados.

## Em uma frase

Roteamento encaminha uma requisição para a lógica que atende seu contrato.

## O que precisa saber

Em [[expressjs]], rotas podem ser compostas por routers e middleware; em [[api-rest]], método e recurso formam parte do contrato. Rotas precisam de validação, autenticação, tratamento de erro e ordem previsível.

## Erros comuns

- Criar rotas ambíguas ou dependentes de ordem acidental.
- Colocar regra de negócio inteira no handler.
- Expor rota interna sem contrato ou autorização.

## Onde aparece

- Aulas 5–8 — Roteamento e Endpoints.
- Conecta [[expressjs]], [[endpoint]], [[api]], [[api-rest]] e middleware.

## Fontes

- Aula 7, páginas 1–6 dos slides: Router, middleware e endpoints.
