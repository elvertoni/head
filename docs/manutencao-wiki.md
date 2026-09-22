# Manutenção da wiki de conceitos

Este procedimento aplica o padrão LLM Wiki ao acervo PROF-TONI. O `lake/` guarda
fontes brutas e imutáveis; `conceitos/` é a wiki persistente; `aulas/` consome
conceitos em páginas canônicas; `saidas/` contém derivados regeneráveis.

Snapshot operacional de 2026-09-21: `manifesto.json` valida 89 aulas aprovadas e
o grafo contém cerca de 1.042 conceitos ativos. Os rótulos de disciplinas e
trilhas são mantidos em `tools/gerar_manifesto.py`.

## Camadas e proveniência

- `lake/`: fonte bruta, como notas, transcrições, PDFs e materiais estudados;
  o agente lê e não edita essa camada.
- `lake/**/graphify-out/`: cache derivado de extração. Pode apoiar recuperação e
  auditoria local, mas cache não substitui a fonte bruta ausente, nem deve ser
  tratado como nova fonte de autoria.
- `conceitos/`, `aulas/`, `tools/` e `docs/`: conteúdo sintetizado e regras
  operacionais versionados no Git.

Quando uma fonte não está disponível, registre a lacuna mesmo que exista cache
derivado. A proveniência continua pendente até a fonte original ser recuperada
ou uma URL de origem ser registrada.

## Ingestão

1. Leia a fonte em `lake/` sem editá-la.
2. Procure conceitos existentes por `slug` e `aka` antes de criar páginas.
3. Atualize a síntese, os wikilinks, `## Onde aparece`, `index.md` e acrescente
   uma entrada em `conceitos/log.md`.
4. Deixe novos conceitos como `status: rascunho` até haver revisão humana e
   proveniência conferível. Fonte ausente nesta máquina é uma pendência de
   acesso; não crie uma fonte substituta.

## Regra de escopo: ingestão não é aula

Ingerir material significa incorporá-lo ao segundo cérebro com rastreabilidade;
isso **não cria uma aula automaticamente**. Notas, transcrições, cursos e outros
materiais estudados podem permanecer como transcrição, anotação, resumo ou fonte
bruta no `lake/`, atualizar um conceito existente, ou gerar um conceito/síntese
em rascunho.

`aulas: []` é válido e esperado quando o conceito ainda não foi usado numa aula.
Só crie ou edite `aulas/**/canonica.md` quando houver uma decisão pedagógica
explícita: objetivo, público, sequência e revisão da aula. Nesse caso, aplique o
contrato do manifesto, incremente `versao`/`atualizado_em` e regenere o manifesto.
Nenhum PDF, curso, transcrição ou nota entra no portal por ser apenas ingerido.

Uma fonte também pode não gerar página alguma: se for repetida, contextual ou
sem valor durável, ela continua disponível como material de estudo no `lake/`.

## Consulta

Busque primeiro em `conceitos/index.md` e depois leia as páginas relevantes.
Responda com `[[slug]]`, fontes e limitações. Promova a `tipo: sintese` quando a
resposta tiver valor durável e realmente for salva; só então registre no diário:

```text
## [AAAA-MM-DD] query | pergunta → [[slug-da-sintese]]; fontes verificadas; limitações registradas
```

Uma resposta transitória não deve ser registrada como página publicada.

## Auditoria

```powershell
python tools/lint_wiki.py
python tools/lint_wiki.py --format json
python tools/lint_wiki.py --fail-on error
python tools/gerar_indice.py --check
python tools/gerar_manifesto.py --check
python -m unittest discover -s tests -v
```

`lint_wiki.py` é somente leitura. Ele verifica frontmatter, anatomia, slugs,
aliases, links mortos, stubs catalogados, órfãos, aulas sem conceitos,
backlinks em ambas as direções e proveniência. Também aponta `stale` quando a
data de modificação local de uma fonte `lake/` é posterior a `atualizado_em` do
conceito. O `mtime` é uma aproximação: uma cópia ou sincronização pode mudar a
data do arquivo sem mudar seu conteúdo, então confira a fonte antes de editar o
conceito. Referências `lake/` inexistentes são relatadas como indisponíveis
localmente; URLs não são acessadas pelo lint. `--format json` produz diagnósticos
estáveis para automação. O código de saída é `1` quando há achados na severidade
escolhida e `2` quando a ferramenta não consegue executar.

Para fechar um backlink, `## Onde aparece` deve registrar o caminho exato da
canônica aprovada entre crases (`aulas/{disciplina}/{trilha}/{NN-slug}/canonica.md`).
`aulas: [ordem]` permanece por compatibilidade, mas não identifica a aula sozinho
quando a ordem se repete — e o lint também sinaliza a ausência do caminho quando
a ordem é única.

## Índice e manifesto

`gerar_indice.py --write` reorganiza o catálogo por disciplina, preserva os
resumos existentes por slug e mantém stubs explícitos na seção de pendências.
Não edite o índice manualmente depois da geração sem registrar a decisão.

`gerar_manifesto.py --check` valida as aulas e compara o manifesto persistido
com o estado atual, ignorando somente a data global de geração. Depois de editar
uma aula aprovada, incremente `versao` ou `atualizado_em` e regenere o manifesto.

O lint propõe correções; promoção de rascunhos, fusão de conceitos, resolução
de contradições, recuperação de fontes e alteração de slugs continuam decisões
editoriais humanas.
