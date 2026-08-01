---
conceito: Pipes e filtros
slug: pipes-e-filtros
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [pipes and filters]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Frameworks e Aplicações/16 - Aula 16 - Uso de MVC como Padrão de Projeto - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Pipes e filtros organiza um processamento como sequência de filtros independentes conectados por fluxos de dados. Cada filtro transforma uma entrada e entrega uma saída ao próximo estágio.

## Em uma frase

Pipes e filtros compõe transformações independentes em um pipeline.

## O que precisa saber

O padrão favorece composição e teste isolado, mas exige contrato de dados, tratamento de erro e controle de fluxo. [[streams-nodejs]] é uma forma operacional relacionada.

## Erros comuns

- Compartilhar estado oculto entre filtros.
- Ignorar backpressure e volume de dados.
- Criar pipeline cuja ordem não é explicitada.

## Onde aparece

- Frameworks e Aplicações, Aula 16, páginas 2–3.
- Relaciona-se a [[streams-nodejs]], [[programacao-assincrona]] e [[padroes-arquiteturais]].

## Fontes

- Aula 16, páginas 2–3 dos slides: padrão pipes e filtros.
