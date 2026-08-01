---
conceito: Chave estrangeira
slug: chave-estrangeira
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [foreign key, FK]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Modelagem de Banco de Dados/22 - Aula 22 - Esquemas, Relações e Chaves II - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Chave estrangeira é um atributo ou conjunto de atributos de uma relação que referencia uma chave de outra relação. Ela representa um vínculo entre ocorrências e permite ao SGBD aplicar regras de [[integridade-referencial]].

## Em uma frase

Chave estrangeira conecta uma relação à identidade de outra relação.

## O que precisa saber

O valor referenciado deve existir, salvo regra explícita de opcionalidade. Uma chave estrangeira é um mecanismo do [[modelo-relacional]] e pode materializar [[relacionamento-binario]] ou [[tabela-associativa]]. A ação para atualização e exclusão precisa ser decidida pelo domínio.

## Erros comuns

- Criar referência sem índice ou sem regra de ciclo de vida.
- Aceitar ids órfãos ou apagar dados sem entender dependências.
- Confundir chave estrangeira com qualquer coluna que contenha um id.

## Onde aparece

- Aulas 22–23 — Esquemas, Relações e Chaves.
- Conecta [[chave-primaria]], [[integridade-referencial]], [[modelo-relacional]] e [[relacionamento-binario]].

## Fontes

- Aula 22, slides: chaves estrangeiras e referências entre relações.
