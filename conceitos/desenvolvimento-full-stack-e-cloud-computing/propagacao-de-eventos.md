---
conceito: Propagação de eventos
slug: propagacao-de-eventos
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [event bubbling and capturing]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/JavaScript e Aplicações Práticas/05 - Aula 5 - Imersão JavaScript - Coleções e Funções - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Propagação de eventos é o percurso de um evento pela árvore DOM, passando pela captura até o alvo e, em seguida, pela fase de bubbling. O percurso define quais listeners podem reagir.

## Em uma frase

Eventos percorrem a árvore DOM em fases previsíveis.

## O que precisa saber

stopPropagation interrompe o percurso; preventDefault cancela a ação padrão e tem finalidade diferente. A compreensão do fluxo é essencial à [[delegacao-de-eventos]].

## Erros comuns

- Usar stopPropagation para corrigir arquitetura confusa.
- Confundir impedir propagação com impedir ação padrão.
- Registrar listener na fase errada.

## Onde aparece

- JavaScript e Aplicações Práticas, Aula 5, páginas 2–3.
- Relaciona-se a [[modelo-de-eventos-do-dom]], [[delegacao-de-eventos]] e [[manipulacao-do-dom]].

## Fontes

- Aula 5, páginas 2–3 dos slides: propagação de eventos.
