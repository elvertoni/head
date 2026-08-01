---
conceito: Modelo entidade-relacionamento estendido
slug: modelo-entidade-relacionamento-estendido
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [MER estendido, EER]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Modelagem de Banco de Dados/15 - Aula 15 - Modelo Entidade Relacionamento Estendido - Apostila (Slides).pdf"
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Modelagem de Banco de Dados/17 - Aula 17 - Modelo Entidade Relacionamento Estendido III - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Modelo entidade-relacionamento estendido amplia o [[modelo-entidade-relacionamento]] com abstrações como superclasses, subclasses, especialização, generalização e agregação. Ele representa domínios em que herança ou relações entre associações são relevantes.

## Em uma frase

MER estendido adiciona abstrações para modelar hierarquias e relações complexas.

## O que precisa saber

[[superclasse]], [[subclasse]], [[especializacao]], [[generalizacao]] e [[agregacao]] devem representar regras reais, não apenas reutilização de desenho. A transformação para o [[modelo-logico]] precisa preservar identidade, cobertura e participação.

## Erros comuns

- Usar herança para qualquer diferença de atributo.
- Omitir restrições de disjunção e cobertura.
- Achar que a notação estendida já define a implementação.

## Onde aparece

- Aulas 15–17 — Modelo Entidade Relacionamento Estendido.
- Amplia [[modelo-entidade-relacionamento]] e conecta [[superclasse]], [[subclasse]], [[especializacao]], [[generalizacao]] e [[agregacao]].

## Fontes

- Aula 15, slides: especialização, generalização e hierarquias.
- Aula 17, slides: agregação e extensões do modelo.
