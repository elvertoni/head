---
conceito: Integridade referencial
slug: integridade-referencial
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [referential integrity]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Modelagem de Banco de Dados/24 - Aula 24 - Restrições do Modelo Relacional - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Integridade referencial garante que valores de uma [[chave-estrangeira]] correspondam a uma chave válida na relação referenciada, ou respeitem uma regra explícita de ausência. Ela evita vínculos órfãos e preserva a coerência entre relações.

## Em uma frase

Integridade referencial mantém válidos os vínculos entre relações.

## O que precisa saber

A regra depende de [[chave-primaria]], [[chave-estrangeira]] e ciclo de vida das entidades. Ao excluir ou alterar uma referência, o [[sgbd]] pode rejeitar, propagar, substituir ou permitir a operação conforme o modelo. A regra deve nascer da [[modelagem-de-dados]].

## Erros comuns

- Desativar a restrição para fazer uma carga rápida e esquecer de revalidar.
- Aceitar id órfão porque a aplicação “sabe” que é inválido.
- Usar cascata sem compreender o impacto da exclusão.

## Onde aparece

- Aulas 24–27 — Restrições do Modelo Relacional.
- Conecta [[chave-primaria]], [[chave-estrangeira]], [[restricoes-do-modelo-relacional]] e [[modelo-relacional]].

## Fontes

- Aula 24, slides: integridade referencial e restrições entre relações.
