---
conceito: Chaves de lista no React
slug: chaves-de-lista-react
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [React list keys, keys de lista]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Projeto Front - End e Desenvolvimento Web/09 - Aula 9 - Sintaxe da Linguagem JSX IV - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Chaves de lista no React são identificadores estáveis atribuídos aos elementos de uma coleção para que o reconciliador acompanhe a identidade de cada item entre renderizações. A chave orienta a atualização da árvore; ela não é uma propriedade de negócio entregue automaticamente ao componente.

## Em uma frase

Uma chave estável permite ao React distinguir itens de uma lista quando a interface muda.

## O que precisa saber

Ao usar [[renderizacao-de-listas]], prefira um identificador estável e único no conjunto, derivado do domínio. Usar o índice como chave só é seguro quando a lista é estática e não reordena. A escolha incorreta pode reaproveitar estado visual no item errado.

## Erros comuns

- Usar `Math.random()` e trocar a chave a cada renderização.
- Usar índice em listas que podem inserir, remover ou reordenar itens.
- Esperar receber `key` dentro de `props`.

## Onde aparece

- Projeto Front-End e Desenvolvimento Web, Aula 9, páginas 7–8.
- Relaciona-se a [[react]], [[renderizacao-de-listas]], [[componente-react]] e [[props]].

## Fontes

- Projeto Front-End e Desenvolvimento Web, Aula 9, slides sobre listas e identidade de elementos.
