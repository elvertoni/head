---
conceito: Tabela associativa
slug: tabela-associativa
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [relação associativa, tabela de junção]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Modelagem de Banco de Dados/30 - Aula 30 - Mapeamento do Modelo Conceitual para o Lógico III - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Tabela associativa é uma relação criada para representar no modelo relacional um relacionamento muitos-para-muitos ou um relacionamento que possui atributos próprios. Ela normalmente contém chaves estrangeiras para as relações participantes.

## Em uma frase

Tabela associativa transforma uma associação complexa em uma relação consultável e restrita.

## O que precisa saber

A chave pode ser composta pelas referências ou por um identificador próprio com restrição de unicidade. A decisão deve preservar [[cardinalidade]], atributos do [[relacionamento]] e [[integridade-referencial]]. O desenho vem do [[mapeamento-conceitual-logico]].

## Erros comuns

- Criar tabela associativa para relação um-para-muitos sem necessidade.
- Permitir duplicidade da mesma combinação.
- Esquecer atributos que pertencem à associação, não às entidades.

## Onde aparece

- Aulas 28–31 — Mapeamento do Modelo Conceitual para o Lógico.
- Conecta [[relacionamento-binario]], [[cardinalidade]], [[chave-composta]], [[chave-estrangeira]] e [[modelo-relacional]].

## Fontes

- Aula 30, slides: transformação de relacionamentos e tabelas associativas.
