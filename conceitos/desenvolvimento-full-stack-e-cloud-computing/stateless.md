---
conceito: Stateless
slug: stateless
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [sem estado]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Arquitetura e Programação/05 - Aula 5 - Gerenciamento de Sessão e Controle de Cache - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Uma interação stateless não exige que o servidor preserve o contexto da requisição anterior para interpretar a atual. Cada requisição carrega as informações necessárias ou referencia um estado externo.

## Em uma frase

Stateless trata cada requisição sem depender de memória de sessão local.

## O que precisa saber

O modelo facilita escala horizontal e recuperação, mas não elimina estado do sistema. Tokens, banco ou cache podem manter estado fora do processo, em combinação com [[gerenciamento-de-sessao]].

## Erros comuns

- Achar que stateless significa ausência total de estado.
- Colocar dados sensíveis demais em tokens enviados pelo cliente.
- Ignorar revogação e expiração de credenciais.

## Onde aparece

- Arquitetura e Programação, Aula 5, páginas 2 e 5.
- Contrasta com [[stateful]] e relaciona-se a [[gerenciamento-de-sessao]].

## Fontes

- Aula 5, páginas 2 e 5 dos slides: modelos de estado e sessão.
