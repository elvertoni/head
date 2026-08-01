---
conceito: Virtual DOM
slug: virtual-dom
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [DOM virtual]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Projeto Front - End e Desenvolvimento Web/04 - Aula 4 - Primeiros Passos com React I - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Virtual DOM é uma representação em memória da árvore de interface usada por bibliotecas como React para calcular mudanças antes de atualizar o DOM do navegador.

## Em uma frase

Virtual DOM compara árvores para aplicar atualizações necessárias na interface.

## O que precisa saber

Ele apoia o modelo declarativo de [[react]], mas não torna toda atualização instantânea nem substitui medir desempenho. Estado e identidade de elementos afetam reconciliação.

## Erros comuns

- Tratar Virtual DOM como cópia completa sempre atualizada do DOM real.
- Usar keys instáveis e provocar remontagens desnecessárias.

## Onde aparece

- Aula 4 — Primeiros passos com React.

## Fontes

- Aula 4, páginas 5–6 dos slides: Virtual DOM e React.
