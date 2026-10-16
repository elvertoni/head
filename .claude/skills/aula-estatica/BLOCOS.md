# BLOCOS — snippets prontos (v3 · Volta Atelier)

Copie o bloco e troque só o conteúdo. Os nomes de classe são os mesmos do leitor de aulas do
ProfessorDash (`static/css/app.css`) sempre que o portal tem o componente — assim a apostila e o
site são a mesma peça vestida de dois jeitos. Nada de `style=""` inline, exceto dentro de `.demo-body`.

Sumário: 1 capa · 2 sumário · 3 seção · 4 divisor de parte · 5 fechamento · 6 callouts ·
7 código · 8 tabela · 9 passos · 10 exercícios · 11 checklist · 12 chips · 13 demo ·
14 figura · 15 citação · 16 roteiro do professor · 17 capa ilustrada · 18 gráfico SVG ·
19 resumo do tema

---

## 1 — Capa (`.lesson-header`)

```html
<header class="lesson-header" id="topo">
  <p class="eyebrow">Aula 03 · Programação Front-End</p>
  <ul class="chips">
    <li class="chip">Programação Front-End</li>
    <li class="chip chip--signal">2ª série</li>
  </ul>
  <h1>Formulários que <em>não recarregam</em></h1>
  <p class="dek">Uma a três frases que situam o aluno: o que ele vai conseguir fazer no fim.</p>
  <dl class="meta">
    <div><dt>Disciplina</dt><dd>Programação Front-End</dd></div>
    <div><dt>Série</dt><dd>2ª série</dd></div>
    <div><dt>Duração</dt><dd>50 minutos</dd></div>
    <div><dt>Entrega</dt><dd>1 atividade prática</dd></div>
  </dl>
</header>
```

- `<em>` no título = palavra-chave em `--signal` (vermelho). **Um só** por página, no conceito
  central da aula (nunca em "Aula", "Introdução", "Parte").
- `chip--signal` destaca **um** chip (trilha ou série). Os demais são `chip` simples.
- `meta` aceita de 2 a 5 itens.

## 2 — Sumário (`.toc`)

```html
<nav class="toc" id="sumario" aria-label="Sumário">
  <p class="eyebrow">Nesta aula</p>
  <ol class="toc-list">
    <li><a href="#sec-1"><span class="toc-num">01</span><span>O problema</span></a></li>
    <li><a href="#sec-2"><span class="toc-num">02</span><span>Passo a passo</span></a></li>
    <li><a href="#sec-3"><span class="toc-num">03</span><span>Fechamento</span></a></li>
  </ol>
</nav>
```

Cada `href="#sec-N"` precisa de uma `<section id="sec-N">`, na mesma ordem (o `build.py` confere).

## 3 — Seção

```html
<section class="section" id="sec-1">
  <header class="section-heading">
    <p class="eyebrow">Seção 01</p>
    <h2>O problema</h2>
  </header>

  <p>Texto corrido com <strong>destaque</strong> e <code>código inline</code>.</p>

  <h3>Subtópico</h3>
  <p>...</p>

  <h4>Detalhe dentro do subtópico</h4>
  <p>...</p>
</section>
```

Hierarquia: `h2` (título da seção, Archivo) → `h3` (subtópico, mono 700) → `h4` (detalhe).
Parágrafos, listas, `h3` e `h4` ficam presos na medida de leitura (`--measure`); tabelas e código
usam a largura toda — igual ao `.prose` do portal.

## 4 — Divisor de parte (só em material longo)

Quando uma seção tem partes grandes (as habilidades de uma apostila de revisão, os capítulos de
um módulo), abra cada parte com o divisor. Os subtópicos dentro dela descem para `h4`.

```html
<header class="part-head">
  <p class="eyebrow">HE-DSI-05</p>
  <h3>Comandos, operadores e tipos de dados</h3>
</header>
<h4>5.1 · O que é um algoritmo</h4>
```

## 5 — Fechamento (sempre a última seção)

```html
<section class="section section--close" id="sec-3">
  <header class="section-heading">
    <p class="eyebrow">Fechamento</p>
    <h2>O que levamos desta aula</h2>
  </header>
  <ul class="checklist">
    <li>Ponto principal 1.</li>
    <li>Ponto principal 2.</li>
    <li>Na próxima aula: <strong>tópico seguinte</strong>.</li>
  </ul>
  <p class="footer-note">Material produzido pelo Prof. Toni Coimbra · aulas.tonicoimbra.com</p>
</section>
```

## 6 — Callouts (anatomia do portal: `.ic` + `.ct` + rótulo `<b>`)

O ícone vem do CSS (máscara Lucide): a `<div class="ic">` fica **vazia**. O rótulo segue o padrão
do portal, **"Tipo · Título"** (só "Tipo" se não houver título). Sem listas dentro do callout:
quebre com `<p>` ou `<br>`.

