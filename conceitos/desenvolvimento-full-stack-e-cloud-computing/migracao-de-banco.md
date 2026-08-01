---
conceito: Migração de banco
slug: migracao-de-banco
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [migração de esquema]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Arquitetura e Programação/25 - Aula 25 - Acesso ao Banco de Dados SQL III - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Migração de banco é uma mudança versionada e reproduzível no esquema ou nos dados estruturais de um banco. Ela permite que ambientes diferentes avancem de forma coordenada.

## Em uma frase

Migração registra e aplica evoluções controladas do banco.

## O que precisa saber

Cada migração deve ter ordem, operação e estratégia de aplicação; mudanças incompatíveis exigem fases de compatibilidade. A ferramenta ORM pode gerar arquivos, mas a revisão continua necessária.

## Erros comuns

- Alterar produção manualmente e perder a história do esquema.
- Fazer uma migração destrutiva sem plano de dados.
- Acoplar deploy da aplicação a uma mudança impossível de reverter.

## Onde aparece

- Arquitetura e Programação, Aula 25, páginas 1–6.
- Relaciona-se a [[sequelize]], [[banco-de-dados-relacional]] e [[compatibilidade-retroativa]].

## Fontes

- Aula 25, páginas 1–6 dos slides: migrações e evolução do banco.
