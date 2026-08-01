---
conceito: Modelo físico
slug: modelo-fisico
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [modelo físico de dados]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Modelagem de Banco de Dados/32 - Aula 32 - Modelo Físico de Dados - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Modelo físico descreve como o modelo lógico será implementado em um SGBD concreto, incluindo tipos, índices, objetos, armazenamento e escolhas de desempenho. Ele materializa decisões sem substituir a validação do domínio.

## Em uma frase

O modelo físico traduz estruturas lógicas para uma tecnologia de banco específica.

## O que precisa saber

O modelo físico parte do [[modelo-logico]] e pode definir [[tipos-de-dados-sql]], [[indice-de-banco-de-dados]] e objetos como [[visao-de-banco-de-dados]]. Ele deve respeitar chaves e regras de [[banco-de-dados-relacional]], mas pode incluir otimizações dependentes do [[sgbd]].

## Erros comuns

- Escolher índices antes de conhecer consultas reais.
- Confundir otimização física com correção do modelo.
- Tornar o projeto dependente de um SGBD sem registrar a decisão.

## Onde aparece

- Aulas 32–35 — Modelo Físico de Dados.
- Conecta [[modelo-logico]], [[tipos-de-dados-sql]], [[indice-de-banco-de-dados]] e [[sgbd]].

## Fontes

- Aula 32, slides: finalidade e componentes do modelo físico.