```html
<aside class="callout conceito">
  <div class="ic" aria-hidden="true"></div>
  <div class="ct">
    <b>Conceito · Variável</b>
    <p>Um espaço na memória, com nome, que guarda um valor que pode mudar.</p>
  </div>
</aside>
```

| Classe | Cor | Ícone | Use para | Vem de (`:::tipo`) |
|---|---|---|---|---|
| `conceito` | info (azul-céu) | lâmpada | definição, ideia central | `conceito`, `definicao` |
| `atencao` | amber | triângulo | erro comum, cuidado (Sintoma / Solução) | `atencao`, `aviso`, `erro` |
| `dica` | emerald | brilho | atalho, boa prática | `dica` |
| `exemplo` | info / título neutro | livro | exemplo curto ilustrativo | `exemplo` |
| `importante` | amber / título neutro | estrela | destaque, desafio, conteúdo extra | `importante`, `desafio`, `extra` |
| `curiosidade` | neutro | bússola | contexto histórico, curiosidade | `curiosidade` |
| `objetivo` ¹ | emerald | alvo | objetivo, entrega, resultado esperado | `objetivo`, `entrega`, `resultado` |
| `erro` ¹ | signal (vermelho) | círculo-x | erro crítico (raro) | `erro-critico` |

¹ Extensões da apostila: o portal mostra objetivos num bloco próprio e não tem erro crítico.

Padrão do erro comum:

```html
<aside class="callout atencao">
  <div class="ic" aria-hidden="true"></div>
  <div class="ct">
    <b>Atenção · A página recarrega e some tudo</b>
    <p><strong>Sintoma:</strong> você clica em Salvar e a página pisca.<br>
    <strong>Solução:</strong> faltou o <code>preventDefault()</code>.</p>
  </div>
</aside>
```

## 7 — Código

```html
<pre data-lang="python"><code>def media(n1, n2):
    return (n1 + n2) / 2      # devolve um valor

if media(8, 6) &gt;= 7:
    print("aprovado")</code></pre>
```

- `data-lang` vira o rótulo do bloco; o botão **Copiar** é criado pelo JS sozinho.
- **Escape obrigatório**: dentro de `<pre><code>`, todo `<` vira `&lt;` e todo `>` vira `&gt;`.
- Destaque de sintaxe é **opcional**. Se usar, só estas classes: `tok-k` (palavra-chave/tag),
  `tok-a` (atributo/propriedade), `tok-s` (string), `tok-n` (número), `tok-c` (comentário).
  Na dúvida, não use: bloco sem destaque é melhor que bloco quebrado.
- Valores de `data-lang`: `html`, `css`, `javascript`, `python`, `java`, `sql`, `bash`, `json`,
  `portugol`, `txt`, `árvore`.

## 8 — Tabela

```html
<table>
  <caption>Tipos primitivos</caption>
  <thead>
    <tr><th>Tipo</th><th>Guarda</th><th>Exemplo</th></tr>
  </thead>
  <tbody>
    <tr><td>inteiro</td><td>números sem vírgula</td><td>idade</td></tr>
    <tr><td>real</td><td>números com vírgula</td><td>preço</td></tr>
  </tbody>
  <tfoot>
    <tr><td colspan="3">Observação curta que vale para a tabela toda.</td></tr>
  </tfoot>
</table>
```

`<caption>` é o rótulo da tabela (mono, caixa-alta). Tabela larga rola sozinha na horizontal.

## 9 — Passos (diagrama progressivo do portal)

```html
<ol class="lesson-steps">
  <li><span class="lesson-step-index">1</span><div><strong>Buscar</strong><p>A UC traz a instrução da memória.</p></div></li>
  <li><span class="lesson-step-index">2</span><div><strong>Decodificar</strong><p>A UC descobre o que a instrução pede.</p></div></li>
  <li><span class="lesson-step-index">3</span><div><strong>Executar</strong><p>A ULA faz a operação.</p></div></li>
</ol>
```

Mapeia `diagrama-progressivo`: cada camada vira um `<li>`, `rotulo` em `<strong>`, `conteudo` em `<p>`.
Para listas comuns numeradas, use `<ol>` simples.

## 10 — Exercícios / quiz (com gabarito comentado)

Um bloco `.lesson-quiz` reúne as questões de uma seção (ou do tema inteiro). Na tela, o aluno
clica numa alternativa, vê na hora se acertou e o gabarito comentado abre sozinho; no fim, aparece
o placar. Sem JavaScript ou no PDF, as alternativas viram lista e o gabarito sai aberto.

