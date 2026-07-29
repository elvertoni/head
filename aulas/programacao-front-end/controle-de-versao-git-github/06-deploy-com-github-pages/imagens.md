# Imagens — GitHub Pages: transformando repositório num site que qualquer pessoa acessa

Brief neutro de plataforma. Nenhuma imagem existe ainda — prompts prontos para colar num gerador (Gemini Nano Banana / GPT). O `alt` já carrega a informação de verdade (nenhum renderer hoje serve `img/` de conteúdo).

---

## 1. Do push ao link público, em um minuto

- **secao:** Desenvolvimento › Ativando o GitHub Pages pro Petfinder (diagrama-progressivo)
- **objetivo:** Tornar visível o ciclo automático "push → detecção → publicação" que o texto descreve em três camadas, reforçando que não existe passo manual de "reenviar o site" depois da configuração inicial.
- **alt:** Diagrama circular de três etapas conectadas por setas em loop. Primeira etapa: ícone de terminal com o texto "git push". Segunda etapa: ícone do logo do GitHub com uma lupa, texto "detecta a mudança automaticamente". Terceira etapa: ícone de globo/link com o texto "site atualizado (~1 min)", com uma seta voltando para a primeira etapa indicando que o ciclo se repete a cada push.
- **prompt:** "Diagrama circular técnico sobre fundo escuro (#0a0a0a), três nós conectados por setas curvas formando um ciclo. Nó 1: ícone de terminal preto com texto verde, rotulado 'git push'. Seta levando ao nó 2: ícone do logo do GitHub com uma pequena lupa sobreposta, rotulado 'detecta automaticamente'. Seta levando ao nó 3: ícone de globo terrestre com um link saindo dele, rotulado 'site atualizado (~1 min)'. Uma seta pontilhada do nó 3 de volta para o nó 1 indica que o ciclo se repete a cada novo push. Tipografia sans-serif técnica, estilo editorial minimalista, poucas cores saturadas sobre fundo escuro, sem sombras pesadas."

## 2. Por que a mesma imagem funciona local e quebra publicada

- **secao:** Desenvolvimento › O erro mais comum: um caminho que funciona local e quebra publicado
- **objetivo:** Mostrar concretamente a raiz do erro de maiúscula/minúscula — dois sistemas de arquivo tratando o mesmo nome de forma diferente — algo mais fácil de fixar vendo os dois lados lado a lado do que só lendo a explicação em texto.
- **alt:** Comparação lado a lado de dois sistemas operacionais. À esquerda, um ícone representando Windows/Mac com dois nomes de arquivo escritos, "logo.png" e "Logo.png", ligados por um sinal de igual, com a legenda "mesmo arquivo para o seu computador". À direita, um ícone de pinguim representando Linux (o servidor do GitHub Pages) com os mesmos dois nomes de arquivo, agora ligados por um sinal de diferente, com a legenda "dois arquivos diferentes para o servidor".
- **prompt:** "Ilustração técnica comparativa dividida em duas metades sobre fundo escuro (#0a0a0a). Metade esquerda com um ícone estilizado de janela (representando Windows/Mac) no topo, abaixo dele o texto 'logo.png' e 'Logo.png' lado a lado conectados por um sinal de igual (=) grande, e a legenda 'mesmo arquivo no seu computador'. Metade direita com um ícone estilizado de pinguim (representando o servidor Linux do GitHub Pages) no topo, abaixo dele os mesmos dois textos 'logo.png' e 'Logo.png' conectados por um sinal de diferente (≠) grande em vermelho, e a legenda 'dois arquivos diferentes no servidor'. Tipografia monoespaçada para os nomes de arquivo, sans-serif para as legendas, estilo técnico-editorial minimalista, poucas cores saturadas sobre fundo escuro."
