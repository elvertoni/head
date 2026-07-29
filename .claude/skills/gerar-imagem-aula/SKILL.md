---
name: gerar-imagem-aula
description: Monta o prompt v6 "The Digital Atelier" pronto para colar no ChatGPT do navegador e depois valida/registra o PNG que voltar de lá. Use sempre que o pedido envolver imagem de aula do acervo PROF-TONI — produzir, refazer, editar, validar, executar propostas de imagens.md, criar capa.png, criar infográfico de miolo ou trabalhar com tools/imagen-generator. A geração acontece FORA do Claude Code (navegador); esta skill escolhe o perfil (capa densa 3:2 ou infográfico enxuto 16:9), escreve o prompt completo, audita o resultado contra 12 defeitos conhecidos e registra o caminho. Branding (logo, curso, canvas) é aplicado depois no Photoshop.
---

# gerar-imagem-aula

Esta skill **não gera a imagem**. Decisão do Toni (29/07/2026): a geração fica no
ChatGPT do navegador, que com o `prompt.xml` entrega qualidade bem superior à
ferramenta de imagem disponível aqui.

Papel da skill: **escolher o perfil, escrever o prompt v6 pronto pra colar, e
depois auditar e registrar o PNG que o Toni trouxer de volta.**

Nunca gerar a imagem com ferramenta interna, nem oferecer isso como atalho.

## Fontes obrigatórias

1. Ler integralmente `tools/imagen-generator/prompt.xml`.
2. Confirmar `versao="6.0"` e `modo="arte_base_para_branding_externo"`. Se não
   casar, interromper e reportar a divergência.
3. Ler a `canonica.md` e o `imagens.md` da aula-alvo.
4. XML = fonte de verdade visual. O brief define o conceito específico.

Nunca instruir o Toni a anexar `logo-prof-toni-coimbra-horizontal.png` ao
ChatGPT. A logo pertence à etapa do Photoshop.

## Os dois perfis

O primeiro passo, sempre, é declarar o perfil. Eles não se misturam.

| | **capa** | **infografico** |
|---|---|---|
| onde vive | `capa.png` na pasta da aula | `img/{slug}.png`, no miolo do texto |
| função | mapa da aula inteira, vende no card do portal | ensina UM conceito difícil |
| proporção | 3:2 (alvo 1536×1024) | 16:9 |
| blocos | 4 a 10 (ideal 7) | 2 a 5 |
| texto | rótulo caixa-alta + micro-parágrafo de 1–3 linhas por bloco | só rótulos: até 8, de até 4 palavras |
| subtítulo | obrigatório, 1–2 linhas | proibido |
| faixa de rodapé | obrigatória (`EM RESUMO`, `LEMBRE-SE`...) | proibida |
| ocupação do miolo | 70–90% da altura útil | 60–80% |

Errar o perfil é o defeito **D12** do XML: capa esparsa em 16:9 fica órfã,
infográfico com parágrafos em 3:2 vira capa ruim.

## Quantas imagens por aula

**Uma capa + no máximo um infográfico.** Nada de lote, alternativa ou variação.
Se `imagens.md` trouxer várias propostas de miolo, escolher uma só, nesta ordem:

1. a que explica visualmente algo difícil de entender só por texto;
2. a que não duplica tabela, quiz ou `diagrama-progressivo` já suficiente;
3. a que permanece clara em três segundos e no celular.

Ideias inseparáveis → integrar numa composição só. Já existe imagem?
Substituir no mesmo caminho; não criar arquivo irmão.

## Modo A — preparar o prompt (padrão)

1. Rodar `git status --short` para ver o que já existe.
2. **Declarar o perfil** e reafirmar o **título exato da aula-alvo**. Isso não é
   burocracia: três capas do acervo saíram com o conteúdo da aula seguinte
   (defeito **D8**) por erro de pareamento entre brief e aula.
3. Análise pedagógica do XML: conceito difícil, erro comum, relação visual,
   mensagem de três segundos.
4. Preencher as `<variaveis_da_aula>`, incluindo a lista de blocos com rótulo e
   micro-texto (perfil capa) ou os rótulos curtos (perfil infográfico).
5. Entregar, num único bloco de código pronto pra colar, o
   `<prompt_arte_base>` **do perfil correto**, com todos os `[insert ...]`
   substituídos e sem cortar nenhuma seção — `RESERVED EMPTY ZONES`,
   `COLOR SYSTEM`, `TYPOGRAPHY`, `LAYOUT` e `AVOID` vão inteiras.
6. Informar o caminho alvo (`capa.png` ou `img/{slug-kebab}.png`) e o alt text
   em português.

A entrega do Modo A é texto. Nenhuma imagem é gerada aqui.

## Modo B — validar o PNG que voltou do navegador

Quando o Toni salvar o arquivo e pedir conferência, abrir o PNG e percorrer o
`checklist_final` do XML **e** os 12 defeitos conhecidos da regra `R3`. Cada um
já aconteceu de verdade no acervo:

| | defeito | caso real |
|---|---|---|
| D1 | texto de placeholder impresso na arte | aula 10 de IA saiu com "ESPAÇO RESERVADO PARA LOGO" |
| D2 | palavra inventada em português | "nulhado" (aula 08), "madruagda" (aula 06) |
| D3 | peça sem título | aula 31 de arquitetura, aula 06 de IA |
| D4 | fundo claro/branco | aulas 05 e 06 de IA, as duas de tráfego orgânico |
| D5 | texto/objeto cortado pela borda | "AM" solto na aula 25 |
| D6 | faixa superior vazia demais | aulas 04 e 09 de IA |
| D7 | ornamento dentro de zona reservada | aula 33, nivelamento 01 |
| D8 | conteúdo da aula errada | aulas 06, 07 e 08 de IA |
| D9 | wireframe cinza sem ícone/cor/título | falha recorrente da v5 |
| D10 | comparação com um lado só rotulado | — |
| D11 | logo real de terceiro desenhada | logos de SO na aula 35 |
| D12 | perfil trocado | — |

Fluxo:

1. Reprovado → apontar o defeito **pelo id** e devolver o prompt reforçado
   exatamente no ponto que falhou. Nova rodada no navegador.
2. Aprovado → registrar o caminho em `imagens.md`. Não criar caminho para
   proposta descartada. Não apagar arquivo antigo sem pedido. Imagens não
   alteram `manifesto.json`.

Verificar também a proporção do perfil e a resolução. **Não** normalizar para
1536×1024 nem 1600×900 — isso é da action do Photoshop.

## Limite de responsabilidade

A skill termina na arte-base aprovada. Nunca aplicar logo, nome "Prof. Toni
Coimbra", identificação "TÉCNICO EM DESENVOLVIMENTO DE SISTEMAS", smart object,
overlay ou normalização de canvas. Pedido de imagem já brandada → explicar que a
etapa seguinte é a action determinística do Photoshop.

A logo pode ficar no repositório como insumo externo, mas nunca entra na entrada
do modelo generativo.

## Entrega

**Modo A:** perfil declarado + prompt colável + caminho alvo + conceito central +
mensagem 3s + alt text + a frase `Prompt v6 pronto para o navegador.`

**Modo B:** veredito (aprovado/reprovado), defeitos por id, caminho registrado e
a frase `Arte-base validada com cantos superiores reservados e limpos.`
