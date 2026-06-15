---
conceito: RAG
slug: rag
disciplina: inteligencia-artificial
tipo: conceito
aka: [retrieval-augmented generation, geração aumentada por recuperação, recuperação com geração aumentada]
status: vivo
fontes:
  - lake/inteligencia-artificial/elite-wiki/arquitetura/blueprint-sistema-rag-para-suporte-a-alunos.md
  - lake/inteligencia-artificial/ia-master
aulas: [16, 17]
atualizado_em: 2026-06-15
---

RAG é a técnica de dar ao modelo de linguagem o conteúdo certo na hora da pergunta, em vez de esperar que ele já "saiba" a resposta. Antes de o [[llm]] gerar o texto, um sistema de busca vai num acervo próprio (PDFs, transcrições, documentação), pesca os trechos mais relevantes para aquela pergunta e cola esses trechos no contexto junto com a pergunta. O modelo então responde olhando para esse material fresco — não só para o que aprendeu no treino, que tem [[cutoff|data de corte]] e não conhece o seu conteúdo privado.

## Em uma frase

Buscar os trechos certos do seu acervo e entregá-los ao [[llm]] junto com a pergunta, para ele responder com base neles em vez de só pela memória do treino.

## O que precisa saber

RAG resolve duas dores do LLM puro: ele não conhece o seu conteúdo específico, e o que ele sabe parou na [[cutoff|data de corte]] do treino. As alternativas são piores para a maioria dos casos — fine-tuning é caro, lento e perde flexibilidade; jogar tudo no prompt esbarra no limite de contexto. RAG é barato, rápido de iterar e **auditável**: você sempre sabe de qual documento veio a resposta.

O sistema tem duas metades. A primeira roda **antes**, uma vez por material: o pipeline de ingestão quebra cada documento em pedaços ([[chunking]]), transforma cada pedaço em um vetor de números que captura seu significado ([[embeddings]]) e guarda tudo num banco que busca por proximidade de significado ([[vector-store]]). A segunda roda **a cada pergunta**: a pergunta também vira embedding, o banco devolve os chunks mais próximos, e esses chunks entram no contexto do LLM junto com a pergunta. Montar esse contexto bem é exatamente o trabalho de [[context-engineering]].

```
INGESTÃO (1x por material)          CONSULTA (a cada pergunta)
documento → chunking                 pergunta → embedding
       → embeddings                        → busca no vector-store
       → vector-store                      → top-k chunks + pergunta → LLM → resposta
```

O ponto que os alunos costumam errar: RAG **não treina** o modelo. Nada nos pesos do LLM muda. Você está montando o prato que o modelo vai comer naquela pergunta, não reeducando o cozinheiro.

## Erros comuns

- **Achar que RAG "ensina" o modelo.** Não muda peso nenhum; é busca + contexto. Quem muda pesos é fine-tuning.
- **Pular a auditoria da fonte.** A vantagem do RAG é saber de onde veio a resposta. Se a resposta não cita o chunk de origem, você perdeu metade do valor.
- **Chunk do tamanho errado.** Pedaço grande demais dilui o significado no [[embeddings|embedding]]; pequeno demais perde o contexto. É decisão de projeto, não default — ver [[chunking]].
- **Confundir "não achou" com "alucinou".** Se o vector-store não devolve trecho relevante, o LLM pode inventar. RAG reduz [[alucinacoes]], não elimina — depende da qualidade da recuperação.

## Onde aparece

- Aula 16 — *RAG — recuperação com geração aumentada* (conceito central)
- Aula 17 — *Chunking, embeddings e vector stores* (a mecânica da ingestão)
- Conceitos vizinhos: [[chunking]], [[embeddings]], [[vector-store]], [[llm]], [[context-engineering]], [[alucinacoes]], [[cutoff]]

## Fontes

- `blueprint-sistema-rag-para-suporte-a-alunos.md` (elite-wiki) — arquitetura geral, por que RAG e não fine-tuning, stack (FAISS/Qdrant/pgvector).
- `lake/inteligencia-artificial/ia-master` — Imersão IA para Devs, material de origem das Aulas 16/17 (`.docx`, ainda a tratar).
