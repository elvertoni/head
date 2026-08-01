---
conceito: DDL
slug: ddl
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [Data Definition Language, linguagem de definição de dados]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Modelagem de Banco de Dados/32 - Aula 32 - Modelo Físico de Dados - Apostila (Slides).pdf"
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Linguagens e Aplicações de Banco de Dados/12 - Aula 12 - Linguagem de Definição de Dados (DDL) - Apostila (Slides).pdf"
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Linguagens e Aplicações de Banco de Dados/13 - Aula 13 - Linguagem de Definição de Dados (DDL) II - Apostila (Slides).pdf"
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Linguagens e Aplicações de Banco de Dados/14 - Aula 14 - Linguagem de Definição de Dados (DDL) III - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

DDL é a parte do [[sql]] usada para definir e alterar estruturas do banco, como tabelas, esquemas, restrições e outros objetos. Seus comandos mudam o ambiente estrutural que recebe os dados.

## Em uma frase

DDL define a estrutura persistente sobre a qual os dados serão armazenados.

## O que precisa saber

DDL se relaciona ao [[modelo-fisico]], [[tipos-de-dados-sql]] e [[restricoes-do-modelo-relacional]]. Mudanças estruturais precisam de migração, revisão e compatibilidade com aplicações; o dialeto do [[sgbd]] importa.

## Erros comuns

- Alterar estrutura em produção sem plano de migração.
- Confundir definição de tabela com carga de dados.
- Ignorar dependências entre chaves, índices e visões.

## Onde aparece

- Aulas 32–35 — Modelo Físico de Dados.
- É uma categoria de [[sql]] ao lado de [[dml]], [[dql]], [[dcl]] e [[dtl]].

## Fontes

- Aula 32, slides: SQL, definição de estruturas e objetos.
