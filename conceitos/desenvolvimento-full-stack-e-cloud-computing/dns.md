---
conceito: DNS
slug: dns
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [Domain Name System, sistema de nomes de domínio]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Arquitetura e Programação/01 - Aula 1 - Arquitetura de Uma Aplicação Web e o Formato Json - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

DNS é o sistema distribuído que traduz nomes de domínio em endereços e outros registros usados na comunicação de rede. Ele separa o nome amigável usado pelo cliente da localização técnica do serviço.

## Em uma frase

DNS resolve nomes de domínio para localizar serviços na rede.

## O que precisa saber

Resolução envolve caches, servidores autoritativos e registros como A, AAAA e CNAME. Uma aplicação Web normalmente depende de DNS antes de estabelecer [[https]] ou [[http]].

## Erros comuns

- Tratar DNS como um banco de dados instantaneamente consistente.
- Ignorar TTL e caches ao alterar um domínio.
- Confundir falha de DNS com falha do servidor de aplicação.

## Onde aparece

- Arquitetura e Programação, Aula 1, página 4.
- Relaciona-se a [[http]], [[https]] e [[tls]].

## Fontes

- Aula 1, página 4 dos slides: nomes e comunicação em aplicações Web.
