---
conceito: Chave de API
slug: chave-de-api
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [API key]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo III - Cloud Computing/Desenvolvimento Web/17 - Aula 17 - Projeto Web - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Chave de API é um identificador ou credencial usado para associar requisições a um projeto, aplicação ou cota. Sua exposição e seus privilégios precisam ser tratados conforme o serviço e o risco.

## Em uma frase

API key identifica ou autoriza uma integração com um serviço.

## O que precisa saber

Chaves públicas ainda exigem restrição por origem, serviço ou cota; chaves secretas não devem ir para o cliente. Rotação, revogação e [[protecao-de-credenciais]] são essenciais.

## Erros comuns

- Commitar chave secreta no repositório.
- Confundir identificação de projeto com autorização ampla.
- Não monitorar uso ou revogar chave comprometida.

## Onde aparece

- Desenvolvimento Web, Aula 17, páginas 3; Aula 18, página 3.
- Relaciona-se a [[firebase]], [[autenticacao]], [[protecao-de-credenciais]] e [[variaveis-de-ambiente]].

## Fontes

- Aula 17, página 3, e Aula 18, página 3 dos slides: chaves de API.
