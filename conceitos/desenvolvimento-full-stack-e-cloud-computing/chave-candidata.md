---
conceito: Chave candidata
slug: chave-candidata
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [candidate key]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Modelagem de Banco de Dados/23 - Aula 23 - Esquemas, Relações e Chaves III - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Chave candidata é um conjunto mínimo de atributos capaz de identificar unicamente cada tupla de uma relação. Uma delas é escolhida como [[chave-primaria]]; as demais continuam podendo receber restrições de unicidade.

## Em uma frase

Chave candidata é uma alternativa mínima para identificar uma ocorrência.

## O que precisa saber

“Mínimo” significa que nenhum atributo pode ser removido sem perder unicidade. A escolha da primária deve considerar estabilidade e referências; uma chave composta usa [[chave-composta]]. Chaves candidatas nascem de regras do [[modelo-conceitual]] e do domínio.

## Erros comuns

- Chamar qualquer conjunto único de candidata sem testar minimalidade.
- Escolher a chave mais curta sem considerar estabilidade.
- Ignorar identificadores naturais que o domínio já garante.

## Onde aparece

- Aula 23 — Esquemas, Relações e Chaves III.
- Conecta [[chave-primaria]], [[chave-composta]], [[relacao]] e [[modelo-relacional]].

## Fontes

- Aula 23, slides: chaves candidatas, alternativas e minimalidade.
