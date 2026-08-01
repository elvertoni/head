---
conceito: HTTP
slug: http
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [Hypertext Transfer Protocol]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Arquitetura e Programação/01 - Aula 1 - Arquitetura de Uma Aplicação Web e o Formato Json - Apostila (Slides).pdf"
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Arquitetura e Programação/02 - Aula 2 - Arquitetura de Uma Aplicação Web e o Formato Json II - Apostila (Slides).pdf"
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Arquitetura e Programação/36 - Aula 36 - Conceitos Sobre API REST (métodos e HTTP Codes) IV - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

HTTP é um protocolo de aplicação baseado em mensagens de requisição e resposta para comunicação entre clientes e servidores. Métodos, cabeçalhos, status e corpo expressam a intenção e o resultado de uma operação.

## Em uma frase

HTTP define como clientes e servidores trocam mensagens na Web.

## O que precisa saber

[[api]] e [[api-rest]] usam HTTP, mas o protocolo não define sozinho um bom desenho de domínio. Cookies, cache, autenticação, métodos e códigos precisam ser tratados com segurança e sem assumir que a rede é confiável.

## Erros comuns

- Confundir HTTP com HTML ou com uma API.
- Ignorar métodos idempotentes, cache e códigos de status.
- Enviar dados sensíveis sem transporte e autorização adequados.

## Onde aparece

- Aula 1 e Aulas 33–36 — Arquitetura Web e API REST.
- Conecta [[json]], [[api]], [[rest]], [[api-rest]] e cookies.

## Fontes

- Aula 1, páginas 2–4 dos slides: comunicação Web.