```html
<section class="lesson-quiz">
  <div class="lesson-quiz-head"><strong>Exercícios</strong><span>2 questões</span></div>
  <ol class="lesson-quiz-list">
    <li class="lesson-quiz-question" data-correct="b">
      <p><strong>Questão 1.</strong> Qual é o valor de <code>17 mod 5</code>?</p>
      <div class="quiz-options">
        <button type="button" class="quiz-option"><span class="quiz-option-letter">a</span><span class="quiz-option-text">3</span><span class="quiz-option-icon" aria-hidden="true"></span></button>
        <button type="button" class="quiz-option"><span class="quiz-option-letter">b</span><span class="quiz-option-text">2</span><span class="quiz-option-icon" aria-hidden="true"></span></button>
        <button type="button" class="quiz-option"><span class="quiz-option-letter">c</span><span class="quiz-option-text">3,4</span><span class="quiz-option-icon" aria-hidden="true"></span></button>
        <button type="button" class="quiz-option"><span class="quiz-option-letter">d</span><span class="quiz-option-text">0</span><span class="quiz-option-icon" aria-hidden="true"></span></button>
      </div>
      <p class="quiz-feedback" hidden></p>
      <details class="quiz-answer"><summary>Gabarito comentado</summary><p><strong>Resposta: b)</strong> 17 ÷ 5 dá quociente 3 e resto 2. <code>mod</code> devolve o resto. A alternativa a) é o <code>div</code>.</p></details>
    </li>
    <!-- próxima questão: outro <li class="lesson-quiz-question" data-correct="..."> -->
  </ol>
  <p class="quiz-result" hidden></p>
</section>
```

- `data-correct` = letra da correta (minúscula). Ela **não** aparece marcada nas alternativas.
- Dê `id="qN"` a cada questão quando houver um gabarito rápido: ele linka `<a href="#q12">12-c</a>`.
- O JS acrescenta sozinho o botão **Refazer** no cabeçalho do bloco e o `aria-live` do feedback.
- O comentário explica por que a correta está certa **e** por que as outras estão erradas.
- Código no enunciado: coloque o `<pre>` entre o `<p>` do enunciado e as `.quiz-options`.
- Questão aberta (sem alternativas): omita `data-correct`, `.quiz-options` e `.quiz-feedback`; deixe
  só o enunciado e o `<details class="quiz-answer">` com a resposta esperada.

Mapeia `:::questao` e o bloco ```` ```quiz ```` (uma pergunta por `<li>`; `correta: true` → `data-correct`).

## 11 — Checklist

```html
<ul class="checklist">
  <li>Item verificável com <strong>destaque</strong>.</li>
  <li>Outro item.</li>
</ul>
```

Check esmeralda (no Volta Atelier, verde = conclusão). Mapeia `:::resumo`.

**Checklist de estudo** (`class="checklist todo"`): caixas vazias que o aluno marca, salvas no
navegador. Use no fechamento quando a lista é "o que você precisa saber fazer"; o check já
preenchido do `.checklist` comum passa a ideia de que está tudo feito. Ponha um link para a seção
de cada item (`<strong><a href="#sec-3">Tema III</a>:</strong> ...`).

## 12 — Chips de vocabulário

```html
<ul class="chips">
  <li class="chip">&lt;form&gt;</li>
  <li class="chip">preventDefault()</li>
  <li class="chip">FormData</li>
</ul>
```

Mapeia `:::vocabulario`. Escape `<` e `>` de tags HTML.

No máximo **8 chips** juntos. Em material longo, coloque o vocabulário no **fim** do tema, antes
dos exercícios (`<h4>Vocabulário do tema</h4>` + uma frase), e não antes do primeiro parágrafo:
um muro de chips na abertura é ruído; no fim, vira revisão.

## 13 — Demonstração (HTML real renderizado)

```html
<div class="demo">
  <p class="demo-label">Renderizado no navegador</p>
  <div class="demo-body">
    <form onsubmit="event.preventDefault()">
      <label>Nome <input type="text"></label>
      <button type="submit">Enviar</button>
    </form>
  </div>
</div>
```

O `.demo-body` tem fundo branco e fonte de navegador padrão de propósito: mostra como o código do
aluno fica de verdade. É o único lugar onde `style=""` inline é aceito.

## 14 — Figura

```html
<figure class="lesson-figure">
  <div class="lesson-figure-frame"><img class="lesson-figure-img" src="img/ciclo-de-instrucao.png" alt="Descrição completa do que a imagem ensina"></div>
  <figcaption class="lesson-figure-caption">Legenda curta.</figcaption>
</figure>
```

O `src` é relativo: a pasta `img/` precisa ir junto do `.html`. O `alt` carrega a informação toda
(se a imagem faltar, o aluno ainda aprende).

## 15 — Citação

```html
<blockquote><p>Programas devem ser escritos para pessoas lerem.</p></blockquote>
```

## 16 — Roteiro do professor (some no PDF)

```html
<aside class="roteiro">
  <p class="roteiro-label">Roteiro do professor</p>
  <p>Instruções em imperativo: "Mostre no projetor...", "Reserve 10 minutos para...".</p>
