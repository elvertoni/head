---
conceito: MCP
slug: mcp
disciplina: inteligencia-artificial
tipo: conceito
aka: [Model Context Protocol, protocolo MCP]
status: vivo
fontes:
  - aulas/inteligencia-artificial/fundamentos-de-ia/20-mcp-model-context-protocol/canonica.md
  - lake/inteligencia-artificial/ia-coders/o-que-e-model-context-protocol-mcp.md
aulas: [20]
atualizado_em: 2026-06-15
---

MCP (Model Context Protocol) é um **protocolo aberto** (criado pela Anthropic em 2024) que padroniza como aplicações de IA se conectam a ferramentas, dados e serviços externos. É o **"USB da IA"**: em vez de programar cada integração na mão, qualquer IA que "fala MCP" conecta a qualquer ferramenta que "fala MCP".

## Em uma frase

O padrão (tipo USB/HTTP) que faz qualquer IA conectar a qualquer ferramenta sem integração na mão.

## O que precisa saber

Resolve o caos da integração ponto a ponto (N×N feita na mão, que não escala). Funciona por **cliente** (na IA) e **servidor** (no serviço): conecta-se uma vez, serve para todos. Um servidor MCP expõe **ferramentas** ([[tool-use]]) e **dados** à IA. Importante: MCP é **protocolo**, não uma IA — não pensa, só padroniza a comunicação, como o HTTP na web.

## Erros comuns

- Achar que "MCP é uma IA inteligente" — é um protocolo de comunicação.

## Onde aparece

- Aula 20 — *MCP — Model Context Protocol*
- Conceitos vizinhos: [[tool-use]], [[agente]], [[harness]]

## Fontes

- Canônica da Aula 20 (modo Material); transcrição ia-coders (lake).
