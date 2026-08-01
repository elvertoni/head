---
conceito: Early stopping
slug: early-stopping
disciplina: inovacao-inteligencia-artificial-e-robotica-educacional
tipo: conceito
aka: [parada antecipada]
status: rascunho
fontes:
  - "lake/Inovacao-Inteligencia-Artificial-e-Robotica-Educacional/Módulo II - Inteligência Artificial/Conceitos Avançados em IA e Blockchain/06 - Aula 6 - Aprendizado de Máquina III - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Early stopping interrompe o treinamento quando o desempenho de validação deixa de melhorar, antes que o modelo memorize ruído do treino.

## Em uma frase

Parada antecipada usa a validação para limitar o tempo de ajuste.

## O que precisa saber

É uma forma prática de [[regularizacao]] e precisa guardar o melhor estado observado. A métrica e a paciência devem refletir a tarefa, não apenas o último lote.

## Erros comuns

- Parar com base apenas no erro de treino.
- Usar o teste como sinal durante o treinamento.

## Onde aparece

- Aula 6 — Aprendizado de Máquina III.

## Fontes

- Aula 6, páginas 5–8 dos slides: early stopping.
