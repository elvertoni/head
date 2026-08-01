---
conceito: Busca de dados no servidor
slug: busca-de-dados-no-servidor
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [server-side data fetching]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Frameworks, Programação e Estratégias/07 - Aula 7 - Busca de Dados e Roteamento Dinâmico I - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Busca de dados no servidor obtém dados durante ou antes da renderização do servidor, reduzindo trabalho inicial no navegador e mantendo credenciais fora do cliente.

## Em uma frase

Buscar no servidor aproxima dados e renderização da aplicação protegida.

## O que precisa saber

Cache, revalidação, latência e tratamento de erro afetam [[ssr]]. A estratégia deve combinar com a frescor necessária e com o contrato da [[api]].

## Erros comuns

- Bloquear toda a página por uma dependência lenta sem fallback.
- Compartilhar segredo de backend no componente de cliente.

## Onde aparece

- Aulas 7–9 — Busca de dados e roteamento dinâmico.

## Fontes

- Aula 7, páginas 1–4 dos slides: busca de dados no servidor.
