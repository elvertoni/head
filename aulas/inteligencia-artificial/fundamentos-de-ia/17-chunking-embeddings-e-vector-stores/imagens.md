# Brief de imagem — Aula 17: Chunking, Embeddings e Vector Stores

> Neutro de plataforma. Imagem só entra com justificativa pedagógica (teste anti-decoração). Final web ≤500 KB em `img/`; original pesado fica no `lake/` (fora do git).

## 1. O pipeline de ingestão do RAG

- **secao:** Desenvolvimento › Depois: virar vetor e guardar (fallback do diagrama-progressivo)
- **objetivo:** Mostrar a esteira documento → chunks → embeddings → vector store, e a busca na hora da pergunta. Amarra as três peças num quadro só.
- **alt:** Esteira: um documento é cortado em pedaços (chunks), cada pedaço vira uma lista de números (embedding), os vetores entram num banco (vector store); à parte, uma pergunta vira vetor e puxa os chunks mais próximos.
- **prompt:** A pipeline conveyor: a document sliced into chunk cards → each chunk becoming a small number list (embedding) → vectors stored into a database cylinder labeled "vector store". Below, a question turning into a vector with an arrow pulling the nearest chunks out. Flat vector, left-to-right, minimal text. 16:9.

## 2. (Opcional) Tamanho do chunk
- **alt:** Três versões do mesmo texto: chunk grande demais (borrado/misturado), pequeno demais (cortado no meio), e "na medida" (foco nítido).
- **prompt:** Three versions of the same paragraph: "grande demais" (blurry, many topics mixed), "pequeno demais" (a sentence cut mid-idea), "na medida" (clean focused chunk with a check). Flat vector, minimal text. 16:9.
