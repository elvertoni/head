---
conceito: EJS
slug: ejs
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: entidade
aka: [Embedded JavaScript Templates]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Frameworks e Aplicações/03 - Aula 3 - Framework Express.js III - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

EJS é um motor de templates que combina dados e JavaScript para gerar HTML no servidor. Em aplicações [[expressjs]], ele pode renderizar uma visão a partir de um modelo e de dados preparados pelo controlador.

## Em uma frase

EJS gera HTML no servidor a partir de dados e templates.

## O que precisa saber

A visão deve receber dados necessários, escapar conteúdo não confiável e permanecer separada das regras de domínio. O padrão conversa com [[mvc]] e [[backend]].

## Erros comuns

- Inserir conteúdo externo sem escape e abrir XSS.
- Colocar consultas e regras complexas dentro do template.
- Confundir renderização de visão com uma API de dados.

## Onde aparece

- Frameworks e Aplicações, Aula 3, páginas 1–4.
- Relaciona-se a [[expressjs]], [[mvc]] e [[backend]].

## Fontes

- Aula 3, páginas 1–4 dos slides: templates EJS no Express.
