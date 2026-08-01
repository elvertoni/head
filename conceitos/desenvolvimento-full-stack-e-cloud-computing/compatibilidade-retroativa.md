---
conceito: Compatibilidade retroativa
slug: compatibilidade-retroativa
disciplina: desenvolvimento-full-stack-e-cloud-computing
tipo: conceito
aka: [backward compatibility, compatibilidade para trás]
status: rascunho
fontes:
  - "lake/desenvolvimento-full-stack-e-cloud-computing/Módulo II - Desenvolvimento Full Stack/Arquitetura e Programação/32 - Aula 32 - Evolução e Gestão do Ciclo de Vida de uma API III - Apostila (Slides).pdf"
aulas: []
atualizado_em: 2026-08-01
---

Compatibilidade retroativa é a capacidade de uma nova versão preservar o comportamento esperado por consumidores existentes. Em APIs, envolve caminhos, formatos, códigos, autenticação e semântica dos dados.

## Em uma frase

Compatibilidade retroativa permite evoluir sem quebrar clientes atuais.

## O que precisa saber

Adicionar campos opcionais costuma ser menos arriscado que renomear ou remover campos. Testes de contrato, telemetria e [[versionamento-de-api]] ajudam a identificar o impacto real.

## Erros comuns

- Considerar uma mudança semântica compatível porque o JSON ainda é válido.
- Remover enum, campo ou código usado por clientes.
- Não testar consumidores representativos.

## Onde aparece

- Arquitetura e Programação, Aula 32, página 4.
- Relaciona-se a [[versionamento-de-api]], [[ciclo-de-vida-de-api]] e [[deprecacao-de-api]].

## Fontes

- Aula 32, página 4 dos slides: compatibilidade em evolução de APIs.
