---
conceito: Instância de dados
slug: instancia-de-dados
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [estado do banco, instância relacional]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Modelagem de Banco de Dados/23 - Aula 23 - Esquemas, Relações e Chaves III - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Instância de dados é o conjunto de valores que ocupa um esquema em um determinado momento. Ela muda conforme inserções, alterações e remoções, enquanto o esquema define as estruturas e regras que os valores devem respeitar.

## Em uma frase

Instância é o estado atual dos dados dentro de um esquema.

## O que precisa saber

Uma instância contém [[tupla|tuplas]] em [[relacao|relações]] e deve satisfazer [[restricoes-do-modelo-relacional]]. Mudanças de instância são operações de [[dml]]; mudanças de esquema são operações de [[ddl]].

## Erros comuns

- Confundir uma fotografia dos dados com o modelo permanente.
- Alterar instância sem respeitar chaves e domínios.
- Usar exemplo de dados como se fosse regra de estrutura.

## Onde aparece

- Aula 23 — Esquemas, Relações e Chaves III.
- Conecta [[esquema-de-banco-de-dados]], [[tupla]], [[relacao]], [[ddl]] e [[dml]].

## Fontes

- Aula 23, slides: instância, esquema e estado das relações.
