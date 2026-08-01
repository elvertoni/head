---
conceito: Geração de parâmetros estáticos no Next.js
slug: geracao-de-parametros-estaticos-nextjs
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [generateStaticParams]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Frameworks, Programação e Estratégias/12 - Aula 12 - Modos de Renderização SSG, SSR, ISR e CSR III - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Geração de parâmetros estáticos no Next.js produz antecipadamente os valores de rotas dinâmicas que serão construídas durante a geração estática. Ela conecta dados conhecidos à estratégia de [[ssg]] ou [[isr]].

## Em uma frase

Parâmetros estáticos antecipam quais rotas dinâmicas serão geradas.

## O que precisa saber

A lista inicial precisa ser atualizada quando o domínio muda e não deve ser usada para autorizar acesso. A estratégia conversa com [[roteamento-dinamico]], [[ssg]] e [[isr]].

## Erros comuns

- Confundir geração de rota com autorização.
- Gerar uma lista incompleta e retornar páginas ausentes.
- Ignorar revalidação de dados e de novas rotas.

## Onde aparece

- Frameworks, Programação e Estratégias, Aula 12, páginas 2–4.
- Relaciona-se a [[roteamento-dinamico]], [[ssg]] e [[isr]].

## Fontes

- Aula 12, páginas 2–4 dos slides: parâmetros estáticos.
