---
conceito: Jogos de azar
slug: jogos-de-azar
disciplina: inovacao-inteligencia-artificial-e-robotica-educacional
tipo: conceito
aka: [jogos estocásticos, chance nodes]
status: rascunho
fontes:
  - "lake/Inovacao-Inteligencia-Artificial-e-Robotica-Educacional/Módulo II - Inteligência Artificial/Inteligência Artificial e Blockchain/10 - Aula 10 - Busca Competitiva - Resumo (Aula em PDF).pdf"
  - "lake/Inovacao-Inteligencia-Artificial-e-Robotica-Educacional/Módulo II - Inteligência Artificial/Inteligência Artificial e Blockchain/10 - Aula 10 - Busca Competitiva - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Jogos de azar são jogos ou situações de decisão em que eventos aleatórios influenciam o próximo estado ou resultado. Na busca competitiva, nós de acaso e probabilidades ampliam a árvore e exigem comparar valores esperados, em vez de presumir que todo resultado decorre apenas da ação de um jogador.

## Em uma frase

Jogos com acaso exigem modelar probabilidades além das escolhas dos agentes.

## O que precisa saber

Uma árvore pode alternar nós MAX, MIN e nós de chance. [[funcao-de-utilidade|Função de utilidade]] e expectativa ajudam a comparar resultados; [[minimax]] precisa ser adaptado quando o acaso entra no modelo. O agente deve distinguir aleatoriedade real de informação incompleta.

## Erros comuns

- Tratar acaso como se fosse um adversário racional.
- Usar o resultado mais provável como se fosse garantido.
- Ignorar como probabilidades são obtidas e atualizadas.

## Onde aparece

- Aulas 10–12 — Busca Competitiva, no Módulo II.
- Conecta [[jogos]], [[arvore-de-jogo]], [[funcao-de-utilidade]], [[minimax]] e [[jogo-de-soma-zero]].

## Fontes

- Resumo da Aula 10, página 6: jogos de azar e nós de acaso.
- Slides da Aula 10, páginas 1–6: jogos e resultados.
