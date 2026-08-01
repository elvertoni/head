---
conceito: Flyweight
slug: flyweight
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [padrão Flyweight]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Frameworks e Aplicações/16 - Aula 16 - Uso de MVC como Padrão de Projeto - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Flyweight reduz consumo de memória compartilhando estado intrínseco entre muitos objetos semelhantes e mantendo o estado contextual fora deles. A economia depende de separar corretamente o que é comum do que varia.

## Em uma frase

Flyweight compartilha estado comum para reduzir objetos repetidos.

## O que precisa saber

Uma fábrica ou cache pode reutilizar instâncias, enquanto o cliente fornece o estado extrínseco. O padrão troca memória por complexidade e disciplina de ciclo de vida.

## Erros comuns

- Compartilhar estado que deveria ser independente.
- Criar cache sem limite ou política de remoção.
- Medir otimização sem evidência de pressão de memória.

## Onde aparece

- Frameworks e Aplicações, Aula 16, página 4.
- Relaciona-se a [[padroes-de-projeto]] e [[cache-de-entidades]].

## Fontes

- Aula 16, página 4 dos slides: padrão Flyweight.
