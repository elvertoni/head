# Design System — Apostila Prof Toni Coimbra

Versão: **2.0** — Valores numéricos auditados contra o CSS real do `template.html`. Componente "Questão de fixação" adicionado. Exemplo antes/depois incluído.

Este documento é a **fonte da verdade** visual. Qualquer IA que siga este documento produz output idêntico ao padrão aprovado.

---

## 1. Identidade

- **Nome do sistema:** Apostila Prof Toni Coimbra
- **URL de referência:** aulas.tonicoimbra.com
- **Assinatura fixa no rodapé:** `Material produzido pelo Prof. Toni Coimbra · aulas.tonicoimbra.com`
- **Tema padrão ao abrir:** dark (`data-theme="dark"` no `<html>`)
- **Idioma:** `lang="pt-BR"`
- **Logo:** SVG inline de **duas cores fixas** — ciano `#00B4D8` (arco) e azul `#023E8A` (barra). Não sobrescrever via CSS.

---

## 2. Fontes

Carregadas via Google Fonts CDN. Este é o ÚNICO link externo permitido no arquivo standalone.

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Geist:wght@300;400;500;600;700;800&family=Geist+Mono:wght@400;500&display=swap" rel="stylesheet">
```

| Papel | Família | Pesos usados |
|---|---|---|
| Corpo / UI | `Geist` | 300, 400, 500, 600, 700, 800 |
| Código / Mono | `Geist Mono` | 400, 500 |
| Fallback | `ui-sans-serif, system-ui, -apple-system, sans-serif` | — |

### Escala tipográfica (valores reais do CSS)

| Elemento | Tamanho | Transformação |
|---|---|---|
| Hero title (h1) | `clamp(2.25rem, 4.4vw, 3.75rem)` | font-weight 700, line-height 1.02 |
| Hero lead | `1.02rem` | (sem clamp; tamanho fixo) |
| Section h2 | `clamp(1.5rem, 2.3vw, 1.9rem)` | font-weight 700, line-height 1.12 |
| h3 dentro de section | `1.08rem` | font-weight 600 |
| Corpo (p) | herda do body (≈1rem) | line-height 1.75 |
| Callout title | `0.95rem` | font-weight 700 (NÃO uppercase) |
| Callout text | herda | — |
| Code-shell `pre` | `0.88rem` | Geist Mono, line-height 1.7 |
| Section index | `0.72rem` | Geist Mono, uppercase, letter-spacing 0.16em |
| Eyebrow | `0.72rem` | uppercase, letter-spacing 0.18em |
| Sumário title | `0.7rem` | uppercase, letter-spacing 0.18em |
| Meta-card dt | `0.66rem` | uppercase, letter-spacing 0.16em |
| Meta-card dd | `0.95rem` | font-weight 600 |
| Roteiro chip | `0.7rem` | Geist Mono, uppercase, letter-spacing 0.14em |
| Code-lang | `0.72rem` | Geist Mono, uppercase, letter-spacing 0.12em |
| Demo-label | `0.7rem` | Geist Mono, uppercase, letter-spacing 0.14em |
| Tags li | `0.78rem` | Geist Mono |
| Footer note | `0.82rem` | — |

---

## 3. Paleta de cores

### Modo escuro (padrão — `data-theme="dark"`)

```css
--shell-bg:              #040405       /* fundo da página */
--shell-bg-2:            #09090b       /* fundo alternativo */
--shell-surface:         rgba(17,17,20,0.92)
--shell-surface-strong:  rgba(23,23,28,0.96)
--shell-surface-soft:    rgba(14,14,17,0.82)
--shell-surface-elev:    #111114
--shell-border:          rgba(255,255,255,0.08)
--shell-border-strong:   rgba(255,255,255,0.14)
--shell-text:            #ece8e7
--shell-text-muted:      #b0adb5
--shell-text-soft:       #84808c
--shell-primary:         #10b981       /* verde-esmeralda */
--shell-primary-200:     #6ee7b7
--shell-primary-100:     #d1fae5
--shell-secondary:       #8b5cf6       /* roxo */
--shell-secondary-200:   #c4b5fd
--shell-tertiary:        #06b6d4       /* ciano */
--shell-tertiary-200:    #67e8f9
--shell-danger:          #f87171
--shell-warning:         #fbbf24
```

### Modo claro (`data-theme="light"`)

```css
--shell-bg:              #f3f5f9
--shell-bg-2:            #e9ecf3
--shell-surface:         rgba(255,255,255,0.94)
--shell-surface-strong:  rgba(255,255,255,0.98)
--shell-surface-soft:    rgba(250,251,253,0.88)
--shell-surface-elev:    #ffffff
--shell-border:          rgba(15,23,42,0.08)
--shell-border-strong:   rgba(15,23,42,0.14)
--shell-text:            #0f172a
--shell-text-muted:      #475569
--shell-text-soft:       #64748b
/* accent colors permanecem iguais nos dois temas */
```

### Cores do logo (fixas no SVG, não usam variáveis)

| Cor | Hex | Onde |
|---|---|---|
| Ciano marca | `#00B4D8` | arco (path 1) |
| Azul marca | `#023E8A` | barra horizontal (path 2) |

