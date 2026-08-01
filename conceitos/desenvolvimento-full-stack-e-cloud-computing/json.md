---
conceito: JSON
slug: json
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [JavaScript Object Notation]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Arquitetura e Programação/04 - Aula 4 - Arquitetura de Uma Aplicação Web e o Formato Json IV - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-07-31
---

JSON é um formato textual de troca de dados baseado em objetos e arrays, com valores de texto, número, booleano e nulo. Sua simplicidade facilita comunicação entre serviços, mas o contrato ainda precisa definir tipos, campos obrigatórios e compatibilidade.

## Em uma frase

JSON representa dados estruturados em texto para troca entre sistemas.

## O que precisa saber

JSON aparece em APIs, arquivos e mensagens; [[api]] e [[api-rest]] precisam de contratos claros para interpretar seus documentos. Sintaxe válida não garante semântica, validação ou segurança. Campos desconhecidos e versões devem ser tratados explicitamente.

## Erros comuns

- Confundir JSON válido com resposta correta.
- Não validar tipos, campos obrigatórios ou tamanho.
- Expor dados sensíveis no payload.

## Onde aparece

- Aulas 1–4 — Arquitetura de uma aplicação Web e formato JSON.
- Conecta [[api]], [[api-rest]], [[http]] e [[rest]].

## Fontes

- Aula 4, páginas 1–5 dos slides: estrutura e uso de JSON.
