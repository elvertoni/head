# Brief de imagem — Aula 14: Mobile-first: o MVP no celular de quem vai validar

> Neutro de plataforma. O prompt final é montado pela skill `gerar-imagem-aula` sobre o `prompt.xml` v6 — não escrever prompt à mão aqui. Branding (logo, curso, canvas) entra depois no Photoshop.

## Capa

- **perfil:** capa
- **arquivo:** `capa.png`
- **estado:** gerada e aprovada em 2026-08-21 (Codex, v6, r1 — 1536×1024, sem defeito). Canônica.
- **objetivo:** Dar o mapa da aula num olhar — a inversão da ordem de escrita do CSS. Mostra a tela pequena como caso padrão, os breakpoints acrescentando regras conforme a largura cresce, e a lista de verificação que fecha a aula no aparelho real. É o que o portal exibe no card.
- **alt:** Três telas em ordem crescente de largura, da esquerda para a direita — celular, tablet e monitor. A tela do celular está marcada como o padrão, de onde parte uma seta que atravessa as outras duas, com duas marcas de fronteira ao longo do percurso indicando onde novas regras são acrescentadas. Acima de cada fronteira aparece o que muda a partir dali: o título aumenta, o topo volta a ficar lado a lado. Na lateral direita, uma pequena lista de verificação com os itens do teste final — sem deslizamento lateral, texto legível sem aproximar, botão do tamanho do dedo.
- **prompt:** (esboço) três telas em largura crescente com o celular marcado como padrão, duas fronteiras de breakpoint no percurso e a lista de verificação na lateral.

## Infográfico

- **perfil:** infografico
- **arquivo:** `img/sem-viewport-o-celular-finge.png`
- **estado:** gerada e aprovada em 2026-08-19 (Codex, v6, r1 — 1672×941, sem defeito). Canônica.
- **secao:** Desenvolvimento › A linha sem a qual nada funciona
- **objetivo:** Ensinar o mecanismo invisível que produz o erro mais frustrante do responsivo — o CSS correto que não é aplicado. Como o comportamento acontece dentro do navegador e não aparece no código, é impossível deduzi-lo lendo o arquivo; a figura torna visível a largura fingida e explica por que a media query não dispara.
- **alt:** Comparação de dois celulares idênticos exibindo a mesma página. No da esquerda, sem a linha de viewport, uma régua sobreposta mostra que o navegador assume uma largura muito maior que a do aparelho; a página é montada nessa largura imaginária e depois reduzida para caber, resultando em conteúdo minúsculo, e uma marca indica que a regra escrita para telas estreitas não foi acionada. No da direita, com a linha declarada, a régua coincide com a largura real do aparelho, a página é montada nessa medida e o texto aparece em tamanho legível, com a marca indicando que a regra de tela estreita foi acionada.
- **prompt:** (esboço) dois celulares com a mesma página, um com régua de largura fingida e conteúdo encolhido, outro com régua da largura real e texto legível, indicando em cada caso se a media query disparou.
