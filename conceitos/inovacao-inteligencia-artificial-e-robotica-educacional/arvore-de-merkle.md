---
conceito: Árvore de Merkle
slug: arvore-de-merkle
disciplina: inovacao-inteligencia-artificial-e-robotica-educacional
tipo: conceito
aka: [Merkle Tree, Merkle Hash Tree]
status: rascunho
fontes:
  - "lake/Inovacao-Inteligencia-Artificial-e-Robotica-Educacional/Módulo II - Inteligência Artificial/Inteligência Artificial e Blockchain/30 - Aula 30 - Armazenamento na Blockchain e Estrutura de Dados Merkle Tree III - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Árvore de Merkle é uma estrutura hierárquica em que hashes de dados ou transações são combinados em níveis até produzir uma [[raiz-de-merkle|raiz de Merkle]]. Ela permite verificar a inclusão e a integridade de um item usando um caminho curto de hashes, sem comparar todo o conjunto armazenado.

## Em uma frase

Uma árvore de Merkle resume muitos dados em uma raiz que permite verificações eficientes de integridade e inclusão.

## O que precisa saber

Folhas representam resumos dos itens; nós internos combinam hashes dos filhos e a raiz representa a estrutura inteira. Uma alteração em uma folha propaga mudanças até a raiz. A estrutura usa [[hashing]], apoia a verificação em [[blockchain]] e não deve ser confundida com [[arvore-de-decisao|árvore de decisão]].

## Erros comuns

- Confundir árvore de Merkle com modelo de classificação e regressão.
- Achar que a raiz revela ou armazena todos os dados originais.
- Verificar apenas a raiz sem receber o caminho de prova correspondente ao item.

## Onde aparece

- Aula 30 — Armazenamento e Estrutura de Dados III, no Módulo II.
- Conecta [[hashing]], [[blockchain]], [[integridade-de-dados]], [[imutabilidade-de-registro]], [[poda-de-arvore]], [[arvore-de-decisao]] e [[raiz-de-merkle]].

## Fontes

- Slides da Aula 30, páginas 1–4: árvore de Merkle, hashes hierárquicos e verificação de integridade.
- O Resumo da Aula 28 foi usado apenas como confirmação do tema; os resumos das Aulas 28–30 são duplicados.
