---
conceito: Sequência de banco de dados
slug: sequencia-de-banco-de-dados
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [database sequence]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Modelagem de Banco de Dados/35 - Aula 35 - Modelo Físico de Dados IV - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Sequência de banco de dados é um objeto que produz valores numéricos conforme uma política de incremento, frequentemente para apoiar identificadores. Ela é gerenciada pelo SGBD e pode apresentar lacunas por concorrência, rollback ou consumo antecipado.

## Em uma frase

Sequência gera valores ordenados segundo regras do banco, não necessariamente sem lacunas.

## O que precisa saber

Sequência pode apoiar uma [[chave-primaria]], mas não garante por si só unicidade global, significado de negócio ou continuidade. A configuração depende do [[sgbd]] e do [[modelo-fisico]]; aplicações distribuídas precisam entender concorrência e cache.

## Erros comuns

- Usar sequência como relógio ou prova de ordem absoluta.
- Esperar que rollback devolva o número consumido.
- Confundir valor gerado com identidade de negócio.

## Onde aparece

- Aula 35 — Modelo Físico de Dados IV.
- Conecta [[chave-primaria]], [[sgbd]], [[modelo-fisico]] e [[sql]].

## Fontes

- Aula 35, slides: sequências e objetos físicos.