### Accent gradient (`.accent`)

Palavra-chave do título com gradiente animado roxo → ciano:

```css
.accent {
  background: linear-gradient(120deg, var(--shell-secondary) 0%, var(--shell-tertiary) 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}
```

---

## 4. Layout

```
--max-width: 980px        /* container central */
.topbar-inner: calc(var(--max-width) + 80px)  /* topbar mais largo */
--content-gap: 28px       /* espaçamento entre hero/sumário/section */
padding horizontal shell: 20px (mobile: 14px)
breakpoint mobile: 720px
```

A estrutura raiz é `<body class="apostila-shell">` com `<main class="shell">` como container central.

---

## 5. Componentes

### 5.1 Topbar

Barra fixa no topo (`position: sticky; top: 0`). Contém logo + nome, botão de sumário, toggle de tema e botão PDF.

```html
<header class="topbar">
  <div class="topbar-inner">
    <a class="brand" href="#">
      <span class="brand-mark" aria-hidden="true">
        <!-- SVG do logo oficial inline (duas cores fixas) -->
      </span>
      <span class="brand-text">
        <strong>Prof Toni Coimbra</strong>
        <small>Apostila · [DISCIPLINA]</small>
      </span>
    </a>
    <nav class="toolbar">
      <a class="pill" href="#sumario">Sumário</a>
      <button class="btn btn-secondary" id="theme-toggle" type="button">...</button>
      <button class="btn btn-primary" onclick="window.print()" type="button">Salvar PDF</button>
    </nav>
  </div>
</header>
```

`.btn-primary` é gradient verde→ciano. `.btn-secondary` é superfície com borda.

---

### 5.2 Hero

Seção de capa da aula. Sempre o primeiro filho de `<main class="shell">`.

```html
<section class="hero">
  <div class="hero-gradient" aria-hidden="true"></div>
  <div class="hero-inner">
    <div class="eyebrow">
      <span class="eyebrow-line"></span>
      Aula 01 · Tema curto
    </div>
    <h1 class="hero-title">
      Título com <span class="accent">palavra-chave</span> em destaque
    </h1>
    <p class="hero-lead">Parágrafo de abertura em 1–3 frases.</p>
    <dl class="meta-grid">
      <div class="meta-card"><dt>Disciplina</dt><dd>Programação Web</dd></div>
      <div class="meta-card"><dt>Nível</dt><dd>Ensino Técnico</dd></div>
      <div class="meta-card"><dt>Duração</dt><dd>50 minutos</dd></div>
      <div class="meta-card"><dt>Entrega</dt><dd>1 atividade prática</dd></div>
    </dl>
  </div>
</section>
```

`.hero-gradient`: radial verde-esmeralda no canto superior direito + roxo no inferior esquerdo.
`.eyebrow-line`: linha horizontal verde antes do texto.
`.meta-grid`: grid `repeat(auto-fit, minmax(160px,1fr))`.

---

### 5.3 Sumário

```html
<nav class="sumario" id="sumario" aria-label="Sumário da aula">
  <p class="sumario-title">Nesta aula</p>
  <ol class="sumario-list">
    <li><a href="#sec-1"><span class="sumario-num">01</span><span>Título</span></a></li>
    <!-- 4–8 itens total -->
  </ol>
</nav>
```

`.sumario-num`: Geist Mono `0.78rem`, cor `var(--shell-text-soft)`.

---

### 5.4 Section

```html
<section class="section" id="sec-N">
  <header class="section-head">
    <span class="section-index">Seção 0N</span>
    <h2>Título da seção</h2>
  </header>
  <!-- conteúdo: p, h3, callouts, code-shell, demo-wrap, checklist, roteiro -->
</section>
```

**Última section:** adicionar classe `section-close` — aplica gradient verde sutil.

```html
<section class="section section-close" id="sec-N">
```

---

### 5.5 Callouts (5 variantes)

