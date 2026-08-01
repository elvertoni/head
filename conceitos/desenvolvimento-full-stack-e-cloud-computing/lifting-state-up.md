---
conceito: Lifting state up
slug: lifting-state-up
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [elevação de estado]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Projeto Front - End e Desenvolvimento Web/22 - Aula 22 - Gerenciamento Avançado de Estados com React I - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Lifting state up move o estado compartilhado para o ancestral comum mais próximo dos componentes que precisam lê-lo ou alterá-lo.

## Em uma frase

Elevar estado cria uma única fonte de verdade para componentes relacionados.

## O que precisa saber

O pai passa [[props]] e callbacks; filhos continuam focados em apresentação e interação. Elevar demais aumenta re-renderizações e complexidade de API.

## Erros comuns

- Duplicar o mesmo estado em irmãos.
- Elevar estado que poderia permanecer local ao componente.

## Onde aparece

- Aula 22 — Gerenciamento avançado de estado React.

## Fontes

- Aula 22, páginas 1–2 dos slides: lifting state up.
