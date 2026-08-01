---
conceito: Query string
slug: query-string
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [cadeia de consulta, parâmetros de consulta]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Arquitetura e Programação/02 - Aula 2 - Arquitetura de Uma Aplicação Web e o Formato Json II - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Query string é a parte opcional da URL que transporta pares de parâmetros depois do caminho. Ela costuma representar filtros, paginação, ordenação ou opções de uma requisição.

## Em uma frase

Query string leva parâmetros de consulta na URL.

## O que precisa saber

Parâmetros precisam ser codificados, validados e tratados como entrada não confiável. Diferem de [[parametros-de-rota]], que fazem parte da estrutura do caminho, embora ambos cheguem ao handler de uma [[api]].

## Erros comuns

- Colocar segredo ou dado pessoal na URL.
- Não validar tipos, limites e valores repetidos.
- Tratar a ordem dos parâmetros como significativa sem contrato.

## Onde aparece

- Arquitetura e Programação, Aula 2, páginas 3 e 6.
- Relaciona-se a [[http]], [[endpoint]] e [[parametros-de-rota]].

## Fontes

- Aula 2, páginas 3 e 6 dos slides: parâmetros de URL.
