---
conceito: Esquema de banco de dados
slug: esquema-de-banco-de-dados
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [database schema, esquema relacional]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Modelagem de Banco de Dados/21 - Aula 21 - Esquemas, Relações e Chaves - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Esquema de banco de dados é a descrição da estrutura de uma relação ou banco, incluindo nomes, atributos, domínios, chaves e restrições. Ele descreve a forma relativamente estável; a instância registra os valores presentes em um momento.

## Em uma frase

Esquema descreve a estrutura; instância descreve os dados que a ocupam.

## O que precisa saber

No [[modelo-relacional]], o esquema define relações, atributos e regras; [[instancia-de-dados]] é o estado atual. O esquema pode mudar por DDL, mas alterações precisam considerar aplicações e [[independencia-de-dados]].

## Erros comuns

- Confundir esquema com uma cópia dos dados.
- Alterar estrutura sem migração ou compatibilidade.
- Omitir chaves e restrições da descrição.

## Onde aparece

- Aulas 21–23 — Esquemas, Relações e Chaves.
- Conecta [[modelo-relacional]], [[relacao]], [[tupla]], [[instancia-de-dados]] e [[ddl]].

## Fontes

- Aula 21, slides: esquema, relação e instância.
