---
conceito: A unidade fr
slug: unidade-fr
disciplina: programacao-front-end
tipo: conceito
aka: [fr, fração do espaço livre]
status: rascunho
fontes: []
aulas: [13]
atualizado_em: 2026-09-24
---

`fr` significa fração do espaço livre — uma unidade que só existe dentro do [[css-grid|CSS Grid]]. `1fr 1fr 1fr` divide em três partes iguais o que sobrou depois de descontar o `gap` e as margens, e por isso quase nunca estoura: enquanto a porcentagem é calculada sobre o total e ignora os espaços entre colunas, `fr` reparte só o que de fato sobrou.

## Em uma frase

`fr` reparte o espaço que sobrou depois do `gap`, e por isso não estoura como a porcentagem.

## O que precisa saber

`repeat(3, 1fr)` cria sempre três colunas — mas `repeat(auto-fit, minmax(250px, 1fr))` deixa o navegador calcular sozinho quantas colunas de pelo menos 250px cabem na largura disponível, reorganizando cards sem nenhuma media query. `fr` nasceu com o CSS Grid, criado do zero para pensar em duas dimensões, em contraste com a era de `float` usado para simular grade.

## Erros comuns

- Misturar `width: 33.33%` com `gap` no mesmo layout — as porcentagens já somam 100%, e os espaços do `gap` são somados por cima, estourando a largura da linha e derrubando o último card para a linha de baixo.

## Onde aparece

- Aula 13 — *Grid: os três benefícios viram cards* `aulas/programacao-front-end/landing-page-mvp/13-grid-cards-de-beneficio/canonica.md`
- Conceitos vizinhos: [[css-grid]], [[flexbox]]

## Fontes

- Conteúdo autoral da Aula 13 (modo_origem: tema), sem fonte externa direta — `fr`, `repeat(auto-fit, minmax(...))` e o estouro de linha com porcentagem.
