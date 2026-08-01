---
conceito: Axios
slug: axios
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [cliente HTTP Axios]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Projeto Front - End e Desenvolvimento Web/32 - Aula 32 - Consumindo APIs com React II - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Axios é uma biblioteca cliente para realizar requisições HTTP em aplicações JavaScript, com interceptors, transformação de dados e tratamento de respostas.

## Em uma frase

Axios encapsula chamadas HTTP para consumo de APIs no frontend e backend.

## O que precisa saber

Timeout, cancelamento, erros, autenticação e base URL precisam ser configurados. Interceptors não devem esconder falhas nem vazar [[jwt]] ou credenciais.

## Erros comuns

- Considerar qualquer resposta HTTP como sucesso.
- Repetir requisições sem cancelamento ou controle de concorrência.

## Onde aparece

- Aula 32 — Consumo de APIs com React.

## Fontes

- Aula 32, páginas 1–5 dos slides: Axios e consumo de APIs.
