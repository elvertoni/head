---
conceito: Superclasse
slug: superclasse
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [entidade supertipo]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Modelagem de Banco de Dados/15 - Aula 15 - Modelo Entidade Relacionamento Estendido - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Superclasse é a entidade geral que reúne atributos e relacionamentos comuns a um conjunto de [[subclasse|subclasses]]. Ela representa a abstração compartilhada sem apagar propriedades específicas dos subtipos.

## Em uma frase

Superclasse concentra o que é comum a entidades especializadas.

## O que precisa saber

Superclasse aparece em [[generalizacao]] e [[especializacao]]. O modelo precisa indicar cobertura, disjunção e identidade; na passagem para o [[modelo-logico]], atributos comuns e específicos precisam continuar rastreáveis.

## Erros comuns

- Colocar na superclasse atributos que não valem para todos os subtipos.
- Confundir superclasse com uma tabela-pai sem discutir semântica.
- Omitir como a identidade será herdada.

## Onde aparece

- Aula 15 — Modelo Entidade Relacionamento Estendido.
- Conecta [[especializacao]], [[generalizacao]], [[subclasse]] e [[modelo-entidade-relacionamento-estendido]].

## Fontes

- Aula 15, slides: superclasse, subclasses e herança.
