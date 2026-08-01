---
conceito: Requisição e resposta HTTP
slug: request-response
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [request/response, requisição e resposta HTTP]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Arquitetura e Programação/02 - Aula 2 - Arquitetura de Uma Aplicação Web e o Formato Json II - Apostila (Slides).pdf"
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Arquitetura e Programação/36 - Aula 36 - Conceitos Sobre API REST (métodos e HTTP Codes) IV - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

O modelo de requisição e resposta descreve a interação em que um cliente envia uma mensagem com método, destino, cabeçalhos e eventualmente corpo, enquanto o servidor devolve uma resposta com status, cabeçalhos e representação do resultado.

## Em uma frase

Uma requisição expressa a intenção do cliente; uma resposta comunica o resultado do servidor.

## O que precisa saber

O par é a unidade básica de [[http]] e sustenta contratos de [[api]] e [[api-rest]]. Métodos, códigos de status, autenticação, cache, idempotência e formatos como [[json]] precisam ser definidos em conjunto para que o contrato seja previsível.

## Erros comuns

- Tratar toda resposta `200` como sucesso de negócio ou ignorar códigos de erro e corpo de diagnóstico.
- Colocar dados sensíveis em URL, logs ou cabeçalhos sem considerar exposição e retenção.

## Onde aparece

Relaciona-se a [[http]], [[api]], [[api-rest]], [[metodos-http]], [[codigos-de-status-http]], [[query-string]] e [[parametros-de-rota]]. Ainda não há aula canônica registrada em `aulas`.

## Fontes

- Aulas 2 e 36 de Arquitetura e Programação, slides indicados no frontmatter.

