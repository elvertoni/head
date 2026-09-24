---
conceito: Variável CSS (custom property)
slug: variavel-css
disciplina: programacao-front-end
tipo: conceito
aka: [custom property, propriedade customizada CSS]
status: rascunho
fontes: []
aulas: [11]
atualizado_em: 2026-09-24
---

Uma variável CSS é um apelido que se cria para um valor e se reutiliza no arquivo inteiro. Declara-se em `:root` — que representa a página toda — com dois hífens na frente do nome, e usa-se com `var()`. Trocar o valor em `:root` muda todos os lugares que pedem aquele apelido, e só eles.

## Em uma frase

Variável CSS é um apelido declarado uma vez em `:root` e reutilizado com `var()` no arquivo inteiro.

## O que precisa saber

Escrever a cor da marca direto em cada regra funciona até o dia em que ela muda: um "substituir tudo" no editor atinge também códigos parecidos que não eram a cor da marca (uma borda, uma sombra). Declarando em `:root`, a troca vira uma linha, e só os lugares que pediram aquele apelido mudam. `font-family` também deve ser variável, e como lista de alternativas terminando em `sans-serif` — fonte do Google Fonts é baixada no momento em que a página abre, e esse download falha com frequência em wi-fi de escola.

## Erros comuns

- Escrever o código da cor direto em cada regra em vez de usar `var()` — troca vira um "substituir tudo" arriscado, que pode atingir valores só parecidos.
- Declarar `font-family` com um nome só, sem alternativa — se a fonte não carregar, a página inteira aparece em Times New Roman sem nenhum CSS ter quebrado.

## Onde aparece

- Aula 11 — *Cor e tipografia: a marca em seis linhas de CSS* `aulas/programacao-front-end/landing-page-mvp/11-cor-e-tipografia/canonica.md`
- Conceitos vizinhos: [[escala-tipografica]], [[box-model]]

## Fontes

- Conteúdo autoral da Aula 11 (modo_origem: tema), sem fonte externa direta — `:root`, `var()` e fallback de `font-family`.
