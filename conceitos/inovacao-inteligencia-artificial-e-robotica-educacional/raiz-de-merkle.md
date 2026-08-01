---
conceito: Raiz de Merkle
slug: raiz-de-merkle
disciplina: inovacao-inteligencia-artificial-e-robotica-educacional
tipo: conceito
aka: [Merkle root, hash-raiz]
status: rascunho
fontes:
  - "lake/Inovacao-Inteligencia-Artificial-e-Robotica-Educacional/Módulo II - Inteligência Artificial/Inteligência Artificial e Blockchain/30 - Aula 30 - Armazenamento na Blockchain e Estrutura de Dados Merkle Tree III - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Raiz de Merkle é o hash no topo de uma [[arvore-de-merkle|árvore de Merkle]], calculado a partir dos hashes dos níveis inferiores. Ela funciona como um compromisso compacto com o conjunto organizado de dados: se uma folha ou combinação mudar, a raiz esperada também muda.

## Em uma frase

A raiz de Merkle resume a estrutura inteira em um único hash verificável.

## O que precisa saber

A raiz não substitui os dados nem prova sozinha que eles são verdadeiros; ela permite comparar o compromisso esperado e verificar caminhos de inclusão. Sua segurança depende de [[hashing]], da resistência a [[colisao-criptografica|colisões]] e da forma como a prova é distribuída.

## Erros comuns

- Confundir a raiz com uma cópia de todas as transações.
- Tratar qualquer hash como uma raiz de Merkle sem conhecer a estrutura combinada.
- Ignorar a prova de caminho necessária para verificar uma folha.

## Onde aparece

- Aula 30 — Armazenamento e Estrutura de Dados III, no Módulo II.
- É o resumo superior de [[arvore-de-merkle]] baseado em [[hashing]] e avaliado quanto a [[colisao-criptografica]].

## Fontes

- Slides da Aula 30, páginas 1–4: raiz e estrutura hierárquica de hashes.
- Resumo da Aula 28, páginas 4–6: confirmação do conceito de Merkle root.
