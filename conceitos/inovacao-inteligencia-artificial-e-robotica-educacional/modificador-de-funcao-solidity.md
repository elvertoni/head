---
conceito: Modificador de função Solidity
slug: modificador-de-funcao-solidity
disciplina: inovacao-inteligencia-artificial-e-robotica-educacional
tipo: conceito
aka: [function modifier]
status: rascunho
fontes:
  - "lake/Inovacao-Inteligencia-Artificial-e-Robotica-Educacional/Módulo II - Inteligência Artificial/Conceitos Avançados em IA e Blockchain/23 - Aula 23 - Programação de Smart Contracts Em Solidity II - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Modificador de função Solidity encapsula uma condição ou preparação reutilizável que deve ser satisfeita antes ou depois da execução de uma função.

## Em uma frase

Modificador centraliza pré-condições e controles de acesso.

## O que precisa saber

Ele pode verificar remetente, estado e invariantes, mas lógica implícita dificulta leitura se usada em excesso. Testes precisam cobrir todas as combinações.

## Erros comuns

- Esconder efeitos importantes em modificadores encadeados.
- Usar `tx.origin` ou identidade inadequada para autorização.

## Onde aparece

- Aula 23 — Programação de smart contracts em Solidity II.

## Fontes

- Aula 23, páginas 4–5 dos slides: funções e modificadores.
