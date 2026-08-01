---
conceito: Atributo derivado
slug: atributo-derivado
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [atributo calculado]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Modelagem de Banco de Dados/11 - Aula 11 - Entidade e Atributos III - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Atributo derivado é um valor obtido por cálculo ou regra a partir de outros dados, em vez de ser necessariamente armazenado como entrada independente. Idade calculada a partir da data de nascimento é um exemplo clássico.

## Em uma frase

Atributo derivado pode ser calculado a partir de dados já existentes.

## O que precisa saber

Persistir o derivado pode melhorar desempenho, mas cria risco de divergência; calculá-lo reduz duplicação, mas pode custar consulta. A decisão deve considerar [[dado]], regras e [[modelo-fisico]]. O [[atributo]] de origem precisa permanecer confiável.

## Erros comuns

- Armazenar resultado derivado sem atualizar sua origem.
- Confundir valor calculável com valor que o negócio realmente registra.
- Ignorar data, fuso ou versão da regra no cálculo.

## Onde aparece

- Aula 11 — Entidade e Atributos III.
- É um tipo de [[atributo]] e afeta [[modelo-logico]] e [[modelo-fisico]].

## Fontes

- Aula 11, slides: atributos derivados e valores calculados.
