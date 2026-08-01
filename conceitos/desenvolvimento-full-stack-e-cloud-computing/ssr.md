---
conceito: Server-side rendering
slug: ssr
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [SSR, renderização no servidor]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Frameworks, Programação e Estratégias/10 - Aula 10 - Modos de Renderização SSG, SSR, ISR e CSR I - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Server-side rendering gera HTML no servidor para uma requisição ou conjunto de dados antes de enviá-lo ao cliente. A estratégia pode melhorar tempo até conteúdo e SEO, mas adiciona custo, dependência de dados e complexidade de cache.

## Em uma frase

SSR renderiza uma página no servidor antes de entregá-la ao navegador.

## O que precisa saber

SSR é uma estratégia do [[nextjs]], diferente de [[ssg]], [[isr]] e renderização no cliente. A decisão depende de frescor, interatividade, latência, privacidade e custo; HTML inicial não elimina JavaScript posterior.

## Erros comuns

- Fazer todas as páginas SSR sem medir necessidade.
- Expor dados privados no HTML ou cache.
- Ignorar hidratação e diferença entre ambiente servidor e cliente.

## Onde aparece

- Aulas 10–12 — Modos de Renderização SSG, SSR, ISR e CSR.
- Conecta [[nextjs]], [[ssg]], [[isr]] e React.

## Fontes

- Aula 10, páginas 1–4 dos slides: modos de renderização.
