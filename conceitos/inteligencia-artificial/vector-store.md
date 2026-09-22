---
conceito: Vector store
slug: vector-store
disciplina: inteligencia-artificial
tipo: conceito
aka: [banco vetorial, banco de vetores, vector database]
status: vivo
fontes:
  - lake/inteligencia-artificial/elite-wiki/arquitetura/blueprint-sistema-rag-para-suporte-a-alunos.md
aulas: [17]
atualizado_em: 2026-06-15
---

Vector store é o banco que guarda os [[embeddings]] dos chunks e responde rápido à pergunta "quais são os mais parecidos com este vetor?". É onde o [[rag]] busca na hora da consulta. Como compara **vetores** (significado) e não palavras, acha "encerrar plano" quando você pergunta "cancelar assinatura". Exemplos: FAISS, Qdrant, pgvector.

## Em uma frase

O banco que guarda embeddings e devolve os mais parecidos com a consulta — busca por significado.

## O que precisa saber

O vector store guarda o embedding, o identificador do chunk e metadados que ajudam a filtrar a busca. Na consulta, transforma a pergunta em vetor e devolve os vizinhos mais próximos segundo uma medida de distância. A qualidade depende de [[chunking]], do modelo de [[embeddings]], dos filtros e da quantidade de resultados recuperados. O banco encontra trechos relevantes; não garante sozinho que a resposta esteja correta.

## Erros comuns

- Misturar embeddings produzidos por modelos incompatíveis no mesmo índice.
- Recuperar trechos sem filtros ou contexto suficiente e enviar ruído ao [[rag]].
- Confundir proximidade vetorial com verdade ou relevância garantida.

## Onde aparece

- Aula 17 — *Chunking, embeddings e vector stores*
- `aulas/inteligencia-artificial/fundamentos-de-ia/17-chunking-embeddings-e-vector-stores/canonica.md`
- Conceitos vizinhos: [[rag]], [[chunking]], [[embeddings]]

## Fontes

- `blueprint-sistema-rag-para-suporte-a-alunos.md` (elite-wiki) — opções de banco vetorial.
