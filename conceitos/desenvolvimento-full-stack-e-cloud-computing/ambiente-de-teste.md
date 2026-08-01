---
conceito: Ambiente de teste
slug: ambiente-de-teste
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [test environment]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Frameworks e Aplicações/09 - Aula 9 - Ferramentas para Testar Back - End - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Ambiente de teste é uma configuração isolada e reproduzível de código, banco, variáveis, serviços e dados usada para executar verificações sem depender do ambiente de produção. Sua confiabilidade depende de controlar estado, migrações, dependências externas e limpeza entre execuções.

## Em uma frase

Ambiente de teste cria condições isoladas e repetíveis para verificar o sistema.

## O que precisa saber

Um ambiente pode usar banco temporário, fixtures, mocks ou serviços dedicados conforme o tipo de teste. [[testes-unitarios]], integração e ponta a ponta exigem graus diferentes de isolamento; [[jest]] e [[supertest]] executam verificações, mas não definem sozinhos o ambiente. Configuração explícita reduz “funciona na minha máquina”.

## Erros comuns

- Rodar teste contra banco de produção ou estado compartilhado.
- Não versionar migrações e configuração necessária.
- Deixar dados de um teste contaminarem o seguinte.

## Onde aparece

- Frameworks e Aplicações, Aula 9, páginas 2 e 4–5.
- Relaciona-se a [[testes-unitarios]], [[testes-de-integracao]], [[jest]], [[supertest]] e [[variaveis-de-ambiente]].

## Fontes

- Frameworks e Aplicações, Aula 9, slides sobre ferramentas e configuração de testes de backend.
