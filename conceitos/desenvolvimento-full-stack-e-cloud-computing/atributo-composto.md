---
conceito: Atributo composto
slug: atributo-composto
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [atributo estruturado]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Modelagem de Banco de Dados/10 - Aula 10 - Entidade e Atributos II - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Atributo composto é uma propriedade que pode ser decomposta em componentes com significado próprio. Um endereço, por exemplo, pode reunir rua, número, cidade e código postal quando essas partes forem usadas separadamente.

## Em uma frase

Atributo composto reúne componentes que também têm significado no domínio.

## O que precisa saber

A decomposição deve responder a consultas e regras reais. O [[modelo-conceitual]] pode registrar a estrutura, enquanto o [[modelo-logico]] decide sua representação. Nem todo texto com várias palavras é composto.

## Erros comuns

- Decompor automaticamente qualquer valor textual.
- Guardar o composto e as partes sem definir qual é a fonte de verdade.
- Ignorar diferenças culturais de formato e endereço.

## Onde aparece

- Aula 10 — Entidade e Atributos II.
- É um tipo de [[atributo]] em [[modelo-entidade-relacionamento]].

## Fontes

- Aula 10, slides: atributos compostos e componentes.
