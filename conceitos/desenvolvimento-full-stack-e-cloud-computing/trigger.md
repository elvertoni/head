---
conceito: Trigger
slug: trigger
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [gatilho de banco de dados]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Modelagem de Banco de Dados/35 - Aula 35 - Modelo Físico de Dados IV - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Trigger é uma rotina disparada automaticamente por eventos definidos no banco, como inserção, alteração ou remoção. Ele pode impor auditoria ou regras, mas torna efeitos colaterais menos visíveis para quem executa a operação.

## Em uma frase

Trigger executa lógica automaticamente quando um evento do banco acontece.

## O que precisa saber

Triggers fazem parte do [[modelo-fisico]] e podem atuar junto a [[restricoes-do-modelo-relacional]], [[dml]] e transações. Seu uso exige documentação, observabilidade, ordem de execução e cuidado com recursão ou cascatas inesperadas.

## Erros comuns

- Esconder alterações importantes em efeitos implícitos.
- Criar cascatas difíceis de depurar.
- Usar trigger para toda regra que deveria estar explícita na aplicação ou constraint.

## Onde aparece

- Aula 35 — Modelo Físico de Dados IV.
- Conecta [[sql]], [[dml]], [[dtl]], [[stored-procedure]] e [[modelo-fisico]].

## Fontes

- Aula 35, slides: triggers e execução orientada a eventos.
