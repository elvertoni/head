# Brief de imagem — Aula 10: A ossatura: toda landing do mundo tem o mesmo esqueleto

> Neutro de plataforma. O prompt final é montado pela skill `gerar-imagem-aula` sobre o `prompt.xml` v6 — não escrever prompt à mão aqui. Branding (logo, curso, canvas) entra depois no Photoshop.

## Capa

- **perfil:** capa
- **arquivo:** `capa.png`
- **estado:** gerada e aprovada em 2026-08-19 (Codex, v6, r2 — 1536×1024, sem defeito). Canônica. A r1 reprovou em D11: o modelo inventou uma fileira social dentro do `<footer>` do mockup e desenhou as marcas do Instagram e do YouTube. A r2 reforçou a seção AVOID nomeando marcas sociais e fixou o conteúdo do rodapé do mockup como barras neutras.
- **objetivo:** Dar o mapa da aula num olhar — o esqueleto de cinco faixas de uma landing page, cada faixa pareada com a pergunta do visitante que ela responde e com a tag semântica que a constrói, mais a linha da dobra cortando a primeira tela. É o desenho que o professor reproduz no quadro e o que o portal exibe no card.
- **alt:** Página de site vista como um empilhamento de cinco faixas horizontais, de cima a baixo. A primeira faixa é o topo com o nome do produto e um menu; a segunda é o bloco grande com título, linha de apoio e botão; a terceira traz três blocos de benefício lado a lado; a quarta é a prova; a quinta repete o botão. Uma linha tracejada atravessa logo abaixo da segunda faixa, marcando o limite da tela antes da rolagem. À direita de cada faixa, a tag correspondente e a pergunta que ela responde.
- **prompt:** (esboço) cinco faixas empilhadas de uma landing, com a linha tracejada da dobra logo abaixo do hero e as tags anotadas na lateral.

## Infográfico

- **perfil:** infografico
- **arquivo:** `img/mesma-pagina-quatro-leitores.png`
- **estado:** gerada e aprovada em 2026-08-19 (Codex, v6, r3 — 1672×941, sem defeito). Canônica. A r1 reprovou em D2: o fechamento saiu como `</seticl>` no lugar de `</section>`, numa aula que ensina HTML semântico. A r2 corrigiu o código (passou a receber os dois trechos literais para transcrever) mas imprimiu "Titulo" sem acento nos mockups, erro herdado do próprio reforço. A r3 fixou a acentuação e passou limpa.
- **secao:** Desenvolvimento › Tags que dizem o que a coisa é
- **objetivo:** Ensinar o conceito mais contraintuitivo da aula — que a escolha entre div e tag semântica não tem sintoma visual, e por isso precisa ser justificada por quem lê a página sem enxergá-la. Uma figura com quatro leitores olhando o mesmo código resolve num olhar o que o texto só consegue por acumulação de argumentos.
- **alt:** No centro, um mesmo trecho de página. Dele saem quatro linhas para quatro leitores diferentes, cada um mostrando o que recebe. O leitor visual recebe a página desenhada, idêntica nas duas versões. O leitor de tela recebe, de um lado, uma lista de regiões nomeadas e, de outro, uma sequência de caixas sem nome. O buscador recebe, de um lado, o assunto identificado e, de outro, nada. O programador recebe, de um lado, um arquivo legível e, de outro, uma pilha de caixas aninhadas. A comparação entre versão com tags semânticas e versão só com div aparece em cada leitor, menos no visual, onde as duas são iguais.
- **prompt:** (esboço) um trecho de página no centro e quatro leitores ao redor, cada um recebendo uma coisa diferente, com a versão semântica e a versão só com div comparadas.
