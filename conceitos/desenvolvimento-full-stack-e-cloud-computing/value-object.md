---
conceito: Value object
slug: value-object
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [objeto-valor]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Frameworks e Aplicações/17 - Aula 17 - Uso de MVC como Padrão de Projeto II - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Value object é um objeto definido pelos seus valores e pelas regras que os tornam válidos, sem identidade própria relevante no domínio. Dois objetos com os mesmos valores podem ser considerados equivalentes.

## Em uma frase

Value object representa um valor do domínio, não uma entidade identificável.

## O que precisa saber

Imutabilidade e validação no construtor protegem invariantes. O conceito ajuda a separar valores como dinheiro ou endereço de [[entidade]] persistida.

## Erros comuns

- Dar identidade artificial a todo valor.
- Permitir estado inválido depois da criação.
- Confundir igualdade por valor com igualdade de referência em JavaScript.

## Onde aparece

- Frameworks e Aplicações, Aula 17, página 3.
- Relaciona-se a [[entidade]], [[modelagem-de-dados]] e [[orm]].

## Fontes

- Aula 17, página 3 dos slides: value objects.
