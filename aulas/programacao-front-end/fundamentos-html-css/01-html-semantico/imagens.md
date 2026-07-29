# Imagens — HTML semântico: por que `<div>` não conta a história toda

Brief neutro de plataforma. Nenhuma imagem existe ainda — os prompts abaixo estão prontos para colar num gerador (Gemini Nano Banana / GPT) assim que o Toni quiser produzi-las. Enquanto isso, o `alt` já carrega a informação de verdade (nenhum renderer hoje serve `img/` de conteúdo).

---

## 1. Mesmo visual, dois códigos

- **secao:** Desenvolvimento › O problema da div-soup / O catálogo que resolve isso
- **objetivo:** Mostrar lado a lado o mesmo layout renderizado (header/article/aside/nav/footer) com duas árvores DOM diferentes — uma toda em `<div class="...">` cinza, outra com as tags semânticas destacadas em cores — provando que o resultado visual é idêntico mas o "significado" só existe num dos dois.
- **alt:** Duas árvores de elementos HTML lado a lado, representando o mesmo layout visual (header no topo, article/aside/nav no meio, footer embaixo). À esquerda, todos os nós são `<div>` cinza com apenas o atributo class diferenciando-os. À direita, os mesmos nós usam as tags `<header>`, `<article>`, `<aside>`, `<nav>` e `<footer>`, destacadas em cores distintas, mostrando que o significado structural é explícito na tag, não no nome da classe.
- **prompt:** "Infográfico plano, estilo editorial minimalista, fundo escuro (#0a0a0a). Dois painéis lado a lado com o título pequeno acima de cada um: à esquerda 'Só <div>', à direita 'Tags semânticas'. Cada painel mostra uma árvore de nós retangulares empilhados representando um layout de página (um retângulo largo no topo rotulado 'header', três retângulos médios lado a lado no meio rotulados 'article', 'aside', 'nav', e um retângulo largo embaixo rotulado 'footer'). No painel esquerdo, todos os retângulos são cinza-chumbo idênticos, com uma legenda pequena `class=\"header\"` etc. dentro de cada um. No painel direito, os mesmos retângulos têm cores distintas (verde, roxo, ciano, laranja, azul) e a legenda dentro de cada um mostra a tag semântica em negrito (`<header>`, `<article>`, `<aside>`, `<nav>`, `<footer>`). Tipografia sans-serif técnica, sem elementos decorativos supérfluos, paleta com poucas cores saturadas sobre fundo escuro."

## 2. Como o leitor de tela navega a página

- **secao:** Desenvolvimento › Por que isso importa fora da tela
- **objetivo:** Ilustrar a diferença prática entre navegar uma página div-soup (sequencial, sem atalho) e uma página semântica (pulos diretos entre landmarks) — reforça o `diagrama-progressivo` da Canônica com um visual único e comparável.
- **alt:** Diagrama comparando dois caminhos de leitura de uma mesma página por um leitor de tela. À esquerda, uma seta longa e reta descendo por todos os blocos da página em sequência (menu, conteúdo, rodapé), rotulada 'sem tags semânticas: só dá pra ler tudo em ordem'. À direita, a mesma página com três setas curtas ligando diretamente do topo a cada marco (nav, main, footer), rotuladas 'com tags semânticas: pula direto pro marco desejado'.
- **prompt:** "Diagrama esquemático plano, duas colunas comparativas sobre fundo escuro (#0a0a0a). Coluna esquerda com título 'Sem tags semânticas': uma coluna vertical de retângulos empilhados (menu, artigo, rodapé) todos da mesma cor cinza, conectados por uma única seta reta e longa descendo por todos em sequência, com o texto pequeno 'leitura linear, sem atalho' ao lado da seta. Coluna direita com título 'Com tags semânticas': os mesmos retângulos agora coloridos (nav em laranja, main em verde, footer em azul), cada um com uma seta curta e direta partindo de um ícone de leitor de tela no topo, com o texto pequeno 'pulo direto pro marco' ao lado de cada seta. Estilo técnico-editorial, tipografia sans-serif, sem gradientes nem sombras pesadas, poucas cores saturadas sobre fundo escuro."
