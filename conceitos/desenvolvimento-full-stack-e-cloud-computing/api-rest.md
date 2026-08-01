---
conceito: API REST
slug: api-rest
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [API RESTful]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Arquitetura e Programação/33 - Aula 33 - Conceitos Sobre API REST (métodos e HTTP Codes) I - Apostila (Slides).pdf"
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Arquitetura e Programação/36 - Aula 36 - Conceitos Sobre API REST (métodos e HTTP Codes) IV - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

API REST é uma API Web que usa recursos, representações e convenções HTTP inspiradas no estilo [[rest]]. Ela define caminhos, métodos, payloads, status e regras para consumidores interagirem com um serviço.

## Em uma frase

API REST expõe recursos por um contrato HTTP orientado a representações.

## O que precisa saber

[[http]], [[json]], métodos e códigos de status formam a superfície técnica; autenticação, autorização, versionamento e documentação completam o contrato. Uma API REST pode ser bem ou mal projetada independentemente da ferramenta usada.

## Erros comuns

- Usar sempre 200 e esconder erros no corpo.
- Confundir endpoint com recurso e ignorar idempotência.
- Expor dados de banco sem contrato e autorização.

## Onde aparece

- Aulas 33–36 — Conceitos sobre API REST.
- Conecta [[rest]], [[api]], [[http]], [[json]] e endpoints.

## Fontes

- Aula 33, páginas 1–5 dos slides: arquitetura REST e métodos HTTP.
