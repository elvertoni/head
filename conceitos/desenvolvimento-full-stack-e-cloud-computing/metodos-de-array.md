---
conceito: Métodos de array
slug: metodos-de-array
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [array methods]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/JavaScript e Aplicações Práticas/01 - Aula 1 - Arrays - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Métodos de array são operações da linguagem para consultar, transformar, selecionar, reduzir ou percorrer coleções JavaScript. Eles expressam intenção sobre dados sem exigir sempre um laço manual.

## Em uma frase

Métodos de array tornam transformações e consultas de coleções explícitas.

## O que precisa saber

map transforma, filter seleciona, find localiza e reduce combina valores, com diferenças de retorno e efeitos. O uso deve respeitar [[imutabilidade]] quando a interface depende de estado previsível.

## Erros comuns

- Usar map quando a intenção é apenas efeito colateral.
- Confundir find, filter e some.
- Mutar objetos compartilhados dentro de uma transformação.

## Onde aparece

- JavaScript e Aplicações Práticas, Aula 1, páginas 3–5.
- Relaciona-se a [[arrays-em-javascript]], [[funcoes-em-javascript]] e [[estado-mutavel]].

## Fontes

- Aula 1, páginas 3–5 dos slides: métodos de arrays.
