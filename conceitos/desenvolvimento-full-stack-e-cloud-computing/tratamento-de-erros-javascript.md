---
conceito: Tratamento de erros em JavaScript
slug: tratamento-de-erros-javascript
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [error handling JavaScript]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/JavaScript e Aplicações Práticas/03 - Aula 3 - Funções - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Tratamento de erros em JavaScript é o conjunto de práticas para detectar, propagar, classificar, registrar e apresentar falhas sem deixar o sistema em estado incoerente. Ele vale para código síncrono e assíncrono.

## Em uma frase

Tratar erro é tornar a falha observável e segura para cada camada.

## O que precisa saber

try/catch, throw, finally, rejeições de [[promises]] e respostas HTTP têm limites diferentes. O erro deve carregar contexto suficiente sem vazar segredo.

## Erros comuns

- Engolir exceção e continuar com estado inválido.
- Não aguardar ou observar rejeição de Promise.
- Mostrar stack trace e dados internos ao usuário.

## Onde aparece

- JavaScript e Aplicações Práticas, Aulas 3–4, páginas indicadas nos slides.
- Relaciona-se a [[promises]], [[fetch-api]], [[testes-unitarios]] e [[codigos-de-status-http]].

## Fontes

- Aula 3, páginas 1–7, e Aula 4, páginas 2–5 dos slides: erros JavaScript.
