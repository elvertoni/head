---
conceito: Revalidação de dados
slug: revalidacao-de-dados
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [data revalidation]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Frameworks, Programação e Estratégias/12 - Aula 12 - Modos de Renderização SSG, SSR, ISR e CSR III - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Revalidação de dados atualiza uma representação armazenada depois de um intervalo ou evento, equilibrando frescor, custo e latência.

## Em uma frase

Revalidar troca dados potencialmente antigos por uma atualização controlada.

## O que precisa saber

No [[isr]], a política define quando uma página ou resposta será refeita; [[cache-http]] e invalidação precisam ser coerentes. Frescor é requisito, não detalhe.

## Erros comuns

- Prometer atualização imediata com janela de revalidação.
- Invalidar cache sem considerar concorrência e falhas.

## Onde aparece

- Aulas 7 e 12 — Dados e modos de renderização.

## Fontes

- Aula 12, páginas 2–4 dos slides: ISR e revalidação.
