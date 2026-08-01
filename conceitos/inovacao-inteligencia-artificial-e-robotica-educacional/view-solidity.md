---
conceito: View Solidity
slug: view-solidity
disciplina: inovacao-inteligencia-artificial-e-robotica-educacional
tipo: conceito
aka: [view function]
status: rascunho
fontes:
  - "lake/Inovacao-Inteligencia-Artificial-e-Robotica-Educacional/Módulo II - Inteligência Artificial/Conceitos Avançados em IA e Blockchain/27 - Aula 27 - Programação de Smart Contracts em Solidity III - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

View Solidity marca uma função que declara não alterar o estado persistente do contrato.

## Em uma frase

View documenta uma consulta sem escrita de estado.

## O que precisa saber

O modificador orienta compilador e leitores, mas a função ainda pode consumir recursos em certos contextos e fazer chamadas com efeitos indiretos proibidos ou limitados.

## Erros comuns

- Tratar view como garantia de custo zero em toda chamada.
- Confiar no modificador sem revisar chamadas internas.

## Onde aparece

- Aula 27 — Programação de smart contracts em Solidity III.

## Fontes

- Aula 27, páginas 4–6 dos slides: view e laços.
