---
conceito: Inversão de controle
slug: inversao-de-controle
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [Inversion of Control, IoC]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Arquitetura e Programação/30 - Aula 30 - Evolução e Gestão do Ciclo de Vida de uma API - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Inversão de controle ocorre quando um framework, contêiner ou infraestrutura assume o fluxo de chamar componentes, em vez de a aplicação controlar todas as chamadas. [[injecao-de-dependencia]] é uma forma comum de aplicá-la.

## Em uma frase

Inversão de controle entrega o fluxo de execução à infraestrutura configurada.

## O que precisa saber

Handlers, middlewares, eventos e contêineres são exemplos de pontos de extensão. O contrato de ciclo de vida precisa ser compreendido para que o código seja previsível.

## Erros comuns

- Confundir IoC com uma biblioteca específica.
- Esconder efeitos importantes em hooks automáticos.
- Criar configuração global impossível de testar isoladamente.

## Onde aparece

- Arquitetura e Programação, Aula 30, páginas 3–4.
- Relaciona-se a [[injecao-de-dependencia]], [[backend]] e [[expressjs]].

## Fontes

- Aula 30, páginas 3–4 dos slides: inversão de controle e arquitetura de API.
