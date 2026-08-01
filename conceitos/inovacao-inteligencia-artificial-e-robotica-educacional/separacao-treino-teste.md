---
conceito: Separação treino-teste
slug: separacao-treino-teste
disciplina: inovacao-inteligencia-artificial-e-robotica-educacional
tipo: conceito
aka: [divisão treino-teste]
status: rascunho
fontes:
  - "lake/Inovacao-Inteligencia-Artificial-e-Robotica-Educacional/Módulo II - Inteligência Artificial/Conceitos Avançados em IA e Blockchain/05 - Aula 5 - Aprendizado de Máquina II - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Separação treino-teste reserva parte dos exemplos para ajustar o modelo e outra parte independente para estimar seu desempenho em dados não vistos.

## Em uma frase

Treino aprende; teste verifica se a hipótese generaliza.

## O que precisa saber

O procedimento combate avaliação enganosa e se relaciona a [[validacao-cruzada]] e [[dados-treino-inferencia]]. A separação deve respeitar tempo, grupos e dependências do problema.

## Erros comuns

- Ajustar transformações usando também o teste.
- Reutilizar o teste para escolher repetidamente o modelo.

## Onde aparece

- Aula 5 — Aprendizado de Máquina II.

## Fontes

- Aula 5, páginas 2–6 dos slides: conjunto de treino e conjunto de teste.
