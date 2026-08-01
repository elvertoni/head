---
conceito: Bloco de blockchain
slug: bloco-de-blockchain
disciplina: inovacao-inteligencia-artificial-e-robotica-educacional
tipo: conceito
aka: [block, bloco da cadeia]
status: rascunho
fontes:
  - "lake/Inovacao-Inteligencia-Artificial-e-Robotica-Educacional/Módulo II - Inteligência Artificial/Inteligência Artificial e Blockchain/28 - Aula 28 - Armazenamento na Blockchain e Estrutura de Dados Merkle Tree - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Bloco de blockchain é uma unidade de dados que reúne transações ou informações e é adicionada linearmente à cadeia conforme as regras de consenso. Seu cabeçalho e conteúdo permitem relacionar o bloco ao histórico anterior e verificar se os dados foram alterados.

## Em uma frase

Um bloco agrupa dados e entra na cadeia somente depois de passar pelas regras de validação da rede.

## O que precisa saber

O bloco pode carregar metadados, transações e referências ao bloco anterior. A combinação com [[hashing]] e [[imutabilidade-de-registro]] torna alterações detectáveis, mas não impede que a governança aceite uma reorganização válida. Nós propagam e verificam blocos conforme seu papel em [[blockchain]].

## Erros comuns

- Confundir bloco com a blockchain inteira.
- Supor que adicionar um bloco torne qualquer dado verdadeiro.
- Ignorar validação, consenso e referências ao histórico anterior.

## Onde aparece

- Aula 28 — Armazenamento e Estrutura de Dados, no Módulo II.
- É uma unidade estrutural de [[blockchain]] relacionada a [[imutabilidade-de-registro]] e [[hashing]].

## Fontes

- Slides da Aula 28, páginas 4–5: composição e adição linear de blocos.
