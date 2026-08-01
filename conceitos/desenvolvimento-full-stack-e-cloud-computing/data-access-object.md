---
conceito: Data Access Object
slug: data-access-object
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [DAO, objeto de acesso a dados]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Frameworks e Aplicações/17 - Aula 17 - Uso de MVC como Padrão de Projeto II - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Data Access Object é uma camada que encapsula operações de persistência e oferece ao restante da aplicação uma interface de acesso a dados. Ela reduz o acoplamento entre domínio e tecnologia de banco.

## Em uma frase

DAO isola consultas e persistência atrás de uma interface.

## O que precisa saber

O DAO pode usar [[orm]], SQL ou outro repositório, mantendo transações e mapeamentos explícitos. A abstração deve refletir necessidades reais, não esconder diferenças importantes.

## Erros comuns

- Criar um DAO genérico que não expressa o domínio.
- Esconder custo e paginação das consultas.
- Abrir transação fora do limite de consistência necessário.

## Onde aparece

- Frameworks e Aplicações, Aulas 17–18, páginas 1–5.
- Relaciona-se a [[mvc]], [[sequelize]] e [[orm]].

## Fontes

- Aula 17, página 3, e Aula 18, páginas 1–5 dos slides: DAO e persistência.
