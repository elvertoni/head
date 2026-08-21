# Brief de imagem — Aula 16: JavaScript na conta certa: três comportamentos, vinte linhas

> Neutro de plataforma. O prompt final é montado pela skill `gerar-imagem-aula` sobre o `prompt.xml` v6 — não escrever prompt à mão aqui. Branding (logo, curso, canvas) entra depois no Photoshop.

## Capa

- **perfil:** capa
- **arquivo:** `capa.png`
- **estado:** gerada e aprovada em 2026-08-21 (Codex, v6, r1 — 1536×1024, sem defeito). Canônica.
- **objetivo:** Dar o mapa da aula num olhar — as três camadas de uma página e o lugar exato do JavaScript nelas, com os três comportamentos da aula distribuídos e um deles marcado como resolvido sem script. É o que o portal exibe no card.
- **alt:** Três folhas empilhadas em perspectiva, uma sobre a outra, rotuladas de baixo para cima como conteúdo, aparência e comportamento. Da folha do topo saem chamadas para três comportamentos da página: o menu que abre e fecha no celular, o botão que copia o endereço, e a rolagem que desliza até a seção — este último com uma marca indicando que vem da folha do meio, não da de cima. Ao lado, uma indicação de que a folha de baixo continua legível mesmo se a de cima falhar.
- **prompt:** (esboço) três camadas empilhadas em perspectiva com os três comportamentos apontados, sendo a rolagem suave marcada como vinda da camada de aparência.

## Infográfico

- **perfil:** infografico
- **arquivo:** `img/o-recado-que-fica-esperando.png`
- **estado:** gerada e aprovada em 2026-08-21 (Codex, v6, r1 — 1672×941, sem defeito). Canônica.
- **secao:** Desenvolvimento › Achar o elemento, e deixar um recado
- **objetivo:** Ensinar o modelo mental mais difícil do primeiro JavaScript — que o script é lido uma vez e termina, e que a função registrada só roda depois, disparada por um evento. Esse descompasso entre o momento da leitura e o momento da execução é invisível no código e é a origem direta do erro de elemento inexistente; uma linha do tempo mostra de uma vez o que o texto precisa contar em etapas.
- **alt:** Linha do tempo horizontal dividida em dois territórios. No trecho inicial, marcado como leitura do arquivo, o navegador percorre as linhas do script de cima a baixo, e no ponto da linha que registra o ouvinte aparece um envelope guardado, com a indicação de que a função não foi executada. Logo depois, a linha do tempo entra num trecho longo e vazio, rotulado como espera, sem nenhuma atividade. Mais adiante, um toque de dedo marca o evento, o envelope guardado é aberto e só então a função aparece em execução. Abaixo do trecho inicial, uma ramificação mostra o caso em que o script é lido antes de o elemento existir — a busca volta vazia e nenhum envelope chega a ser guardado.
- **prompt:** (esboço) linha do tempo com leitura do script e envelope guardado, trecho longo de espera, evento disparando a execução, e ramificação mostrando a busca que volta vazia quando o script vem cedo demais.