Estrutura comum:

```html
<aside class="callout [VARIANTE]">
  <div class="callout-mark" aria-hidden="true">[MARK]</div>
  <div class="callout-body">
    <p class="callout-title">Título curto</p>
    <p class="callout-text">Texto. Pode ter <code>inline</code> e <strong>negrito</strong>.</p>
  </div>
</aside>
```

| Classe | Cor | Mark default | Uso |
|---|---|---|---|
| `c-primary` | verde | `✓` | Objetivos, entregas, definições positivas, checkpoint OK |
| `c-secondary` | roxo | `+` | Desafios, destaques, conteúdo extra |
| `c-tertiary` | ciano | `i` | Conceitos, dicas, informações neutras, exemplos, curiosidades |
| `c-warning` | amarelo | `!` | Erros comuns, alertas, cuidados |
| `c-error` | vermelho | `✗` | Erros críticos (use com parcimônia) |

`.callout-title`: `0.95rem`, font-weight 700, **NÃO uppercase**, cor da variante.
`.callout-mark`: quadrado `36×36px`, radius 10px, cor da variante, Geist Mono 700.
Não usar `<ul>`/`<ol>` dentro do callout — use `<br>` para quebras.

---

### 5.6 Code-shell

```html
<div class="code-shell">
  <header class="code-top">
    <span class="dot dot-red"></span>
    <span class="dot dot-yellow"></span>
    <span class="dot dot-green"></span>
    <span class="code-lang">html</span>
  </header>
<pre><code><!-- conteúdo escapado: &lt; &gt; --></code></pre>
</div>
```

Dots: vermelho `#f87171`, amarelo `#fbbf24`, verde `#10b981`, todos a `~0.7` de opacidade.
Fundo: `#0b0b0e`. Fonte: Geist Mono `0.88rem`, line-height `1.7`.

**Valores aceitos para `.code-lang`:** `html`, `css`, `javascript`, `bash`, `sql`, `json`, `txt`, `árvore`, `python`

#### Syntax highlighting manual (opcional)

| Classe | Cor | Para |
|---|---|---|
| `.tag` | `#c4b5fd` (roxo claro) | Tags HTML (`&lt;form&gt;`), keywords JS (`const`, `function`, `new`) |
| `.attr` | `#67e8f9` (ciano) | Atributos HTML, propriedades CSS |
| `.str` | `#6ee7b7` (verde menta) | Strings entre aspas, template strings |
| `.com` | cinza | Comentários |
| `.prop` | `#67e8f9` (ciano) | Propriedades CSS (`width:`, `color:`) |
| `.num` | `#fbbf24` (amarelo) | Números, unidades, valores |

**Fallback aceito:** se houver qualquer dúvida sobre escape ou aplicação dos `<span>`, omita os spans e mantenha apenas o escape `<` → `&lt;` e `>` → `&gt;`. Um code-shell sem highlight renderiza com cor neutra mas íntegro — melhor que um quebrado.

---

### 5.7 Demo-wrap

Área que renderiza HTML de verdade (não como código).

```html
<div class="demo-wrap">
  <div class="demo-label">Renderizado no navegador</div>
  <div class="demo-body">
    <form onsubmit="event.preventDefault()">...</form>
  </div>
</div>
```

#### Tabela demo (dentro de `.demo-body`)

```html
<table class="demo">
  <thead><tr><th>Col 1</th><th>Col 2</th></tr></thead>
  <tbody><tr><td>A</td><td>B</td></tr></tbody>
  <tfoot><tr><td colspan="2">Rodapé</td></tr></tfoot>
</table>
```

Zebra automática. `<thead>` roxo translúcido. `<tfoot>` verde translúcido.

---

### 5.8 Roteiro do professor

```html
<aside class="roteiro">
  <header class="roteiro-head">
    <span class="roteiro-chip">Roteiro do professor</span>
  </header>
  <p>Texto em primeira pessoa, imperativo direto.</p>
</aside>
```

Borda tracejada ciano, fundo ciano translúcido. **Oculto na impressão** (`@media print { display: none }`).

---

### 5.9 Checklist

```html
<ul class="checklist">
  <li>Item com <strong>negrito</strong> e <code>código inline</code>.</li>
</ul>
```

Ícone `✓` verde antes de cada item. Uso típico: checkpoint de verificação e fechamento da aula.

---

### 5.10 Tags (pílulas de vocabulário)

```html
<ul class="tags">
  <li>&lt;table&gt;</li>
  <li>fetch()</li>
</ul>
```

