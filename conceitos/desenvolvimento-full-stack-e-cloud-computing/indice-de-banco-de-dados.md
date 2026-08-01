---
conceito: Índice de banco de dados
slug: indice-de-banco-de-dados
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [índice de banco, database index]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Modelagem de Banco de Dados/32 - Aula 32 - Modelo Físico de Dados - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Índice de banco de dados é uma estrutura auxiliar que acelera a localização de registros conforme determinadas colunas ou expressões. Ele troca espaço e custo de manutenção por menor custo em consultas favorecidas.

## Em uma frase

Índice acelera acessos selecionados, mas tem custo de armazenamento e atualização.

## O que precisa saber

Índices pertencem ao [[modelo-fisico]] e devem responder a consultas reais, seletividade e volume. Eles não substituem [[chave-primaria]], [[restricoes-do-modelo-relacional]] ou um modelo lógico coerente; muitos índices podem degradar escrita.

## Erros comuns

- Criar índice para toda coluna sem observar o plano de consulta.
- Confundir índice com regra de unicidade.
- Esquecer que cada escrita precisa manter os índices.

## Onde aparece

- Aulas 32–35 — Modelo Físico de Dados.
- Conecta [[modelo-fisico]], [[sgbd]], [[sql]] e [[chave-primaria]].

## Fontes

- Aula 32, slides: objetos e otimização do modelo físico.
