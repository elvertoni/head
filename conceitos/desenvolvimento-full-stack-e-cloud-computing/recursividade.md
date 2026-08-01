---
conceito: Recursividade
slug: recursividade
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [recursão]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/JavaScript e Aplicações Práticas/04 - Aula 4 - Recursividade - Apostila (Slides).pdf"
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/JavaScript e Aplicações Práticas/04 - Aula 4 - Recursividade - Resumo (Aula em PDF).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Recursividade é uma técnica em que uma função resolve um problema chamando a si própria com uma instância menor. A solução precisa de um caso-base e de uma redução que aproxime cada chamada desse caso.

## Em uma frase

Recursividade repete uma definição por chamadas menores até alcançar uma condição de parada.

## O que precisa saber

Recursão depende de [[funcoes-em-javascript]] e usa a pilha de chamadas; cada chamada precisa preservar seu contexto. Ela é útil para estruturas naturalmente aninhadas, mas um [[lacos-de-repeticao]] pode ser mais simples e econômico em outros problemas.

## Erros comuns

- Esquecer o caso-base e causar chamadas infinitas.
- Não reduzir o problema a cada chamada.
- Ignorar custo de memória e recomputação.

## Onde aparece

- Aula 4 — Recursividade, na trilha JavaScript e Aplicações Práticas.
- É uma aplicação de [[funcoes-em-javascript]].

## Fontes

- Aula 4, slides e resumo: função recursiva, caso-base e chamadas sucessivas.