Pílulas Geist Mono `0.78rem`, fundo `var(--shell-surface)`, borda. Use no início de uma seção para enumerar termos.

---

### 5.11 Footer note

```html
<p class="footer-note">
  Material produzido pelo Prof. Toni Coimbra · <span class="mono">aulas.tonicoimbra.com</span>
</p>
```

`0.82rem`, cor suave, dentro de `.section-close`.

---

### 5.12 Page footer

```html
<footer class="page-foot">
  <div class="page-foot-inner">
    <span>© <span id="year"></span> Prof Toni Coimbra</span>
    <span class="dotsep">·</span>
    <span>Apostila estática</span>
    <span class="dotsep">·</span>
    <a href="https://aulas.tonicoimbra.com" target="_blank" rel="noopener">aulas.tonicoimbra.com</a>
  </div>
</footer>
```

`<span id="year">` é preenchido automaticamente pelo JS.

---

### 5.13 Questão de fixação (NOVO)

Componente para `:::questao` do ProfessorDash. Multi-componente: enunciado, alternativas com correta marcada, e callout de resposta comentada.

```html
<h3>Questão de fixação</h3>
<p>Antes de responder, considere o trecho abaixo:</p>

<!-- (opcional) code-shell com o trecho da questão -->

<p>O usuário clica em Salvar. <strong>O que acontece, na ordem real?</strong></p>
<ol type="a">
  <li>Alternativa A.</li>
  <li>Alternativa B. <strong>(correta)</strong></li>
  <li>Alternativa C.</li>
  <li>Alternativa D.</li>
</ol>

<aside class="callout c-tertiary">
  <div class="callout-mark" aria-hidden="true">i</div>
  <div class="callout-body">
    <p class="callout-title">Resposta comentada</p>
    <p class="callout-text">Explicação do raciocínio que leva à alternativa correta, e por que as outras estão erradas.</p>
  </div>
</aside>
```

Convenções:
- Use `<ol type="a">` para alternativas (geram a, b, c, d automaticamente)
- Marque a correta com `<strong>(correta)</strong>` no final do `<li>`
- A explicação vai em `c-tertiary` com mark `i`
- Se houver código relacionado à questão, insira o `.code-shell` entre o enunciado e as alternativas

---

## 6. Comportamentos JavaScript

O `<script>` do template implementa três comportamentos. **Não reescreva — use o JS do template.**

### Toggle de tema
- Botão `id="theme-toggle"` alterna `data-theme="dark"`/`light"` no `<html>`
- Label `id="theme-label"` alterna "Tema claro" / "Tema escuro"
- Persiste em `localStorage` com chave `apostila-theme`
- Carrega preferência salva ao iniciar

### Ano dinâmico
Preenche `id="year"` com `new Date().getFullYear()`

### Botão PDF
`onclick="window.print()"` no botão `.btn-primary` — abre o diálogo de impressão

---

## 7. Impressão e PDF (A4)

```css
@media print {
  .topbar, .roteiro { display: none; }   /* oculta topbar e roteiro */
  .hero-gradient    { display: none; }
  body              { background: white; color: black; }
  .section          { break-inside: avoid; }
  .code-shell       { break-inside: avoid; border: 1px solid #ccc; }
  a[href]::after    { content: none; }   /* não mostra URLs */
}
```

@page A4 com margem 14mm. Cores convertidas para o esquema claro.

---

## 8. Breakpoint móvel (720px)

```css
@media (max-width: 720px) {
  .topbar-inner { padding: 10px 16px; min-height: 60px; }
  .shell        { padding: 22px 14px 52px; }
  .hero-inner   { padding: 28px 22px 26px; }
  .section      { padding: 24px 20px; }
  .hero-title   { font-size: clamp(1.9rem, 7vw, 2.5rem); }
  .brand-text small { display: none; }
}
```

---

## 9. Mapeamento de conteúdo → componentes

### Tabela A — ProfessorDash → Componente (markdown com `:::tipo`)

Ver `SKILL.md` seção "Passo 3" — tabela completa.

### Tabela B — Tipo de conteúdo → Componente (markdown comum)

