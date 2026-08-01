---
conceito: Transação de banco
slug: transacao-de-banco
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [transação de banco de dados]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Arquitetura e Programação/28 - Aula 28 - Consumindo Dados de um Banco de Dados Relacional III - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Transação de banco é uma unidade lógica de operações que deve ser confirmada ou desfeita de acordo com suas garantias de consistência. Ela coordena mudanças relacionadas em um banco relacional.

## Em uma frase

Transação agrupa operações persistentes com um resultado controlado.

## O que precisa saber

COMMIT confirma e ROLLBACK desfaz o trabalho conforme o mecanismo do banco. [[acid]] e [[nivel-de-isolamento]] explicam garantias e interferências; ORMs como [[sequelize]] devem expor limites transacionais claros.

## Erros comuns

- Atualizar parte do agregado sem transação quando há invariantes conjuntas.
- Manter transações abertas durante chamadas externas demoradas.
- Capturar erro sem executar rollback ou liberar a conexão.

## Onde aparece

- Arquitetura e Programação, Aula 28, páginas 2–5.
- Relaciona-se a [[acid]], [[nivel-de-isolamento]], [[sequelize]] e [[dtl]].

## Fontes

- Aula 28, páginas 2–5 dos slides: transações relacionais e ACID.
