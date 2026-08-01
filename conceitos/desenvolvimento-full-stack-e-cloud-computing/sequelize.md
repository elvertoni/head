---
conceito: Sequelize
slug: sequelize
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: entidade
aka: [Sequelize ORM]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Arquitetura e Programação/24 - Aula 24 - Acesso ao Banco de Dados SQL II - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Sequelize é uma biblioteca ORM para JavaScript e Node.js que representa modelos relacionais e executa operações sobre bancos compatíveis. Ela fornece modelos, associações, consultas e suporte a migrações.

## Em uma frase

Sequelize implementa mapeamento objeto-relacional em aplicações Node.js.

## O que precisa saber

Modelos e associações descrevem o domínio; transações e consultas controlam a persistência. [[migracao-de-banco]] e [[seeder-de-banco]] organizam a evolução e os dados iniciais fora do código de execução.

## Erros comuns

- Misturar sincronização automática do modelo com migrações controladas.
- Não usar transação em operações relacionadas.
- Expor atributos internos do modelo diretamente na API.

## Onde aparece

- Arquitetura e Programação, Aula 24, páginas 2–5.
- Relaciona-se a [[orm]], [[mysql]], [[migracao-de-banco]] e [[transacao-de-banco]].

## Fontes

- Aula 24, páginas 2–5 dos slides: Sequelize e modelos relacionais.
