---
conceito: Mapeamento conceitual-lógico
slug: mapeamento-conceitual-logico
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [transformação conceitual para lógico]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Modelagem de Banco de Dados/28 - Aula 28 - Mapeamento do Modelo Conceitual para o Lógico - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Mapeamento conceitual-lógico é o conjunto de regras que transforma entidades, atributos e relacionamentos do modelo conceitual em estruturas do modelo lógico. Ele decide como identidades, cardinalidades e dependências serão preservadas.

## Em uma frase

Mapeamento transforma o significado do domínio em estruturas do modelo escolhido.

## O que precisa saber

Entidades costumam virar relações; atributos viram colunas ou relações próprias; relacionamentos dependem de sua [[cardinalidade]] e podem exigir [[chave-estrangeira]] ou [[tabela-associativa]]. O resultado deve ser validado contra o [[modelo-conceitual]] e o [[modelo-relacional]].

## Erros comuns

- Fazer tradução mecânica sem preservar regras.
- Perder atributos de relacionamentos.
- Criar duplicidade ou referência sem integridade.

## Onde aparece

- Aulas 28–31 — Mapeamento do Modelo Conceitual para o Lógico.
- Conecta [[modelo-conceitual]], [[modelo-logico]], [[modelo-entidade-relacionamento]], [[cardinalidade]] e [[tabela-associativa]].

## Fontes

- Aula 28, slides: regras iniciais de mapeamento conceitual para lógico.
