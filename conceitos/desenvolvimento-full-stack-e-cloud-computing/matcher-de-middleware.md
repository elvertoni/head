---
conceito: Matcher de middleware
slug: matcher-de-middleware
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [middleware matcher]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Frameworks, Programação e Estratégias/20 - Aula 20 - Criando Middlewares II - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Matcher de middleware define quais caminhos ou padrões devem passar por uma função intermediária antes de chegar ao destino.

## Em uma frase

Matcher limita o alcance de um middleware por padrão de rota.

## O que precisa saber

Padrões precisam ser testados contra caminhos públicos, internos e dinâmicos. [[middleware]], [[roteamento]] e [[protecao-de-rotas]] formam uma cadeia que deve ser auditável.

## Erros comuns

- Deixar rota sensível fora do matcher por engano.
- Criar matcher amplo que degrada todos os assets e endpoints.

## Onde aparece

- Aula 20 — Middlewares.

## Fontes

- Aula 20, páginas 4–7 dos slides: matcher e seleção de rotas.
