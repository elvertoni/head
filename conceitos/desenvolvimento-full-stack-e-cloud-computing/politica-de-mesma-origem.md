---
conceito: Política de mesma origem
slug: politica-de-mesma-origem
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [Same-Origin Policy, SOP]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Desafio_ Desenvolvimento Front - End/01 - Aula 1 - Hands on_ Desenvolvimento Front - End - Contextualização - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Política de mesma origem é um isolamento de segurança que restringe como um documento ou script acessa recursos de outra [[origem-web]]. Ela limita leitura e interação cruzada para reduzir vazamento de dados.

## Em uma frase

Same-Origin Policy separa contextos Web que não compartilham origem.

## O que precisa saber

Exceções controladas incluem [[cors]], postMessage e recursos incorporados específicos. A política não substitui autenticação nem impede todo envio de requisição entre origens.

## Erros comuns

- Achar que SOP impede qualquer requisição cruzada.
- Usar CORS como autorização de usuário.
- Liberar credenciais para qualquer origem.

## Onde aparece

- Desafio Desenvolvimento Front-End, Aula 1, páginas 2–5.
- Relaciona-se a [[origem-web]], [[cors]], [[fetch-api]] e [[xss]].

## Fontes

- Aula 1, páginas 2–5 dos slides: política de mesma origem.
