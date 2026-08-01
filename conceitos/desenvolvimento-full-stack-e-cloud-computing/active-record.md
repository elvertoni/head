---
conceito: Active Record
slug: active-record
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [padrão Active Record]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Frameworks e Aplicações/17 - Aula 17 - Uso de MVC como Padrão de Projeto II - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Active Record é um padrão em que o objeto do domínio combina dados de um registro com operações de persistência. Ele aproxima o modelo do banco e simplifica casos CRUD.

## Em uma frase

Active Record reúne estado de um registro e operações para persisti-lo.

## O que precisa saber

O padrão é comum em ORMs como [[sequelize]], mas pode acoplar domínio, esquema e infraestrutura. [[orm]] não exige que todo modelo use Active Record.

## Erros comuns

- Misturar regras complexas e consultas no mesmo objeto sem limites.
- Expor modelo persistente diretamente na API.
- Confundir conveniência de CRUD com modelagem de domínio completa.

## Onde aparece

- Frameworks e Aplicações, Aula 17, página 3.
- Relaciona-se a [[sequelize]], [[orm]] e [[mvc]].

## Fontes

- Aula 17, página 3 dos slides: padrão Active Record.
