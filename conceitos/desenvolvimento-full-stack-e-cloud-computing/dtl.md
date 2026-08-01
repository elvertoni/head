---
conceito: DTL
slug: dtl
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [Data Transaction Language, linguagem de controle de transações]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Modelagem de Banco de Dados/35 - Aula 35 - Modelo Físico de Dados IV - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

DTL é a classificação de comandos que controlam transações, permitindo confirmar ou desfazer grupos coerentes de operações. Ela ajuda a preservar consistência quando uma tarefa envolve múltiplas mudanças.

## Em uma frase

DTL coordena confirmação e reversão de operações relacionadas.

## O que precisa saber

Transações dependem de regras do [[sgbd]], isolamento, concorrência e recuperação. DTL trabalha junto a [[dml]] e [[restricoes-do-modelo-relacional]], mas não substitui o desenho correto do domínio nem tratamento de falhas.

## Erros comuns

- Confirmar parcialmente um fluxo que deveria ser atômico.
- Manter transações abertas e bloquear recursos.
- Assumir que rollback desfaz efeitos externos ao banco.

## Onde aparece

- Aula 35 — Modelo Físico de Dados IV.
- É uma categoria de [[sql]] relacionada a [[dml]], [[sgbd]] e [[modelo-relacional]].

## Fontes

- Aula 35, slides: transações, confirmação e reversão.
