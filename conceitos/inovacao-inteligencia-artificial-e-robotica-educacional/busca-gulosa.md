---
conceito: Busca gulosa
slug: busca-gulosa
disciplina: inovacao-inteligencia-artificial-e-robotica-educacional
tipo: conceito
aka: [greedy search, greedy best-first search]
status: rascunho
fontes:
  - "lake/Inovacao-Inteligencia-Artificial-e-Robotica-Educacional/Módulo II - Inteligência Artificial/Inteligência Artificial e Blockchain/08 - Aula 8 - Busca Heurística II - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Busca gulosa é uma estratégia de [[busca-heuristica|busca heurística]] que escolhe para expansão o estado com a menor estimativa de custo restante até a meta. Ela pode encontrar rapidamente uma solução, mas olha apenas para a promessa futura indicada por `h(n)` e não para o custo já pago no caminho.

## Em uma frase

Busca gulosa segue o estado que parece mais perto da meta segundo a heurística.

## O que precisa saber

O algoritmo ordena a fronteira pelo valor heurístico. Sua simplicidade pode ser útil quando uma solução rápida basta, mas a estratégia não garante por si só um caminho ótimo e pode ser enganada por uma estimativa localmente atraente. A [[busca-a-estrela|busca A*]] acrescenta o custo acumulado, enquanto [[heuristica-admissivel|heurística admissível]] é uma propriedade da estimativa, não da busca gulosa em si.

## Erros comuns

- Confundir menor estimativa com menor custo total da solução.
- Afirmar que a busca gulosa é ótima apenas porque usa uma heurística.
- Esquecer de controlar estados repetidos e ciclos no grafo de busca.

## Onde aparece

- Aula 8 — Busca Heurística II, no Módulo II.
- É uma estratégia de [[busca-heuristica]] e ponto de comparação para [[busca-a-estrela]], [[busca-de-custo-uniforme]] e [[heuristica-admissivel]].

## Fontes

- Slides da Aula 8, páginas 1–5: seção “Busca Gulosa”, heurística, vantagens e limitações.
