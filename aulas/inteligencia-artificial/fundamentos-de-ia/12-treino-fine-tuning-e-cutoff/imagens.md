# Brief de imagem — Aula 12: Treino, Fine-tuning e Cutoff

> Neutro de plataforma. Imagem só entra com justificativa pedagógica (teste anti-decoração). Final web ≤500 KB em `img/`; original pesado fica no `lake/` (fora do git).

## 1. A linha do tempo do modelo e o cutoff

- **secao:** Desenvolvimento › O conhecimento congela: cutoff (fallback do diagrama-progressivo)
- **objetivo:** Mostrar que o conhecimento do modelo para numa data (cutoff): antes ele conhece, depois é cego. A linha do tempo com uma "parede" no cutoff fixa o conceito.
- **alt:** Linha do tempo: coleta de dados e treino até uma "parede" marcada "CUTOFF"; depois da parede, o período de uso com um ponto de interrogação sobre eventos recentes.
- **prompt:** A horizontal timeline: a filled section labeled "treino (dados até aqui)" ending at a wall/barrier labeled "CUTOFF"; beyond the wall a greyed-out section labeled "uso" with question marks over recent-event icons the model cannot see. Flat vector, minimal text. 16:9.

## 2. (Opcional) Pré-treino x fine-tuning
- **alt:** Dois blocos: um grande "Pré-treino" (montanha de livros) e um pequeno "Fine-tuning" (ajuste fino com chave de fenda), formando o modelo final.
- **prompt:** Two blocks feeding a final model: a large "Pré-treino" block shown as a mountain of books, a small "Fine-tuning" block shown as fine adjustment with a screwdriver/dial. Flat vector, minimal text. 16:9.
