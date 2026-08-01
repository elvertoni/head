---
conceito: Códigos de status HTTP
slug: codigos-de-status-http
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [HTTP status codes]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Desafio_ Desenvolvimento Front - End/01 - Aula 1 - Hands on_ Desenvolvimento Front - End - Contextualização - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Códigos de status HTTP comunicam o resultado semântico de uma requisição em classes de informação, sucesso, redirecionamento, erro do cliente ou erro do servidor. O código integra o contrato entre [[api]] e consumidor.

## Em uma frase

Status HTTP informa como o servidor interpretou a requisição.

## O que precisa saber

O consumidor deve tratar status e corpo de erro de modo coerente. Status não substitui validação de payload nem deve esconder falhas de autorização.

## Erros comuns

- Responder sempre 200 e colocar o erro apenas no JSON.
- Usar 404, 401 e 403 sem distinguir seus significados.
- Expor detalhes internos em respostas 5xx.

## Onde aparece

- Desafio Desenvolvimento Front-End, Aula 1, página 5.
- Relaciona-se a [[http]], [[api-rest]], [[idempotencia-http]] e [[teste-de-api]].

## Fontes

- Aula 1, página 5 dos slides: códigos de status HTTP.
