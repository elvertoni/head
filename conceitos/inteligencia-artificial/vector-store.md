---
conceito: Vector store
slug: vector-store
disciplina: inteligencia-artificial
tipo: conceito
aka: [banco vetorial, banco de vetores, vector database]
status: vivo
fontes:
  - aulas/inteligencia-artificial/fundamentos-de-ia/17-chunking-embeddings-e-vector-stores/canonica.md
  - lake/inteligencia-artificial/elite-wiki/arquitetura/blueprint-sistema-rag-para-suporte-a-alunos.md
aulas: [17]
atualizado_em: 2026-06-15
---

Vector store é o banco que guarda os [[embeddings]] dos chunks e responde rápido à pergunta "quais são os mais parecidos com este vetor?". É onde o [[rag]] busca na hora da consulta. Como compara **vetores** (significado) e não palavras, acha "encerrar plano" quando você pergunta "cancelar assinatura". Exemplos: FAISS, Qdrant, pgvector.

## Em uma frase

O banco que guarda embeddings e devolve os mais parecidos com a consulta — busca por significado.

## Onde aparece

- Aula 17 — *Chunking, embeddings e vector stores*
- Conceitos vizinhos: [[rag]], [[chunking]], [[embeddings]]

## Fontes

- `blueprint-sistema-rag-para-suporte-a-alunos.md` (elite-wiki) — opções de banco vetorial.
