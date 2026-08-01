---
conceito: Delegação de eventos
slug: delegacao-de-eventos
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [event delegation]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/JavaScript e Aplicações Práticas/05 - Aula 5 - Imersão JavaScript - Coleções e Funções - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Delegação de eventos registra um listener em um ancestral para tratar eventos de elementos descendentes, aproveitando a propagação. Ela reduz listeners e funciona bem para listas dinâmicas quando o alvo é validado.

## Em uma frase

Delegação centraliza eventos de elementos relacionados em um ancestral.

## O que precisa saber

closest, target e currentTarget têm papéis diferentes; a lógica deve confirmar o elemento esperado. O padrão depende do [[modelo-de-eventos-do-dom]] e da [[propagacao-de-eventos]].

## Erros comuns

- Aceitar qualquer target e permitir ações indevidas.
- Delegar eventos que não propagam como esperado.
- Manter listener no ancestral depois que o componente foi destruído.

## Onde aparece

- JavaScript e Aplicações Práticas, Aula 5, páginas 2–3.
- Relaciona-se a [[modelo-de-eventos-do-dom]], [[propagacao-de-eventos]] e [[ciclo-de-vida-do-documento]].

## Fontes

- Aula 5, páginas 2–3 dos slides: delegação de eventos.
