---
conceito: Not found no Next.js
slug: not-found-nextjs
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [not-found.tsx, notFound]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Frameworks, Programação e Estratégias/13 - Aula 13 - Roteamento Avançado I - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Not found no Next.js é o tratamento de uma rota ou recurso inexistente por meio de uma interface e do status apropriados. Ele separa ausência esperada de falha interna da aplicação.

## Em uma frase

Not found representa corretamente um recurso que não existe.

## O que precisa saber

O tratamento deve preservar segurança, navegação e informação suficiente ao usuário. Rotas dinâmicas, [[parametros-de-rota]] e [[nextjs]] precisam definir quando um id inválido vira 404.

## Erros comuns

- Responder 200 para uma página inexistente.
- Revelar se um recurso protegido existe.
- Confundir ausência com erro de banco ou falha de rede.

## Onde aparece

- Frameworks, Programação e Estratégias, Aula 13, página 5.
- Relaciona-se a [[nextjs]], [[roteamento]] e [[roteamento-dinamico]].

## Fontes

- Aula 13, página 5 dos slides: tratamento de not found.
