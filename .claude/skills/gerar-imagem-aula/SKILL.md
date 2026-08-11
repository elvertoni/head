---
name: gerar-imagem-aula
description: Produz e valida as artes-base das aulas do acervo PROF-TONI, do brief até o PNG auditado. Use sempre que o pedido tocar em imagem de aula — gerar capa.png, gerar infográfico de miolo, refazer ou editar uma arte, executar propostas de imagens.md, auditar um PNG que voltou do ChatGPT, ajustar o Projeto do navegador ou mexer em tools/imagen-generator — mesmo que o Toni não use as palavras "skill", "prompt" ou "imagem". Escolhe o perfil (capa densa 3:2 ou infográfico enxuto 16:9), monta o prompt v6 "The Digital Atelier", delega a geração ao Codex (que gera aqui mesmo, sem navegador) ou entrega o prompt pronto pra colar, e audita o resultado contra os 12 defeitos conhecidos do acervo. Branding — logo, curso, canvas — é aplicado depois no Photoshop, nunca aqui.
---

# gerar-imagem-aula

A skill leva a arte-base do brief até o PNG auditado. Ela **gera**: o Codex CLI
tem ferramenta nativa de imagem e produz aqui mesmo, sem navegador.

O trabalho que agrega valor não é apertar o botão de gerar — é a análise
pedagógica que vira prompt e a auditoria que impede peça defeituosa de entrar no
acervo. O gerador é intercambiável; essas duas pontas não são.

Dois caminhos de geração, na ordem de preferência:

1. **Codex, aqui** (padrão) — ver `references/delegar-ao-codex.md`.
2. **Projeto do ChatGPT, no navegador** — quando o Toni pedir, ou se o Codex
   falhar. Ver `references/instrucoes-projeto-gpt.md`.

## Fontes obrigatórias

1. Ler integralmente `tools/imagen-generator/prompt.xml`.
2. Confirmar `versao="6.0"` e `modo="arte_base_para_branding_externo"`. Não
   casou? Interromper e reportar a divergência antes de gerar qualquer coisa.
3. Ler a `canonica.md` e o `imagens.md` da aula-alvo.

O XML é a fonte de verdade visual; o brief define o conceito específico. Se os
dois conflitarem, o XML ganha na forma e o brief ganha no conteúdo.

`logo-prof-toni-coimbra-horizontal.png` nunca entra na entrada de um modelo
generativo, em nenhum dos dois caminhos. Dar a marca ao modelo é convite para
ele redesenhá-la.

## Os dois perfis

Declarar o perfil é sempre o passo zero. Eles não se misturam, e não se
empilham num quadro só.

| | **capa** | **infografico** |
|---|---|---|
| onde vive | `capa.png` na pasta da aula | `img/{slug}.png`, no miolo do texto |
| função | mapa da aula inteira, vende no card do portal | ensina UM conceito difícil |
| proporção | 3:2 (alvo 1536×1024) | 16:9 |
| blocos | 4 a 10 (ideal 7) | 2 a 5 |
| texto | rótulo caixa-alta + micro-parágrafo de 1–3 linhas por bloco | só rótulos: até 8, de até 4 palavras |
| subtítulo | obrigatório, 1–2 linhas | proibido |
| faixa de rodapé | obrigatória (`EM RESUMO`, `LEMBRE-SE`…) | proibida |
| ocupação do miolo | 70–90% da altura útil | 60–80% |

Errar ou fundir o perfil é o defeito **D12**: capa esparsa em 16:9 fica órfã,
infográfico com parágrafos em 3:2 vira capa ruim, e capa com painel de
comparação pendurado embaixo vira duas peças brigando pelo mesmo olhar.

## Quantas imagens por aula

**Uma capa + no máximo um infográfico.** Nada de lote, alternativa ou variação —
o custo de escolher recai no Toni depois, e ele não pediu opções.

Se `imagens.md` trouxer várias propostas de miolo, escolher uma, nesta ordem:

1. a que explica visualmente algo difícil de entender só por texto;
2. a que não duplica tabela, quiz ou `diagrama-progressivo` já suficiente;
3. a que permanece clara em três segundos e no celular.

Ideias inseparáveis → integrar numa composição só.

## Onde o arquivo cai

