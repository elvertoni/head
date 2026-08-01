---
conceito: Testes de integração
slug: testes-de-integracao
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [integration tests]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Frameworks e Aplicações/09 - Aula 9 - Ferramentas para Testar Back - End - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Testes de integração verificam a interação entre componentes, como servidor, banco, filas ou módulos. Eles revelam incompatibilidades que um teste unitário isolado não alcança.

## Em uma frase

Teste de integração verifica se componentes colaboram corretamente.

## O que precisa saber

O ambiente e as dependências precisam ser controlados, mas o teste deve preservar a integração relevante. [[teste-de-api]] é uma aplicação comum para contratos HTTP.

## Erros comuns

- Chamar teste unitário de integração sem dependência real.
- Compartilhar estado entre casos e gerar ordem acidental.
- Ignorar limpeza, dados e isolamento do ambiente.

## Onde aparece

- Frameworks e Aplicações, Aula 9, páginas 2 e 4–5.
- Relaciona-se a [[teste-de-api]], [[orm]] e [[testes-unitarios]].

## Fontes

- Aula 9, páginas 2 e 4–5 dos slides: testes de integração.
