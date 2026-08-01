---
conceito: Conversão de tipos
slug: conversao-de-tipos
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [coerção e conversão de tipos]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Padrões Web - HTML e CSS/05 - Aula 5 - Criando Soluções WEB - Resumo (Aula em PDF).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Conversão de tipos é a transformação explícita de um valor de uma representação para outra, como converter texto recebido em número. Em JavaScript, ela é importante porque entradas de interfaces costumam chegar como strings.

## Em uma frase

Converter tipos torna explícita a representação necessária para uma operação.

## O que precisa saber

parseInt, Number e outras operações têm regras diferentes para entradas inválidas e decimais. A conversão deve ocorrer perto da fronteira de [[entrada-e-saida-em-javascript]], antes de cálculos com [[operadores-javascript]]. O resultado precisa ser validado, não apenas convertido.

## Erros comuns

- Somar strings esperando uma soma numérica.
- Aceitar conversão parcial ou NaN como dado válido.
- Converter sem informar unidade, base ou formato esperado.

## Onde aparece

- Aula 5 — Criando Soluções WEB.
- Conecta [[entrada-e-saida-em-javascript]], [[operadores-javascript]], [[manipulacao-do-dom]] e [[caixas-de-dialogo-javascript]].

## Fontes

- Resumo da Aula 5, páginas 2–3 e 8: parseInt, entrada e conversão.
