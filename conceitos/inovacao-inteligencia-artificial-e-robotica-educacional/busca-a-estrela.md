---
conceito: Busca A*
slug: busca-a-estrela
disciplina: inovacao-inteligencia-artificial-e-robotica-educacional
tipo: conceito
aka: [A*, a-star, algoritmo A-estrela]
status: rascunho
fontes:
  - "lake/Inovacao-Inteligencia-Artificial-e-Robotica-Educacional/Módulo II - Inteligência Artificial/Inteligência Artificial e Blockchain/09 - Aula 9 - Busca Heurística III - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Busca A* é uma estratégia de [[busca-heuristica|busca heurística]] que ordena os estados pela soma do custo já percorrido `g(n)` com a estimativa do custo restante `h(n)`, formando `f(n)=g(n)+h(n)`. O equilíbrio entre caminho percorrido e promessa futura torna o método mais informado que a [[busca-gulosa]].

## Em uma frase

Busca A* escolhe o estado com menor custo acumulado mais estimativa de custo restante.

## O que precisa saber

O algoritmo mantém uma fronteira de estados e prioriza o menor `f(n)`. Sob as condições adequadas de representação e com uma [[heuristica-admissivel|heurística admissível]], pode preservar a garantia de solução ótima; a qualidade da estimativa afeta diretamente o trabalho de busca. A busca gulosa usa apenas `h(n)`, enquanto A* também considera `g(n)`.

## Erros comuns

- Escrever `f(n)=h(n)` e chamar o procedimento de A*; isso descreve a busca gulosa.
- Supor optimalidade sem verificar as condições da heurística e dos custos.
- Ignorar memória e crescimento da fronteira em problemas grandes.

## Onde aparece

- Aula 9 — Busca Heurística III, no Módulo II.
- Combina [[busca-heuristica]], [[busca-gulosa]], [[busca-de-custo-uniforme]] e [[heuristica-admissivel]].

## Fontes

- Slides da Aula 9, páginas 1–6: seção “Busca A*”, custos `g`, `h` e `f(n)=g(n)+h(n)`.