Uma regra só, porque duas se contradizem e o custo cai no Toni. Toda rodada
nasce no scratchpad da sessão, não no acervo:

```
{scratchpad}/imagem-aula/{slug-da-aula}--{perfil}--r{n}.png
```

Rodada reprovada morre ali e nunca entra em `aulas/`. Isso é o que impede a
pasta da aula de acumular tentativa — foi assim que dois PNGs de fundo claro
ficaram semanas ocupando espaço na pasta de HTML semântico.

Só a peça **aprovada na auditoria** é copiada para o acervo, e o destino depende
do que já existe lá:

| situação | destino |
|---|---|
| caminho canônico vazio | grava direto em `capa.png` ou `img/{slug}.png` |
| já existe arte no caminho | grava como `{stem}.proposta.png` ao lado |

`{stem}.proposta.png` é sempre o mesmo nome — a proposta seguinte sobrescreve a
anterior. Nunca sufixar com a versão do prompt: `v6` identifica o sistema, não a
tentativa, e `capa-v6 (2).png` é o beco sem saída que essa regra existe pra
evitar.

Substituir arte que já está no acervo é decisão do Toni, nunca da rodada. Ao
entregar uma proposta, dizer qual arquivo é o canônico atual, qual é a proposta,
e o que muda entre os dois — ele precisa disso pra decidir sem abrir os dois no
Photoshop.

## Modo 1 — gerar aqui (padrão)

1. Listar a pasta da aula para ver que arte já existe e qual caminho está
   ocupado.
2. **Declarar o perfil** e reafirmar o **título exato da aula-alvo**. Não é
   burocracia: três capas do acervo saíram com o conteúdo da aula seguinte
   (**D8**) por erro de pareamento entre brief e aula.
3. Análise pedagógica exigida pelo XML: conceito mais difícil, erro comum a
   evitar, relação visual que precisa ficar evidente, mensagem de três segundos.
4. Montar o `<prompt_arte_base>` **do perfil correto** com todos os
   `[insert …]` resolvidos. Nenhuma seção sai — `RESERVED EMPTY ZONES`,
   `COLOR SYSTEM`, `TYPOGRAPHY`, `LAYOUT` e `AVOID` vão inteiras. São elas que
   seguram os defeitos, e são as primeiras que a tentação de encurtar ataca.
5. Gravar o prompt montado num `.txt` no scratchpad e delegar ao Codex conforme
   `references/delegar-ao-codex.md`, de forma síncrona.
6. Auditar o PNG (Modo 3). Sem exceção — o relato de quem gerou cobre existência
   e medida, nunca conteúdo.
7. Aprovado → copiar pro acervo e registrar. Reprovado → nova rodada.

**Teto de três rodadas** (`r1`, `r2`, `r3`). Se a terceira reprovar, parar e
reportar: o defeito que persistiu, pelo id, e o que mudou em cada tentativa. Aí
a decisão é do Toni — insistir, mudar o brief, ou ir pro navegador (Modo 2).
Girar sozinho gasta dinheiro dele sem convergir, e falha repetida no mesmo
defeito costuma ser sinal de brief ambíguo, não de gerador ruim.

O gerador nativo do Codex **não aceita ajuste de qualidade** — `quality`, modelo
e tamanho não são expostos, e um pedido de `quality=high` é descartado em
silêncio. Não prometa ao Toni um ganho por parâmetro que a ferramenta não tem;
o que separa peça boa de peça ruim aqui é o prompt ir montado, não cru.

Entregar ao Toni o prompt montado junto do resultado. Ele reusa esse texto no
navegador quando quiser comparar geradores.

## Modo 2 — prompt pronto pro navegador

Quando o Toni pedir o caminho do navegador, a entrega é texto: o prompt colável
num único bloco de código, o caminho alvo e o alt text. Detalhes de configuração
do Projeto, anexos e mensagem de rodada estão em
`references/instrucoes-projeto-gpt.md`.

## Modo 3 — auditar o PNG

Vale para qualquer PNG, venha do Codex, do navegador ou do Downloads do Toni.

