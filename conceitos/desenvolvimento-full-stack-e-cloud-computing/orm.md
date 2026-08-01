---
conceito: ORM
slug: orm
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [Object-Relational Mapping, mapeamento objeto-relacional]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Arquitetura e Programação/24 - Aula 24 - Acesso ao Banco de Dados SQL II - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

ORM é uma técnica e camada de software que mapeia objetos da aplicação para tabelas, linhas e relações de um banco relacional. Ela reduz SQL repetitivo, mas não elimina a necessidade de entender o banco.

## Em uma frase

ORM traduz operações entre objetos da aplicação e relações persistidas.

## O que precisa saber

Modelos, associações, consultas, transações e migrações compõem o mapeamento. A abstração deve ser inspecionada para evitar consultas excessivas, inconsistentes ou caras.

## Erros comuns

- Supor que ORM sempre produz a consulta mais eficiente.
- Criar o problema N+1 ao navegar associações.
- Esconder transações e regras de integridade atrás do modelo.

## Onde aparece

- Arquitetura e Programação, Aula 24, páginas 1–2.
- Relaciona-se a [[sequelize]], [[banco-de-dados-relacional]] e [[modelagem-de-dados]].

## Fontes

- Aula 24, páginas 1–2 dos slides: ORM e acesso relacional.
