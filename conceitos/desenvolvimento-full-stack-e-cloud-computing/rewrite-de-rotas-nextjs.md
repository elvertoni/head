---
conceito: Rewrite de rotas no Next.js
slug: rewrite-de-rotas-nextjs
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [URL rewrite Next.js]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Frameworks, Programação e Estratégias/21 - Aula 21 - Criando Middlewares III - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Rewrite de rotas no Next.js altera internamente o destino de uma requisição sem necessariamente mudar a URL exibida ao cliente. Ele pode encaminhar uma rota pública para outro recurso, esconder detalhes de backend ou adaptar caminhos, enquanto um redirect comunica uma nova URL ao navegador.

## Em uma frase

Rewrite encaminha uma requisição internamente sem exigir mudança visível na URL.

## O que precisa saber

A regra pode ser aplicada na configuração ou em middleware, conforme o caso. A separação entre URL pública e destino interno deve preservar autenticação, cache, observabilidade e semântica de erro. O recurso se relaciona a [[nextjs]], [[middleware]], [[rotas-de-api-nextjs]] e [[roteamento-dinamico]].

## Erros comuns

- Confundir rewrite silencioso com redirect visível.
- Criar ciclos ou regras que capturam mais rotas do que o previsto.
- Esconder destino sem registrar contexto suficiente para depuração.

## Onde aparece

- Frameworks, Programação e Estratégias, Aula 21, páginas 2–5.
- Relaciona-se a [[nextjs]], [[middleware]], [[rotas-de-api-nextjs]] e [[roteamento-dinamico]].

## Fontes

- Frameworks, Programação e Estratégias, Aula 21, slides sobre middleware e encaminhamento de rotas.
