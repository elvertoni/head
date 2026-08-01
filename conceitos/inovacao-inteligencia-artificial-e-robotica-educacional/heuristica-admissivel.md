---
conceito: Heurística admissível
slug: heuristica-admissivel
disciplina: inovacao-inteligencia-artificial-e-robotica-educacional
tipo: conceito
aka: [admissible heuristic]
status: rascunho
fontes:
  - "lake/Inovacao-Inteligencia-Artificial-e-Robotica-Educacional/Módulo II - Inteligência Artificial/Inteligência Artificial e Blockchain/07 - Aula 7 - Busca Heurística - Resumo (Aula em PDF).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Heurística admissível é uma estimativa `h(n)` que nunca superestima o custo real mínimo de alcançar a meta a partir do estado `n`. Essa propriedade torna a estimativa otimista e é uma condição importante para analisar a optimalidade da [[busca-a-estrela|busca A*]].

## Em uma frase

Uma heurística admissível nunca estima um custo restante maior que o custo real mínimo.

## O que precisa saber

A admissibilidade restringe o valor da estimativa, não determina sozinha como os estados serão explorados. A [[busca-gulosa]] pode usar uma heurística admissível sem se tornar ótima, porque desconsidera `g(n)`; a [[busca-a-estrela|busca A*]] combina `h(n)` com o custo acumulado.

## Erros comuns

- Confundir admissibilidade com precisão: uma estimativa admissível pode ser muito fraca.
- Dizer que toda heurística útil precisa ser admissível.
- Esquecer que a propriedade deve ser avaliada em relação ao custo real do problema.

## Onde aparece

- Aula 7 — Busca Heurística, no Módulo II.
- Apoia [[busca-heuristica]], [[busca-gulosa]] e [[busca-a-estrela]].

## Fontes

- Resumo da Aula 7, páginas 1, 5 e 7: estimativa que não superestima o custo.
