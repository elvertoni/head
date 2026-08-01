---
conceito: Proxy
slug: proxy-pattern
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [padrão Proxy]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Frameworks e Aplicações/16 - Aula 16 - Uso de MVC como Padrão de Projeto - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Proxy é um objeto substituto que controla ou acrescenta comportamento ao acesso a outro objeto ou serviço. Ele pode mediar autorização, cache, lazy loading, logging ou comunicação remota.

## Em uma frase

Proxy controla o acesso a um objeto por meio de uma interface compatível.

## O que precisa saber

O proxy deve preservar o contrato relevante e tornar custos ou efeitos observáveis quando necessário. Ele se relaciona a [[broker]], [[cache-de-entidades]] e segurança.

## Erros comuns

- Esconder uma chamada remota cara atrás de uma interface local.
- Aplicar autorização incompleta no proxy.
- Alterar semântica e tratamento de erros sem documentar.

## Onde aparece

- Frameworks e Aplicações, Aula 16, página 4.
- Relaciona-se a [[padroes-de-projeto]], [[broker]] e [[cache-de-entidades]].

## Fontes

- Aula 16, página 4 dos slides: padrão Proxy.
