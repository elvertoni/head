---
conceito: Static site generation
slug: ssg
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [SSG, geração estática]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Frameworks, Programação e Estratégias/10 - Aula 10 - Modos de Renderização SSG, SSR, ISR e CSR I - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Static site generation produz páginas antecipadamente, durante build ou geração programada, para serem servidas como arquivos estáticos. Ela reduz custo de requisição, mas exige estratégia para dados que mudam.

## Em uma frase

SSG gera páginas antes da requisição para servir conteúdo estático com rapidez.

## O que precisa saber

SSG é uma escolha de [[nextjs]] distinta de [[ssr]] e [[isr]]. Ela funciona bem para conteúdo conhecido e cacheável; dados privados ou altamente dinâmicos exigem cuidado. O build passa a depender da disponibilidade dos dados de origem.

## Erros comuns

- Gerar conteúdo sensível ou específico de usuário no build.
- Tratar conteúdo estático como atualizado em tempo real.
- Ignorar custo de reconstrução e invalidação.

## Onde aparece

- Aulas 10–12 — Modos de Renderização SSG, SSR, ISR e CSR.
- Conecta [[nextjs]], [[ssr]] e [[isr]].

## Fontes

- Aula 10, páginas 1–4 dos slides: modos de renderização.
