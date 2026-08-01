---
conceito: Modelo lógico
slug: modelo-logico
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [modelo lógico de dados]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Modelagem de Banco de Dados/07 - Aula 7 - Modelo Entidade Relacionamento III - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Modelo lógico organiza o domínio segundo um modelo de dados, detalhando relações, atributos, chaves e restrições sem ainda depender de armazenamento específico. No modelo relacional, ele aproxima o desenho conceitual da estrutura de tabelas.

## Em uma frase

O modelo lógico transforma significado em estruturas e regras do modelo escolhido.

## O que precisa saber

O modelo lógico recebe o resultado do [[modelo-conceitual]] por meio do [[mapeamento-conceitual-logico]]. Em um [[banco-de-dados-relacional]], chaves e relações tornam explícita a identidade dos registros. Decisões sobre índices e tipos de armazenamento ficam para o [[modelo-fisico]].

## Erros comuns

- Confundir modelo lógico com script DDL pronto.
- Criar uma tabela para cada tela sem representar o domínio.
- Esquecer cardinalidades e restrições ao transformar relações.

## Onde aparece

- Aulas 7–8 — Modelo Entidade Relacionamento.
- É uma etapa de [[modelagem-de-dados]] entre [[modelo-conceitual]] e [[modelo-fisico]].

## Fontes

- Aula 7, slides: transformação do modelo conceitual e organização lógica.
