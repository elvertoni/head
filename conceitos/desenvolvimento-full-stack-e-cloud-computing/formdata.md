---
conceito: FormData
slug: formdata
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [API FormData]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo I - Padrões Web e Banco de Dados/JavaScript e Aplicações Práticas/05 - Aula 5 - Imersão JavaScript - Coleções e Funções - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

FormData representa pares de campos e arquivos de um formulário para envio em uma requisição Web. Ele preserva a codificação adequada para multipart/form-data quando usado com Fetch.

## Em uma frase

FormData empacota campos e arquivos para envio de formulário.

## O que precisa saber

Entradas ainda precisam ser validadas no cliente e no servidor. Ao usar FormData com Fetch, o navegador define o boundary do multipart; não se deve sobrescrever o cabeçalho de forma ingênua.

## Erros comuns

- Confiar na validação do navegador como autorização.
- Tentar enviar arquivo sem limites de tamanho e tipo.
- Definir Content-Type manualmente e quebrar o boundary.

## Onde aparece

- JavaScript e Aplicações Práticas, Aula 5, páginas 2–3.
- Relaciona-se a [[fetch-api]], [[validacao-de-formulario]] e [[web-apis-do-navegador]].

## Fontes

- Aula 5, páginas 2–3 dos slides: FormData e formulários.
