---
conceito: Origem Web
slug: origem-web
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [Web origin]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Desafio_ Desenvolvimento Front - End/01 - Aula 1 - Hands on_ Desenvolvimento Front - End - Contextualização - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Origem Web é a combinação de esquema, host e porta que identifica o contexto de segurança de um recurso. URLs com origens diferentes podem estar sujeitas a restrições de acesso entre documentos.

## Em uma frase

Origem é esquema, host e porta usados para delimitar confiança na Web.

## O que precisa saber

Subdomínio, porta e protocolo podem mudar a origem. [[politica-de-mesma-origem]] e [[cors]] usam esse conceito para controlar requisições e leitura de respostas.

## Erros comuns

- Considerar dois domínios parecidos como mesma origem.
- Confundir origem com site ou domínio registrável.
- Liberar origens dinamicamente sem validar valores.

## Onde aparece

- Desafio Desenvolvimento Front-End, Aula 1, páginas 2–5.
- Relaciona-se a [[politica-de-mesma-origem]], [[cors]] e [[url-web]].

## Fontes

- Aula 1, páginas 2–5 dos slides: origem e segurança Web.
