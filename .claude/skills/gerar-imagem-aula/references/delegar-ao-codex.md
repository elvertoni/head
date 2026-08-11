# Delegar a geração ao Codex

O Codex CLI tem ferramenta nativa de imagem. Verificado em 29/07/2026: a partir
do prompt v6 já montado, o `image_gen` nativo entregou um infográfico em
1672×941. O arquivo 1664×936 existente no acervo veio depois de um crop
(`Rectangle(4,2,1664,936)`), não é resolução nativa. Na Images API, os tamanhos
16:9 válidos são `1536x864` e `2048x1152`.

Esse é o caminho padrão de geração. O navegador continua válido, mas é a
segunda opção — ver `instrucoes-projeto-gpt.md`. A ferramenta nativa é opaca:
não expõe modelo, `quality`, `size`, `background` nem `fidelity`. Um pedido de
`quality=high` é descartado silenciosamente; no mesmo prompt, os dois PNGs
medidos saíram em 1536×1024, com 1764423 e 1862719 bytes. A diferença é
variação estocástica, não efeito de parâmetro. O PNG nasce em
`.codex/generated_images/` e deve ser copiado de lá para o caminho de saída
pedido.

### Caminho futuro: Images API

A receita controlável fica documentada, mas está indisponível nesta máquina:

```powershell
image_gen.py generate --model gpt-image-2 --no-augment --quality high --size 1536x1024 --background opaque --output-format png --n 1
```

A tentativa retornou literalmente: `Error: OPENAI_API_KEY is not set. Export it
before running.` O Codex está autenticado por login ChatGPT (`stored ChatGPT
tokens true`, `stored API key false`); token de ChatGPT não equivale a
`OPENAI_API_KEY`. Definir `OPENAI_API_KEY` no ambiente destrava esse caminho.

## Por que o prompt vai montado

Nas duas rodadas do mesmo dia, o resultado divergiu conforme o que o modelo
recebeu:

| entrada | resultado |
|---|---|
| prompt v6 já preenchido, em inglês, seção por seção | aprovado de primeira |
| "execute integralmente o XML v6" + `canonica.md` + `imagens.md` | duas peças reprovadas: fundo branco (D4), cantos superiores ocupados (R1), capa e infográfico fundidos num quadro só (D12), "rosolveu" e "flex-contáiner" (D2) |

A leitura: pedir que o modelo *interprete* o design system deixa a camada de
estilo por conta dele, e ele cai no default editorial claro. Entregar o prompt
já resolvido tira essa variância. A análise pedagógica — escolher blocos,
rótulos, cores semânticas — é trabalho da skill, feito aqui, onde a
`canonica.md` está aberta.

Portanto: monte o prompt completo, grave num arquivo, e passe **o caminho do
arquivo** ao Codex. Não peça ao Codex para ler a aula nem para decidir o
conteúdo.

## Contrato da delegação

Grave o prompt montado em um `.txt` no scratchpad e chame o subagente
`codex:codex-rescue` de forma **síncrona** (`run_in_background: false`) — o PNG
precisa estar em disco antes de você auditar.

A saída de cada rodada deve ficar sempre no scratchpad da sessão, nunca em
`aulas/`: `{scratchpad}/imagem-aula/{slug-da-aula}--{perfil}--r{n}.png`. A
rodada reprovada morre fora do repo. A cópia da peça aprovada para o acervo
acontece fora desta delegação, pelo Claude Code, depois da auditoria e conforme
a tabela de destinos do `SKILL.md`.

Modelo do pedido:

```
Tarefa: GERAR UM ARQUIVO PNG DE IMAGEM (não código, não descrição).

O prompt de imagem já está pronto e completo, em texto puro, neste arquivo:
{CAMINHO_DO_TXT}

Leia esse arquivo inteiro e use o conteúdo dele, sem alterar, como prompt de
geração de imagem.

Saída esperada: um PNG {PROPORCAO}, na maior resolução possível, salvo em:
{CAMINHO_DE_SAIDA}

Não leia, não altere e não grave nada dentro de aulas/ nesta tarefa.

Use a ferramenta nativa de imagem do Codex. Se ela não estiver disponível,
investigue alternativas no ambiente (API de imagens da OpenAI via credencial
local, servidor MCP de imagem, CLI instalado) e prefira o modelo mais capaz
a que a conta tiver acesso.

Regras:
- Não invente sucesso. Confirme com o tamanho em bytes e as dimensões reais
  (largura x altura) do PNG.
- Se NÃO for possível gerar imagem, diga isso de forma direta, listando os
  comandos rodados e os erros literais. Não entregue como substituto um SVG,
  um HTML, um script "que geraria" a imagem, nem uma descrição da imagem.

Relate: caminho do arquivo gerado, dimensões, e qual mecanismo/modelo foi usado.
```

Três cláusulas carregam peso e não devem ser cortadas:

- **"não código, não descrição"** e a proibição explícita de SVG/HTML/script.
  Sem isso, um agente de código tende a resolver "gerar imagem" escrevendo um
  gerador — tecnicamente engenhoso, inútil aqui.
- **"não invente sucesso" + dimensões em bytes e pixels.** Dá uma verificação
  barata antes de você abrir o arquivo.
- **proteção do acervo.** O pedido precisa conter literalmente a linha
  `Não leia, não altere e não grave nada dentro de aulas/ nesta tarefa.`. A
  versão v6 identifica o sistema de prompt, não a tentativa; por isso o nome
  usa `r{n}` no scratchpad e nunca um sufixo de versão no PNG.

## Depois que o PNG voltar

Auditar sempre, sem exceção — o relato do subagente cobre existência e medida,
não conteúdo. Abrir o PNG com `Read` e percorrer a tabela de defeitos do
`SKILL.md`. A conferência de proporção sai de graça com:

```bash
python .claude/skills/gerar-imagem-aula/scripts/inspecionar_png.py \
    infografico caminho/da/arte.png
```

Reprovou? Reforce no prompt exatamente a seção que falhou — não o prompt
inteiro — e chame o Codex de novo. Dá para continuar o mesmo subagente com
`SendMessage`, o que preserva o contexto da rodada anterior e sai mais barato
que abrir outro. O teto é de três rodadas, nomeadas `r1`, `r2` e `r3`. Na
terceira reprovação, pare e reporte ao Toni o defeito persistente pelo id e o
que mudou em cada tentativa; falha repetida no mesmo defeito costuma indicar
brief ambíguo, não gerador ruim.
