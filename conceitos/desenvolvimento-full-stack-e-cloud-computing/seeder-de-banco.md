---
conceito: Seeder de banco
slug: seeder-de-banco
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [seed de banco, carga inicial]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Arquitetura e Programação/25 - Aula 25 - Acesso ao Banco de Dados SQL III - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Seeder de banco é um script controlado que insere dados iniciais, de referência ou de demonstração em um banco. Ele torna a preparação de ambientes repetível.

## Em uma frase

Seeder povoa o banco com dados necessários ou controlados.

## O que precisa saber

Seeds devem ser idempotentes ou ter execução claramente versionada. Dados de teste não podem ser confundidos com dados reais nem carregar segredos.

## Erros comuns

- Executar seed de demonstração em produção sem revisão.
- Criar duplicatas a cada execução.
- Fixar senhas ou dados pessoais no repositório.

## Onde aparece

- Arquitetura e Programação, Aula 25, páginas 1–6.
- Relaciona-se a [[sequelize]], [[migracao-de-banco]] e [[mysql]].

## Fontes

- Aula 25, páginas 1–6 dos slides: seeders e preparação de dados.
