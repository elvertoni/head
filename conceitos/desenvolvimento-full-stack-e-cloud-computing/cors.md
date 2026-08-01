---
conceito: CORS
slug: cors
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [Cross-Origin Resource Sharing]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Desafio_ Desenvolvimento Front - End/01 - Aula 1 - Hands on_ Desenvolvimento Front - End - Contextualização - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

CORS é o mecanismo pelo qual um servidor declara quais origens podem ler respostas de requisições feitas por scripts do navegador. Ele configura uma exceção controlada à [[politica-de-mesma-origem]].

## Em uma frase

CORS permite compartilhamento explícito de recursos entre origens Web.

## O que precisa saber

Headers, preflight, métodos, cabeçalhos e credenciais compõem o contrato. CORS protege o navegador, não torna o endpoint público nem substitui [[autenticacao]] e [[autorizacao]].

## Erros comuns

- Usar wildcard com credenciais.
- Liberar o Origin refletido sem validação.
- Diagnosticar erro de CORS sem olhar a resposta do servidor.

## Onde aparece

- Desafio Desenvolvimento Front-End, Aula 1, páginas 2–5.
- Relaciona-se a [[origem-web]], [[politica-de-mesma-origem]], [[fetch-api]] e [[http]].

## Fontes

- Aula 1, páginas 2–5 dos slides: CORS e requisições entre origens.
