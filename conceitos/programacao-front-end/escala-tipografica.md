---
conceito: Escala tipográfica
slug: escala-tipografica
disciplina: programacao-front-end
tipo: conceito
aka: [type scale]
status: rascunho
fontes: []
aulas: [11]
atualizado_em: 2026-09-24
---

Escala tipográfica é um conjunto pequeno e fixo de tamanhos de fonte, com saltos claros entre eles, usado na página inteira. Cinco degraus bastam. A regra: se dois textos têm importância diferente, os tamanhos precisam ser visivelmente diferentes; se têm a mesma importância, precisam ser exatamente iguais.

## Em uma frase

Escala tipográfica é um punhado fixo de tamanhos — não um chute de tamanho a cada elemento.

## O que precisa saber

Quem escolhe tamanho "na base do acho que tá bom" acaba com sete tamanhos quase iguais e uma página que parece desalinhada sem se saber dizer por quê. Uma escala típica de landing page: 14px (legenda), 16px (parágrafo — o padrão de todo navegador), 20px (subtítulo), 28px (`h2`), 44px (`h1`/headline). Ela normalmente é declarada como [[variavel-css|variável CSS]] em `:root`, junto com a paleta de cores.

## Erros comuns

- Fixar texto de leitura abaixo de 16px — quem aumentou a fonte do celular fez isso porque precisa, e a página que ignora essa escolha simplesmente não é lida por essa pessoa.

## Onde aparece

- Aula 11 — *Cor e tipografia: a marca em seis linhas de CSS* `aulas/programacao-front-end/landing-page-mvp/11-cor-e-tipografia/canonica.md`
- Conceitos vizinhos: [[variavel-css]], [[html-semantico]]

## Fontes

- Conteúdo autoral da Aula 11 (modo_origem: tema), sem fonte externa direta — escala de cinco tamanhos e cargo de cada cor da paleta.
