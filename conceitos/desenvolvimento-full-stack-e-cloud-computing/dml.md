---
conceito: DML
slug: dml
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [Data Manipulation Language, linguagem de manipulação de dados]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Modelagem de Banco de Dados/33 - Aula 33 - Modelo Físico de Dados II - Apostila (Slides).pdf"
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Linguagens e Aplicações de Banco de Dados/15 - Aula 15 - Linguagem de Manipulação de Dados (DML) - Apostila (Slides).pdf"
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Linguagens e Aplicações de Banco de Dados/16 - Aula 16 - Linguagem de Manipulação de Dados (DML) II - Apostila (Slides).pdf"
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Linguagens e Aplicações de Banco de Dados/17 - Aula 17 - Linguagem de Manipulação de Dados (DML) III - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

DML é a parte do [[sql]] usada para inserir, atualizar e remover dados nas estruturas do banco. Ela altera instâncias das relações sem necessariamente alterar o esquema.

## Em uma frase

DML modifica os dados armazenados dentro de uma estrutura já definida.

## O que precisa saber

Operações DML devem respeitar [[restricoes-do-modelo-relacional]], [[integridade-referencial]] e transações. Validação, autorização e concorrência pertencem ao contexto do [[sgbd]] e da aplicação.

## Erros comuns

- Executar update ou delete sem filtro e sem transação controlada.
- Ignorar referências e constraints.
- Tratar carga de dados como operação sem auditoria.

## Onde aparece

- Aula 33 — Modelo Físico de Dados II.
- É uma categoria de [[sql]] relacionada a [[dtl]] e [[modelo-relacional]].

## Fontes

- Aula 33, slides: manipulação e alteração de dados.
