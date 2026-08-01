---
conceito: State em React
slug: state
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [estado de componente]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Projeto Front - End e Desenvolvimento Web/10 - Aula 10 - Componentes, Props e States I - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

State é o conjunto de dados mutáveis que influencia a renderização de um componente React. Quando atualizado pela API apropriada, ele provoca novo cálculo da interface e preserva a separação entre entrada e estado local.

## Em uma frase

State representa dados que mudam e determinam o que o componente renderiza.

## O que precisa saber

State não deve ser mutado diretamente; atualizações podem ser agrupadas e depender do valor anterior. [[props]] passam dados entre componentes, enquanto [[componente-react]] decide onde o estado deve viver. Estado derivado e duplicado aumentam inconsistência.

## Erros comuns

- Mutar array ou objeto no lugar.
- Colocar estado no componente errado e criar prop drilling desnecessário.
- Guardar no state o que pode ser calculado das props.

## Onde aparece

- Aulas 10–13 e 22–24 — States e gerenciamento de estado.
- Conecta [[react]], [[componente-react]], [[props]] e hooks.

## Fontes

- Aula 10, páginas 2–5 dos slides: state e renderização.
