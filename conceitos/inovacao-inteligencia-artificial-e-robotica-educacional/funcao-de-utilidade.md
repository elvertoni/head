---
conceito: Função de utilidade
slug: funcao-de-utilidade
disciplina: inovacao-inteligencia-artificial-e-robotica-educacional
tipo: conceito
aka: [utility function, utilidade de estado]
status: rascunho
fontes:
  - "lake/Inovacao-Inteligencia-Artificial-e-Robotica-Educacional/Módulo II - Inteligência Artificial/Inteligência Artificial e Blockchain/10 - Aula 10 - Busca Competitiva - Resumo (Aula em PDF).pdf"
  - "lake/Inovacao-Inteligencia-Artificial-e-Robotica-Educacional/Módulo II - Inteligência Artificial/Inteligência Artificial e Blockchain/11 - Aula 11 - Busca Competitiva II - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Função de utilidade atribui valores a estados ou resultados para representar o quanto são desejáveis para um agente. Em jogos, ela traduz vitória, derrota, empate ou preferências graduais em uma escala que permite comparar consequências; não é uma verdade objetiva sobre o estado, mas parte do modelo e dos objetivos escolhidos.

## Em uma frase

Utilidade transforma preferências do agente em valores que orientam escolhas.

## O que precisa saber

A função é aplicada em folhas ou estados avaliados da [[arvore-de-jogo|árvore de jogo]] e é propagada por [[minimax]]. Em [[jogo-de-soma-zero|jogos de soma zero]], o ganho de um agente corresponde à perda do outro; em [[jogos-de-azar|jogos de azar]], valores esperados incorporam probabilidades.

## Erros comuns

- Confundir utilidade com probabilidade de vencer.
- Escolher uma escala sem verificar se preserva a ordem das preferências.
- Ignorar que uma função ruim produz estratégias ruins mesmo com busca perfeita.

## Onde aparece

- Aulas 10–12 — Busca Competitiva, no Módulo II.
- Conecta [[busca-competitiva]], [[arvore-de-jogo]], [[minimax]], [[jogo-de-soma-zero]] e [[jogos-de-azar]].

## Fontes

- Resumo da Aula 10, páginas 2–4: utilidade e avaliação.
- Slides da Aula 11, página 6: função de utilidade.
