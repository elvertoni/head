---
conceito: Interceptação de rotas
slug: interceptacao-de-rotas
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [route interception]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Frameworks, Programação e Estratégias/20 - Aula 20 - Criando Middlewares II - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Interceptação de rotas permite executar lógica antes que uma requisição prossiga, como validar sessão, redirecionar ou acrescentar contexto.

## Em uma frase

Interceptar uma rota cria uma fronteira de decisão antes do handler final.

## O que precisa saber

O middleware deve ser rápido, previsível e seguro; redirecionamentos precisam evitar loops. [[matcher-de-middleware]] define onde a interceptação ocorre.

## Erros comuns

- Usar middleware como lugar para toda a regra de negócio.
- Redirecionar requisições de API como se fossem páginas.

## Onde aparece

- Aula 20 — Middlewares.

## Fontes

- Aula 20, páginas 2–7 dos slides: interceptação e middleware.
