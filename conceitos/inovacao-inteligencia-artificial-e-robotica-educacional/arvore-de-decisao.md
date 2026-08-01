---
conceito: Árvore de decisão
slug: arvore-de-decisao
disciplina: inovacao-inteligencia-artificial-e-robotica-educacional
tipo: conceito
aka: [decision tree, árvore de decisão em aprendizado de máquina]
status: rascunho
fontes:
  - "lake/Inovacao-Inteligencia-Artificial-e-Robotica-Educacional/Módulo II - Inteligência Artificial/Inteligência Artificial e Blockchain/29 - Aula 29 - Armazenamento na Blockchain e Estrutura de Dados Merkle Tree II - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Árvore de decisão é um modelo de [[aprendizado-supervisionado|aprendizado supervisionado]] que divide exemplos recursivamente por atributos até produzir uma classe ou uma previsão. Cada nó representa uma decisão, cada ramo uma condição e cada folha um resultado; a escolha dos cortes procura separar melhor os dados.

## Em uma frase

Uma árvore de decisão transforma sucessivas perguntas sobre atributos em uma previsão.

## O que precisa saber

O modelo pode ser usado em [[classificacao-e-regressao|classificação e regressão]]. A construção escolhe atributos e pontos de corte segundo critérios de impureza ou erro, e precisa controlar profundidade para não memorizar o conjunto de treino. Não confundir esta estrutura com [[arvore-de-merkle|árvore de Merkle]], que organiza hashes para verificar integridade.

## Erros comuns

- Confundir árvore de decisão com árvore de Merkle por causa do nome “árvore”.
- Deixar a árvore crescer sem controle e produzir sobreajuste.
- Interpretar uma divisão do treinamento como causalidade no mundo real.

## Onde aparece

- Aula 29 — Armazenamento e Estrutura de Dados II, no Módulo II.
- Conecta [[aprendizado-supervisionado]], [[classificacao-e-regressao]], [[poda-de-arvore]] e contrasta com [[arvore-de-merkle]].

## Fontes

- Slides da Aula 29, páginas 1–7: árvore de decisão, divisão por atributos, impureza e parada.
- A fonte foi priorizada porque os slides tratam de árvore de decisão, apesar do nome do arquivo mencionar Merkle Tree.
