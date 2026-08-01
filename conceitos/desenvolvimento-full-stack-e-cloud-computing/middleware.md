---
conceito: Middleware
slug: middleware
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [camada intermediária]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Frameworks, Programação e Estratégias/19 - Aula 19 - Criando Middlewares I - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Middleware é uma função ou camada intermediária que observa, transforma, autoriza ou encaminha uma requisição antes ou depois do handler principal. Ele compõe preocupações transversais como logging, autenticação, cache e tratamento de erros.

## Em uma frase

Middleware intercepta o fluxo para aplicar uma responsabilidade antes de chegar ao handler.

## O que precisa saber

Em [[expressjs]] e [[nextjs]], middlewares têm ordem, escopo e contrato de execução. Eles não substituem [[autenticacao]] nem [[autorizacao]]: apenas oferecem um ponto para aplicar essas decisões. Fluxos de erro e continuação precisam ser explícitos.

## Erros comuns

- Esquecer de retornar, encerrar ou encaminhar o fluxo.
- Colocar lógica de negócio complexa em uma camada transversal.
- Executar middleware caro em rotas que não precisam dele.

## Onde aparece

- Aulas 19–21 — Criando Middlewares.
- Conecta [[expressjs]], [[nextjs]], [[roteamento]], [[autenticacao]] e [[autorizacao]].

## Fontes

- Aula 19, páginas 2–7 dos slides: middleware e interceptação de rotas.
