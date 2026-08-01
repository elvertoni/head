---
conceito: ACID
slug: acid
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [propriedades ACID]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Arquitetura e Programação/28 - Aula 28 - Consumindo Dados de um Banco de Dados Relacional III - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

ACID reúne atomicidade, consistência, isolamento e durabilidade, propriedades esperadas de transações em bancos relacionais. O conjunto descreve garantias, não uma promessa de que toda aplicação está automaticamente correta.

## Em uma frase

ACID organiza garantias de confiabilidade para transações.

## O que precisa saber

[[transacao-de-banco]] delimita a unidade de trabalho; [[nivel-de-isolamento]] controla interferência entre transações. Integridade depende também de restrições, modelo, tratamento de erros e recuperação.

## Erros comuns

- Assumir que ACID elimina conflitos de negócio.
- Abrir uma transação e não encerrá-la em todos os caminhos.
- Escolher isolamento máximo sem medir custo e necessidade.

## Onde aparece

- Arquitetura e Programação, Aula 28, páginas 2–5.
- Relaciona-se a [[transacao-de-banco]], [[nivel-de-isolamento]] e [[banco-de-dados-relacional]].

## Fontes

- Aula 28, páginas 2–5 dos slides: propriedades ACID.
