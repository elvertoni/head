---
conceito: Chamadas de mensagem
slug: chamadas-de-mensagem
disciplina: inovacao-inteligencia-artificial-e-robotica-educacional
tipo: conceito
aka: [message calls]
status: rascunho
fontes:
  - "lake/Inovacao-Inteligencia-Artificial-e-Robotica-Educacional/Módulo II - Inteligência Artificial/Conceitos Avançados em IA e Blockchain/22 - Aula 22 - Programação de Smart Contracts Em Solidity - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Chamadas de mensagem são invocações entre contas ou contratos Ethereum que transportam dados, valor e contexto de execução.

## Em uma frase

Uma chamada conecta contratos e propaga contexto e custo.

## O que precisa saber

Chamadas podem falhar, consumir gas e alterar estado. `msg.sender`, valor e permissões devem ser validados em cada fronteira.

## Erros comuns

- Confiar no remetente aparente após uma chamada encadeada.
- Ignorar reentrância e tratamento de erro.

## Onde aparece

- Aula 22 — Programação de smart contracts em Solidity.

## Fontes

- Aula 22, página 5 dos slides: chamadas entre contratos.
