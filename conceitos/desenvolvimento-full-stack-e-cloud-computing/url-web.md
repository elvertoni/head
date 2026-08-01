---
conceito: URL Web
slug: url-web
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [Uniform Resource Locator]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/Desafio_ Desenvolvimento Front - End/01 - Aula 1 - Hands on_ Desenvolvimento Front - End - Contextualização - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

URL é a forma de identificar a localização e o modo de acesso a um recurso Web, combinando esquema, autoridade, caminho, consulta e fragmento. Ela é interpretada pelo cliente e pelo servidor segundo contratos distintos.

## Em uma frase

URL identifica um recurso e os parâmetros de acesso a ele.

## O que precisa saber

Codificação, normalização, origem e [[query-string]] afetam semântica e segurança. URLs são visíveis em histórico, logs e cabeçalhos; não devem carregar segredos.

## Erros comuns

- Montar URL por concatenação sem codificar parâmetros.
- Usar fragmento esperando que o servidor o receba.
- Colocar token, senha ou dado sensível na URL.

## Onde aparece

- Desafio Desenvolvimento Front-End, Aula 1, páginas 2–5.
- Relaciona-se a [[http]], [[query-string]], [[origem-web]] e [[parametros-de-rota]].

## Fontes

- Aula 1, páginas 2–5 dos slides: estrutura e uso de URLs.
