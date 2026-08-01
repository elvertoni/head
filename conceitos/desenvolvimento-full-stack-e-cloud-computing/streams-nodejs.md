---
conceito: Streams no Node.js
slug: streams-nodejs
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [Node.js streams, fluxos de dados]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Arquitetura e Programação/20 - Aula 20 - Programação Assíncrona II - Apostila (Slides).pdf"
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Arquitetura e Programação/21 - Aula 21 - Programação Assíncrona III - Apostila (Slides).pdf"
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Arquitetura e Programação/22 - Aula 22 - Programação Assíncrona IV - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Streams no Node.js processam dados incrementalmente, em partes, sem exigir que todo o conteúdo esteja na memória. Eles representam fontes legíveis, destinos graváveis ou transformações entre os dois.

## Em uma frase

Streams tratam dados continuamente e em pedaços.

## O que precisa saber

Backpressure coordena a velocidade entre produtor e consumidor. Streams são úteis para arquivos, rede e respostas HTTP, e se conectam ao modelo de [[programacao-assincrona]].

## Erros comuns

- Acumular todo o fluxo e perder a vantagem de memória.
- Ignorar backpressure e sobrecarregar o consumidor.
- Não tratar eventos de erro e encerramento.

## Onde aparece

- Arquitetura e Programação, Aula 20, páginas 2 e 6.
- Relaciona-se a [[nodejs]], [[programacao-assincrona]] e [[http]].

## Fontes

- Aula 20, páginas 2 e 6 dos slides: streams e programação assíncrona.
