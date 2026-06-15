---
conceito: Embeddings
slug: embeddings
disciplina: inteligencia-artificial
tipo: conceito
aka: [vetores de significado, representação vetorial, vector embeddings]
status: vivo
fontes:
  - lake/inteligencia-artificial/elite-wiki/arquitetura/blueprint-sistema-rag-para-suporte-a-alunos.md
aulas: [10, 17]
atualizado_em: 2026-06-15
---

Embedding é transformar um texto em uma lista de números (um vetor) que captura o seu significado, de um jeito que textos com sentido parecido ficam com vetores próximos. É como a máquina representa significado para poder **comparar** textos por proximidade em vez de por palavras iguais — a base da busca semântica que faz o [[rag]] funcionar.

## Em uma frase

Converter texto em vetores onde proximidade numérica = proximidade de significado, permitindo buscar por sentido e não por palavra exata.

## O que precisa saber

A intuição: cada texto vira um ponto num espaço de muitas dimensões. "Cachorro" e "cão" caem perto; "cachorro" e "imposto de renda", longe. Buscar então é geometria — pega o vetor da pergunta e procura os pontos mais próximos. Por isso a busca acha "como cancelar minha assinatura" mesmo num documento que diz "encerramento de plano": as palavras diferem, o significado não, e os vetores ficam vizinhos.

No pipeline de um [[rag]], cada chunk produzido pelo [[chunking]] vira um embedding e é guardado no [[vector-store]]. Na hora da pergunta, a própria pergunta vira embedding e o banco devolve os chunks de vetor mais próximo. Embeddings são o mesmo mecanismo por trás de como o [[llm]] representa [[tokens]] internamente — daí a Aula 10 trazê-los antes.

## Erros comuns

- **Confundir embedding com o LLM.** Gerar embeddings é um modelo separado e barato; não é o modelo que escreve a resposta.
- **Misturar modelos de embedding.** Vetores de modelos diferentes não são comparáveis. Indexar e consultar têm que usar o mesmo modelo.
- **Achar que busca vetorial é busca por palavra-chave.** É por significado; pode acertar sem nenhuma palavra em comum (e errar quando o significado é ambíguo).

## Onde aparece

- Aula 10 — *Tokens, embeddings e vetores*
- Aula 17 — *Chunking, embeddings e vector stores*
- Conceitos vizinhos: [[rag]], [[chunking]], [[vector-store]], [[llm]], [[tokens]]

## Fontes

- `blueprint-sistema-rag-para-suporte-a-alunos.md` (elite-wiki) — etapa de embedding no pipeline de ingestão.
