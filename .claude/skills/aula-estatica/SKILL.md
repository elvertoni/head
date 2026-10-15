---
name: aula-estatica
description: Transforma conteúdo de aula (canonica.md do acervo, markdown com sintaxe :::tipo do ProfessorDash, texto colado, descrição oral ou outra apostila) em UM arquivo HTML standalone no design system Volta Atelier do ProfessorDash (aulas.tonicoimbra.com / prof.tonicoimbra.com) — marca TC, Archivo + JetBrains Mono, tema claro/escuro, exercícios interativos com gabarito comentado, PDF A4 e fontes embutidas para abrir offline. Use SEMPRE que o Toni pedir "aplica a skill aula-estatica", "transforma essa aula em apostila HTML", "apostila para distribuir aos alunos", "versão estática da Aula NN", "aula em arquivo único", "salvar PDF da aula", "converte para o padrão tonicoimbra/ProfessorDash", "monta uma apostila de revisão", ou quando enviar um .md de aula sem outra instrução. Use também para ATUALIZAR apostilas antigas (logo C ciano, gradientes, Geist) para o visual novo. Não é para publicar no portal (isso é o import do ProfessorDash).
---

# aula-estatica — apostila HTML no Volta Atelier

Gera **um único `.html`** que abre com duplo clique, funciona offline, alterna claro/escuro,
tem exercícios clicáveis com gabarito comentado e imprime em A4 pelo botão "Salvar PDF".
O visual é o mesmo do leitor de aulas do ProfessorDash: a apostila e o portal são a mesma
aula vestida de dois jeitos.

## Arquivos

| Arquivo | Quando ler |
|---|---|
| `template.html` | **Sempre.** Ponto de partida obrigatório: CSS, JS e marca prontos. |
| `BLOCOS.md` | **Sempre**, antes de escrever o corpo. Snippets de cada componente. |
| `DESIGN_SYSTEM.md` | Quando o conteúdo pedir algo que os blocos não cobrem, ou para entender o porquê de uma regra. |
| `scripts/build.py` | No fim: embute as fontes e roda o checklist. |
| `scripts/migrar_v2.py` | Para converter apostila antiga (v2) para o v3. |
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

Estrutura: cabeçalho fixo → capa (`.lesson-header`) → sumário (`.toc`) → seções
(`.section` com `id="sec-N"`) → fechamento (`.section.section--close`) → rodapé.
Aula de 50 min: 4 a 8 seções. Material longo (apostila, módulo): pode passar disso, use o
**divisor de parte** (BLOCOS §4) e `<body data-print="capitulos">`.

### 3. Mapear o conteúdo nos componentes

| Na entrada | Componente v3 (BLOCOS.md) |
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
| ```` ```diagrama-progressivo ```` | `.lesson-steps` |
| `:::resumo` | `.checklist` no fechamento |
| `:::vocabulario` | `.chips` |
| `:::roteiro` | `.roteiro` (último bloco da seção; **omita** em material só do aluno) |
| bloco de código | `<pre data-lang="..."><code>` |
| tabela | `<table>` com `<caption>` |
| HTML para mostrar renderizado | `.demo` |
| `![alt](img/x.png)` | `.lesson-figure` |
| gráfico de dados, cálculo, diagrama com números | `.chart` com SVG (BLOCOS §18), nunca imagem gerada |
| capa ilustrada | `.lesson-cover` (BLOCOS §17) |
| texto corrido / subtítulos | `<p>` / `<h3>` / `<h4>` |

O rótulo do callout segue o portal: **"Tipo · Título"** (ex.: `Atenção · Loop infinito`).

### 3b. Enriquecer com visuais (quando pedido)
Separe primeiro o **meio** de cada visual — é o que decide se ele ensina ou confunde:
- **ilustração conceitual** (arquitetura, fluxo, ciclo, comparação, capa) → skill
  `gerar-imagem-aula` (prompt v7 Volta Atelier, gerado pelo Codex e auditado); o PNG aprovado vai
  para `img/{slug}.png` ao lado do `.html` e entra como `.lesson-figure` ou `.lesson-cover`;
- **qualquer coisa com número ou palavra exata** (gráfico, tabela, sub-rede, estatística) →
  SVG escrito aqui (BLOCOS §18), com texto real e as classes de token.
Um visual por conceito difícil, ao lado do parágrafo que ele explica; o `alt`/`<title>` descreve
a informação inteira (sem a imagem, o aluno ainda aprende). O `build.py` embute tudo no arquivo
final, convertendo PNG para WebP.

### 4. Título da capa
Escolha **uma** palavra ou expressão curta do título para o `<em>` (fica em vermelho signal):
o conceito central da aula (`formulários`, `JOIN`, `polimorfismo`), nunca "Aula", "Parte",
"Introdução".

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
Ele troca o Google Fonts pelas fontes embutidas (offline de verdade), embute as imagens de
`img/` (PNG → WebP com ffmpeg, quando houver) e roda o checklist:
um `<h1>`, nenhum `[EDIT`, sumário ↔ seções, fechamento por último, código escapado, tipos de
callout válidos, `data-correct` existente nas alternativas, gabarito em toda questão, tags
balanceadas, nenhuma classe do v2, toda imagem com `alt` e arquivo existente. Corrija o que ele apontar e rode de novo.
Sem Python disponível, entregue o arquivo do template preenchido: ele funciona com as fontes
do Google Fonts (só precisa de internet na primeira abertura).

Nome do arquivo: kebab-case sem acento, `aula-NN-tema-curto.html`.

### 8. Entregar
Salve ao lado da canônica (ou onde o Toni pedir) e diga em poucas linhas: onde está, como usar
(duplo clique · botão Salvar PDF · pode hospedar em qualquer servidor estático) e o que foi
adaptado ou omitido (ex.: roteiro removido por ser material do aluno).

## Migrar apostila antiga (v2 → v3)

```bash
python scripts/migrar_v2.py antiga.html migrada.html [--capitulos]
python scripts/build.py migrada.html final.html
```
O conteúdo e a voz ficam intactos; muda só a roupa: callouts, código, tabelas, questões
(que viram quiz interativo), roteiros e chips. Confira o resultado no navegador, porque
estruturas fora do padrão v2 passam sem tradução e o `build.py` aponta o que sobrou.

## Uso com outras IAs (ChatGPT, Gemini, Codex...)
Entregue `template.html`, `BLOCOS.md` e `DESIGN_SYSTEM.md` como contexto e instrua:
"Preencha o template seguindo o BLOCOS.md; não reescreva CSS, JS nem o SVG da marca." O
`build.py` pode ser rodado depois por quem tiver Python.

## Regras que não mudam
1. Partir do `template.html`; não reconstruir o visual de memória.
2. Só componentes do `BLOCOS.md`; o que não tiver componente vira `<p>`.
3. Um `<h1>` e um `<em>` de destaque na capa.
4. Código escapado em `<pre><code>`.
5. Última seção com `section--close`, checklist e `.footer-note`.
6. Marca TC exatamente como no template.
7. Nada de degradê decorativo, glassmorphism ou barra lateral colorida.
8. Comentário HTML nunca dentro de outro (o primeiro `-->` fecha tudo e o resto vaza para a página).
