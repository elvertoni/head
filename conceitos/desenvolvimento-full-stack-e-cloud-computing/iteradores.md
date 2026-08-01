---
conceito: Iteradores
slug: iteradores
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [iterators]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/JavaScript e Aplicações Práticas/03 - Aula 3 - Funções - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Iteradores são objetos que implementam um protocolo para produzir valores sucessivos sob demanda, geralmente por next. Eles permitem percorrer coleções com abstração uniforme.

## Em uma frase

Iterador produz a próxima parte de uma sequência quando solicitado.

## O que precisa saber

O protocolo distingue iterável de iterador; for...of consome iteráveis. O padrão se relaciona a [[arrays-em-javascript]], [[geradores]] e consumo incremental.

## Erros comuns

- Confundir iterador com array materializado.
- Reutilizar iterador já consumido sem reiniciá-lo.
- Fazer operação síncrona pesada em sequência grande.

## Onde aparece

- JavaScript e Aplicações Práticas, Aula 3, páginas 5–7.
- Relaciona-se a [[geradores]], [[arrays-em-javascript]] e [[metodos-de-array]].

## Fontes

- Aula 3, páginas 5–7 dos slides: iteradores e percursos.
