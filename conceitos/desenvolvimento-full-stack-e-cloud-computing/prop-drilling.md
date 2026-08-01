---
conceito: Prop drilling
slug: prop-drilling
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [passagem prop em cadeia]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Projeto Front - End e Desenvolvimento Web/22 - Aula 22 - Gerenciamento Avançado de Estados com React I - Apostila (Slides).pdf"
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Projeto Front - End e Desenvolvimento Web/23 - Aula 23 - Gerenciamento Avançado de Estados com React II - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Prop drilling é a passagem repetitiva de dados por componentes intermediários que não usam esses dados, apenas para que um descendente os receba. Em React, pode ser aceitável em árvores pequenas, mas torna limites e mudanças difíceis quando a cadeia cresce.

## Em uma frase

Prop drilling é transportar props por componentes intermediários até um componente distante.

## O que precisa saber

O problema aparece quando um estado precisa atravessar muitos níveis. [[lifting-state-up]] pode manter uma fonte comum; [[use-context]] pode reduzir passagem em certos casos; composição ou uma store também podem ser adequadas. A solução depende da frequência, escopo e semântica do dado.

## Erros comuns

- Tratar qualquer passagem de props como problema.
- Criar contexto global para um dado usado por dois componentes próximos.
- Esconder dependências sem melhorar a arquitetura.

## Onde aparece

- Projeto Front-End e Desenvolvimento Web, Aulas 22–23, páginas 2–3.
- Relaciona-se a [[react]], [[props]], [[lifting-state-up]], [[use-context]] e [[state]].

## Fontes

- Projeto Front-End e Desenvolvimento Web, Aulas 22–23, slides sobre gerenciamento de estado.
