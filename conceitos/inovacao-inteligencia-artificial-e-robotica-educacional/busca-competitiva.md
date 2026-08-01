---
conceito: Busca competitiva
slug: busca-competitiva
disciplina: inovacao-inteligencia-artificial-e-robotica-educacional
tipo: conceito
aka: [busca adversarial, competitive search]
status: rascunho
fontes:
  - "lake/Inovacao-Inteligencia-Artificial-e-Robotica-Educacional/Módulo II - Inteligência Artificial/Inteligência Artificial e Blockchain/10 - Aula 10 - Busca Competitiva - Apostila (Slides).pdf"
  - "lake/Inovacao-Inteligencia-Artificial-e-Robotica-Educacional/Módulo II - Inteligência Artificial/Inteligência Artificial e Blockchain/10 - Aula 10 - Busca Competitiva - Resumo (Aula em PDF).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Busca competitiva é a busca por uma ação em ambientes em que outro agente também escolhe ações e tenta maximizar seus próprios resultados. O problema é modelado como jogo, com estados, ações, turnos, resultados e uma estratégia que considera respostas possíveis do adversário, em vez de buscar apenas um caminho até uma meta fixa.

## Em uma frase

Busca competitiva escolhe ações levando em conta que outro agente tentará frustrar ou superar a estratégia.

## O que precisa saber

O modelo usa [[arvore-de-jogo|árvore de jogo]], [[funcao-de-utilidade|função de utilidade]] e, em muitos casos, [[minimax]]. Jogos podem ser determinísticos ou incluir acaso; limites de tempo e fator de ramificação exigem aproximações como [[poda-alfa-beta|poda alfa-beta]] e [[heuristica-de-corte|corte heurístico]].

## Erros comuns

- Tratar o adversário como ruído aleatório em vez de agente estratégico.
- Confundir busca competitiva com uma simples busca em grafo.
- Ignorar tempo, incerteza, função de utilidade e custo de explorar a árvore.

## Onde aparece

- Aulas 10–12 — Busca Competitiva, no Módulo II.
- Conecta [[inteligencia-artificial]], [[jogos]], [[arvore-de-jogo]], [[funcao-de-utilidade]], [[minimax]], [[poda-alfa-beta]] e [[heuristica-de-corte]].

## Fontes

- Slides da Aula 10, páginas 1–6: busca competitiva e jogos.
- Resumo da Aula 10, páginas 1–2: agentes, estados e estratégias.
