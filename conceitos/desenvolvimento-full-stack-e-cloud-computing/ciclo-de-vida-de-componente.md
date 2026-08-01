---
conceito: Ciclo de vida de componente
slug: ciclo-de-vida-de-componente
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [component lifecycle]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Projeto Front - End e Desenvolvimento Web/25 - Aula 25 - Gerenciamento Ciclos de Vida de Componentes_ Classes e Hooks I - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Ciclo de vida de componente descreve fases de criação, atualização e desmontagem, além dos efeitos associados a cada fase da interface.

## Em uma frase

Ciclo de vida orienta quando um componente deve preparar, reagir e limpar recursos.

## O que precisa saber

Hooks modelam efeitos e dependências no [[react]]; classes usam métodos próprios. Timers, listeners e requisições precisam de cleanup e cancelamento.

## Erros comuns

- Criar efeito que nunca é limpo.
- Usar efeito para calcular valor que poderia ser derivado durante a renderização.

## Onde aparece

- Aulas 25–27 — Ciclo de vida, classes e hooks.

## Fontes

- Aula 25, páginas 2–5 dos slides: ciclo de vida de componentes.
