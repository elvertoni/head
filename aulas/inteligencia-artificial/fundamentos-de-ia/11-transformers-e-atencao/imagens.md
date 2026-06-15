# Brief de imagem — Aula 11: Transformers e Atenção

> Neutro de plataforma. Imagem só entra com justificativa pedagógica (teste anti-decoração). Final web ≤500 KB em `img/`; original pesado fica no `lake/` (fora do git).

## 1. A atenção iluminando a palavra certa

- **secao:** Desenvolvimento › Atenção: olhar para o que importa
- **objetivo:** Mostrar visualmente o mecanismo de atenção — ao processar "ela", o modelo "ilumina" a palavra de que ela depende. Concretiza um conceito abstrato.
- **alt:** A frase "colocou o livro na mochila porque ela estava pesada", com a palavra "ela" conectada por linhas de destaque mais fortes para "mochila" e fracas para as demais.
- **prompt:** The sentence "colocou o livro na mochila porque ELA estava pesada" laid out, with the word "ela" highlighted and attention lines of varying thickness connecting it to other words — thick bright line to "mochila", faint lines to others. Flat vector, conveys "attention weighting", minimal extra text. 16:9.

## 2. (Opcional) Ler em fila x olhar tudo de uma vez
- **alt:** À esquerda, modelo antigo lendo palavra por palavra com o começo desbotando; à direita, transformer com todas as palavras visíveis e conectadas ao mesmo tempo.
- **prompt:** Split: left a model reading words one-by-one in a queue with earlier words fading out (forgetting); right a transformer with all words visible at once, interconnected. Flat vector, contrast sequential vs parallel, minimal text. 16:9.
