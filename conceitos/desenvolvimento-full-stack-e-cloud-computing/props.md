---
conceito: Props
slug: props
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [properties em React]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Projeto Front - End e Desenvolvimento Web/10 - Aula 10 - Componentes, Props e States I - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Props são valores fornecidos por um componente pai a um componente filho para configurar sua renderização ou comportamento. Elas formam parte do contrato de entrada e devem ser tratadas como dados recebidos.

## Em uma frase

Props passam dados e configuração entre componentes React.

## O que precisa saber

Props são somente leitura no componente que recebe; mudanças vêm do pai ou de callbacks. Elas diferem de [[state]], que pertence ao componente ou a um mecanismo de estado. [[componente-react]] usa props para composição e reutilização.

## Erros comuns

- Alterar props diretamente.
- Passar objetos enormes e acoplar componentes.
- Confundir prop callback com mudança automática de estado.

## Onde aparece

- Aulas 10–13 — Componentes, Props e States.
- Conecta [[react]], [[componente-react]], [[jsx]] e [[state]].

## Fontes

- Aula 10, páginas 2–5 dos slides: props e comunicação entre componentes.
