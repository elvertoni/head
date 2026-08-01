---
conceito: Generalização
slug: generalizacao
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [generalização de entidades]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Modelagem de Banco de Dados/15 - Aula 15 - Modelo Entidade Relacionamento Estendido - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Generalização é o processo de abstrair atributos e relacionamentos comuns de várias entidades em uma superclasse. Ela reduz repetição conceitual sem apagar diferenças relevantes dos subtipos.

## Em uma frase

Generalização extrai o que é comum a entidades para formar uma abstração mais ampla.

## O que precisa saber

O resultado se relaciona a [[especializacao]], [[superclasse]] e [[subclasse]]. A abstração deve ser justificada pelo domínio e mapeada para o [[modelo-logico]] com regras claras de identidade e cobertura.

## Erros comuns

- Criar superclasse apenas para reutilizar nomes sem significado de domínio.
- Colocar na superclasse o que só vale para um subtipo.
- Não decidir como a herança será persistida.

## Onde aparece

- Aulas 15–17 — Modelo Entidade Relacionamento Estendido.
- É o movimento complementar de [[especializacao]].

## Fontes

- Aula 15, slides: generalização e abstração de entidades.
