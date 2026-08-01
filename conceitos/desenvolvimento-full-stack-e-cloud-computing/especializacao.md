---
conceito: Especialização
slug: especializacao
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [especialização de entidades]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Modelagem de Banco de Dados/15 - Aula 15 - Modelo Entidade Relacionamento Estendido - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Especialização é o processo de definir subentidades mais específicas a partir de uma entidade geral, acrescentando propriedades ou restrições próprias. Ela representa diferenças relevantes entre subconjuntos do domínio.

## Em uma frase

Especialização divide uma entidade geral em subtipos com características próprias.

## O que precisa saber

A entidade geral é a [[superclasse]] e cada subtipo é uma [[subclasse]]. A modelagem deve definir se a cobertura é total ou parcial e se os subtipos são disjuntos ou sobrepostos. [[generalizacao]] descreve o movimento inverso de abstração.

## Erros comuns

- Criar subtipo para cada valor de um atributo sem comportamento distinto.
- Omitir se uma instância pode pertencer a mais de um subtipo.
- Usar herança para resolver apenas diferenças de apresentação.

## Onde aparece

- Aulas 15–17 — Modelo Entidade Relacionamento Estendido.
- Conecta [[generalizacao]], [[superclasse]], [[subclasse]] e herança em modelagem de dados.

## Fontes

- Aula 15, slides: especialização, subtipos e entidade geral.
