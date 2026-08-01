---
conceito: Incremental static regeneration
slug: isr
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [ISR, regeneração estática incremental]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Frameworks, Programação e Estratégias/10 - Aula 10 - Modos de Renderização SSG, SSR, ISR e CSR I - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Incremental static regeneration combina páginas estáticas com revalidação posterior para atualizar conteúdo sem reconstruir todo o site a cada mudança. Ela troca simplicidade por regras explícitas de frescor, cache e consistência.

## Em uma frase

ISR atualiza páginas estáticas incrementalmente conforme uma política de revalidação.

## O que precisa saber

ISR é uma estratégia de [[nextjs]] entre [[ssg]] e [[ssr]]. A equipe precisa definir janela de frescor, comportamento durante regeneração, falha da origem e invalidação manual quando necessário.

## Erros comuns

- Prometer atualização imediata com janela de revalidação.
- Cachear dados privados ou dependentes de sessão.
- Ignorar falhas e servir conteúdo antigo sem sinalização.

## Onde aparece

- Aulas 10–12 — Modos de Renderização SSG, SSR, ISR e CSR.
- Conecta [[nextjs]], [[ssg]], [[ssr]] e cache HTTP.

## Fontes

- Aula 10, páginas 1–4 dos slides: modos de renderização.
