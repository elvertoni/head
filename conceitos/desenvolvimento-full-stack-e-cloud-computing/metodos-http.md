---
conceito: Métodos HTTP
slug: metodos-http
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [verbos HTTP, métodos de requisição HTTP]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Projeto Front - End e Desenvolvimento Web/02 - Aula 2 - Introdução ao Front - End II - Apostila (Slides).pdf"
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Desafio_ Desenvolvimento Front - End/01 - Aula 1 - Hands on_ Desenvolvimento Front - End - Contextualização - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Métodos HTTP são verbos que expressam a intenção de uma requisição sobre um recurso Web, como consultar, criar, substituir ou remover uma representação. Além do nome, cada método tem semântica própria sobre segurança, idempotência, corpo e efeitos esperados, orientando contratos de [[api]] e [[http]].

## Em uma frase

Métodos HTTP descrevem o tipo e a semântica da operação solicitada a um recurso.

## O que precisa saber

GET costuma recuperar uma representação; POST pode criar ou disparar processamento; PUT substitui uma representação; PATCH aplica alteração parcial; DELETE solicita remoção. A semântica deve ser coerente com códigos de resposta e [[idempotencia-http]]. Métodos não substituem autorização nem validação de entrada.

## Erros comuns

- Usar GET para uma operação que altera estado.
- Tratar todos os métodos como igualmente idempotentes.
- Escolher o verbo sem definir o contrato do recurso e seus efeitos.

## Onde aparece

- Projeto Front-End e Desenvolvimento Web, Aula 2, página 4.
- Desafio Front-End, Aula 1, página 5.
- Relaciona-se a [[http]], [[api]], [[api-rest]], [[codigos-de-status-http]] e [[idempotencia-http]].

## Fontes

- Projeto Front-End e Desenvolvimento Web, Aula 2, slide sobre métodos HTTP.
- Desafio Front-End, Aula 1, slide de requisições Web.
