---
conceito: Agregação
slug: agregacao
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [agregação em modelo ER]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Modelagem de Banco de Dados/17 - Aula 17 - Modelo Entidade Relacionamento Estendido III - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Agregação trata um relacionamento e suas entidades participantes como uma unidade conceitual que pode participar de outro relacionamento. Ela permite representar relações entre fatos compostos sem perder a associação original.

## Em uma frase

Agregação permite relacionar uma associação inteira com outro elemento do domínio.

## O que precisa saber

Ela é um recurso do [[modelo-entidade-relacionamento]] estendido, usado quando um relacionamento precisa ser tratado como objeto de uma nova relação. A decisão deve preservar papéis, identidade e [[cardinalidade]] ao chegar ao [[modelo-logico]].

## Erros comuns

- Usar agregação para qualquer relacionamento complexo.
- Confundir agregação conceitual com soma ou agrupamento de valores.
- Esconder a relação original dentro de uma abstração sem nome.

## Onde aparece

- Aula 17 — Modelo Entidade Relacionamento Estendido III.
- Conecta [[relacionamento]], [[modelo-entidade-relacionamento]], [[cardinalidade]] e [[modelo-logico]].

## Fontes

- Aula 17, slides: agregação e relacionamentos em modelos estendidos.
