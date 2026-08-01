---
conceito: useContext
slug: use-context
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [React Context]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Projeto Front - End e Desenvolvimento Web/23 - Aula 23 - Gerenciamento Avançado de Estados com React II - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

useContext é o hook React que permite ler um valor fornecido por um contexto sem repassar props manualmente por cada componente intermediário.

## Em uma frase

useContext compartilha dependência por uma árvore de componentes.

## O que precisa saber

Contexto é adequado para temas, identidade e configurações relativamente estáveis. Estado muito mutável pode causar re-renderização ampla; composição ou store dedicada podem ser melhores.

## Erros comuns

- Usar Context para todo estado da aplicação.
- Criar valor novo a cada render e invalidar consumidores desnecessariamente.

## Onde aparece

- Aula 23 — Gerenciamento avançado de estado React.

## Fontes

- Aula 23, páginas 1–3 dos slides: Context e useContext.
