---
conceito: Instância de entidade
slug: instancia-de-entidade
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [ocorrência de entidade]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Modelagem de Banco de Dados/09 - Aula 9 - Entidade e Atributos - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

Instância de entidade é uma ocorrência concreta de uma entidade em determinado momento, com seus valores de atributos. Se entidade é o tipo Pedido, cada pedido registrado é uma instância desse tipo.

## Em uma frase

Instância é uma ocorrência identificável de uma entidade.

## O que precisa saber

A [[entidade]] descreve o conjunto ou conceito; a instância corresponde ao registro individual. Seus valores precisam respeitar [[dominio-de-atributo]] e sua identidade costuma ser garantida por uma [[chave-primaria]] no [[modelo-relacional]].

## Erros comuns

- Usar o nome da classe como se fosse um registro específico.
- Presumir que dois registros iguais são necessariamente a mesma instância.
- Ignorar a identidade ao modelar atualizações e vínculos.

## Onde aparece

- Aula 9 — Entidade e Atributos.
- Conecta [[entidade]], [[atributo]], [[chave-primaria]] e [[modelo-relacional]].

## Fontes

- Aula 9, slides: entidade, ocorrência e identificação.
