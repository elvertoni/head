---
conceito: Mobile-first
slug: mobile-first
disciplina: programacao-front-end
tipo: conceito
aka: [mobile first]
status: rascunho
fontes: []
aulas: [4, 8, 14]
atualizado_em: 2026-09-24
---

Mobile-first é escrever o CSS partindo da tela pequena como caso padrão e, à medida que a tela cresce, acrescentar o que couber — usando [[media-query|media queries]] de `min-width`. O caminho inverso, desenhar para o monitor e remendar depois para o celular, dá mais trabalho, porque desfazer decisões de layout é mais difícil do que adicionar.

## Em uma frase

Mobile-first escreve para a tela pequena primeiro e soma regras com `min-width` conforme a tela cresce.

## O que precisa saber

Sem a meta tag `<meta name="viewport" content="width=device-width, initial-scale=1.0">`, o celular finge ter cerca de 980px de largura e nenhuma media query de tela pequena chega a disparar — o CSS responsivo fica correto e sem efeito nenhum. A tela pequena não perdoa excesso: o que sobra depois de decidir o que cabe em 360px costuma ser exatamente o essencial.

## Erros comuns

- Esquecer a meta viewport — sem ela, o navegador móvel monta a página numa largura imaginária de ~980px e depois encolhe tudo, resultando em texto minúsculo, e nenhuma media query de tela pequena é acionada.
- Misturar `width: 100%` com `padding` fixo sem `box-sizing: border-box`, criando rolagem horizontal — o padding soma por fora da largura declarada por padrão.

## Onde aparece

- Aula 14 — *Mobile-first: o MVP no celular de quem vai validar* `aulas/programacao-front-end/landing-page-mvp/14-mobile-first/canonica.md`
- Aula 4 — *Blueprint · Espaço Delas* `aulas/tcc/blueprint-tcc/04-blueprint-espaco-delas/canonica.md` — sistema web responsivo mobile-first, usável a partir de 320px.
- Aula 8 — *Blueprint · Lumina* `aulas/tcc/blueprint-tcc/08-blueprint-lumina/canonica.md` — aplicativo web mobile-first, otimizado para telas de até 448px.
- Conceitos vizinhos: [[media-query]], [[box-model]]

## Fontes

- Conteúdo autoral da Aula 14 (modo_origem: tema), sem fonte externa direta — meta viewport, media query de `min-width` e rolagem horizontal.
