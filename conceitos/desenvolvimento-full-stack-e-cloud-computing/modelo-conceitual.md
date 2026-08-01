---
conceito: Modelo conceitual
slug: modelo-conceitual
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [modelo conceitual de dados]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Modelagem de Banco de Dados/06 - Aula 6 - Modelo Entidade Relacionamento II - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Modelo conceitual descreve entidades, atributos, relacionamentos e regras do domínio sem depender de um SGBD específico. Seu objetivo é validar significado e escopo com as pessoas envolvidas.

## Em uma frase

O modelo conceitual explica o domínio antes de escolher tabelas e tecnologia.

## O que precisa saber

O [[modelo-entidade-relacionamento]] é uma forma de construir o modelo conceitual; a [[uml]] oferece outra notação. Depois, o modelo pode ser transformado por [[mapeamento-conceitual-logico]] em um [[modelo-logico]]. A qualidade depende de regras do negócio, não da quantidade de símbolos.

## Erros comuns

- Colocar tipos físicos, índices e detalhes de SQL no modelo conceitual.
- Confundir entidade com tela ou relatório.
- Validar o diagrama apenas com a equipe técnica.

## Onde aparece

- Aulas 5–8 — Modelo Entidade Relacionamento.
- Conecta [[modelagem-de-dados]], [[modelo-entidade-relacionamento]], [[modelo-logico]] e [[diagrama-entidade-relacionamento]].

## Fontes

- Aula 6, slides: papel do modelo conceitual e representação de entidades e relações.
