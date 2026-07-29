# Imagens — Branches: testando ideia arriscada sem bagunçar o que funciona

Brief neutro de plataforma. Nenhuma imagem existe ainda — prompts prontos para colar num gerador (Gemini Nano Banana / GPT). O `alt` já carrega a informação de verdade (nenhum renderer hoje serve `img/` de conteúdo).

---

## 1. Branch como rótulo móvel, não cópia de pasta

- **secao:** Desenvolvimento › Branch: um ponteiro que se move, não uma cópia da pasta
- **objetivo:** Corrigir a intuição errada mais comum (branch = pasta duplicada) mostrando o histórico como uma única linha de commits com dois rótulos móveis apontando pontos diferentes — não duas árvores de arquivo separadas.
- **alt:** Diagrama de uma linha de commits representada por círculos conectados em sequência horizontal. No terceiro círculo, dois rótulos coloridos — "main" e "modo-escuro" — apontam para o mesmo commit inicial. Uma seta mostra o rótulo "modo-escuro" avançando para dois círculos novos à direita, enquanto o rótulo "main" permanece parado no commit original, ilustrando que branch é um ponteiro que se move, não uma cópia de arquivos.
- **prompt:** "Diagrama técnico plano sobre fundo escuro (#0a0a0a). Uma fileira horizontal de círculos verdes conectados por linhas finas, representando commits em sequência. No terceiro círculo da esquerda, duas etiquetas retangulares coloridas ficam lado a lado apontando pra ele com pequenas setas: uma etiqueta azul rotulada 'main' e uma etiqueta laranja rotulada 'modo-escuro'. A partir desse ponto, uma linha se ramifica para cima e para a direita com mais dois círculos laranja conectados, com a etiqueta 'modo-escuro' agora apontando para o último círculo dessa ramificação. A etiqueta 'main' permanece parada no círculo original. Tipografia sans-serif técnica, estilo editorial minimalista, poucas cores saturadas sobre fundo escuro, sem sombras pesadas."

## 2. Anatomia de um conflito de merge no arquivo

- **secao:** Desenvolvimento › Quando o Git não consegue decidir sozinho: o conflito
- **objetivo:** Mostrar visualmente a anatomia dos marcadores de conflito dentro do arquivo real — o que cada seção entre `<<<<<<<`, `=======` e `>>>>>>>` representa — reforçando com cor o que o texto explica em prosa.
- **alt:** Trecho de código com marcadores de conflito de merge destacados por cores: a linha `<<<<<<< HEAD` em uma cor, o bloco de texto logo abaixo dela (a versão da branch atual) destacado em uma cor de fundo, a linha `=======` como divisor neutro, o bloco de texto seguinte (a versão da outra branch) destacado em outra cor de fundo, e a linha `>>>>>>> modo-escuro` na mesma cor da primeira. Setas ou chaves ao lado indicam "versão atual" e "versão da outra branch".
- **prompt:** "Captura de tela estilizada de um editor de código sobre fundo escuro (#0a0a0a), fonte monoespaçada. Mostra um trecho de HTML com marcadores de conflito de merge do Git: a linha '<<<<<<< HEAD' destacada em azul, seguida por uma linha de parágrafo destacada com fundo azul translúcido representando a versão atual; depois a linha '=======' em cinza neutro como divisor; em seguida outra linha de parágrafo destacada com fundo laranja translúcido representando a versão da outra branch; por fim a linha '>>>>>>> modo-escuro' destacada em laranja. Ao lado direito, duas chaves curvas com as legendas 'versão atual (HEAD)' e 'versão da branch modo-escuro' apontando para os respectivos blocos. Estilo técnico-editorial, tipografia monoespaçada, sem elementos decorativos supérfluos."
