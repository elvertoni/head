# Brief de imagem — Aula 16: RAG

> Neutro de plataforma. Imagem só entra com justificativa pedagógica (teste anti-decoração). Final web ≤500 KB em `img/`; original pesado fica no `lake/` (fora do git).

## 1. O fluxo do RAG (recuperar → gerar)

- **secao:** Desenvolvimento › As duas metades (fallback do diagrama-progressivo)
- **objetivo:** Mostrar o caminho pergunta → busca no acervo → trechos no contexto → resposta com fonte. Concretiza o que o RAG faz sem virar caixa-preta.
- **alt:** Fluxo: pergunta entra → busca num acervo de documentos (lupa) → trechos relevantes saem → entram no contexto junto da pergunta → LLM gera resposta citando a fonte.
- **prompt:** Horizontal flow diagram: a question → a magnifying glass searching a stack of documents → a few relevant snippets pulled out → snippets + question entering an LLM box → an answer with a small "fonte" citation tag. Flat vector, left-to-right, minimal text. 16:9.

## 2. (Opcional) RAG x fine-tuning
- **alt:** À esquerda "RAG": entrega uma ficha ao modelo (não muda o modelo); à direita "Fine-tuning": ajusta o interior do modelo (treino).
- **prompt:** Split: left "RAG" shows handing a document card to an unchanged model; right "Fine-tuning" shows adjusting gears inside the model. Flat vector, minimal text. 16:9.