</aside>
```

Sempre o **último bloco** da seção. Em material que vai só para o aluno (apostila de estudo, PDF
para a turma), **omita** — o aluno não precisa ler instruções dirigidas ao professor.

## 17 — Capa ilustrada (imagem de capa, perfil "capa" 3:2)

Logo depois do `</header>` da capa, antes do sumário. A imagem vem da skill
`gerar-imagem-aula` (perfil `capa`), salva em `img/capa.png` ao lado do `.html`.

```html
<figure class="lesson-cover">
  <img src="img/capa.png" alt="Descrição completa do que a capa mostra: título e os blocos com seus rótulos.">
</figure>
```

## 18 — Gráfico ou diagrama SVG (texto real, cores do tema)

Para tudo que tem **número, palavra exata ou dado**: gráfico estatístico, máscara de rede bit a
bit, pirâmide com valores, diagrama de conjuntos. Nunca peça isso ao gerador de imagem: ele erra
dígito e ortografia. SVG escrito à mão sai exato, leve, nítido em qualquer zoom e muda sozinho
entre claro e escuro, porque as cores vêm de **classes ligadas aos tokens**:

```html
<figure class="chart">
  <div class="chart-frame">
    <svg viewBox="0 0 760 240" role="img" aria-labelledby="g1-t">
      <title id="g1-t">Descrição completa para leitor de tela: o que o gráfico mostra e a conclusão.</title>
      <line x1="60" y1="172" x2="700" y2="172" class="k-line" stroke-width="2"/>
      <circle cx="140" cy="150" r="7" class="f-volt"/>
      <line x1="140" y1="64" x2="140" y2="164" class="k-emerald" stroke-width="2.5" stroke-dasharray="6 5"/>
      <text x="132" y="58" text-anchor="end" class="t t-emerald" font-weight="700">mediana = 5</text>
    </svg>
  </div>
  <figcaption>Legenda de uma linha com a conclusão.</figcaption>
</figure>
```

| Classe | Uso |
|---|---|
| `f-signal` `f-emerald` `f-amber` `f-volt` `f-info` | preenchimento sólido semântico |
| `f-tint-signal` … `f-tint-amber` | preenchimento tingido (fundo de barra/caixa) |
| `f-base` `f-panel` `f-none` | superfícies e sem preenchimento |
| `k-signal` `k-emerald` `k-amber` `k-volt` `k-info` `k-line` `k-fg` | contorno (`stroke`) |
| `t` `t-m` `t-l` `t-d` `t-on` | texto: normal, secundário, rótulo mono caixa-alta, display Archivo, branco sobre cor |
| `t-signal` `t-emerald` `t-amber` `t-volt` `t-info` | texto colorido com contraste AA nos dois temas |

Regras: `viewBox` com largura 760 (a moldura rola na horizontal no celular, mínimo 520 px);
fonte 13–17 px; `<title>` sempre; cor com o mesmo significado do resto da apostila (signal =
destaque/rede, esmeralda = certo/não volátil, âmbar = atenção/volátil, volt = dados neutros).

## 19 — Resumo do tema (ficha de revisão)

Em material longo (apostila de revisão), feche a explicação de cada tema com uma ficha, logo
antes dos exercícios. Uma linha por habilidade; o código leva de volta à explicação. Pontos
curtos, com o número, a regra ou a fórmula que cai na prova, sem conteúdo novo.

```html
<header class="part-head" id="resumo-tema-1">
  <p class="eyebrow">Resumo</p>
  <h3>O essencial do Tema I</h3>
</header>
<p>A ficha do tema, para revisar antes dos exercícios e na véspera da prova. Clique no código da habilidade para voltar à explicação.</p>
<dl class="resumo">
  <div class="resumo-item">
    <dt><a href="#he-dsi-02">HE-DSI-02</a><span>Sistemas de numeração</span></dt>
    <dd><ul>
      <li>Binário → decimal: some as potências onde há 1.</li>
      <li>Com n bits cabem 2<sup>n</sup> valores, de 0 a 2<sup>n</sup> − 1.</li>
    </ul></dd>
  </div>
</dl>
```

O `id` no `.part-head` põe o resumo na lista "Tópicos desta seção". No celular a ficha vira uma
coluna; no PDF cada linha não quebra entre páginas e continua no PDF sem respostas. Junto com os
resumos, a seção de abertura pode trazer um **roteiro de estudo**: tabela tema → sessões de
50 min → onde pôr atenção, e um callout `dica` com o plano para 3 semanas, 1 semana e véspera.
