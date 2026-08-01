---
conceito: Chave composta
slug: chave-composta
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [composite key]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Modelagem de Banco de Dados/23 - Aula 23 - Esquemas, Relações e Chaves III - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Chave composta usa dois ou mais atributos em conjunto para identificar uma tupla. Cada componente isolado pode repetir, mas a combinação precisa obedecer à unicidade da relação.

## Em uma frase

Chave composta identifica uma ocorrência pela combinação de atributos.

## O que precisa saber

Ela pode ser uma [[chave-primaria]] ou [[chave-candidata]] e aparece com frequência em [[tabela-associativa]]. Os atributos precisam formar um conjunto mínimo e estável; referências externas devem reproduzir a composição de forma consistente.

## Erros comuns

- Usar colunas redundantes ou que não participam da identidade.
- Referenciar parcialmente uma chave composta.
- Confundir chave composta com duas chaves independentes.

## Onde aparece

- Aula 23 — Esquemas, Relações e Chaves III.
- Conecta [[chave-primaria]], [[chave-candidata]], [[tabela-associativa]] e [[relacao]].

## Fontes

- Aula 23, slides: chaves compostas e identificação por combinação.
