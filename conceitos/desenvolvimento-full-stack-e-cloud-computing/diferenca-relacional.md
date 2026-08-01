---
conceito: Diferença relacional
slug: diferenca-relacional
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [diferença de relações, EXCEPT]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Linguagens e Aplicações de Banco de Dados/07 - Aula 7 - Operações de Conjunto III - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Diferença relacional retorna as tuplas que estão na primeira relação e não estão na segunda. A operação é direcionada: trocar os operandos normalmente muda o resultado.

## Em uma frase

Diferença remove de uma relação as tuplas encontradas em outra.

## O que precisa saber

As relações devem ser compatíveis. Em SQL, a ideia aparece em EXCEPT ou em anti-junções e subconsultas, sempre com atenção à semântica de NULL.

## Erros comuns

- Tratar a diferença como operação comutativa.
- Confundir ausência de correspondência com valor nulo.
- Usar NOT IN sem analisar o comportamento de NULL.

## Onde aparece

- Linguagens e Aplicações de Banco de Dados, Aula 7, páginas 1–3.
- Relaciona-se a [[operacoes-de-conjunto-relacional]] e [[subconsulta-sql]].

## Fontes

- Aula 7, páginas 1–3 dos slides: diferença entre relações.
