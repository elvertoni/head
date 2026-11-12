---
name: aula-estatica
description: Transforma conteúdo de aula (canonica.md do acervo, markdown com sintaxe :::tipo do ProfessorDash, texto colado, descrição oral ou outra apostila) em UM arquivo HTML standalone no design system Caderno Noturno (DS v4) do ProfessorDash (aulas.tonicoimbra.com / prof.tonicoimbra.com) — monograma TC, Archivo + Geist + JetBrains Mono, tema claro/escuro à escolha do aluno, exercícios interativos com gabarito comentado, PDF A4 e fontes embutidas para abrir offline. Use SEMPRE que o Toni pedir "aplica a skill aula-estatica", "transforma essa aula em apostila HTML", "apostila para distribuir aos alunos", "versão estática da Aula NN", "aula em arquivo único", "salvar PDF da aula", "converte para o padrão tonicoimbra/ProfessorDash", "monta uma apostila de revisão", ou quando enviar um .md de aula sem outra instrução. Use também para ATUALIZAR apostilas antigas (v2 com logo C ciano e gradientes; v3 Volta Atelier com C vermelho) para o visual novo. Não é para publicar no portal (isso é o import do ProfessorDash).
---

# aula-estatica — apostila HTML no Caderno Noturno

Gera **um único `.html`** que abre com duplo clique, funciona offline, alterna claro/escuro,
tem exercícios clicáveis com gabarito comentado e imprime em A4 pelo botão "Salvar PDF".
O visual segue o leitor de aulas do ProfessorDash (Caderno Noturno, decisão #042): cabeçalho e
faixa da aula noturnos, folha clara para ler, e o aluno escolhe claro ou escuro.

## Arquivos

| Arquivo | Quando ler |
|---|---|
| `template.html` | **Sempre.** Ponto de partida obrigatório: CSS, JS e marca prontos. |
| `BLOCOS.md` | **Sempre**, antes de escrever o corpo. Snippets de cada componente. |
| `DESIGN_SYSTEM.md` | Quando o conteúdo pedir algo que os blocos não cobrem, ou para entender o porquê de uma regra. |
| `scripts/build.py` | No fim: embute as fontes e roda o checklist. |
| `scripts/migrar_v2.py` | Para converter apostila antiga (v2) para o template atual. |
| `exemplo-aula-01-formularios.html` | Referência de saída pronta (aula curta). |

## Fluxo

### 1. Entender a entrada
Pode vir de uma `canonica.md` do acervo (`aulas/{disciplina}/{trilha}/{NN-slug}/`), markdown
com `:::tipo`, texto solto, PDF ou uma apostila antiga. Se for **apostila v2** (tem
`class="apostila-shell"`, logo C ciano, gradientes), pule para "Migrar apostila antiga".

### 2. Copiar o `template.html` e preencher
Preencha **só** os marcadores `<!-- [EDIT...] -->` (e apague-os). Não reescreva CSS, JS ou SVG da
marca: é isso que garante que qualquer IA produza o mesmo visual. Ajuste pontual vai numa regra
nova no fim do `<style>`.

Estrutura: cabeçalho fixo → faixa da aula (`.lesson-header`, fora do `<main>`) → folha
(`<main class="shell">`: sumário `.toc` → seções `.section` com `id="sec-N"` → fechamento
`.section.section--close`) → rodapé.
Aula de 50 min: 4 a 8 seções. Material longo (apostila, módulo): pode passar disso, use o
**divisor de parte** (BLOCOS §4) e `<body data-print="capitulos">`. Apostila de revisão: feche
cada tema com o **resumo** (BLOCOS §19) e considere `data-layout="amplo"`.

### 3. Mapear o conteúdo nos componentes

| Na entrada | Componente (BLOCOS.md) |
|---|---|
| `:::conceito`, `:::definicao` | `callout conceito` |
| `:::atencao`, `:::aviso`, `:::erro` | `callout atencao` (com **Sintoma:** / **Solução:**) |
| `:::dica` | `callout dica` |
| `:::exemplo` | `callout exemplo` |
| `:::importante`, `:::desafio`, `:::extra` | `callout importante` |
| `:::curiosidade` | `callout curiosidade` |
| `:::objetivo`, `:::entrega`, `:::resultado` | `callout objetivo` |
| `:::erro-critico` | `callout erro` (raro) |
| `:::questao`, bloco ```` ```quiz ```` | `.lesson-quiz` (uma pergunta por `<li>`) |
| ```` ```diagrama-progressivo ```` | `figure.lesson-diagram` + `.lesson-steps` (`titulo` no `figcaption`) |
| `:::resumo` | `.checklist` no fechamento |
| `:::vocabulario` | `.chips` |
| `:::roteiro` | **omitir** (padrão). `.roteiro` só na versão do professor, pedida explicitamente (`build.py --professor`) |
| bloco de código | `<pre data-lang="..."><code>` |
| tabela | `<table>` com `<caption>` |
| HTML para mostrar renderizado | `.demo` |
| `![alt](img/x.png)` | `.lesson-figure` |
| gráfico de dados, cálculo, diagrama com números | `.chart` com SVG (BLOCOS §18), nunca imagem gerada |
| capa ilustrada | `.lesson-cover` dentro da faixa da aula (BLOCOS §17) |
| texto corrido / subtítulos | `<p>` / `<h3>` / `<h4>` |

O rótulo do callout segue o portal: **"Tipo · Título"** (ex.: `Atenção · Loop infinito`).

### 3b. Enriquecer com visuais (quando pedido)
Separe primeiro o **meio** de cada visual — é o que decide se ele ensina ou confunde:
- **ilustração conceitual** (arquitetura, fluxo, ciclo, comparação, capa) → skill
  `gerar-imagem-aula` (peça final sem marca, gerada pelo Codex e auditada); o PNG aprovado vai
  para `img/{slug}.png` ao lado do `.html` e entra como `.lesson-figure` ou `.lesson-cover`;
- **qualquer coisa com número ou palavra exata** (gráfico, tabela, sub-rede, estatística) →
  SVG escrito aqui (BLOCOS §18), com texto real e as classes de token.
Um visual por conceito difícil, ao lado do parágrafo que ele explica; o `alt`/`<title>` descreve
a informação inteira (sem a imagem, o aluno ainda aprende). O `build.py` embute tudo no arquivo
final, convertendo PNG para WebP.

### 4. Título da faixa
Título limpo, **sem `<em>`** (o v4 não destaca palavra, como o portal; o `build.py` acusa).
Preencha o numeral `.lesson-num` com o número da aula em dois dígitos, ou apague o parágrafo
se o material não for uma aula numerada.

### 5. Voz
A skill cuida do visual, não do tom. Preserve a voz do Toni: segunda pessoa ("você"),
analogias concretas, exemplos do dia a dia dos alunos, humor. Não "corporativize" o texto,
não corte exemplos, não acrescente disclaimers. Texto longo demais para uma seção vira duas
seções, nunca um corte.

### 6. Código
Dentro de `<pre><code>`, `<` vira `&lt;` e `>` vira `&gt;`, sempre. Destaque de sintaxe
(`tok-k/a/s/n/c`) é opcional; na dúvida, deixe sem.

### 7. Finalizar com o script
```bash
python scripts/build.py rascunho.html aula-NN-tema-curto.html
```
Ele troca o Google Fonts pelas fontes embutidas (Archivo, Geist e JetBrains Mono, SIL OFL;
offline de verdade), embute as imagens de `img/` (PNG → WebP com ffmpeg, quando houver) e roda o
checklist: um `<h1>` sem `<em>`, nenhum `[EDIT`, nenhum `.roteiro` (salvo com `--professor`), sumário ↔ seções, fechamento por último, código escapado, tipos de
callout válidos, `data-correct` existente nas alternativas, gabarito em toda questão, tags
balanceadas, nenhuma classe do v2, toda imagem com `alt` e arquivo existente. Corrija o que ele apontar e rode de novo.
Sem Python disponível, entregue o arquivo do template preenchido: ele funciona com as fontes
do Google Fonts (só precisa de internet na primeira abertura).

Nome do arquivo: kebab-case sem acento, `aula-NN-tema-curto.html`.

### 7b. Olhar o resultado
O checklist confere estrutura, não aparência. Onde houver o comando `chromium` (no WSL do Toni há;
é o Chromium headless do Playwright), tire duas capturas e um PDF e **olhe** antes de entregar:

```bash
chromium --headless=new --window-size=1366,2000 --screenshot=desktop.png file:///caminho/abs.html
chromium --headless=new --window-size=390,2000 --screenshot=celular.png file:///caminho/abs.html
chromium --headless=new --no-pdf-header-footer --print-to-pdf=apostila.pdf file:///caminho/abs.html
```

Para o tema escuro, capture uma cópia com `data-theme="dark"` no `<html>`. Sem navegador
disponível, diga ao Toni que o visual não foi conferido; não abra o Chrome do Windows por conta
própria (deixa processos e perfis temporários para trás).

### 8. Entregar
Salve em `saidas/` da pasta da aula (derivado, não versionado — decisão #001), ou onde o Toni
pedir. Saída nunca se edita: corrija a canônica e regere. Diga em poucas linhas: onde está, como usar
(duplo clique · botão Salvar PDF · pode hospedar em qualquer servidor estático) e o que foi
adaptado ou omitido (ex.: roteiro removido por ser material do aluno).

## Migrar apostila antiga (v2 → atual)

```bash
python scripts/migrar_v2.py antiga.html migrada.html [--capitulos]
python scripts/build.py migrada.html final.html
```
O conteúdo e a voz ficam intactos; muda só a roupa: callouts, código, tabelas, questões
(que viram quiz interativo), roteiros e chips. Roteiro migrado só passa no `build.py` com
`--professor`; para o aluno, apague os `.roteiro`. Apostila v3 (Volta Atelier) não tem
migrador: regere a partir da canônica. Confira o resultado no navegador, porque
estruturas fora do padrão v2 passam sem tradução e o `build.py` aponta o que sobrou.

## Uso com outras IAs (ChatGPT, Gemini, Codex...)
Entregue `template.html`, `BLOCOS.md` e `DESIGN_SYSTEM.md` como contexto e instrua:
"Preencha o template seguindo o BLOCOS.md; não reescreva CSS, JS nem o SVG da marca." O
`build.py` pode ser rodado depois por quem tiver Python.

## Regras que não mudam
1. Partir do `template.html`; não reconstruir o visual de memória.
2. Só componentes do `BLOCOS.md`; o que não tiver componente vira `<p>`.
3. Um `<h1>`, sem `<em>` de destaque.
4. Código escapado em `<pre><code>`.
5. Última seção com `section--close`, checklist e `.footer-note`.
6. Monograma TC exatamente como no template (T na cor do texto, C sempre amarelo).
7. Nada de degradê, glassmorphism ou barra lateral colorida; vermelho só para erro.
8. Comentário HTML nunca dentro de outro (o primeiro `-->` fecha tudo e o resto vaza para a página).
