---
conceito: useState
slug: use-state
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [React useState]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Projeto Front - End e Desenvolvimento Web/13 - Aula 13 - Componentes, Props e States IV - Apostila (Slides).pdf"
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Projeto Front - End e Desenvolvimento Web/25 - Aula 25 - Gerenciamento Ciclos de Vida de Componentes_ Classes e Hooks I - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

`useState` é o hook do React que declara estado local em um componente funcional e devolve o valor atual junto com uma função de atualização. Atualizar o estado agenda uma nova renderização; não se deve alterar diretamente o valor anterior.

## Em uma frase

`useState` mantém estado local reativo em componentes funcionais do React.

## O que precisa saber

O inicializador pode ser um valor ou uma função avaliada sob demanda. Para atualizações dependentes do valor anterior, use a forma funcional; para objetos e arrays, produza uma nova referência. O estado pertence ao componente e pode ser elevado quando vários componentes precisam compartilhar a fonte.

## Erros comuns

- Mutar objeto ou array armazenado no estado.
- Ler um valor antigo em várias atualizações seguidas sem forma funcional.
- Usar estado para duplicar dados que podem ser derivados.

## Onde aparece

- Projeto Front-End e Desenvolvimento Web, Aula 13, página 3; Aula 25, página 5.
- Relaciona-se a [[hooks-react]], [[react]], [[state]] e [[lifting-state-up]].

## Fontes

- Projeto Front-End e Desenvolvimento Web, Aula 13, slide sobre estados.
- Projeto Front-End e Desenvolvimento Web, Aula 25, slide sobre `useState`.
