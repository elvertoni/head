---
conceito: Geradores JavaScript
slug: geradores
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [generator functions]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/JavaScript e Aplicações Práticas/03 - Aula 3 - Funções - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Geradores são funções que podem pausar em yield e produzir valores sob demanda, devolvendo um iterador. Eles permitem controlar progressão e consumo de sequências.

## Em uma frase

Gerador pausa e retoma uma função para produzir valores sob demanda.

## O que precisa saber

O estado da execução é preservado entre chamadas next. Geradores implementam o protocolo de [[iteradores]] e podem representar sequências grandes sem materializá-las inteiras.

## Erros comuns

- Confundir yield com return definitivo.
- Ignorar o custo de trabalho realizado a cada next.
- Criar gerador sem definir encerramento e tratamento de erro.

## Onde aparece

- JavaScript e Aplicações Práticas, Aula 3, páginas 5–7.
- Relaciona-se a [[iteradores]], [[programacao-assincrona]] e [[funcoes-em-javascript]].

## Fontes

- Aula 3, páginas 5–7 dos slides: funções geradoras.
