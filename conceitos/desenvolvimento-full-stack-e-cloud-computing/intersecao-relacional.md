---
conceito: Interseção relacional
slug: intersecao-relacional
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [interseção de relações, INTERSECT]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Linguagens e Aplicações de Banco de Dados/06 - Aula 6 - Operações de Conjunto II - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Interseção relacional retorna as tuplas que pertencem simultaneamente a duas relações compatíveis. Ela representa a parte comum entre dois resultados.

## Em uma frase

Interseção conserva apenas o que aparece nos dois conjuntos relacionais.

## O que precisa saber

Assim como a [[uniao-relacional]], exige compatibilidade de esquema. Em dialetos SQL que suportam INTERSECT, a operação pode ser expressa diretamente; em outros, pode ser reescrita com junções ou subconsultas.

## Erros comuns

- Comparar relações incompatíveis.
- Confundir interseção com uma junção por chave.
- Não verificar duplicatas e valores nulos na reescrita SQL.

## Onde aparece

- Linguagens e Aplicações de Banco de Dados, Aulas 5–6.
- Relaciona-se a [[operacoes-de-conjunto-relacional]] e [[subconsulta-sql]].

## Fontes

- Aulas 5–6, páginas iniciais dos slides: interseção relacional.
