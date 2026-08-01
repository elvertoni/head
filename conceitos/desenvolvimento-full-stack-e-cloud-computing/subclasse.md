---
conceito: Subclasse
slug: subclasse
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [entidade subtipo]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Modelagem de Banco de Dados/15 - Aula 15 - Modelo Entidade Relacionamento Estendido - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Subclasse é uma entidade especializada que herda características da [[superclasse]] e acrescenta propriedades ou relações próprias. Uma ocorrência de subtipo mantém a identidade da entidade geral e participa das regras de especialização.

## Em uma frase

Subclasse representa um subtipo com identidade herdada e propriedades específicas.

## O que precisa saber

Subclasses são definidas por [[especializacao]] e podem ser exclusivas ou sobrepostas conforme o domínio. O [[modelo-entidade-relacionamento-estendido]] precisa registrar cobertura e restrições; o [[modelo-logico]] precisa escolher uma estratégia de persistência.

## Erros comuns

- Criar subclasse para cada estado temporário.
- Esquecer atributos herdados ou a chave da superclasse.
- Presumir que uma ocorrência pertence a apenas um subtipo.

## Onde aparece

- Aula 15 — Modelo Entidade Relacionamento Estendido.
- Conecta [[superclasse]], [[especializacao]], [[generalizacao]] e [[modelo-entidade-relacionamento-estendido]].

## Fontes

- Aula 15, slides: subclasses, herança e especialização.