| Tipo de conteúdo | Componente |
|---|---|
| Objetivo/entrega da aula | `callout c-primary` mark `✓` |
| Conceito teórico/definição | `callout c-tertiary` mark `i` |
| Dica prática | `callout c-tertiary` mark `i` |
| Erro comum / atenção | `callout c-warning` mark `!` |
| Desafio / extra | `callout c-secondary` mark `+` ou `★` |
| Erro crítico (raro) | `callout c-error` mark `✗` |
| Resumo / fechamento | `checklist` dentro de `section-close` |
| Roteiro do professor | `.roteiro` (oculto na impressão) |
| Vocabulário da aula | `.tags` (lista de pílulas) |
| Exemplo de UI | `.demo-wrap` com HTML real dentro |
| Código para digitar | `.code-shell` com syntax highlight manual |
| Tabela de dados | `table.demo` dentro de `.demo-wrap` |
| Checklist de verificação | `.checklist` |
| Questão de múltipla escolha | Componente "Questão de fixação" (§5.13) |
| Texto comum | `<p>` direto na section |
| Sub-tópico | `<h3>` |

---

## 10. O que NÃO fazer

- ❌ Criar componentes novos não documentados aqui
- ❌ Adicionar classes de frameworks externos (Bootstrap, Tailwind, etc.)
- ❌ Usar `<h1>` fora do `.hero-title`
- ❌ Colocar dois `<span class="accent">` na mesma página
- ❌ Usar `<ul>/<ol>` dentro de callouts (use `<br>` para quebras)
- ❌ Deixar `<` ou `>` literais dentro de `<pre><code>`
- ❌ Linkar `.css` ou `.js` como arquivo externo no standalone
- ❌ Omitir o `.roteiro` quando houver orientação ao professor
- ❌ Criar mais de 8 sections (deixa o sumário enorme)
- ❌ Usar imagens externas obrigatórias (demos devem ser HTML puro)
- ❌ Sobrescrever as cores fixas do SVG do logo via CSS
- ❌ Polir a voz do autor para um tom corporativo neutro
- ❌ Deixar dois `</main>` no arquivo (bug histórico do template — confira)

---

## 11. Exemplo antes/depois (calibração)

Esta seção serve de calibração rápida para qualquer LLM. Mostra um trecho de markdown de origem e o HTML resultante exato.

### Markdown de entrada

```markdown
## A analogia do garçom

Imagina que você está num restaurante e pede um suco. O garçom anota e sai correndo. Resultado: chega doce, e agora é tarde.

:::conceito O ciclo padrão de um formulário
Sem JavaScript interceptando, o navegador empacota os campos, dispara uma requisição HTTP e recarrega a página inteira. Tudo se perde no caminho.
:::

A função `preventDefault()` é você segurando o braço do garçom.

:::atencao A página recarrega e some tudo
Sintoma: você clica em Salvar e a página pisca. Solução: esqueceu o preventDefault, ou ele está depois de um erro de sintaxe.
:::
```

### HTML de saída

```html
<section class="section" id="sec-2">
  <header class="section-head">
    <span class="section-index">Seção 02</span>
    <h2>A analogia do garçom</h2>
  </header>

  <p>Imagina que você está num restaurante e pede um suco. O garçom anota e sai correndo. Resultado: chega doce, e agora é tarde.</p>

  <aside class="callout c-tertiary">
    <div class="callout-mark" aria-hidden="true">i</div>
    <div class="callout-body">
      <p class="callout-title">O ciclo padrão de um formulário</p>
      <p class="callout-text">Sem JavaScript interceptando, o navegador empacota os campos, dispara uma requisição HTTP e recarrega a página inteira. Tudo se perde no caminho.</p>
    </div>
  </aside>

  <p>A função <code>preventDefault()</code> é você segurando o braço do garçom.</p>

  <aside class="callout c-warning">
    <div class="callout-mark" aria-hidden="true">!</div>
    <div class="callout-body">
      <p class="callout-title">A página recarrega e some tudo</p>
      <p class="callout-text"><strong>Sintoma:</strong> você clica em Salvar e a página pisca.<br><strong>Solução:</strong> esqueceu o <code>preventDefault</code>, ou ele está depois de um erro de sintaxe.</p>
    </div>
  </aside>
</section>
```

Observações sobre o mapeamento:

1. O `##` virou `<h2>` dentro de `.section-head` com `<span class="section-index">` precedendo
2. Parágrafos comuns viraram `<p>` direto na section
3. `:::conceito` virou `callout c-tertiary` com mark `i`
4. `:::atencao` virou `callout c-warning` com mark `!`
5. Os marcadores `**Sintoma:**` e `**Solução:**` viraram `<strong>` com `<br>` separando
6. Trechos `código entre crases` viraram `<code>inline</code>`
7. O título do callout veio do que segue `:::tipo` na mesma linha
8. Voz preservada: "Imagina que você está", "agora é tarde", "esqueceu o preventDefault" — sem normalizar
