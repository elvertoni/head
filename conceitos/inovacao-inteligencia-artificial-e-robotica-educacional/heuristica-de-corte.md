---
conceito: Heurística de corte
slug: heuristica-de-corte
disciplina: inovacao-inteligencia-artificial-e-robotica-educacional
tipo: conceito
aka: [cutoff heuristic, avaliação de corte]
status: rascunho
fontes:
  - "lake/Inovacao-Inteligencia-Artificial-e-Robotica-Educacional/Módulo II - Inteligência Artificial/Inteligência Artificial e Blockchain/10 - Aula 10 - Busca Competitiva - Resumo (Aula em PDF).pdf"
  - "lake/Inovacao-Inteligencia-Artificial-e-Robotica-Educacional/Módulo II - Inteligência Artificial/Inteligência Artificial e Blockchain/12 - Aula 12 - Busca Competitiva III - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Heurística de corte é a regra que interrompe a expansão de uma árvore de jogo em uma profundidade, tempo ou condição escolhida e avalia o estado sem alcançar necessariamente um terminal. Ela permite que [[minimax]] funcione sob recursos limitados, ao custo de aproximar o valor real da posição.

## Em uma frase

Corte heurístico troca exploração completa por uma avaliação aproximada dentro do limite de recursos.

## O que precisa saber

O corte pode depender de profundidade, relógio, estabilidade da posição ou orçamento de nós. A função de avaliação deve estimar a utilidade dos estados intermediários; [[poda-alfa-beta|alfa-beta]] pode reduzir ainda mais a expansão sem alterar o resultado da parte explorada.

## Erros comuns

- Confundir corte heurístico com poda alfa-beta.
- Avaliar posições intermediárias com critérios que favorecem o resultado errado.
- Ignorar horizonte: uma ameaça pode aparecer logo depois do corte.

## Onde aparece

- Aulas 10–12 — Busca Competitiva, no Módulo II.
- Apoia [[busca-competitiva]], [[minimax]] e se combina com [[poda-alfa-beta]].

## Fontes

- Resumo da Aula 10, página 5: corte e limite de busca.
- Slides da Aula 12, páginas 2–4: avaliação limitada.