**Olhar antes de lembrar.** Abrir a imagem com `Read` e primeiro descrever o que
está de fato ali — cada bloco, cada palavra renderizada — sem reler o prompt que
a gerou. Só depois comparar com o brief e percorrer o `checklist_final` do XML.
A ordem importa porque quem montou o prompt sabe o que deveria estar na peça e
lê o que espera ver; D2 e D4 escapam por isso, não por falta de checklist. Se a
peça reprovar duas vezes no mesmo defeito, vale pedir ao Toni uma auditoria de
terceiro — alguém que receba só o PNG e a tabela abaixo, nunca o prompt.

A lista canônica dos 12 defeitos é a regra `R3` do `prompt.xml`; a tabela aqui é
a mesma lista com os casos reais anexados. Divergiu entre as duas? O XML manda,
e a divergência se reporta. Defeito novo que chegar ao acervo entra nos dois
lugares: a regra no XML, o caso aqui.

| | defeito | caso real |
|---|---|---|
| D1 | texto de placeholder impresso na arte | aula 10 de IA: "ESPAÇO RESERVADO PARA LOGO" |
| D2 | palavra inventada em português | "nulhado" (aula 08), "madruagda" (aula 06), "rosolveu" e "flex-contáiner" (HTML semântico) |
| D3 | peça sem título | aula 31 de arquitetura, aula 06 de IA |
| D4 | fundo claro/branco | aulas 05 e 06 de IA, as duas de tráfego orgânico, duas tentativas de HTML semântico |
| D5 | texto/objeto cortado pela borda | "AM" solto na aula 25 |
| D6 | faixa superior vazia demais | aulas 04 e 09 de IA |
| D7 | ornamento dentro de zona reservada | aula 33, nivelamento 01 |
| D8 | conteúdo da aula errada | aulas 06, 07 e 08 de IA |
| D9 | wireframe cinza sem ícone/cor/título | falha recorrente da v5 |
| D10 | comparação com um lado só rotulado | — |
| D11 | logo real de terceiro desenhada | logos de SO na aula 35 |
| D12 | perfil trocado ou fundido | HTML semântico: capa + infográfico no mesmo quadro |

Além da tabela, checar sempre:

- **zonas reservadas** — os dois cantos superiores escuros e vazios, e o título
  não invadindo nenhum deles;
- **proporção** — `python .claude/skills/gerar-imagem-aula/scripts/inspecionar_png.py {perfil} {arquivo}`
  mede e compara com o alvo do perfil. Proporção errada se regenera; **não** se
  recorta, e **não** se normaliza para 1536×1024 nem 1600×900 — canvas é da
  action do Photoshop;
- **cada palavra renderizada** — existe em português, escrita certa. D2 é o
  defeito que mais passa batido porque a peça está bonita.

Reprovado → apontar o defeito **pelo id**, reforçar no prompt exatamente a seção
que falhou (não o prompt inteiro) e regerar. Não entregar peça reprovada com
ressalva: o Toni não tem como consertar isso no Photoshop.

## Registro

Aprovado → copiar do scratchpad para o acervo conforme a tabela de destinos,
atualizar o **estado** da entrada correspondente em `imagens.md` e confirmar o
caminho. Não criar entrada para proposta descartada. Não apagar nem sobrescrever
arte que já está no acervo sem pedido explícito do Toni.

Imagens não alteram `manifesto.json` e não exigem bump de `versao` na aula.

## Limite de responsabilidade

A skill termina na arte-base aprovada. Nunca aplicar logo, nome "Prof. Toni
Coimbra", identificação "TÉCNICO EM DESENVOLVIMENTO DE SISTEMAS", smart object,
overlay ou normalização de canvas. Pedido de imagem já brandada → explicar que a
etapa seguinte é a action determinística do Photoshop.

## Entrega

A entrega prova o trabalho com medida e veredito, não com frase de encerramento
— atestado que o modelo consegue escrever sem ter olhado a imagem não vale nada
pro Toni.

**Modo 1:** perfil declarado · caminho final do PNG e se é canônico ou proposta ·
dimensões medidas pelo script · veredito da auditoria, defeito por id ou
"nenhum" · quantas rodadas foram · conceito central · mensagem de 3 segundos ·
alt text em português · o prompt montado.

**Modo 2:** perfil declarado · prompt colável · caminho alvo · conceito central ·
mensagem de 3 segundos · alt text.

**Modo 3:** veredito · defeitos por id · proporção medida contra o alvo do
perfil · caminho auditado.
