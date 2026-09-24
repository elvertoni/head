---
conceito: classList.toggle
slug: classlist
disciplina: programacao-front-end
tipo: conceito
aka: [classList, alternar classe]
status: rascunho
fontes: []
aulas: [16]
atualizado_em: 2026-09-24
---

`elemento.classList.toggle("nome")` alterna uma classe CSS: se o elemento não a tem, ela é adicionada; se já tem, é removida. Uma linha cobre abrir e fechar, sem `if`. O [[javascript|JavaScript]] decide o estado; o CSS decide a aparência daquele estado — divisão que é o padrão em interfaces bem construídas.

## Em uma frase

`classList.toggle` alterna presença/ausência de uma classe numa linha só, sem `if`.

## O que precisa saber

O padrão típico é achar o elemento com `querySelector`, registrar um `addEventListener("click", ...)` e, dentro dele, chamar `classList.toggle`. Isso resolve, por exemplo, o menu que abre e fecha no celular: o CSS já define o que a classe `aberto` significa visualmente (`display: none` vira `display: flex`), e o JavaScript só liga e desliga o interruptor.

## Erros comuns

- Colocar o `<script>` no `<head>` ou no topo do `<body>`: ele roda antes de o elemento existir, `querySelector` devolve `null`, e o `addEventListener` seguinte estoura `Cannot read properties of null`. O `<script>` precisa ser a última coisa antes de `</body>`.

## Onde aparece

- Aula 16 — *JavaScript na conta certa: três comportamentos, vinte linhas* `aulas/programacao-front-end/landing-page-mvp/16-os-tres-javascripts/canonica.md`
- Conceitos vizinhos: [[javascript]], [[manipulacao-do-dom]]

## Fontes

- Conteúdo autoral da Aula 16 (modo_origem: tema), sem fonte externa direta — `querySelector`, `addEventListener` e `classList.toggle` no menu mobile.
