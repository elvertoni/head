---
conceito: Erro customizado Solidity
slug: erro-customizado-solidity
disciplina: inovacao-inteligencia-artificial-e-robotica-educacional
tipo: conceito
aka: [custom error]
status: rascunho
fontes:
  - "lake/Inovacao-Inteligencia-Artificial-e-Robotica-Educacional/Módulo II - Inteligência Artificial/Conceitos Avançados em IA e Blockchain/23 - Aula 23 - Programação de Smart Contracts Em Solidity II - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Erro customizado Solidity nomeia uma condição de falha e pode transportar parâmetros de diagnóstico com menos custo que mensagens genéricas.

## Em uma frase

Erro customizado comunica falhas de contrato de forma estruturada.

## O que precisa saber

Ele se relaciona a [[require-solidity]] e [[revert-solidity]]. O cliente deve interpretar erros sem expor dados que não deveria confiar ou exibir.

## Erros comuns

- Tratar erro retornado como prova de que nada mudou sem entender o rollback.
- Criar mensagens sem documentar invariantes violadas.

## Onde aparece

- Aulas 21 e 23 — Smart contracts e Solidity.

## Fontes

- Aula 23, páginas 6–7 dos slides: erros e eventos.
