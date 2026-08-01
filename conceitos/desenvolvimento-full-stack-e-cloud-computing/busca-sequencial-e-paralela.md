---
conceito: Busca sequencial e paralela
slug: busca-sequencial-e-paralela
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [fetch sequencial e paralelo]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Frameworks, Programação e Estratégias/07 - Aula 7 - Busca de Dados e Roteamento Dinâmico I - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Busca sequencial aguarda uma operação antes de iniciar a próxima; busca paralela inicia operações independentes em conjunto. A escolha altera latência, carga e tratamento de falhas.

## Em uma frase

Buscas independentes podem ocorrer em paralelo para reduzir espera total.

## O que precisa saber

Dependências reais exigem sequência, enquanto operações independentes podem usar composição de [[promises]]. Limites de concorrência, cancelamento e erros continuam necessários.

## Erros comuns

- Paralelizar operações dependentes e produzir dados inconsistentes.
- Abrir requisições ilimitadas.
- Abortar uma etapa sem tratar as demais.

## Onde aparece

- Frameworks, Programação e Estratégias, Aula 7, página 4.
- Relaciona-se a [[programacao-assincrona]], [[promises]] e [[busca-de-dados-no-servidor]].

## Fontes

- Aula 7, página 4 dos slides: buscas sequenciais e paralelas.
